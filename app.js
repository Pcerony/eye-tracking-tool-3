/* ============================================================
   app.js — 眼动追踪工具核心逻辑（真实摄像头版本）
   绝对不使用任何鼠标模拟 / 降级模式。
   WebGazer 初始化失败 → 显示错误弹窗，禁止继续操作。
============================================================ */

'use strict';

// ─── 状态 ──────────────────────────────────────────────────────
const State = {
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
  calibrationRecording: false,
  currentA4Plane: null,
  reportShowBackground: true,
  lastReportRunId: null,
  cameraDevices: [],
  selectedCameraDeviceId: '',
  activeCameraDeviceId: '',
  cameraSelectPreviewStream: null,
  gazePlaybackPlaying: false,
  gazePlaybackFrameId: null,
  gazePlaybackStartedAt: 0,
  gazePlaybackDurationMs: 0,
  gazePlaybackToken: 0,
  cameraSelectContinuing: false,
  calibrationScreenStarting: false,
  archiveDirty: false,
  archiveUnloadPrompted: false,
};

// ─── DOM ────────────────────────────────────────────────────────
const $ = (id) => document.getElementById(id);
const EL = {
  // 弹窗
  loadingOverlay:  $('loading-overlay'),
  loadingStatus:   $('loading-status'),
  errorModal:      $('error-modal'),
  errorMessage:    $('error-message'),
  errorDetail:     $('error-detail'),
  retryInitBtn:    $('retry-init-btn'),

  // 屏幕
  homeScreen:      $('home-screen'),
  cameraSelectScreen: $('camera-select-screen'),
  cameraAdjustScreen: $('camera-adjust-screen'),
  calibScreen:     $('calibration-screen'),
  trackingScreen:  $('tracking-screen'),
  reportScreen:    $('report-screen'),

  // 摄像头选择
  cameraDeviceSelect: $('camera-device-select'),
  cameraSelectVideo: $('camera-select-video'),
  cameraSelectStatus: $('camera-select-status'),
  cameraSelectContinueBtn: $('camera-select-continue-btn'),
  cameraSelectBackBtn: $('camera-select-back-btn'),
  cameraRefreshBtn: $('camera-refresh-btn'),

  // 摄像头调整
  cameraAdjustVideo: $('camera-adjust-video'),
  cameraAdjustStatus: $('camera-adjust-status'),
  cameraAdjustContinueBtn: $('camera-adjust-continue-btn'),
  cameraAdjustBackBtn: $('camera-adjust-back-btn'),

  // 校准
  calibPointsContainer: $('calibration-points-container'),
  calibPaperFrame:      $('calibration-paper-frame'),
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
  imageGallery:    $('image-gallery'),

  // 追踪
  trackingImage:        $('tracking-image'),
  trackingPaperPlane:   $('tracking-paper-plane'),
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
  vizBackgroundToggle: $('viz-background-toggle'),
  vizTimeStart:  $('viz-time-start'),
  vizTimeEnd:    $('viz-time-end'),
  vizTimeResetBtn: $('viz-time-reset-btn'),
  vizRangeStatus: $('viz-range-status'),
  gazePlaybackBtn: $('gaze-playback-btn'),
  exportVizLayerBtn: $('export-viz-layer-btn'),
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
const A4_SIZE_MM = { width: 297, height: 210 };
const A4_ASPECT = A4_SIZE_MM.width / A4_SIZE_MM.height;
const CLICKS_PER_POINT = 3;
const CALIBRATION_SAMPLES_PER_CONFIRM = 3;
const CALIBRATION_SAMPLE_INTERVAL_MS = 45;
const CALIBRATION_KEYS = new Set([' ', 'Enter', '0']);
const BUILTIN_IMAGES = [
  { id: 'a1', name: 'a1', group: 'A', condition: 'control', conditionLabel: '对照类', src: 'A1.png' },
  { id: 'a2', name: 'a2', group: 'A', condition: 'control', conditionLabel: '对照类', src: 'A2.png' },
  { id: 'b1', name: 'b1', group: 'B', condition: 'experiment', conditionLabel: '实验类', src: 'B1.png' },
  { id: 'b2', name: 'b2', group: 'B', condition: 'experiment', conditionLabel: '实验类', src: 'B2.png' },
];

// ─── 显示/隐藏弹窗 ─────────────────────────────────────────────
function showModal(el)  { el?.classList.add('active'); }
function hideModal(el)  { el?.classList.remove('active'); }

// ─── 屏幕切换 ──────────────────────────────────────────────────
function showScreen(screenEl) {
  [EL.homeScreen, EL.cameraSelectScreen, EL.cameraAdjustScreen, EL.calibScreen, EL.trackingScreen, EL.reportScreen]
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
  const enteredName = EL.participantIdInput.value.trim();
  const participantId = enteredName || `未命名参与者-${State.calibrationSessionSeq}`;
  const session = {
    id: participantId,
    label: participantId,
    calibratedAt: now,
    coordinateSystem: 'a4-landscape-paper',
    a4Plane: State.currentA4Plane ? { ...State.currentA4Plane } : null,
    paperSizeMm: { ...A4_SIZE_MM },
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

function getCurrentHomeSession() {
  return State.calibrationSessions.find(session => session.id === State.selectedSessionId)
    || State.calibrationSession
    || findRunRecord(State.currentReportRun)?.session
    || null;
}

function updateHomeDataSummary() {
  const session = getCurrentHomeSession();
  EL.homeParticipantCount.textContent = session?.label || '未选择';
  EL.homeRunCount.textContent = getAllTrackingRuns().length;
}

function findRunRecord(targetRun = State.currentReportRun) {
  if (!targetRun) return null;
  return getAllTrackingRuns().find(record => record.run === targetRun || record.run.id === targetRun.id) || null;
}

function selectSession(sessionId) {
  stopGazePlayback(false);
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
  updateHomeDataSummary();
}

function selectRun(sessionId, runId) {
  stopGazePlayback(false);
  const session = State.calibrationSessions.find(item => item.id === sessionId);
  const run = session?.runs.find(item => item.id === runId);
  if (!session || !run) return;

  State.selectedSessionId = session.id;
  State.currentReportRun = run;
  State.uploadedImageSrc = run.imageSrc;
  State.gazeHistory = run.points;
  renderDataWorkbench();
  updateReportFromCurrentRun();
  updateHomeDataSummary();
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
    stopGazePlayback(false);
    EL.statDuration.textContent = '0.0 s';
    EL.statPoints.textContent = '0';
    EL.statQuality.textContent = '—';
    EL.statQuality.style.color = '';
    EL.statFps.textContent = '— Hz';
    updateReportRangeStatus(null);
    const ctx = EL.reportCanvas.getContext('2d');
    ctx.clearRect(0, 0, EL.reportCanvas.width, EL.reportCanvas.height);
    return;
  }
  const reportRunKey = `${State.selectedSessionId || ''}:${run.id}`;
  if (State.lastReportRunId !== reportRunKey) {
    State.lastReportRunId = reportRunKey;
    resetReportTimeRange(run);
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

function clamp01(value) {
  return Math.max(0, Math.min(1, value));
}

function createA4PlaneRect(topOffset = 0, bottomOffset = 0) {
  const sideMargin = Math.max(24, Math.min(72, window.innerWidth * 0.06));
  const verticalMargin = 28;
  const availableW = Math.max(240, window.innerWidth - sideMargin * 2);
  const availableH = Math.max(320, window.innerHeight - topOffset - bottomOffset - verticalMargin * 2);
  let width = Math.min(availableW, availableH * A4_ASPECT);
  let height = width / A4_ASPECT;

  if (height > availableH) {
    height = availableH;
    width = height * A4_ASPECT;
  }

  return {
    left: Math.round((window.innerWidth - width) / 2),
    top: Math.round(topOffset + verticalMargin),
    width: Math.round(width),
    height: Math.round(height),
    paperWidthMm: A4_SIZE_MM.width,
    paperHeightMm: A4_SIZE_MM.height,
  };
}

function getCalibrationA4Plane() {
  const header = document.getElementById('calibration-header');
  const headerH = header ? header.offsetHeight : 90;
  return createA4PlaneRect(headerH, 0);
}

function setElementToA4Plane(el, plane) {
  if (!el || !plane) return;
  el.style.left = `${plane.left}px`;
  el.style.top = `${plane.top}px`;
  el.style.width = `${plane.width}px`;
  el.style.height = `${plane.height}px`;
}

function a4ToVirtualScreen(pos, plane) {
  return {
    x: plane.left + pos.x * plane.width,
    y: plane.top + pos.y * plane.height,
  };
}

function virtualScreenToA4(x, y, plane) {
  if (!plane || !plane.width || !plane.height) {
    return { x: 0, y: 0, xMm: 0, yMm: 0, onPaper: false };
  }

  const rawX = (x - plane.left) / plane.width;
  const rawY = (y - plane.top) / plane.height;
  const nx = clamp01(rawX);
  const ny = clamp01(rawY);

  return {
    x: nx,
    y: ny,
    xMm: nx * A4_SIZE_MM.width,
    yMm: ny * A4_SIZE_MM.height,
    onPaper: rawX >= 0 && rawX <= 1 && rawY >= 0 && rawY <= 1,
  };
}

function getActiveA4Plane() {
  return State.calibrationSession?.a4Plane || State.currentA4Plane || getCalibrationA4Plane();
}

function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function resetTrackingAvailability(text = '摄像头已关闭，请重新校准后开始追踪') {
  State.webgazerReady = false;
  State.calibrationDone = false;
  State.isTracking = false;
  State.activeCameraDeviceId = '';

  EL.calibStatusIndicator.className = 'status-indicator status-pending';
  EL.calibStatusLabel.textContent = '未校准';
  EL.startCalibBtn.textContent = '选择摄像头并校准';
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
  State.activeCameraDeviceId = '';
}

function stopCameraSelectPreview() {
  if (State.cameraSelectPreviewStream) {
    State.cameraSelectPreviewStream.getTracks().forEach(track => track.stop());
  }
  State.cameraSelectPreviewStream = null;
  if (EL.cameraSelectVideo) {
    EL.cameraSelectVideo.pause();
    EL.cameraSelectVideo.srcObject = null;
  }
}

function getCameraConstraints(deviceId = State.selectedCameraDeviceId) {
  const video = {
    width: { min: 320, ideal: 640, max: 1920 },
    height: { min: 240, ideal: 480, max: 1080 },
  };

  if (deviceId) video.deviceId = { exact: deviceId };
  else video.facingMode = 'user';

  return { video };
}

function formatCameraLabel(device, index) {
  return device.label || `摄像头 ${index + 1}`;
}

function populateCameraDeviceSelect() {
  EL.cameraDeviceSelect.innerHTML = '';
  State.cameraDevices.forEach((device, index) => {
    const option = document.createElement('option');
    option.value = device.deviceId;
    option.textContent = formatCameraLabel(device, index);
    EL.cameraDeviceSelect.appendChild(option);
  });

  if (State.selectedCameraDeviceId && State.cameraDevices.some(device => device.deviceId === State.selectedCameraDeviceId)) {
    EL.cameraDeviceSelect.value = State.selectedCameraDeviceId;
  } else if (State.cameraDevices.length) {
    State.selectedCameraDeviceId = State.cameraDevices[0].deviceId;
    EL.cameraDeviceSelect.value = State.selectedCameraDeviceId;
  }
}

async function refreshCameraDevices() {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia || !navigator.mediaDevices.enumerateDevices) {
    showError(
      '您的浏览器不支持摄像头选择',
      'navigator.mediaDevices.getUserMedia 或 enumerateDevices 不可用，请使用 Chrome / Edge 并通过 localhost 或 HTTPS 访问'
    );
    return false;
  }

  EL.cameraSelectStatus.textContent = '正在请求摄像头权限…';

  try {
    const permissionStream = await navigator.mediaDevices.getUserMedia({ video: true });
    permissionStream.getTracks().forEach(track => track.stop());

    const devices = await navigator.mediaDevices.enumerateDevices();
    State.cameraDevices = devices.filter(device => device.kind === 'videoinput');
    populateCameraDeviceSelect();

    if (!State.cameraDevices.length) {
      EL.cameraSelectStatus.textContent = '未检测到可用摄像头';
      return false;
    }

    EL.cameraSelectStatus.textContent = `检测到 ${State.cameraDevices.length} 个摄像头`;
    await startCameraSelectPreview(State.selectedCameraDeviceId);
    return true;
  } catch (err) {
    handleCameraAccessError(err, '无法读取摄像头列表');
    return false;
  }
}

async function startCameraSelectPreview(deviceId) {
  stopCameraSelectPreview();
  if (!deviceId) return;

  try {
    const stream = await navigator.mediaDevices.getUserMedia(getCameraConstraints(deviceId));
    State.cameraSelectPreviewStream = stream;
    EL.cameraSelectVideo.srcObject = stream;
    await EL.cameraSelectVideo.play();
  } catch (err) {
    handleCameraAccessError(err, '无法预览所选摄像头');
  }
}

function handleCameraAccessError(err, fallbackMessage = '摄像头访问失败') {
  const name = err?.name || '';
  let msg = fallbackMessage;
  if (name === 'NotAllowedError' || name === 'PermissionDeniedError') {
    msg = '您拒绝了摄像头权限。请在浏览器地址栏点击摄像头图标，允许访问后再重试。';
  } else if (name === 'NotFoundError' || name === 'DevicesNotFoundError') {
    msg = '未检测到摄像头设备，请确认摄像头已连接并正常工作。';
  } else if (name === 'NotReadableError') {
    msg = '摄像头被其他应用占用，请关闭其他使用摄像头的程序后重试。';
  } else if (name === 'OverconstrainedError') {
    msg = '所选摄像头无法按当前配置启动，请选择其他摄像头。';
  }

  EL.cameraSelectStatus.textContent = msg;
  showError(msg, `${name}: ${err?.message || err}`);
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

function stopCameraAdjustmentPreview() {
  if (!EL.cameraAdjustVideo) return;
  EL.cameraAdjustVideo.pause();
  EL.cameraAdjustVideo.srcObject = null;
}

function syncCameraAdjustmentPreview() {
  const sourceVideo = document.getElementById('webgazerVideoFeed');
  const stream = sourceVideo && sourceVideo.srcObject;

  if (!stream) {
    EL.cameraAdjustStatus.textContent = '摄像头画面尚未就绪，请稍候…';
    return false;
  }

  if (EL.cameraAdjustVideo.srcObject !== stream) {
    EL.cameraAdjustVideo.srcObject = stream;
  }

  EL.cameraAdjustVideo.play().catch(() => {
    EL.cameraAdjustStatus.textContent = '请点击预览区域或继续按钮以激活摄像头画面';
  });
  EL.cameraAdjustStatus.textContent = '请让双眼位于画面中央，并保持面部清晰可见';
  return true;
}

// ─── 更新视线光标位置 ──────────────────────────────────────────
function moveCursor(cursorEl, x, y) {
  if (!cursorEl) return;
  cursorEl.classList.remove('hidden');
  cursorEl.style.left = x + 'px';
  cursorEl.style.top  = y + 'px';
}

function isCalibrationScreenActive() {
  return EL.calibScreen && !EL.calibScreen.classList.contains('hidden');
}

function isCameraSelectScreenActive() {
  return EL.cameraSelectScreen && !EL.cameraSelectScreen.classList.contains('hidden');
}

function isCameraAdjustScreenActive() {
  return EL.cameraAdjustScreen && !EL.cameraAdjustScreen.classList.contains('hidden');
}

function disableWebGazerMouseCalibration() {
  if (typeof webgazer === 'undefined') return;

  try {
    webgazer.removeMouseEventListeners();
  } catch (_) {}

  if (!webgazer.__eyeTrackMouseCalibrationDisabled) {
    try {
      webgazer.__eyeTrackOriginalAddMouseEventListeners = webgazer.addMouseEventListeners;
      webgazer.addMouseEventListeners = () => webgazer;
      webgazer.__eyeTrackMouseCalibrationDisabled = true;
    } catch (_) {}
  }
}

function blockCalibrationMouseMove(event) {
  if (!isCalibrationScreenActive()) return;
  event.preventDefault();
  event.stopImmediatePropagation();
}

// ─── WebGazer 初始化（唯一真实入口，无降级）───────────────────
async function initWebGazer() {
  if (State.webgazerReady && State.activeCameraDeviceId === State.selectedCameraDeviceId) return true;
  if (State.webgazerReady && State.activeCameraDeviceId !== State.selectedCameraDeviceId) {
    stopCameraStream();
    State.webgazerReady = false;
  }

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

  const selectedCamera = State.cameraDevices.find(device => device.deviceId === State.selectedCameraDeviceId);
  EL.loadingStatus.textContent = selectedCamera
    ? `正在启用摄像头：${selectedCamera.label || '所选摄像头'}…`
    : '正在启用摄像头…';

  try {
    const stream = await navigator.mediaDevices.getUserMedia(getCameraConstraints());
    stream.getTracks().forEach(t => t.stop());
  } catch (permErr) {
    handleCameraAccessError(permErr, '摄像头访问被拒绝，无法启动眼动追踪');
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
          const paperPoint = virtualScreenToA4(x, y, getActiveA4Plane());
          State.gazeHistory.push({
            x,
            y,
            a4X: paperPoint.x,
            a4Y: paperPoint.y,
            a4Xmm: paperPoint.xMm,
            a4Ymm: paperPoint.yMm,
            onPaper: paperPoint.onPaper,
            timestamp: clock,
          });
        }
      }
    });

    await webgazer.setCameraConstraints(getCameraConstraints());
    await webgazer
      .setRegression('ridge')
      .saveDataAcrossSessions(false)
      .begin();

    // 禁用默认鼠标校准（会引入偏差）
    disableWebGazerMouseCalibration();
    // 隐藏 WebGazer 自带的视频预览和红点
    webgazer.showVideoPreview(false).showPredictionPoints(false);

    // 将视频元素移出可视区域（但保持活跃以维持视频帧处理）
    setTimeout(hideWebGazerElements, 600);
    setTimeout(hideWebGazerElements, 1500); // 二次确保

    State.webgazerReady = true;
    State.activeCameraDeviceId = State.selectedCameraDeviceId;
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
  State.calibrationRecording = false;
  State.currentA4Plane = getCalibrationA4Plane();
  setElementToA4Plane(EL.calibPaperFrame, State.currentA4Plane);

  CALIB_POSITIONS.forEach((pos, i) => {
    const el = document.createElement('div');
    el.className = 'calib-point';
    el.id = `cp-${i}`;

    const paperPoint = a4ToVirtualScreen(pos, State.currentA4Plane);
    const px = paperPoint.x;
    const py = paperPoint.y;
    el.style.left = `${px}px`;
    el.style.top  = `${py}px`;

    el.innerHTML = `
      <div class="calib-point-ring"></div>
      <div class="calib-point-dot"></div>
      <div class="calib-check">✓</div>
      <div class="calib-point-index">${i + 1}</div>
      <div class="calib-point-progress">0/${CLICKS_PER_POINT}</div>
    `;

    const pointData = {
      el,
      x: px,
      y: py,
      a4X: pos.x,
      a4Y: pos.y,
      clicks: 0,
      done: false,
    };
    State.calibPoints.push(pointData);

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

async function resetWebGazerCalibrationData() {
  disableWebGazerMouseCalibration();

  try {
    localStorage.removeItem('webgazerGlobalData');
    localStorage.removeItem('webgazerGlobalSettings');
  } catch (_) {}

  try {
    if (typeof webgazer?.clearData === 'function') {
      await webgazer.clearData();
    }
  } catch (err) {
    console.warn('[EyeTrack] 清除旧校准数据失败:', err);
  }

  try {
    webgazer.saveDataAcrossSessions(false);
  } catch (_) {}

  disableWebGazerMouseCalibration();
}

async function recordWebGazerCalibrationSamples(point) {
  disableWebGazerMouseCalibration();

  for (let i = 0; i < CALIBRATION_SAMPLES_PER_CONFIRM; i++) {
    try {
      if (typeof webgazer.getCurrentPrediction === 'function') {
        await webgazer.getCurrentPrediction();
      }
      webgazer.recordScreenPosition(point.x, point.y, 'click');
    } catch (err) {
      console.warn('[EyeTrack] 校准样本记录失败:', err);
    }

    if (i < CALIBRATION_SAMPLES_PER_CONFIRM - 1) {
      await wait(CALIBRATION_SAMPLE_INTERVAL_MS);
    }
  }

  disableWebGazerMouseCalibration();
}

async function confirmCurrentCalibrationPoint() {
  await recordCalibrationPoint(State.currentCalibIndex);
}

async function recordCalibrationPoint(index) {
  if (index !== State.currentCalibIndex) return;
  const point = State.calibPoints[index];
  if (!point || point.done) return;
  if (State.calibrationRecording) return;

  State.calibrationRecording = true;
  try {
    await recordWebGazerCalibrationSamples(point);

    point.clicks++;

    // 闪烁动效
    point.el.classList.add('clicking');
    setTimeout(() => point.el.classList.remove('clicking'), 320);

    // 更新进度文字
    const prog = point.el.querySelector('.calib-point-progress');
    prog.textContent = `${point.clicks}/${CLICKS_PER_POINT}`;

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
  } finally {
    State.calibrationRecording = false;
  }
}

function handleCalibrationMouseConfirm(event) {
  if (!isCalibrationScreenActive()) return;
  if (event.button !== 0) return;
  if (event.target.matches('input, textarea, select, button, a')) return;

  event.preventDefault();
  event.stopImmediatePropagation();
  disableWebGazerMouseCalibration();
  confirmCurrentCalibrationPoint();
}

function handleCalibrationKeydown(event) {
  if (event.repeat) return;
  if (!isCalibrationScreenActive()) return;
  if (event.target.matches('input, textarea, select')) return;
  if (!CALIBRATION_KEYS.has(event.key) && event.code !== 'Numpad0') return;

  event.preventDefault();
  event.stopImmediatePropagation();
  disableWebGazerMouseCalibration();
  confirmCurrentCalibrationPoint();
}

function handlePreCalibrationStepKeydown(event) {
  if (event.repeat) return;
  if (event.key !== ' ' && event.code !== 'Space') return;
  if (event.target.matches('input, textarea, select, button, a')) return;

  if (isCameraSelectScreenActive()) {
    event.preventDefault();
    event.stopImmediatePropagation();
    handleCameraSelectContinue();
    return;
  }

  if (isCameraAdjustScreenActive()) {
    event.preventDefault();
    event.stopImmediatePropagation();
    beginCalibrationScreen();
  }
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
      setTrackStatus('status-pending', '请选择内置图片以开始追踪');
    }
  }, 1000);
}

// ─── 内置图片选择 ───────────────────────────────────────────────
function initializeBuiltinImages() {
  State.uploadedImages = BUILTIN_IMAGES.map(image => ({
    ...image,
    size: 0,
  }));
  selectImage(State.selectedImageId || State.uploadedImages[0]?.id);
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
    setTrackStatus('status-pending', `已选择「${image.name}」${image.conditionLabel}，请先完成校准`);
  }
}

