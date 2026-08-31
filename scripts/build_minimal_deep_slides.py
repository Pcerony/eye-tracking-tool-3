# -*- coding: utf-8 -*-
import json
import os

slides_data = {}

# ------------------------------------------------------------------------------
# Slide 20: s18a-entropy-intro (Short, Clean Text Comparison with Huge Bits Numbers)
# ------------------------------------------------------------------------------
slides_data["s18a-entropy-intro"] = {
    "id": "s18a-entropy-intro",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：文本信息量对比",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": [],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS</div><div class="r">20 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18a.title">文本信息量对比</h2><div class="analysis-kicker-desc" data-i18n="slides.s18a.guide">控制事实总量一致的前提下，常规表述与反常识表述的信息量差异</div></div><div class="analysis-anim-badge" aria-label="Text Animation"><span class="analysis-anim-label">INFORMATION</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="8" width="40" height="14" rx="2" fill="#eff6ff" stroke="#93c5fd" /><rect x="66" y="8" width="40" height="14" rx="2" fill="#fef2f2" stroke="#ef4444" /></svg></div></div><div class="analysis-body-group"><div class="clean-compare-grid"><div class="clean-compare-col"><span class="clean-compare-tag" style="color:var(--text-secondary)" data-i18n="slides.s18a.c1.tag">对照组 · 常规表述</span><p class="clean-text-quote"><span data-i18n="slides.s18a.c1.p1">九重葛为</span><span class="heat-blue" data-i18n="slides.s18a.c1.h1">紫茉莉科木质藤本</span><span data-i18n="slides.s18a.c1.p2">，原产于南美洲，夏季开花。</span></p><div class="clean-stat-row"><span class="clean-stat-num" style="color:#1e40af">0.42<small style="font-size:22px;margin-left:4px">bits</small></span><span class="clean-stat-desc" data-i18n="slides.s18a.c1.desc">先验概率高 P=0.75<br>司空见惯事实 · 知识增量极低</span></div></div><div class="clean-compare-col"><span class="clean-compare-tag" style="color:var(--accent)" data-i18n="slides.s18a.c2.tag">改良组 · 感官表述</span><p class="clean-text-quote"><span data-i18n="slides.s18a.c2.p1">红色的</span><span class="heat-red" data-i18n="slides.s18a.c2.h1">不是花瓣是苞片！</span><span data-i18n="slides.s18a.c2.p2">请用手触摸</span><span class="heat-red" data-i18n="slides.s18a.c2.h2">干爽纸质触感</span>。</p><div class="clean-stat-row"><span class="clean-stat-num" style="color:var(--accent)">3.06<small style="font-size:22px;margin-left:4px">bits</small></span><span class="clean-stat-desc" data-i18n="slides.s18a.c2.desc">先验概率低 P=0.12<br>颠覆预期反常识 · 知识增量 7.37 倍</span></div></div></div><div style="padding-top:16px;border-top:1px solid var(--border-subtle);display:flex;justify-content:space-between;align-items:center"><div style="font-size:16px;color:var(--ink);font-weight:500" data-i18n="slides.s18a.summary">字数相当、事实受控的前提下，反常识表述所释放的有效信息量激增 7.37 倍。</div><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">7.37x SURPRISAL</span></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 21: s18b-conventional-metrics (Huge Formula, 4-Column Variable Mapping, Metric Flaws)
# ------------------------------------------------------------------------------
slides_data["s18b-conventional-metrics"] = {
    "id": "s18b-conventional-metrics",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：香农惊讶度模型",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": [],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS</div><div class="r">21 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18b.title">香农惊讶度数学模型</h2><div class="analysis-kicker-desc" data-i18n="slides.s18b.guide">衡量信息打破读者先验预期的程度，以及传统眼动指标的均质化缺陷</div></div><div class="analysis-anim-badge" aria-label="Mapping Animation"><span class="analysis-anim-label">SURPRISAL</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 24 L 38 18 L 68 12 L 106 6" stroke="var(--accent)" stroke-width="2" fill="none" /><circle cx="106" cy="6" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div class="hero-formula-wrap"><div class="hero-formula">I(x) = - log₂( P(x) )</div></div><div class="clean-map-grid"><div class="clean-map-col"><span class="clean-map-symbol">x</span><span class="clean-map-name" data-i18n="slides.s18b.v1.name">信息单元</span><p class="clean-map-desc" data-i18n="slides.s18b.v1.desc">文本具体词句（如“紫茉莉科” vs “其实是苞片”）。</p></div><div class="clean-map-col"><span class="clean-map-symbol">P(x)</span><span class="clean-map-name" data-i18n="slides.s18b.v2.name">先验预期概率</span><p class="clean-map-desc" data-i18n="slides.s18b.v2.desc">读者读到该词前的心理预期（常识 0.75 vs 意外 0.12）。</p></div><div class="clean-map-col"><span class="clean-map-symbol">-log₂</span><span class="clean-map-name" data-i18n="slides.s18b.v3.name">逆对数尺度</span><p class="clean-map-desc" data-i18n="slides.s18b.v3.desc">打破预期的冲击程度呈对数倍增。</p></div><div class="clean-map-col"><span class="clean-map-symbol">I(x)</span><span class="clean-map-name" data-i18n="slides.s18b.v4.name">自信息量 (bits)</span><p class="clean-map-desc" data-i18n="slides.s18b.v4.desc">读者实际获得的新知量（0.42 b [低] vs 3.06 b [高]）。</p></div></div><div style="padding-top:16px;border-top:1px solid var(--border-subtle)"><p style="font-size:15px;color:var(--ink);line-height:1.45;margin:0" data-i18n="slides.s18b.criticalFlaw"><strong>传统指标盲区：</strong>注视时长与热力图默认“每秒注视等价”，无法辨识游客在文本 A 停留 10 秒（因枯燥卡顿）与在文本 B 停留 10 秒（吸收高价值新知）的本质区别。</p></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 22: s18c-cognitive-friction (Huge Formula & Huge Contrast Numbers)
# ------------------------------------------------------------------------------
slides_data["s18c-cognitive-friction"] = {
    "id": "s18c-cognitive-friction",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：认知摩擦与状态熵",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": [],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS</div><div class="r">22 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18c.title">视线状态信息熵与认知摩擦</h2><div class="analysis-kicker-desc" data-i18n="slides.s18c.guide">衡量注视点在区域间分布的混乱度与停滞阻力</div></div><div class="analysis-anim-badge" aria-label="Friction Animation"><span class="analysis-anim-label">FRICTION</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><line x1="10" y1="15" x2="106" y2="15" stroke="rgba(220,38,38,0.8)" stroke-width="2" stroke-dasharray="4 2" /><circle cx="58" cy="15" r="5" fill="rgba(220,38,38,0.9)" /></svg></div></div><div class="analysis-body-group"><div class="hero-formula-wrap"><div class="hero-formula">H(X) = - ∑ P(xᵢ) log₂ P(xᵢ)</div></div><div class="clean-compare-grid"><div class="clean-compare-col"><span class="clean-compare-tag" style="color:rgba(220,38,38,0.9)" data-i18n="slides.s18c.c1.tag">对照组 · 高认知摩擦</span><div class="clean-stat-num" style="color:rgba(220,38,38,0.9)">2.14<small style="font-size:22px;margin-left:4px">bits</small></div><p style="font-size:15px;color:var(--text-primary);line-height:1.5;margin:0" data-i18n="slides.s18c.c1.body">长文本缺乏意外度与结构引导，视线反复自旋（自循环率 93%），80% 读者半途中断放弃。</p></div><div class="clean-compare-col"><span class="clean-compare-tag" style="color:var(--accent)" data-i18n="slides.s18c.c2.tag">改良组 · 低认知摩擦</span><div class="clean-stat-num" style="color:var(--accent)">1.48<small style="font-size:22px;margin-left:4px">bits</small></div><p style="font-size:15px;color:var(--text-primary);line-height:1.5;margin:0" data-i18n="slides.s18c.c2.body">高惊讶度气泡提供清晰着陆点，视线顺畅流转至多模态区域，加工顺畅度提升 +63.5%。</p></div></div><div style="padding-top:16px;border-top:1px solid var(--border-subtle)"><p style="font-size:15px;color:var(--ink);line-height:1.45;margin:0" data-i18n="slides.s18c.rethink">长文本高停留往往是认知摩擦（Cognitive Friction）与解码受阻的假象，需信息论加权还原真实吸收。</p></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 23: s18d-surprisal-theory (4-Step Logic Clean Flow)
# ------------------------------------------------------------------------------
slides_data["s18d-surprisal-theory"] = {
    "id": "s18d-surprisal-theory",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：实验控制与加权框架",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": [],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS</div><div class="r">23 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18d.title">实验控制与信息加权框架</h2><div class="analysis-kicker-desc" data-i18n="slides.s18d.guide">文本事实总量受控，信息熵作为客观权重矩阵，AOI 视线数据为真实自变量</div></div><div class="analysis-anim-badge" aria-label="Framework Animation"><span class="analysis-anim-label">FRAMEWORK</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 15 Q 35 5 60 15 T 110 15" stroke="var(--accent)" stroke-width="1.8" fill="none" /><circle cx="60" cy="15" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div class="clean-map-grid"><div class="clean-map-col"><span class="clean-compare-tag" style="color:var(--text-secondary)">01 · BASELINE</span><span class="clean-map-name" data-i18n="slides.s18d.s1.title">事实基线控制</span><p class="clean-map-desc" data-i18n="slides.s18d.s1.desc">两组标牌传达的核心植物学事实总量大体相等，控制文本事实为恒定实验基准。</p></div><div class="clean-map-col"><span class="clean-compare-tag" style="color:var(--accent)">02 · WEIGHTS</span><span class="clean-map-name" data-i18n="slides.s18d.s2.title">客观信息熵矩阵</span><p class="clean-map-desc" data-i18n="slides.s18d.s2.desc">基于先验概率建立各区域客观信息权重 I(AOI)，形成衡量新知密度的价值标尺。</p></div><div class="clean-map-col"><span class="clean-compare-tag" style="color:var(--accent)">03 · GAZE</span><span class="clean-map-name" data-i18n="slides.s18d.s3.title">动态视线分配 (pᵢ)</span><p class="clean-map-desc" data-i18n="slides.s18d.s3.desc">版面与叙事改变后，受众在各区域的注视时间占比 p_i 发生实质性重组。</p></div><div class="clean-map-col"><span class="clean-compare-tag" style="color:#16a34a">04 · GAIN</span><span class="clean-map-name" data-i18n="slides.s18d.s4.title">净认知产出 E_gain</span><p class="clean-map-desc" data-i18n="slides.s18d.s4.desc">视线分配自变量作用于客观信息矩阵（E_gain = ∑ p_i I_i），量化真实学习增量。</p></div></div><div style="padding-top:16px;border-top:1px solid var(--border-subtle);display:flex;justify-content:space-between;align-items:center"><div style="font-size:15px;color:var(--ink);font-weight:500" data-i18n="slides.s18d.frameworkSummary">信息熵提供客观“知识价值标尺”，眼动数据记录“注意力分配”，二者结合揭开认知黑盒。</div><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">INTEGRATED MODEL</span></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 24: s18e-case-information-weight (4 Functional Zones Huge Bits Values)
# ------------------------------------------------------------------------------
slides_data["s18e-case-information-weight"] = {
    "id": "s18e-case-information-weight",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：四大功能区权重",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": [],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS</div><div class="r">24 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18e.title">四大功能区信息量客观权重</h2><div class="analysis-kicker-desc" data-i18n="slides.s18e.guide">标定各语义区域的自信息量客观数值，建立加权基准</div></div><div class="analysis-anim-badge" aria-label="Calculation Animation"><span class="analysis-anim-label">WEIGHTS</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="8" stroke="var(--border-subtle)" stroke-width="1.5" /><circle cx="96" cy="15" r="8" stroke="var(--accent)" stroke-width="1.5" /><line x1="28" y1="15" x2="88" y2="15" stroke="var(--accent)" stroke-width="2" /></svg></div></div><div class="analysis-body-group"><div class="clean-map-grid"><div class="clean-map-col"><span class="clean-stat-num" style="color:var(--text-secondary)">0.42<small style="font-size:18px;margin-left:2px">bits</small></span><span class="clean-map-name" data-i18n="slides.s18e.w1.title">传统科属长文</span><p class="clean-map-desc" data-i18n="slides.s18e.w1.desc">“紫茉莉科木质藤本”<br>先验概率 P=0.75 · 基础常识</p></div><div class="clean-map-col"><span class="clean-stat-num" style="color:var(--ink)">2.00<small style="font-size:18px;margin-left:2px">bits</small></span><span class="clean-map-name" data-i18n="slides.s18e.w4.title">花语文化提示</span><p class="clean-map-desc" data-i18n="slides.s18e.w4.desc">“热情、坚韧与魅力”<br>先验概率 P=0.25 · 趣味延展</p></div><div class="clean-map-col"><span class="clean-stat-num" style="color:var(--ink)">2.74<small style="font-size:18px;margin-left:2px">bits</small></span><span class="clean-map-name" data-i18n="slides.s18e.w3.title">拟人对话引导</span><p class="clean-map-desc" data-i18n="slides.s18e.w3.desc">“猜猜我的艳丽秘密？”<br>先验概率 P=0.15 · 情境代入</p></div><div class="clean-map-col"><span class="clean-stat-num" style="color:var(--accent)">3.06<small style="font-size:18px;margin-left:2px">bits</small></span><span class="clean-map-name" style="color:var(--accent)" data-i18n="slides.s18e.w2.title">触觉互动气泡 (R)</span><p class="clean-map-desc" data-i18n="slides.s18e.w2.desc">“红色的不是花是苞片！”<br>先验概率 P=0.12 · 7.37x 驱动</p></div></div><div style="padding-top:16px;border-top:1px solid var(--border-subtle)"><p style="font-size:15px;color:var(--ink);line-height:1.45;margin:0" data-i18n="slides.s18e.summary">身体触觉互动区（3.06 bits）成为全标牌信息密度最高的核心知识锚点。</p></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 25: s18f-cognitive-gain-formula (Huge Formula, Huge +127.7% KPI)
# ------------------------------------------------------------------------------
slides_data["s18f-cognitive-gain-formula"] = {
    "id": "s18f-cognitive-gain-formula",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：E_gain模型",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": [],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS</div><div class="r">25 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18f.title">认知吸收总量模型 E_gain</h2><div class="analysis-kicker-desc" data-i18n="slides.s18f.guide">动态视线时间权重乘以静态区域信息量</div></div><div class="analysis-anim-badge" aria-label="Gain Animation"><span class="analysis-anim-label">E_GAIN</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 24 L 38 18 L 68 12 L 106 6" stroke="var(--accent)" stroke-width="2" fill="none" /><circle cx="106" cy="6" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div class="hero-formula-wrap"><div class="hero-formula">E_gain = ∑ [ pᵢ × I(AOIᵢ) ]</div></div><div class="clean-compare-grid"><div class="clean-compare-col"><span class="clean-compare-tag" style="color:var(--text-secondary)">VARIABLES</span><div style="font-size:15px;color:var(--text-primary);line-height:1.65"><div data-i18n="slides.s18f.v1">• E_gain (bits)：整张标牌吸收的信息总量</div><div data-i18n="slides.s18f.v2">• p_i = T_i / ∑T_j：区域注视时间权重 (自变量)</div><div data-i18n="slides.s18f.v3">• I(AOI_i)：区域客观自信息量 (静态权重)</div></div></div><div class="clean-compare-col"><span class="clean-compare-tag" style="color:var(--accent)">EMPIRICAL RESULT</span><div class="clean-stat-row" style="padding-top:0"><span class="clean-stat-num" style="color:var(--accent);font-size:62px">+127.7%</span><span class="clean-stat-desc" style="font-size:16px"><strong style="color:var(--ink)">0.585 b → 1.332 b</strong><br>t(12) = 11.23, p &lt; 0.001</span></div></div></div><div style="padding-top:16px;border-top:1px solid var(--border-subtle)"><p style="font-size:15px;color:var(--ink);line-height:1.45;margin:0" data-i18n="slides.s18f.modelSummary">成功将“看哪里的时间 (p_i)”与“该处的新知价值 (I_i)”结合，解决停留时长与认知质量脱节难题。</p></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 26: s18g-markov-stagnation (Huge 93% -> 56% Drop Number)
# ------------------------------------------------------------------------------
slides_data["s18g-markov-stagnation"] = {
    "id": "s18g-markov-stagnation",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：马尔可夫转移矩阵",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": [],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS</div><div class="r">26 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18g.title">马尔可夫转移矩阵</h2><div class="analysis-kicker-desc" data-i18n="slides.s18g.guide">基于一阶马尔可夫链量化视线在各功能区之间的流转秩序</div></div><div class="analysis-anim-badge" aria-label="Markov Animation"><span class="analysis-anim-label">MARKOV</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="7" stroke="var(--ink)" stroke-width="1.5" fill="none" /><circle cx="96" cy="15" r="7" stroke="var(--accent)" stroke-width="1.5" fill="none" /><path d="M 27 15 Q 58 5 89 15" stroke="var(--accent)" stroke-width="1.8" fill="none" /></svg></div></div><div class="analysis-body-group"><div style="display:flex;align-items:baseline;justify-content:space-between;padding:12px 0"><div style="font-size:18px;font-weight:600;color:var(--ink)" data-i18n="slides.s18g.kpiTitle">长文本自循环停滞率</div><div class="clean-stat-num" style="color:var(--accent);font-size:62px">93% → 56%<small style="font-size:20px;color:var(--text-secondary);margin-left:10px">-39.8% (p &lt; 0.001)</small></div></div><div class="clean-compare-grid"><div class="clean-compare-col"><span class="clean-compare-tag" style="color:rgba(220,38,38,0.9)" data-i18n="slides.s18g.box1.title">对照组：封闭文本阅读陷阱 (0.93)</span><p style="font-size:15px;color:var(--text-primary);line-height:1.5;margin:0" data-i18n="slides.s18g.box1.body">视线在正文内反复自旋，转移至图片的概率仅 4%，无法形成图文互证。</p></div><div class="clean-compare-col"><span class="clean-compare-tag" style="color:var(--accent)" data-i18n="slides.s18g.box2.title">改良组：多模态导流网络 (0.56)</span><p style="font-size:15px;color:var(--text-primary);line-height:1.5;margin:0" data-i18n="slides.s18g.box2.body">视线平稳分流至触觉气泡 (0.19)、图标 (0.13) 与花语 (0.38)，构建顺畅探索动线。</p></div></div><div style="padding-top:16px;border-top:1px solid var(--border-subtle)"><p style="font-size:15px;color:var(--ink);line-height:1.45;margin:0" data-i18n="slides.s18g.summary">彻底打破长文本自循环死锁，实现图文互证的高效认知流。</p></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 27: s18h-efficiency-ratio (Huge Formula, Huge +29.9% Number)
# ------------------------------------------------------------------------------
slides_data["s18h-efficiency-ratio"] = {
    "id": "s18h-efficiency-ratio",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：认知传递能效比",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": [],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS</div><div class="r">27 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18h.title">认知传递能效比</h2><div class="analysis-kicker-desc" data-i18n="slides.s18h.guide">量化单位视觉搜索努力换取的信息增益</div></div><div class="analysis-anim-badge" aria-label="Efficiency Animation"><span class="analysis-anim-label">EFFICIENCY</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="96" height="12" rx="6" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="12" y="12" width="70" height="8" rx="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div class="hero-formula-wrap"><div class="hero-formula">η = E_gain / ( H_GTE + ε )</div></div><div class="clean-compare-grid"><div class="clean-compare-col"><span class="clean-compare-tag" style="color:var(--accent)">EMPIRICAL BOOST</span><div class="clean-stat-row" style="padding-top:0"><span class="clean-stat-num" style="color:var(--accent);font-size:62px">+29.9%</span><span class="clean-stat-desc" style="font-size:16px"><strong style="color:var(--ink)">1.083 → 1.407</strong><br>t(12) = 3.540, p = 0.004</span></div></div><div class="clean-compare-col"><span class="clean-compare-tag" style="color:var(--text-secondary)">IMPLICATIONS</span><div style="font-size:15px;color:var(--text-primary);line-height:1.65"><div data-i18n="slides.s18h.i1">• 优化信息结构，降低无序搜索负荷</div><div data-i18n="slides.s18h.i2">• 每一次注视均产生实质新知增益</div><div data-i18n="slides.s18h.i3">• 真正实现“视觉减负”与“认知增效”</div></div></div></div><div style="padding-top:16px;border-top:1px solid var(--border-subtle)"><p style="font-size:15px;color:var(--ink);line-height:1.45;margin:0" data-i18n="slides.s18h.summary">将眼动研究从物理行为统计提升至认知传递能效定量评价。</p></div></div></div>"""
}

# Write slide JSON files
for sid, data in slides_data.items():
    file_path = f"src/content/slides/{sid}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Written: {file_path}")

print("All slide JSON files generated successfully!")
