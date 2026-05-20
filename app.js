/* ============================================================
   app.js — 眼动追踪工具核心逻辑（真实摄像头版本）
   绝对不使用任何鼠标模拟 / 降级模式。
   WebGazer 初始化失败 → 显示错误弹窗，禁止继续操作。
============================================================ */

'use strict';

// ─── 状态 ──────────────────────────────────────────────────────
const State = {
  privacyAccepted: false,
  pendingCalibrationStart: false,
  webgazerReady: false,   // WebGazer + 摄像头完全就绪
  calibrationDone: false,
  isTracking: false,
  uploadedImageSrc: null,
  uploadedImages: [],
  selectedImageId: null,
  gazeHistory: [],        // {x, y, timestamp}[]
  trackingStartTime: null,
  trackingStartedAt: null,
  trackingImage: null,
  currentReportRun: null,
  calibrationSession: null,
  calibrationSessions: [],
  calibrationSessionSeq: 0,
  selectedSessionId: null,
  calibPoints: [],
  currentCalibIndex: 0,
};

// ─── DOM ────────────────────────────────────────────────────────
const $ = (id) => document.getElementById(id);
const EL = {
  // 弹窗
  privacyModal:    $('privacy-modal'),
  acceptPrivacy:   $('accept-privacy'),
  loadingOverlay:  $('loading-overlay'),
  loadingStatus:   $('loading-status'),
  errorModal:      $('error-modal'),
  errorMessage:    $('error-message'),
  errorDetail:     $('error-detail'),
  retryInitBtn:    $('retry-init-btn'),

  // 屏幕
  homeScreen:      $('home-screen'),
  calibScreen:     $('calibration-screen'),
  trackingScreen:  $('tracking-screen'),
  reportScreen:    $('report-screen'),

  // 校准
  calibPointsContainer: $('calibration-points-container'),
  calibProgressFill:    $('calib-progress-fill'),
  calibProgressPct:     $('calib-progress-pct'),
  calibStatusText:      $('calib-status-text'),
  gazeCursor:           $('gaze-cursor'),

  // 首页
  startCalibBtn:         $('start-calib-btn'),
  participantIdInput:    $('participant-id-input'),
  openDataBtn:           $('open-data-btn'),
  importArchiveHomeBtn:  $('import-archive-home-btn'),
  homeParticipantCount:  $('home-participant-count'),
  homeRunCount:          $('home-run-count'),
  startTrackBtn:         $('start-track-btn'),
  calibStatusIndicator:  $('calib-status-indicator'),
  calibStatusLabel:      $('calib-status-label'),
  trackStatusIndicator:  $('track-status-indicator'),
  dropzone:        $('dropzone'),
  dropzoneInner:   $('dropzone-inner'),
  fileInput:       $('file-input'),
  imageGallery:    $('image-gallery'),

  // 追踪
  trackingImage:        $('tracking-image'),
  gazeCursorTracking:   $('gaze-cursor-tracking'),
  stopTrackingBtn:      $('stop-tracking-btn'),

  // 报告
  statDuration:  $('stat-duration'),
  statPoints:    $('stat-points'),
  statQuality:   $('stat-quality'),
  statFps:       $('stat-fps'),
  reportCanvas:  $('report-canvas'),
  participantCount: $('participant-count'),
  participantList:  $('participant-list'),
  runCount:         $('run-count'),
  runList:          $('run-list'),
  selectedRunLabel: $('selected-run-label'),
  selectedRunNote:  $('selected-run-note'),
  tabHeatmap:    $('tab-heatmap'),
  tabGazeplot:   $('tab-gazeplot'),
  backHomeBtn:   $('back-home-btn'),
  importArchiveBtn:   $('import-archive-btn'),
  importArchiveInput: $('import-archive-input'),
  exportArchiveBtn:   $('export-archive-btn'),
  exportSelectedDataBtn: $('export-selected-data-btn'),
  exportDataBtn: $('export-data-btn'),
  exportPdfBtn:  $('export-pdf-btn'),
};

// ─── 校准点布局 ─────────────────────────────────────────────────
const CALIB_POSITIONS = [
  { x: 0.10, y: 0.10 }, { x: 0.50, y: 0.10 }, { x: 0.90, y: 0.10 },
  { x: 0.10, y: 0.50 }, { x: 0.50, y: 0.50 }, { x: 0.90, y: 0.50 },
  { x: 0.10, y: 0.90 }, { x: 0.50, y: 0.90 }, { x: 0.90, y: 0.90 },
];
const CLICKS_PER_POINT = 3;
const MAX_IMAGE_BYTES = 10 * 1024 * 1024;
const MAX_STORED_IMAGES = 5;
const CALIBRATION_KEYS = new Set([' ', 'Enter', '0']);

// ─── 显示/隐藏弹窗 ─────────────────────────────────────────────
function showModal(el)  { el.classList.add('active'); }
function hideModal(el)  { el.classList.remove('active'); }

// ─── 屏幕切换 ──────────────────────────────────────────────────
function showScreen(screenEl) {
  [EL.homeScreen, EL.calibScreen, EL.trackingScreen, EL.reportScreen]
    .forEach(el => el && el.classList.add('hidden'));
  if (screenEl) screenEl.classList.remove('hidden');
}

// ─── 错误显示 ──────────────────────────────────────────────────
function showError(msg, detail = '') {
  hideModal(EL.loadingOverlay);
  EL.errorMessage.textContent = msg;
  EL.errorDetail.textContent  = detail ? `错误详情：${detail}` : '';
  showModal(EL.errorModal);
}

function createCalibrationSession() {
  State.calibrationSessionSeq += 1;
  const now = new Date().toISOString();
  const enteredId = EL.participantIdInput.value.trim();
  const participantId = enteredId || `participant-${State.calibrationSessionSeq}`;
  const session = {
    id: participantId,
    label: participantId,
    calibratedAt: now,
    runs: [],
  };
  State.calibrationSession = session;
  State.selectedSessionId = session.id;
  State.calibrationSessions.push(session);
  updateHomeDataSummary();
}

function getSelectedImage() {
  return State.uploadedImages.find(item => item.id === State.selectedImageId) || null;
}

