# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLIDES_DIR = os.path.join(BASE_DIR, 'src', 'content', 'slides')
I18N_DIR = os.path.join(BASE_DIR, 'src', 'i18n')
MANIFEST_FILE = os.path.join(BASE_DIR, 'deck-manifest.json')

# 1. Fully i18n-bound slide definitions
slides_data = [
    # Full Screen Stage Cover (matching s01 full-bleed style)
    {
        "id": "s18-deep-analysis-cover",
        "chapterId": "deep-analysis",
        "layout": "cover",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "深度分析",
        "animation": "hero",
        "legacyLayout": "SWISS-COVER-ASCII",
        "legacyClass": "slide accent",
        "assets": [],
        "claims": [],
        "markup": """<div class="canvas-card" style="position:relative;">
    <canvas class="ascii-bg" aria-hidden="true"></canvas>
    <div class="cover-layout">
      <div data-anim="kicker" class="cover-author">
        <div>PHASE 05 · DEEP COGNITIVE ANALYSIS</div>
        <div>SHANNON INFORMATION THEORY &amp; SURPRISAL MODEL</div>
        <div>N = 13 PARTICIPANTS · 27 TRIALS · PAIRED EMPIRICAL VALIDATION</div>
        <div>KYUSHU UNIVERSITY</div>
      </div>
      <h1 data-anim="title" style="align-self:center;font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:52px;line-height:1.08;letter-spacing:0;color:#fff;max-width:20ch;text-align:center;hyphens:none" data-i18n="slides.s18cover.title">基于信息熵与惊讶度的深度认知分析<br/><span style="display:block;margin-top:1.8vh;font-size:24px;line-height:1.2;letter-spacing:0;font-weight:300;opacity:0.9" data-i18n="slides.s18cover.desc">超越表面注视时长假象 · 计算认知科学量化模型与全量实证</span></h1>
      <div data-anim="bottom" class="cover-bottom">
        <div class="cover-tags">
          <span class="cover-tag"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"></rect><path d="M3 9h18M9 21V9"></path></svg>SHANNON SURPRISAL</span>
          <span class="cover-tag"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z"></path><circle cx="12" cy="12" r="3"></circle></svg>MARKOV FLOW</span>
          <span class="cover-tag"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v18M5 6h11l3 3-3 3H5z"></path></svg>E_GAIN (+127.7%)</span>
        </div>
        <div class="t-meta" style="color:rgba(255,255,255,0.7);font-family:var(--mono);font-size:13px;letter-spacing:0.08em;font-weight:600">
          PHASE 05 / 06
        </div>
      </div>
    </div>
  </div>"""
    },
    # s18a: Entropy Intro
    {
        "id": "s18a-entropy-intro",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：信息熵理论引入",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": [],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · SECTION INTRO</div><div class="r">20 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18a.title">基于信息熵与惊讶度理论的深度分析</h2><div class="analysis-kicker-desc" data-i18n="slides.s18a.guide">【理论引入】超越“注视时长”表面假象，量化真实知识吸收与阅读认知流</div></div><div class="analysis-anim-badge" aria-label="Entropy Wave Animation"><span class="analysis-anim-label">THEORY</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 6 15 Q 32 4 58 15 T 110 15" stroke="var(--border-subtle)" stroke-width="1.5" fill="none" /><path d="M 6 15 Q 32 26 58 15 T 110 15" stroke="var(--accent)" stroke-width="2" fill="none" /><circle cx="58" cy="15" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:28px"><div style="background:#fff;border:1px solid var(--border-subtle);border-top:4px solid #94a3b8;padding:36px 36px;border-radius:4px;display:flex;flex-direction:column;justify-content:center;gap:16px"><span style="font-family:var(--mono);font-size:13px;color:var(--text-secondary);font-weight:700;letter-spacing:0.08em" data-i18n="slides.s18a.tag1">CONFOUNDING OF GAZE TIME</span><h3 style="font-size:28px;color:var(--ink);font-weight:600;line-height:1.3;margin:0" data-i18n="slides.s18a.q1.title">看得久就是好吗？</h3><p style="font-size:18px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18a.q1.body">传统眼动指标假定“注视越久 = 越感兴趣”。但在植物标牌中，生僻文字导致的卡顿与犹豫常被误判为深度沉浸。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-top:4px solid var(--accent);padding:36px 36px;border-radius:4px;display:flex;flex-direction:column;justify-content:center;gap:16px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700;letter-spacing:0.08em" data-i18n="slides.s18a.tag2">SHANNON SURPRISAL PARADIGM</span><h3 style="font-size:28px;color:var(--ink);font-weight:600;line-height:1.3;margin:0" data-i18n="slides.s18a.q2.title">信息论度量真实获得</h3><p style="font-size:18px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18a.q2.body">引入香农信息熵与惊讶度（Surprisal），结合“信息违背预期时信息量最大”的原理，精确量化观众吸收的有效知识增量。</p></div></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:20px 28px;border-radius:4px;display:flex;align-items:center;justify-content:space-between"><div style="font-size:16.5px;color:var(--ink);line-height:1.5" data-i18n="slides.s18a.summary"><strong>认知范式升级：</strong>从“表面物理注视时长”转向“单位视觉负荷下的有效信息吸收量与动线流转秩序”。</div><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">PARADIGM SHIFT</span></div></div></div>"""
    },
    # s18b: Conventional Metrics
    {
        "id": "s18b-conventional-metrics",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：常规指标局限",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": [],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · CONVENTIONAL METRICS</div><div class="r">21 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18b.title">传统眼动三大常规指标及其假设</h2><div class="analysis-kicker-desc" data-i18n="slides.s18b.guide">【基线梳理】归纳现有植物标牌研究普遍依赖的三大常规眼动度量体系</div></div><div class="analysis-anim-badge" aria-label="Baseline Animation"><span class="analysis-anim-label">BASELINE</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="8" width="24" height="14" rx="2" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="46" y="8" width="24" height="14" rx="2" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="82" y="8" width="24" height="14" rx="2" stroke="var(--border-subtle)" stroke-width="1.5" /></svg></div></div><div class="analysis-body-group"><div class="analysis-visual-row" style="grid-template-columns:repeat(3, 1fr);gap:24px"><div style="background:#fff;border:1px solid var(--border-subtle);border-top:3px solid var(--accent);padding:32px 26px;border-radius:4px;display:flex;flex-direction:column;gap:14px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700">METRIC 01</span><h4 style="font-size:24px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18b.m1.title">注视时长 (Dwell Time)</h4><p style="font-size:17.5px;color:var(--text-primary);line-height:1.6;margin:0" data-i18n="slides.s18b.m1.body">记录视线在某区域停留的总秒数或时间百分比，底层假设“停越久 = 越感兴趣”。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-top:3px solid var(--accent);padding:32px 26px;border-radius:4px;display:flex;flex-direction:column;gap:14px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700">METRIC 02</span><h4 style="font-size:24px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18b.m2.title">注视次数 (Fixation Count)</h4><p style="font-size:17.5px;color:var(--text-primary);line-height:1.6;margin:0" data-i18n="slides.s18b.m2.body">记录视线落入该区域的落点频次，底层假设“落点越多 = 越具视觉重要性”。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-top:3px solid var(--accent);padding:32px 26px;border-radius:4px;display:flex;flex-direction:column;gap:14px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700">METRIC 03</span><h4 style="font-size:24px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18b.m3.title">注视热力图 (Heatmap)</h4><p style="font-size:17.5px;color:var(--text-primary);line-height:1.6;margin:0" data-i18n="slides.s18b.m3.body">高斯核密度渲染的空间点云，底层假设“红色高亮区代表绝对吸引力焦点”。</p></div></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid rgba(220,38,38,0.85);padding:22px 28px;border-radius:4px"><div style="font-size:14px;font-family:var(--mono);font-weight:700;color:rgba(220,38,38,0.9);margin-bottom:6px" data-i18n="slides.s18b.flawTag">UNCHECKED ASSUMPTION: 均质化假定缺陷</div><p style="font-size:17px;color:var(--ink);line-height:1.55;margin:0" data-i18n="slides.s18b.criticalFlaw">三大指标默认“每秒注视具有均等的信息加工价值”，仅记录物理停留坐标，无法辨识注视背后的认知理解质量与晦涩文字带来的无序停滞。</p></div></div></div>"""
    },
    # s18c: Cognitive Friction
    {
        "id": "s18c-cognitive-friction",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：认知受阻误区",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": [],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · COGNITIVE FRICTION</div><div class="r">22 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18c.title">常规指标的致命误区：认知受阻而非深度阅读</h2><div class="analysis-kicker-desc" data-i18n="slides.s18c.guide">【误区揭示】剖析传统大段科普文字如何造成高注视时长的“虚假繁荣”</div></div><div class="analysis-anim-badge" aria-label="Friction Animation"><span class="analysis-anim-label">CONFOUNDING</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><line x1="10" y1="15" x2="106" y2="15" stroke="rgba(220,38,38,0.8)" stroke-width="2" stroke-dasharray="4 2" /><circle cx="58" cy="15" r="5" fill="rgba(220,38,38,0.9)" /></svg></div></div><div class="analysis-body-group"><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:28px"><div style="background:#fff;border:1px solid rgba(220,38,38,0.3);border-top:4px solid rgba(220,38,38,0.85);padding:36px 36px;border-radius:4px;display:flex;flex-direction:column;gap:16px"><span style="font-family:var(--mono);font-size:13px;color:rgba(220,38,38,0.9);font-weight:700" data-i18n="slides.s18c.tag1">SUPERFICIAL METRIC (MISJUDGED)</span><h4 style="font-size:26px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18c.c1.title">表面数据假象：长文本注视占比 44.3%</h4><p style="font-size:18px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18c.c1.body">在对照组中，说明文字区注视时长位居首位。传统眼动模型据此推论“观众对大段科普内容最感兴趣”。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-top:4px solid var(--accent);padding:36px 36px;border-radius:4px;display:flex;flex-direction:column;gap:16px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700" data-i18n="slides.s18c.tag2">COGNITIVE REALITY (FRICTION)</span><h4 style="font-size:26px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18c.c2.title">真实认知困境：认知摩擦与阅读停滞</h4><p style="font-size:18px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18c.c2.body">大段生僻拉丁学名与形态学术语导致“读不下去、找不到重点”，视线在文本内被动打转卡顿，实为负荷过载而非深度阅读。</p></div></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:20px 28px;border-radius:4px"><p style="font-size:17px;color:var(--ink);line-height:1.55;margin:0" data-i18n="slides.s18c.rethink">诊断结论：高停留时长反映的是信息解码受阻（Cognitive Friction）而非有效知识吸收，必须引入度量信息意外度与流转秩序的信息论工具。</p></div></div></div>"""
    },
    # s18d: Surprisal Theory
    {
        "id": "s18d-surprisal-theory",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：香农惊讶度建模",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": [],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · SURPRISAL THEORY</div><div class="r">23 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18d.title">香农信息论与惊讶度：违背预期的认知增益</h2><div class="analysis-kicker-desc" data-i18n="slides.s18d.guide">【数理建模】引入自信息量 I = -log2(P)，量化反常识感官互动的高知识价值</div></div><div class="analysis-anim-badge" aria-label="Surprisal Animation"><span class="analysis-anim-label">SURPRISAL</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 25 C 28 25, 42 6, 58 6 C 74 6, 88 25, 106 25" stroke="var(--ink)" stroke-width="1.5" fill="none" /><line x1="58" y1="6" x2="58" y2="25" stroke="var(--accent)" stroke-width="2" stroke-dasharray="2 2" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:28px 36px;border-radius:4px;display:flex;align-items:center;justify-content:space-between"><div style="font-family:var(--sans);font-size:48px;font-weight:200;color:var(--accent)">I(AOI) = - log₂( P<sub style="font-size:24px">prior</sub> )</div><div style="font-size:22px;font-weight:600;color:var(--ink)" data-i18n="slides.s18d.axiom">“信息在违背预期时，其承载的信息量最大”</div></div><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:28px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:30px 32px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><span style="font-family:var(--mono);font-size:13px;color:var(--text-secondary);font-weight:700" data-i18n="slides.s18d.tag1">PREDICTIVE CODING</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18d.box1.title">人脑预测编码机制</h4><p style="font-size:17.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18d.box1.body">日常司空见惯的常识（先验概率高）无法激活深层认知；打破预期的反常识线索（先验概率低）能显著触发海马体记忆编码。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:30px 32px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700" data-i18n="slides.s18d.tag2">SELF-INFORMATION (BITS)</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18d.box2.title">自信息量 (比特 bits)</h4><p style="font-size:17.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18d.box2.body">自信息量 I 以比特为量纲，精确度量了受众在消除不确定性时所获得的新知价值，为量化真实学习效果提供数学基石。</p></div></div></div></div>"""
    },
    # s18e: Case Calculation
    {
        "id": "s18e-case-information-weight",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：案例信息量量化",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": [],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · AOI INFORMATION WEIGHTS</div><div class="r">24 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18e.title">标牌各区域信息量权重与案例量化计算</h2><div class="analysis-kicker-desc" data-i18n="slides.s18e.guide">【数值演算】对比传统分类学常识与共创感官互动的自信息量数值差异</div></div><div class="analysis-anim-badge" aria-label="Calculation Animation"><span class="analysis-anim-label">CALCULATION</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="8" stroke="var(--border-subtle)" stroke-width="1.5" /><line x1="16" y1="15" x2="24" y2="15" stroke="var(--accent)" stroke-width="2" /><line x1="20" y1="11" x2="20" y2="19" stroke="var(--accent)" stroke-width="2" /><circle cx="96" cy="15" r="8" stroke="var(--accent)" stroke-width="1.5" /><line x1="92" y1="15" x2="100" y2="15" stroke="var(--accent)" stroke-width="2" /></svg></div></div><div class="analysis-body-group"><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:24px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:24px 26px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:var(--mono);font-size:12px;color:var(--text-secondary);font-weight:700">CONVENTIONAL TAXONOMY</span><span style="font-size:24px;font-weight:700;color:var(--text-secondary)">0.415 <small style="font-size:13px">bits</small></span></div><svg width="100%" height="80" viewBox="0 0 400 80" fill="none" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid var(--border-subtle);border-radius:4px"><rect x="15" y="15" width="100" height="50" rx="3" fill="#cbd5e1" /><rect x="130" y="15" width="250" height="50" rx="3" fill="#fecaca" stroke="#dc2626" stroke-width="1" stroke-dasharray="3 3"/><text x="255" y="44" font-size="12" fill="#dc2626" font-weight="bold" text-anchor="middle" data-i18n="slides.s18e.svgCtrl">大段科普长文本 (P=0.75, I=0.415 bits)</text></svg><h4 style="font-size:20px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18e.box1.title">传统科普长文本（高预期 · 低信息量）</h4><p style="font-size:16px;color:var(--text-primary);line-height:1.55;margin:0" data-i18n="slides.s18e.box1.body">“九重葛为紫茉莉科木质藤本，原产于南美”</p><div style="font-size:15px;color:var(--text-secondary);background:#f9f9f9;padding:8px 12px;border-radius:4px" data-i18n="slides.s18e.box1.calc">先验概率 P = 0.75 → 自信息量 I = -log₂(0.75) = 0.415 bits</div></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:3px solid var(--accent);padding:24px 26px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">SENSORY RELEVANCE (R)</span><span style="font-size:24px;font-weight:700;color:var(--accent)">3.059 <small style="font-size:13px">bits</small></span></div><svg width="100%" height="80" viewBox="0 0 400 80" fill="none" xmlns="http://www.w3.org/2000/svg" style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:4px"><rect x="15" y="12" width="70" height="26" rx="3" fill="#cbd5e1" /><rect x="95" y="12" width="180" height="26" rx="3" fill="#e2e8f0" /><rect x="285" y="12" width="100" height="26" rx="3" fill="#fed7aa" /><rect x="15" y="44" width="370" height="26" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/><text x="200" y="62" font-size="12" fill="#15803d" font-weight="bold" text-anchor="middle" data-i18n="slides.s18e.svgExp">身体感官触觉气泡 (P=0.12, I=3.059 bits - 提高 7.37 倍)</text></svg><h4 style="font-size:20px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18e.box2.title">身体感官互动气泡（低预期 · 极高信息量）</h4><p style="font-size:16px;color:var(--text-primary);line-height:1.55;margin:0" data-i18n="slides.s18e.box2.body">“红色的不是花瓣是苞片！请用手指触摸干爽纸质触感”</p><div style="font-size:15px;color:var(--accent);background:rgba(22,101,52,0.06);padding:8px 12px;border-radius:4px;font-weight:600" data-i18n="slides.s18e.box2.calc">先验概率 P = 0.12 → 自信息量 I = -log₂(0.12) = 3.059 bits</div></div></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:16px 22px;border-radius:4px;font-size:16px;color:var(--text-primary);display:flex;justify-content:space-around"><span data-i18n="slides.s18e.ticker1">拟人化对话：P = 0.15 → I = 2.737 bits</span><span data-i18n="slides.s18e.ticker2">花语提示：P = 0.25 → I = 2.000 bits</span><span data-i18n="slides.s18e.ticker3">传统分类学：P = 0.75 → I = 0.415 bits</span></div></div></div>"""
    },
    # s18f: E_gain Formula
    {
        "id": "s18f-cognitive-gain-formula",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：E_gain计算模型",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": [],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · COGNITIVE GAIN MODEL</div><div class="r">25 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18f.title">信息加权认知吸收量（E_gain）计算模型</h2><div class="analysis-kicker-desc" data-i18n="slides.s18f.guide">【公式推导】将空间注视概率与区域信息量加权求和，度量真实知识吸收总量</div></div><div class="analysis-anim-badge" aria-label="Gain Animation"><span class="analysis-anim-label">E_GAIN</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 24 L 38 18 L 68 12 L 106 6" stroke="var(--accent)" stroke-width="2" fill="none" /><circle cx="106" cy="6" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:24px 36px;border-radius:4px;display:flex;align-items:center;justify-content:space-between"><div style="font-family:var(--sans);font-size:46px;font-weight:200;color:var(--accent)">E_gain = ∑<sub style="font-size:20px">i=1</sub><sup style="font-size:20px">K</sup> [ p<sub style="font-size:20px">i</sub> × I(AOI<sub style="font-size:20px">i</sub>) ]</div><div style="font-size:20px;font-weight:600;color:var(--ink)" data-i18n="slides.s18f.meaning">期望认知吸收总量 = 各区域注视时间占比 × 语义自信息量</div></div><div class="analysis-visual-row" style="grid-template-columns:1.1fr 1fr;gap:24px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:24px 26px;border-radius:4px;display:flex;flex-direction:column;gap:10px"><span style="font-family:var(--mono);font-size:12px;color:var(--text-secondary);font-weight:700" data-i18n="slides.s18f.varTag">VARIABLE DEFINITIONS &amp; SYMBOLS</span><h4 style="font-size:20px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18f.varTitle">公式中各符号变量详尽释义</h4><div style="font-size:16px;color:var(--text-primary);line-height:1.65;display:flex;flex-direction:column;gap:6px"><div data-i18n="slides.s18f.v1">• E_gain (bits)：观众在整张标牌浏览中吸收的期望信息总量。</div><div data-i18n="slides.s18f.v2">• K：标牌划分的独立语义功能区（AOI）总数。</div><div data-i18n="slides.s18f.v3">• p_i = T_i / ∑T_j：观众在区域 i 的注视时间占比（满足 ∑ p_i = 1）。</div><div data-i18n="slides.s18f.v4">• I(AOI_i) (bits)：区域 i 的惊讶度自信息量（I = -log₂ P_prior）。</div></div></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:24px 26px;border-radius:4px;display:flex;flex-direction:column;gap:10px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18f.physTag">PHYSICAL &amp; COGNITIVE INSIGHT</span><h4 style="font-size:20px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18f.physTitle">数理模型的物理与认知含义</h4><p style="font-size:16px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18f.physBody">如果观众把 20 秒全部浪费在低惊讶度说明文上（I=0.42），E_gain 仅为 0.585 bits；但若视线探索了高惊讶度感官气泡（I=3.06），即便停留时间更短，E_gain 也将暴增至 1.332 bits 以上（+127.7%），真正度量了知识获取的质与量。</p></div></div></div></div>"""
    },
    # s18g: Markov Stagnation
    {
        "id": "s18g-markov-stagnation",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：马尔可夫死循环",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": ["entropy-markov-chart"],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · MARKOV TRANSITION</div><div class="r">26 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18g.title">马尔可夫转移矩阵：打破 93% 长文本死循环</h2><div class="analysis-kicker-desc" data-i18n="slides.s18g.guide">【动线解构】基于一阶马尔可夫链量化视线在各语义功能区之间的流转秩序</div></div><div class="analysis-anim-badge" aria-label="Markov Chain Animation"><span class="analysis-anim-label">MARKOV</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="7" stroke="var(--ink)" stroke-width="1.5" fill="none" /><circle cx="96" cy="15" r="7" stroke="var(--accent)" stroke-width="1.5" fill="none" /><path d="M 27 15 Q 58 5 89 15" stroke="var(--accent)" stroke-width="1.8" fill="none" /><path d="M 89 15 Q 58 25 27 15" stroke="var(--border-subtle)" stroke-width="1.5" stroke-dasharray="2 2" fill="none" /></svg></div></div><div class="analysis-body-group"><div class="analysis-hero-grid"><div class="analysis-sub-stack"><div class="analysis-sub-card"><span class="lbl">CTRL SELF-LOOP</span><span class="nb" style="color:rgba(220,38,38,0.9)">0.93<span class="unit">P(Text|Text)</span></span></div><div class="analysis-sub-card"><span class="lbl">EXP SELF-LOOP</span><span class="nb" style="color:var(--accent)">0.56<span class="unit">P(Text|Text)</span></span></div><div class="analysis-sub-card"><span class="lbl">STAGNATION DROP</span><span class="nb">-39.8<span class="unit">%</span></span></div></div><div class="analysis-hero-card"><h3 class="analysis-hero-title" data-i18n="slides.s18g.kpi.title">长文本自循环停滞率</h3><div class="analysis-hero-num" style="color:var(--accent)">93% → 56%</div><div class="analysis-hero-sub" data-i18n="slides.s18g.kpi.sub">马尔可夫矩阵证实：长文本死循环被彻底打破，视线平稳转导至感官互动区 (p &lt; 0.001)</div></div></div><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:24px"><div style="background:#fff;border:1px solid rgba(220,38,38,0.25);padding:24px 28px;border-radius:4px;display:flex;flex-direction:column;gap:8px"><h4 style="font-size:22px;color:rgba(220,38,38,0.9);font-weight:600;margin:0" data-i18n="slides.s18g.box1.title">对照组：死死困在长文本中 (0.93)</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.55;margin:0" data-i18n="slides.s18g.box1.body">视线在文本区内反复自循环（93%），跳至图片的概率仅 4%，形成了封闭的阅读陷阱与严重停滞。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:24px 28px;border-radius:4px;display:flex;flex-direction:column;gap:8px"><h4 style="font-size:22px;color:var(--accent);font-weight:600;margin:0" data-i18n="slides.s18g.box2.title">改良组：多模态自由流转 (多点开花)</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.55;margin:0" data-i18n="slides.s18g.box2.body">视线自正文平稳流向感官气泡（0.19）、图标（0.13）与花语（0.38），构建了顺畅的认知导流网络。</p></div></div></div></div>"""
    },
    # s18h: Efficiency Ratio
    {
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
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · EFFICIENCY RATIO</div><div class="r">27 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18h.title">认知信息传递能效比：单位视觉负荷的产出</h2><div class="analysis-kicker-desc" data-i18n="slides.s18h.guide">【能效建模】构建 η = E_gain / GTE 指标，量化单位视觉搜索努力换取的信息增益</div></div><div class="analysis-anim-badge" aria-label="Efficiency Animation"><span class="analysis-anim-label">EFFICIENCY</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="96" height="12" rx="6" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="12" y="12" width="70" height="8" rx="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:24px 36px;border-radius:4px;display:flex;align-items:center;justify-content:space-between"><div style="font-family:var(--sans);font-size:46px;font-weight:200;color:var(--accent)">η = E_gain / ( H<sub style="font-size:20px">GTE</sub> + ε )</div><div style="font-size:20px;font-weight:600;color:var(--ink)" data-i18n="slides.s18h.meaning">认知能效比 = 有效知识吸收量 / 动线转移熵（视觉搜索努力）</div></div><div class="analysis-visual-row" style="grid-template-columns:1.1fr 1fr;gap:24px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:24px 26px;border-radius:4px;display:flex;flex-direction:column;gap:10px"><span style="font-family:var(--mono);font-size:12px;color:var(--text-secondary);font-weight:700" data-i18n="slides.s18h.varTag">VARIABLE DEFINITIONS &amp; SYMBOLS</span><h4 style="font-size:20px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18h.varTitle">公式中各符号变量详尽释义</h4><div style="font-size:16px;color:var(--text-primary);line-height:1.65;display:flex;flex-direction:column;gap:6px"><div data-i18n="slides.s18h.v1">• η (bits/bit)：认知信息传递能效比，衡量单位搜索努力下的产出率。</div><div data-i18n="slides.s18h.v2">• E_gain (bits)：分子为有效知识吸收总量（有效收益）。</div><div data-i18n="slides.s18h.v3">• H_GTE (bits)：分母为动线转移熵（视觉搜索路径随机度与认知负荷）。</div><div data-i18n="slides.s18h.v4">• ε = 0.1：平滑常数，防止转移熵极低时的除零不稳定。</div></div></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:24px 26px;border-radius:4px;display:flex;flex-direction:column;gap:10px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18h.gainTag">SIGNIFICANT GAIN</span><h4 style="font-size:20px;color:var(--accent);font-weight:600;margin:0" data-i18n="slides.s18h.gainTitle">实证显著提升 +29.9% (p=0.004)</h4><p style="font-size:16px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18h.gainBody">对照组 1.083 ± 0.439 → 改良组 1.407 ± 0.347（t = 3.540, d = 0.982）。证实共创标牌并非单向堆砌信息，而是以更少、更舒适的视觉搜索消耗换取了更高价值的知识吸收，实现了认知减负与增效。</p></div></div></div></div>"""
    },
    # s18i1: Chart A (GTE)
    {
        "id": "s18i1-chart-gte",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：动线转移熵分析",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": ["entropy-chart-gte"],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · EMPIRICAL CHARTS · GAZE TRANSITION ENTROPY</div><div class="r">28 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18i1.title">动线转移熵 (GTE) 分析：探索路径与认知负荷</h2><div class="analysis-kicker-desc" data-i18n="slides.s18i1.guide">【图表A】量化视线转移随机度与跨语义功能区的自主探索活力</div></div><div class="analysis-anim-badge" aria-label="GTE Animation"><span class="analysis-anim-label">CHART A</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="5" fill="var(--text-secondary)"/><circle cx="96" cy="15" r="5" fill="var(--accent)"/><line x1="25" y1="15" x2="91" y2="15" stroke="var(--accent)" stroke-width="2"/></svg></div></div><div class="analysis-body-group" style="display:grid;grid-template-columns:1.3fr 1fr;gap:28px;align-items:center"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;padding:12px;display:flex;justify-content:center;align-items:center;height:500px"><img src="asset:entropy-chart-gte" alt="GTE Chart" style="max-width:100%;max-height:100%;object-fit:contain"></div><div style="display:flex;flex-direction:column;gap:20px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:26px 26px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--text-secondary);font-weight:700" data-i18n="slides.s18i1.c1.tag">METRIC MEANING</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:6px 0 10px" data-i18n="slides.s18i1.c1.title">动线转移熵 H_GTE (bits)</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18i1.c1.body">衡量视线在各语义区之间转移的一阶条件熵。低值代表死死困在单一区域（对照组 0.495 bits），高值代表跨区域自由流转（改良组 0.900 bits）。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:26px 26px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18i1.c2.tag">EMPIRICAL RESULT</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:6px 0 10px" data-i18n="slides.s18i1.c2.title">显著提升 +82.0% (p &lt; 0.0001 ***)</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18i1.c2.body">t(12) = 6.849, Cohen's d = 1.900。证实视线跳出了大段文字的吸附陷阱，实现了多模态区域间的活跃自主探索。</p></div></div></div></div>"""
    },
    # s18i2: Chart B (E_gain)
    {
        "id": "s18i2-chart-egain",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：认知吸收量全景",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": ["entropy-chart-egain"],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · EMPIRICAL CHARTS · COGNITIVE GAIN</div><div class="r">29 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18i2.title">认知吸收量 (E_gain) 配对检验：全量 13 人无一下降</h2><div class="analysis-kicker-desc" data-i18n="slides.s18i2.guide">【图表B】13 位被试配对连线全部陡峭向上倾斜，有效知识获得量翻倍暴增</div></div><div class="analysis-anim-badge" aria-label="Egain Animation"><span class="analysis-anim-label">CHART B</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 24 L 38 18 L 68 12 L 106 6" stroke="var(--accent)" stroke-width="2" fill="none" /><circle cx="106" cy="6" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group" style="display:grid;grid-template-columns:1.3fr 1fr;gap:28px;align-items:center"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;padding:12px;display:flex;justify-content:center;align-items:center;height:500px"><img src="asset:entropy-chart-egain" alt="Egain Chart" style="max-width:100%;max-height:100%;object-fit:contain"></div><div style="display:flex;flex-direction:column;gap:20px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:26px 26px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18i2.c1.tag">100% CONSISTENT LEAP</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:6px 0 10px" data-i18n="slides.s18i2.c1.title">全量 13 位被试单调显著递增</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18i2.c1.body">图中 13 条绿色细连线全部呈现极强的陡峭上扬趋势，无论是在 Group A 还是 Group B，没有一位被试出现下降（增长率区间 +86.8% ~ +243.1%）。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:26px 26px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18i2.c2.tag">DECISIVE EFFECT SIZE</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:6px 0 10px" data-i18n="slides.s18i2.c2.title">0.585 → 1.332 bits (+127.7%)</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18i2.c2.body">配对 t 检验 t(12) = 12.481, p &lt; 0.000001 ***, 效应量 Cohen's d = 3.462（远超常规大效应门槛 0.8），展现出决定性的改良效果。</p></div></div></div></div>"""
    },
    # s18i3: Chart C (eta)
    {
        "id": "s18i3-chart-eta",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：认知能效比实证",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": ["entropy-chart-eta"],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · EMPIRICAL CHARTS · EFFICIENCY RATIO</div><div class="r">30 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18i3.title">认知传递能效比 (η) 分析：单位视觉努力下的知识产出</h2><div class="analysis-kicker-desc" data-i18n="slides.s18i3.guide">【图表C】量化单位视线搜索转移负荷所能换取的有效信息增益</div></div><div class="analysis-anim-badge" aria-label="Eta Animation"><span class="analysis-anim-label">CHART C</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="96" height="12" rx="6" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="12" y="12" width="70" height="8" rx="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group" style="display:grid;grid-template-columns:1.3fr 1fr;gap:28px;align-items:center"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;padding:12px;display:flex;justify-content:center;align-items:center;height:500px"><img src="asset:entropy-chart-eta" alt="Eta Chart" style="max-width:100%;max-height:100%;object-fit:contain"></div><div style="display:flex;flex-direction:column;gap:20px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:26px 26px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18i3.c1.tag">EFFICIENCY METRIC</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:6px 0 10px" data-i18n="slides.s18i3.c1.title">能效比 η = E_gain / (GTE + 0.1)</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18i3.c1.body">将知识获得作为分子、搜索疲劳作为分母。橙色配对连线普遍上扬，证明观众以更高的“信息性价比”进行阅读。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:26px 26px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18i3.c2.tag">EMPIRICAL RESULT</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:6px 0 10px" data-i18n="slides.s18i3.c2.title">1.083 → 1.407 (+29.9%, p=0.004)</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18i3.c2.body">t(12) = 3.540, Cohen's d = 0.982。证实共创排版实现了认知减负与增效的完美结合。</p></div></div></div></div>"""
    },
    # s18i4: Chart D (SGE & KL)
    {
        "id": "s18i4-chart-sge",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：空间均衡度图解",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": ["entropy-chart-sge"],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · EMPIRICAL CHARTS · SPATIAL GAZE STRUCTURE</div><div class="r">31 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18i4.title">空间注视均衡度 (SGE) 与设计对齐 (KL 散度)</h2><div class="analysis-kicker-desc" data-i18n="slides.s18i4.guide">【图表D】量化视线空间离散度与共创设计预期的拟合收敛程度</div></div><div class="analysis-anim-badge" aria-label="SGE Animation"><span class="analysis-anim-label">CHART D</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="20" height="15" fill="#64748b"/><rect x="40" y="6" width="20" height="19" fill="#059669"/></svg></div></div><div class="analysis-body-group" style="display:grid;grid-template-columns:1.3fr 1fr;gap:28px;align-items:center"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;padding:12px;display:flex;justify-content:center;align-items:center;height:500px"><img src="asset:entropy-chart-sge" alt="SGE Chart" style="max-width:100%;max-height:100%;object-fit:contain"></div><div style="display:flex;flex-direction:column;gap:20px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:26px 26px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18i4.c1.tag">SPATIAL GAZE ENTROPY</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:6px 0 10px" data-i18n="slides.s18i4.c1.title">空间注视均衡度 SGE: +66.9%</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18i4.c1.body">1.203 → 2.008 bits (t=7.636, p&lt;0.0001)。证明视线不再单极化聚集在文本区，而是均匀覆盖了插图、花语和互动气泡。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:26px 26px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18i4.c2.tag">DESIGN CONVERGENCE</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:6px 0 10px" data-i18n="slides.s18i4.c2.title">KL 散度与设计预期对齐</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18i4.c2.body">D_KL 量化了实际视线分布与工坊设计意图的匹配度，证实共创原则成功达成了预期的人机交互导流目标。</p></div></div></div></div>"""
    },
    # s18j: Empirical Summary
    {
        "id": "s18j-empirical-summary",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：实证推断汇总",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": [],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · EMPIRICAL SUMMARY</div><div class="r">32 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18j.title">全量实证结果：有效认知信息吸收量翻倍暴增</h2><div class="analysis-kicker-desc" data-i18n="slides.s18j.guide">【全量验证】13 位被试配对检验证实有效认知吸收量与能效比实现全面跃升</div></div><div class="analysis-anim-badge" aria-label="Evidence Animation"><span class="analysis-anim-label">EVIDENCE</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><line x1="6" y1="25" x2="110" y2="25" stroke="var(--border-subtle)" stroke-width="1.5" /><path d="M 10 25 C 28 25, 42 6, 58 6 C 74 6, 88 25, 106 25" stroke="var(--ink)" stroke-width="1.5" fill="none" /><line x1="84" y1="11" x2="84" y2="25" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="2 2" /><g class="anim-stat-star"><circle cx="94" cy="17" r="3.5" fill="var(--accent)" /><circle cx="94" cy="17" r="7" stroke="var(--accent)" stroke-width="1" opacity="0.4" /></g></svg></div></div><div class="analysis-body-group"><div class="analysis-hero-grid"><div class="analysis-sub-stack"><div class="analysis-sub-card"><span class="lbl">PAIRED T-TEST</span><span class="nb">t(12) = 12.48<span class="unit">***</span></span></div><div class="analysis-sub-card"><span class="lbl">EFFECT SIZE</span><span class="nb">d = 3.46<span class="unit">Huge</span></span></div><div class="analysis-sub-card"><span class="lbl">EFFICIENCY (η)</span><span class="nb">+29.9<span class="unit">% (p=0.004)</span></span></div></div><div class="analysis-hero-card"><h3 class="analysis-hero-title" data-i18n="slides.s18j.kpi.title">有效认知信息吸收总量 (E_gain)</h3><div class="analysis-hero-num">+127.7<span class="unit">%</span></div><div class="analysis-hero-sub" data-i18n="slides.s18j.kpi.sub">0.585 bits → 1.332 bits (p &lt; 0.000001 ***) | 全量 13 位被试全部单调显著上升</div></div></div><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:24px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:24px 28px;border-radius:4px;display:flex;flex-direction:column;gap:8px"><div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18j.b1.tag">KNOWLEDGE ABSORPTION GAIN</span><span style="font-size:20px;font-weight:700;color:var(--accent)">+127.7%</span></div><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18j.box1.title">真实认知获取成倍跃升</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.55;margin:0" data-i18n="slides.s18j.box1.body">将注视时间与信息惊讶度结合后，实验组有效知识获得量翻倍，13 位被试无一下降（+86.8% ~ +243.1%）。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:24px 28px;border-radius:4px;display:flex;flex-direction:column;gap:8px"><div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18j.b2.tag">PROCESSING EFFICIENCY (η)</span><span style="font-size:20px;font-weight:700;color:var(--accent)">+29.9%</span></div><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18j.box2.title">认知信息传递能效比显著提升</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.55;margin:0" data-i18n="slides.s18j.box2.body">能效比从 1.083 提升至 1.407（p = 0.004, d = 0.982），证明观众以更少、更舒适的视觉搜索换取了更高价值的信息。</p></div></div></div></div>"""
    },
    # s18k: 13-Participant Table
    {
        "id": "s18k-participants-table",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：13人数据明细",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": [],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · PARTICIPANTS DATA LEDGER</div><div class="r">33 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18k.title">全量 13 位被试逐人明细数据表 (Group A &amp; B)</h2><div class="analysis-kicker-desc" data-i18n="slides.s18k.guide">【逐人明细】记录 Group A (7人) 与 Group B (6人) 每位被试的对照与改良数据及增益率</div></div><div class="analysis-anim-badge" aria-label="Ledger Animation"><span class="analysis-anim-label">LEDGER</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><line x1="10" y1="8" x2="106" y2="8" stroke="var(--border-subtle)" stroke-width="1.5" /><line x1="10" y1="15" x2="106" y2="15" stroke="var(--border-subtle)" stroke-width="1.5" /><line x1="10" y1="22" x2="106" y2="22" stroke="var(--border-subtle)" stroke-width="1.5" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;padding:32px 40px;display:grid;grid-template-columns:1fr 1fr;gap:48px;font-size:16px"><div style="display:flex;flex-direction:column;gap:12px"><div style="font-weight:700;color:var(--accent);border-bottom:2px solid var(--border-subtle);padding-bottom:10px;margin-bottom:6px;display:flex;justify-content:space-between"><span style="font-size:17px" data-i18n="slides.s18k.groupA">GROUP A · 九重葛 (N=7)</span><span style="font-size:14px;color:var(--text-secondary);font-weight:400">Ctrl → Exp (ΔE_gain)</span></div><div style="display:flex;justify-content:space-between"><span>akama_kumiko:</span><span>0.403 → 1.246 <strong style="color:var(--accent);margin-left:8px">+208.9%</strong></span></div><div style="display:flex;justify-content:space-between"><span>ataqi:</span><span>0.487 → 1.326 <strong style="color:var(--accent);margin-left:8px">+172.4%</strong></span></div><div style="display:flex;justify-content:space-between"><span>harada_keiko:</span><span>0.589 → 1.385 <strong style="color:var(--accent);margin-left:8px">+135.2%</strong></span></div><div style="display:flex;justify-content:space-between"><span>koga_eiichi:</span><span>0.366 → 0.974 <strong style="color:var(--accent);margin-left:8px">+166.0%</strong></span></div><div style="display:flex;justify-content:space-between"><span>moro_izumi:</span><span>0.699 → 1.429 <strong style="color:var(--accent);margin-left:8px">+104.4%</strong></span></div><div style="display:flex;justify-content:space-between"><span>saku_yoshisuke:</span><span>0.702 → 1.408 <strong style="color:var(--accent);margin-left:8px">+100.6%</strong></span></div><div style="display:flex;justify-content:space-between"><span>yamada_rena:</span><span>0.828 → 1.547 <strong style="color:var(--accent);margin-left:8px">+86.8%</strong></span></div></div><div style="display:flex;flex-direction:column;gap:12px"><div style="font-weight:700;color:var(--accent);border-bottom:2px solid var(--border-subtle);padding-bottom:10px;margin-bottom:6px;display:flex;justify-content:space-between"><span style="font-size:17px" data-i18n="slides.s18k.groupB">GROUP B · 千日小坊 (N=6)</span><span style="font-size:14px;color:var(--text-secondary);font-weight:400">Ctrl → Exp (ΔE_gain)</span></div><div style="display:flex;justify-content:space-between"><span>abcde:</span><span>0.603 → 1.295 <strong style="color:var(--accent);margin-left:8px">+114.7%</strong></span></div><div style="display:flex;justify-content:space-between"><span>kimura:</span><span>0.562 → 1.300 <strong style="color:var(--accent);margin-left:8px">+131.3%</strong></span></div><div style="display:flex;justify-content:space-between"><span>nonntixyan:</span><span>0.607 → 1.411 <strong style="color:var(--accent);margin-left:8px">+132.5%</strong></span></div><div style="display:flex;justify-content:space-between"><span>p186:</span><span>0.567 → 1.111 <strong style="color:var(--accent);margin-left:8px">+95.9%</strong></span></div><div style="display:flex;justify-content:space-between"><span>rep_chen:</span><span>0.793 → 1.513 <strong style="color:var(--accent);margin-left:8px">+90.7%</strong></span></div><div style="display:flex;justify-content:space-between"><span>umetu_ayane:</span><span>0.399 → 1.370 <strong style="color:var(--accent);margin-left:8px">+243.1%</strong></span></div></div></div></div></div>"""
    },
    # s18l: 3-Step Defense Guide
    {
        "id": "s18l-defense-guide",
        "chapterId": "deep-analysis",
        "layout": "data",
        "chapter": "5",
        "chapterTitle": "深度分析",
        "shortTitle": "阶段五：答辩话术指南",
        "animation": "statement-rise",
        "legacyLayout": "S06",
        "legacyClass": "slide",
        "assets": [],
        "claims": [],
        "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · DEFENSE &amp; REPORTING GUIDE</div><div class="r">34 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18l.title">答辩与学术汇报“三步法话术指南”</h2><div class="analysis-kicker-desc" data-i18n="slides.s18l.guide">【汇报策略】向导师与答辩评审阐述本信息论创新方法的专业逻辑路径</div></div><div class="analysis-anim-badge" aria-label="Defense Animation"><span class="analysis-anim-label">DEFENSE</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="7" stroke="var(--ink)" stroke-width="1.5" fill="none" /><text x="20" y="18" font-size="9" font-weight="700" text-anchor="middle" fill="var(--ink)">1</text><circle cx="58" cy="15" r="7" stroke="var(--ink)" stroke-width="1.5" fill="none" /><text x="58" y="18" font-size="9" font-weight="700" text-anchor="middle" fill="var(--ink)">2</text><circle cx="96" cy="15" r="7" stroke="var(--accent)" stroke-width="1.5" fill="none" /><text x="96" y="18" font-size="9" font-weight="700" text-anchor="middle" fill="var(--accent)">3</text></svg></div></div><div class="analysis-body-group"><div class="analysis-visual-row" style="grid-template-columns:repeat(3, 1fr);gap:24px"><div style="background:#fff;border:1px solid var(--border-subtle);border-top:4px solid var(--accent);padding:32px 26px;border-radius:4px;display:flex;flex-direction:column;gap:14px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18l.s1.tag">STEP 1 · 指出传统缺陷</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18l.s1.title">破除时长假象</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18l.s1.body">“传统分析只看时长，但对照组长文本的高停留实为认知受阻；马尔可夫矩阵证实其自循环停滞率高达 93%。”</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-top:4px solid var(--accent);padding:32px 26px;border-radius:4px;display:flex;flex-direction:column;gap:14px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18l.s2.tag">STEP 2 · 阐述信息论创新</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18l.s2.title">引入惊讶度加权</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18l.s2.body">“引入香农信息论，根据‘信息违背预期时信息量最大’原则构建 E_gain 与能效比 η，精准度量真实知识获得。”</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-top:4px solid var(--accent);padding:32px 26px;border-radius:4px;display:flex;flex-direction:column;gap:14px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700" data-i18n="slides.s18l.s3.tag">STEP 3 · 亮出硬核实证</span><h4 style="font-size:22px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18l.s3.title">证实有效吸收翻倍</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.65;margin:0" data-i18n="slides.s18l.s3.body">“全量 13 人配对检验证实 E_gain 提升 127.7%（p&lt;0.000001, d=3.46），13人全上升，科学证实共创卓越价值。”</p></div></div></div></div>"""
    }
]

