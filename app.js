/* ============================================================
   app.js — 眼动追踪工具核心逻辑（真实摄像头版本）
   绝对不使用任何鼠标模拟 / 降级模式。
   WebGazer 初始化失败 → 显示错误弹窗，禁止继续操作。
============================================================ */

'use strict';

// ─── 多语言支持 ────────────────────────────────────────────────
const LANGUAGE_STORAGE_KEY = 'signVisualAttentionLanguage';
const SUPPORTED_LANGUAGES = new Set(['zh-CN', 'en', 'ja']);
const I18N_TEXT = {
  en: {
    '语言': 'Language',
    'SIGN Visual Attention v3 是面向标识视觉注意力研究的浏览器眼动追踪与分析工具。': 'SIGN Visual Attention v3 is a browser-based eye-tracking and analysis tool for sign-oriented visual attention research.',
    '基于浏览器的实时眼动追踪工具，无需专业设备，利用摄像头即可进行眼动数据采集、热力图与视线轨迹分析。': 'A browser-based real-time eye-tracking tool that uses a camera for gaze data collection, heatmaps, and gaze-trajectory analysis without specialized hardware.',
    'SIGN Visual Attention v3 · 基于浏览器的实时眼动追踪系统': 'SIGN Visual Attention v3 · Browser-Based Real-Time Eye-Tracking System',
    '正在初始化眼动追踪引擎': 'Initializing eye-tracking engine',
    '正在加载 WebGazer.js 并请求摄像头权限…': 'Loading WebGazer.js and requesting camera permission...',
    '眼动追踪初始化失败': 'Eye-tracking initialization failed',
    '无法启动眼动追踪引擎。': 'Unable to start the eye-tracking engine.',
    '请确认已允许浏览器访问摄像头': 'Confirm that camera access is allowed in the browser.',
    '请使用 Chrome / Edge 等现代浏览器': 'Use a modern browser such as Chrome or Edge.',
    '页面需通过 HTTPS 或 localhost 访问': 'Open this page through HTTPS or localhost.',
    '请确保环境光线充足、面部正对摄像头': 'Keep the face centered and the lighting sufficient.',
    '重试初始化': 'Retry Initialization',
    '摄像头选择': 'Camera Selection',
    '流畅摄像头选择': 'Smooth Camera Selection',
    '选择用于眼动追踪的摄像头': 'Select the camera for eye tracking',
    '正在读取摄像头列表…': 'Reading camera list...',
    '视频输入设备': 'Video Input Device',
    '刷新列表': 'Refresh List',
    '返回首页': 'Back Home',
    '使用此摄像头（Space）': 'Use This Camera (Space)',
    '校准前检查': 'Pre-Calibration Check',
    '调整摄像头至眼部位置': 'Align the camera to eye level',
    '正在读取摄像头画面…': 'Reading camera preview...',
    '进入九点校准（Space）': 'Start 9-Point Calibration (Space)',
    '校准进行中': 'Calibration in progress',
    '参与者注视打印校准纸上的当前编号点；操作员按 Space / Enter / 0，或单击鼠标左键确认当前点 3 次': 'The participant looks at the numbered point on the printed calibration sheet; the operator presses Space / Enter / 0 or left-clicks to confirm each point 3 times.',
    '打印标识校准映射': 'Printed Sign Calibration Map',
    '打印标识追踪': 'Printed Sign Tracking',
    '请让参与者观看打印出来的标识': 'Ask the participant to view the printed sign.',
    '屏幕仅用于操作员监看。系统会把视线估计映射到打印标识坐标，再叠加到报告图像上。': 'The screen is for operator monitoring only. Gaze estimates are mapped to printed-sign coordinates and overlaid on the report image.',
    '正在记录打印标识视线坐标...': 'Recording printed-sign gaze coordinates...',
    '结束追踪': 'Stop Tracking',
    '分析页面切换': 'Analysis page switcher',
    '聚合数据分析': 'Aggregate Data Analysis',
    '内置图片选择': 'Built-in image selection',
    '图片选择': 'Image selection',
    '请输入参与者姓名': 'Enter participant name',
    '分析报告': 'Analysis Report',
    '导出存档': 'Export Archive',
    '单个数据分析': 'Single-Run Analysis',
    '整体数据分析': 'Overall Analysis',
    '参与者': 'Participants',
    '追踪记录': 'Tracking Records',
    '当前回顾': 'Current Review',
    '未选择': 'Not selected',
    '导入存档或完成追踪后，可在这里选择并回顾单次数据。': 'After importing an archive or completing tracking, select and review each run here.',
    '当前时段': 'Current Interval',
    '当前点数': 'Current Points',
    '关注质量': 'Attention Quality',
    '采样频率': 'Sampling Frequency',
    '聚合分析': 'Aggregate Analysis',
    '当前没有可分析的数据。': 'No analyzable data is currently available.',
    '范围': 'Scope',
    '全部数据': 'All Data',
    '当前参与者': 'Current Participant',
    '当前记录': 'Current Record',
    '图片': 'Image',
    '全部图片': 'All Images',
    '条件对比': 'Condition Comparison',
    '条件': 'Condition',
    '记录': 'Records',
    '点数': 'Points',
    '有效率': 'Valid Rate',
    '平均时长': 'Mean Duration',
    '中心偏移': 'Center Bias',
    '图片对比': 'Image Comparison',
    '平均 X/Y': 'Mean X/Y',
    '路径长度': 'Path Length',
    '打印区域分布': 'Printed Region Distribution',
    '异常筛查': 'Anomaly Screening',
    '技术异常': 'Technical Anomaly',
    '覆盖': 'Coverage',
    '偏移': 'Bias',
    '建议': 'Suggestion',
    '自动摘要': 'Automated Summary',
    '导出分析 CSV': 'Export Analysis CSV',
    '导出分析 JSON': 'Export Analysis JSON',
    '导出整体分析图': 'Export Overall Figure',
    '热力图': 'Heatmap',
    '视线轨迹图': 'Gaze Plot',
    '叠加背景图': 'Overlay Background',
    '开始': 'Start',
    '结束': 'End',
    '重置': 'Reset',
    '显示全部数据': 'Show all data',
    '坐标修正': 'Coordinate Correction',
    '原始': 'Raw',
    '中心平移': 'Center Shift',
    '范围拉伸': 'Range Stretch',
    '手动修正': 'Manual Correction',
    '自动': 'Auto',
    '模拟回放': 'Replay',
    '停止回放': 'Stop Replay',
    '导出透明图层': 'Export Transparent Layer',
    '导出学术图片': 'Export Academic Figure',
    '工具': 'Tool',
    '移动/变换': 'Move / Transform',
    '涂抹异常点': 'Brush Outliers',
    '恢复涂抹点': 'Restore Brushed Points',
    '涂抹半径': 'Brush Radius',
    '偏移 0 / 0 · 缩放 1.00 / 1.00': 'Offset 0 / 0 · Scale 1.00 / 1.00',
    '已涂抹 0 点': 'Brushed 0 points',
    '重置手动修正': 'Reset Manual Correction',
    '另存为修正版': 'Save as Corrected Version',
    '导入存档文件': 'Import Archive File',
    '导入 data523 文件夹': 'Import data523 Folder',
    '导出单次数据': 'Export Selected Run',
    '导出全部数据': 'Export All Data',
    '导出 PDF': 'Export PDF',
    '基于浏览器 · 本地处理 · 隐私保护': 'Browser-based · Local processing · Privacy preserving',
    '实时眼动追踪系统': 'Real-Time Eye-Tracking System',
    '利用视觉追踪技术': 'Use Visual Tracking Technology',
    '了解标识的注意力分布': 'Understand Sign Attention Distribution',
    '面向通用打印标识的眼动追踪实验：参与者观看纸面内容，系统用摄像头记录并映射打印标识视线坐标。 采用 WebGazer.js 驱动，支持热力图与视线轨迹双重可视化分析。': 'An eye-tracking experiment for general printed signs: participants view printed content while the system records and maps gaze coordinates through the camera. Powered by WebGazer.js, with both heatmap and gaze-trajectory analysis.',
    '摄像头校准': 'Camera Calibration',
    '先选择用于眼动追踪的摄像头，再通过预览调整眼部位置，并让参与者依次注视打印校准纸上的 9 个点。 操作员按 Space、Enter、0 或单击鼠标左键确认当前点，每点 3 次。': 'Select the tracking camera, align eye position in the preview, then ask the participant to look at the 9 points on the printed calibration sheet. The operator confirms each point 3 times with Space, Enter, 0, or a left click.',
    '参与者姓名': 'Participant Name',
    '摄像头预览': 'Camera Preview',
    '通用打印映射': 'General Print Mapping',
    '未校准': 'Not Calibrated',
    '开始校准': 'Start Calibration',
    '选择图片并追踪': 'Select Image and Track',
    '从 a1、a2、b1、b2 四张内置标识中选择，或载入外部图片。a1/b1 为对照组，a2/b2 为实验组。': 'Choose one of the four built-in signs, a1, a2, b1, and b2, or load an external image. a1/b1 are control stimuli; a2/b2 are experimental stimuli.',
    '载入外部图片': 'Load External Image',
    '外部图片': 'External Image',
    '对照组 a1/b1': 'Control a1/b1',
    '实验组 a2/b2': 'Experimental a2/b2',
    '实时视线光标': 'Live Gaze Cursor',
    '请先完成校准': 'Complete calibration first',
    '开始追踪': 'Start Tracking',
    '数据回顾与存档': 'Data Review and Archive',
    '回顾参与者的所有图片追踪记录，查看热力图与轨迹图，导出单次数据、全部数据或完整存档。': 'Review all image-tracking records, inspect heatmaps and gaze plots, and export selected runs, all data, or the complete archive.',
    '单次导出': 'Selected Export',
    '全部导出': 'Full Export',
    '存档导入': 'Archive Import',
    '无需摄像头即可回顾': 'Review without camera',
    '导入存档': 'Import Archive',
    '打开回顾': 'Open Review',
    'SIGN Visual Attention v3 · 基于浏览器的实时眼动追踪系统 · 本地处理，保护隐私': 'SIGN Visual Attention v3 · Browser-Based Real-Time Eye-Tracking System · Local processing, privacy preserving',
    '还没有参与者数据。可先完成追踪，或导入参与者存档。': 'No participant data yet. Complete tracking or import a participant archive.',
    '请选择参与者。': 'Select a participant.',
    '该参与者还没有完成任何图片追踪。': 'This participant has not completed any image tracking yet.',
    '完成一次图片追踪后，记录会出现在这里。': 'After an image-tracking run is completed, the record will appear here.',
    '未知时间': 'Unknown time',
    '摄像头已关闭，请重新校准后开始追踪': 'The camera is closed. Recalibrate before tracking.',
    '请选择图像并重新校准': 'Select an image and recalibrate.',
    '选择摄像头并校准': 'Select Camera and Calibrate',
    '所选摄像头': 'Selected camera',
    '您的浏览器不支持摄像头选择': 'Your browser does not support camera selection.',
    '正在请求摄像头权限…': 'Requesting camera permission...',
    '未检测到可用摄像头': 'No available camera detected',
    '无法读取摄像头列表': 'Unable to read the camera list',
    '无法预览所选摄像头': 'Unable to preview the selected camera',
    '摄像头访问失败': 'Camera access failed',
    '您拒绝了摄像头权限。请在浏览器地址栏点击摄像头图标，允许访问后再重试。': 'Camera permission was denied. Click the camera icon in the browser address bar, allow access, and retry.',
    '未检测到摄像头设备，请确认摄像头已连接并正常工作。': 'No camera device was detected. Confirm that the camera is connected and working.',
    '摄像头被其他应用占用，请关闭其他使用摄像头的程序后重试。': 'The camera is being used by another application. Close other camera apps and retry.',
    '所选摄像头无法按当前配置启动，请选择其他摄像头。': 'The selected camera cannot start with the current configuration. Choose another camera.',
    '摄像头画面尚未就绪，请稍候…': 'Camera preview is not ready yet. Please wait...',
    '请点击预览区域或继续按钮以激活摄像头画面': 'Click the preview area or continue button to activate the camera preview.',
    '请让双眼位于画面中央，并保持面部清晰可见': 'Keep both eyes centered in the frame and the face clearly visible.',
    '无法加载 WebGazer.js 眼动追踪引擎': 'Unable to load the WebGazer.js eye-tracking engine',
    '您的浏览器不支持摄像头访问': 'Your browser does not support camera access',
    '正在启用摄像头…': 'Enabling camera...',
    '摄像头访问被拒绝，无法启动眼动追踪': 'Camera access was denied, so eye tracking cannot start',
    '正在初始化眼动追踪模型，请稍候…': 'Initializing the eye-tracking model. Please wait...',
    '眼动追踪引擎启动失败，请确认摄像头正常并重试。': 'The eye-tracking engine failed to start. Confirm that the camera works and retry.',
    '正在重置旧校准数据…': 'Resetting previous calibration data...',
    '校准完成！': 'Calibration complete!',
    '重新校准': 'Recalibrate',
    '请选择图片以开始追踪': 'Select an image to start tracking',
    '请先输入参与者姓名。': 'Enter the participant name first.',
    '请先选择一个摄像头。': 'Select a camera first.',
    '正在启用所选摄像头…': 'Enabling the selected camera...',
    '眼动追踪引擎尚未就绪，请等待初始化完成。': 'The eye-tracking engine is not ready. Wait for initialization to finish.',
    '请先完成一次校准。': 'Complete calibration first.',
    '请先选择要分析的图像。': 'Select an image to analyze first.',
    '低': 'Low',
    '中': 'Medium',
    '高': 'High',
    '未选择记录': 'No record selected',
    '当前时间段的数据点不足，无法回放轨迹。': 'There are not enough points in the current interval to replay the trajectory.',
    '没有可用的背景图像': 'No background image is available',
    '无法加载背景图像': 'Unable to load the background image',
    '当前时间段数据点不足': 'Not enough data points in the current interval',
    '有效坐标数据点不足': 'Not enough valid coordinate points',
    '注意力密度': 'Attention Density',
    '左上': 'Upper Left',
    '中上': 'Upper Center',
    '右上': 'Upper Right',
    '左中': 'Middle Left',
    '中心': 'Center',
    '右中': 'Middle Right',
    '左下': 'Lower Left',
    '中下': 'Lower Center',
    '右下': 'Lower Right',
    '正常': 'Normal',
    '有效点偏低': 'Low valid-point rate',
    '严重偏移': 'Severe offset',
    '边缘截断': 'Edge clipping',
    '样本过少': 'Too few samples',
    '无需修正': 'No correction needed',
    '样本过少，建议排除该记录或补采': 'Too few samples; exclude this record or collect additional data.',
    '优先仅使用有效点；不建议强修正': 'Use valid points first; forced correction is not recommended.',
    '疑似坐标系整体偏移，可尝试中心平移修正': 'Possible coordinate-system offset; try center-shift correction.',
    '建议筛除打印区域外点后再分析': 'Filter out points outside the printed region before analysis.',
    '疑似映射边界截断，谨慎拉伸': 'Possible boundary clipping; use stretching cautiously.',
    '人工复核': 'Manual review',
    '未命名图片': 'Unnamed Image',
    '实验组': 'Experimental',
    '对照组': 'Control',
    '未分组': 'Ungrouped',
    '视线集中在局部区域；这可能是正常观看行为，必要时可用范围拉伸做探索性预览。': 'Gaze is concentrated in a local region; this may be normal viewing behavior. Use range stretching only as an exploratory preview if needed.',
    '平均视线位置偏离中心；这可能来自观看内容本身，建议结合刺激图人工判断。': 'Mean gaze position deviates from center; this may come from the stimulus itself. Review it together with the stimulus image.',
    '暂无可分析记录。': 'No analyzable records.',
    '参与者': 'Participants',
    '采样点': 'Samples',
    '有效点比例': 'Valid Point Rate',
    '疑似异常': 'Potential Anomalies',
    '平均频率': 'Mean Frequency',
    '暂无数据': 'No data',
    '当前范围内未发现明显技术异常。局部凝视不单独计为异常。': 'No clear technical anomalies were detected in the current scope. Localized attention alone is not treated as an anomaly.',
    '暂无可导出的分析数据': 'No analysis data to export',
    '批量导出学术图片': 'Batch Export Academic Figures',
    '选择批量导出记录': 'Select Records to Export',
    '按当前分析范围选择需要导出的追踪记录。': 'Choose tracking records from the current analysis scope.',
    '全选': 'Select All',
    '清空': 'Clear',
    '导出选中图片': 'Export Selected Figures',
    '取消': 'Cancel',
    '请至少选择一条记录。': 'Select at least one record.',
    '无法导出图层，请稍后重试。': 'Unable to export the layer. Try again later.',
    '请先选择一次追踪记录。': 'Select a tracking record first.',
    '当前时间段的数据点不足，无法导出图层。': 'There are not enough points in the current interval to export the layer.',
    '当前时间段的数据点不足，无法导出学术图片。': 'There are not enough points in the current interval to export an academic figure.',
    '请先将坐标修正模式切换为“手动修正”。': 'Switch the coordinate correction mode to "Manual Correction" first.',
    '当前有效时间段或涂抹后剩余数据点不足，无法另存为修正版。': 'The current valid interval or remaining brushed data has too few points to save a corrected version.',
    '没有可保存的数据点。请调整有效时间段或恢复被涂抹的点。': 'There are no data points to save. Adjust the valid interval or restore brushed points.',
    '修正版': 'Corrected Version',
    '已另存为修正版：': 'Saved corrected version: ',
    '暂无可导出的追踪数据': 'No tracking data to export',
    '暂无参与者存档可导出': 'No participant archive to export',
    '文件读取失败': 'File read failed',
    '存档中没有可用的参与者数据': 'The archive contains no usable participant data',
    '当前追踪数据可能尚未导出存档，请确认是否已经存档。': 'Current tracking data may not have been exported. Confirm that it has been archived.',
    '请先选择图像': 'Select an image first',
    '拖框内移动，拖控制点拉伸': 'Drag inside the box to move; drag handles to stretch',
    '视线热力图分析': 'Gaze Heatmap Analysis',
    '视线序列分析': 'Gaze Sequence Analysis',
    '未知参与者': 'Unknown participant',
    '未知图片': 'Unknown image',
    '原始坐标': 'raw coordinates',
    '修正预览': 'correction preview',
    '样本数': 'Samples',
    '有效坐标率': 'Valid Coordinate Rate',
    '平均位置': 'Mean Position',
    '质控标记': 'QC Flag',
    '未发现技术标记': 'No technical flag',
    '可视化保留原始数据；修正模式仅影响预览和导出。': 'Visualization preserves original data; correction mode affects preview/export only.',
    '由 SIGN Visual Attention 生成': 'Generated by SIGN Visual Attention',
    '整体眼动分析': 'Aggregate Eye-Tracking Analysis',
    '分析范围': 'Scope',
    '生成时间': 'Generated',
    '平均 FPS': 'Mean FPS',
    '质控标记数': 'QC Flags',
    '自动解释摘要': 'Automated Interpretation Notes',
    '技术异常筛查不会将局部注意力本身视为无效。': 'Technical anomaly screening does not treat localized attention as invalid by itself.',
  },
  ja: {
    '语言': '言語',
    'SIGN Visual Attention v3 是面向标识视觉注意力研究的浏览器眼动追踪与分析工具。': 'SIGN Visual Attention v3 は、サインに対する視覚的注意研究のためのブラウザベース視線追跡・分析ツールです。',
    '基于浏览器的实时眼动追踪工具，无需专业设备，利用摄像头即可进行眼动数据采集、热力图与视线轨迹分析。': '専門機器を使わず、カメラで視線データ収集、ヒートマップ、視線軌跡分析を行えるブラウザベースのリアルタイム視線追跡ツールです。',
    'SIGN Visual Attention v3 · 基于浏览器的实时眼动追踪系统': 'SIGN Visual Attention v3 · ブラウザベースのリアルタイム視線追跡システム',
    '正在初始化眼动追踪引擎': '視線追跡エンジンを初期化しています',
    '正在加载 WebGazer.js 并请求摄像头权限…': 'WebGazer.js を読み込み、カメラ権限を要求しています...',
    '眼动追踪初始化失败': '視線追跡の初期化に失敗しました',
    '无法启动眼动追踪引擎。': '視線追跡エンジンを起動できません。',
    '请确认已允许浏览器访问摄像头': 'ブラウザでカメラアクセスが許可されているか確認してください。',
    '请使用 Chrome / Edge 等现代浏览器': 'Chrome / Edge などの最新ブラウザを使用してください。',
    '页面需通过 HTTPS 或 localhost 访问': 'ページは HTTPS または localhost 経由で開いてください。',
    '请确保环境光线充足、面部正对摄像头': '十分な明るさを確保し、顔をカメラの正面に向けてください。',
    '重试初始化': '初期化を再試行',
    '摄像头选择': 'カメラ選択',
    '流畅摄像头选择': 'スムーズなカメラ選択',
    '选择用于眼动追踪的摄像头': '視線追跡に使用するカメラを選択',
    '正在读取摄像头列表…': 'カメラ一覧を読み込んでいます...',
    '视频输入设备': '映像入力デバイス',
    '刷新列表': '一覧を更新',
    '返回首页': 'ホームへ戻る',
    '使用此摄像头（Space）': 'このカメラを使用（Space）',
    '校准前检查': 'キャリブレーション前チェック',
    '调整摄像头至眼部位置': 'カメラを目の位置に合わせる',
    '正在读取摄像头画面…': 'カメラ映像を読み込んでいます...',
    '进入九点校准（Space）': '9点キャリブレーションへ（Space）',
    '校准进行中': 'キャリブレーション中',
    '参与者注视打印校准纸上的当前编号点；操作员按 Space / Enter / 0，或单击鼠标左键确认当前点 3 次': '参加者は印刷したキャリブレーション用紙の番号点を注視し、操作者は Space / Enter / 0 または左クリックで各点を3回確認します。',
    '打印标识校准映射': '印刷サインキャリブレーションマップ',
    '打印标识追踪': '印刷サイントラッキング',
    '请让参与者观看打印出来的标识': '参加者に印刷したサインを見てもらってください。',
    '屏幕仅用于操作员监看。系统会把视线估计映射到打印标识坐标，再叠加到报告图像上。': '画面は操作者の確認用です。視線推定は印刷サイン座標へ変換され、レポート画像に重ねて表示されます。',
    '正在记录打印标识视线坐标...': '印刷サイン上の視線座標を記録しています...',
    '结束追踪': 'トラッキング終了',
    '分析页面切换': '分析ページ切り替え',
    '聚合数据分析': '集計データ分析',
    '内置图片选择': '内蔵画像選択',
    '图片选择': '画像選択',
    '请输入参与者姓名': '参加者名を入力',
    '分析报告': '分析レポート',
    '导出存档': 'アーカイブを書き出し',
    '单个数据分析': '単一データ分析',
    '整体数据分析': '全体データ分析',
    '参与者': '参加者',
    '追踪记录': '追跡記録',
    '当前回顾': '現在のレビュー',
    '未选择': '未選択',
    '导入存档或完成追踪后，可在这里选择并回顾单次数据。': 'アーカイブを読み込むか追跡を完了すると、ここで各記録を選択して確認できます。',
    '当前时段': '現在の時間範囲',
    '当前点数': '現在の点数',
    '关注质量': '注視品質',
    '采样频率': 'サンプリング頻度',
    '聚合分析': '集計分析',
    '当前没有可分析的数据。': '現在分析できるデータはありません。',
    '范围': '範囲',
    '全部数据': '全データ',
    '当前参与者': '現在の参加者',
    '当前记录': '現在の記録',
    '图片': '画像',
    '全部图片': '全画像',
    '条件对比': '条件比較',
    '条件': '条件',
    '记录': '記録',
    '点数': '点数',
    '有效率': '有効率',
    '平均时长': '平均時間',
    '中心偏移': '中心偏位',
    '图片对比': '画像比較',
    '平均 X/Y': '平均 X/Y',
    '路径长度': '経路長',
    '打印区域分布': '印刷領域分布',
    '异常筛查': '異常スクリーニング',
    '技术异常': '技術的異常',
    '覆盖': '被覆',
    '偏移': '偏位',
    '建议': '推奨',
    '自动摘要': '自動要約',
    '导出分析 CSV': '分析 CSV を書き出し',
    '导出分析 JSON': '分析 JSON を書き出し',
    '导出整体分析图': '全体分析図を書き出し',
    '热力图': 'ヒートマップ',
    '视线轨迹图': '視線軌跡図',
    '叠加背景图': '背景画像を重ねる',
    '开始': '開始',
    '结束': '終了',
    '重置': 'リセット',
    '显示全部数据': '全データを表示',
    '坐标修正': '座標補正',
    '原始': '生データ',
    '中心平移': '中心移動',
    '范围拉伸': '範囲伸縮',
    '手动修正': '手動補正',
    '自动': '自動',
    '模拟回放': '再生',
    '停止回放': '再生停止',
    '导出透明图层': '透明レイヤーを書き出し',
    '导出学术图片': '学術図を書き出し',
    '工具': 'ツール',
    '移动/变换': '移動 / 変形',
    '涂抹异常点': '異常点をブラシ除外',
    '恢复涂抹点': 'ブラシ点を復元',
    '涂抹半径': 'ブラシ半径',
    '偏移 0 / 0 · 缩放 1.00 / 1.00': 'オフセット 0 / 0 · スケール 1.00 / 1.00',
    '已涂抹 0 点': 'ブラシ済み 0 点',
    '重置手动修正': '手動補正をリセット',
    '另存为修正版': '補正版として保存',
    '导入存档文件': 'アーカイブファイルを読み込み',
    '导入 data523 文件夹': 'data523 フォルダを読み込み',
    '导出单次数据': '単一データを書き出し',
    '导出全部数据': '全データを書き出し',
    '导出 PDF': 'PDF を書き出し',
    '基于浏览器 · 本地处理 · 隐私保护': 'ブラウザベース · ローカル処理 · プライバシー保護',
    '实时眼动追踪系统': 'リアルタイム視線追跡システム',
    '利用视觉追踪技术': '視線追跡技術を用いて',
    '了解标识的注意力分布': 'サインの注意分布を把握',
    '面向通用打印标识的眼动追踪实验：参与者观看纸面内容，系统用摄像头记录并映射打印标识视线坐标。 采用 WebGazer.js 驱动，支持热力图与视线轨迹双重可视化分析。': '汎用の印刷サインを対象にした視線追跡実験です。参加者は紙面を見て、システムはカメラで視線座標を記録し印刷サイン座標へ変換します。WebGazer.js を利用し、ヒートマップと視線軌跡の両方で分析できます。',
    '摄像头校准': 'カメラキャリブレーション',
    '先选择用于眼动追踪的摄像头，再通过预览调整眼部位置，并让参与者依次注视打印校准纸上的 9 个点。 操作员按 Space、Enter、0 或单击鼠标左键确认当前点，每点 3 次。': '視線追跡に使うカメラを選択し、プレビューで目の位置を調整したうえで、印刷したキャリブレーション用紙の9点を順に注視してもらいます。操作者は Space、Enter、0、または左クリックで各点を3回確認します。',
    '参与者姓名': '参加者名',
    '摄像头预览': 'カメラプレビュー',
    '通用打印映射': '汎用印刷マッピング',
    '未校准': '未キャリブレーション',
    '开始校准': 'キャリブレーション開始',
    '选择图片并追踪': '画像を選択して追跡',
    '从 a1、a2、b1、b2 四张内置标识中选择，或载入外部图片。a1/b1 为对照组，a2/b2 为实验组。': 'a1、a2、b1、b2 の4枚の内蔵サインから選択するか、外部画像を読み込みます。a1/b1 は対照群、a2/b2 は実験群です。',
    '载入外部图片': '外部画像を読み込み',
    '外部图片': '外部画像',
    '对照组 a1/b1': '対照群 a1/b1',
    '实验组 a2/b2': '実験群 a2/b2',
    '实时视线光标': 'リアルタイム視線カーソル',
    '请先完成校准': '先にキャリブレーションを完了してください',
    '开始追踪': '追跡開始',
    '数据回顾与存档': 'データレビューとアーカイブ',
    '回顾参与者的所有图片追踪记录，查看热力图与轨迹图，导出单次数据、全部数据或完整存档。': '参加者の全画像追跡記録を確認し、ヒートマップと軌跡図を閲覧し、単一データ、全データ、または完全なアーカイブを書き出します。',
    '单次导出': '単一書き出し',
    '全部导出': '全体書き出し',
    '存档导入': 'アーカイブ読み込み',
    '无需摄像头即可回顾': 'カメラなしでレビュー可能',
    '导入存档': 'アーカイブ読み込み',
    '打开回顾': 'レビューを開く',
    'SIGN Visual Attention v3 · 基于浏览器的实时眼动追踪系统 · 本地处理，保护隐私': 'SIGN Visual Attention v3 · ブラウザベースのリアルタイム視線追跡システム · ローカル処理でプライバシーを保護',
    '还没有参与者数据。可先完成追踪，或导入参与者存档。': '参加者データはまだありません。追跡を完了するか、参加者アーカイブを読み込んでください。',
    '请选择参与者。': '参加者を選択してください。',
    '该参与者还没有完成任何图片追踪。': 'この参加者には完了した画像追跡がまだありません。',
    '完成一次图片追踪后，记录会出现在这里。': '画像追跡を1回完了すると、記録がここに表示されます。',
    '未知时间': '不明な時刻',
    '摄像头已关闭，请重新校准后开始追踪': 'カメラは閉じられています。再キャリブレーション後に追跡を開始してください。',
    '请选择图像并重新校准': '画像を選択して再キャリブレーションしてください。',
    '选择摄像头并校准': 'カメラを選択してキャリブレーション',
    '所选摄像头': '選択したカメラ',
    '您的浏览器不支持摄像头选择': 'このブラウザはカメラ選択に対応していません。',
    '正在请求摄像头权限…': 'カメラ権限を要求しています...',
    '未检测到可用摄像头': '利用可能なカメラが検出されません',
    '无法读取摄像头列表': 'カメラ一覧を読み込めません',
    '无法预览所选摄像头': '選択したカメラをプレビューできません',
    '摄像头访问失败': 'カメラアクセスに失敗しました',
    '您拒绝了摄像头权限。请在浏览器地址栏点击摄像头图标，允许访问后再重试。': 'カメラ権限が拒否されました。ブラウザのアドレスバーのカメラアイコンから許可し、再試行してください。',
    '未检测到摄像头设备，请确认摄像头已连接并正常工作。': 'カメラデバイスが検出されません。接続と動作を確認してください。',
    '摄像头被其他应用占用，请关闭其他使用摄像头的程序后重试。': 'カメラは他のアプリで使用中です。該当アプリを閉じて再試行してください。',
    '所选摄像头无法按当前配置启动，请选择其他摄像头。': '選択したカメラは現在の設定で起動できません。別のカメラを選択してください。',
    '摄像头画面尚未就绪，请稍候…': 'カメラ映像はまだ準備できていません。しばらくお待ちください...',
    '请点击预览区域或继续按钮以激活摄像头画面': 'プレビュー領域または続行ボタンをクリックしてカメラ映像を有効にしてください。',
    '请让双眼位于画面中央，并保持面部清晰可见': '両目を画面中央に置き、顔がはっきり見える状態を保ってください。',
    '无法加载 WebGazer.js 眼动追踪引擎': 'WebGazer.js 視線追跡エンジンを読み込めません',
    '您的浏览器不支持摄像头访问': 'このブラウザはカメラアクセスに対応していません',
    '正在启用摄像头…': 'カメラを有効化しています...',
    '摄像头访问被拒绝，无法启动眼动追踪': 'カメラアクセスが拒否されたため、視線追跡を開始できません',
    '正在初始化眼动追踪模型，请稍候…': '視線追跡モデルを初期化しています。しばらくお待ちください...',
    '眼动追踪引擎启动失败，请确认摄像头正常并重试。': '視線追跡エンジンの起動に失敗しました。カメラが正常か確認して再試行してください。',
    '正在重置旧校准数据…': '以前のキャリブレーションデータをリセットしています...',
    '校准完成！': 'キャリブレーション完了！',
    '重新校准': '再キャリブレーション',
    '请选择图片以开始追踪': '追跡を開始するには画像を選択してください',
    '请先输入参与者姓名。': '先に参加者名を入力してください。',
    '请先选择一个摄像头。': '先にカメラを選択してください。',
    '正在启用所选摄像头…': '選択したカメラを有効化しています...',
    '眼动追踪引擎尚未就绪，请等待初始化完成。': '視線追跡エンジンはまだ準備できていません。初期化完了をお待ちください。',
    '请先完成一次校准。': '先にキャリブレーションを1回完了してください。',
    '请先选择要分析的图像。': '先に分析する画像を選択してください。',
    '低': '低',
    '中': '中',
    '高': '高',
    '未选择记录': '記録が選択されていません',
    '当前时间段的数据点不足，无法回放轨迹。': '現在の時間範囲のデータ点が不足しているため、軌跡を再生できません。',
    '没有可用的背景图像': '利用可能な背景画像がありません',
    '无法加载背景图像': '背景画像を読み込めません',
    '当前时间段数据点不足': '現在の時間範囲のデータ点が不足しています',
    '有效坐标数据点不足': '有効座標データ点が不足しています',
    '注意力密度': '注意密度',
    '左上': '左上',
    '中上': '上中央',
    '右上': '右上',
    '左中': '左中央',
    '中心': '中央',
    '右中': '右中央',
    '左下': '左下',
    '中下': '下中央',
    '右下': '右下',
    '正常': '正常',
    '有效点偏低': '有効点が少ない',
    '严重偏移': '大きな偏位',
    '边缘截断': '端部クリッピング',
    '样本过少': 'サンプル不足',
    '无需修正': '補正不要',
    '样本过少，建议排除该记录或补采': 'サンプル不足です。この記録を除外するか追加収集してください。',
    '优先仅使用有效点；不建议强修正': 'まず有効点のみを使用してください。強制補正は推奨しません。',
    '疑似坐标系整体偏移，可尝试中心平移修正': '座標系全体の偏位が疑われます。中心移動補正を試せます。',
    '建议筛除打印区域外点后再分析': '印刷領域外の点を除外してから分析することを推奨します。',
    '疑似映射边界截断，谨慎拉伸': 'マッピング境界のクリッピングが疑われます。伸縮は慎重に使用してください。',
    '人工复核': '手動確認',
    '未命名图片': '名称未設定画像',
    '实验组': '実験群',
    '对照组': '対照群',
    '未分组': '未分類',
    '视线集中在局部区域；这可能是正常观看行为，必要时可用范围拉伸做探索性预览。': '視線が局所領域に集中しています。通常の閲覧行動である可能性があります。必要な場合のみ探索的プレビューとして範囲伸縮を使用してください。',
    '平均视线位置偏离中心；这可能来自观看内容本身，建议结合刺激图人工判断。': '平均視線位置が中心からずれています。刺激画像自体による可能性があるため、刺激図と合わせて確認してください。',
    '暂无可分析记录。': '分析可能な記録がありません。',
    '采样点': 'サンプル',
    '有效点比例': '有効点率',
    '疑似异常': '疑似異常',
    '平均频率': '平均頻度',
    '暂无数据': 'データなし',
    '当前范围内未发现明显技术异常。局部凝视不单独计为异常。': '現在の範囲で明確な技術的異常は検出されませんでした。局所的注視だけでは異常とはみなしません。',
    '暂无可导出的分析数据': '書き出し可能な分析データがありません',
    '批量导出学术图片': '学術図を一括書き出し',
    '选择批量导出记录': '一括書き出し記録を選択',
    '按当前分析范围选择需要导出的追踪记录。': '現在の分析範囲から書き出す追跡記録を選択してください。',
    '全选': 'すべて選択',
    '清空': 'クリア',
    '导出选中图片': '選択した図を書き出し',
    '取消': 'キャンセル',
    '请至少选择一条记录。': '少なくとも1件の記録を選択してください。',
    '无法导出图层，请稍后重试。': 'レイヤーを書き出せません。後でもう一度お試しください。',
    '请先选择一次追踪记录。': '先に追跡記録を1つ選択してください。',
    '当前时间段的数据点不足，无法导出图层。': '現在の時間範囲のデータ点が不足しているため、レイヤーを書き出せません。',
    '当前时间段的数据点不足，无法导出学术图片。': '現在の時間範囲のデータ点が不足しているため、学術図を書き出せません。',
    '请先将坐标修正模式切换为“手动修正”。': '先に座標補正モードを「手動補正」に切り替えてください。',
    '当前有效时间段或涂抹后剩余数据点不足，无法另存为修正版。': '現在の有効時間範囲、またはブラシ後に残った点が不足しているため、補正版として保存できません。',
    '没有可保存的数据点。请调整有效时间段或恢复被涂抹的点。': '保存できるデータ点がありません。有効時間範囲を調整するか、ブラシ除外した点を復元してください。',
    '修正版': '補正版',
    '已另存为修正版：': '補正版として保存しました：',
    '暂无可导出的追踪数据': '書き出し可能な追跡データがありません',
    '暂无参与者存档可导出': '書き出し可能な参加者アーカイブがありません',
    '文件读取失败': 'ファイル読み込みに失敗しました',
    '存档中没有可用的参与者数据': 'アーカイブに使用可能な参加者データがありません',
    '当前追踪数据可能尚未导出存档，请确认是否已经存档。': '現在の追跡データはまだアーカイブ書き出しされていない可能性があります。保存済みか確認してください。',
    '请先选择图像': '先に画像を選択してください',
    '拖框内移动，拖控制点拉伸': '枠内をドラッグして移動、ハンドルをドラッグして伸縮',
    '视线热力图分析': '視線ヒートマップ分析',
    '视线序列分析': '視線シーケンス分析',
    '未知参与者': '不明な参加者',
    '未知图片': '不明な画像',
    '原始坐标': '生座標',
    '修正预览': '補正プレビュー',
    '样本数': 'サンプル数',
    '有效坐标率': '有効座標率',
    '平均位置': '平均位置',
    '质控标记': '品質管理フラグ',
    '未发现技术标记': '技術的フラグなし',
    '可视化保留原始数据；修正模式仅影响预览和导出。': '可視化は元データを保持します。補正モードはプレビューと書き出しにのみ反映されます。',
    '由 SIGN Visual Attention 生成': 'SIGN Visual Attention により生成',
    '整体眼动分析': '全体視線追跡分析',
    '分析范围': '範囲',
    '生成时间': '生成日時',
    '平均 FPS': '平均 FPS',
    '质控标记数': '品質管理フラグ数',
    '自动解释摘要': '自動解釈メモ',
    '技术异常筛查不会将局部注意力本身视为无效。': '技術的異常スクリーニングでは、局所的注意そのものを無効とはみなしません。',
  },
};