function getAllTrackingRuns() {
  return State.calibrationSessions.flatMap(session =>
    session.runs.map((run, index) => ({ session, run, trialIndex: index + 1 }))
  );
}

function updateHomeDataSummary() {
  EL.homeParticipantCount.textContent = State.calibrationSessions.length;
  EL.homeRunCount.textContent = getAllTrackingRuns().length;
}

function findRunRecord(targetRun = State.currentReportRun) {
  if (!targetRun) return null;
  return getAllTrackingRuns().find(record => record.run === targetRun || record.run.id === targetRun.id) || null;
}

function selectSession(sessionId) {
  const session = State.calibrationSessions.find(item => item.id === sessionId);
  if (!session) return;

  State.selectedSessionId = session.id;
  State.currentReportRun = session.runs[0] || null;
  if (State.currentReportRun) {
    State.uploadedImageSrc = State.currentReportRun.imageSrc;
    State.gazeHistory = State.currentReportRun.points;
  }
  renderDataWorkbench();
  updateReportFromCurrentRun();
}

function selectRun(sessionId, runId) {
  const session = State.calibrationSessions.find(item => item.id === sessionId);
  const run = session?.runs.find(item => item.id === runId);
  if (!session || !run) return;

  State.selectedSessionId = session.id;
  State.currentReportRun = run;
  State.uploadedImageSrc = run.imageSrc;
  State.gazeHistory = run.points;
  renderDataWorkbench();
  updateReportFromCurrentRun();
}

function showDataScreen(run = State.currentReportRun) {
  if (run) {
    const record = findRunRecord(run);
    if (record) {
      State.selectedSessionId = record.session.id;
      State.currentReportRun = record.run;
    }
  } else if (!State.selectedSessionId && State.calibrationSessions.length) {
    State.selectedSessionId = State.calibrationSessions[0].id;
    State.currentReportRun = State.calibrationSessions[0].runs[0] || null;
  }

  renderDataWorkbench();
  showScreen(EL.reportScreen);
  updateReportFromCurrentRun();
}

function renderDataWorkbench() {
  updateHomeDataSummary();
  EL.participantCount.textContent = State.calibrationSessions.length;
  EL.participantList.innerHTML = '';
  EL.runList.innerHTML = '';

  if (!State.calibrationSessions.length) {
    EL.participantList.innerHTML = '<p class="data-empty">还没有参与者数据。可先完成追踪，或导入参与者存档。</p>';
    EL.runList.innerHTML = '<p class="data-empty">请选择参与者。</p>';
    EL.runCount.textContent = '0';
    EL.selectedRunLabel.textContent = '未选择';
    EL.selectedRunNote.textContent = '导入存档或完成追踪后，可在这里选择并回顾单次数据。';
    return;
  }

  State.calibrationSessions.forEach(session => {
    const item = document.createElement('button');
    item.type = 'button';
    item.className = `data-item${session.id === State.selectedSessionId ? ' active' : ''}`;
    item.innerHTML = `
      <span class="data-item-title">${escapeHtml(session.label)}</span>
      <span class="data-item-meta">${session.runs.length} 次追踪 · ${formatDateTime(session.calibratedAt)}</span>
    `;
    item.addEventListener('click', () => selectSession(session.id));
    EL.participantList.appendChild(item);
  });

  const session = State.calibrationSessions.find(item => item.id === State.selectedSessionId) || State.calibrationSessions[0];
  State.selectedSessionId = session.id;
  EL.runCount.textContent = session.runs.length;

  if (!session.runs.length) {
    EL.runList.innerHTML = '<p class="data-empty">该参与者还没有完成任何图片追踪。</p>';
    EL.selectedRunLabel.textContent = session.label;
    EL.selectedRunNote.textContent = '完成一次图片追踪后，记录会出现在这里。';
    return;
  }

  session.runs.forEach((run, index) => {
    const item = document.createElement('button');
    item.type = 'button';
    item.className = `data-item${run === State.currentReportRun ? ' active' : ''}`;
    item.innerHTML = `
      <span class="data-item-title">${index + 1}. ${escapeHtml(run.image.name)}</span>
      <span class="data-item-meta">${run.points.length} 点 · ${run.duration.toFixed(1)} s · ${formatDateTime(run.startedAt)}</span>
    `;
    item.addEventListener('click', () => selectRun(session.id, run.id));
    EL.runList.appendChild(item);
  });

  const current = State.currentReportRun;
  if (current) {
    EL.selectedRunLabel.textContent = `${session.label} / ${current.image.name}`;
    EL.selectedRunNote.textContent = `${current.points.length} 个数据点，追踪 ${current.duration.toFixed(1)} 秒。`;
  }
}

function updateReportFromCurrentRun() {
  const run = State.currentReportRun;
  if (!run) {
    EL.statDuration.textContent = '0.0 s';
    EL.statPoints.textContent = '0';
    EL.statQuality.textContent = '—';
    EL.statQuality.style.color = '';
    EL.statFps.textContent = '— Hz';
    const ctx = EL.reportCanvas.getContext('2d');
    ctx.clearRect(0, 0, EL.reportCanvas.width, EL.reportCanvas.height);
    return;
  }
  updateReportStats(run);
  if (EL.tabHeatmap.classList.contains('active')) drawHeatmap();
  else drawGazePlot();
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, char => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
  }[char]));
}

function formatDateTime(value) {
  if (!value) return '未知时间';
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleString('zh-CN', { hour12: false });
}

function resetTrackingAvailability(text = '摄像头已关闭，请重新校准后开始追踪') {
  State.webgazerReady = false;
  State.calibrationDone = false;
  State.isTracking = false;

  EL.calibStatusIndicator.className = 'status-indicator status-pending';
  EL.calibStatusLabel.textContent = '未校准';
  EL.startCalibBtn.textContent = '启用摄像头并校准';
  EL.startTrackBtn.disabled = true;
  EL.startTrackBtn.className = 'btn btn-secondary';
  if (State.uploadedImageSrc) {
    setTrackStatus('status-pending', text);
  } else {
    setTrackStatus('status-pending', '请选择图像并重新校准');
  }
}

