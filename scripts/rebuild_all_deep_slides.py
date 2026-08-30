# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLIDES_DIR = os.path.join(BASE_DIR, 'src', 'content', 'slides')
MANIFEST_FILE = os.path.join(BASE_DIR, 'deck-manifest.json')
I18N_DIR = os.path.join(BASE_DIR, 'src', 'i18n')

deep_slides = [
    # 1. s18a: Introduction & Paradigm Shift
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · SECTION INTRO</div><div class="r">19 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18a.title">基于信息熵与惊讶度理论的深度分析</h2><div class="analysis-kicker-desc" data-i18n="slides.s18a.guide">【理论引入】超越“注视时长”表面假象，量化真实知识吸收与阅读认知流</div></div><div class="analysis-anim-badge" aria-label="Entropy Wave Animation"><span class="analysis-anim-label">THEORY</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 6 15 Q 32 4 58 15 T 110 15" stroke="var(--border-subtle)" stroke-width="1.5" fill="none" /><path d="M 6 15 Q 32 26 58 15 T 110 15" stroke="var(--accent)" stroke-width="2" fill="none" /><circle cx="58" cy="15" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:24px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:28px 32px;border-radius:4px;display:flex;flex-direction:column;justify-content:center;gap:14px"><span style="font-family:var(--mono);font-size:13px;color:var(--text-secondary);font-weight:700;letter-spacing:0.08em">CONFOUNDING OF GAZE TIME</span><h3 style="font-size:26px;color:var(--ink);font-weight:600;line-height:1.3" data-i18n="slides.s18a.q1.title">看得久就是好吗？</h3><p style="font-size:18px;color:var(--text-primary);line-height:1.55" data-i18n="slides.s18a.q1.body">传统眼动指标假定“注视越久 = 越感兴趣”。但在植物标牌中，生僻文字导致的卡顿与犹豫常被误判为深度沉浸。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:28px 32px;border-radius:4px;display:flex;flex-direction:column;justify-content:center;gap:14px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700;letter-spacing:0.08em">SHANNON SURPRISAL PARADIGM</span><h3 style="font-size:26px;color:var(--ink);font-weight:600;line-height:1.3" data-i18n="slides.s18a.q2.title">信息论度量真实获得</h3><p style="font-size:18px;color:var(--text-primary);line-height:1.55" data-i18n="slides.s18a.q2.body">引入香农信息熵与惊讶度（Surprisal），结合“信息违背预期时信息量最大”的原理，精确量化观众吸收的有效知识增量。</p></div></div></div><div class="analysis-ledger-v2"><div class="analysis-ledger-row"><div class="analysis-ledger-left"><span class="analysis-ledger-tag">PARADIGM</span><strong class="analysis-ledger-title" data-i18n="slides.s18a.finding1.title" data-hybrid-ja="never">认知范式升级</strong></div><p class="analysis-ledger-detail" data-i18n="slides.s18a.finding1.body" data-hybrid-ja="never">从“表面注视时长”转向“单位视觉负荷下的有效信息吸收量与动线秩序”。</p></div><div class="analysis-ledger-row"><div class="analysis-ledger-left"><span class="analysis-ledger-tag">FRAMEWORK</span><strong class="analysis-ledger-title" data-i18n="slides.s18a.finding2.title" data-hybrid-ja="never">循序渐进分析链条</strong></div><p class="analysis-ledger-detail" data-i18n="slides.s18a.finding2.body" data-hybrid-ja="never">分步拆解：常规指标局限 → 文本停滞误区 → 惊讶度建模 → 案例计算 → 马尔可夫死循环 → 4维实证图解与全量检验。</p></div></div></div>'
    },
    # 2. s18b: Conventional Metrics (Spacious, No redundant bottom ledger)
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · CONVENTIONAL METRICS</div><div class="r">20 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18b.title">传统眼动三大常规指标及其假设</h2><div class="analysis-kicker-desc" data-i18n="slides.s18b.guide">【基线梳理】归纳现有植物标牌研究普遍依赖的三大常规眼动度量体系</div></div><div class="analysis-anim-badge" aria-label="Baseline Animation"><span class="analysis-anim-label">BASELINE</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="8" width="24" height="14" rx="2" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="46" y="8" width="24" height="14" rx="2" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="82" y="8" width="24" height="14" rx="2" stroke="var(--border-subtle)" stroke-width="1.5" /></svg></div></div><div class="analysis-body-group" style="height:520px;display:flex;flex-direction:column;justify-content:space-between"><div class="analysis-visual-row" style="grid-template-columns:repeat(3, 1fr);gap:24px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:28px 24px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700">METRIC 01</span><h4 style="font-size:24px;color:var(--ink);font-weight:600" data-i18n="slides.s18b.m1.title">注视时长 (Dwell Time)</h4><p style="font-size:17px;color:var(--text-primary);line-height:1.55" data-i18n="slides.s18b.m1.body">记录视线在某区域停留的总秒数或时间百分比，底层假设“停越久 = 越感兴趣”。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:28px 24px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700">METRIC 02</span><h4 style="font-size:24px;color:var(--ink);font-weight:600" data-i18n="slides.s18b.m2.title">注视次数 (Fixation Count)</h4><p style="font-size:17px;color:var(--text-primary);line-height:1.55" data-i18n="slides.s18b.m2.body">记录视线落入该区域的落点频次，底层假设“落点越多 = 越具视觉重要性”。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:28px 24px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700">METRIC 03</span><h4 style="font-size:24px;color:var(--ink);font-weight:600" data-i18n="slides.s18b.m3.title">注视热力图 (Heatmap)</h4><p style="font-size:17px;color:var(--text-primary);line-height:1.55" data-i18n="slides.s18b.m3.body">高斯核密度渲染的空间点云，底层假设“红色高亮区代表绝对吸引力焦点”。</p></div></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid rgba(220,38,38,0.85);padding:20px 26px;border-radius:4px"><div style="font-size:15px;font-family:var(--mono);font-weight:700;color:rgba(220,38,38,0.9);margin-bottom:4px">UNCHECKED ASSUMPTION</div><p style="font-size:17px;color:var(--ink);line-height:1.5;margin:0" data-i18n="slides.s18b.critical_flaw">三大指标默认“每秒注视具有均等的信息加工价值”，仅记录物理停留坐标，无法辨识注视背后的认知理解质量与晦涩文字带来的无序停滞。</p></div></div></div>'
    },
    # 3. s18c: Cognitive Friction
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · COGNITIVE FRICTION</div><div class="r">21 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18c.title">常规指标的致命误区：认知受阻而非深度阅读</h2><div class="analysis-kicker-desc" data-i18n="slides.s18c.guide">【误区揭示】剖析传统大段科普文字如何造成高注视时长的“虚假繁荣”</div></div><div class="analysis-anim-badge" aria-label="Friction Animation"><span class="analysis-anim-label">CONFOUNDING</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><line x1="10" y1="15" x2="106" y2="15" stroke="rgba(220,38,38,0.8)" stroke-width="2" stroke-dasharray="4 2" /><circle cx="58" cy="15" r="5" fill="rgba(220,38,38,0.9)" /></svg></div></div><div class="analysis-body-group" style="height:520px;display:flex;flex-direction:column;justify-content:space-between"><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:28px"><div style="background:#fff;border:1px solid rgba(220,38,38,0.3);border-top:4px solid rgba(220,38,38,0.85);padding:30px 32px;border-radius:4px;display:flex;flex-direction:column;gap:14px"><span style="font-family:var(--mono);font-size:13px;color:rgba(220,38,38,0.9);font-weight:700">SUPERFICIAL METRIC (MISJUDGED)</span><h4 style="font-size:26px;color:var(--ink);font-weight:600" data-i18n="slides.s18c.c1.title">表面数据假象：长文本注视占比 44.3%</h4><p style="font-size:18px;color:var(--text-primary);line-height:1.6" data-i18n="slides.s18c.c1.body">在对照组中，说明文字区注视时长位居首位。传统眼动模型据此推论“观众对大段科普内容最感兴趣”。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-top:4px solid var(--accent);padding:30px 32px;border-radius:4px;display:flex;flex-direction:column;gap:14px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700">COGNITIVE REALITY (FRICTION)</span><h4 style="font-size:26px;color:var(--ink);font-weight:600" data-i18n="slides.s18c.c2.title">真实认知困境：认知摩擦与阅读停滞</h4><p style="font-size:18px;color:var(--text-primary);line-height:1.6" data-i18n="slides.s18c.c2.body">大段生僻拉丁学名与形态学术语导致“读不下去、找不到重点”，视线在文本内被动打转卡顿，实为负荷过载而非深度阅读。</p></div></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:18px 24px;border-radius:4px"><p style="font-size:16.5px;color:var(--text-primary);line-height:1.5;margin:0" data-i18n="slides.s18c.rethink">诊断结论：高停留时长反映的是信息解码受阻（Cognitive Friction）而非有效知识吸收，必须引入度量信息意外度与流转秩序的信息论工具。</p></div></div></div>'
    },
    # 4. s18d: Shannon Surprisal Theory (Huge clean focus)
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · SURPRISAL THEORY</div><div class="r">22 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18d.title">香农信息论与惊讶度：违背预期的认知增益</h2><div class="analysis-kicker-desc" data-i18n="slides.s18d.guide">【数理建模】引入自信息量 I = -log2(P)，量化反常识感官互动的高知识价值</div></div><div class="analysis-anim-badge" aria-label="Surprisal Animation"><span class="analysis-anim-label">SURPRISAL</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 25 C 28 25, 42 6, 58 6 C 74 6, 88 25, 106 25" stroke="var(--ink)" stroke-width="1.5" fill="none" /><line x1="58" y1="6" x2="58" y2="25" stroke="var(--accent)" stroke-width="2" stroke-dasharray="2 2" /></svg></div></div><div class="analysis-body-group" style="height:520px;display:flex;flex-direction:column;justify-content:space-between"><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:24px 32px;border-radius:4px;display:flex;align-items:center;justify-content:space-between"><div style="font-family:var(--sans);font-size:46px;font-weight:200;color:var(--accent)">I(AOI) = - log₂( P<sub style="font-size:22px">prior</sub> )</div><div style="font-size:22px;font-weight:600;color:var(--ink)" data-i18n="slides.s18d.axiom">“信息在违背预期时，其承载的信息量最大”</div></div><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:24px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:26px 28px;border-radius:4px;display:flex;flex-direction:column;gap:10px"><span style="font-family:var(--mono);font-size:13px;color:var(--text-secondary);font-weight:700">PREDICTIVE CODING</span><h4 style="font-size:20px;color:var(--ink);font-weight:600" data-i18n="slides.s18d.box1.title">人脑预测编码机制</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.6" data-i18n="slides.s18d.box1.body">日常司空见惯的常识（先验概率高）无法激活深层认知；打破预期的反常识线索（先验概率低）能显著触发海马体记忆编码。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:26px 28px;border-radius:4px;display:flex;flex-direction:column;gap:10px"><span style="font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:700">SELF-INFORMATION (BITS)</span><h4 style="font-size:20px;color:var(--ink);font-weight:600" data-i18n="slides.s18d.box2.title">自信息量 (比特 bits)</h4><p style="font-size:16.5px;color:var(--text-primary);line-height:1.6" data-i18n="slides.s18d.box2.body">自信息量 I 以比特为量纲，精确度量了受众在消除不确定性时所获得的新知价值，为量化真实学习效果提供数学基石。</p></div></div></div></div>'
    },
    # 5. s18e: Case Calculation with clean SVG Botanical Signage Schematics
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · AOI INFORMATION WEIGHTS</div><div class="r">23 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18e.title">标牌各区域信息量权重与案例量化计算</h2><div class="analysis-kicker-desc" data-i18n="slides.s18e.guide">【数值演算】对比传统分类学常识与共创感官互动的自信息量数值差异</div></div><div class="analysis-anim-badge" aria-label="Calculation Animation"><span class="analysis-anim-label">CALCULATION</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="8" stroke="var(--border-subtle)" stroke-width="1.5" /><line x1="16" y1="15" x2="24" y2="15" stroke="var(--accent)" stroke-width="2" /><line x1="20" y1="11" x2="20" y2="19" stroke="var(--accent)" stroke-width="2" /><circle cx="96" cy="15" r="8" stroke="var(--accent)" stroke-width="1.5" /><line x1="92" y1="15" x2="100" y2="15" stroke="var(--accent)" stroke-width="2" /></svg></div></div><div class="analysis-body-group" style="height:520px;display:flex;flex-direction:column;justify-content:space-between"><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:24px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:22px 24px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:var(--mono);font-size:12px;color:var(--text-secondary);font-weight:700">CONVENTIONAL TAXONOMY</span><span style="font-size:24px;font-weight:700;color:var(--text-secondary)">0.415 <small style="font-size:13px">bits</small></span></div><svg width="100%" height="80" viewBox="0 0 400 80" fill="none" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid var(--border-subtle);border-radius:4px"><rect x="15" y="15" width="100" height="50" rx="3" fill="#cbd5e1" /><rect x="130" y="15" width="250" height="50" rx="3" fill="#fecaca" stroke="#dc2626" stroke-width="1" stroke-dasharray="3 3"/><text x="255" y="44" font-size="12" fill="#dc2626" font-weight="bold" text-anchor="middle">大段科普长文本 (P=0.75, I=0.415 bits)</text></svg><h4 style="font-size:19px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18e.box1.title">传统科普长文本（高预期 · 低信息量）</h4><p style="font-size:15.5px;color:var(--text-primary);line-height:1.5;margin:0" data-i18n="slides.s18e.box1.body">“九重葛为紫茉莉科木质藤本，原产于南美”</p><div style="font-size:14.5px;color:var(--text-secondary);background:#f9f9f9;padding:8px 12px;border-radius:4px">先验概率 P = 0.75 &rarr; 自信息量 I = -log₂(0.75) = <strong style="color:var(--ink)">0.415 bits</strong></div></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:3px solid var(--accent);padding:22px 24px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">SENSORY RELEVANCE (R)</span><span style="font-size:24px;font-weight:700;color:var(--accent)">3.059 <small style="font-size:13px">bits</small></span></div><svg width="100%" height="80" viewBox="0 0 400 80" fill="none" xmlns="http://www.w3.org/2000/svg" style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:4px"><rect x="15" y="12" width="70" height="26" rx="3" fill="#cbd5e1" /><rect x="95" y="12" width="180" height="26" rx="3" fill="#e2e8f0" /><rect x="285" y="12" width="100" height="26" rx="3" fill="#fed7aa" /><rect x="15" y="44" width="370" height="26" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/><text x="200" y="62" font-size="12" fill="#15803d" font-weight="bold" text-anchor="middle">身体感官触觉气泡 (P=0.12, I=3.059 bits - 提高 7.37 倍)</text></svg><h4 style="font-size:19px;color:var(--ink);font-weight:600;margin:0" data-i18n="slides.s18e.box2.title">身体感官互动气泡（低预期 · 极高信息量）</h4><p style="font-size:15.5px;color:var(--text-primary);line-height:1.5;margin:0" data-i18n="slides.s18e.box2.body">“红色的不是花瓣是苞片！请用手指触摸干爽纸质触感”</p><div style="font-size:14.5px;color:var(--accent);background:rgba(22,101,52,0.06);padding:8px 12px;border-radius:4px;font-weight:600">先验概率 P = 0.12 &rarr; 自信息量 I = -log₂(0.12) = <strong>3.059 bits</strong></div></div></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:14px 20px;border-radius:4px;font-size:15px;color:var(--text-primary)">拟人化对话：P = 0.15 &rarr; I = <strong>2.737 bits</strong> ｜ 花语提示：P = 0.25 &rarr; I = <strong>2.000 bits</strong> ｜ 传统分类学：P = 0.75 &rarr; I = <strong>0.415 bits</strong></div></div></div>'
    },
    # 6. s18f: E_gain Formula with Comprehensive Variable Definitions (Slide 24)
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · COGNITIVE GAIN MODEL</div><div class="r">24 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18f.title">信息加权认知吸收量（E_gain）计算模型</h2><div class="analysis-kicker-desc" data-i18n="slides.s18f.guide">【公式推导】将空间注视概率与区域信息量加权求和，度量真实知识吸收总量</div></div><div class="analysis-anim-badge" aria-label="Gain Animation"><span class="analysis-anim-label">E_GAIN</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 24 L 38 18 L 68 12 L 106 6" stroke="var(--accent)" stroke-width="2" fill="none" /><circle cx="106" cy="6" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group" style="height:520px;display:flex;flex-direction:column;justify-content:space-between"><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:20px 28px;border-radius:4px;display:flex;align-items:center;justify-content:space-between"><div style="font-family:var(--sans);font-size:42px;font-weight:200;color:var(--accent)">E_gain = ∑<sub style="font-size:18px">i=1</sub><sup style="font-size:18px">K</sup> [ p<sub style="font-size:18px">i</sub> × I(AOI<sub style="font-size:18px">i</sub>) ]</div><div style="font-size:18px;font-weight:600;color:var(--ink)" data-i18n="slides.s18f.meaning">期望认知吸收总量 = 各区域注视时间占比 × 语义自信息量</div></div><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:20px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:20px 22px;border-radius:4px;display:flex;flex-direction:column;gap:8px"><span style="font-family:var(--mono);font-size:12px;color:var(--text-secondary);font-weight:700">VARIABLE DEFINITIONS &amp; SYMBOLS</span><h4 style="font-size:18px;color:var(--ink);font-weight:600">公式中各符号变量详尽释义</h4><div style="font-size:15px;color:var(--text-primary);line-height:1.6;display:flex;flex-direction:column;gap:5px"><div>• <strong style="color:var(--accent)">E_gain</strong> (bits)：观众在整张标牌浏览中吸收的期望信息总量。</div><div>• <strong style="color:var(--accent)">K</strong>：标牌划分的独立语义功能区（AOI）总数。</div><div>• <strong style="color:var(--accent)">p_i</strong> = T_i / ∑T_j：观众在区域 i 的注视时间占比（满足 ∑ p_i = 1）。</div><div>• <strong style="color:var(--accent)">I(AOI_i)</strong> (bits)：区域 i 的惊讶度自信息量（I = -log₂ P_prior）。</div></div></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:20px 22px;border-radius:4px;display:flex;flex-direction:column;gap:8px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">PHYSICAL &amp; COGNITIVE INSIGHT</span><h4 style="font-size:18px;color:var(--ink);font-weight:600">数理模型的物理与认知含义</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.6;margin:0">如果观众把 20 秒全部浪费在低惊讶度说明文上（I=0.42），E_gain 仅为 <strong>0.585 bits</strong>；但若视线探索了高惊讶度感官气泡（I=3.06），即便停留时间更短，E_gain 也将暴增至 <strong>1.332 bits 以上（+127.7%）</strong>，真正度量了知识获取的质与量。</p></div></div></div></div>'
    },
    # 7. s18g: Markov Stagnation Drop
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
        "assets": [
            "entropy-markov-chart"
        ],
        "claims": [],
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · MARKOV TRANSITION</div><div class="r">25 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18g.title">马尔可夫转移矩阵：打破 93% 长文本死循环</h2><div class="analysis-kicker-desc" data-i18n="slides.s18g.guide">【动线解构】基于一阶马尔可夫链量化视线在各语义功能区之间的流转秩序</div></div><div class="analysis-anim-badge" aria-label="Markov Chain Animation"><span class="analysis-anim-label">MARKOV</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="7" stroke="var(--ink)" stroke-width="1.5" fill="none" /><circle cx="96" cy="15" r="7" stroke="var(--accent)" stroke-width="1.5" fill="none" /><path d="M 27 15 Q 58 5 89 15" stroke="var(--accent)" stroke-width="1.8" fill="none" /><path d="M 89 15 Q 58 25 27 15" stroke="var(--border-subtle)" stroke-width="1.5" stroke-dasharray="2 2" fill="none" /></svg></div></div><div class="analysis-body-group" style="height:520px;display:flex;flex-direction:column;justify-content:space-between"><div class="analysis-hero-grid"><div class="analysis-sub-stack"><div class="analysis-sub-card"><span class="lbl">CTRL SELF-LOOP</span><span class="nb" style="color:rgba(220,38,38,0.9)">0.93<span class="unit">P(Text|Text)</span></span></div><div class="analysis-sub-card"><span class="lbl">EXP SELF-LOOP</span><span class="nb" style="color:var(--accent)">0.56<span class="unit">P(Text|Text)</span></span></div><div class="analysis-sub-card"><span class="lbl">STAGNATION DROP</span><span class="nb">-39.8<span class="unit">%</span></span></div></div><div class="analysis-hero-card"><h3 class="analysis-hero-title" data-i18n="slides.s18g.kpi.title">长文本自循环停滞率</h3><div class="analysis-hero-num" style="color:var(--accent)">93% → 56%</div><div class="analysis-hero-sub" data-i18n="slides.s18g.kpi.sub">马尔可夫矩阵证实：长文本死循环被彻底打破，视线平稳转导至感官互动区 (p &lt; 0.001)</div></div></div><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:20px"><div style="background:#fff;border:1px solid rgba(220,38,38,0.25);padding:18px 22px;border-radius:4px;display:flex;flex-direction:column;gap:6px"><h4 style="font-size:19px;color:rgba(220,38,38,0.9);font-weight:600" data-i18n="slides.s18g.box1.title">对照组：死死困在长文本中 (0.93)</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.5" data-i18n="slides.s18g.box1.body">视线在文本区内反复自循环（93%），跳至图片的概率仅 4%，形成了封闭的阅读陷阱与严重停滞。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:18px 22px;border-radius:4px;display:flex;flex-direction:column;gap:6px"><h4 style="font-size:19px;color:var(--accent);font-weight:600" data-i18n="slides.s18g.box2.title">改良组：多模态自由流转 (多点开花)</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.5" data-i18n="slides.s18g.box2.body">视线自正文平稳流向感官气泡（0.19）、图标（0.13）与花语（0.38），构建了顺畅的认知导流网络。</p></div></div></div></div>'
    },
    # 8. s18h: Efficiency Ratio Formula with Full Variable Breakout (Slide 26)
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · EFFICIENCY RATIO</div><div class="r">26 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18h.title">认知信息传递能效比：单位视觉负荷的产出</h2><div class="analysis-kicker-desc" data-i18n="slides.s18h.guide">【能效建模】构建 η = E_gain / GTE 指标，量化单位视觉搜索努力换取的信息增益</div></div><div class="analysis-anim-badge" aria-label="Efficiency Animation"><span class="analysis-anim-label">EFFICIENCY</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="96" height="12" rx="6" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="12" y="12" width="70" height="8" rx="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group" style="height:520px;display:flex;flex-direction:column;justify-content:space-between"><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:20px 28px;border-radius:4px;display:flex;align-items:center;justify-content:space-between"><div style="font-family:var(--sans);font-size:42px;font-weight:200;color:var(--accent)">η = E_gain / ( H<sub style="font-size:18px">GTE</sub> + ε )</div><div style="font-size:18px;font-weight:600;color:var(--ink)" data-i18n="slides.s18h.meaning">认知能效比 = 有效知识吸收量 / 动线转移熵（视觉搜索努力）</div></div><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:20px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:20px 22px;border-radius:4px;display:flex;flex-direction:column;gap:8px"><span style="font-family:var(--mono);font-size:12px;color:var(--text-secondary);font-weight:700">VARIABLE DEFINITIONS &amp; SYMBOLS</span><h4 style="font-size:18px;color:var(--ink);font-weight:600">公式中各符号变量详尽释义</h4><div style="font-size:15px;color:var(--text-primary);line-height:1.6;display:flex;flex-direction:column;gap:5px"><div>• <strong style="color:var(--accent)">η</strong> (bits/bit)：认知信息传递能效比，衡量单位搜索努力下的产出率。</div><div>• <strong style="color:var(--accent)">E_gain</strong> (bits)：分子为有效知识吸收总量（有效收益）。</div><div>• <strong style="color:var(--accent)">H_GTE</strong> (bits)：分母为动线转移熵（视觉搜索路径随机度与认知负荷）。</div><div>• <strong style="color:var(--accent)">ε</strong> = 0.1：平滑常数，防止转移熵极低时的除零不稳定。</div></div></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:20px 22px;border-radius:4px;display:flex;flex-direction:column;gap:8px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">SIGNIFICANT GAIN</span><h4 style="font-size:18px;color:var(--accent);font-weight:600" data-i18n="slides.s18h.m2.title">实证显著提升 +29.9% (p=0.004)</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.6;margin:0">对照组 1.083 ± 0.439 &rarr; 改良组 1.407 ± 0.347（t = 3.540, d = 0.982）。证实共创标牌并非单向堆砌信息，而是以更少、更舒适的视觉搜索消耗换取了更高价值的知识吸收，实现了认知减负与增效。</p></div></div></div></div>'
    },
    # 9. s18i1: Dedicated Chart A - GTE
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · EMPIRICAL CHARTS · GAZE TRANSITION ENTROPY</div><div class="r">27 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18i1.title">动线转移熵 (GTE) 分析：探索路径与认知负荷</h2><div class="analysis-kicker-desc" data-i18n="slides.s18i1.guide">【图表A】量化视线转移随机度与跨语义功能区的自主探索活力</div></div><div class="analysis-anim-badge" aria-label="GTE Animation"><span class="analysis-anim-label">CHART A</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="5" fill="var(--text-secondary)"/><circle cx="96" cy="15" r="5" fill="var(--accent)"/><line x1="25" y1="15" x2="91" y2="15" stroke="var(--accent)" stroke-width="2"/></svg></div></div><div class="analysis-body-group" style="height:520px;display:grid;grid-template-columns:1.2fr 1fr;gap:24px;align-items:center"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;padding:12px;display:flex;justify-content:center;align-items:center;height:480px"><img src="asset:entropy-chart-gte" alt="GTE Chart" style="max-width:100%;max-height:100%;object-fit:contain"></div><div style="display:flex;flex-direction:column;gap:16px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:20px 22px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--text-secondary);font-weight:700">METRIC MEANING</span><h4 style="font-size:18px;color:var(--ink);font-weight:600;margin:4px 0 8px">动线转移熵 H_GTE (bits)</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.55;margin:0">衡量视线在各语义区之间转移的一阶条件熵。低值代表死死困在单一区域（对照组 0.495 bits），高值代表跨区域自由流转（改良组 0.900 bits）。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:20px 22px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">EMPIRICAL RESULT</span><h4 style="font-size:18px;color:var(--ink);font-weight:600;margin:4px 0 8px">显著提升 +82.0% (p &lt; 0.0001 ***)</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.55;margin:0">t(12) = 6.849, Cohen\'s d = 1.900。证实视线跳出了大段文字的吸附陷阱，实现了多模态区域间的活跃自主探索。</p></div></div></div></div>'
    },
    # 10. s18i2: Dedicated Chart B - E_gain
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · EMPIRICAL CHARTS · COGNITIVE GAIN</div><div class="r">28 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18i2.title">认知吸收量 (E_gain) 配对检验：全量 13 人无一下降</h2><div class="analysis-kicker-desc" data-i18n="slides.s18i2.guide">【图表B】13 位被试配对连线全部陡峭向上倾斜，有效知识获得量翻倍暴增</div></div><div class="analysis-anim-badge" aria-label="Egain Animation"><span class="analysis-anim-label">CHART B</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 24 L 38 18 L 68 12 L 106 6" stroke="var(--accent)" stroke-width="2" fill="none" /><circle cx="106" cy="6" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group" style="height:520px;display:grid;grid-template-columns:1.2fr 1fr;gap:24px;align-items:center"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;padding:12px;display:flex;justify-content:center;align-items:center;height:480px"><img src="asset:entropy-chart-egain" alt="Egain Chart" style="max-width:100%;max-height:100%;object-fit:contain"></div><div style="display:flex;flex-direction:column;gap:16px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:20px 22px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">100% CONSISTENT LEAP</span><h4 style="font-size:18px;color:var(--ink);font-weight:600;margin:4px 0 8px">全量 13 位被试单调显著递增</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.55;margin:0">图中 13 条绿色细连线全部呈现极强的陡峭上扬趋势，无论是在 Group A 还是 Group B，没有一位被试出现下降（增长率区间 +86.8% ~ +243.1%）。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:20px 22px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">DECISIVE EFFECT SIZE</span><h4 style="font-size:18px;color:var(--ink);font-weight:600;margin:4px 0 8px">0.585 &rarr; 1.332 bits (+127.7%)</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.55;margin:0">配对 t 检验 t(12) = 12.481, p &lt; 0.000001 ***, 效应量 Cohen\'s d = 3.462（远超常规大效应门槛 0.8），展现出决定性的改良效果。</p></div></div></div></div>'
    },
    # 11. s18i3: Dedicated Chart C - eta
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · EMPIRICAL CHARTS · EFFICIENCY RATIO</div><div class="r">29 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18i3.title">认知传递能效比 (η) 分析：单位视觉努力下的知识产出</h2><div class="analysis-kicker-desc" data-i18n="slides.s18i3.guide">【图表C】量化单位视线搜索转移负荷所能换取的有效信息增益</div></div><div class="analysis-anim-badge" aria-label="Eta Animation"><span class="analysis-anim-label">CHART C</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="96" height="12" rx="6" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="12" y="12" width="70" height="8" rx="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group" style="height:520px;display:grid;grid-template-columns:1.2fr 1fr;gap:24px;align-items:center"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;padding:12px;display:flex;justify-content:center;align-items:center;height:480px"><img src="asset:entropy-chart-eta" alt="Eta Chart" style="max-width:100%;max-height:100%;object-fit:contain"></div><div style="display:flex;flex-direction:column;gap:16px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:20px 22px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">EFFICIENCY METRIC</span><h4 style="font-size:18px;color:var(--ink);font-weight:600;margin:4px 0 8px">能效比 η = E_gain / (GTE + 0.1)</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.55;margin:0">将知识获得作为分子、搜索疲劳作为分母。橙色配对连线普遍上扬，证明观众以更高的“信息性价比”进行阅读。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:20px 22px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">EMPIRICAL RESULT</span><h4 style="font-size:18px;color:var(--ink);font-weight:600;margin:4px 0 8px">1.083 &rarr; 1.407 (+29.9%, p=0.004)</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.55;margin:0">t(12) = 3.540, Cohen\'s d = 0.982。证实共创排版实现了认知减负与增效的完美结合。</p></div></div></div></div>'
    },
    # 12. s18i4: Dedicated Chart D - SGE & KL
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · EMPIRICAL CHARTS · SPATIAL GAZE STRUCTURE</div><div class="r">30 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18i4.title">空间注视均衡度 (SGE) 与设计对齐 (KL 散度)</h2><div class="analysis-kicker-desc" data-i18n="slides.s18i4.guide">【图表D】量化视线空间离散度与共创设计预期的拟合收敛程度</div></div><div class="analysis-anim-badge" aria-label="SGE Animation"><span class="analysis-anim-label">CHART D</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="20" height="15" fill="#64748b"/><rect x="40" y="6" width="20" height="19" fill="#059669"/></svg></div></div><div class="analysis-body-group" style="height:520px;display:grid;grid-template-columns:1.2fr 1fr;gap:24px;align-items:center"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;padding:12px;display:flex;justify-content:center;align-items:center;height:480px"><img src="asset:entropy-chart-sge" alt="SGE Chart" style="max-width:100%;max-height:100%;object-fit:contain"></div><div style="display:flex;flex-direction:column;gap:16px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:20px 22px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">SPATIAL GAZE ENTROPY</span><h4 style="font-size:18px;color:var(--ink);font-weight:600;margin:4px 0 8px">空间注视均衡度 SGE: +66.9%</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.55;margin:0">1.203 &rarr; 2.008 bits (t=7.636, p&lt;0.0001)。证明视线不再单极化聚集在文本区，而是均匀覆盖了插图、花语和互动气泡。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid var(--accent);padding:20px 22px;border-radius:4px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">DESIGN CONVERGENCE</span><h4 style="font-size:18px;color:var(--ink);font-weight:600;margin:4px 0 8px">KL 散度与设计预期对齐</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.55;margin:0">D_KL 量化了实际视线分布与工坊设计意图的匹配度，证实共创原则成功达成了预期的人机交互导流目标。</p></div></div></div></div>'
    },
    # 13. s18j: Empirical Summary & Statistical Inference
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · EMPIRICAL SUMMARY</div><div class="r">31 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18j.title">全量实证结果：有效认知信息吸收量翻倍暴增</h2><div class="analysis-kicker-desc" data-i18n="slides.s18j.guide">【全量验证】13 位被试配对检验证实有效认知吸收量与能效比实现全面跃升</div></div><div class="analysis-anim-badge" aria-label="Evidence Animation"><span class="analysis-anim-label">EVIDENCE</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><line x1="6" y1="25" x2="110" y2="25" stroke="var(--border-subtle)" stroke-width="1.5" /><path d="M 10 25 C 28 25, 42 6, 58 6 C 74 6, 88 25, 106 25" stroke="var(--ink)" stroke-width="1.5" fill="none" /><line x1="84" y1="11" x2="84" y2="25" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="2 2" /><g class="anim-stat-star"><circle cx="94" cy="17" r="3.5" fill="var(--accent)" /><circle cx="94" cy="17" r="7" stroke="var(--accent)" stroke-width="1" opacity="0.4" /></g></svg></div></div><div class="analysis-body-group"><div class="analysis-hero-grid"><div class="analysis-sub-stack"><div class="analysis-sub-card"><span class="lbl">PAIRED T-TEST</span><span class="nb">t(12) = 12.48<span class="unit">***</span></span></div><div class="analysis-sub-card"><span class="lbl">EFFECT SIZE</span><span class="nb">d = 3.46<span class="unit">Huge</span></span></div><div class="analysis-sub-card"><span class="lbl">EFFICIENCY (η)</span><span class="nb">+29.9<span class="unit">% (p=0.004)</span></span></div></div><div class="analysis-hero-card"><h3 class="analysis-hero-title" data-i18n="slides.s18j.kpi.title">有效认知信息吸收总量 (E_gain)</h3><div class="analysis-hero-num">+127.7<span class="unit">%</span></div><div class="analysis-hero-sub" data-i18n="slides.s18j.kpi.sub">0.585 bits → 1.332 bits (p &lt; 0.000001 ***) | 全量 13 位被试全部单调显著上升</div></div></div><div class="analysis-visual-row" style="grid-template-columns:1fr 1fr;gap:20px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:18px 22px;border-radius:4px;display:flex;flex-direction:column;gap:6px"><div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">KNOWLEDGE ABSORPTION GAIN</span><span style="font-size:18px;font-weight:700;color:var(--accent)">+127.7%</span></div><h4 style="font-size:20px;color:var(--ink);font-weight:600" data-i18n="slides.s18j.box1.title">真实认知获取成倍跃升</h4><p style="font-size:15.5px;color:var(--text-primary);line-height:1.45" data-i18n="slides.s18j.box1.body">将注视时间与信息惊讶度结合后，实验组有效知识获得量翻倍，13 位被试无一下降（+86.8% ~ +243.1%）。</p></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:18px 22px;border-radius:4px;display:flex;flex-direction:column;gap:6px"><div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">PROCESSING EFFICIENCY (η)</span><span style="font-size:18px;font-weight:700;color:var(--accent)">+29.9%</span></div><h4 style="font-size:20px;color:var(--ink);font-weight:600" data-i18n="slides.s18j.box2.title">认知信息传递能效比显著提升</h4><p style="font-size:15.5px;color:var(--text-primary);line-height:1.45" data-i18n="slides.s18j.box2.body">能效比从 1.083 提升至 1.407（p = 0.004, d = 0.982），证明观众以更少、更舒适的视觉搜索换取了更高价值的信息。</p></div></div></div><div class="analysis-ledger-v2"><div class="analysis-ledger-row"><div class="analysis-ledger-left"><span class="analysis-ledger-tag">EVIDENCE</span><strong class="analysis-ledger-title" data-i18n="slides.s18j.finding1.title" data-hybrid-ja="never">信息论对共创原则的坚实支撑</strong></div><p class="analysis-ledger-detail" data-i18n="slides.s18j.finding1.body" data-hybrid-ja="never">以香农信息论底层数学模型严谨证实了共创标牌（A/R/S原则）在降低认知负荷的同时实现了知识获得最大化。</p></div><div class="analysis-ledger-row"><div class="analysis-ledger-left"><span class="analysis-ledger-tag">DOCTORAL</span><strong class="analysis-ledger-title" data-i18n="slides.s18j.finding2.title" data-hybrid-ja="never">博士阶段研究的理论支点</strong></div><p class="analysis-ledger-detail" data-i18n="slides.s18j.finding2.body" data-hybrid-ja="never">高惊讶度与顺畅马尔可夫流为后续结合双重编码理论与长期记忆保持（Retention）实验奠定了量化计算基础。</p></div></div></div>'
    },
    # 14. s18k: 13-Participant Data Table
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · PARTICIPANTS DATA LEDGER</div><div class="r">32 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18k.title">全量 13 位被试逐人明细数据表 (Group A &amp; B)</h2><div class="analysis-kicker-desc" data-i18n="slides.s18k.guide">【逐人明细】记录 Group A (7人) 与 Group B (6人) 每位被试的对照与改良数据及增益率</div></div><div class="analysis-anim-badge" aria-label="Ledger Animation"><span class="analysis-anim-label">LEDGER</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><line x1="10" y1="8" x2="106" y2="8" stroke="var(--border-subtle)" stroke-width="1.5" /><line x1="10" y1="15" x2="106" y2="15" stroke="var(--border-subtle)" stroke-width="1.5" /><line x1="10" y1="22" x2="106" y2="22" stroke="var(--border-subtle)" stroke-width="1.5" /></svg></div></div><div class="analysis-body-group" style="height:520px;display:flex;flex-direction:column;justify-content:center"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;padding:24px 32px;display:grid;grid-template-columns:1fr 1fr;gap:36px;font-size:15px"><div style="display:flex;flex-direction:column;gap:9px"><div style="font-weight:700;color:var(--accent);border-bottom:1.5px solid var(--border-subtle);padding-bottom:8px;margin-bottom:4px;display:flex;justify-content:space-between"><span>GROUP A · 九重葛 (N=7)</span><span style="font-size:13px;color:var(--text-secondary);font-weight:400">Ctrl → Exp (ΔE_gain)</span></div><div style="display:flex;justify-content:space-between"><span>akama_kumiko:</span><span>0.403 &rarr; 1.246 <strong style="color:var(--accent);margin-left:6px">+208.9%</strong></span></div><div style="display:flex;justify-content:space-between"><span>ataqi:</span><span>0.487 &rarr; 1.326 <strong style="color:var(--accent);margin-left:6px">+172.4%</strong></span></div><div style="display:flex;justify-content:space-between"><span>harada_keiko:</span><span>0.589 &rarr; 1.385 <strong style="color:var(--accent);margin-left:6px">+135.2%</strong></span></div><div style="display:flex;justify-content:space-between"><span>koga_eiichi:</span><span>0.366 &rarr; 0.974 <strong style="color:var(--accent);margin-left:6px">+166.0%</strong></span></div><div style="display:flex;justify-content:space-between"><span>moro_izumi:</span><span>0.699 &rarr; 1.429 <strong style="color:var(--accent);margin-left:6px">+104.4%</strong></span></div><div style="display:flex;justify-content:space-between"><span>saku_yoshisuke:</span><span>0.702 &rarr; 1.408 <strong style="color:var(--accent);margin-left:6px">+100.6%</strong></span></div><div style="display:flex;justify-content:space-between"><span>yamada_rena:</span><span>0.828 &rarr; 1.547 <strong style="color:var(--accent);margin-left:6px">+86.8%</strong></span></div></div><div style="display:flex;flex-direction:column;gap:9px"><div style="font-weight:700;color:var(--accent);border-bottom:1.5px solid var(--border-subtle);padding-bottom:8px;margin-bottom:4px;display:flex;justify-content:space-between"><span>GROUP B · 千日小坊 (N=6)</span><span style="font-size:13px;color:var(--text-secondary);font-weight:400">Ctrl → Exp (ΔE_gain)</span></div><div style="display:flex;justify-content:space-between"><span>abcde:</span><span>0.603 &rarr; 1.295 <strong style="color:var(--accent);margin-left:6px">+114.7%</strong></span></div><div style="display:flex;justify-content:space-between"><span>kimura:</span><span>0.562 &rarr; 1.300 <strong style="color:var(--accent);margin-left:6px">+131.3%</strong></span></div><div style="display:flex;justify-content:space-between"><span>nonntixyan:</span><span>0.607 &rarr; 1.411 <strong style="color:var(--accent);margin-left:6px">+132.5%</strong></span></div><div style="display:flex;justify-content:space-between"><span>p186:</span><span>0.567 &rarr; 1.111 <strong style="color:var(--accent);margin-left:6px">+95.9%</strong></span></div><div style="display:flex;justify-content:space-between"><span>rep_chen:</span><span>0.793 &rarr; 1.513 <strong style="color:var(--accent);margin-left:6px">+90.7%</strong></span></div><div style="display:flex;justify-content:space-between"><span>umetu_ayane:</span><span>0.399 &rarr; 1.370 <strong style="color:var(--accent);margin-left:6px">+243.1%</strong></span></div></div></div></div></div>'
    },
    # 15. s18l: 3-Step Defense & Reporting Guide
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
        "markup": '<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · DEFENSE &amp; REPORTING GUIDE</div><div class="r">33 / 36</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18l.title">答辩与学术汇报“三步法话术指南”</h2><div class="analysis-kicker-desc" data-i18n="slides.s18l.guide">【汇报策略】向导师与答辩评审阐述本信息论创新方法的专业逻辑路径</div></div><div class="analysis-anim-badge" aria-label="Defense Animation"><span class="analysis-anim-label">DEFENSE</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="7" stroke="var(--ink)" stroke-width="1.5" fill="none" /><text x="20" y="18" font-size="9" font-weight="700" text-anchor="middle" fill="var(--ink)">1</text><circle cx="58" cy="15" r="7" stroke="var(--ink)" stroke-width="1.5" fill="none" /><text x="58" y="18" font-size="9" font-weight="700" text-anchor="middle" fill="var(--ink)">2</text><circle cx="96" cy="15" r="7" stroke="var(--accent)" stroke-width="1.5" fill="none" /><text x="96" y="18" font-size="9" font-weight="700" text-anchor="middle" fill="var(--accent)">3</text></svg></div></div><div class="analysis-body-group" style="height:520px;display:flex;flex-direction:column;justify-content:center"><div class="analysis-visual-row" style="grid-template-columns:repeat(3, 1fr);gap:20px"><div style="background:#fff;border:1px solid var(--border-subtle);padding:26px 22px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">STEP 1 · 指出传统缺陷</span><h4 style="font-size:22px;color:var(--ink);font-weight:600" data-i18n="slides.s18l.s1.title">破除时长假象</h4><p style="font-size:16px;color:var(--text-primary);line-height:1.6" data-i18n="slides.s18l.s1.body">“传统分析只看时长，但对照组长文本的高停留实为认知受阻；马尔可夫矩阵证实其自循环停滞率高达 93%。”</p></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:26px 22px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">STEP 2 · 阐述信息论创新</span><h4 style="font-size:22px;color:var(--ink);font-weight:600" data-i18n="slides.s18l.s2.title">引入惊讶度加权</h4><p style="font-size:16px;color:var(--text-primary);line-height:1.6" data-i18n="slides.s18l.s2.body">“引入香农信息论，根据‘信息违背预期时信息量最大’原则构建 E_gain 与能效比 η，精准度量真实知识获得。”</p></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:26px 22px;border-radius:4px;display:flex;flex-direction:column;gap:12px"><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">STEP 3 · 亮出硬核实证</span><h4 style="font-size:22px;color:var(--ink);font-weight:600" data-i18n="slides.s18l.s3.title">证实有效吸收翻倍</h4><p style="font-size:16px;color:var(--text-primary);line-height:1.6" data-i18n="slides.s18l.s3.body">“全量 13 人配对检验证实 E_gain 提升 127.7%（p&lt;0.000001, d=3.46），13人全上升，科学证实共创卓越价值。”</p></div></div></div></div>'
    }
]