const I18N_PATTERNS = {
  en: [
    [/^错误详情：(.+)$/, match => `Error details: ${match[1]}`],
    [/^摄像头 (\d+)$/, match => `Camera ${match[1]}`],
    [/^(.+) · (对照组|实验组|外部图片)$/, match => `${match[1]} · ${localizeText(match[2])}`],
    [/^检测到 (\d+) 个摄像头$/, match => `Detected ${match[1]} camera${match[1] === '1' ? '' : 's'}`],
    [/^正在启用摄像头：(.+)…$/, match => `Enabling camera: ${match[1]}...`],
    [/^已选择「(.+)」(.+)，请先完成校准$/, match => `Selected "${match[1]}" (${localizeText(match[2])}); complete calibration first.`],
    [/^(.+) 校准完成$/, match => `${match[1]} calibration complete`],
    [/^(.+) · 打印标识校准 · 已记录 (\d+) 次$/, match => `${match[1]} · printed-sign calibration · ${match[2]} run${match[2] === '1' ? '' : 's'} recorded`],
    [/^(.+) · (.+)可开始追踪$/, match => `${match[1]} · ${match[2]} is ready for tracking`],
    [/^(.+) 次追踪 · (.+)$/, match => `${match[1]} tracking run${match[1] === '1' ? '' : 's'} · ${match[2]}`],
    [/^(.+) 点 · (.+) s · (.+)$/, match => `${match[1]} points · ${match[2]} s · ${match[3]}`],
    [/^(.+) 个数据点，追踪 (.+) 秒。$/, match => `${match[1]} data points, tracked for ${match[2]} seconds.`],
    [/^显示全部 (\d+) 点$/, match => `Showing all ${match[1]} points`],
    [/^(.+)-(.+) s · (.+)\/(.+) 点$/, match => `${match[1]}-${match[2]} s · ${match[3]}/${match[4]} points`],
    [/^偏移 (.+) \/ (.+) · 缩放 (.+) \/ (.+)$/, match => `Offset ${match[1]} / ${match[2]} · Scale ${match[3]} / ${match[4]}`],
    [/^已涂抹 (.+) 点$/, match => `Brushed ${match[1]} points`],
    [/^(.+) 点$/, match => `${match[1]} points`],
    [/^共 (.+) 名参与者、(.+) 次追踪、(.+) 个采样点。$/, match => `${match[1]} participant${match[1] === '1' ? '' : 's'}, ${match[2]} tracking run${match[2] === '1' ? '' : 's'}, and ${match[3]} samples in total.`],
    [/^筛查出 (.+) 次疑似技术异常记录，局部凝视不会单独计为异常。$/, match => `${match[1]} potential technical-anomaly run${match[1] === '1' ? '' : 's'} detected; localized attention alone is not treated as an anomaly.`],
    [/^打印区域有效点比例为 (.+)，平均采样频率 (.+) Hz。$/, match => `The printed-region valid-point rate is ${match[1]}, with a mean sampling frequency of ${match[2]} Hz.`],
    [/^视线最集中区域是「(.+)」，占有效点 (.+)。$/, match => `The densest gaze region is "${localizeText(match[1])}", accounting for ${match[2]} of valid points.`],
    [/^条件有效率最高的是「(.+)」，比最低条件高 (.+)。$/, match => `The highest valid rate appears in "${localizeText(match[1])}", ${match[2]} higher than the lowest condition.`],
    [/^平均视线移动路径最长的图片是「(.+)」，约 (.+) mm。$/, match => `The image with the longest mean gaze path is "${match[1]}", approximately ${match[2]} mm.`],
    [/^(.+) · (.+) 次记录 · (.+) 点$/, match => `${localizeText(match[1])} · ${match[2]} records · ${match[3]} points`],
    [/^无法导出图层：(.+)$/, match => `Unable to export layer: ${match[1]}`],
    [/^无法导出学术图片：(.+)$/, match => `Unable to export academic figure: ${match[1]}`],
    [/^批量导出完成：(\d+) 张(?:，跳过 (\d+) 条点数不足记录)?$/, match => `Batch export complete: ${match[1]} figure${match[1] === '1' ? '' : 's'}${match[2] ? `, skipped ${match[2]} record${match[2] === '1' ? '' : 's'} with too few points` : ''}`],
    [/^无法载入外部图片：(.+)$/, match => `Unable to load external image: ${match[1]}`],
    [/^已另存为修正版：(.+)$/, match => `Saved corrected version: ${match[1]}`],
    [/^无法导入存档：(.+)$/, match => `Unable to import archive: ${match[1]}`],
    [/^(.+): 文件读取失败$/, match => `${match[1]}: file read failed`],
    [/^(.+): 存档中没有可用的参与者数据$/, match => `${match[1]}: archive contains no usable participant data`],
    [/^选择图片 (\d+): (.+)，(.+)$/, match => `Select image ${match[1]}: ${match[2]}, ${localizeText(match[3])}`],
    [/^选择内置图片 (\d+): (.+)，(.+)$/, match => `Select built-in image ${match[1]}: ${match[2]}, ${localizeText(match[3])}`],
  ],
  ja: [
    [/^错误详情：(.+)$/, match => `エラー詳細：${match[1]}`],
    [/^摄像头 (\d+)$/, match => `カメラ ${match[1]}`],
    [/^(.+) · (对照组|实验组|外部图片)$/, match => `${match[1]} · ${localizeText(match[2])}`],
    [/^检测到 (\d+) 个摄像头$/, match => `${match[1]} 台のカメラを検出しました`],
    [/^正在启用摄像头：(.+)…$/, match => `カメラを有効化しています：${match[1]}...`],
    [/^已选择「(.+)」(.+)，请先完成校准$/, match => `「${match[1]}」（${localizeText(match[2])}）を選択しました。先にキャリブレーションを完了してください。`],
    [/^(.+) 校准完成$/, match => `${match[1]} のキャリブレーション完了`],
    [/^(.+) · 打印标识校准 · 已记录 (\d+) 次$/, match => `${match[1]} · 印刷サインキャリブレーション · ${match[2]} 回記録済み`],
    [/^(.+) · (.+)可开始追踪$/, match => `${match[1]} · ${match[2]} は追跡を開始できます`],
    [/^(.+) 次追踪 · (.+)$/, match => `${match[1]} 回の追跡 · ${match[2]}`],
    [/^(.+) 点 · (.+) s · (.+)$/, match => `${match[1]} 点 · ${match[2]} s · ${match[3]}`],
    [/^(.+) 个数据点，追踪 (.+) 秒。$/, match => `${match[1]} 個のデータ点、追跡時間 ${match[2]} 秒。`],
    [/^显示全部 (\d+) 点$/, match => `全 ${match[1]} 点を表示`],
    [/^(.+)-(.+) s · (.+)\/(.+) 点$/, match => `${match[1]}-${match[2]} s · ${match[3]}/${match[4]} 点`],
    [/^偏移 (.+) \/ (.+) · 缩放 (.+) \/ (.+)$/, match => `オフセット ${match[1]} / ${match[2]} · スケール ${match[3]} / ${match[4]}`],
    [/^已涂抹 (.+) 点$/, match => `ブラシ済み ${match[1]} 点`],
    [/^(.+) 点$/, match => `${match[1]} 点`],
    [/^共 (.+) 名参与者、(.+) 次追踪、(.+) 个采样点。$/, match => `合計 ${match[1]} 名の参加者、${match[2]} 回の追跡、${match[3]} 個のサンプルがあります。`],
    [/^筛查出 (.+) 次疑似技术异常记录，局部凝视不会单独计为异常。$/, match => `${match[1]} 回の疑似技術的異常を検出しました。局所的注視だけでは異常とはみなしません。`],
    [/^打印区域有效点比例为 (.+)，平均采样频率 (.+) Hz。$/, match => `印刷領域の有効点率は ${match[1]}、平均サンプリング頻度は ${match[2]} Hz です。`],
    [/^视线最集中区域是「(.+)」，占有效点 (.+)。$/, match => `視線が最も集中した領域は「${localizeText(match[1])}」で、有効点の ${match[2]} を占めます。`],
    [/^条件有效率最高的是「(.+)」，比最低条件高 (.+)。$/, match => `有効率が最も高い条件は「${localizeText(match[1])}」で、最低条件より ${match[2]} 高いです。`],
    [/^平均视线移动路径最长的图片是「(.+)」，约 (.+) mm。$/, match => `平均視線移動経路が最も長い画像は「${match[1]}」で、約 ${match[2]} mm です。`],
    [/^(.+) · (.+) 次记录 · (.+) 点$/, match => `${localizeText(match[1])} · ${match[2]} 件の記録 · ${match[3]} 点`],
    [/^无法导出图层：(.+)$/, match => `レイヤーを書き出せません：${match[1]}`],
    [/^无法导出学术图片：(.+)$/, match => `学術図を書き出せません：${match[1]}`],
    [/^批量导出完成：(\d+) 张(?:，跳过 (\d+) 条点数不足记录)?$/, match => `一括書き出し完了：${match[1]}件${match[2] ? `、点数不足の記録を${match[2]}件スキップ` : ''}`],
    [/^无法载入外部图片：(.+)$/, match => `外部画像を読み込めません：${match[1]}`],
    [/^已另存为修正版：(.+)$/, match => `補正版として保存しました：${match[1]}`],
    [/^无法导入存档：(.+)$/, match => `アーカイブを読み込めません：${match[1]}`],
    [/^(.+): 文件读取失败$/, match => `${match[1]}: ファイル読み込みに失敗しました`],
    [/^(.+): 存档中没有可用的参与者数据$/, match => `${match[1]}: アーカイブに使用可能な参加者データがありません`],
    [/^选择图片 (\d+): (.+)，(.+)$/, match => `画像 ${match[1]} を選択：${match[2]}、${localizeText(match[3])}`],
    [/^选择内置图片 (\d+): (.+)，(.+)$/, match => `内蔵画像 ${match[1]} を選択：${match[2]}、${localizeText(match[3])}`],
  ],
};