# Write slide JSON files
for s in slides_data:
    fpath = os.path.join(SLIDES_DIR, f"{s['id']}.json")
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(s, f, ensure_ascii=False, indent=2)

print(f"[*] 成功更新 {len(slides_data)} 张完全数据驱动 i18n 的幻灯片 JSON 文件！")

# 2. Comprehensive 4-language dictionaries
dict_zh = {
    "slides.s18cover.shortTitle": "深度分析",
    "slides.s18cover.title": "基于信息熵与惊讶度的深度认知分析",
    "slides.s18cover.desc": "超越表面注视时长假象 · 计算认知科学量化模型与全量实证",
    
    "slides.s18a.tag1": "CONFOUNDING OF GAZE TIME",
    "slides.s18a.tag2": "SHANNON SURPRISAL PARADIGM",
    "slides.s18a.summary": "认知范式升级：从“表面物理注视时长”转向“单位视觉负荷下的有效信息吸收量与动线流转秩序”。",
    
    "slides.s18b.flawTag": "UNCHECKED ASSUMPTION: 均质化假定缺陷",
    
    "slides.s18c.tag1": "SUPERFICIAL METRIC (MISJUDGED)",
    "slides.s18c.tag2": "COGNITIVE REALITY (FRICTION)",
    "slides.s18c.rethink": "诊断结论：高停留时长反映的是信息解码受阻（Cognitive Friction）而非有效知识吸收，必须引入度量信息意外度与流转秩序的信息论工具。",
    
    "slides.s18d.tag1": "PREDICTIVE CODING",
    "slides.s18d.tag2": "SELF-INFORMATION (BITS)",
    
    "slides.s18e.svgCtrl": "大段科普长文本 (P=0.75, I=0.415 bits)",
    "slides.s18e.svgExp": "身体感官触觉气泡 (P=0.12, I=3.059 bits - 提高 7.37 倍)",
    "slides.s18e.box1.calc": "先验概率 P = 0.75 → 自信息量 I = -log₂(0.75) = 0.415 bits",
    "slides.s18e.box2.calc": "先验概率 P = 0.12 → 自信息量 I = -log₂(0.12) = 3.059 bits",
    "slides.s18e.ticker1": "拟人化对话：P = 0.15 → I = 2.737 bits",
    "slides.s18e.ticker2": "花语提示：P = 0.25 → I = 2.000 bits",
    "slides.s18e.ticker3": "传统分类学：P = 0.75 → I = 0.415 bits",
    
    "slides.s18f.meaning": "期望认知吸收总量 = 各区域注视时间占比 × 语义自信息量",
    "slides.s18f.varTag": "VARIABLE DEFINITIONS & SYMBOLS",
    "slides.s18f.varTitle": "公式中各符号变量详尽释义",
    "slides.s18f.v1": "• E_gain (bits)：观众在整张标牌浏览中吸收的期望信息总量。",
    "slides.s18f.v2": "• K：标牌划分的独立语义功能区（AOI）总数。",
    "slides.s18f.v3": "• p_i = T_i / ∑T_j：观众在区域 i 的注视时间占比（满足 ∑ p_i = 1）。",
    "slides.s18f.v4": "• I(AOI_i) (bits)：区域 i 的惊讶度自信息量（I = -log₂ P_prior）。",
    "slides.s18f.physTag": "PHYSICAL & COGNITIVE INSIGHT",
    "slides.s18f.physTitle": "数理模型的物理与认知含义",
    "slides.s18f.physBody": "如果观众把 20 秒全部浪费在低惊讶度说明文上（I=0.42），E_gain 仅为 0.585 bits；但若视线探索了高惊讶度感官气泡（I=3.06），即便停留时间更短，E_gain 也将暴增至 1.332 bits 以上（+127.7%），真正度量了知识获取的质与量。",
    
    "slides.s18h.meaning": "认知能效比 = 有效知识吸收量 / 动线转移熵（视觉搜索努力）",
    "slides.s18h.varTag": "VARIABLE DEFINITIONS & SYMBOLS",
    "slides.s18h.varTitle": "公式中各符号变量详尽释义",
    "slides.s18h.v1": "• η (bits/bit)：认知信息传递能效比，衡量单位搜索努力下的产出率。",
    "slides.s18h.v2": "• E_gain (bits)：分子为有效知识吸收总量（有效收益）。",
    "slides.s18h.v3": "• H_GTE (bits)：分母为动线转移熵（视觉搜索路径随机度与认知负荷）。",
    "slides.s18h.v4": "• ε = 0.1：平滑常数，防止转移熵极低时的除零不稳定。",
    "slides.s18h.gainTag": "SIGNIFICANT GAIN",
    "slides.s18h.gainTitle": "实证显著提升 +29.9% (p=0.004)",
    "slides.s18h.gainBody": "对照组 1.083 ± 0.439 → 改良组 1.407 ± 0.347（t = 3.540, d = 0.982）。证实共创标牌并非单向堆砌信息，而是以更少、更舒适的视觉搜索消耗换取了更高价值的知识吸收，实现了认知减负与增效。",
    
    "slides.s18i1.c1.tag": "METRIC MEANING",
    "slides.s18i1.c1.title": "动线转移熵 H_GTE (bits)",
    "slides.s18i1.c1.body": "衡量视线在各语义区之间转移的一阶条件熵。低值代表死死困在单一区域（对照组 0.495 bits），高值代表跨区域自由流转（改良组 0.900 bits）。",
    "slides.s18i1.c2.tag": "EMPIRICAL RESULT",
    "slides.s18i1.c2.title": "显著提升 +82.0% (p < 0.0001 ***)",
    "slides.s18i1.c2.body": "t(12) = 6.849, Cohen's d = 1.900。证实视线跳出了大段文字的吸附陷阱，实现了多模态区域间的活跃自主探索。",
    
    "slides.s18i2.c1.tag": "100% CONSISTENT LEAP",
    "slides.s18i2.c1.title": "全量 13 位被试单调显著递增",
    "slides.s18i2.c1.body": "图中 13 条绿色细连线全部呈现极强的陡峭上扬趋势，无论是在 Group A 还是 Group B，没有一位被试出现下降（增长率区间 +86.8% ~ +243.1%）。",
    "slides.s18i2.c2.tag": "DECISIVE EFFECT SIZE",
    "slides.s18i2.c2.title": "0.585 → 1.332 bits (+127.7%)",
    "slides.s18i2.c2.body": "配对 t 检验 t(12) = 12.481, p < 0.000001 ***, 效应量 Cohen's d = 3.462（远超常规大效应门槛 0.8），展现出决定性的改良效果。",
    
    "slides.s18i3.c1.tag": "EFFICIENCY METRIC",
    "slides.s18i3.c1.title": "能效比 η = E_gain / (GTE + 0.1)",
    "slides.s18i3.c1.body": "将知识获得作为分子、搜索疲劳作为分母。橙色配对连线普遍上扬，证明观众以更高的“信息性价比”进行阅读。",
    "slides.s18i3.c2.tag": "EMPIRICAL RESULT",
    "slides.s18i3.c2.title": "1.083 → 1.407 (+29.9%, p=0.004)",
    "slides.s18i3.c2.body": "t(12) = 3.540, Cohen's d = 0.982。证实共创排版实现了认知减负与增效的完美结合。",
    
    "slides.s18i4.c1.tag": "SPATIAL GAZE ENTROPY",
    "slides.s18i4.c1.title": "空间注视均衡度 SGE: +66.9%",
    "slides.s18i4.c1.body": "1.203 → 2.008 bits (t=7.636, p<0.0001)。证明视线不再单极化聚集在文本区，而是均匀覆盖了插图、花语和互动气泡。",
    "slides.s18i4.c2.tag": "DESIGN CONVERGENCE",
    "slides.s18i4.c2.title": "KL 散度与设计预期对齐",
    "slides.s18i4.c2.body": "D_KL 量化了实际视线分布与工坊设计意图的匹配度，证实共创原则成功达成了预期的人机交互导流目标。",
    
    "slides.s18j.b1.tag": "KNOWLEDGE ABSORPTION GAIN",
    "slides.s18j.b2.tag": "PROCESSING EFFICIENCY (η)",
    
    "slides.s18k.groupA": "GROUP A · 九重葛 (N=7)",
    "slides.s18k.groupB": "GROUP B · 千日小坊 (N=6)",
    
    "slides.s18l.s1.tag": "STEP 1 · 指出传统缺陷",
    "slides.s18l.s2.tag": "STEP 2 · 阐述信息论创新",
    "slides.s18l.s3.tag": "STEP 3 · 亮出硬核实证"
}