for s in deep_slides:
    fpath = os.path.join(SLIDES_DIR, f"{s['id']}.json")
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(s, f, ensure_ascii=False, indent=2)

print(f"[*] 已成功重新生成 {len(deep_slides)} 张深度分析幻灯片 JSON 文件！")

# 2. Update deck-manifest.json
with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# Register new chart assets
existing_asset_ids = {a['id'] for a in manifest.get('assets', [])}
new_assets = [
    {"id": "entropy-chart-gte", "path": "src/assets/images/entropy-chart-gte.png", "access": "public"},
    {"id": "entropy-chart-egain", "path": "src/assets/images/entropy-chart-egain.png", "access": "public"},
    {"id": "entropy-chart-eta", "path": "src/assets/images/entropy-chart-eta.png", "access": "public"},
    {"id": "entropy-chart-sge", "path": "src/assets/images/entropy-chart-sge.png", "access": "public"},
    {"id": "entropy-markov-chart", "path": "src/assets/images/entropy-markov-chart.png", "access": "public"}
]
for a in new_assets:
    if a['id'] not in existing_asset_ids:
        manifest['assets'].append(a)

manifest_deep_slides = []
for s in deep_slides:
    manifest_deep_slides.append({
        "id": s["id"],
        "chapterId": "deep-analysis",
        "layout": "data",
        "content": f"src/content/slides/{s['id']}.json",
        "assets": s.get("assets", []),
        "claims": []
    })

# Reconstruct slide manifest
new_manifest_slides = []
for s in manifest['slides']:
    if s['id'] == 's17e-statistical-synthesis':
        new_manifest_slides.append(s)
        new_manifest_slides.extend(manifest_deep_slides)
    elif s['id'].startswith('s18'):
        continue  # skip any old s18 slides
    else:
        new_manifest_slides.append(s)

manifest['slides'] = new_manifest_slides

with open(MANIFEST_FILE, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"[*] deck-manifest.json 注册完毕，总幻灯片数: {len(manifest['slides'])}")