function stopCameraStream() {
  const video = document.getElementById('webgazerVideoFeed');
  if (video && video.srcObject) {
    video.srcObject.getTracks().forEach(track => track.stop());
  }
  try { webgazer.pause(); } catch (_) {}
  try { webgazer.end(); } catch (_) {}
  ['webgazerVideoFeed', 'webgazerVideoContainer',
   'webgazerFaceOverlay', 'webgazerFaceFeedbackBox', 'webgazerGazeDot']
    .forEach(id => document.getElementById(id)?.remove());
}

// ─── WebGazer 视频元素处理 ─────────────────────────────────────
// 必须保持 display:block（否则部分浏览器停止处理视频帧）
// 但通过 position:fixed + top/left:-9999px 移出屏幕
function hideWebGazerElements() {
  // 视频及容器
  ['webgazerVideoFeed', 'webgazerVideoContainer',
   'webgazerFaceOverlay', 'webgazerFaceFeedbackBox'].forEach(id => {
    const el = document.getElementById(id);
    if (!el) return;
    el.style.cssText = `
      display: block !important;
      position: fixed !important;
      top: -9999px !important;
      left: -9999px !important;
      width: 1px !important;
      height: 1px !important;
      opacity: 0 !important;
      pointer-events: none !important;
      z-index: -999 !important;
    `;
  });
}

// ─── 更新视线光标位置 ──────────────────────────────────────────
function moveCursor(cursorEl, x, y) {
  if (!cursorEl) return;
  cursorEl.classList.remove('hidden');
  cursorEl.style.left = x + 'px';
  cursorEl.style.top  = y + 'px';
}

// ─── WebGazer 初始化（唯一真实入口，无降级）───────────────────
async function initWebGazer() {
  if (State.webgazerReady) return true;

  // 检查 WebGazer 是否加载成功
  if (typeof webgazer === 'undefined') {
    showError(
      '无法加载 WebGazer.js 眼动追踪引擎',
      'webgazer 全局对象未定义，请检查 webgazer.js 文件是否存在'
    );
    return false;
  }

  // 检查浏览器是否支持摄像头
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    showError(
      '您的浏览器不支持摄像头访问',
      'navigator.mediaDevices.getUserMedia 不可用，请使用 Chrome / Edge 并通过 localhost 或 HTTPS 访问'
    );
    return false;
  }

  EL.loadingStatus.textContent = '正在请求摄像头权限…';

  try {
    // 先用 getUserMedia 主动请求权限，明确捕获拒绝
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    // 获得权限后立刻停止流，WebGazer 会自己重新请求
    stream.getTracks().forEach(t => t.stop());
  } catch (permErr) {
    const name = permErr.name || '';
    let msg = '摄像头访问被拒绝，无法启动眼动追踪';
    if (name === 'NotAllowedError' || name === 'PermissionDeniedError') {
      msg = '您拒绝了摄像头权限。请在浏览器地址栏点击摄像头图标，允许访问后再重试。';
    } else if (name === 'NotFoundError' || name === 'DevicesNotFoundError') {
      msg = '未检测到摄像头设备，请确认摄像头已连接并正常工作。';
    } else if (name === 'NotReadableError') {
      msg = '摄像头被其他应用占用，请关闭其他使用摄像头的程序后重试。';
    }
    showError(msg, `${name}: ${permErr.message}`);
    return false;
  }

  EL.loadingStatus.textContent = '正在初始化眼动追踪模型，请稍候…';

  try {
    // 注册 gaze listener——此函数只记录数据，不含任何模拟逻辑
    webgazer.setGazeListener((data, clock) => {
      if (!data) return;
      const x = data.x, y = data.y;

      // 校准界面：实时视线光标
      if (!EL.calibScreen.classList.contains('hidden')) {
        moveCursor(EL.gazeCursor, x, y);
      }
      // 追踪界面：视线光标 + 数据采集
      if (!EL.trackingScreen.classList.contains('hidden')) {
        moveCursor(EL.gazeCursorTracking, x, y);
        if (State.isTracking) {
          State.gazeHistory.push({ x, y, timestamp: clock });
        }
      }
    });

    await webgazer
      .setRegression('ridge')
      .saveDataAcrossSessions(false)
      .begin();

    // 禁用默认鼠标校准（会引入偏差）
    webgazer.removeMouseEventListeners();
    // 隐藏 WebGazer 自带的视频预览和红点
    webgazer.showVideoPreview(false).showPredictionPoints(false);

    // 将视频元素移出可视区域（但保持活跃以维持视频帧处理）
    setTimeout(hideWebGazerElements, 600);
    setTimeout(hideWebGazerElements, 1500); // 二次确保

    State.webgazerReady = true;
    hideModal(EL.loadingOverlay);
    showScreen(EL.homeScreen);
    console.log('[EyeTrack] WebGazer 初始化成功，摄像头已就绪');
    return true;

  } catch (err) {
    console.error('[EyeTrack] WebGazer.begin() 失败:', err);
    showError(
      '眼动追踪引擎启动失败，请确认摄像头正常并重试。',
      String(err)
    );
    return false;
  }
}

// ─── 校准系统 ─────────────────────────────────────────────────
function buildCalibrationPoints() {
  EL.calibPointsContainer.innerHTML = '';
  EL.calibProgressFill.style.background = '';
  State.calibPoints = [];
  State.currentCalibIndex = 0;

  const header  = document.getElementById('calibration-header');
  const headerH = header ? header.offsetHeight + 20 : 90;
  const margin  = 44;
  const usableW = window.innerWidth  - margin * 2;
  const usableH = window.innerHeight - headerH - margin;

  CALIB_POSITIONS.forEach((pos, i) => {
    const el = document.createElement('div');
    el.className = 'calib-point';
    el.id = `cp-${i}`;

    const px = margin + pos.x * usableW;
    const py = headerH + pos.y * usableH;
    el.style.left = `${px}px`;
    el.style.top  = `${py}px`;

    el.innerHTML = `
      <div class="calib-point-ring"></div>
      <div class="calib-point-dot"></div>
      <div class="calib-check">✓</div>
      <div class="calib-point-progress">0/${CLICKS_PER_POINT}</div>
    `;

    const pointData = { el, x: px, y: py, clicks: 0, done: false };
    State.calibPoints.push(pointData);

    el.addEventListener('click', () => handleCalibClick(i));
    EL.calibPointsContainer.appendChild(el);
  });

  activateCalibPoint(0);
  updateCalibProgress();
}