dict_en = {
    "slides.s18cover.shortTitle": "Deep Analysis",
    "slides.s18cover.title": "Deep Cognitive Analysis: Information Entropy & Surprisal",
    "slides.s18cover.desc": "Transcending Gaze Dwell Illusions · Computational Cognitive Modeling & Empirical Validation",
    
    "slides.s18a.tag1": "CONFOUNDING OF GAZE TIME",
    "slides.s18a.tag2": "SHANNON SURPRISAL PARADIGM",
    "slides.s18a.summary": "Cognitive Paradigm Shift: Transitioning from raw dwell time to information gain and transition order.",
    
    "slides.s18b.flawTag": "UNCHECKED ASSUMPTION: HOMOGENEOUS VALUE FLAW",
    
    "slides.s18c.tag1": "SUPERFICIAL METRIC (MISJUDGED)",
    "slides.s18c.tag2": "COGNITIVE REALITY (FRICTION)",
    "slides.s18c.rethink": "Diagnosis: High dwell duration reflects cognitive friction and deciphering hurdles rather than deep knowledge absorption.",
    
    "slides.s18d.tag1": "PREDICTIVE CODING",
    "slides.s18d.tag2": "SELF-INFORMATION (BITS)",
    
    "slides.s18e.svgCtrl": "Dense Explanatory Text (P=0.75, I=0.415 bits)",
    "slides.s18e.svgExp": "Sensory Interactive Bubble (P=0.12, I=3.059 bits - 7.37x Gain)",
    "slides.s18e.box1.calc": "Prior Probability P = 0.75 → Self-Information I = -log2(0.75) = 0.415 bits",
    "slides.s18e.box2.calc": "Prior Probability P = 0.12 → Self-Information I = -log2(0.12) = 3.059 bits",
    "slides.s18e.ticker1": "Dialogic Prompt: P = 0.15 → I = 2.737 bits",
    "slides.s18e.ticker2": "Floral Note: P = 0.25 → I = 2.000 bits",
    "slides.s18e.ticker3": "Taxonomy: P = 0.75 → I = 0.415 bits",
    
    "slides.s18f.meaning": "Expected Knowledge Gain = ∑ (AOI Gaze Proportion × Semantic Surprisal)",
    "slides.s18f.varTag": "VARIABLE DEFINITIONS & SYMBOLS",
    "slides.s18f.varTitle": "Mathematical Variable Definitions",
    "slides.s18f.v1": "• E_gain (bits): Total expected information gain absorbed across the signage.",
    "slides.s18f.v2": "• K: Total number of independent semantic AOIs on the board.",
    "slides.s18f.v3": "• p_i = T_i / ∑T_j: Proportion of total dwell time spent in AOI i (∑ p_i = 1).",
    "slides.s18f.v4": "• I(AOI_i) (bits): Surprisal self-information of AOI i (I = -log2 P_prior).",
    "slides.s18f.physTag": "PHYSICAL & COGNITIVE INSIGHT",
    "slides.s18f.physTitle": "Physical and Cognitive Interpretation",
    "slides.s18f.physBody": "Spending 20s stuck on generic text yields only 0.585 bits. Exploring high-surprisal sensory prompts lifts E_gain to 1.332 bits (+127.7%), capturing genuine learning.",
    
    "slides.s18h.meaning": "Cognitive Efficiency Ratio = Knowledge Gain / Transition Entropy (Search Effort)",
    "slides.s18h.varTag": "VARIABLE DEFINITIONS & SYMBOLS",
    "slides.s18h.varTitle": "Efficiency Variable Definitions",
    "slides.s18h.v1": "• η (bits/bit): Information transmission efficiency per unit visual effort.",
    "slides.s18h.v2": "• E_gain (bits): Numerator representing effective knowledge absorbed.",
    "slides.s18h.v3": "• H_GTE (bits): Denominator representing gaze transition entropy and search burden.",
    "slides.s18h.v4": "• ε = 0.1: Smoothing constant preventing zero-division instability.",
    "slides.s18h.gainTag": "SIGNIFICANT GAIN",
    "slides.s18h.gainTitle": "Statistically Significant Leap +29.9% (p=0.004)",
    "slides.s18h.gainBody": "Control 1.083 ± 0.439 → Intervention 1.407 ± 0.347 (t = 3.540, d = 0.982). Visitors absorbed higher knowledge value with lighter search burden.",
    
    "slides.s18i1.c1.tag": "METRIC MEANING",
    "slides.s18i1.c1.title": "Gaze Transition Entropy H_GTE (bits)",
    "slides.s18i1.c1.body": "Quantifies first-order transition entropy across AOIs. Low values indicate text traps (0.495 bits); high values reflect fluid multi-modal browsing (0.900 bits).",
    "slides.s18i1.c2.tag": "EMPIRICAL RESULT",
    "slides.s18i1.c2.title": "Significant Increase +82.0% (p < 0.0001 ***)",
    "slides.s18i1.c2.body": "t(12) = 6.849, Cohen's d = 1.900. Confirming visitors broke free from dense text traps into active multi-modal exploration.",
    
    "slides.s18i2.c1.tag": "100% CONSISTENT LEAP",
    "slides.s18i2.c1.title": "100% Monotonic Increase Across All 13 Participants",
    "slides.s18i2.c1.body": "All 13 participant trajectories sloped steeply upward with zero exceptions (+86.8% to +243.1% individual gains across Group A and B).",
    "slides.s18i2.c2.tag": "DECISIVE EFFECT SIZE",
    "slides.s18i2.c2.title": "0.585 → 1.332 bits (+127.7%)",
    "slides.s18i2.c2.body": "Paired t-test t(12) = 12.481, p < 0.000001 ***, Cohen's d = 3.462 (vastly exceeding the 0.8 benchmark for large effects).",
    
    "slides.s18i3.c1.tag": "EFFICIENCY METRIC",
    "slides.s18i3.c1.title": "Efficiency Ratio η = E_gain / (GTE + 0.1)",
    "slides.s18i3.c1.body": "Balancing knowledge yield over search effort. Paired lines consistently rose, proving higher information cost-performance.",
    "slides.s18i3.c2.tag": "EMPIRICAL RESULT",
    "slides.s18i3.c2.title": "1.083 → 1.407 (+29.9%, p=0.004)",
    "slides.s18i3.c2.body": "t(12) = 3.540, Cohen's d = 0.982. Proving co-creation signage reduced cognitive burden while elevating information absorption.",
    
    "slides.s18i4.c1.tag": "SPATIAL GAZE ENTROPY",
    "slides.s18i4.c1.title": "Spatial Gaze Entropy SGE: +66.9%",
    "slides.s18i4.c1.body": "1.203 → 2.008 bits (t=7.636, p<0.0001). Gaze broadened from text fixation to balanced exploration of graphics, flower notes, and sensory prompts.",
    "slides.s18i4.c2.tag": "DESIGN CONVERGENCE",
    "slides.s18i4.c2.title": "KL Divergence & Design Intent Alignment",
    "slides.s18i4.c2.body": "D_KL measured how closely actual gaze matched co-creation design intentions, verifying successful interactive flow guidance.",
    
    "slides.s18j.b1.tag": "KNOWLEDGE ABSORPTION GAIN",
    "slides.s18j.b2.tag": "PROCESSING EFFICIENCY (η)",
    
    "slides.s18k.groupA": "GROUP A · Bougainvillea (N=7)",
    "slides.s18k.groupB": "GROUP B · Alternanthera (N=6)",
    
    "slides.s18l.s1.tag": "STEP 1 · Expose Conventional Flaws",
    "slides.s18l.s2.tag": "STEP 2 · Introduce Information Theory",
    "slides.s18l.s3.tag": "STEP 3 · Present Hard Evidence"
}