const originalTextNodes = new WeakMap();
const originalAttributes = new WeakMap();
const nativeAlert = window.alert.bind(window);

function getInitialLanguage() {
  const saved = localStorage.getItem(LANGUAGE_STORAGE_KEY);
  if (SUPPORTED_LANGUAGES.has(saved)) return saved;
  const browserLanguage = navigator.language || '';
  if (browserLanguage.toLowerCase().startsWith('ja')) return 'ja';
  if (browserLanguage.toLowerCase().startsWith('en')) return 'en';
  return 'zh-CN';
}

function translateSourceText(source, language = State?.language || 'zh-CN') {
  const text = String(source ?? '');
  if (language === 'zh-CN') return text;
  const exact = I18N_TEXT[language]?.[text];
  if (exact) return exact;
  const patterns = I18N_PATTERNS[language] || [];
  for (const [pattern, formatter] of patterns) {
    const match = text.match(pattern);
    if (match) return formatter(match);
  }
  return text;
}

function localizeText(source) {
  return translateSourceText(source, State.language);
}

function getDisplayLocale() {
  if (State.language === 'ja') return 'ja-JP';
  if (State.language === 'en') return 'en-US';
  return 'zh-CN';
}

function localizeTextNode(node) {
  const raw = node.nodeValue || '';
  const trimmed = raw.trim();
  if (!trimmed) return;
  const knownSource = I18N_TEXT.en[trimmed] || I18N_TEXT.ja[trimmed] || I18N_PATTERNS.en.some(([pattern]) => pattern.test(trimmed)) || I18N_PATTERNS.ja.some(([pattern]) => pattern.test(trimmed));
  if (knownSource || !originalTextNodes.has(node)) {
    originalTextNodes.set(node, trimmed);
  }
  const source = originalTextNodes.get(node) || trimmed;
  const translated = localizeText(source);
  const leading = raw.match(/^\s*/)?.[0] || '';
  const trailing = raw.match(/\s*$/)?.[0] || '';
  const next = `${leading}${translated}${trailing}`;
  if (node.nodeValue !== next) node.nodeValue = next;
}

function localizeAttributes(el) {
  const attrs = ['placeholder', 'title', 'aria-label', 'alt'];
  attrs.forEach(attr => {
    if (!el.hasAttribute(attr)) return;
    let attrMap = originalAttributes.get(el);
    if (!attrMap) {
      attrMap = {};
      originalAttributes.set(el, attrMap);
    }
    const current = el.getAttribute(attr);
    const knownSource = I18N_TEXT.en[current] || I18N_TEXT.ja[current] || I18N_PATTERNS.en.some(([pattern]) => pattern.test(current)) || I18N_PATTERNS.ja.some(([pattern]) => pattern.test(current));
    if (knownSource || !attrMap[attr]) attrMap[attr] = current;
    const translated = localizeText(attrMap[attr]);
    if (current !== translated) el.setAttribute(attr, translated);
  });
}

function localizeElementTree(root = document.body) {
  if (!root) return;
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT, {
    acceptNode(node) {
      const parent = node.nodeType === Node.TEXT_NODE ? node.parentElement : node;
      if (!parent || parent.closest('script, style, textarea')) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    },
  });

  do {
    const node = walker.currentNode;
    if (node.nodeType === Node.TEXT_NODE) localizeTextNode(node);
    else if (node.nodeType === Node.ELEMENT_NODE) localizeAttributes(node);
  } while (walker.nextNode());
}

function applyLanguage(language) {
  State.language = SUPPORTED_LANGUAGES.has(language) ? language : 'zh-CN';
  localStorage.setItem(LANGUAGE_STORAGE_KEY, State.language);
  document.documentElement.lang = State.language === 'ja' ? 'ja' : (State.language === 'en' ? 'en' : 'zh-CN');
  document.title = localizeText('SIGN Visual Attention v3 · 基于浏览器的实时眼动追踪系统');
  document.querySelector('meta[name="description"]')?.setAttribute(
    'content',
    localizeText('SIGN Visual Attention v3 是面向标识视觉注意力研究的浏览器眼动追踪与分析工具。')
  );
  if (EL.languageSelect) EL.languageSelect.value = State.language;
  localizeElementTree(document.body);
}