function renderImageGallery() {
  EL.imageGallery.innerHTML = '';

  State.uploadedImages.forEach((image, index) => {
    const item = document.createElement('div');
    item.className = `image-thumb builtin-image-thumb${image.id === State.selectedImageId ? ' selected' : ''}`;
    item.tabIndex = 0;
    item.setAttribute('role', 'button');
    item.setAttribute('aria-label', `选择内置图片 ${index + 1}: ${image.name}，${image.conditionLabel}`);
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
    name.textContent = `${image.name} · ${image.conditionLabel}`;

    item.append(img, name);
    EL.imageGallery.appendChild(item);
  });
}

async function startCalibrationFromHome() {
  if (!EL.participantIdInput.value.trim()) {
    alert('请先输入参与者姓名。');
    EL.participantIdInput.focus();
    return;
  }

  await beginCameraSelectScreen();
}

async function beginCameraSelectScreen() {
  stopCameraAdjustmentPreview();
  stopCameraSelectPreview();
  showScreen(EL.cameraSelectScreen);
  await refreshCameraDevices();
}

async function handleCameraDeviceChange() {
  State.selectedCameraDeviceId = EL.cameraDeviceSelect.value;
  await startCameraSelectPreview(State.selectedCameraDeviceId);
}

async function handleCameraSelectContinue() {
  if (State.cameraSelectContinuing) return;
  State.selectedCameraDeviceId = EL.cameraDeviceSelect.value;
  if (!State.selectedCameraDeviceId) {
    alert('请先选择一个摄像头。');
    return;
  }

  State.cameraSelectContinuing = true;
  try {
    stopCameraSelectPreview();
    showModal(EL.loadingOverlay);
    EL.loadingStatus.textContent = '正在启用所选摄像头…';
    const ready = await initWebGazer();
    if (ready) beginCameraAdjustmentScreen();
  } finally {
    State.cameraSelectContinuing = false;
  }
}