dict_ja = {
    "slides.s18cover.shortTitle": "深層分析",
    "slides.s18cover.title": "情報エントロピーとサプライザルに基づく認知深化分析",
    "slides.s18cover.desc": "表面的な注視時間の錯覚を超えて · 計算論的認知モデルの構築と全量実証検証",
    
    "slides.s18a.tag1": "注視時間の交絡要因",
    "slides.s18a.tag2": "シャノンサプライザルモデル",
    "slides.s18a.summary": "認知パラダイム転換：単なる物理的注視時間から「視覚負荷あたりの有効情報吸収量と動線秩序」へ。",
    
    "slides.s18b.flawTag": "暗黙の前提：均質性仮定の欠陥",
    
    "slides.s18c.tag1": "表面指標の誤読",
    "slides.s18c.tag2": "認知的現実（読解摩擦）",
    "slides.s18c.rethink": "診断結論：長時間の滞在は深い知識吸収ではなく読解摩擦（Cognitive Friction）を反映しており、サプライザルと遷移秩序の導入が不可欠です。",
    
    "slides.s18d.tag1": "予測符号化理論",
    "slides.s18d.tag2": "自己情報量（ビット単位）",
    
    "slides.s18e.svgCtrl": "長文解説テキスト (P=0.75, I=0.415 bits)",
    "slides.s18e.svgExp": "感覚インタラクティブ吹出 (P=0.12, I=3.059 bits - 7.37倍)",
    "slides.s18e.box1.calc": "事前確率 P = 0.75 → 自己情報量 I = -log₂(0.75) = 0.415 bits",
    "slides.s18e.box2.calc": "事前確率 P = 0.12 → 自己情報量 I = -log₂(0.12) = 3.059 bits",
    "slides.s18e.ticker1": "対話型プロンプト：P = 0.15 → I = 2.737 bits",
    "slides.s18e.ticker2": "花言葉ノート：P = 0.25 → I = 2.000 bits",
    "slides.s18e.ticker3": "分類学解説：P = 0.75 → I = 0.415 bits",
    
    "slides.s18f.meaning": "期待認知獲得総量 = 各領域の注視時間割合 × 意味論的サプライザル",
    "slides.s18f.varTag": "数理変数と記号の定義",
    "slides.s18f.varTitle": "公式内の各変数の詳細定義",
    "slides.s18f.v1": "• E_gain (bits)：サインボード全体で獲得された期待情報総量。",
    "slides.s18f.v2": "• K：サインボード上で分割された独立意味領域（AOI）の総数。",
    "slides.s18f.v3": "• p_i = T_i / ∑T_j：領域 i における注視時間の割合（∑ p_i = 1）。",
    "slides.s18f.v4": "• I(AOI_i) (bits)：領域 i のサプライザル自己情報量（I = -log₂ P_prior）。",
    "slides.s18f.physTag": "物理的および認知的解釈",
    "slides.s18f.physTitle": "数理モデルの認知科学的意味",
    "slides.s18f.physBody": "定型文に20秒停滞しても獲得量はわずか 0.585 bits ですが、高サプライザルな感覚吹出に視線が届くことで 1.332 bits（+127.7%）へと跳躍し、質の高い学びを定量化します。",
    
    "slides.s18h.meaning": "認知情報効率比 = 有効知識獲得量 / 動線遷移エントロピー（探索負荷）",
    "slides.s18h.varTag": "効率指標の変数定義",
    "slides.s18h.varTitle": "公式内の各変数の詳細定義",
    "slides.s18h.v1": "• η (bits/bit)：視覚探索努力あたりの情報伝達能効率比。",
    "slides.s18h.v2": "• E_gain (bits)：分子となる有効知識獲得量（正の成果）。",
    "slides.s18h.v3": "• H_GTE (bits)：分母となる注視遷移エントロピー（探索負荷）。",
    "slides.s18h.v4": "• ε = 0.1：ゼロ除算を防ぐための平滑化定数。",
    "slides.s18h.gainTag": "統計的有意な向上",
    "slides.s18h.gainTitle": "実証的有意向上 +29.9% (p=0.004)",
    "slides.s18h.gainBody": "対照群 1.083 ± 0.439 → 改良群 1.407 ± 0.347（t = 3.540, d = 0.982）。より負担の少ない視覚探索でより価値の高い知識獲得を達成しました。",
    
    "slides.s18i1.c1.tag": "指標の定義",
    "slides.s18i1.c1.title": "注視遷移エントロピー H_GTE (bits)",
    "slides.s18i1.c1.body": "各意味領域間の一次条件付き遷移エントロピー。低値は単一領域での膠着（0.495 bits）、高値はマルチモーダルな流転（0.900 bits）を示します。",
    "slides.s18i1.c2.tag": "実証結果",
    "slides.s18i1.c2.title": "有意な向上 +82.0% (p < 0.0001 ***)",
    "slides.s18i1.c2.body": "t(12) = 6.849, Cohen's d = 1.900。視線が長文トラップを脱し、自発的かつ活発な領域間探索を実現しました。",
    
    "slides.s18i2.c1.tag": "13名全員の単調増加",
    "slides.s18i2.c1.title": "全13名の被験者で例外なき向上",
    "slides.s18i2.c1.body": "13本の緑色連結線すべてが急峻な上昇傾向を示し、Group A・Bともに1人も低下しませんでした（向上率 +86.8%〜+243.1%）。",
    "slides.s18i2.c2.tag": "決定的な効果量",
    "slides.s18i2.c2.title": "0.585 → 1.332 bits (+127.7%)",
    "slides.s18i2.c2.body": "対応のある t 検定 t(12) = 12.481, p < 0.000001 ***, 効果量 Cohen's d = 3.462（極めて巨大な改善効果）。",
    
    "slides.s18i3.c1.tag": "効率性指標",
    "slides.s18i3.c1.title": "能効率比 η = E_gain / (GTE + 0.1)",
    "slides.s18i3.c1.body": "知識獲得を分子、探索疲労を分母と定義。全被験者で効率比が上昇し、より高い情報対費用効果を実証。",
    "slides.s18i3.c2.tag": "実証結果",
    "slides.s18i3.c2.title": "1.083 → 1.407 (+29.9%, p=0.004)",
    "slides.s18i3.c2.body": "t(12) = 3.540, Cohen's d = 0.982。共創サインが認知負荷の軽減と獲得量の増大を両立させた証拠です。",
    
    "slides.s18i4.c1.tag": "空間注視エントロピー",
    "slides.s18i4.c1.title": "空間注視均等度 SGE: +66.9%",
    "slides.s18i4.c1.body": "1.203 → 2.008 bits (t=7.636, p<0.0001)。視線が文章領域への一極集中から、図版や感覚吹出へのバランス良い分散へと転換。",
    "slides.s18i4.c2.tag": "設計意図への適合",
    "slides.s18i4.c2.title": "KLダイバージェンスと共創適合",
    "slides.s18i4.c2.body": "実際の注視分布とワークショップ設計意図の一致度を定量化し、意図通りの対話的誘導を達成したことを証明。",
    
    "slides.s18j.b1.tag": "知識獲得量の飛躍",
    "slides.s18j.b2.tag": "情報処理効率 (η)",
    
    "slides.s18k.groupA": "GROUP A · ブーゲンビレア (N=7)",
    "slides.s18k.groupB": "GROUP B · センニチコボウ (N=6)",
    
    "slides.s18l.s1.tag": "STEP 1 · 従来指標の限界指摘",
    "slides.s18l.s2.tag": "STEP 2 · 情報理論の革新性提示",
    "slides.s18l.s3.tag": "STEP 3 · 確固たる実証成果提示"
}

# Update all 4 JSON dictionaries
for fname, updates in [('zh.json', dict_zh), ('en.json', dict_en), ('ja.json', dict_ja), ('es-MX.json', dict_en)]:
    fpath = os.path.join(I18N_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        d = json.load(f)
    d.update(updates)
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

print("[*] 4 种语言字典全部同步完成！")