function startLanguageObserver() {
  const observer = new MutationObserver(mutations => {
    mutations.forEach(mutation => {
      if (mutation.type === 'characterData') {
        localizeTextNode(mutation.target);
      } else if (mutation.type === 'childList') {
        mutation.addedNodes.forEach(node => {
          if (node.nodeType === Node.TEXT_NODE) localizeTextNode(node);
          else if (node.nodeType === Node.ELEMENT_NODE) localizeElementTree(node);
        });
      } else if (mutation.type === 'attributes') {
        localizeAttributes(mutation.target);
      }
    });
  });
  observer.observe(document.body, {
    childList: true,
    subtree: true,
    characterData: true,
    attributes: true,
    attributeFilter: ['placeholder', 'title', 'aria-label', 'alt'],
  });
}

window.alert = message => nativeAlert(localizeText(message));

// ─── 状态 ──────────────────────────────────────────────────────
const State = {
  language: getInitialLanguage(),
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
  reportCorrectionMode: 'raw',
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
  latestAnalysisSnapshot: null,
  manualCorrection: null,
  manualCorrectionRunKey: '',
  academicBatchRecords: [],
};

// ─── DOM ────────────────────────────────────────────────────────
const $ = (id) => document.getElementById(id);
const EL = {
  // 弹窗
  languageSelect:  $('language-select'),
  loadingOverlay:  $('loading-overlay'),
  loadingStatus:   $('loading-status'),
  errorModal:      $('error-modal'),
  errorMessage:    $('error-message'),
  errorDetail:     $('error-detail'),
  retryInitBtn:    $('retry-init-btn'),
  academicBatchModal: $('academic-batch-modal'),
  academicBatchSummary: $('academic-batch-summary'),
  academicBatchList: $('academic-batch-list'),
  academicBatchSelectAllBtn: $('academic-batch-select-all-btn'),
  academicBatchClearBtn: $('academic-batch-clear-btn'),
  academicBatchCancelBtn: $('academic-batch-cancel-btn'),
  academicBatchCancelSecondaryBtn: $('academic-batch-cancel-secondary-btn'),
  academicBatchStartBtn: $('academic-batch-start-btn'),

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
  externalImageInput: $('external-image-input'),
  externalImageBtn: $('external-image-btn'),

  // 追踪
  trackingImage:        $('tracking-image'),
  trackingPaperPlane:   $('tracking-paper-plane'),
  gazeCursorTracking:   $('gaze-cursor-tracking'),
  stopTrackingBtn:      $('stop-tracking-btn'),

  // 报告
  singleAnalysisTab: $('single-analysis-tab'),
  overallAnalysisTab: $('overall-analysis-tab'),
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
  vizCorrectionMode: $('viz-correction-mode'),
  manualCorrectionPanel: $('manual-correction-panel'),
  manualCorrectionCanvas: $('manual-correction-canvas'),
  manualCorrectionTool: $('manual-correction-tool'),
  manualBrushRadius: $('manual-brush-radius'),
  manualTransformStatus: $('manual-transform-status'),
  manualExcludedStatus: $('manual-excluded-status'),
  manualResetBtn: $('manual-reset-btn'),
  saveCorrectedVersionBtn: $('save-corrected-version-btn'),
  gazePlaybackBtn: $('gaze-playback-btn'),
  exportVizLayerBtn: $('export-viz-layer-btn'),
  exportAcademicFigureBtn: $('export-academic-figure-btn'),
  exportAcademicBatchBtn: $('export-academic-batch-btn'),
  analysisScopeNote: $('analysis-scope-note'),
  analysisScopeSelect: $('analysis-scope-select'),
  analysisImageSelect: $('analysis-image-select'),
  analysisSummaryGrid: $('analysis-summary-grid'),
  analysisConditionCount: $('analysis-condition-count'),
  analysisConditionTable: $('analysis-condition-table'),
  analysisImageCount: $('analysis-image-count'),
  analysisImageTable: $('analysis-image-table'),
  analysisZoneTotal: $('analysis-zone-total'),
  analysisZoneGrid: $('analysis-zone-grid'),
  analysisAnomalyCount: $('analysis-anomaly-count'),
  analysisAnomalyTable: $('analysis-anomaly-table'),
  analysisInsightCount: $('analysis-insight-count'),
  analysisInsights: $('analysis-insights'),
  exportAnalysisCsvBtn: $('export-analysis-csv-btn'),
  exportAnalysisJsonBtn: $('export-analysis-json-btn'),
  exportAnalysisFigureBtn: $('export-analysis-figure-btn'),
  backHomeBtn:   $('back-home-btn'),
  importArchiveBtn:   $('import-archive-btn'),
  importArchiveInput: $('import-archive-input'),
  importArchiveFolderBtn: $('import-archive-folder-btn'),
  importArchiveFolderInput: $('import-archive-folder-input'),
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
  { id: 'a1', name: 'a1', group: 'A', condition: 'control', conditionLabel: '对照组', src: 'A1.png' },
  { id: 'a2', name: 'a2', group: 'A', condition: 'experiment', conditionLabel: '实验组', src: 'A2.png' },
  { id: 'b1', name: 'b1', group: 'B', condition: 'control', conditionLabel: '对照组', src: 'B1.png' },
  { id: 'b2', name: 'b2', group: 'B', condition: 'experiment', conditionLabel: '实验组', src: 'B2.png' },
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
  const participantLabel = enteredName || `未命名参与者-${State.calibrationSessionSeq}`;
  const usedIds = new Set(State.calibrationSessions.map(session => session.id));
  let participantId = participantLabel;
  let suffix = 2;
  while (usedIds.has(participantId)) {
    participantId = `${participantLabel}-${suffix}`;
    suffix += 1;
  }
  const session = {
    id: participantId,
    label: participantLabel,
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
  setReportMode('single');
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

function setReportMode(mode = 'single') {
  const normalized = mode === 'overall' ? 'overall' : 'single';
  EL.reportScreen.classList.toggle('report-mode-single', normalized === 'single');
  EL.reportScreen.classList.toggle('report-mode-overall', normalized === 'overall');
  EL.singleAnalysisTab.classList.toggle('active', normalized === 'single');
  EL.overallAnalysisTab.classList.toggle('active', normalized === 'overall');
  EL.singleAnalysisTab.setAttribute('aria-selected', String(normalized === 'single'));
  EL.overallAnalysisTab.setAttribute('aria-selected', String(normalized === 'overall'));

  if (normalized === 'single') {
    updateReportFromCurrentRun();
  } else {
    stopGazePlayback(false);
    updateAnalysisDashboard();
  }
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
    updateAnalysisDashboard();
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
    updateAnalysisDashboard();
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
  updateAnalysisDashboard();
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
    if (State.reportCorrectionMode === 'manual') ensureManualCorrectionState(run);
  }
  updateReportStats(run);
  updateManualCorrectionPanel();
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
  return date.toLocaleString(getDisplayLocale(), { hour12: false });
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
      setTrackStatus('status-pending', '请选择图片以开始追踪');
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
    item.setAttribute('aria-label', `选择图片 ${index + 1}: ${image.name}，${image.conditionLabel}`);
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

function readFileAsDataUrl(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = event => resolve(String(event.target?.result || ''));
    reader.onerror = () => reject(new Error('文件读取失败'));
    reader.readAsDataURL(file);
  });
}