function beginCameraAdjustmentScreen() {
  try { webgazer.resume(); } catch (_) {}
  EL.gazeCursor.classList.add('hidden');
  showScreen(EL.cameraAdjustScreen);
  syncCameraAdjustmentPreview();
  setTimeout(syncCameraAdjustmentPreview, 300);
  setTimeout(syncCameraAdjustmentPreview, 1000);
}

async function beginCalibrationScreen() {
  if (State.calibrationScreenStarting) return;
  State.calibrationScreenStarting = true;
  try {
    stopCameraAdjustmentPreview();
    try { webgazer.resume(); } catch (_) {}
    disableWebGazerMouseCalibration();
    showScreen(EL.calibScreen);
    EL.calibStatusText.textContent = '正在重置旧校准数据…';
    await resetWebGazerCalibrationData();
    EL.calibStatusText.textContent = '校准进行中';
    buildCalibrationPoints();
    EL.gazeCursor.classList.remove('hidden');
    disableWebGazerMouseCalibration();
  } finally {
    State.calibrationScreenStarting = false;
  }
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
  const sessionText = State.calibrationSession ? `${State.calibrationSession.label} · A4纸面校准 · 已记录 ${runCount} 次` : '已校准';
  setTrackStatus('status-active', `${sessionText} · ${name}可开始追踪`);
}

