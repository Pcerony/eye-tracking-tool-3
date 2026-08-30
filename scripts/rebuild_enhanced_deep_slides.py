import json
import os

slides_data = {}

# ------------------------------------------------------------------------------
# Slide 20: s18a-entropy-intro
# ------------------------------------------------------------------------------
slides_data["s18a-entropy-intro"] = {
    "id": "s18a-entropy-intro",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：信息熵理论引入",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": ["entropy-fig-01-paradigm"],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · SECTION INTRO</div><div class="r">20 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18a.title">基于信息熵与惊讶度理论的深度分析</h2><div class="analysis-kicker-desc" data-i18n="slides.s18a.guide">【理论引入】超越“注视时长”表面假象，量化真实知识吸收与阅读认知流</div></div><div class="analysis-anim-badge" aria-label="Entropy Wave Animation"><span class="analysis-anim-label">THEORY</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 6 15 Q 32 4 58 15 T 110 15" stroke="var(--border-subtle)" stroke-width="1.5" fill="none" /><path d="M 6 15 Q 32 26 58 15 T 110 15" stroke="var(--accent)" stroke-width="2" fill="none" /><circle cx="58" cy="15" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;overflow:hidden;display:flex;justify-content:center;align-items:center;padding:10px"><img src="asset:entropy-fig-01-paradigm" alt="Cognitive Paradigm Shift on Real Botanical Signage" style="width:100%;max-height:460px;object-fit:contain;border-radius:4px" /></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:16px 24px;border-radius:4px;display:flex;align-items:center;justify-content:space-between"><div style="font-size:16px;color:var(--ink);line-height:1.5" data-i18n="slides.s18a.summary"><strong>核心范式演进：</strong>从“表面物理停留时长”升级为“单位视觉负荷下的有效新知吸收量与流转秩序”。</div><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">PARADIGM SHIFT</span></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 21: s18b-conventional-metrics
# ------------------------------------------------------------------------------
slides_data["s18b-conventional-metrics"] = {
    "id": "s18b-conventional-metrics",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：常规指标局限",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": ["entropy-fig-02-metrics-flaw"],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · CONVENTIONAL METRICS</div><div class="r">21 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18b.title">传统眼动三大常规指标及其均质化假定缺陷</h2><div class="analysis-kicker-desc" data-i18n="slides.s18b.guide">【基线解构】剖析传统时长、落点与热力图如何将“读不下去的卡顿”误判为“深度阅读”</div></div><div class="analysis-anim-badge" aria-label="Baseline Animation"><span class="analysis-anim-label">BASELINE</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="8" width="24" height="14" rx="2" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="46" y="8" width="24" height="14" rx="2" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="82" y="8" width="24" height="14" rx="2" stroke="var(--border-subtle)" stroke-width="1.5" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;overflow:hidden;display:flex;justify-content:center;align-items:center;padding:10px"><img src="asset:entropy-fig-02-metrics-flaw" alt="Flaws in Conventional Eye Tracking Metrics" style="width:100%;max-height:460px;object-fit:contain;border-radius:4px" /></div><div style="background:#fff;border:1px solid var(--border-subtle);border-left:4px solid rgba(220,38,38,0.85);padding:14px 22px;border-radius:4px"><p style="font-size:15.5px;color:var(--ink);line-height:1.5;margin:0" data-i18n="slides.s18b.criticalFlaw">三大常规指标默认“每秒注视具有均等知识加工价值”，仅记录物理停留坐标，无法辨识注视背后的认知理解质量与晦涩文字带来的无序停滞。</p></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 22: s18c-cognitive-friction
# ------------------------------------------------------------------------------
slides_data["s18c-cognitive-friction"] = {
    "id": "s18c-cognitive-friction",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：认知受阻误区",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": ["entropy-fig-03-friction"],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · COGNITIVE FRICTION</div><div class="r">22 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18c.title">认知受阻与信息熵：量化视线分布的无序与摩擦</h2><div class="analysis-kicker-desc" data-i18n="slides.s18c.guide">【数学建模】引入视线状态熵 H(X) = -∑ P(x) log2 P(x)，揭示长文本造成的虚假高停留</div></div><div class="analysis-anim-badge" aria-label="Friction Animation"><span class="analysis-anim-label">CONFOUNDING</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><line x1="10" y1="15" x2="106" y2="15" stroke="rgba(220,38,38,0.8)" stroke-width="2" stroke-dasharray="4 2" /><circle cx="58" cy="15" r="5" fill="rgba(220,38,38,0.9)" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;overflow:hidden;display:flex;justify-content:center;align-items:center;padding:10px"><img src="asset:entropy-fig-03-friction" alt="Cognitive Friction and Entropy Breakdown" style="width:100%;max-height:460px;object-fit:contain;border-radius:4px" /></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:14px 22px;border-radius:4px"><p style="font-size:15.5px;color:var(--ink);line-height:1.5;margin:0" data-i18n="slides.s18c.rethink">诊断结论：高停留时长反映的是信息解码受阻（Cognitive Friction）而非有效知识吸收，必须引入度量信息意外度与流转秩序的信息论工具。</p></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 23: s18d-surprisal-theory
# ------------------------------------------------------------------------------
slides_data["s18d-surprisal-theory"] = {
    "id": "s18d-surprisal-theory",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：香农惊讶度建模",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": ["entropy-fig-04-surprisal"],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · SURPRISAL THEORY</div><div class="r">23 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18d.title">香农信息论与惊讶度：违背预期的认知增益</h2><div class="analysis-kicker-desc" data-i18n="slides.s18d.guide">【数理公式】基于真实九重葛标牌文本，逐个演示自信息量 I = -log2(P) 的变量释义与计算</div></div><div class="analysis-anim-badge" aria-label="Surprisal Animation"><span class="analysis-anim-label">SURPRISAL</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 25 C 28 25, 42 6, 58 6 C 74 6, 88 25, 106 25" stroke="var(--ink)" stroke-width="1.5" fill="none" /><line x1="58" y1="6" x2="58" y2="25" stroke="var(--accent)" stroke-width="2" stroke-dasharray="2 2" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;overflow:hidden;display:flex;justify-content:center;align-items:center;padding:10px"><img src="asset:entropy-fig-04-surprisal" alt="Surprisal Theory Demonstrated on Real Bougainvillea Signage" style="width:100%;max-height:460px;object-fit:contain;border-radius:4px" /></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:14px 22px;border-radius:4px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:15.5px;color:var(--ink);line-height:1.5" data-i18n="slides.s18d.axiom">“信息在违背预期时，其承载的信息量最大” —— 解释了为何 3 秒感官触觉互动能够大幅激发深度记忆。</div><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">SHANNON AXIOM</span></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 24: s18e-case-information-weight
# ------------------------------------------------------------------------------
slides_data["s18e-case-information-weight"] = {
    "id": "s18e-case-information-weight",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：案例信息量量化",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": ["entropy-fig-05-aoi-weights"],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · AOI INFORMATION WEIGHTS</div><div class="r">24 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18e.title">真实标牌各区域信息量权重与案例量化计算</h2><div class="analysis-kicker-desc" data-i18n="slides.s18e.guide">【实证剖析】从真实九重葛标牌截选四大功能区切片，对比自信息量数值差异</div></div><div class="analysis-anim-badge" aria-label="Calculation Animation"><span class="analysis-anim-label">CALCULATION</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="8" stroke="var(--border-subtle)" stroke-width="1.5" /><line x1="16" y1="15" x2="24" y2="15" stroke="var(--accent)" stroke-width="2" /><line x1="20" y1="11" x2="20" y2="19" stroke="var(--accent)" stroke-width="2" /><circle cx="96" cy="15" r="8" stroke="var(--accent)" stroke-width="1.5" /><line x1="92" y1="15" x2="100" y2="15" stroke="var(--accent)" stroke-width="2" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;overflow:hidden;display:flex;justify-content:center;align-items:center;padding:10px"><img src="asset:entropy-fig-05-aoi-weights" alt="Real Signage AOI Information Weights" style="width:100%;max-height:460px;object-fit:contain;border-radius:4px" /></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:14px 22px;border-radius:4px;font-size:15.5px;color:var(--text-primary);display:flex;justify-content:space-around"><span data-i18n="slides.s18e.ticker1">触觉互动 (R)：P = 0.12 → I = 3.059 bits (7.37x)</span><span data-i18n="slides.s18e.ticker2">拟人化对话：P = 0.15 → I = 2.737 bits</span><span data-i18n="slides.s18e.ticker3">花语提示：P = 0.25 → I = 2.000 bits</span><span data-i18n="slides.s18e.ticker4">传统分类学：P = 0.75 → I = 0.415 bits</span></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 25: s18f-cognitive-gain-formula
# ------------------------------------------------------------------------------
slides_data["s18f-cognitive-gain-formula"] = {
    "id": "s18f-cognitive-gain-formula",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：E_gain计算模型",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": ["entropy-fig-06-egain-walkthrough"],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · COGNITIVE GAIN MODEL</div><div class="r">25 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18f.title">信息加权认知吸收量（E_gain）计算模型</h2><div class="analysis-kicker-desc" data-i18n="slides.s18f.guide">【公式推导】在九重葛真实标牌上演示 E_gain = ∑ [ p_i × I(AOI_i) ] 逐区域演算全过程</div></div><div class="analysis-anim-badge" aria-label="Gain Animation"><span class="analysis-anim-label">E_GAIN</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 24 L 38 18 L 68 12 L 106 6" stroke="var(--accent)" stroke-width="2" fill="none" /><circle cx="106" cy="6" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;overflow:hidden;display:flex;justify-content:center;align-items:center;padding:10px"><img src="asset:entropy-fig-06-egain-walkthrough" alt="E_gain Mathematical Walkthrough on Real Signage" style="width:100%;max-height:460px;object-fit:contain;border-radius:4px" /></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:14px 22px;border-radius:4px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:15.5px;color:var(--ink);line-height:1.5" data-i18n="slides.s18f.meaning">期望认知吸收总量 = 各功能区注视时间权重 (p_i) × 区域自信息量 (I_i)，实现质与量的统一度量。</div><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">+127.7% COGNITIVE GAIN</span></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 26: s18g-markov-stagnation
# ------------------------------------------------------------------------------
slides_data["s18g-markov-stagnation"] = {
    "id": "s18g-markov-stagnation",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：马尔可夫死循环",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": ["entropy-fig-07-markov-flow"],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · MARKOV TRANSITION</div><div class="r">26 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18g.title">马尔可夫转移矩阵：打破 93% 长文本死循环</h2><div class="analysis-kicker-desc" data-i18n="slides.s18g.guide">【动线解构】在真实标牌上标注一阶转移概率，量化视线自长文本向感官气泡的良性分流</div></div><div class="analysis-anim-badge" aria-label="Markov Chain Animation"><span class="analysis-anim-label">MARKOV</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="15" r="7" stroke="var(--ink)" stroke-width="1.5" fill="none" /><circle cx="96" cy="15" r="7" stroke="var(--accent)" stroke-width="1.5" fill="none" /><path d="M 27 15 Q 58 5 89 15" stroke="var(--accent)" stroke-width="1.8" fill="none" /><path d="M 89 15 Q 58 25 27 15" stroke="var(--border-subtle)" stroke-width="1.5" stroke-dasharray="2 2" fill="none" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;overflow:hidden;display:flex;justify-content:center;align-items:center;padding:10px"><img src="asset:entropy-fig-07-markov-flow" alt="Markov Chain Transitions on Real Signage" style="width:100%;max-height:460px;object-fit:contain;border-radius:4px" /></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:14px 22px;border-radius:4px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:15.5px;color:var(--ink);line-height:1.5" data-i18n="slides.s18g.kpi.sub">马尔可夫矩阵证实：长文本自循环死锁从 93% 大幅降至 56%（-39.8%, p &lt; 0.001），构建起顺畅的图文认知流。</div><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">93% → 56% DROP</span></div></div></div>"""
}

# ------------------------------------------------------------------------------
# Slide 27: s18h-efficiency-ratio
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
    "assets": ["entropy-fig-08-eta-efficiency"],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS · EFFICIENCY RATIO</div><div class="r">27 / 37</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18h.title">认知信息传递能效比：单位视觉负荷的产出</h2><div class="analysis-kicker-desc" data-i18n="slides.s18h.guide">【能效建模】构建 η = E_gain / (H_GTE + ε) 指标，量化单位视觉搜索努力换取的信息增益</div></div><div class="analysis-anim-badge" aria-label="Efficiency Animation"><span class="analysis-anim-label">EFFICIENCY</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="96" height="12" rx="6" stroke="var(--border-subtle)" stroke-width="1.5" /><rect x="12" y="12" width="70" height="8" rx="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div style="background:#fff;border:1px solid var(--border-subtle);border-radius:4px;overflow:hidden;display:flex;justify-content:center;align-items:center;padding:10px"><img src="asset:entropy-fig-08-eta-efficiency" alt="Cognitive Information Efficiency Ratio" style="width:100%;max-height:460px;object-fit:contain;border-radius:4px" /></div><div style="background:#fff;border:1px solid var(--border-subtle);padding:14px 22px;border-radius:4px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:15.5px;color:var(--ink);line-height:1.5" data-i18n="slides.s18h.gainBody">实证证实：能效比自 1.083 跃升至 1.407（+29.9%, p=0.004），用更少视觉消耗换取了更高价值知识吸收。</div><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">η +29.9% BOOST</span></div></div></div>"""
}

# Write slide JSON files
for sid, data in slides_data.items():
    file_path = f"src/content/slides/{sid}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Written: {file_path}")

print("All slide JSON files updated with asset: prefix successfully!")