async function loadExternalImage(file) {
  if (!file || !file.type?.startsWith('image/')) {
    alert('请先选择图像');
    return;
  }

  try {
    const src = await readFileAsDataUrl(file);
    if (!src) throw new Error('文件读取失败');
    const id = `external-${Date.now()}`;
    const image = {
      id,
      name: file.name.replace(/\.[^.]+$/, '') || localizeText('外部图片'),
      group: 'external',
      condition: 'external',
      conditionLabel: '外部图片',
      size: file.size || 0,
      src,
    };
    State.uploadedImages.push(image);
    selectImage(id);
  } catch (err) {
    alert(`无法载入外部图片：${err.message}`);
  } finally {
    if (EL.externalImageInput) EL.externalImageInput.value = '';
  }
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
  const sessionText = State.calibrationSession ? `${State.calibrationSession.label} · 打印标识校准 · 已记录 ${runCount} 次` : '已校准';
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

function getPointIdentity(point, index) {
  return String(point?.index ?? index + 1);
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

function getTimeFilteredReportPoints(run = State.currentReportRun) {
  const points = run ? run.points : State.gazeHistory;
  if (!points.length) return [];

  const range = getReportTimeRange(run);
  return points
    .map((point, index) => ({ point, index }))
    .filter(({ point, index }) => {
    const t = getPointTimeSeconds(point, index, points, run);
    return t >= range.start && t <= range.end;
  });
}

function getFilteredReportPoints(run = State.currentReportRun) {
  const entries = getTimeFilteredReportPoints(run);
  if (!isManualCorrectionActive(run)) return entries.map(entry => entry.point);
  const excluded = State.manualCorrection?.excluded || new Set();
  return entries
    .filter(({ point, index }) => !excluded.has(getPointIdentity(point, index)))
    .map(entry => entry.point);
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
    canvas.style.width = '';
    canvas.style.height = '';
    return;
  }

  const container = canvas.parentElement;
  const containerW = Math.max(1, (container?.clientWidth || window.innerWidth) - 2);
  const containerH = Math.max(1, (container?.clientHeight || window.innerHeight * 0.65) - 2);
  const scale = Math.min(
    containerW / img.naturalWidth,
    containerH / img.naturalHeight,
    1
  );
  canvas.width  = Math.round(img.naturalWidth  * scale);
  canvas.height = Math.round(img.naturalHeight * scale);
  canvas.style.width = `${canvas.width}px`;
  canvas.style.height = `${canvas.height}px`;
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
  ctx.fillText(localizeText(text), (canvas.width || 1) / 2, (canvas.height || 1) / 2);
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

function getMetricForRun(run) {
  const record = findRunRecord(run);
  if (record) return computeRunMetrics(record);
  const session = State.calibrationSession || { id: 'current', label: '当前参与者' };
  return computeRunMetrics({ session, run, trialIndex: 1 });
}

function getRunManualKey(run = State.currentReportRun) {
  const record = findRunRecord(run);
  return `${record?.session?.id || State.selectedSessionId || 'session'}:${run?.id || 'run'}`;
}

function createManualCorrectionState() {
  return {
    offsetX: 0,
    offsetY: 0,
    scaleX: 1,
    scaleY: 1,
    brushRadius: 0.04,
    excluded: new Set(),
    pointer: null,
    lastBox: null,
    needsBaseRedraw: false,
  };
}

function ensureManualCorrectionState(run = State.currentReportRun) {
  const key = getRunManualKey(run);
  if (!State.manualCorrection || State.manualCorrectionRunKey !== key) {
    State.manualCorrection = createManualCorrectionState();
    State.manualCorrectionRunKey = key;
  }
  return State.manualCorrection;
}

function isManualCorrectionActive(run = State.currentReportRun) {
  return Boolean(run && State.reportCorrectionMode === 'manual');
}

function updateManualCorrectionPanel() {
  const active = isManualCorrectionActive();
  EL.manualCorrectionPanel?.classList.toggle('hidden', !active);
  EL.manualCorrectionCanvas?.classList.toggle('hidden', !active);
  if (!active) {
    clearManualOverlay();
    return;
  }
  const state = ensureManualCorrectionState();
  if (EL.manualBrushRadius) EL.manualBrushRadius.value = String(Math.round(state.brushRadius * 100));
  if (EL.manualTransformStatus) {
    EL.manualTransformStatus.textContent = `偏移 ${state.offsetX.toFixed(2)} / ${state.offsetY.toFixed(2)} · 缩放 ${state.scaleX.toFixed(2)} / ${state.scaleY.toFixed(2)}`;
  }
  if (EL.manualExcludedStatus) {
    EL.manualExcludedStatus.textContent = `已涂抹 ${state.excluded.size.toLocaleString()} 点`;
  }
  syncManualOverlayCanvas();
  drawManualOverlay();
}

function resolveCorrectionMode(run, requestedMode = State.reportCorrectionMode) {
  if (requestedMode === 'manual') return 'manual';
  if (requestedMode !== 'auto') return requestedMode || 'raw';
  return getMetricForRun(run).autoCorrectionMode || 'raw';
}

function transformManualPosition(pos, state, shouldClamp = true) {
  const transformed = {
    x: 0.5 + (pos.x - 0.5) * state.scaleX + state.offsetX,
    y: 0.5 + (pos.y - 0.5) * state.scaleY + state.offsetY,
  };
  return shouldClamp
    ? { x: clamp01(transformed.x), y: clamp01(transformed.y) }
    : transformed;
}

function applyA4Correction(pos, run, requestedMode = State.reportCorrectionMode) {
  const mode = resolveCorrectionMode(run, requestedMode);
  if (!run || mode === 'raw') return pos;

  const metric = getMetricForRun(run);
  if (mode === 'manual') {
    const state = ensureManualCorrectionState(run);
    return transformManualPosition(pos, state);
  }

  if (mode === 'shift' && metric.meanX != null && metric.meanY != null) {
    return {
      x: clamp01(pos.x + (0.5 - metric.meanX)),
      y: clamp01(pos.y + (0.5 - metric.meanY)),
    };
  }

  if (mode === 'stretch') {
    const bounds = metric.robustBounds || {};
    const width = Number(bounds.maxX) - Number(bounds.minX);
    const height = Number(bounds.maxY) - Number(bounds.minY);
    if (width > 0.08 && height > 0.08) {
      const margin = 0.04;
      const scale = 1 - margin * 2;
      return {
        x: clamp01(margin + ((pos.x - bounds.minX) / width) * scale),
        y: clamp01(margin + ((pos.y - bounds.minY) / height) * scale),
      };
    }
  }

  return pos;
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
  if (!['a4-paper', 'a4-landscape-paper'].includes(run?.coordinateSystem)) return null;
  const paperPoint = getRawA4Position(point, run);
  if (!paperPoint) return null;
  const corrected = applyA4Correction(paperPoint, run);

  return {
    x: clamp01(corrected.x) * canvas.width,
    y: clamp01(corrected.y) * canvas.height,
  };
}

function getRawA4Position(point, run) {
  const plane = run?.a4Plane || State.calibrationSession?.a4Plane || State.currentA4Plane;
  if (Number.isFinite(point.a4X) && Number.isFinite(point.a4Y)) {
    return { x: clamp01(point.a4X), y: clamp01(point.a4Y) };
  }
  if (plane && Number.isFinite(Number(point?.x)) && Number.isFinite(Number(point?.y))) {
    const mapped = virtualScreenToA4(Number(point.x), Number(point.y), plane);
    return { x: mapped.x, y: mapped.y };
  }
  if (Number.isFinite(Number(point?.x)) && Number.isFinite(Number(point?.y))) {
    return {
      x: clamp01(Number(point.x) / Math.max(1, window.innerWidth)),
      y: clamp01(Number(point.y) / Math.max(1, window.innerHeight)),
    };
  }
  return null;
}

function createPointToCanvasMapper(canvas, img, run) {
  if (resolveCorrectionMode(run, State.reportCorrectionMode) === 'manual') {
    return point => {
      const raw = getRawA4Position(point, run);
      if (!raw) return null;
      const corrected = applyA4Correction(raw, run, 'manual');
      return {
        x: clamp01(corrected.x) * canvas.width,
        y: clamp01(corrected.y) * canvas.height,
      };
    };
  }
  if (['a4-paper', 'a4-landscape-paper'].includes(run?.coordinateSystem)) {
    return point => a4PointToCanvas(point, canvas, run);
  }
  return legacyScreenToCanvasMapper(canvas, img);
}

function clearManualOverlay() {
  const overlay = EL.manualCorrectionCanvas;
  if (!overlay) return;
  const ctx = overlay.getContext('2d');
  ctx.clearRect(0, 0, overlay.width || 1, overlay.height || 1);
}

function syncManualOverlayCanvas() {
  const overlay = EL.manualCorrectionCanvas;
  const canvas = EL.reportCanvas;
  if (!overlay || !canvas || !isManualCorrectionActive()) return false;
  const canvasRect = canvas.getBoundingClientRect();
  const parentRect = canvas.parentElement.getBoundingClientRect();
  if (!canvasRect.width || !canvasRect.height) return false;
  const ratio = window.devicePixelRatio || 1;
  overlay.style.left = `${canvasRect.left - parentRect.left}px`;
  overlay.style.top = `${canvasRect.top - parentRect.top}px`;
  overlay.style.width = `${canvasRect.width}px`;
  overlay.style.height = `${canvasRect.height}px`;
  overlay.width = Math.max(1, Math.round(canvasRect.width * ratio));
  overlay.height = Math.max(1, Math.round(canvasRect.height * ratio));
  const ctx = overlay.getContext('2d');
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
  return true;
}

function getCanvasRelativePosition(event, options = {}) {
  const canvas = EL.reportCanvas;
  if (!canvas) return null;
  const rect = canvas.getBoundingClientRect();
  if (!rect.width || !rect.height) return null;
  const x = (event.clientX - rect.left) / rect.width;
  const y = (event.clientY - rect.top) / rect.height;
  const shouldClamp = options.clamp !== false;
  return {
    x: shouldClamp ? clamp01(x) : x,
    y: shouldClamp ? clamp01(y) : y,
    rect,
  };
}

function drawManualOverlay() {
  const overlay = EL.manualCorrectionCanvas;
  const run = State.currentReportRun;
  if (!overlay || !run || !isManualCorrectionActive() || !syncManualOverlayCanvas()) return;
  const ctx = overlay.getContext('2d');
  const width = overlay.getBoundingClientRect().width;
  const height = overlay.getBoundingClientRect().height;
  ctx.clearRect(0, 0, width, height);

  const state = ensureManualCorrectionState(run);
  const entries = getManualOverlayEntries(run);
  const step = Math.max(1, Math.floor(entries.length / 900));
  entries.forEach(({ point, index, corrected }, entryIndex) => {
    if (entryIndex % step !== 0) return;
    const excluded = state.excluded.has(getPointIdentity(point, index));
    ctx.beginPath();
    ctx.arc(corrected.x * width, corrected.y * height, excluded ? 4 : 2.2, 0, Math.PI * 2);
    ctx.fillStyle = excluded ? 'rgba(200,66,63,0.86)' : 'rgba(37,84,166,0.36)';
    ctx.fill();
    if (excluded) {
      ctx.strokeStyle = 'rgba(255,255,255,0.9)';
      ctx.lineWidth = 1;
      ctx.stroke();
    }
  });

  const box = getManualTransformBox(run, entries);
  state.lastBox = box;
  if (box) drawManualTransformBox(ctx, box, width, height);

  const pointer = state.pointer?.current;
  const tool = EL.manualCorrectionTool?.value || 'transform';
  if (pointer && (tool === 'erase' || tool === 'restore')) {
    ctx.beginPath();
    ctx.arc(pointer.x * width, pointer.y * height, state.brushRadius * Math.min(width, height), 0, Math.PI * 2);
    ctx.strokeStyle = tool === 'erase' ? 'rgba(200,66,63,0.9)' : 'rgba(31,122,92,0.9)';
    ctx.lineWidth = 2;
    ctx.stroke();
  }
}

function getManualOverlayEntries(run = State.currentReportRun) {
  const state = ensureManualCorrectionState(run);
  return getTimeFilteredReportPoints(run).map(({ point, index }) => {
    const raw = getRawA4Position(point, run);
    if (!raw) return null;
    const transformed = transformManualPosition(raw, state, false);
    return {
      point,
      index,
      raw,
      transformed,
      corrected: {
        x: clamp01(transformed.x),
        y: clamp01(transformed.y),
      },
    };
  }).filter(Boolean);
}

function getManualTransformBox(run = State.currentReportRun, preparedEntries = null) {
  const state = ensureManualCorrectionState(run);
  const entries = preparedEntries || getManualOverlayEntries(run);
  const active = entries.filter(({ point, index }) => !state.excluded.has(getPointIdentity(point, index)));
  if (!active.length) return null;
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  active.forEach(({ corrected, transformed }) => {
    const point = transformed || corrected;
    minX = Math.min(minX, point.x);
    minY = Math.min(minY, point.y);
    maxX = Math.max(maxX, point.x);
    maxY = Math.max(maxY, point.y);
  });
  const pad = 0.012;
  return {
    minX: minX - pad,
    minY: minY - pad,
    maxX: maxX + pad,
    maxY: maxY + pad,
  };
}

function getManualBoxDisplayBox(box, width = 1, height = 1) {
  if (!box) return null;
  const insetX = Math.min(0.08, 14 / Math.max(1, width));
  const insetY = Math.min(0.08, 14 / Math.max(1, height));
  const minX = Math.max(insetX, Math.min(1 - insetX, box.minX));
  const maxX = Math.max(insetX, Math.min(1 - insetX, box.maxX));
  const minY = Math.max(insetY, Math.min(1 - insetY, box.minY));
  const maxY = Math.max(insetY, Math.min(1 - insetY, box.maxY));
  return {
    minX: Math.min(minX, maxX),
    minY: Math.min(minY, maxY),
    maxX: Math.max(minX, maxX),
    maxY: Math.max(minY, maxY),
  };
}

function getManualBoxHandles(box, displayBox = box) {
  if (!box) return [];
  const visible = displayBox || box;
  const cx = (visible.minX + visible.maxX) / 2;
  const cy = (visible.minY + visible.maxY) / 2;
  return [
    { id: 'nw', x: visible.minX, y: visible.minY, cursor: 'nwse-resize' },
    { id: 'n', x: cx, y: visible.minY, cursor: 'ns-resize' },
    { id: 'ne', x: visible.maxX, y: visible.minY, cursor: 'nesw-resize' },
    { id: 'e', x: visible.maxX, y: cy, cursor: 'ew-resize' },
    { id: 'se', x: visible.maxX, y: visible.maxY, cursor: 'nwse-resize' },
    { id: 's', x: cx, y: visible.maxY, cursor: 'ns-resize' },
    { id: 'sw', x: visible.minX, y: visible.maxY, cursor: 'nesw-resize' },
    { id: 'w', x: visible.minX, y: cy, cursor: 'ew-resize' },
  ];
}

function drawManualTransformBox(ctx, box, width, height) {
  const displayBox = getManualBoxDisplayBox(box, width, height);
  const x = displayBox.minX * width;
  const y = displayBox.minY * height;
  const w = Math.max(1, (displayBox.maxX - displayBox.minX) * width);
  const h = Math.max(1, (displayBox.maxY - displayBox.minY) * height);
  ctx.save();
  ctx.strokeStyle = 'rgba(23,32,47,0.86)';
  ctx.lineWidth = 1.5;
  ctx.setLineDash([7, 5]);
  ctx.strokeRect(x, y, w, h);
  ctx.setLineDash([]);
  ctx.fillStyle = 'rgba(255,255,255,0.96)';
  ctx.strokeStyle = 'rgba(37,84,166,0.95)';
  ctx.lineWidth = 2;
  getManualBoxHandles(box, displayBox).forEach(handle => {
    const hx = handle.x * width;
    const hy = handle.y * height;
    ctx.beginPath();
    ctx.rect(hx - 5, hy - 5, 10, 10);
    ctx.fill();
    ctx.stroke();
  });
  ctx.fillStyle = 'rgba(23,32,47,0.72)';
  ctx.font = '12px Inter, Arial, sans-serif';
  ctx.textAlign = 'left';
  ctx.textBaseline = 'bottom';
  ctx.fillText(localizeText('拖框内移动，拖控制点拉伸'), x, Math.max(14, y - 8));
  ctx.restore();
}

function getManualTransformHit(normPos) {
  const state = ensureManualCorrectionState();
  const box = state.lastBox || getManualTransformBox();
  if (!box) return { action: 'move', handle: null, box: null };
  const rect = EL.reportCanvas.getBoundingClientRect();
  const threshold = 12 / Math.max(1, Math.min(rect.width, rect.height));
  const displayBox = getManualBoxDisplayBox(box, rect.width, rect.height);
  const handle = getManualBoxHandles(box, displayBox).find(item =>
    Math.hypot(item.x - normPos.x, item.y - normPos.y) <= threshold
  );
  if (handle) return { action: 'scale', handle: handle.id, box };
  const inside = normPos.x >= displayBox.minX && normPos.x <= displayBox.maxX && normPos.y >= displayBox.minY && normPos.y <= displayBox.maxY;
  return { action: inside ? 'move' : 'move', handle: null, box };
}

function updateManualCursor(normPos = null) {
  const overlay = EL.manualCorrectionCanvas;
  if (!overlay || !isManualCorrectionActive()) return;
  const tool = EL.manualCorrectionTool?.value || 'transform';
  if (tool === 'erase' || tool === 'restore') {
    overlay.style.cursor = 'crosshair';
    return;
  }
  if (!normPos) {
    overlay.style.cursor = 'move';
    return;
  }
  const hit = getManualTransformHit(normPos);
  if (hit.action === 'scale' && hit.handle) {
    const rect = EL.reportCanvas.getBoundingClientRect();
    const displayBox = getManualBoxDisplayBox(hit.box, rect.width, rect.height);
    overlay.style.cursor = getManualBoxHandles(hit.box, displayBox).find(handle => handle.id === hit.handle)?.cursor || 'move';
  } else {
    overlay.style.cursor = 'move';
  }
}

function applyManualBrushAt(normPos, restore = false) {
  const run = State.currentReportRun;
  if (!run || !isManualCorrectionActive()) return;
  const state = ensureManualCorrectionState(run);
  const radius = state.brushRadius;
  getTimeFilteredReportPoints(run).forEach(({ point, index }) => {
    const raw = getRawA4Position(point, run);
    if (!raw) return;
    const corrected = applyA4Correction(raw, run, 'manual');
    if (Math.hypot(corrected.x - normPos.x, corrected.y - normPos.y) <= radius) {
      const key = getPointIdentity(point, index);
      if (restore) state.excluded.delete(key);
      else state.excluded.add(key);
    }
  });
  state.needsBaseRedraw = true;
  updateManualCorrectionPanel();
}

function handleManualPointerDown(event) {
  if (!isManualCorrectionActive()) return;
  const pos = getCanvasRelativePosition(event);
  if (!pos) return;
  const state = ensureManualCorrectionState();
  const tool = EL.manualCorrectionTool?.value || 'transform';
  const hit = tool === 'transform' ? getManualTransformHit(pos) : { action: tool, handle: null };
  state.pointer = {
    start: pos,
    current: pos,
    offsetX: state.offsetX,
    offsetY: state.offsetY,
    scaleX: state.scaleX,
    scaleY: state.scaleY,
    action: hit.action,
    handle: hit.handle,
    box: hit.box,
  };
  EL.manualCorrectionCanvas.setPointerCapture?.(event.pointerId);
  if (tool === 'erase' || tool === 'restore') {
    applyManualBrushAt(pos, tool === 'restore');
  }
  event.preventDefault();
}

function handleManualPointerMove(event) {
  if (!isManualCorrectionActive()) return;
  const state = ensureManualCorrectionState();
  const tool = EL.manualCorrectionTool?.value || 'transform';
  const pos = getCanvasRelativePosition(event, { clamp: !(state.pointer?.start && tool === 'transform') });
  if (!pos) return;
  if (!state.pointer?.start) {
    state.pointer = { current: pos };
    updateManualCursor(pos);
    drawManualOverlay();
    return;
  }
  state.pointer.current = pos;
  const dx = pos.x - state.pointer.start.x;
  const dy = pos.y - state.pointer.start.y;
  if (tool === 'transform' && state.pointer.action === 'move') {
    state.offsetX = Math.max(-1, Math.min(1, state.pointer.offsetX + dx));
    state.offsetY = Math.max(-1, Math.min(1, state.pointer.offsetY + dy));
    state.needsBaseRedraw = true;
    updateManualCorrectionPanel();
  } else if (tool === 'transform' && state.pointer.action === 'scale') {
    applyManualBoxScaleFromDrag(state, dx, dy);
    state.needsBaseRedraw = true;
    updateManualCorrectionPanel();
  } else if (tool === 'erase' || tool === 'restore') {
    applyManualBrushAt(pos, tool === 'restore');
  } else {
    drawManualOverlay();
  }
  event.preventDefault();
}

function applyManualBoxScaleFromDrag(state, dx, dy) {
  const handle = state.pointer?.handle || '';
  const box = state.pointer?.box;
  if (!box || !handle) return;

  const oldW = Math.max(0.001, box.maxX - box.minX);
  const oldH = Math.max(0.001, box.maxY - box.minY);
  const oldCx = (box.minX + box.maxX) / 2;
  const oldCy = (box.minY + box.maxY) / 2;
  const next = { ...box };
  if (handle.includes('w')) next.minX += dx;
  if (handle.includes('e')) next.maxX += dx;
  if (handle.includes('n')) next.minY += dy;
  if (handle.includes('s')) next.maxY += dy;

  const minSize = 0.04;
  if (next.maxX - next.minX < minSize) {
    if (handle.includes('w')) next.minX = next.maxX - minSize;
    else next.maxX = next.minX + minSize;
  }
  if (next.maxY - next.minY < minSize) {
    if (handle.includes('n')) next.minY = next.maxY - minSize;
    else next.maxY = next.minY + minSize;
  }

  const newW = Math.max(minSize, next.maxX - next.minX);
  const newH = Math.max(minSize, next.maxY - next.minY);
  const newCx = (next.minX + next.maxX) / 2;
  const newCy = (next.minY + next.maxY) / 2;
  const fx = handle === 'n' || handle === 's' ? 1 : newW / oldW;
  const fy = handle === 'e' || handle === 'w' ? 1 : newH / oldH;

  state.scaleX = Math.max(0.2, Math.min(4, state.pointer.scaleX * fx));
  state.scaleY = Math.max(0.2, Math.min(4, state.pointer.scaleY * fy));
  state.offsetX = Math.max(-1, Math.min(1, newCx - 0.5 - (oldCx - 0.5 - state.pointer.offsetX) * fx));
  state.offsetY = Math.max(-1, Math.min(1, newCy - 0.5 - (oldCy - 0.5 - state.pointer.offsetY) * fy));
}

function handleManualPointerUp(event) {
  if (!State.manualCorrection) return;
  const shouldRedraw = State.manualCorrection.needsBaseRedraw;
  State.manualCorrection.pointer = null;
  State.manualCorrection.needsBaseRedraw = false;
  EL.manualCorrectionCanvas?.releasePointerCapture?.(event.pointerId);
  updateManualCorrectionPanel();
  if (shouldRedraw) redrawCurrentVisualization();
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
      drawManualOverlay();
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
    if (includeLegend) drawLegend(ctx, canvas.width, canvas.height, options.legendLabels);
    updateReportRangeStatus(run, data.length);
    drawManualOverlay();
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
      drawManualOverlay();
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
        drawReportMessage(canvas, '有效坐标数据点不足', !includeBackground);
      }
      updateReportRangeStatus(run, data.length);
      drawManualOverlay();
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
    drawManualOverlay();
    options.onComplete?.(canvas);
  };
  img.src = imageSrc;
}

function drawLegend(ctx, w, h, labels = {}) {
  const lowLabel = labels.low || localizeText('低');
  const highLabel = labels.high || localizeText('高');
  const titleLabel = labels.title || localizeText('注意力密度');
  const lw = Math.min(360, Math.max(240, w * 0.24));
  const lh = Math.max(18, Math.min(28, w * 0.012));
  const x  = w - lw - 28;
  const y  = h - 58;

  ctx.fillStyle = 'rgba(0,0,0,0.5)';
  ctx.beginPath();
  ctx.roundRect(x - 12, y - 30, lw + 24, lh + 48, 8);
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
  ctx.font         = '15px Inter,sans-serif';
  ctx.textAlign    = 'left';
  ctx.textBaseline = 'top';
  ctx.fillText(lowLabel, x, y + lh + 5);
  ctx.textAlign = 'right';
  ctx.fillText(highLabel, x + lw, y + lh + 5);
  ctx.textAlign    = 'center';
  ctx.fillStyle    = 'rgba(255,255,255,0.55)';
  ctx.font         = '14px Inter,sans-serif';
  ctx.fillText(titleLabel, x + lw / 2, y - 22);
}

// ─── 聚合数据分析 ────────────────────────────────────────────────
const ANALYSIS_ZONE_LABELS = [
  '左上', '中上', '右上',
  '左中', '中心', '右中',
  '左下', '中下', '右下',
];

function getAnalysisZoneLabel(index) {
  return localizeText(ANALYSIS_ZONE_LABELS[index] || '');
}

function formatMetric(value, digits = 1, fallback = '—') {
  const number = Number(value);
  if (!Number.isFinite(number)) return fallback;
  return number.toFixed(digits);
}

function formatPercent(value, digits = 1) {
  const number = Number(value);
  if (!Number.isFinite(number)) return '—';
  return `${(number * 100).toFixed(digits)}%`;
}

function getRunImageName(run) {
  return String(run?.image?.name || run?.image?.id || '未命名图片');
}

function getRunImageKey(run) {
  return String(run?.image?.id || getRunImageName(run)).toLowerCase();
}

function getImageConditionMeta(image = {}) {
  const key = String(image.id || image.name || '').trim().toLowerCase();
  if (key === 'a2' || key === 'b2') return { condition: 'experiment', label: '实验组' };
  if (key === 'a1' || key === 'b1') return { condition: 'control', label: '对照组' };
  if (image.condition === 'experiment') return { condition: 'experiment', label: '实验组' };
  if (image.condition === 'control') return { condition: 'control', label: '对照组' };
  if (image.conditionLabel) return { condition: String(image.condition || ''), label: String(image.conditionLabel) };
  return { condition: String(image.condition || ''), label: '未分组' };
}

function getRunConditionLabel(run) {
  return getImageConditionMeta(run?.image).label;
}

function getPointA4Position(point, run) {
  const a4X = Number(point?.a4X);
  const a4Y = Number(point?.a4Y);
  if (Number.isFinite(a4X) && Number.isFinite(a4Y)) {
    return { x: clamp01(a4X), y: clamp01(a4Y) };
  }

  const plane = run?.a4Plane;
  if (plane && Number.isFinite(Number(point?.x)) && Number.isFinite(Number(point?.y))) {
    const mapped = virtualScreenToA4(Number(point.x), Number(point.y), plane);
    return { x: mapped.x, y: mapped.y };
  }

  return null;
}

function getA4ZoneIndex(pos) {
  const col = Math.min(2, Math.max(0, Math.floor(pos.x * 3)));
  const row = Math.min(2, Math.max(0, Math.floor(pos.y * 3)));
  return row * 3 + col;
}

function percentile(values, ratio) {
  if (!values.length) return null;
  const sorted = [...values].sort((a, b) => a - b);
  const index = (sorted.length - 1) * clamp01(ratio);
  const low = Math.floor(index);
  const high = Math.ceil(index);
  if (low === high) return sorted[low];
  return sorted[low] + (sorted[high] - sorted[low]) * (index - low);
}

function describeAnomalyFlags(flags) {
  if (!flags.length) return '正常';
  const labels = {
    lowValid: '有效点偏低',
    severeOffset: '严重偏移',
    edgeClipped: '边缘截断',
    tooShort: '样本过少',
  };
  return flags.map(flag => labels[flag] || flag).join('、');
}

