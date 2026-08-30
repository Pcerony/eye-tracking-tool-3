# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I18N_DIR = os.path.join(BASE_DIR, 'src', 'i18n')

zh_dict = {
    "chapters.methods": "研究方法",
    "chapters.basicAnalysis": "基础分析",
    "chapters.deepAnalysis": "深度分析",

    "slides.s18a.shortTitle": "阶段五：信息熵理论引入",
    "slides.s18a.title": "基于信息熵与惊讶度理论的深度分析",
    "slides.s18a.guide": "【理论引入】超越“注视时长”表面假象，量化真实知识吸收与阅读认知流",
    "slides.s18a.q1.title": "看得久就是好吗？",
    "slides.s18a.q1.body": "传统眼动指标假定“注视越久 = 越感兴趣”。但在植物标牌中，生僻文字导致的卡顿与犹豫常被误判为深度沉浸。",
    "slides.s18a.q2.title": "信息论度量真实获得",
    "slides.s18a.q2.body": "引入香农信息熵与惊讶度（Surprisal），结合“信息违背预期时信息量最大”的原理，精确量化观众吸收的有效知识增量。",
    "slides.s18a.finding1.title": "认知范式升级",
    "slides.s18a.finding1.body": "从“表面注视时长”转向“单位视觉负荷下的有效信息吸收量与动线秩序”。",
    "slides.s18a.finding2.title": "循序渐进分析链条",
    "slides.s18a.finding2.body": "分步拆解：常规指标局限 → 文本停滞误区 → 惊讶度建模 → 案例计算 → 马尔可夫死循环 → 4维实证图解与全量检验。",

    "slides.s18b.shortTitle": "阶段五：常规指标局限",
    "slides.s18b.title": "传统眼动三大常规指标及其假设",
    "slides.s18b.guide": "【基线梳理】归纳现有植物标牌研究普遍依赖的三大常规眼动度量体系",
    "slides.s18b.m1.title": "注视时长 (Dwell Time)",
    "slides.s18b.m1.body": "记录视线在某区域停留的总秒数或时间百分比，底层假设“停越久 = 越感兴趣”。",
    "slides.s18b.m2.title": "注视次数 (Fixation Count)",
    "slides.s18b.m2.body": "记录视线落入该区域的落点频次，底层假设“落点越多 = 越具视觉重要性”。",
    "slides.s18b.m3.title": "注视热力图 (Heatmap)",
    "slides.s18b.m3.body": "高斯核密度渲染的空间点云，底层假设“红色高亮区代表绝对吸引力焦点”。",
    "slides.s18b.critical_flaw": "三大指标默认“每秒注视具有均等的信息加工价值”，仅记录物理停留坐标，无法辨识注视背后的认知理解质量与晦涩文字带来的无序停滞。",

    "slides.s18c.shortTitle": "阶段五：认知受阻误区",
    "slides.s18c.title": "常规指标的致命误区：认知受阻而非深度阅读",
    "slides.s18c.guide": "【误区揭示】剖析传统大段科普文字如何造成高注视时长的“虚假繁荣”",
    "slides.s18c.c1.title": "表面数据假象：长文本注视占比 44.3%",
    "slides.s18c.c1.body": "在对照组中，说明文字区注视时长位居首位。传统眼动模型据此推论“观众对大段科普内容最感兴趣”。",
    "slides.s18c.c2.title": "真实认知困境：认知摩擦与阅读停滞",
    "slides.s18c.c2.body": "大段生僻拉丁学名与形态学术语导致“读不下去、找不到重点”，视线在文本内被动打转卡顿，实为负荷过载而非深度阅读。",
    "slides.s18c.rethink": "诊断结论：高停留时长反映的是信息解码受阻（Cognitive Friction）而非有效知识吸收，必须引入度量信息意外度与流转秩序的信息论工具。",

    "slides.s18d.shortTitle": "阶段五：香农惊讶度建模",
    "slides.s18d.title": "香农信息论与惊讶度：违背预期的认知增益",
    "slides.s18d.guide": "【数理建模】引入自信息量 I = -log2(P)，量化反常识感官互动的高知识价值",
    "slides.s18d.axiom": "“信息在违背预期时，其承载的信息量最大”",
    "slides.s18d.box1.title": "人脑预测编码机制",
    "slides.s18d.box1.body": "日常司空见惯的常识（先验概率高）无法激活深层认知；打破预期的反常识线索（先验概率低）能显著触发海马体记忆编码。",
    "slides.s18d.box2.title": "自信息量 (比特 bits)",
    "slides.s18d.box2.body": "自信息量 I 以比特为量纲，精确度量了受众在消除不确定性时所获得的新知价值，为量化真实学习效果提供数学基石。",

    "slides.s18e.shortTitle": "阶段五：案例信息量量化",
    "slides.s18e.title": "标牌各区域信息量权重与案例量化计算",
    "slides.s18e.guide": "【数值演算】对比传统分类学常识与共创感官互动的自信息量数值差异",
    "slides.s18e.box1.title": "传统科普长文本（高预期 · 低信息量）",
    "slides.s18e.box1.body": "“九重葛为紫茉莉科木质藤本，原产于南美”",
    "slides.s18e.box2.title": "身体感官互动气泡（低预期 · 极高信息量）",
    "slides.s18e.box2.body": "“红色的不是花瓣是苞片！请用手指触摸干爽纸质触感”",

    "slides.s18f.shortTitle": "阶段五：E_gain计算模型",
    "slides.s18f.title": "信息加权认知吸收量（E_gain）计算模型",
    "slides.s18f.guide": "【公式推导】将空间注视概率与区域信息量加权求和，度量真实知识吸收总量",
    "slides.s18f.meaning": "期望认知吸收总量 = 各区域注视时间占比 × 语义自信息量",

    "slides.s18g.shortTitle": "阶段五：马尔可夫死循环",
    "slides.s18g.title": "马尔可夫转移矩阵：打破 93% 长文本死循环",
    "slides.s18g.guide": "【动线解构】基于一阶马尔可夫链量化视线在各语义功能区之间的流转秩序",
    "slides.s18g.kpi.title": "长文本自循环停滞率",
    "slides.s18g.kpi.sub": "马尔可夫矩阵证实：长文本死循环被彻底打破，视线平稳转导至感官互动区 (p < 0.001)",
    "slides.s18g.box1.title": "对照组：死死困在长文本中 (0.93)",
    "slides.s18g.box1.body": "视线在文本区内反复自循环（93%），跳至图片的概率仅 4%，形成了封闭的阅读陷阱与严重停滞。",
    "slides.s18g.box2.title": "改良组：多模态自由流转 (多点开花)",
    "slides.s18g.box2.body": "视线自正文平稳流向感官气泡（0.19）、图标（0.13）与花语（0.38），构建了顺畅的认知导流网络。",

    "slides.s18h.shortTitle": "阶段五：认知传递能效比",
    "slides.s18h.title": "认知信息传递能效比：单位视觉负荷的产出",
    "slides.s18h.guide": "【能效建模】构建 η = E_gain / GTE 指标，量化单位视觉搜索努力换取的信息增益",
    "slides.s18h.meaning": "认知能效比 = 有效知识吸收量 / 动线转移熵（视觉搜索努力）",
    "slides.s18h.m2.title": "实证显著提升 +29.9% (p=0.004)",

    "slides.s18i1.shortTitle": "阶段五：动线转移熵分析",
    "slides.s18i1.title": "动线转移熵 (GTE) 分析：探索路径与认知负荷",
    "slides.s18i1.guide": "【图表A】量化视线转移随机度与跨语义功能区的自主探索活力",

    "slides.s18i2.shortTitle": "阶段五：认知吸收量全景",
    "slides.s18i2.title": "认知吸收量 (E_gain) 配对检验：全量 13 人无一下降",
    "slides.s18i2.guide": "【图表B】13 位被试配对连线全部陡峭向上倾斜，有效知识获得量翻倍暴增",

    "slides.s18i3.shortTitle": "阶段五：认知能效比实证",
    "slides.s18i3.title": "认知传递能效比 (η) 分析：单位视觉努力下的知识产出",
    "slides.s18i3.guide": "【图表C】量化单位视线搜索转移负荷所能换取的有效信息增益",

    "slides.s18i4.shortTitle": "阶段五：空间均衡度图解",
    "slides.s18i4.title": "空间注视均衡度 (SGE) 与设计对齐 (KL 散度)",
    "slides.s18i4.guide": "【图表D】量化视线空间离散度与共创设计预期的拟合收敛程度",

    "slides.s18j.shortTitle": "阶段五：实证推断汇总",
    "slides.s18j.title": "全量实证结果：有效认知信息吸收量翻倍暴增",
    "slides.s18j.guide": "【全量验证】13 位被试配对检验证实有效认知吸收量与能效比实现全面跃升",
    "slides.s18j.kpi.title": "有效认知信息吸收总量 (E_gain)",
    "slides.s18j.kpi.sub": "0.585 bits → 1.332 bits (p < 0.000001 ***) | 全量 13 位被试全部单调显著上升",
    "slides.s18j.box1.title": "真实认知获取成倍跃升",
    "slides.s18j.box1.body": "将注视时间与信息惊讶度结合后，实验组有效知识获得量翻倍，13 位被试无一下降（+86.8% ~ +243.1%）。",
    "slides.s18j.box2.title": "认知信息传递能效比显著提升",
    "slides.s18j.box2.body": "能效比从 1.083 提升至 1.407（p = 0.004, d = 0.982），证明观众以更少、更舒适的视觉搜索换取了更高价值的信息。",
    "slides.s18j.finding1.title": "信息论对共创原则的坚实支撑",
    "slides.s18j.finding1.body": "以香农信息论底层数学模型严谨证实了共创标牌（A/R/S原则）在降低认知负荷的同时实现了知识获得最大化。",
    "slides.s18j.finding2.title": "博士阶段研究的理论支点",
    "slides.s18j.finding2.body": "高惊讶度与顺畅马尔可夫流为后续结合双重编码理论与长期记忆保持（Retention）实验奠定了量化计算基础。",

    "slides.s18k.shortTitle": "阶段五：13人数据明细",
    "slides.s18k.title": "全量 13 位被试逐人明细数据表 (Group A & B)",
    "slides.s18k.guide": "【逐人明细】记录 Group A (7人) 与 Group B (6人) 每位被试的对照与改良数据及增益率",

    "slides.s18l.shortTitle": "阶段五：答辩话术指南",
    "slides.s18l.title": "答辩与学术汇报“三步法话术指南”",
    "slides.s18l.guide": "【汇报策略】向导师与答辩评审阐述本信息论创新方法的专业逻辑路径",
    "slides.s18l.s1.title": "破除时长假象",
    "slides.s18l.s1.body": "“传统分析只看时长，但对照组长文本的高停留实为认知受阻；马尔可夫矩阵证实其自循环停滞率高达 93%。”",
    "slides.s18l.s2.title": "引入惊讶度加权",
    "slides.s18l.s2.body": "“引入香农信息论，根据‘信息违背预期时信息量最大’原则构建 E_gain 与能效比 η，精准度量真实知识获得。”",
    "slides.s18l.s3.title": "证实有效吸收翻倍",
    "slides.s18l.s3.body": "“全量 13 人配对检验证实 E_gain 提升 127.7%（p<0.000001, d=3.46），13人全上升，科学证实共创卓越价值。”"
}