function prepareTrackingPaperPlane(imageSrc) {
  const plane = getActiveA4Plane();
  State.currentA4Plane = plane;
  setElementToA4Plane(EL.trackingPaperPlane, plane);
  EL.trackingImage.src = imageSrc;
  EL.gazeCursorTracking.classList.add('hidden');
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
    group: image.group,
    condition: image.condition,
    conditionLabel: image.conditionLabel,
  };
  State.currentReportRun = null;

  // WebGazer 在 begin() 后持续运行，这里只需恢复（如果暂停过）
  try { webgazer.resume(); } catch (_) {}

  prepareTrackingPaperPlane(State.uploadedImageSrc);
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
      group: image.group,
      condition: image.condition,
      conditionLabel: image.conditionLabel,
    },
    imageSrc: image.src,
    coordinateSystem: 'a4-landscape-paper',
    a4Plane: State.calibrationSession?.a4Plane ? { ...State.calibrationSession.a4Plane } : { ...getActiveA4Plane() },
    paperSizeMm: { ...A4_SIZE_MM },
    points: State.gazeHistory.map((point, index) => ({
      index: index + 1,
      x: point.x,
      y: point.y,
      a4X: point.a4X,
      a4Y: point.a4Y,
      a4Xmm: point.a4Xmm,
      a4Ymm: point.a4Ymm,
      onPaper: point.onPaper,
      timestamp: point.timestamp,
    })),
  };

  session.runs.push(run);
  State.currentReportRun = run;
  State.gazeHistory = run.points;
  State.uploadedImageSrc = run.imageSrc;
  State.archiveDirty = true;
  State.archiveUnloadPrompted = false;
  updateHomeDataSummary();
  return run;
}