function getRepairSuggestion(flags) {
  if (!flags.length) return '无需修正';
  if (flags.includes('tooShort')) return '样本过少，建议排除该记录或补采';
  if (flags.includes('lowValid') && flags.includes('edgeClipped')) return '优先仅使用有效点；不建议强修正';
  if (flags.includes('severeOffset')) return '疑似坐标系整体偏移，可尝试中心平移修正';
  if (flags.includes('lowValid')) return '建议筛除打印区域外点后再分析';
  if (flags.includes('edgeClipped')) return '疑似映射边界截断，谨慎拉伸';
  return '人工复核';
}

function getAutoCorrectionMode(metric) {
  if (!metric || !metric.anomalyFlags?.length) return 'raw';
  if (metric.anomalyFlags.includes('tooShort')) return 'raw';
  if (metric.anomalyFlags.includes('severeOffset')) return 'shift';
  return 'raw';
}

function computeRunMetrics(record) {
  const { session, run, trialIndex } = record;
  const points = Array.isArray(run.points) ? run.points : [];
  const zoneCounts = Array(9).fill(0);
  const duration = Math.max(0, Number(run.duration) || 0);
  let validCount = 0;
  let sumX = 0;
  let sumY = 0;
  let centerDistanceSum = 0;
  let pathLengthMm = 0;
  let previousPos = null;
  const validPositions = [];

  points.forEach(point => {
    const pos = getPointA4Position(point, run);
    if (!pos || point.onPaper === false) return;

    validCount += 1;
    validPositions.push(pos);
    sumX += pos.x;
    sumY += pos.y;
    centerDistanceSum += Math.hypot(pos.x - 0.5, pos.y - 0.5);
    zoneCounts[getA4ZoneIndex(pos)] += 1;

    if (previousPos) {
      const dxMm = (pos.x - previousPos.x) * A4_SIZE_MM.width;
      const dyMm = (pos.y - previousPos.y) * A4_SIZE_MM.height;
      pathLengthMm += Math.hypot(dxMm, dyMm);
    }
    previousPos = pos;
  });

  const xs = validPositions.map(pos => pos.x);
  const ys = validPositions.map(pos => pos.y);
  const p02x = percentile(xs, 0.02);
  const p98x = percentile(xs, 0.98);
  const p02y = percentile(ys, 0.02);
  const p98y = percentile(ys, 0.98);
  const robustWidth = p02x == null || p98x == null ? 0 : Math.max(0, p98x - p02x);
  const robustHeight = p02y == null || p98y == null ? 0 : Math.max(0, p98y - p02y);
  const robustCoverage = robustWidth * robustHeight;
  const edgeRate = validPositions.length
    ? validPositions.filter(pos => pos.x <= 0.02 || pos.x >= 0.98 || pos.y <= 0.02 || pos.y >= 0.98).length / validPositions.length
    : 0;
  const meanX = validCount ? sumX / validCount : null;
  const meanY = validCount ? sumY / validCount : null;
  const centerBias = validCount ? centerDistanceSum / validCount : null;
  const anomalyFlags = [];
  if (points.length < 120 || duration < 5) anomalyFlags.push('tooShort');
  if (points.length && validCount / points.length < 0.65) anomalyFlags.push('lowValid');
  if (centerBias != null && centerBias > 0.38 && robustCoverage < 0.28) anomalyFlags.push('severeOffset');
  if (edgeRate > 0.22) anomalyFlags.push('edgeClipped');
  const coverageNote = validCount >= 120 && (robustWidth < 0.45 || robustHeight < 0.45 || robustCoverage < 0.24)
    ? '视线集中在局部区域；这可能是正常观看行为，必要时可用范围拉伸做探索性预览。'
    : '';
  const offsetNote = centerBias != null && centerBias > 0.22 && !anomalyFlags.includes('severeOffset')
    ? '平均视线位置偏离中心；这可能来自观看内容本身，建议结合刺激图人工判断。'
    : '';

  return {
    participantId: session.id,
    participantLabel: session.label,
    trialId: run.id,
    trialIndex,
    imageId: String(run.image?.id || ''),
    imageName: getRunImageName(run),
    condition: getRunConditionLabel(run),
    startedAt: run.startedAt || '',
    duration,
    points: points.length,
    validPoints: validCount,
    validRate: points.length ? validCount / points.length : 0,
    fps: duration > 0 ? points.length / duration : 0,
    meanX,
    meanY,
    centerBias,
    robustBounds: { minX: p02x, maxX: p98x, minY: p02y, maxY: p98y },
    robustWidth,
    robustHeight,
    robustCoverage,
    coverageNote,
    offsetNote,
    edgeRate,
    anomalyFlags,
    anomalyLabel: describeAnomalyFlags(anomalyFlags),
    repairSuggestion: getRepairSuggestion(anomalyFlags),
    autoCorrectionMode: getAutoCorrectionMode({ anomalyFlags }),
    pathLengthMm,
    zoneCounts,
  };
}

function aggregateMetrics(metrics) {
  const zoneCounts = Array(9).fill(0);
  const participants = new Set();
  let durationSum = 0;
  let pointSum = 0;
  let validPointSum = 0;
  let weightedX = 0;
  let weightedY = 0;
  let weightedCenterBias = 0;
  let pathLengthSum = 0;
  let anomalyRuns = 0;

  metrics.forEach(metric => {
    participants.add(metric.participantId);
    durationSum += metric.duration;
    pointSum += metric.points;
    validPointSum += metric.validPoints;
    pathLengthSum += metric.pathLengthMm;
    if (metric.meanX != null) weightedX += metric.meanX * metric.validPoints;
    if (metric.meanY != null) weightedY += metric.meanY * metric.validPoints;
    if (metric.centerBias != null) weightedCenterBias += metric.centerBias * metric.validPoints;
    metric.zoneCounts.forEach((count, index) => { zoneCounts[index] += count; });
    if (metric.anomalyFlags?.length) anomalyRuns += 1;
  });

  return {
    runs: metrics.length,
    participants: participants.size,
    points: pointSum,
    validPoints: validPointSum,
    validRate: pointSum ? validPointSum / pointSum : 0,
    durationTotal: durationSum,
    durationAvg: metrics.length ? durationSum / metrics.length : 0,
    fpsAvg: durationSum > 0 ? pointSum / durationSum : 0,
    meanX: validPointSum ? weightedX / validPointSum : null,
    meanY: validPointSum ? weightedY / validPointSum : null,
    centerBias: validPointSum ? weightedCenterBias / validPointSum : null,
    pathLengthAvgMm: metrics.length ? pathLengthSum / metrics.length : 0,
    anomalyRuns,
    zoneCounts,
  };
}

function groupMetrics(metrics, getKey, getLabel = getKey) {
  const groups = new Map();
  metrics.forEach(metric => {
    const key = getKey(metric);
    if (!groups.has(key)) groups.set(key, { key, label: getLabel(metric), metrics: [] });
    groups.get(key).metrics.push(metric);
  });

  return Array.from(groups.values())
    .map(group => ({ ...group, summary: aggregateMetrics(group.metrics) }))
    .sort((a, b) => b.summary.runs - a.summary.runs || a.label.localeCompare(b.label, getDisplayLocale()));
}

function getAllAnalysisRecords() {
  return getAllTrackingRuns().filter(record => Array.isArray(record.run.points));
}

function getScopedAnalysisRecords() {
  const scope = EL.analysisScopeSelect?.value || 'all';
  const imageFilter = EL.analysisImageSelect?.value || 'all';
  let records = getAllAnalysisRecords();

  if (scope === 'session' && State.selectedSessionId) {
    records = records.filter(record => record.session.id === State.selectedSessionId);
  } else if (scope === 'run' && State.currentReportRun) {
    records = records.filter(record => record.run === State.currentReportRun || record.run.id === State.currentReportRun.id);
  }

  if (imageFilter !== 'all') {
    records = records.filter(record => getRunImageKey(record.run) === imageFilter);
  }

  return records;
}

function updateAnalysisImageOptions() {
  if (!EL.analysisImageSelect) return;
  const previous = EL.analysisImageSelect.value || 'all';
  const options = groupMetrics(
    getAllAnalysisRecords().map(computeRunMetrics),
    metric => String(metric.imageId || metric.imageName).toLowerCase(),
    metric => metric.imageName
  );

  EL.analysisImageSelect.innerHTML = '<option value="all">全部图片</option>';
  options.forEach(group => {
    const option = document.createElement('option');
    option.value = group.key;
    option.textContent = `${group.label} (${group.summary.runs})`;
    EL.analysisImageSelect.appendChild(option);
  });
  EL.analysisImageSelect.value = Array.from(EL.analysisImageSelect.options).some(option => option.value === previous)
    ? previous
    : 'all';
}

function buildAnalysisInsights(snapshot) {
  const insights = [];
  const { overall, conditions, images } = snapshot;
  if (!overall.runs) return ['暂无可分析记录。'];

  insights.push(`共 ${overall.participants} 名参与者、${overall.runs} 次追踪、${overall.points.toLocaleString()} 个采样点。`);
  if (overall.anomalyRuns) {
    insights.push(`筛查出 ${overall.anomalyRuns} 次疑似技术异常记录，局部凝视不会单独计为异常。`);
  }
  insights.push(`打印区域有效点比例为 ${formatPercent(overall.validRate)}，平均采样频率 ${formatMetric(overall.fpsAvg, 1)} Hz。`);

  const topZoneIndex = overall.zoneCounts.reduce((best, count, index, arr) => count > arr[best] ? index : best, 0);
  const topZoneCount = overall.zoneCounts[topZoneIndex] || 0;
  if (topZoneCount) {
    insights.push(`视线最集中区域是「${ANALYSIS_ZONE_LABELS[topZoneIndex]}」，占有效点 ${formatPercent(topZoneCount / Math.max(1, overall.validPoints))}。`);
  }

  if (conditions.length >= 2) {
    const sorted = [...conditions].sort((a, b) => b.summary.validRate - a.summary.validRate);
    const diff = sorted[0].summary.validRate - sorted[sorted.length - 1].summary.validRate;
    insights.push(`条件有效率最高的是「${sorted[0].label}」，比最低条件高 ${formatPercent(diff)}。`);
  }

  if (images.length) {
    const longestPath = [...images].sort((a, b) => b.summary.pathLengthAvgMm - a.summary.pathLengthAvgMm)[0];
    insights.push(`平均视线移动路径最长的图片是「${longestPath.label}」，约 ${formatMetric(longestPath.summary.pathLengthAvgMm, 0)} mm。`);
  }

  return insights;
}

function createAnalysisSnapshot() {
  const records = getScopedAnalysisRecords();
  const metrics = records.map(computeRunMetrics);
  const conditions = groupMetrics(metrics, metric => metric.condition);
  const images = groupMetrics(metrics, metric => String(metric.imageId || metric.imageName).toLowerCase(), metric => metric.imageName);
  const overall = aggregateMetrics(metrics);
  const snapshot = {
    createdAt: new Date().toISOString(),
    scope: EL.analysisScopeSelect?.value || 'all',
    imageFilter: EL.analysisImageSelect?.value || 'all',
    overall,
    runs: metrics,
    anomalies: metrics.filter(metric => metric.anomalyFlags.length),
    conditions,
    images,
    insights: [],
  };
  snapshot.insights = buildAnalysisInsights(snapshot);
  return snapshot;
}

function renderAnalysisSummary(overall) {
  const cards = [
    ['参与者', overall.participants.toLocaleString(), 'people'],
    ['追踪记录', overall.runs.toLocaleString(), 'runs'],
    ['采样点', overall.points.toLocaleString(), 'points'],
    ['有效点比例', formatPercent(overall.validRate), 'valid'],
    ['疑似异常', overall.anomalyRuns.toLocaleString(), 'anomaly'],
    ['平均频率', `${formatMetric(overall.fpsAvg, 1)} Hz`, 'fps'],
  ];
  EL.analysisSummaryGrid.innerHTML = cards.map(([label, value, tone]) => `
    <div class="analysis-summary-card analysis-tone-${tone}">
      <span>${label}</span>
      <strong>${value}</strong>
    </div>
  `).join('');
}

function renderAnalysisTable(tbody, groups, mode) {
  tbody.innerHTML = '';
  if (!groups.length) {
    tbody.innerHTML = '<tr><td colspan="6">暂无数据</td></tr>';
    return;
  }

  tbody.innerHTML = groups.map(group => {
    const s = group.summary;
    if (mode === 'image') {
      const condition = group.metrics[0]?.condition || '未分组';
      return `
        <tr>
          <td>${escapeHtml(group.label)}</td>
          <td>${escapeHtml(condition)}</td>
          <td>${s.runs}</td>
          <td>${formatPercent(s.validRate)}</td>
          <td>${s.meanX == null ? '—' : `${formatMetric(s.meanX, 2)} / ${formatMetric(s.meanY, 2)}`}</td>
          <td>${formatMetric(s.pathLengthAvgMm, 0)} mm</td>
        </tr>
      `;
    }

    return `
      <tr>
        <td>${escapeHtml(group.label)}</td>
        <td>${s.runs}</td>
        <td>${s.points.toLocaleString()}</td>
        <td>${formatPercent(s.validRate)}</td>
        <td>${formatMetric(s.durationAvg, 1)} s</td>
        <td>${formatMetric(s.centerBias, 2)}</td>
      </tr>
    `;
  }).join('');
}

function renderAnalysisZones(overall) {
  const max = Math.max(1, ...overall.zoneCounts);
  EL.analysisZoneTotal.textContent = `${overall.validPoints.toLocaleString()} 点`;
  EL.analysisZoneGrid.innerHTML = overall.zoneCounts.map((count, index) => {
    const ratio = overall.validPoints ? count / overall.validPoints : 0;
    const intensity = count / max;
    return `
      <div class="analysis-zone-cell" style="--zone-alpha:${intensity.toFixed(3)}">
        <span>${ANALYSIS_ZONE_LABELS[index]}</span>
        <strong>${formatPercent(ratio, 1)}</strong>
        <small>${count.toLocaleString()} 点</small>
      </div>
    `;
  }).join('');
}

function renderAnalysisAnomalies(anomalies) {
  EL.analysisAnomalyCount.textContent = anomalies.length;
  if (!anomalies.length) {
    EL.analysisAnomalyTable.innerHTML = '<tr><td colspan="5">当前范围内未发现明显技术异常。局部凝视不单独计为异常。</td></tr>';
    return;
  }

  EL.analysisAnomalyTable.innerHTML = anomalies
    .sort((a, b) => b.anomalyFlags.length - a.anomalyFlags.length || b.centerBias - a.centerBias)
    .map(metric => `
      <tr>
        <td>${escapeHtml(metric.participantLabel)} / ${escapeHtml(metric.imageName)}</td>
        <td>${escapeHtml(metric.anomalyLabel)}</td>
        <td>${formatMetric(metric.robustWidth, 2)} x ${formatMetric(metric.robustHeight, 2)}</td>
        <td>${formatMetric(metric.centerBias, 2)}</td>
        <td>${escapeHtml(metric.coverageNote || metric.offsetNote || metric.repairSuggestion)}</td>
      </tr>
    `).join('');
}

function updateAnalysisDashboard() {
  if (!EL.analysisSummaryGrid) return;
  updateAnalysisImageOptions();
  const snapshot = createAnalysisSnapshot();
  State.latestAnalysisSnapshot = snapshot;

  const scopeText = {
    all: '全部数据',
    session: '当前参与者',
    run: '当前记录',
  }[snapshot.scope] || '全部数据';
  EL.analysisScopeNote.textContent = `${scopeText} · ${snapshot.overall.runs} 次记录 · ${snapshot.overall.points.toLocaleString()} 点`;
  EL.analysisConditionCount.textContent = snapshot.conditions.length;
  EL.analysisImageCount.textContent = snapshot.images.length;

  renderAnalysisSummary(snapshot.overall);
  renderAnalysisTable(EL.analysisConditionTable, snapshot.conditions, 'condition');
  renderAnalysisTable(EL.analysisImageTable, snapshot.images, 'image');
  renderAnalysisZones(snapshot.overall);
  renderAnalysisAnomalies(snapshot.anomalies);

  EL.analysisInsightCount.textContent = snapshot.insights.length;
  EL.analysisInsights.innerHTML = snapshot.insights.map(text => `<li>${escapeHtml(text)}</li>`).join('');
}

function analysisCsvRows(snapshot) {
  const rows = [[
    'level', 'key', 'label', 'participants', 'runs', 'points', 'valid_points',
    'valid_rate', 'avg_duration_s', 'avg_fps', 'mean_x', 'mean_y',
    'center_bias', 'avg_path_length_mm', 'anomaly_runs', 'robust_width',
    'robust_height', 'edge_rate', 'anomaly_label', 'repair_suggestion', 'observation_note',
  ]];
  const pushSummary = (level, key, label, summary) => {
    rows.push([
      level,
      key,
      label,
      summary.participants,
      summary.runs,
      summary.points,
      summary.validPoints,
      summary.validRate,
      summary.durationAvg,
      summary.fpsAvg,
      summary.meanX ?? '',
      summary.meanY ?? '',
      summary.centerBias ?? '',
      summary.pathLengthAvgMm,
      summary.anomalyRuns ?? '',
      '', '', '', '', '', '',
    ]);
  };

  pushSummary('overall', 'all', '全部数据', snapshot.overall);
  snapshot.conditions.forEach(group => pushSummary('condition', group.key, group.label, group.summary));
  snapshot.images.forEach(group => pushSummary('image', group.key, group.label, group.summary));
  snapshot.overall.zoneCounts.forEach((count, index) => {
    rows.push([
      'zone',
      index + 1,
      getAnalysisZoneLabel(index),
      '',
      '',
      '',
      count,
      snapshot.overall.validPoints ? count / snapshot.overall.validPoints : 0,
      '', '', '', '', '', '', '', '', '', '', '', '', '',
    ]);
  });

  snapshot.anomalies.forEach(metric => {
    rows.push([
      'anomaly',
      metric.trialId,
      `${metric.participantLabel} / ${metric.imageName}`,
      '',
      1,
      metric.points,
      metric.validPoints,
      metric.validRate,
      metric.duration,
      metric.fps,
      metric.meanX ?? '',
      metric.meanY ?? '',
      metric.centerBias ?? '',
      metric.pathLengthMm,
      '',
      metric.robustWidth,
      metric.robustHeight,
      metric.edgeRate,
      metric.anomalyLabel,
      metric.repairSuggestion,
      metric.coverageNote || metric.offsetNote || '',
    ]);
  });

  return rows.map(row => row.map(csvCell).join(',')).join('\n');
}