function activateCalibPoint(index) {
  State.currentCalibIndex = index;
  State.calibPoints.forEach((p, i) => {
    const isActive = (i === index);
    const isDone   = p.done;
    p.el.style.opacity   = (isActive || isDone) ? '1' : '0.3';
    p.el.style.transform = isActive && !isDone
      ? 'translate(-50%,-50%) scale(1.25)'
      : 'translate(-50%,-50%) scale(1)';
  });
}

function recordCalibrationPoint(index) {
  if (index !== State.currentCalibIndex) return;
  const point = State.calibPoints[index];
  if (point.done) return;

  point.clicks++;

  // 闪烁动效
  point.el.classList.add('clicking');
  setTimeout(() => point.el.classList.remove('clicking'), 320);

  // 更新进度文字
  const prog = point.el.querySelector('.calib-point-progress');
  prog.textContent = `${point.clicks}/${CLICKS_PER_POINT}`;

  // 向 WebGazer 提交校准点（实际屏幕坐标）
  const rect = point.el.getBoundingClientRect();
  const sx  = rect.left + rect.width / 2;
  const sy  = rect.top + rect.height / 2;
  try {
    webgazer.recordScreenPosition(sx, sy, 'click');
  } catch (_) {}

  if (point.clicks >= CLICKS_PER_POINT) {
    point.done = true;
    point.el.classList.add('done');
    point.el.style.transform = 'translate(-50%,-50%) scale(1)';
    prog.textContent = '';
    updateCalibProgress();

    const next = State.calibPoints.findIndex((p, j) => j > index && !p.done);
    if (next !== -1) {
      setTimeout(() => activateCalibPoint(next), 350);
    } else {
      setTimeout(onCalibrationComplete, 700);
    }
  } else {
    updateCalibProgress();
  }
}

function handleCalibClick(index) {
  recordCalibrationPoint(index);
}

function handleCalibrationKeydown(event) {
  if (event.repeat) return;
  if (EL.calibScreen.classList.contains('hidden')) return;
  if (event.target.matches('input, textarea, select')) return;
  if (!CALIBRATION_KEYS.has(event.key) && event.code !== 'Numpad0') return;

  event.preventDefault();
  recordCalibrationPoint(State.currentCalibIndex);
}

function updateCalibProgress() {
  const total = CALIB_POSITIONS.length * CLICKS_PER_POINT;
  const done  = State.calibPoints.reduce((s, p) => s + Math.min(p.clicks, CLICKS_PER_POINT), 0);
  const pct   = Math.round((done / total) * 100);
  EL.calibProgressFill.style.width = pct + '%';
  EL.calibProgressPct.textContent  = pct + '%';
}

function onCalibrationComplete() {
  EL.calibStatusText.textContent = '校准完成！';
  EL.calibProgressFill.style.background = 'linear-gradient(90deg, #059669, #34D399)';

  setTimeout(() => {
    createCalibrationSession();
    State.calibrationDone = true;
    EL.gazeCursor.classList.add('hidden');
    showScreen(EL.homeScreen);

    // 更新首页状态
    EL.calibStatusIndicator.className = 'status-indicator status-success';
    EL.calibStatusLabel.textContent   = `${State.calibrationSession.label} 校准完成`;
    EL.startCalibBtn.textContent      = '重新校准';

    if (State.selectedImageId) {
      enableTrackButton();
    } else {
      setTrackStatus('status-pending', '请上传图像以开始追踪');
    }
  }, 1000);
}

// ─── 图像上传 ──────────────────────────────────────────────────
function setupDropzone() {
  EL.dropzone.addEventListener('click', () => {
    if (State.uploadedImages.length >= MAX_STORED_IMAGES) {
      alert('最多只能预存 5 张图片，请先删除一张再继续添加。');
      return;
    }
    EL.fileInput.click();
  });
  EL.fileInput.addEventListener('change', e => {
    loadImageFiles(e.target.files);
  });
  EL.dropzone.addEventListener('dragover', e => {
    e.preventDefault();
    EL.dropzone.classList.add('drag-over');
  });
  EL.dropzone.addEventListener('dragleave', () => EL.dropzone.classList.remove('drag-over'));
  EL.dropzone.addEventListener('drop', e => {
    e.preventDefault();
    EL.dropzone.classList.remove('drag-over');
    loadImageFiles(e.dataTransfer.files);
  });
}

function validateImageFile(file) {
  if (!file.type.startsWith('image/')) {
    alert('请选择 PNG、JPG 或 WEBP 等图片文件。');
    return false;
  }
  if (file.size > MAX_IMAGE_BYTES) {
    alert('图片不能超过 10MB，请压缩后再上传。');
    return false;
  }
  return true;
}

function loadImageFiles(fileList) {
  const remaining = MAX_STORED_IMAGES - State.uploadedImages.length;
  const files = Array.from(fileList || []);

  if (!files.length) return;
  if (remaining <= 0) {
    alert('最多只能预存 5 张图片，请先删除一张再继续添加。');
    EL.fileInput.value = '';
    return;
  }

  const accepted = [];
  for (const file of files) {
    if (!validateImageFile(file)) continue;
    if (accepted.length >= remaining) break;
    accepted.push(file);
  }

  if (files.length > remaining) {
    alert(`最多只能预存 5 张图片，本次已添加前 ${remaining} 张有效图片。`);
  }

  accepted.forEach(loadImageFile);
  EL.fileInput.value = '';
}

function loadImageFile(file) {
  const reader = new FileReader();
  reader.onload = e => {
    const image = {
      id: `${Date.now()}-${Math.random().toString(36).slice(2)}`,
      name: file.name,
      size: file.size,
      src: e.target.result,
    };
    State.uploadedImages.push(image);
    selectImage(image.id);
    renderImageGallery();
  };
  reader.readAsDataURL(file);
}