en_dict = {
    "chapters.methods": "Research Methods",
    "chapters.basicAnalysis": "Basic Analysis",
    "chapters.deepAnalysis": "Deep Analysis",

    "slides.s18a.shortTitle": "Phase 5: Entropy Intro",
    "slides.s18a.title": "Deep Cognitive Analysis: Information Entropy & Surprisal Theory",
    "slides.s18a.guide": "[Theory Introduction] Moving beyond superficial dwell time to quantify knowledge absorption and cognitive flow",
    "slides.s18a.q1.title": "Is Longer Gaze Always Better?",
    "slides.s18a.q1.body": "Conventional eye-tracking equates longer dwell time with higher interest. However, in botanical signage, text difficulty often causes severe hesitation misjudged as deep immersion.",
    "slides.s18a.q2.title": "Information Theory Measures Real Gain",
    "slides.s18a.q2.body": "Applying Shannon Surprisal, where unexpected sensory cues deliver higher information value, accurately captures effective knowledge yield.",
    "slides.s18a.finding1.title": "Paradigm Shift",
    "slides.s18a.finding1.body": "Shifting focus from crude dwell time to effective information yield and gaze flow order under visual effort.",
    "slides.s18a.finding2.title": "Progressive Analytical Sequence",
    "slides.s18a.finding2.body": "Step-by-step breakdown: Baseline limits → Text stagnation trap → Surprisal modeling → Case calculations → Markov loops → 4-panel empirical charts & full test.",

    "slides.s18b.shortTitle": "Phase 5: Baseline Metrics",
    "slides.s18b.title": "Three Conventional Eye-Tracking Metrics and Their Assumptions",
    "slides.s18b.guide": "[Baseline Review] Outlining the three standard gaze metrics commonly used in signage research",
    "slides.s18b.m1.title": "Dwell Time",
    "slides.s18b.m1.body": "Total duration spent in an AOI, assuming longer gaze reflects greater visitor interest.",
    "slides.s18b.m2.title": "Fixation Count",
    "slides.s18b.m2.body": "Number of fixations landing in an AOI, assuming frequency correlates with visual importance.",
    "slides.s18b.m3.title": "Heatmap Visualization",
    "slides.s18b.m3.body": "Gaussian kernel density distributions, assuming hotspot redness denotes primary engagement.",
    "slides.s18b.critical_flaw": "All three metrics implicitly assume every gaze second has equal cognitive processing value, unable to distinguish comprehension from reading struggle.",

    "slides.s18c.shortTitle": "Phase 5: Cognitive Friction",
    "slides.s18c.title": "Fatal Flaw of Conventional Metrics: Cognitive Friction vs Deep Reading",
    "slides.s18c.guide": "[Pitfall Analysis] Exposing how dense botanical texts generate deceptive high dwell times",
    "slides.s18c.c1.title": "Superficial Data Illusion: 44.3% Text Dwell",
    "slides.s18c.c1.body": "In the control sign, descriptive text received the highest dwell time. Standard metrics misinterpret this as peak visitor interest.",
    "slides.s18c.c2.title": "Cognitive Reality: Friction & Stagnation",
    "slides.s18c.c2.body": "Dense Latin taxonomy and morphological jargon cause severe reading friction; gaze wanders helplessly inside text without comprehension.",
    "slides.s18c.rethink": "Diagnosis: High dwell time reflects severe cognitive friction rather than knowledge gain, necessitating information-theoretic tools.",

    "slides.s18d.shortTitle": "Phase 5: Shannon Surprisal",
    "slides.s18d.title": "Shannon Information Theory & Surprisal: Counter-Intuitive Cognitive Gain",
    "slides.s18d.guide": "[Mathematical Modeling] Formulating I = -log2(P) to quantify the high value of sensory interactions",
    "slides.s18d.axiom": "“Information is maximized when an event violates prior expectations”",
    "slides.s18d.box1.title": "Predictive Coding Mechanism",
    "slides.s18d.box1.body": "Routine common knowledge (high prior P) fails to engage deep processing; counter-intuitive cues (low prior P) trigger robust hippocampal encoding.",
    "slides.s18d.box2.title": "Self-Information (bits)",
    "slides.s18d.box2.body": "Self-information I in bits precisely measures uncertainty reduction, providing the mathematical foundation for true knowledge gain.",

    "slides.s18e.shortTitle": "Phase 5: Surprisal Cases",
    "slides.s18e.title": "AOI Information Weights and Case Calculations",
    "slides.s18e.guide": "[Numerical Computation] Comparing surprisal values between conventional text and sensory cues",
    "slides.s18e.box1.title": "Conventional Botanical Text (High Expectation)",
    "slides.s18e.box1.body": "\"Bougainvillea spectabilis is a woody vine native to South America\"",
    "slides.s18e.box2.title": "Sensory Interactive Bubble (Low Expectation)",
    "slides.s18e.box2.body": "\"The red parts are papery bracts, not petals! Touch them with your finger\"",

    "slides.s18f.shortTitle": "Phase 5: E_gain Model",
    "slides.s18f.title": "Information-Weighted Cognitive Gain (E_gain) Model",
    "slides.s18f.guide": "[Mathematical Formulation] Weighting spatial gaze distribution by semantic surprisal",
    "slides.s18f.meaning": "Expected Cognitive Gain = ∑ [ Gaze Duration Proportion × Semantic Surprisal ]",

    "slides.s18g.shortTitle": "Phase 5: Markov Loop",
    "slides.s18g.title": "Markov Transition Matrix: Breaking 93% Long-Text Stagnation",
    "slides.s18g.guide": "[Gaze Flow Modeling] Quantifying gaze transitions across semantic zones via first-order Markov chains",
    "slides.s18g.kpi.title": "Text Self-Loop Stagnation Rate",
    "slides.s18g.kpi.sub": "Markov matrix proves: Text stagnation is dissolved, smoothly guiding gaze into interactive zones (p < 0.001)",
    "slides.s18g.box1.title": "Control: Trapped in Long Text (0.93)",
    "slides.s18g.box1.body": "Gaze loops inside text with 93% probability, transitioning to photos at only 4%, creating a closed reading trap.",
    "slides.s18g.box2.title": "Experimental: Multimodal Fluid Transitions",
    "slides.s18g.box2.body": "Gaze transitions seamlessly from text to sensory bubbles (0.19), icons (0.13), and meanings (0.38).",

    "slides.s18h.shortTitle": "Phase 5: Efficiency Ratio",
    "slides.s18h.title": "Cognitive Transmission Efficiency Ratio (η): Output per Unit Search Effort",
    "slides.s18h.guide": "[Efficiency Modeling] Defining η = E_gain / GTE to measure knowledge return on visual search investment",
    "slides.s18h.meaning": "Cognitive Efficiency = Knowledge Gain / Transition Entropy (Search Load)",
    "slides.s18h.m2.title": "Significant Boost +29.9% (p=0.004)",

    "slides.s18i1.shortTitle": "Phase 5: GTE Chart Analysis",
    "slides.s18i1.title": "Gaze Transition Entropy (GTE): Exploration Paths & Visual Load",
    "slides.s18i1.guide": "[Chart A] Quantifying gaze transition randomness and multi-domain exploration vitality",

    "slides.s18i2.shortTitle": "Phase 5: E_gain Chart Analysis",
    "slides.s18i2.title": "Cognitive Gain (E_gain) Paired Test: Monotonic Increase for All 13 Participants",
    "slides.s18i2.guide": "[Chart B] All 13 participant trajectory lines tilt upward, confirming doubled knowledge acquisition",

    "slides.s18i3.shortTitle": "Phase 5: Efficiency Ratio Chart",
    "slides.s18i3.title": "Cognitive Efficiency (η): Knowledge Yield per Unit Visual Search Effort",
    "slides.s18i3.guide": "[Chart C] Quantifying effective information yield gained per unit of visual search investment",

    "slides.s18i4.shortTitle": "Phase 5: Spatial Balance Chart",
    "slides.s18i4.title": "Spatial Gaze Entropy (SGE) & Design Intent Alignment (KL Divergence)",
    "slides.s18i4.guide": "[Chart D] Measuring gaze spatial dispersion and convergence with co-creation design intent",

    "slides.s18j.shortTitle": "Phase 5: Empirical Summary",
    "slides.s18j.title": "Empirical Findings: Doubling of Cognitive Information Gain",
    "slides.s18j.guide": "[Empirical Proof] Full 13-participant paired tests confirm massive leap in E_gain and efficiency ratio",
    "slides.s18j.kpi.title": "Total Effective Cognitive Gain (E_gain)",
    "slides.s18j.kpi.sub": "0.585 bits → 1.332 bits (p < 0.000001 ***) | All 13 participants showed monotonic increase",
    "slides.s18j.box1.title": "Massive Jump in Knowledge Absorption",
    "slides.s18j.box1.body": "Combining gaze duration with surprisal weights reveals a +127.7% increase in effective knowledge gain across all participants.",
    "slides.s18j.box2.title": "Significant Boost in Efficiency Ratio (η)",
    "slides.s18j.box2.body": "Efficiency ratio improved from 1.083 to 1.407 (+29.9%, p = 0.004), demonstrating higher cognitive yield per visual effort.",
    "slides.s18j.finding1.title": "Solid Information-Theoretic Support",
    "slides.s18j.finding1.body": "Mathematical modeling confirms that co-created signage simultaneously reduces cognitive burden and maximizes knowledge gain.",
    "slides.s18j.finding2.title": "Pillar for Doctoral Research",
    "slides.s18j.finding2.body": "High surprisal and fluent Markov flows lay the computational foundation for upcoming long-term retention experiments.",

    "slides.s18k.shortTitle": "Phase 5: 13-Subject Ledger",
    "slides.s18k.title": "Full 13-Participant Individual Data Ledger (Groups A & B)",
    "slides.s18k.guide": "[Participant Breakdown] Detailed individual performance metrics and percentage gains across Groups A & B",

    "slides.s18l.shortTitle": "Phase 5: Defense Strategy",
    "slides.s18l.title": "Three-Step Academic Defense and Presentation Logic Guide",
    "slides.s18l.guide": "[Presentation Strategy] Strategic logical pathway for reporting this information-theoretic method to supervisors and committees",
    "slides.s18l.s1.title": "Expose Flaws of Dwell Time",
    "slides.s18l.s1.body": "“Traditional gaze time misinterprets text reading friction as engagement; Markov matrices reveal a 93% stagnation trap.”",
    "slides.s18l.s2.title": "Introduce Surprisal Weighting",
    "slides.s18l.s2.body": "“Applying Shannon surprisal principles (I=-log2 P) measures true knowledge yield E_gain and efficiency ratio η.”",
    "slides.s18l.s3.title": "Present Hard Empirical Proof",
    "slides.s18l.s3.body": "“All 13 participants achieved significant E_gain growth (+127.7%, p<0.000001, d=3.46), validating co-creation scientifically.”"
}