function exportAnalysisCSV() {
  const snapshot = State.latestAnalysisSnapshot || createAnalysisSnapshot();
  if (!snapshot.overall.runs) { alert('暂无可导出的分析数据'); return; }
  downloadBlob(
    `eye_tracking_analysis_${new Date().toISOString().replace(/[:.]/g, '-')}.csv`,
    analysisCsvRows(snapshot),
    'text/csv;charset=utf-8;'
  );
}

function exportAnalysisJSON() {
  const snapshot = State.latestAnalysisSnapshot || createAnalysisSnapshot();
  if (!snapshot.overall.runs) { alert('暂无可导出的分析数据'); return; }
  downloadBlob(
    `eye_tracking_analysis_${new Date().toISOString().replace(/[:.]/g, '-')}.json`,
    JSON.stringify(snapshot, null, 2),
    'application/json;charset=utf-8;'
  );
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

function renderVisualizationCanvas(mode, run, data, options = {}) {
  return new Promise((resolve, reject) => {
    const canvas = document.createElement('canvas');
    const renderOptions = {
      canvas,
      run,
      data,
      includeBackground: options.includeBackground ?? true,
      includeLegend: options.includeLegend ?? (mode === 'heatmap'),
      legendLabels: options.legendLabels,
      useNaturalSize: true,
      silentEmpty: options.silentEmpty ?? false,
      onError: reject,
      onComplete: () => resolve(canvas),
    };
    if (mode === 'heatmap') drawHeatmap(renderOptions);
    else drawGazePlot(renderOptions);
  });
}

function drawFigureText(ctx, text, x, y, maxWidth, lineHeight, options = {}) {
  const rawText = String(text || '');
  const words = /\s/.test(rawText)
    ? rawText.split(/\s+/)
    : Array.from(rawText);
  const lines = [];
  let current = '';
  words.forEach(word => {
    const next = current ? `${current} ${word}` : word;
    if (ctx.measureText(next).width <= maxWidth || !current) current = next;
    else {
      lines.push(current);
      current = word;
    }
  });
  if (current) lines.push(current);
  const limit = options.maxLines || lines.length;
  lines.slice(0, limit).forEach((line, index) => ctx.fillText(line, x, y + index * lineHeight));
  return Math.min(lines.length, limit) * lineHeight;
}

function drawFigureMetric(ctx, label, value, x, y, w, h, accent = '#2554a6') {
  ctx.fillStyle = '#f8fafc';
  ctx.strokeStyle = '#d9e0ea';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.roundRect(x, y, w, h, 12);
  ctx.fill();
  ctx.stroke();
  ctx.fillStyle = accent;
  ctx.fillRect(x, y, 7, h);
  ctx.fillStyle = '#596579';
  ctx.font = '22px Inter, Arial, sans-serif';
  ctx.textAlign = 'left';
  ctx.textBaseline = 'top';
  ctx.fillText(label, x + 24, y + 20);
  ctx.fillStyle = '#17202f';
  ctx.font = '700 34px Inter, Arial, sans-serif';
  ctx.fillText(value, x + 24, y + 54);
}

function getAcademicConditionLabel(run) {
  const meta = getImageConditionMeta(run?.image);
  if (meta.condition === 'experiment') return 'Experimental';
  if (meta.condition === 'control') return 'Control';
  if (meta.condition === 'external') return 'External';
  return 'Ungrouped';
}

function getAcademicCorrectionLabel(mode) {
  return {
    raw: 'Raw coordinates',
    shift: 'Center-shift correction',
    stretch: 'Range-stretch correction',
    auto: 'Auto correction',
    manual: 'Manual correction',
  }[mode] || 'Raw coordinates';
}

function normalizeAcademicText(value, fallback) {
  return String(value || fallback || '')
    .replace(/当前参与者/g, 'Current participant')
    .replace(/未知参与者/g, 'Unknown participant')
    .replace(/未知图片/g, 'Unknown image')
    .replace(/未命名图片/g, 'Unnamed image')
    .replace(/外部图片/g, 'External image')
    .replace(/修正版/g, 'Corrected Version ')
    .replace(/对照组/g, 'Control')
    .replace(/实验组/g, 'Experimental')
    .replace(/未分组/g, 'Ungrouped')
    .replace(/\s+/g, ' ')
    .trim();
}

function getAcademicPointPositions(run, data) {
  return data
    .map(point => {
      const raw = getRawA4Position(point, run);
      if (!raw) return null;
      const corrected = applyA4Correction(raw, run);
      return {
        x: clamp01(corrected.x),
        y: clamp01(corrected.y),
      };
    })
    .filter(Boolean);
}

function computeAcademicAttentionMetrics(run, data, range) {
  const positions = getAcademicPointPositions(run, data);
  const sampleCount = data.length;
  const duration = Math.max(0, Number(range?.end) - Number(range?.start)) || Math.max(0, Number(run?.duration) || 0);

  const coverageGrid = 42;
  const occupied = new Set();
  positions.forEach(pos => {
    const col = Math.min(coverageGrid - 1, Math.max(0, Math.floor(pos.x * coverageGrid)));
    const row = Math.min(coverageGrid - 1, Math.max(0, Math.floor(pos.y * coverageGrid)));
    for (let dy = -1; dy <= 1; dy++) {
      for (let dx = -1; dx <= 1; dx++) {
        const x = col + dx;
        const y = row + dy;
        if (x >= 0 && x < coverageGrid && y >= 0 && y < coverageGrid) occupied.add(`${x}:${y}`);
      }
    }
  });
  const readingCoverage = positions.length ? occupied.size / (coverageGrid * coverageGrid) : 0;

  const densityGrid = 32;
  const density = new Map();
  const sequence = positions.map(pos => {
    const col = Math.min(densityGrid - 1, Math.max(0, Math.floor(pos.x * densityGrid)));
    const row = Math.min(densityGrid - 1, Math.max(0, Math.floor(pos.y * densityGrid)));
    const key = `${col}:${row}`;
    density.set(key, (density.get(key) || 0) + 1);
    return key;
  });
  const maxDensity = Math.max(0, ...density.values());
  const yellowThreshold = Math.max(3, Math.ceil(maxDensity * 0.62));
  const deepCells = new Set([...density.entries()]
    .filter(([, count]) => count >= yellowThreshold)
    .map(([key]) => key));
  let deepReadingCount = 0;
  let wasDeep = false;
  sequence.forEach(key => {
    const isDeep = deepCells.has(key);
    if (isDeep && !wasDeep) deepReadingCount += 1;
    wasDeep = isDeep;
  });

  return {
    sampleCount,
    duration,
    readingCoverage,
    deepReadingCount,
  };
}

async function renderAcademicFigureCanvas(run, data, options = {}) {
  const mode = options.mode || getCurrentVizMode();
  const source = await renderVisualizationCanvas(mode, run, data, {
    includeBackground: true,
    includeLegend: mode === 'heatmap',
    legendLabels: {
      low: 'Low',
      high: 'High',
      title: 'Attention Density',
    },
  });
  const record = findRunRecord(run);
  const range = options.range || getReportTimeRange(run);
  const correctionMode = resolveCorrectionMode(run, State.reportCorrectionMode);
  const metrics = computeAcademicAttentionMetrics(run, data, range);
  const figure = document.createElement('canvas');
  const width = 2200;
  const margin = 140;
  const imageWidth = width - margin * 2;
  const scale = Math.min(1, imageWidth / source.width);
  const imageHeight = Math.round(source.height * scale);
  const headerH = 210;
  const metricsH = 170;
  const footerH = 92;
  figure.width = width;
  figure.height = headerH + imageHeight + metricsH + footerH;

  const ctx = figure.getContext('2d');
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, figure.width, figure.height);
  ctx.fillStyle = '#17202f';
  ctx.textAlign = 'left';
  ctx.textBaseline = 'top';
  ctx.font = '700 54px Inter, Arial, sans-serif';
  ctx.fillText(mode === 'heatmap' ? 'Gaze Heatmap Analysis' : 'Gaze Sequence Analysis', margin, 70);
  ctx.font = '28px Inter, Arial, sans-serif';
  ctx.fillStyle = '#596579';
  const subtitle = [
    normalizeAcademicText(record?.session?.label, 'Unknown participant'),
    normalizeAcademicText(run.image?.name, 'Unknown image'),
    getAcademicConditionLabel(run),
    `${range.start.toFixed(1)}-${range.end.toFixed(1)} s`,
    getAcademicCorrectionLabel(correctionMode),
  ].join(' · ');
  drawFigureText(ctx, subtitle, margin, 138, imageWidth, 34, { maxLines: 2 });

  const imgX = margin;
  const imgY = headerH;
  ctx.strokeStyle = '#b9c5d6';
  ctx.lineWidth = 3;
  ctx.strokeRect(imgX - 1, imgY - 1, imageWidth + 2, imageHeight + 2);
  ctx.drawImage(source, imgX, imgY, imageWidth, imageHeight);

  const metricsY = imgY + imageHeight + 48;
  const cardGap = 28;
  const cardW = (imageWidth - cardGap * 2) / 3;
  drawFigureMetric(ctx, 'Samples / Duration', `${metrics.sampleCount.toLocaleString('en-US')} / ${metrics.duration.toFixed(1)} s`, margin, metricsY, cardW, 118, '#2554a6');
  drawFigureMetric(ctx, 'Reading Coverage', `${(metrics.readingCoverage * 100).toFixed(1)}%`, margin + (cardW + cardGap), metricsY, cardW, 118, '#1d8fa3');
  drawFigureMetric(ctx, 'Deep Reading Episodes', metrics.deepReadingCount.toLocaleString('en-US'), margin + (cardW + cardGap) * 2, metricsY, cardW, 118, '#d97a2b');

  ctx.fillStyle = '#8792a3';
  ctx.font = '20px Inter, Arial, sans-serif';
  ctx.fillText(`Generated by SIGN Visual Attention v3 · ${new Date().toLocaleString('en-US', { hour12: false })}`, margin, figure.height - 52);
  return figure;
}

async function exportAcademicFigure() {
  const run = State.currentReportRun;
  if (!run) {
    alert('请先选择一次追踪记录。');
    return;
  }

  const mode = getCurrentVizMode();
  const data = getFilteredReportPoints(run);
  const minPoints = mode === 'heatmap' ? 3 : 2;
  if (data.length < minPoints) {
    alert('当前时间段的数据点不足，无法导出学术图片。');
    return;
  }

  try {
    const figure = await renderAcademicFigureCanvas(run, data, {
      mode,
      range: getReportTimeRange(run),
    });
    const record = findRunRecord(run);
    downloadCanvasPng(
      `academic_${mode}_${safeFileName(record?.session?.label || 'participant')}_${safeFileName(run.image?.name || 'image')}.png`,
      figure
    );
  } catch (err) {
    alert(`无法导出学术图片：${err.message}`);
  }
}

function getAcademicBatchRecordLabel(record, index) {
  const run = record.run;
  const participant = normalizeAcademicText(record.session?.label, `Participant ${index + 1}`);
  const imageName = normalizeAcademicText(run.image?.name, 'Unknown image');
  const condition = getAcademicConditionLabel(run);
  return `${participant} · ${imageName} · ${condition}`;
}

function getAcademicBatchRecordMeta(record) {
  const run = record.run;
  const points = Array.isArray(run.points) ? run.points.length : 0;
  const duration = Math.max(0, Number(run.duration) || 0);
  return `${points.toLocaleString()} points · ${duration.toFixed(1)} s`;
}

function renderAcademicBatchOptions(records) {
  State.academicBatchRecords = records;
  if (EL.academicBatchSummary) {
    EL.academicBatchSummary.textContent = `${records.length.toLocaleString()} ${localizeText('记录')} · ${localizeText('按当前分析范围选择需要导出的追踪记录。')}`;
  }
  if (!EL.academicBatchList) return;
  EL.academicBatchList.innerHTML = records.map((record, index) => `
    <label class="academic-batch-option">
      <input type="checkbox" class="academic-batch-checkbox" value="${index}" checked />
      <span>
        <strong>${escapeHtml(getAcademicBatchRecordLabel(record, index))}</strong>
        <span>${escapeHtml(getAcademicBatchRecordMeta(record))}</span>
      </span>
    </label>
  `).join('');
}

function openAcademicBatchExportMenu() {
  const records = getScopedAnalysisRecords();
  if (!records.length) {
    alert('暂无可导出的分析数据');
    return;
  }
  renderAcademicBatchOptions(records);
  showModal(EL.academicBatchModal);
}

function setAcademicBatchSelection(checked) {
  EL.academicBatchList?.querySelectorAll('.academic-batch-checkbox')
    .forEach(input => { input.checked = checked; });
}

function getSelectedAcademicBatchRecords() {
  const records = State.academicBatchRecords || [];
  return Array.from(EL.academicBatchList?.querySelectorAll('.academic-batch-checkbox:checked') || [])
    .map(input => records[Number(input.value)])
    .filter(Boolean);
}

async function startSelectedAcademicBatchExport() {
  const records = getSelectedAcademicBatchRecords();
  if (!records.length) {
    alert('请至少选择一条记录。');
    return;
  }
  hideModal(EL.academicBatchModal);
  await exportAcademicFiguresBatch(records);
}

async function exportAcademicFiguresBatch(records = getScopedAnalysisRecords()) {
  if (!records.length) {
    alert('暂无可导出的分析数据');
    return;
  }

  const mode = getCurrentVizMode();
  const originalCorrectionMode = State.reportCorrectionMode;
  if (originalCorrectionMode === 'manual') {
    State.reportCorrectionMode = 'raw';
  }

  EL.exportAcademicBatchBtn.disabled = true;
  let exported = 0;
  let skipped = 0;
  try {
    for (const record of records) {
      const run = record.run;
      const data = Array.isArray(run.points) ? run.points : [];
      const minPoints = mode === 'heatmap' ? 3 : 2;
      if (data.length < minPoints) {
        skipped += 1;
        continue;
      }
      const duration = Math.max(0, Number(run.duration) || 0);
      const figure = await renderAcademicFigureCanvas(run, data, {
        mode,
        range: { start: 0, end: duration, duration },
      });
      downloadCanvasPng(
        `academic_${mode}_${safeFileName(record.session?.label || 'participant')}_${safeFileName(run.image?.name || 'image')}.png`,
        figure
      );
      exported += 1;
      await wait(250);
    }
    alert(`批量导出完成：${exported} 张${skipped ? `，跳过 ${skipped} 条点数不足记录` : ''}`);
  } catch (err) {
    alert(`无法导出学术图片：${err.message}`);
  } finally {
    State.reportCorrectionMode = originalCorrectionMode;
    EL.exportAcademicBatchBtn.disabled = false;
  }
}

function resetManualCorrection() {
  State.manualCorrection = createManualCorrectionState();
  State.manualCorrectionRunKey = getRunManualKey();
  updateManualCorrectionPanel();
  redrawCurrentVisualization();
}

function createCorrectedVersionId(session, sourceRun) {
  const base = `${sourceRun.id}-manual`;
  const used = new Set((session?.runs || []).map(run => run.id));
  let id = base;
  let suffix = 2;
  while (used.has(id)) {
    id = `${base}-${suffix}`;
    suffix += 1;
  }
  return id;
}

function getManualSaveEntries(sourceRun, state) {
  const excluded = state?.excluded || new Set();
  const retain = ({ point, index }) => !excluded.has(getPointIdentity(point, index));
  const rangedEntries = getTimeFilteredReportPoints(sourceRun).filter(retain);
  if (rangedEntries.length) {
    return { entries: rangedEntries, usedFallback: false };
  }

  const allEntries = (sourceRun?.points || [])
    .map((point, index) => ({ point, index }))
    .filter(retain);
  return { entries: allEntries, usedFallback: true };
}