function selectImage(id) {
  const image = State.uploadedImages.find(item => item.id === id);
  if (!image) return;

  State.selectedImageId = image.id;
  State.uploadedImageSrc = image.src;
  renderImageGallery();

  if (State.calibrationDone) {
    enableTrackButton();
  } else {
    setTrackStatus('status-pending', `已选择「${image.name}」，请先完成校准`);
  }
}

function removeImage(id) {
  State.uploadedImages = State.uploadedImages.filter(item => item.id !== id);

  if (State.selectedImageId === id) {
    const next = State.uploadedImages[0];
    State.selectedImageId = next ? next.id : null;
    State.uploadedImageSrc = next ? next.src : null;
  }

  renderImageGallery();

  if (State.selectedImageId) {
    const selected = State.uploadedImages.find(item => item.id === State.selectedImageId);
    if (State.calibrationDone) enableTrackButton();
    else setTrackStatus('status-pending', `已选择「${selected.name}」，请先完成校准`);
  } else {
    EL.startTrackBtn.disabled = true;
    EL.startTrackBtn.className = 'btn btn-secondary';
    setTrackStatus('status-pending', '请上传图像以开始追踪');
  }
}

function renderImageGallery() {
  EL.imageGallery.innerHTML = '';
  EL.imageGallery.classList.toggle('hidden', State.uploadedImages.length === 0);

  State.uploadedImages.forEach((image, index) => {
    const item = document.createElement('div');
    item.className = `image-thumb${image.id === State.selectedImageId ? ' selected' : ''}`;
    item.tabIndex = 0;
    item.setAttribute('role', 'button');
    item.setAttribute('aria-label', `选择图片 ${index + 1}: ${image.name}`);
    item.addEventListener('click', () => selectImage(image.id));
    item.addEventListener('keydown', event => {
      if (event.key !== 'Enter' && event.key !== ' ') return;
      event.preventDefault();
      selectImage(image.id);
    });

    const img = document.createElement('img');
    img.src = image.src;
    img.alt = image.name;

    const name = document.createElement('span');
    name.className = 'image-thumb-name';
    name.textContent = image.name;

    const remove = document.createElement('button');
    remove.type = 'button';
    remove.className = 'image-thumb-remove';
    remove.setAttribute('aria-label', `删除图片 ${image.name}`);
    remove.textContent = '×';
    remove.addEventListener('click', event => {
      event.stopPropagation();
      removeImage(image.id);
    });

    item.append(img, name, remove);
    EL.imageGallery.appendChild(item);
  });
}

async function startCalibrationFromHome() {
  if (!State.privacyAccepted) {
    State.pendingCalibrationStart = true;
    showModal(EL.privacyModal);
    return;
  }

  if (!State.webgazerReady) {
    showModal(EL.loadingOverlay);
    EL.loadingStatus.textContent = '正在启用摄像头…';
    const ready = await initWebGazer();
    if (!ready) return;
  }

  beginCalibrationScreen();
}

function beginCalibrationScreen() {
  try { webgazer.resume(); } catch (_) {}
  showScreen(EL.calibScreen);
  buildCalibrationPoints();
  EL.gazeCursor.classList.remove('hidden');
}

function setTrackStatus(cls, text) {
  EL.trackStatusIndicator.className = `status-indicator ${cls}`;
  EL.trackStatusIndicator.querySelector('span:last-child').textContent = text;
}

function enableTrackButton() {
  EL.startTrackBtn.disabled = false;
  EL.startTrackBtn.className = 'btn btn-primary';
  const image = getSelectedImage();
  const name = image ? `「${image.name}」` : '当前图像';
  const runCount = State.calibrationSession ? State.calibrationSession.runs.length : 0;
  const sessionText = State.calibrationSession ? `${State.calibrationSession.label} · 已记录 ${runCount} 次` : '已校准';
  setTrackStatus('status-active', `${sessionText} · ${name}可开始追踪`);
}

// ─── 眼动追踪 ──────────────────────────────────────────────────
function startTracking() {
  if (!State.webgazerReady) {
    alert('眼动追踪引擎尚未就绪，请等待初始化完成。');
    return;
  }
  if (!State.calibrationDone || !State.calibrationSession) {
    alert('请先完成一次校准。');
    return;
  }
  if (!State.uploadedImageSrc) {
    alert('请先选择要分析的图像。');
    return;
  }

  const image = getSelectedImage();
  if (!image) {
    alert('请先选择要分析的图像。');
    return;
  }

  State.gazeHistory     = [];
  State.isTracking      = true;
  State.trackingStartTime = Date.now();
  State.trackingStartedAt = new Date().toISOString();
  State.trackingImage = {
    id: image.id,
    name: image.name,
    size: image.size,
    src: image.src,
  };
  State.currentReportRun = null;

  // WebGazer 在 begin() 后持续运行，这里只需恢复（如果暂停过）
  try { webgazer.resume(); } catch (_) {}

  EL.trackingImage.src = State.uploadedImageSrc;
  showScreen(EL.trackingScreen);
}

function stopTracking() {
  State.isTracking = false;
  const duration = (Date.now() - State.trackingStartTime) / 1000;
  const run = storeTrackingRun(duration);

  // 同一校准会话下会连续观看多张图，因此这里只暂停采集，不清除校准。
  try { webgazer.pause(); } catch (_) {}
  enableTrackButton();

  showDataScreen(run);
}

function storeTrackingRun(duration) {
  const session = State.calibrationSession;
  const image = State.trackingImage || getSelectedImage();
  const run = {
    id: `trial-${session.runs.length + 1}`,
    startedAt: State.trackingStartedAt,
    endedAt: new Date().toISOString(),
    duration,
    image: {
      id: image.id,
      name: image.name,
      size: image.size,
    },
    imageSrc: image.src,
    points: State.gazeHistory.map((point, index) => ({
      index: index + 1,
      x: point.x,
      y: point.y,
      timestamp: point.timestamp,
    })),
  };

  session.runs.push(run);
  State.currentReportRun = run;
  State.gazeHistory = run.points;
  State.uploadedImageSrc = run.imageSrc;
  updateHomeDataSummary();
  return run;
}