function updateReportStats(run) {
  if (!run) {
    EL.statDuration.textContent = '0.0 s';
    EL.statPoints.textContent = '0';
    EL.statQuality.textContent = '—';
    EL.statQuality.style.color = '';
    EL.statFps.textContent = '— Hz';
    return;
  }

  const range = getReportTimeRange(run);
  const duration = Math.max(0, range.end - range.start);
  const pts = getFilteredReportPoints(run).length;
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

function getPointTimeSeconds(point, index, points, run) {
  const first = Number(points[0]?.timestamp);
  const current = Number(point.timestamp);
  if (Number.isFinite(first) && Number.isFinite(current)) {
    return Math.max(0, (current - first) / 1000);
  }

  if (run?.duration > 0 && points.length > 1) {
    return (index / (points.length - 1)) * run.duration;
  }

  return 0;
}

function getReportTimeRange(run = State.currentReportRun) {
  const duration = Math.max(0, Number(run?.duration) || 0);
  const startRaw = Number(EL.vizTimeStart.value);
  const endRaw = Number(EL.vizTimeEnd.value);
  const start = clamp01(duration ? (Number.isFinite(startRaw) ? startRaw / duration : 0) : 0) * duration;
  const end = EL.vizTimeEnd.value === '' || !Number.isFinite(endRaw)
    ? duration
    : clamp01(duration ? endRaw / duration : 0) * duration;

  return {
    start: Math.min(start, end),
    end: Math.max(start, end),
    duration,
  };
}

function getFilteredReportPoints(run = State.currentReportRun) {
  const points = run ? run.points : State.gazeHistory;
  if (!points.length) return [];

  const range = getReportTimeRange(run);
  return points.filter((point, index) => {
    const t = getPointTimeSeconds(point, index, points, run);
    return t >= range.start && t <= range.end;
  });
}

function updateReportRangeStatus(run = State.currentReportRun, count = null) {
  if (!EL.vizRangeStatus) return;
  if (!run) {
    EL.vizRangeStatus.textContent = '未选择记录';
    updateGazePlaybackControls();
    return;
  }

  const range = getReportTimeRange(run);
  const shown = count ?? getFilteredReportPoints(run).length;
  const total = run.points.length;
  const isFull = range.start <= 0 && range.end >= range.duration;
  EL.vizRangeStatus.textContent = isFull
    ? `显示全部 ${total} 点`
    : `${range.start.toFixed(1)}-${range.end.toFixed(1)} s · ${shown}/${total} 点`;
  updateGazePlaybackControls();
}

function resetReportTimeRange(run = State.currentReportRun) {
  if (!EL.vizTimeStart || !EL.vizTimeEnd) return;
  EL.vizTimeStart.value = '0';
  EL.vizTimeEnd.value = run?.duration ? run.duration.toFixed(1) : '';
}

function redrawCurrentVisualization() {
  if (EL.tabHeatmap.classList.contains('active')) drawHeatmap();
  else drawGazePlot();
}

function isGazePlotMode() {
  return EL.tabGazeplot?.classList.contains('active');
}

function getGazePlaybackPointCount(run = State.currentReportRun) {
  return getFilteredReportPoints(run).length;
}

function updateGazePlaybackControls() {
  if (!EL.gazePlaybackBtn) return;

  const canPlay = Boolean(
    State.currentReportRun &&
    isGazePlotMode() &&
    getGazePlaybackPointCount(State.currentReportRun) >= 2
  );
  EL.gazePlaybackBtn.disabled = !canPlay;
  EL.gazePlaybackBtn.textContent = State.gazePlaybackPlaying ? '停止回放' : '模拟回放';
}

function stopGazePlayback(redraw = false) {
  if (State.gazePlaybackFrameId != null) {
    cancelAnimationFrame(State.gazePlaybackFrameId);
  }
  State.gazePlaybackFrameId = null;
  State.gazePlaybackPlaying = false;
  State.gazePlaybackToken += 1;
  updateGazePlaybackControls();
  if (redraw && isGazePlotMode()) drawGazePlot();
}

function getGazePlaybackDurationMs(run = State.currentReportRun) {
  const range = getReportTimeRange(run);
  const span = Math.max(0.1, range.end - range.start || Number(run?.duration) || 0);
  return Math.max(1800, Math.min(12000, span * 350));
}

function startGazePlayback() {
  const run = State.currentReportRun;
  const pointCount = getGazePlaybackPointCount(run);
  if (!run || pointCount < 2) {
    alert('当前时间段的数据点不足，无法回放轨迹。');
    updateGazePlaybackControls();
    return;
  }

  if (!isGazePlotMode()) {
    EL.tabGazeplot.classList.add('active');
    EL.tabHeatmap.classList.remove('active');
  }

  State.gazePlaybackPlaying = true;
  State.gazePlaybackFrameId = null;
  State.gazePlaybackStartedAt = performance.now();
  State.gazePlaybackDurationMs = getGazePlaybackDurationMs(run);
  State.gazePlaybackToken += 1;
  const playbackToken = State.gazePlaybackToken;
  updateGazePlaybackControls();

  const tick = (now) => {
    if (!State.gazePlaybackPlaying || State.gazePlaybackToken !== playbackToken) return;
    const elapsed = now - State.gazePlaybackStartedAt;
    const progress = clamp01(elapsed / State.gazePlaybackDurationMs);

    drawGazePlot({
      playbackProgress: progress,
      playbackToken,
      onComplete: () => {
        if (!State.gazePlaybackPlaying || State.gazePlaybackToken !== playbackToken) return;
        if (progress >= 1) {
          State.gazePlaybackPlaying = false;
          State.gazePlaybackFrameId = null;
          updateGazePlaybackControls();
          return;
        }
        State.gazePlaybackFrameId = requestAnimationFrame(tick);
      },
    });
  };

  State.gazePlaybackFrameId = requestAnimationFrame(tick);
}

function toggleGazePlayback() {
  if (State.gazePlaybackPlaying) stopGazePlayback(true);
  else startGazePlayback();
}

function createReportCanvasForImage(canvas, img, useNaturalSize = false) {
  if (useNaturalSize) {
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    return;
  }

  const containerW = canvas.parentElement?.clientWidth || window.innerWidth;
  const scale = Math.min(
    containerW / img.naturalWidth,
    (window.innerHeight * 0.65) / img.naturalHeight,
    1
  );
  canvas.width  = Math.round(img.naturalWidth  * scale);
  canvas.height = Math.round(img.naturalHeight * scale);
}

function drawReportMessage(canvas, text, transparent = false) {
  const ctx = canvas.getContext('2d');
  if (!transparent) {
    ctx.fillStyle = 'rgba(255,255,255,0.5)';
    ctx.fillRect(0, 0, canvas.width || 1, canvas.height || 1);
  }
  ctx.fillStyle = transparent ? 'rgba(255,255,255,0.82)' : 'rgba(30,27,75,0.72)';
  ctx.font = '16px Inter, sans-serif';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(text, (canvas.width || 1) / 2, (canvas.height || 1) / 2);
}

function handleReportImageError(canvas, options, run, message = '无法加载背景图像') {
  canvas.width = canvas.width || 800;
  canvas.height = canvas.height || 566;
  if (!options.silentEmpty) {
    drawReportMessage(canvas, message, !State.reportShowBackground);
  }
  updateReportRangeStatus(run, 0);
  options.onError?.(new Error(message));
  options.onComplete?.(canvas);
}

function legacyScreenToCanvasMapper(canvas, img) {
  const sw = window.innerWidth, sh = window.innerHeight;
  const ia = img.naturalWidth / img.naturalHeight;
  const sa = sw / sh;
  let dw, dh;
  if (ia > sa) { dw = sw; dh = sw / ia; }
  else         { dh = sh; dw = sh * ia; }
  const ox = (sw - dw) / 2;
  const oy = (sh - dh) / 2;

  return point => ({
    x: ((point.x - ox) / dw) * canvas.width,
    y: ((point.y - oy) / dh) * canvas.height,
  });
}

function a4PointToCanvas(point, canvas, run) {
  const plane = run?.a4Plane || State.calibrationSession?.a4Plane || State.currentA4Plane;
  if (!['a4-paper', 'a4-landscape-paper'].includes(run?.coordinateSystem) || !plane) return null;
  const paperPoint = Number.isFinite(point.a4X) && Number.isFinite(point.a4Y)
    ? { x: point.a4X, y: point.a4Y }
    : virtualScreenToA4(point.x, point.y, plane);

  return {
    x: clamp01(paperPoint.x) * canvas.width,
    y: clamp01(paperPoint.y) * canvas.height,
  };
}

function createPointToCanvasMapper(canvas, img, run) {
  if (['a4-paper', 'a4-landscape-paper'].includes(run?.coordinateSystem)) {
    return point => a4PointToCanvas(point, canvas, run);
  }
  return legacyScreenToCanvasMapper(canvas, img);
}

// ─── 热力图（Canvas 原生实现）───────────────────────────────────
function drawHeatmap(options = {}) {
  const canvas = options.canvas || EL.reportCanvas;
  const run = options.run || State.currentReportRun;
  const data = options.data || getFilteredReportPoints(run);
  const imageSrc = run ? run.imageSrc : State.uploadedImageSrc;
  const includeBackground = options.includeBackground ?? State.reportShowBackground;
  const includeLegend = options.includeLegend ?? includeBackground;
  if (!imageSrc) {
    handleReportImageError(canvas, options, run, '没有可用的背景图像');
    return;
  }

  const img    = new Image();
  img.onerror = () => handleReportImageError(canvas, options, run);
  img.onload   = () => {
    createReportCanvasForImage(canvas, img, options.useNaturalSize);

    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (includeBackground) {
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    }

    if (data.length < 3) {
      if (!options.silentEmpty) {
        drawReportMessage(canvas, '当前时间段数据点不足', !includeBackground);
      }
      updateReportRangeStatus(run, data.length);
      options.onComplete?.(canvas);
      return;
    }

    const mapPoint = createPointToCanvasMapper(canvas, img, run);

    // 生成密度图（离屏 canvas）。单点权重随采样量降低，避免高频采样过早堆满红色。
    const tmp    = document.createElement('canvas');
    tmp.width    = canvas.width;
    tmp.height   = canvas.height;
    const tc     = tmp.getContext('2d');
    tc.globalCompositeOperation = 'lighter';
    const maxRadius = options.useNaturalSize ? 140 : 52;
    const radius = Math.max(22, Math.min(maxRadius, Math.min(canvas.width, canvas.height) * 0.055));
    const pointWeight = Math.max(0.018, Math.min(0.085, 0.75 / Math.sqrt(data.length)));

    data.forEach(pt => {
      const mapped = mapPoint(pt);
      if (!mapped) return;
      const cx = mapped.x, cy = mapped.y;
      if (cx < -radius || cx > canvas.width  + radius) return;
      if (cy < -radius || cy > canvas.height + radius) return;
      const g = tc.createRadialGradient(cx, cy, 0, cx, cy, radius);
      g.addColorStop(0.00, `rgba(0,0,0,${pointWeight})`);
      g.addColorStop(0.35, `rgba(0,0,0,${pointWeight * 0.52})`);
      g.addColorStop(1, 'rgba(0,0,0,0)');
      tc.beginPath();
      tc.fillStyle = g;
      tc.arc(cx, cy, radius, 0, Math.PI * 2);
      tc.fill();
    });

    // 颜色映射：alpha → 蓝绿黄橙红。红色只保留给最高密度的少量区域。
    const gc  = document.createElement('canvas');
    gc.width  = 256; gc.height = 1;
    const gx  = gc.getContext('2d');
    const lg  = gx.createLinearGradient(0, 0, 256, 0);
    lg.addColorStop(0.00, '#2563EB');
    lg.addColorStop(0.25, '#0891B2');
    lg.addColorStop(0.45, '#22C55E');
    lg.addColorStop(0.68, '#84CC16');
    lg.addColorStop(0.84, '#FACC15');
    lg.addColorStop(0.94, '#FB923C');
    lg.addColorStop(1.00, '#DC2626');
    gx.fillStyle = lg;
    gx.fillRect(0, 0, 256, 1);
    const gd = gx.getImageData(0, 0, 256, 1).data;

    const heat = tc.getImageData(0, 0, canvas.width, canvas.height);
    const px   = heat.data;
    const histogram = new Uint32Array(256);
    let positiveCount = 0;

    for (let i = 0; i < px.length; i += 4) {
      const a = px[i + 3];
      if (a > 0) {
        histogram[a]++;
        positiveCount++;
      }
    }

    const percentileAlpha = (percentile) => {
      if (!positiveCount) return 1;
      const target = Math.max(1, Math.ceil(positiveCount * percentile));
      let seen = 0;
      for (let alpha = 0; alpha < histogram.length; alpha++) {
        seen += histogram[alpha];
        if (seen >= target) return alpha;
      }
      return 255;
    };

    const normAlpha = Math.max(28, percentileAlpha(0.997));

    for (let i = 0; i < px.length; i += 4) {
      const a = px[i + 3];
      if (a > 0) {
        const normalized = Math.min(1, a / normAlpha);
        const intensity = Math.pow(normalized, 1.35);
        const ci = Math.min(255, Math.floor(intensity * 255)) * 4;
        px[i]     = gd[ci];
        px[i + 1] = gd[ci + 1];
        px[i + 2] = gd[ci + 2];
        px[i + 3] = intensity < 0.035
          ? 0
          : Math.min(205, 22 + Math.pow(intensity, 0.85) * 170);
      }
    }
    tc.putImageData(heat, 0, 0);
    ctx.drawImage(tmp, 0, 0);
    if (includeLegend) drawLegend(ctx, canvas.width, canvas.height);
    updateReportRangeStatus(run, data.length);
    options.onComplete?.(canvas);
  };
  img.src = imageSrc;
}

// ─── 视线轨迹图 ────────────────────────────────────────────────
function drawGazePlot(options = {}) {
  const canvas = options.canvas || EL.reportCanvas;
  const run = options.run || State.currentReportRun;
  const data = options.data || getFilteredReportPoints(run);
  const imageSrc = run ? run.imageSrc : State.uploadedImageSrc;
  const includeBackground = options.includeBackground ?? State.reportShowBackground;
  if (!imageSrc) {
    handleReportImageError(canvas, options, run, '没有可用的背景图像');
    return;
  }

  const img  = new Image();
  img.onerror = () => handleReportImageError(canvas, options, run);
  img.onload = () => {
    if (options.playbackToken && options.playbackToken !== State.gazePlaybackToken) return;
    createReportCanvasForImage(canvas, img, options.useNaturalSize);

    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (includeBackground) {
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    }

    if (data.length < 2) {
      if (!options.silentEmpty) {
        drawReportMessage(canvas, '当前时间段数据点不足', !includeBackground);
      }
      updateReportRangeStatus(run, data.length);
      options.onComplete?.(canvas);
      return;
    }

    const mapPoint = createPointToCanvasMapper(canvas, img, run);

    // 降采样（最多 350 点）
    const step    = Math.max(1, Math.floor(data.length / 350));
    const sampled = data.filter((_, i) => i % step === 0);
    const pts     = sampled.map(mapPoint).filter(Boolean);
    const playbackProgress = Number.isFinite(options.playbackProgress)
      ? clamp01(options.playbackProgress)
      : null;
    const isPlaybackFrame = playbackProgress !== null;
    if (pts.length < 2) {
      if (!options.silentEmpty) {
        drawReportMessage(canvas, '纸面有效数据点不足', !includeBackground);
      }
      updateReportRangeStatus(run, data.length);
      options.onComplete?.(canvas);
      return;
    }

    const visibleCount = isPlaybackFrame
      ? Math.max(1, Math.min(pts.length, Math.ceil(pts.length * playbackProgress)))
      : pts.length;
    const drawPts = pts.slice(0, visibleCount);

    // 连线
    if (drawPts.length > 1) {
      ctx.beginPath();
      ctx.moveTo(drawPts[0].x, drawPts[0].y);
      drawPts.forEach(p => ctx.lineTo(p.x, p.y));
      ctx.strokeStyle = 'rgba(96,165,250,0.5)';
      ctx.lineWidth   = Math.max(1.5, canvas.width * 0.002);
      ctx.lineCap     = 'round';
      ctx.lineJoin    = 'round';
      ctx.stroke();
    }

    // 注视点
    const labelEvery = Math.max(1, Math.floor(drawPts.length / 18));
    drawPts.forEach((p, i) => {
      const prog    = i / Math.max(1, pts.length - 1);
      const r       = (3 + prog * 5) * (canvas.width / 900);
      const opacity = 0.35 + prog * 0.65;

      ctx.beginPath();
      ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
      ctx.fillStyle   = `rgba(96,165,250,${opacity})`;
      ctx.fill();
      ctx.strokeStyle = 'rgba(255,255,255,0.75)';
      ctx.lineWidth   = 1;
      ctx.stroke();

      if (i % labelEvery === 0 || i === 0 || i === drawPts.length - 1) {
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
    if (!isPlaybackFrame || playbackProgress >= 1) {
      drawMarker(pts[pts.length - 1], 'rgba(248,113,113,0.92)', 'E');
    } else {
      const current = drawPts[drawPts.length - 1];
      ctx.beginPath();
      ctx.arc(current.x, current.y, Math.max(10, canvas.width * 0.011), 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(251,191,36,0.95)';
      ctx.lineWidth = Math.max(2, canvas.width * 0.003);
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(current.x, current.y, Math.max(4, canvas.width * 0.005), 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(251,191,36,0.96)';
      ctx.fill();
    }
    updateReportRangeStatus(run, data.length);
    options.onComplete?.(canvas);
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
  g.addColorStop(0.00, 'rgba(37,99,235,0.65)');
  g.addColorStop(0.45, 'rgba(34,197,94,0.72)');
  g.addColorStop(0.84, 'rgba(250,204,21,0.84)');
  g.addColorStop(0.94, 'rgba(251,146,60,0.9)');
  g.addColorStop(1.00, 'rgba(220,38,38,0.94)');
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

function downloadCanvasPng(filename, canvas) {
  canvas.toBlob(blob => {
    if (!blob) {
      alert('无法导出图层，请稍后重试。');
      return;
    }
    const url = URL.createObjectURL(blob);
    const a = Object.assign(document.createElement('a'), { href: url, download: filename });
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }, 'image/png');
}

function getCurrentVizMode() {
  return EL.tabHeatmap.classList.contains('active') ? 'heatmap' : 'gazeplot';
}

function renderTransparentLayer(mode, run, data) {
  return new Promise((resolve, reject) => {
    const canvas = document.createElement('canvas');
    const options = {
      canvas,
      run,
      data,
      includeBackground: false,
      includeLegend: false,
      useNaturalSize: true,
      silentEmpty: true,
      onError: reject,
      onComplete: () => resolve(canvas),
    };
    if (mode === 'heatmap') drawHeatmap(options);
    else drawGazePlot(options);
  });
}

async function exportTransparentVizLayer() {
  const run = State.currentReportRun;
  if (!run) {
    alert('请先选择一次追踪记录。');
    return;
  }

  const mode = getCurrentVizMode();
  const data = getFilteredReportPoints(run);
  const minPoints = mode === 'heatmap' ? 3 : 2;
  if (data.length < minPoints) {
    alert('当前时间段的数据点不足，无法导出图层。');
    return;
  }

  const range = getReportTimeRange(run);
  const modeLabel = mode === 'heatmap' ? 'heatmap' : 'gazeplot';
  const filename = [
    'eye_tracking',
    modeLabel,
    'transparent',
    safeFileName(run.image.name),
    `${range.start.toFixed(1)}-${range.end.toFixed(1)}s`,
  ].join('_') + '.png';

  try {
    const canvas = await renderTransparentLayer(mode, run, data);
    downloadCanvasPng(filename, canvas);
  } catch (err) {
    alert(`无法导出图层：${err.message}`);
  }
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
    'image_group',
    'image_condition',
    'image_condition_label',
    'trial_started_at',
    'trial_ended_at',
    'trial_duration_seconds',
    'coordinate_system',
    'point_index',
    'virtual_x',
    'virtual_y',
    'a4_x_norm',
    'a4_y_norm',
    'a4_x_mm',
    'a4_y_mm',
    'on_a4_paper',
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
        run.image.group || '',
        run.image.condition || '',
        run.image.conditionLabel || '',
        run.startedAt,
        run.endedAt,
        run.duration.toFixed(3),
        run.coordinateSystem || 'screen',
        point.index,
        Math.round(point.x),
        Math.round(point.y),
        point.a4X == null ? '' : Number(point.a4X).toFixed(5),
        point.a4Y == null ? '' : Number(point.a4Y).toFixed(5),
        point.a4Xmm == null ? '' : Number(point.a4Xmm).toFixed(2),
        point.a4Ymm == null ? '' : Number(point.a4Ymm).toFixed(2),
        point.onPaper == null ? '' : String(Boolean(point.onPaper)),
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
  const exportedAt = new Date();
  const archive = {
    schema: 'visual-analytics-eye-archive',
    version: 1,
    exportedAt: exportedAt.toISOString(),
    calibrationSessionSeq: State.calibrationSessionSeq,
    sessions: State.calibrationSessions,
  };

  downloadBlob(
    getArchiveFilename(exportedAt),
    JSON.stringify(archive, null, 2),
    'application/json;charset=utf-8;'
  );
  State.archiveDirty = false;
  State.archiveUnloadPrompted = false;
}

function getArchiveFilename(date = new Date()) {
  const participantName = getArchiveParticipantName();
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  return `${safeFileName(participantName)}-${hours}.${minutes}-visual analytics.json`;
}

function getArchiveParticipantName() {
  const currentRecord = findRunRecord(State.currentReportRun);
  return currentRecord?.session?.label
    || getCurrentHomeSession()?.label
    || State.calibrationSessions[State.calibrationSessions.length - 1]?.label
    || '未命名参与者';
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
      coordinateSystem: session.coordinateSystem || 'screen',
      a4Plane: normalizeA4Plane(session.a4Plane),
      paperSizeMm: normalizePaperSize(session.paperSizeMm),
      runs: (Array.isArray(session.runs) ? session.runs : []).map((run, runIndex) => ({
        id: String(run.id || `trial-${runIndex + 1}`),
        startedAt: run.startedAt || '',
        endedAt: run.endedAt || '',
        duration: Number(run.duration) || 0,
        image: {
          id: String(run.image?.id || `image-${runIndex + 1}`),
          name: String(run.image?.name || `image-${runIndex + 1}`),
          size: Number(run.image?.size) || 0,
          group: run.image?.group ? String(run.image.group) : '',
          condition: run.image?.condition ? String(run.image.condition) : '',
          conditionLabel: run.image?.conditionLabel ? String(run.image.conditionLabel) : '',
        },
        imageSrc: run.imageSrc || '',
        coordinateSystem: run.coordinateSystem || session.coordinateSystem || 'screen',
        a4Plane: normalizeA4Plane(run.a4Plane || session.a4Plane),
        paperSizeMm: normalizePaperSize(run.paperSizeMm || session.paperSizeMm),
        points: (Array.isArray(run.points) ? run.points : []).map((point, pointIndex) => ({
          index: Number(point.index) || pointIndex + 1,
          x: Number(point.x) || 0,
          y: Number(point.y) || 0,
          a4X: point.a4X == null ? undefined : clamp01(Number(point.a4X) || 0),
          a4Y: point.a4Y == null ? undefined : clamp01(Number(point.a4Y) || 0),
          a4Xmm: point.a4Xmm == null ? undefined : Number(point.a4Xmm) || 0,
          a4Ymm: point.a4Ymm == null ? undefined : Number(point.a4Ymm) || 0,
          onPaper: point.onPaper == null ? undefined : Boolean(point.onPaper),
          timestamp: point.timestamp ?? '',
        })),
      })),
    };
  });
}

function normalizeA4Plane(plane) {
  if (!plane || typeof plane !== 'object') return null;
  const width = Number(plane.width);
  const height = Number(plane.height);
  if (!width || !height) return null;
  return {
    left: Number(plane.left) || 0,
    top: Number(plane.top) || 0,
    width,
    height,
    paperWidthMm: Number(plane.paperWidthMm) || A4_SIZE_MM.width,
    paperHeightMm: Number(plane.paperHeightMm) || A4_SIZE_MM.height,
  };
}

function normalizePaperSize(size) {
  return {
    width: Number(size?.width) || A4_SIZE_MM.width,
    height: Number(size?.height) || A4_SIZE_MM.height,
  };
}

function safeFileName(value) {
  return String(value || 'trial').replace(/[\\/:*?"<>|]/g, '_').slice(0, 60);
}

function shouldPromptBeforeUnload() {
  return State.archiveDirty && !State.archiveUnloadPrompted && getAllTrackingRuns().length > 0;
}

function handleBeforeUnload(event) {
  if (!shouldPromptBeforeUnload()) return;
  State.archiveUnloadPrompted = true;
  event.preventDefault();
  event.returnValue = '当前追踪数据可能尚未导出存档，请确认是否已经存档。';
  return event.returnValue;
}

// ─── 事件绑定 ──────────────────────────────────────────────────
function bindEvents() {
  // 重试按钮
  EL.retryInitBtn.addEventListener('click', () => {
    hideModal(EL.errorModal);
    beginCameraSelectScreen();
  });

  // 校准
  EL.startCalibBtn.addEventListener('click', startCalibrationFromHome);
  EL.cameraDeviceSelect.addEventListener('change', handleCameraDeviceChange);
  EL.cameraRefreshBtn.addEventListener('click', refreshCameraDevices);
  EL.cameraSelectContinueBtn.addEventListener('click', handleCameraSelectContinue);
  EL.cameraSelectBackBtn.addEventListener('click', () => {
    stopCameraSelectPreview();
    updateHomeDataSummary();
    showScreen(EL.homeScreen);
  });
  EL.cameraAdjustContinueBtn.addEventListener('click', beginCalibrationScreen);
  EL.cameraAdjustBackBtn.addEventListener('click', () => {
    stopCameraAdjustmentPreview();
    updateHomeDataSummary();
    showScreen(EL.homeScreen);
  });

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
  document.addEventListener('keydown', handlePreCalibrationStepKeydown);
  document.addEventListener('keydown', handleCalibrationKeydown);
  // 校准页鼠标左键确认当前活动点，不读取鼠标位置。
  document.addEventListener('click', handleCalibrationMouseConfirm, true);
  // 校准页彻底隔离鼠标移动，避免 WebGazer 默认 move 训练样本污染模型。
  ['mousemove', 'pointermove', 'mouseover', 'mouseout', 'mouseenter', 'mouseleave']
    .forEach(type => document.addEventListener(type, blockCalibrationMouseMove, true));

  // 报告标签
  EL.tabHeatmap.addEventListener('click', () => {
    stopGazePlayback(false);
    EL.tabHeatmap.classList.add('active');
    EL.tabGazeplot.classList.remove('active');
    drawHeatmap();
    updateGazePlaybackControls();
  });
  EL.tabGazeplot.addEventListener('click', () => {
    EL.tabGazeplot.classList.add('active');
    EL.tabHeatmap.classList.remove('active');
    drawGazePlot();
    updateGazePlaybackControls();
  });

  EL.vizBackgroundToggle.addEventListener('change', () => {
    State.reportShowBackground = EL.vizBackgroundToggle.checked;
    redrawCurrentVisualization();
  });
  [EL.vizTimeStart, EL.vizTimeEnd].forEach(input => {
    input.addEventListener('input', () => {
      stopGazePlayback(false);
      updateReportStats(State.currentReportRun);
      redrawCurrentVisualization();
    });
  });
  EL.vizTimeResetBtn.addEventListener('click', () => {
    stopGazePlayback(false);
    resetReportTimeRange(State.currentReportRun);
    updateReportStats(State.currentReportRun);
    redrawCurrentVisualization();
  });
  EL.gazePlaybackBtn.addEventListener('click', toggleGazePlayback);
  EL.exportVizLayerBtn.addEventListener('click', exportTransparentVizLayer);

  // 返回首页
  EL.backHomeBtn.addEventListener('click', () => {
    stopGazePlayback(false);
    updateHomeDataSummary();
    showScreen(EL.homeScreen);
  });

  // 导出
  EL.importArchiveBtn.addEventListener('click', () => EL.importArchiveInput.click());
  EL.importArchiveInput.addEventListener('change', e => importArchiveFile(e.target.files[0]));
  EL.exportArchiveBtn.addEventListener('click', exportArchive);
  EL.exportSelectedDataBtn.addEventListener('click', exportSelectedCSV);
  EL.exportDataBtn.addEventListener('click', exportCSV);
  EL.exportPdfBtn.addEventListener('click',  () => window.print());

  // 窗口缩放时重绘报告
  window.addEventListener('resize', () => {
    if (EL.reportScreen.classList.contains('hidden')) return;
    if (!State.currentReportRun) return;
    stopGazePlayback(false);
    if (EL.tabHeatmap.classList.contains('active')) drawHeatmap();
    else drawGazePlot();
  });
  window.addEventListener('beforeunload', handleBeforeUnload);
}

// ─── 入口 ─────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  // 默认直接进入主界面；只有开始校准时才请求摄像头权限。
  hideModal(EL.loadingOverlay);
  hideModal(EL.errorModal);
  showScreen(EL.homeScreen);
  initializeBuiltinImages();
  updateHomeDataSummary();

  bindEvents();
});