function saveCorrectedVersion() {
  const sourceRun = State.currentReportRun;
  const record = findRunRecord(sourceRun);
  if (!sourceRun || !record) {
    alert('请先选择一次追踪记录。');
    return;
  }
  if (!isManualCorrectionActive(sourceRun)) {
    alert('请先将坐标修正模式切换为“手动修正”。');
    return;
  }

  const state = ensureManualCorrectionState(sourceRun);
  const range = getReportTimeRange(sourceRun);
  const { entries, usedFallback } = getManualSaveEntries(sourceRun, state);
  if (!entries.length) {
    alert('没有可保存的数据点。请调整有效时间段或恢复被涂抹的点。');
    return;
  }

  const plane = sourceRun.a4Plane || record.session.a4Plane || State.currentA4Plane;
  const correctedPoints = entries.map(({ point }, index) => {
    const raw = getRawA4Position(point, sourceRun);
    const corrected = raw ? applyA4Correction(raw, sourceRun, 'manual') : null;
    const a4X = corrected ? clamp01(corrected.x) : undefined;
    const a4Y = corrected ? clamp01(corrected.y) : undefined;
    return {
      ...point,
      index: index + 1,
      x: corrected && plane ? plane.left + a4X * plane.width : point.x,
      y: corrected && plane ? plane.top + a4Y * plane.height : point.y,
      a4X,
      a4Y,
      a4Xmm: a4X == null ? undefined : a4X * A4_SIZE_MM.width,
      a4Ymm: a4Y == null ? undefined : a4Y * A4_SIZE_MM.height,
      onPaper: corrected ? true : point.onPaper,
    };
  });

  const existingVersions = record.session.runs.filter(run => run.sourceRunId === sourceRun.id || run.manualCorrection?.sourceRunId === sourceRun.id).length;
  const versionNo = existingVersions + 1;
  const correctedRun = {
    ...sourceRun,
    id: createCorrectedVersionId(record.session, sourceRun),
    startedAt: sourceRun.startedAt,
    endedAt: new Date().toISOString(),
    duration: usedFallback ? Math.max(0, Number(sourceRun.duration) || 0) : Math.max(0, range.end - range.start),
    image: {
      ...sourceRun.image,
      name: `${sourceRun.image?.name || 'image'} 修正版${versionNo}`,
    },
    coordinateSystem: 'a4-landscape-paper',
    a4Plane: plane ? { ...plane } : sourceRun.a4Plane,
    paperSizeMm: { ...A4_SIZE_MM },
    points: correctedPoints,
    sourceRunId: sourceRun.id,
    versionLabel: `手动修正版 ${versionNo}`,
    manualCorrection: {
      sourceRunId: sourceRun.id,
      createdAt: new Date().toISOString(),
      timeRange: usedFallback
        ? { start: 0, end: Math.max(0, Number(sourceRun.duration) || 0), fallbackToFullRun: true }
        : { start: range.start, end: range.end },
      offsetX: state.offsetX,
      offsetY: state.offsetY,
      scaleX: state.scaleX,
      scaleY: state.scaleY,
      brushRadius: state.brushRadius,
      excludedPointCount: state.excluded.size,
      retainedPointCount: correctedPoints.length,
    },
  };

  const sourceIndex = record.session.runs.findIndex(run => run === sourceRun || run.id === sourceRun.id);
  if (sourceIndex >= 0) record.session.runs.splice(sourceIndex + 1, 0, correctedRun);
  else record.session.runs.push(correctedRun);
  State.selectedSessionId = record.session.id;
  State.currentReportRun = correctedRun;
  State.gazeHistory = correctedRun.points;
  State.uploadedImageSrc = correctedRun.imageSrc;
  State.reportCorrectionMode = 'raw';
  EL.vizCorrectionMode.value = 'raw';
  State.manualCorrection = null;
  State.manualCorrectionRunKey = '';
  State.archiveDirty = true;
  State.archiveUnloadPrompted = false;
  resetReportTimeRange(correctedRun);
  renderDataWorkbench();
  updateReportFromCurrentRun();
  updateAnalysisDashboard();
  updateManualCorrectionPanel();
  alert(`已另存为修正版：${correctedRun.image.name}`);
}

function exportAnalysisFigure() {
  const snapshot = State.latestAnalysisSnapshot || createAnalysisSnapshot();
  if (!snapshot.overall.runs) {
    alert('暂无可导出的分析数据');
    return;
  }

  const canvas = document.createElement('canvas');
  canvas.width = 2200;
  canvas.height = 1600;
  const ctx = canvas.getContext('2d');
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  const margin = 120;
  ctx.fillStyle = '#17202f';
  ctx.font = '700 58px Inter, Arial, sans-serif';
  ctx.textAlign = 'left';
  ctx.textBaseline = 'top';
  ctx.fillText(localizeText('整体眼动分析'), margin, 80);
  ctx.fillStyle = '#596579';
  ctx.font = '28px Inter, Arial, sans-serif';
  drawFigureText(
    ctx,
    `${localizeText('分析范围')}: ${localizeText({ all: '全部数据', session: '当前参与者', run: '当前记录' }[snapshot.scope] || snapshot.scope)} · ${localizeText('记录')}: ${snapshot.overall.runs} · ${localizeText('样本数')}: ${snapshot.overall.points.toLocaleString()} · ${localizeText('生成时间')} ${new Date().toLocaleString(getDisplayLocale(), { hour12: false })}`,
    margin,
    155,
    1800,
    36,
    { maxLines: 2 }
  );

  const cards = [
    [localizeText('参与者'), snapshot.overall.participants.toLocaleString(), '#2554a6'],
    [localizeText('记录'), snapshot.overall.runs.toLocaleString(), '#1d8fa3'],
    [localizeText('有效率'), formatPercent(snapshot.overall.validRate), '#1f7a5c'],
    [localizeText('平均 FPS'), `${formatMetric(snapshot.overall.fpsAvg, 1)} Hz`, '#d97a2b'],
    [localizeText('质控标记数'), snapshot.overall.anomalyRuns.toLocaleString(), snapshot.overall.anomalyRuns ? '#c8423f' : '#1f7a5c'],
  ];
  const cardGap = 22;
  const cardW = (canvas.width - margin * 2 - cardGap * (cards.length - 1)) / cards.length;
  cards.forEach(([label, value, color], index) => {
    drawFigureMetric(ctx, label, value, margin + index * (cardW + cardGap), 250, cardW, 122, color);
  });

  const chartX = margin;
  const chartY = 460;
  const chartW = 900;
  const chartH = 380;
  ctx.fillStyle = '#17202f';
  ctx.font = '700 34px Inter, Arial, sans-serif';
  ctx.fillText(localizeText('条件对比'), chartX, chartY - 54);
  const maxRuns = Math.max(1, ...snapshot.conditions.map(group => group.summary.runs));
  snapshot.conditions.slice(0, 6).forEach((group, index) => {
    const y = chartY + index * 58;
    const barW = (group.summary.runs / maxRuns) * chartW;
    ctx.fillStyle = '#eef2f6';
    ctx.fillRect(chartX, y, chartW, 34);
    ctx.fillStyle = group.key === '实验组' ? '#c8423f' : '#2554a6';
    ctx.fillRect(chartX, y, barW, 34);
    ctx.fillStyle = '#17202f';
    ctx.font = '24px Inter, Arial, sans-serif';
    ctx.fillText(`${localizeText(group.label)} · ${group.summary.runs} ${localizeText('记录')} · ${localizeText('有效率')} ${formatPercent(group.summary.validRate)}`, chartX + 14, y + 5);
  });

  const zoneX = 1150;
  const zoneY = 460;
  const cell = 180;
  const maxZone = Math.max(1, ...snapshot.overall.zoneCounts);
  ctx.fillStyle = '#17202f';
  ctx.font = '700 34px Inter, Arial, sans-serif';
  ctx.fillText(localizeText('打印区域分布'), zoneX, zoneY - 54);
  snapshot.overall.zoneCounts.forEach((count, index) => {
    const col = index % 3;
    const row = Math.floor(index / 3);
    const x = zoneX + col * (cell + 16);
    const y = zoneY + row * (cell + 16);
    const ratio = snapshot.overall.validPoints ? count / snapshot.overall.validPoints : 0;
    const alpha = 0.08 + (count / maxZone) * 0.46;
    ctx.fillStyle = `rgba(37,84,166,${alpha})`;
    ctx.strokeStyle = '#d9e0ea';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(x, y, cell, cell, 12);
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = '#17202f';
    ctx.font = '700 30px Inter, Arial, sans-serif';
    ctx.fillText(formatPercent(ratio, 1), x + 20, y + 52);
    ctx.fillStyle = '#596579';
    ctx.font = '22px Inter, Arial, sans-serif';
    ctx.fillText(getAnalysisZoneLabel(index), x + 20, y + 22);
    ctx.fillText(`${count.toLocaleString()} ${localizeText('点数')}`, x + 20, y + 96);
  });

  ctx.fillStyle = '#17202f';
  ctx.font = '700 34px Inter, Arial, sans-serif';
  ctx.fillText(localizeText('自动解释摘要'), margin, 1050);
  ctx.fillStyle = '#596579';
  ctx.font = '28px Inter, Arial, sans-serif';
  let noteY = 1110;
  snapshot.insights.slice(0, 6).forEach((insight, index) => {
    ctx.fillStyle = index === 0 ? '#2554a6' : '#596579';
    noteY += drawFigureText(ctx, `${index + 1}. ${localizeText(insight)}`, margin, noteY, 1900, 40, { maxLines: 2 }) + 12;
  });
  ctx.fillStyle = '#8792a3';
  ctx.font = '22px Inter, Arial, sans-serif';
  ctx.fillText(localizeText('技术异常筛查不会将局部注意力本身视为无效。'), margin, canvas.height - 80);

  downloadCanvasPng(
    `academic_overall_analysis_${new Date().toISOString().replace(/[:.]/g, '-')}.png`,
    canvas
  );
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
        getImageConditionMeta(run.image).condition,
        getImageConditionMeta(run.image).label,
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
  return `${safeFileName(participantName)}-${hours}.${minutes}-sign visual attention.json`;
}

function getArchiveParticipantName() {
  const currentRecord = findRunRecord(State.currentReportRun);
  return currentRecord?.session?.label
    || getCurrentHomeSession()?.label
    || State.calibrationSessions[State.calibrationSessions.length - 1]?.label
    || '未命名参与者';
}

function readArchiveFile(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = event => {
      try {
        resolve({
          fileName: file.name,
          archive: JSON.parse(event.target.result),
        });
      } catch (err) {
        reject(new Error(`${file.name}: ${err.message}`));
      }
    };
    reader.onerror = () => reject(new Error(`${file.name}: 文件读取失败`));
    reader.readAsText(file);
  });
}

async function importArchiveFiles(fileList, sourceInput = EL.importArchiveInput) {
  const files = Array.from(fileList || []).filter(file => /\.json$/i.test(file.name));
  if (!files.length) return;

  try {
    const loaded = await Promise.all(files.map(readArchiveFile));
    const sessions = loaded.flatMap(({ archive, fileName }) => {
      const normalized = normalizeImportedSessions(archive);
      if (!normalized.length) throw new Error(`${fileName}: 存档中没有可用的参与者数据`);
      return normalized;
    });

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
    if (sourceInput) sourceInput.value = '';
  }
}

function importArchiveFile(file) {
  if (!file) return;
  importArchiveFiles([file]);
}

function importArchiveFolder(fileList) {
  importArchiveFiles(fileList, EL.importArchiveFolderInput);
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
      runs: uniquifySessionRunIds((Array.isArray(session.runs) ? session.runs : []).map((run, runIndex) => {
        const rawImage = {
          id: String(run.image?.id || `image-${runIndex + 1}`),
          name: String(run.image?.name || `image-${runIndex + 1}`),
          size: Number(run.image?.size) || 0,
          group: run.image?.group ? String(run.image.group) : '',
          condition: run.image?.condition ? String(run.image.condition) : '',
          conditionLabel: run.image?.conditionLabel ? String(run.image.conditionLabel) : '',
        };
        const conditionMeta = getImageConditionMeta(rawImage);
        return {
          id: String(run.id || `trial-${runIndex + 1}`),
          startedAt: run.startedAt || '',
          endedAt: run.endedAt || '',
          duration: Number(run.duration) || 0,
          image: {
            ...rawImage,
            condition: conditionMeta.condition,
            conditionLabel: conditionMeta.label,
          },
          imageSrc: run.imageSrc || '',
          coordinateSystem: run.coordinateSystem || session.coordinateSystem || 'screen',
          a4Plane: normalizeA4Plane(run.a4Plane || session.a4Plane),
          paperSizeMm: normalizePaperSize(run.paperSizeMm || session.paperSizeMm),
          sourceRunId: run.sourceRunId ? String(run.sourceRunId) : undefined,
          versionLabel: run.versionLabel ? String(run.versionLabel) : undefined,
          manualCorrection: run.manualCorrection && typeof run.manualCorrection === 'object'
            ? { ...run.manualCorrection }
            : undefined,
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
        };
      })),
    };
  });
}

function uniquifySessionRunIds(runs) {
  const used = new Set();
  return runs.map((run, index) => {
    const base = run.id || `trial-${index + 1}`;
    let id = base;
    let suffix = 2;
    while (used.has(id)) {
      id = `${base}-${suffix}`;
      suffix += 1;
    }
    used.add(id);
    return id === run.id ? run : { ...run, id };
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
  EL.languageSelect?.addEventListener('change', () => {
    applyLanguage(EL.languageSelect.value);
    updateHomeDataSummary();
    updateManualCorrectionPanel();
    updateAnalysisDashboard();
    updateGazePlaybackControls();
  });

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
  EL.externalImageBtn?.addEventListener('click', () => EL.externalImageInput?.click());
  EL.externalImageInput?.addEventListener('change', event => loadExternalImage(event.target.files?.[0]));

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
  EL.vizCorrectionMode.addEventListener('change', () => {
    State.reportCorrectionMode = EL.vizCorrectionMode.value;
    if (State.reportCorrectionMode === 'manual') ensureManualCorrectionState(State.currentReportRun);
    stopGazePlayback(false);
    updateManualCorrectionPanel();
    redrawCurrentVisualization();
  });
  EL.manualCorrectionTool.addEventListener('change', () => {
    updateManualCursor();
    updateManualCorrectionPanel();
  });
  EL.manualBrushRadius.addEventListener('input', () => {
    const state = ensureManualCorrectionState(State.currentReportRun);
    state.brushRadius = Math.max(0.01, Math.min(0.12, Number(EL.manualBrushRadius.value) / 100));
    updateManualCorrectionPanel();
  });
  EL.manualResetBtn.addEventListener('click', resetManualCorrection);
  EL.saveCorrectedVersionBtn.addEventListener('click', saveCorrectedVersion);
  EL.manualCorrectionCanvas.addEventListener('pointerdown', handleManualPointerDown);
  EL.manualCorrectionCanvas.addEventListener('pointermove', handleManualPointerMove);
  EL.manualCorrectionCanvas.addEventListener('pointerup', handleManualPointerUp);
  EL.manualCorrectionCanvas.addEventListener('pointercancel', handleManualPointerUp);
  EL.manualCorrectionCanvas.addEventListener('pointerleave', () => {
    if (State.manualCorrection?.pointer && !State.manualCorrection.pointer.start) {
      State.manualCorrection.pointer = null;
      drawManualOverlay();
    }
  });
  [EL.vizTimeStart, EL.vizTimeEnd].forEach(input => {
    input.addEventListener('input', () => {
      stopGazePlayback(false);
      updateReportStats(State.currentReportRun);
      updateManualCorrectionPanel();
      redrawCurrentVisualization();
    });
  });
  EL.vizTimeResetBtn.addEventListener('click', () => {
    stopGazePlayback(false);
    resetReportTimeRange(State.currentReportRun);
    updateReportStats(State.currentReportRun);
    updateManualCorrectionPanel();
    redrawCurrentVisualization();
  });
  EL.gazePlaybackBtn.addEventListener('click', toggleGazePlayback);
  EL.exportVizLayerBtn.addEventListener('click', exportTransparentVizLayer);
  EL.exportAcademicFigureBtn.addEventListener('click', exportAcademicFigure);
  EL.exportAcademicBatchBtn.addEventListener('click', openAcademicBatchExportMenu);
  EL.academicBatchSelectAllBtn?.addEventListener('click', () => setAcademicBatchSelection(true));
  EL.academicBatchClearBtn?.addEventListener('click', () => setAcademicBatchSelection(false));
  EL.academicBatchCancelBtn?.addEventListener('click', () => hideModal(EL.academicBatchModal));
  EL.academicBatchCancelSecondaryBtn?.addEventListener('click', () => hideModal(EL.academicBatchModal));
  EL.academicBatchStartBtn?.addEventListener('click', startSelectedAcademicBatchExport);
  EL.singleAnalysisTab.addEventListener('click', () => setReportMode('single'));
  EL.overallAnalysisTab.addEventListener('click', () => setReportMode('overall'));
  EL.analysisScopeSelect.addEventListener('change', updateAnalysisDashboard);
  EL.analysisImageSelect.addEventListener('change', updateAnalysisDashboard);
  EL.exportAnalysisCsvBtn.addEventListener('click', exportAnalysisCSV);
  EL.exportAnalysisJsonBtn.addEventListener('click', exportAnalysisJSON);
  EL.exportAnalysisFigureBtn.addEventListener('click', exportAnalysisFigure);

  // 返回首页
  EL.backHomeBtn.addEventListener('click', () => {
    stopGazePlayback(false);
    updateHomeDataSummary();
    showScreen(EL.homeScreen);
  });

  // 导出
  EL.importArchiveBtn.addEventListener('click', () => EL.importArchiveInput.click());
  EL.importArchiveFolderBtn.addEventListener('click', () => EL.importArchiveFolderInput.click());
  EL.importArchiveInput.addEventListener('change', e => importArchiveFiles(e.target.files, e.target));
  EL.importArchiveFolderInput.addEventListener('change', e => importArchiveFolder(e.target.files));
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
    drawManualOverlay();
  });
  window.addEventListener('beforeunload', handleBeforeUnload);
}

// ─── 入口 ─────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  // 默认直接进入主界面；只有开始校准时才请求摄像头权限。
  startLanguageObserver();
  hideModal(EL.loadingOverlay);
  hideModal(EL.errorModal);
  showScreen(EL.homeScreen);
  initializeBuiltinImages();
  updateHomeDataSummary();
  updateAnalysisDashboard();

  bindEvents();
  applyLanguage(State.language);
});