function updateReportStats(run) {
  const duration = run.duration;
  const pts = run.points.length;
  const fps = duration > 0 ? Math.round(pts / duration) : 0;

  let quality = '低', qualityColor = 'var(--red)';
  if (pts > 500 && fps > 15) { quality = '高'; qualityColor = 'var(--green-dark)'; }
  else if (pts > 100)        { quality = '中'; qualityColor = 'var(--orange)'; }

  EL.statDuration.textContent = duration.toFixed(1) + ' s';
  EL.statPoints.textContent   = pts.toLocaleString();
  EL.statQuality.textContent  = quality;
  EL.statQuality.style.color  = qualityColor;
  EL.statFps.textContent      = fps + ' Hz';
}

// ─── 热力图（Canvas 原生实现） ──────────────────────────────────
function drawHeatmap() {
  const canvas = EL.reportCanvas;
  const run = State.currentReportRun;
  const data = run ? run.points : State.gazeHistory;
  const imageSrc = run ? run.imageSrc : State.uploadedImageSrc;
  if (!imageSrc) return;

  const img    = new Image();
  img.onload   = () => {
    const containerW = canvas.parentElement.clientWidth || window.innerWidth;
    const scale = Math.min(
      containerW / img.naturalWidth,
      (window.innerHeight * 0.65) / img.naturalHeight,
      1
    );
    canvas.width  = Math.round(img.naturalWidth  * scale);
    canvas.height = Math.round(img.naturalHeight * scale);

    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

    if (data.length < 3) {
      ctx.fillStyle = 'rgba(255,255,255,0.5)';
      ctx.font = '16px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('数据点不足，请延长追踪时长', canvas.width / 2, canvas.height / 2);
      return;
    }

    // 坐标映射：屏幕坐标 → canvas 坐标
    const sw = window.innerWidth, sh = window.innerHeight;
    const ia = img.naturalWidth / img.naturalHeight;
    const sa = sw / sh;
    let dw, dh, ox, oy;
    if (ia > sa) { dw = sw; dh = sw / ia; }
    else         { dh = sh; dw = sh * ia; }
    ox = (sw - dw) / 2;
    oy = (sh - dh) / 2;

    const mx = sx => ((sx - ox) / dw) * canvas.width;
    const my = sy => ((sy - oy) / dh) * canvas.height;

    // 生成密度图（离屏 canvas）
    const tmp    = document.createElement('canvas');
    tmp.width    = canvas.width;
    tmp.height   = canvas.height;
    const tc     = tmp.getContext('2d');
    tc.globalCompositeOperation = 'lighter';
    const radius = Math.max(28, canvas.width * 0.055);

    data.forEach(pt => {
      const cx = mx(pt.x), cy = my(pt.y);
      if (cx < -radius || cx > canvas.width  + radius) return;
      if (cy < -radius || cy > canvas.height + radius) return;
      const g = tc.createRadialGradient(cx, cy, 0, cx, cy, radius);
      g.addColorStop(0, 'rgba(0,0,0,0.45)');
      g.addColorStop(1, 'rgba(0,0,0,0)');
      tc.beginPath();
      tc.fillStyle = g;
      tc.arc(cx, cy, radius, 0, Math.PI * 2);
      tc.fill();
    });

    // 颜色映射：alpha → 蓝绿黄红
    const gc  = document.createElement('canvas');
    gc.width  = 256; gc.height = 1;
    const gx  = gc.getContext('2d');
    const lg  = gx.createLinearGradient(0, 0, 256, 0);
    lg.addColorStop(0.00, 'rgba(0,0,255,0)');
    lg.addColorStop(0.25, 'rgba(0,255,255,0.55)');
    lg.addColorStop(0.50, 'rgba(0,255,0,0.70)');
    lg.addColorStop(0.75, 'rgba(255,255,0,0.82)');
    lg.addColorStop(1.00, 'rgba(255,0,0,0.94)');
    gx.fillStyle = lg;
    gx.fillRect(0, 0, 256, 1);
    const gd = gx.getImageData(0, 0, 256, 1).data;

    const heat = tc.getImageData(0, 0, canvas.width, canvas.height);
    const px   = heat.data;
    for (let i = 0; i < px.length; i += 4) {
      const a = px[i + 3];
      if (a > 0) {
        const ci = Math.min(255, Math.floor(a * 1.6)) * 4;
        px[i]     = gd[ci];
        px[i + 1] = gd[ci + 1];
        px[i + 2] = gd[ci + 2];
        px[i + 3] = Math.min(240, a * 2.2);
      }
    }
    ctx.putImageData(heat, 0, 0);
    drawLegend(ctx, canvas.width, canvas.height);
  };
  img.src = imageSrc;
}