ja_dict = {
    "chapters.methods": "研究方法",
    "chapters.basicAnalysis": "基礎分析",
    "chapters.deepAnalysis": "深度分析",

    "slides.s18a.shortTitle": "フェーズ5: エントロピー導入",
    "slides.s18a.title": "情報エントロピーとサプライザル理論に基づく認知深化分析",
    "slides.s18a.guide": "【理論導入】単なる注視時間の錯覚を超え、真の知識獲得量と認知フローを定量化する",
    "slides.s18a.q1.title": "長く見ることが良いことなのか？",
    "slides.s18a.q1.body": "従来の指標は「注視が長い＝興味が高い」と仮定します。しかし難解な長文での停滞や躊躇が誤判定される限界があります。",
    "slides.s18a.q2.title": "情報理論による真の獲得量計測",
    "slides.s18a.q2.body": "シャノンのサプライザル理論（予想外であるほど情報量が高い）を導入し、有効な知識獲得を精密にモデル化します。",
    "slides.s18a.finding1.title": "認知パラダイムの転換",
    "slides.s18a.finding1.body": "表面的な注視時間から、視覚的努力あたりの有効情報獲得量と視線秩序へのシフト。",
    "slides.s18a.finding2.title": "段階的分析ステップ",
    "slides.s18a.finding2.body": "従来指標の限界 → 読解停滞の罠 → サプライザル定式化 → 事例計算 → マルコフ死循環 → 4次元実証図解と全量検証。",

    "slides.s18b.shortTitle": "フェーズ5: 従来指標の限界",
    "slides.s18b.title": "視線計測の三大従来指標とその前提仮定",
    "slides.s18b.guide": "【ベースライン整理】既存の植物サイン研究で多用される3つの従来指標を整理",
    "slides.s18b.m1.title": "注視時間 (Dwell Time)",
    "slides.s18b.m1.body": "領域内の総滞在秒数。「長く見るほど興味がある」と仮定。",
    "slides.s18b.m2.title": "注视回数 (Fixation Count)",
    "slides.s18b.m2.body": "領域への視線着弾頻度。「回数が多いほど視覚的重要度が高い」と仮定。",
    "slides.s18b.m3.title": "ヒートマップ (Heatmap)",
    "slides.s18b.m3.body": "ガウス密度描画。「赤色ハイライトが絶対的関心焦点」と仮定。",
    "slides.s18b.critical_flaw": "三大指標はすべての注視秒数が均等な価値を持つと仮定し、読解の苦戦や受動的停滞を区別できない欠陥があります。",

    "slides.s18c.shortTitle": "フェーズ5: 読解停滞の罠",
    "slides.s18c.title": "従来指標の致命的誤謬：熟読ではなく認知摩擦",
    "slides.s18c.guide": "【誤謬の解明】大段落の難解解説文が生み出す高注視時間の「見せかけの繁栄」を分析",
    "slides.s18c.c1.title": "表面データの錯覚：長文注視割合 44.3%",
    "slides.s18c.c1.body": "対照群では説明文の注視が首位。従来法はこれを「最大の興味関心」と誤読します。",
    "slides.s18c.c2.title": "認知的実態：摩擦と読解停止",
    "slides.s18c.c2.body": "難解な学名や専門用語により「読み進められず、要点が不明」となり、視線が受動的に停滞する認知過負荷です。",
    "slides.s18c.rethink": "診断結論：長滞在時間は知識獲得ではなく情報解読の摩擦を反映しており、情報理論の導入が不可欠です。",

    "slides.s18d.shortTitle": "フェーズ5: サプライザル理論",
    "slides.s18d.title": "シャノン情報論とサプライザル：予想を裏切る認知的価値",
    "slides.s18d.guide": "【数理モデル】自己情報量 I = -log2(P) を導入し、感覚的インタラクションの高い知識価値を算出",
    "slides.s18d.axiom": "「情報は、予想に反するときほど、情報量が多い」",
    "slides.s18d.box1.title": "予測符号化メカニズム",
    "slides.s18d.box1.body": "日常の常識（高事前確率）は深い認知を活性化しません。予想を覆す手がかり（低事前確率）が海馬の記憶符号化を促進します。",
    "slides.s18d.box2.title": "自己情報量 (bits)",
    "slides.s18d.box2.body": "自己情報量 I（bits）は不確実性の解消による真の知識増分を計測し、学習効果の数学的基盤を提供します。",

    "slides.s18e.shortTitle": "フェーズ5: 事例情報量計算",
    "slides.s18e.title": "各領域の情報量重み付けと事例数値計算",
    "slides.s18e.guide": "【数値演習】従来の分類学テキストと共創感覚バブルの自己情報量の格差を計算",
    "slides.s18e.box1.title": "従来の専門解説文（高予想 · 低情報量）",
    "slides.s18e.box1.body": "「オシロイバナ科の木本性蔓植物で南米原産」",
    "slides.s18e.box2.title": "身体感覚インタラクション（低予想 · 超高情報量）",
    "slides.s18e.box2.body": "「赤い部分は花びらではなく苞葉！触って紙のような質感を確かめよう」",

    "slides.s18f.shortTitle": "フェーズ5: E_gain数理モデル",
    "slides.s18f.title": "情報加重認知獲得量（E_gain）計算モデル",
    "slides.s18f.guide": "【公式導出】注視確率と領域情報量を加重合計し、真の知識獲得総量を計測",
    "slides.s18f.meaning": "期待認知獲得総量 = 各領域の注視時間比率 × 意味的自己情報量",

    "slides.s18g.shortTitle": "フェーズ5: マルコフ遷移行列",
    "slides.s18g.title": "マルコフ遷移行列：長文の93%自循環死循環を打破",
    "slides.s18g.guide": "【動線解読】1次マルコフ連鎖により各機能領域間の視線遷移秩序を定量化",
    "slides.s18g.kpi.title": "長文自循環停滞率",
    "slides.s18g.kpi.sub": "マルコフ行列が実証：長文の停滞が解消され、感覚インタラクション領域へとスムーズに誘導 (p < 0.001)",
    "slides.s18g.box1.title": "対照群：長文内に閉じ込められた視線 (0.93)",
    "slides.s18g.box1.body": "視線がテキスト内で自循環（93%）、写真への遷移はわずか4%という閉塞トラップ。",
    "slides.s18g.box2.title": "改良群：マルチモーダルな自由循環",
    "slides.s18g.box2.body": "本文から感覚バブル（0.19）、アイコン（0.13）、花言葉（0.38）へと滑らかに遷移。",

    "slides.s18h.shortTitle": "フェーズ5: 認知能率比",
    "slides.s18h.title": "認知情報伝達効率比（η）：単位視覚負荷あたりの産出量",
    "slides.s18h.guide": "【効率モデル】η = E_gain / GTE 指标を定義し、視覚探索努力に対する情報獲得効率を定量化",
    "slides.s18h.meaning": "認知効率比 = 有効知識獲得量 / 視線遷移エントロピー（探索負荷）",
    "slides.s18h.m2.title": "実証的有意向上 +29.9% (p=0.004)",

    "slides.s18i1.shortTitle": "フェーズ5: 遷移行列エントロピー図",
    "slides.s18i1.title": "視線遷移エントロピー (GTE) 分析：探索経路と認知負荷",
    "slides.s18i1.guide": "【図表A】視線遷移のランダム性と複数領域にまたがる自発的探索活力を定量化",

    "slides.s18i2.shortTitle": "フェーズ5: 認知獲得量図",
    "slides.s18i2.title": "認知獲得量 (E_gain) 対応検定：13名全員で例外なき向上",
    "slides.s18i2.guide": "【図表B】13名すべての推移線が急激に右肩上がりに向上し、獲得量が倍増",

    "slides.s18i3.shortTitle": "フェーズ5: 認知能率比図",
    "slides.s18i3.title": "認知伝達能率比 (η) 分析：単位視覚努力あたりの知識獲得",
    "slides.s18i3.guide": "【図表C】視覚探索努力1単位あたりに獲得できる有効情報量を定量化",

    "slides.s18i4.shortTitle": "フェーズ5: 空間構造図",
    "slides.s18i4.title": "空間注視均等度 (SGE) および設計意図との整合性 (KL情報量)",
    "slides.s18i4.guide": "【図表D】視線の空間分散と共創設計意図への収束度を計測",

    "slides.s18j.shortTitle": "フェーズ5: 実証統計総括",
    "slides.s18j.title": "全量实证结果：有效认知信息吸收量翻倍暴增",
    "slides.s18j.guide": "【全量検証】13名の対応のあるt検定により有効認知獲得量と効率比の大幅向上を実証",
    "slides.s18j.kpi.title": "有効認知情報獲得総量 (E_gain)",
    "slides.s18j.kpi.sub": "0.585 bits → 1.332 bits (p < 0.000001 ***) | 全13名の被験者全員で単調有意増加",
    "slides.s18j.box1.title": "真の認知獲得の倍増",
    "slides.s18j.box1.body": "注視時間とサプライザルを結合した結果、実験群の知識獲得量が倍増（+86.8%〜+243.1%）。",
    "slides.s18j.box2.title": "認知情報伝達効率の有意向上",
    "slides.s18j.box2.body": "効率比が 1.083 から 1.407 へと向上（+29.9%, p = 0.004）、高効率な探索を証明。",
    "slides.s18j.finding1.title": "共創原則への強固な数理的裏付け",
    "slides.s18j.finding1.body": "情報理論モデルにより、共創原則（A/R/S）が負荷低減と知識最大化を両立することを証明。",
    "slides.s18j.finding2.title": "博士課程研究の理論的支柱",
    "slides.s18j.finding2.body": "高サプライザルと円滑なマルコフ流が今後の長期記憶定着実験の基盤となる。",

    "slides.s18k.shortTitle": "フェーズ5: 13名個別台帳",
    "slides.s18k.title": "全13名の被験者個別詳細データ台帳 (グループA・B)",
    "slides.s18k.guide": "【個別詳細】グループA（7名）およびグループB（6名）の各被験者の対照・改良データと伸び率",

    "slides.s18l.shortTitle": "フェーズ5: 発表論理ガイド",
    "slides.s18l.title": "学位審査・学術発表用「3ステップ発表ガイド」",
    "slides.s18l.guide": "【発表戦略】指導教員や審査委員会に本情報理論モデルの論理展開を伝えるガイドライン",
    "slides.s18l.s1.title": "注視時間の錯覚を打破",
    "slides.s18l.s1.body": "「従来の滞在時間は読解摩擦を誤判定；マルコフ行列により93%の停滞死循環を暴露。」",
    "slides.s18l.s2.title": "サプライザル加重を導入",
    "slides.s18l.s2.body": "「シャノン情報理論（I=-log2 P）を適用し、真の知識獲得 E_gain と効率比 η を定式化。」",
    "slides.s18l.s3.title": "確固たる実証データを提示",
    "slides.s18l.s3.body": "「全13名で E_gain が+127.7%（p<0.000001, d=3.46）向上し、共創の卓越性を科学的に実証。」"
}

def sync_dict(filename, new_entries):
    fpath = os.path.join(I18N_DIR, filename)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # clean out old s18i.* keys
    keys_to_del = [k for k in data.keys() if k.startswith('slides.s18i.')]
    for k in keys_to_del:
        del data[k]
    data.update(new_entries)
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

sync_dict('zh.json', zh_dict)
sync_dict('en.json', en_dict)
sync_dict('ja.json', ja_dict)
sync_dict('es-MX.json', en_dict)

print("[*] 4 个语言字典文件同步完毕！")