// ─── 视线轨迹图 ────────────────────────────────────────────────
function drawGazePlot() {
  const canvas = EL.reportCanvas;
  const run = State.currentReportRun;
  const data = run ? run.points : State.gazeHistory;
  const imageSrc = run ? run.imageSrc : State.uploadedImageSrc;
  if (!imageSrc) return;

  const img  = new Image();
  img.onload = () => {
    const containerW = canvas.parentElement.clientWidth || window.innerWidth;
    const scale = Math.min(
      containerW / img.naturalWidth,
      (window.innerHeight * 0.65) / img.naturalHeight,
      1
    );
    canvas.width  = Math.round(img.naturalWidth  * scale);
    canvas.height = Math.round(img.naturalHeight * scale);

    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

    if (data.length < 2) {
      ctx.fillStyle = 'rgba(255,255,255,0.5)';
      ctx.font = '16px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('数据点不足', canvas.width / 2, canvas.height / 2);
      return;
    }

    // 坐标映射
    const sw = window.innerWidth, sh = window.innerHeight;
    const ia = img.naturalWidth / img.naturalHeight;
    const sa = sw / sh;
    let dw, dh, ox, oy;
    if (ia > sa) { dw = sw; dh = sw / ia; }
    else         { dh = sh; dw = sh * ia; }
    ox = (sw - dw) / 2;
    oy = (sh - dh) / 2;

    const mx = sx => ((sx - ox) / dw) * canvas.width;
    const my = sy => ((sy - oy) / dh) * canvas.height;

    // 降采样（最多 350 点）
    const step    = Math.max(1, Math.floor(data.length / 350));
    const sampled = data.filter((_, i) => i % step === 0);
    const pts     = sampled.map(p => ({ x: mx(p.x), y: my(p.y) }));

    // 连线
    ctx.beginPath();
    ctx.moveTo(pts[0].x, pts[0].y);
    pts.forEach(p => ctx.lineTo(p.x, p.y));
    ctx.strokeStyle = 'rgba(96,165,250,0.5)';
    ctx.lineWidth   = Math.max(1.5, canvas.width * 0.002);
    ctx.lineCap     = 'round';
    ctx.lineJoin    = 'round';
    ctx.stroke();

    // 注视点
    const labelEvery = Math.max(1, Math.floor(pts.length / 18));
    pts.forEach((p, i) => {
      const prog    = i / (pts.length - 1);
      const r       = (3 + prog * 5) * (canvas.width / 900);
      const opacity = 0.35 + prog * 0.65;

      ctx.beginPath();
      ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
      ctx.fillStyle   = `rgba(96,165,250,${opacity})`;
      ctx.fill();
      ctx.strokeStyle = 'rgba(255,255,255,0.75)';
      ctx.lineWidth   = 1;
      ctx.stroke();

      if (i % labelEvery === 0 || i === 0 || i === pts.length - 1) {
        ctx.fillStyle    = 'white';
        ctx.font         = `bold ${Math.max(8, canvas.width * 0.011)}px Inter,sans-serif`;
        ctx.textAlign    = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(i + 1, p.x, p.y);
      }
    });

    // 起/终点
    const drawMarker = (p, color, label) => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, 8, 0, Math.PI * 2);
      ctx.fillStyle = color;
      ctx.fill();
      ctx.fillStyle    = 'white';
      ctx.font         = `bold ${Math.max(9, canvas.width * 0.012)}px Inter,sans-serif`;
      ctx.textAlign    = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(label, p.x, p.y);
    };
    drawMarker(pts[0],               'rgba(52,211,153,0.92)', 'S');
    drawMarker(pts[pts.length - 1],  'rgba(248,113,113,0.92)', 'E');
  };
  img.src = imageSrc;
}

function drawLegend(ctx, w, h) {
  const lw = Math.min(160, w * 0.28);
  const lh = 11;
  const x  = w - lw - 14;
  const y  = h - 34;

  ctx.fillStyle = 'rgba(0,0,0,0.5)';
  ctx.beginPath();
  ctx.roundRect(x - 8, y - 18, lw + 16, lh + 30, 6);
  ctx.fill();

  const g = ctx.createLinearGradient(x, 0, x + lw, 0);
  g.addColorStop(0,   'rgba(0,0,255,0.65)');
  g.addColorStop(0.5, 'rgba(0,255,0,0.72)');
  g.addColorStop(1,   'rgba(255,0,0,0.9)');
  ctx.fillStyle = g;
  ctx.fillRect(x, y, lw, lh);

  ctx.fillStyle    = 'rgba(255,255,255,0.75)';
  ctx.font         = '10px Inter,sans-serif';
  ctx.textAlign    = 'left';
  ctx.textBaseline = 'top';
  ctx.fillText('低', x, y + lh + 3);
  ctx.textAlign = 'right';
  ctx.fillText('高', x + lw, y + lh + 3);
  ctx.textAlign    = 'center';
  ctx.fillStyle    = 'rgba(255,255,255,0.55)';
  ctx.fillText('注意力密度', x + lw / 2, y - 14);
}

// ─── 数据导出 ──────────────────────────────────────────────────
function csvCell(value) {
  const text = value == null ? '' : String(value);
  return `"${text.replace(/"/g, '""')}"`;
}

function downloadBlob(filename, content, type) {
  const blob = new Blob([content], { type });
  const url  = URL.createObjectURL(blob);
  const a    = Object.assign(document.createElement('a'), { href: url, download: filename });
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function buildCsv(records) {
  const headers = [
    'participant_id',
    'participant_label',
    'calibrated_at',
    'trial_id',
    'trial_index',
    'image_id',
    'image_name',
    'image_size',
    'trial_started_at',
    'trial_ended_at',
    'trial_duration_seconds',
    'point_index',
    'x',
    'y',
    'timestamp',
  ];
  const rows = [headers.map(csvCell).join(',')];

  records.forEach(({ session, run, trialIndex }) => {
    run.points.forEach(point => {
      rows.push([
        session.id,
        session.label,
        session.calibratedAt,
        run.id,
        trialIndex,
        run.image.id,
        run.image.name,
        run.image.size,
        run.startedAt,
        run.endedAt,
        run.duration.toFixed(3),
        point.index,
        Math.round(point.x),
        Math.round(point.y),
        point.timestamp,
      ].map(csvCell).join(','));
    });
  });

  return rows.join('\n');
}

function exportCSV() {
  const runs = getAllTrackingRuns();
  if (!runs.length) { alert('暂无可导出的追踪数据'); return; }

  downloadBlob(
    `eye_tracking_all_${new Date().toISOString().replace(/[:.]/g, '-')}.csv`,
    buildCsv(runs),
    'text/csv;charset=utf-8;'
  );
}

function exportSelectedCSV() {
  const record = findRunRecord();
  if (!record) { alert('请先选择一次追踪记录。'); return; }

  downloadBlob(
    `eye_tracking_${record.session.id}_${record.run.id}_${safeFileName(record.run.image.name)}.csv`,
    buildCsv([record]),
    'text/csv;charset=utf-8;'
  );
}

function exportArchive() {
  if (!State.calibrationSessions.length) { alert('暂无参与者存档可导出'); return; }
  const archive = {
    schema: 'visual-analytics-eye-archive',
    version: 1,
    exportedAt: new Date().toISOString(),
    calibrationSessionSeq: State.calibrationSessionSeq,
    sessions: State.calibrationSessions,
  };

  downloadBlob(
    `eye_tracking_archive_${new Date().toISOString().replace(/[:.]/g, '-')}.json`,
    JSON.stringify(archive, null, 2),
    'application/json;charset=utf-8;'
  );
}

function importArchiveFile(file) {
  if (!file) return;
  const reader = new FileReader();
  reader.onload = event => {
    try {
      const archive = JSON.parse(event.target.result);
      const sessions = normalizeImportedSessions(archive);
      if (!sessions.length) throw new Error('存档中没有可用的参与者数据');

      const imported = uniquifyImportedSessionIds(sessions);
      State.calibrationSessions.push(...imported);
      State.calibrationSessionSeq = Math.max(State.calibrationSessionSeq, State.calibrationSessions.length);
      State.calibrationSession = State.calibrationDone ? State.calibrationSession : null;
      State.selectedSessionId = imported[0].id;
      State.currentReportRun = imported[0].runs[0] || null;
      State.gazeHistory = State.currentReportRun ? State.currentReportRun.points : [];
      State.uploadedImageSrc = State.currentReportRun ? State.currentReportRun.imageSrc : null;
      updateHomeDataSummary();
      showDataScreen(State.currentReportRun);
    } catch (err) {
      alert(`无法导入存档：${err.message}`);
    } finally {
      EL.importArchiveInput.value = '';
    }
  };
  reader.readAsText(file);
}

function uniquifyImportedSessionIds(sessions) {
  const used = new Set(State.calibrationSessions.map(session => session.id));
  return sessions.map(session => {
    let id = session.id;
    let suffix = 2;
    while (used.has(id)) {
      id = `${session.id}-import-${suffix}`;
      suffix += 1;
    }
    used.add(id);
    return id === session.id ? session : { ...session, id, label: `${session.label} (${id})` };
  });
}

function normalizeImportedSessions(archive) {
  const sessions = Array.isArray(archive?.sessions)
    ? archive.sessions
    : (Array.isArray(archive) ? archive : []);

  return sessions.map((session, sessionIndex) => {
    const id = String(session.id || `imported-participant-${sessionIndex + 1}`);
    return {
      id,
      label: String(session.label || id),
      calibratedAt: session.calibratedAt || archive.exportedAt || new Date().toISOString(),
      runs: (Array.isArray(session.runs) ? session.runs : []).map((run, runIndex) => ({
        id: String(run.id || `trial-${runIndex + 1}`),
        startedAt: run.startedAt || '',
        endedAt: run.endedAt || '',
        duration: Number(run.duration) || 0,
        image: {
          id: String(run.image?.id || `image-${runIndex + 1}`),
          name: String(run.image?.name || `image-${runIndex + 1}`),
          size: Number(run.image?.size) || 0,
        },
        imageSrc: run.imageSrc || '',
        points: (Array.isArray(run.points) ? run.points : []).map((point, pointIndex) => ({
          index: Number(point.index) || pointIndex + 1,
          x: Number(point.x) || 0,
          y: Number(point.y) || 0,
          timestamp: point.timestamp ?? '',
        })),
      })),
    };
  });
}

function safeFileName(value) {
  return String(value || 'trial').replace(/[\\/:*?"<>|]/g, '_').slice(0, 60);
}

// ─── 事件绑定 ──────────────────────────────────────────────────
function bindEvents() {
  // 隐私弹窗 → 显示加载遮罩 → 初始化摄像头
  EL.acceptPrivacy.addEventListener('click', async () => {
    State.privacyAccepted = true;
    hideModal(EL.privacyModal);
    showModal(EL.loadingOverlay);
    const ready = await initWebGazer();
    if (ready && State.pendingCalibrationStart) {
      State.pendingCalibrationStart = false;
      beginCalibrationScreen();
    }
  });

  // 重试按钮
  EL.retryInitBtn.addEventListener('click', () => {
    hideModal(EL.errorModal);
    showModal(EL.loadingOverlay);
    EL.loadingStatus.textContent = '正在重新初始化…';
    initWebGazer().then(ready => {
      if (ready && State.pendingCalibrationStart) {
        State.pendingCalibrationStart = false;
        beginCalibrationScreen();
      }
    });
  });

  // 校准
  EL.startCalibBtn.addEventListener('click', startCalibrationFromHome);

  // 开始追踪
  EL.startTrackBtn.addEventListener('click', () => {
    if (!State.uploadedImageSrc) { alert('请先选择图像'); return; }
    startTracking();
  });

  EL.openDataBtn.addEventListener('click', () => showDataScreen());
  EL.importArchiveHomeBtn.addEventListener('click', () => EL.importArchiveInput.click());

  // 停止追踪
  EL.stopTrackingBtn.addEventListener('click', stopTracking);

  // 校准页键盘确认：Space / Enter / 0
  document.addEventListener('keydown', handleCalibrationKeydown);

  // 报告标签
  EL.tabHeatmap.addEventListener('click', () => {
    EL.tabHeatmap.classList.add('active');
    EL.tabGazeplot.classList.remove('active');
    drawHeatmap();
  });
  EL.tabGazeplot.addEventListener('click', () => {
    EL.tabGazeplot.classList.add('active');
    EL.tabHeatmap.classList.remove('active');
    drawGazePlot();
  });

  // 返回首页
  EL.backHomeBtn.addEventListener('click', () => {
    showScreen(EL.homeScreen);
  });

  // 导出
  EL.importArchiveBtn.addEventListener('click', () => EL.importArchiveInput.click());
  EL.importArchiveInput.addEventListener('change', e => importArchiveFile(e.target.files[0]));
  EL.exportArchiveBtn.addEventListener('click', exportArchive);
  EL.exportSelectedDataBtn.addEventListener('click', exportSelectedCSV);
  EL.exportDataBtn.addEventListener('click', exportCSV);
  EL.exportPdfBtn.addEventListener('click',  () => window.print());

  // 文件上传
  setupDropzone();

  // 窗口缩放时重绘报告
  window.addEventListener('resize', () => {
    if (EL.reportScreen.classList.contains('hidden')) return;
    if (!State.currentReportRun) return;
    if (EL.tabHeatmap.classList.contains('active')) drawHeatmap();
    else drawGazePlot();
  });
}

// ─── 入口 ─────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  // 默认直接进入主界面；只有开始校准时才请求摄像头权限。
  hideModal(EL.privacyModal);
  hideModal(EL.loadingOverlay);
  hideModal(EL.errorModal);
  showScreen(EL.homeScreen);
  updateHomeDataSummary();

  bindEvents();
});
