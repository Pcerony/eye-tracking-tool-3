#!/usr/bin/env python3
"""
scripts/update_deck_and_i18n.py

更新 deck-manifest.json 与 src/i18n/ (zh, en, ja, es-MX) 字典
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_FILE = os.path.join(BASE_DIR, 'deck-manifest.json')
I18N_DIR = os.path.join(BASE_DIR, 'src', 'i18n')

# 1. 更新 deck-manifest.json
with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

new_slide_entries = [
    {
        "id": "s18a-entropy-intro",
        "chapterId": "methods",
        "layout": "data",
        "content": "src/content/slides/s18a-entropy-intro.json",
        "assets": [],
        "claims": []
    },
    {
        "id": "s18b-conventional-metrics",
        "chapterId": "methods",
        "layout": "data",
        "content": "src/content/slides/s18b-conventional-metrics.json",
        "assets": [],
        "claims": []
    },
    {
        "id": "s18c-cognitive-friction",
        "chapterId": "methods",
        "layout": "data",
        "content": "src/content/slides/s18c-cognitive-friction.json",
        "assets": [],
        "claims": []
    },
    {
        "id": "s18d-surprisal-principle",
        "chapterId": "methods",
        "layout": "data",
        "content": "src/content/slides/s18d-surprisal-principle.json",
        "assets": [],
        "claims": []
    },
    {
        "id": "s18e-markov-stagnation",
        "chapterId": "methods",
        "layout": "data",
        "content": "src/content/slides/s18e-markov-stagnation.json",
        "assets": [],
        "claims": []
    },
    {
        "id": "s18f-entropy-empirical",
        "chapterId": "methods",
        "layout": "data",
        "content": "src/content/slides/s18f-entropy-empirical.json",
        "assets": [],
        "claims": []
    }
]

# 找到 s17e-statistical-synthesis 并插入在其后
existing_slides = manifest.get('slides', [])
new_slides_list = []
inserted = False

for slide in existing_slides:
    if slide['id'] in [s['id'] for s in new_slide_entries]:
        continue # 避免重复插入
    new_slides_list.append(slide)
    if slide['id'] == 's17e-statistical-synthesis':
        new_slides_list.extend(new_slide_entries)
        inserted = True

if not inserted:
    new_slides_list.extend(new_slide_entries)

manifest['slides'] = new_slides_list

with open(MANIFEST_FILE, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print(f"[*] deck-manifest.json 已更新，当前幻灯片总数: {len(manifest['slides'])}")

# 2. 定义多语言键值对
zh_keys = {
    "slides.s18a.title": "基于信息熵与惊讶度理论的深度分析",
    "slides.s18a.guide": "【理论引入】超越“注视时长”表面假象，量化真实知识吸收与阅读认知流",
    "slides.s18a.shortTitle": "阶段四：信息熵理论引入",
    "slides.s18a.q1.title": "看得久就是好吗？",
    "slides.s18a.q1.body": "传统眼动指标假定“注视越久 = 越感兴趣”。但在植物标牌中，生僻文字导致的卡顿与犹豫常被误判为深度沉浸。",
    "slides.s18a.q2.title": "信息论度量真实获得",
    "slides.s18a.q2.body": "引入香农信息熵与惊讶度（Surprisal），结合“信息违背预期时信息量最大”的原理，精确量化观众吸收的有效知识增量。",
    "slides.s18a.finding1.title": "认知范式升级",
    "slides.s18a.finding1.body": "从“表面注视时长”转向“单位视觉负荷下的有效信息吸收量与动线秩序”。",
    "slides.s18a.finding2.title": "循序渐进分析链条",
    "slides.s18a.finding2.body": "接下来将分步拆解：常规指标局限 → 文本停滞误区 → 惊讶度建模 → 马尔可夫死循环解构 → 实证跃升成果。",

    "slides.s18b.title": "传统眼动三大常规指标及其假设",
    "slides.s18b.guide": "【基线梳理】归纳现有植物标牌研究普遍依赖的三大常规眼动度量体系",
    "slides.s18b.shortTitle": "阶段四：常规指标局限",
    "slides.s18b.m1.title": "注视时长 (Dwell Time)",
    "slides.s18b.m1.body": "记录视线在某区域停留的总秒数或时间百分比，底层假设“停越久 = 越感兴趣”。",
    "slides.s18b.m2.title": "注视次数 (Fixation Count)",
    "slides.s18b.m2.body": "记录视线落入该区域的落点频次，底层假设“落点越多 = 越具视觉重要性”。",
    "slides.s18b.m3.title": "注视热力图 (Heatmap)",
    "slides.s18b.m3.body": "高斯核密度渲染的空间点云，底层假设“红色高亮区代表绝对吸引力焦点”。",
    "slides.s18b.finding1.title": "常规指标的局限",
    "slides.s18b.finding1.body": "三大指标仅能记录物理空间上的停留位置，无法辨识注视背后的认知理解质量。",
    "slides.s18b.finding2.title": "均质化假定缺陷",
    "slides.s18b.finding2.body": "默认“每秒注视具有均等的信息加工价值”，忽略了晦涩文字带来的认知挣扎与无序停滞。",

    "slides.s18c.title": "常规指标的致命误区：认知受阻而非深度阅读",
    "slides.s18c.guide": "【误区揭示】剖析传统大段科普文字如何造成高注视时长的“虚假繁荣”",
    "slides.s18c.shortTitle": "阶段四：认知受阻误区",
    "slides.s18c.c1.title": "表面数据假象：长文本注视占比 44.3%",
    "slides.s18c.c1.body": "在对照组中，说明文字区注视时长位居首位。传统眼动模型据此推论“观众对大段科普内容最感兴趣”。",
    "slides.s18c.c2.title": "真实认知困境：认知摩擦与阅读停滞",
    "slides.s18c.c2.body": "大段生僻拉丁学名与形态学术语导致“读不下去、找不到重点”，视线在文本内被动打转卡顿，实为负荷过载而非深度阅读。",
    "slides.s18c.finding1.title": "文本注视壁垒的本质",
    "slides.s18c.finding1.body": "高停留时长反映的是信息解码受阻（Cognitive Friction），而非高价值的知识吸收。",
    "slides.s18c.finding2.title": "方法学转向必然性",
    "slides.s18c.finding2.body": "必须引入能精确度量“信息意外度（Surprisal）”与“动线流转秩序（Markov）”的新型信息论分析体系。",

    "slides.s18d.title": "香农信息论与惊讶度：违背预期的认知增益",
    "slides.s18d.guide": "【数学建模】引入自信息量 I = -log2(P)，量化反常识感官互动的高知识价值",
    "slides.s18d.shortTitle": "阶段四：香农惊讶度建模",
    "slides.s18d.axiom": "“信息在违背预期时，其承载的信息量最大”",
    "slides.s18d.box1.title": "常规科属文字（高预期 · 低信息量）",
    "slides.s18d.box1.body": "“九重葛为紫茉莉科木质藤本，原产于南美” —— 属于读者先验知识库内的泛化事实，信息增量极低。",
    "slides.s18d.box2.title": "身体感官互动（低预期 · 极高信息量）",
    "slides.s18d.box2.body": "“红色的不是花瓣是苞片！请用手指触摸干爽纸质触感” —— 打破常识预期，激发高认知惊讶度与记忆编码。",
    "slides.s18d.finding1.title": "预测编码机制",
    "slides.s18d.finding1.body": "人脑对打破先验预期的反常识感官线索具有天然的高效加工与深度编码敏感性。",
    "slides.s18d.finding2.title": "共创 R 原则价值溯源",
    "slides.s18d.finding2.body": "R 原则（身体与感官关联）通过注入高惊讶度信息，在根本上重塑了观众的学习体验与知识吸收能效。",

    "slides.s18e.title": "马尔可夫转移矩阵：打破 93% 长文本死循环",
    "slides.s18e.guide": "【动线解构】基于一阶马尔可夫链量化视线在各语义功能区之间的流转秩序",
    "slides.s18e.shortTitle": "阶段四：马尔可夫死循环解构",
    "slides.s18e.kpi.title": "长文本自循环停滞率",
    "slides.s18e.kpi.sub": "马尔可夫矩阵证实：长文本死循环被彻底打破，视线平稳转导至感官互动区 (p < 0.001)",
    "slides.s18e.box1.title": "对照组：死死困在长文本中 (0.93)",
    "slides.s18e.box1.body": "视线在文本区内反复自循环（93%），跳至图片的概率仅 4%，形成了封闭的阅读陷阱与严重停滞。",
    "slides.s18e.box2.title": "改良组：多模态自由流转 (多点开花)",
    "slides.s18e.box2.body": "视线自正文平稳流向感官气泡（0.19）、图标（0.13）与花语（0.38），构建了顺畅的认知导流网络。",
    "slides.s18e.finding1.title": "阅读死循环的瓦解",
    "slides.s18e.finding1.body": "共创标牌的模块化排版成功消除了长文本的视线吸附陷阱，降低了无序回视消耗。",
    "slides.s18e.finding2.title": "多模态导流闭环",
    "slides.s18e.finding2.body": "视线从被动的单区停滞转变为主动的跨区域多点探索，实现了高效认知流。",

    "slides.s18f.title": "全量实证结果：有效认知信息吸收量翻倍暴增",
    "slides.s18f.guide": "【全量验证】13 位被试配对检验证实有效认知吸收量与能效比实现全面跃升",
    "slides.s18f.shortTitle": "阶段四：实证认知跃升",
    "slides.s18f.kpi.title": "有效认知信息吸收总量 (E_gain)",
    "slides.s18f.kpi.sub": "0.585 bits → 1.332 bits (p < 0.000001 ***) | 全量 13 位被试全部单调显著上升",
    "slides.s18f.box1.title": "真实认知获取成倍跃升",
    "slides.s18f.box1.body": "将注视时间与信息惊讶度结合后，实验组有效知识获得量翻倍，13 位被试无一下降（+86.8% ~ +243.1%）。",
    "slides.s18f.box2.title": "认知信息传递能效比显著提升",
    "slides.s18f.box2.body": "能效比从 1.083 提升至 1.407（p = 0.004, d = 0.982），证明观众以更少、更舒适的视觉搜索换取了更高价值的信息。",
    "slides.s18f.finding1.title": "信息论对共创原则的坚实支撑",
    "slides.s18f.finding1.body": "以香农信息论底层数学模型严谨证实了共创标牌（A/R/S原则）在降低认知负荷的同时实现了知识获得最大化。",
    "slides.s18f.finding2.title": "博士阶段研究的理论支点",
    "slides.s18f.finding2.body": "高惊讶度与顺畅马尔可夫流为后续结合双重编码理论与长期记忆保持（Retention）实验奠定了量化计算基础。"
}

en_keys = {
    "slides.s18a.title": "Deep Analysis: Information Entropy & Surprisal Theory",
    "slides.s18a.guide": "[Theoretical Framework] Going beyond dwell time to quantify knowledge gain and cognitive flow",
    "slides.s18a.shortTitle": "Phase 4: Entropy Intro",
    "slides.s18a.q1.title": "Is Longer Dwell Time Always Better?",
    "slides.s18a.q1.body": "Conventional metrics assume dwell time reflects interest. In signage, lexical difficulty and cognitive friction often masquerade as deep engagement.",
    "slides.s18a.q2.title": "Information Theory Measures Real Gain",
    "slides.s18a.q2.body": "By introducing Shannon Entropy and Surprisal, we quantify how unexpected, high-surprisal sensory prompts deliver genuine knowledge gains.",
    "slides.s18a.finding1.title": "Cognitive Paradigm Shift",
    "slides.s18a.finding1.body": "Moving from superficial dwell time to effective information gain per unit visual cognitive load.",
    "slides.s18a.finding2.title": "Step-by-Step Analytic Progression",
    "slides.s18a.finding2.body": "Deconstructing baseline limits, textual stagnation trap, surprisal modeling, Markov flows, and empirical gains.",

    "slides.s18b.title": "Three Conventional Gaze Metrics and Their Assumptions",
    "slides.s18b.guide": "[Baseline Review] Summarizing the three dominant metrics in conventional signage eye-tracking",
    "slides.s18b.shortTitle": "Phase 4: Conventional Baseline",
    "slides.s18b.m1.title": "Dwell Time",
    "slides.s18b.m1.body": "Total duration or dwell percentage, assuming longer fixation implies higher visitor interest.",
    "slides.s18b.m2.title": "Fixation Count",
    "slides.s18b.m2.body": "Frequency of gaze points entering an AOI, assuming higher count denotes greater visual importance.",
    "slides.s18b.m3.title": "Gaze Heatmaps",
    "slides.s18b.m3.body": "Gaussian kernel density point clouds, assuming hotspot peaks mark core attractions.",
    "slides.s18b.finding1.title": "Limits of Conventional Metrics",
    "slides.s18b.finding1.body": "They record where eyes land in physical space, but cannot differentiate comprehension from stagnation.",
    "slides.s18b.finding2.title": "Flaw of the Homogeneous Time Axiom",
    "slides.s18b.finding2.body": "Assuming every millisecond delivers equal information value overlooks cognitive friction and struggle.",

    "slides.s18c.title": "The Long-Text Confounding: Cognitive Friction vs Reading",
    "slides.s18c.guide": "[Confounding Analysis] Revealing how dense academic text creates an illusion of high interest",
    "slides.s18c.shortTitle": "Phase 4: Cognitive Friction",
    "slides.s18c.c1.title": "Superficial Metric: 44.3% Text Dwell",
    "slides.s18c.c1.body": "Control signs exhibited highest dwell on body text, leading traditional models to falsely conclude high interest.",
    "slides.s18c.c2.title": "Cognitive Reality: Cognitive Friction & Stagnation",
    "slides.s18c.c2.body": "Dense Latin taxonomy caused cognitive overload and trapped scanning loops, reflecting friction rather than deep reading.",
    "slides.s18c.finding1.title": "Essence of the Textual Barrier",
    "slides.s18c.finding1.body": "Prolonged dwell in dense text indicates decoding struggle rather than high-value knowledge acquisition.",
    "slides.s18c.finding2.title": "Necessity of Methodological Turn",
    "slides.s18c.finding2.body": "Information entropy and Markov transition modeling are necessary to quantify genuine cognitive flow.",

    "slides.s18d.title": "Shannon Information Theory: Surprisal & Knowledge Gain",
    "slides.s18d.guide": "[Mathematical Modeling] Formulating self-information I = -log2(P) to weight sensory interaction value",
    "slides.s18d.shortTitle": "Phase 4: Surprisal Modeling",
    "slides.s18d.axiom": "'Information content is highest when violating expectations'",
    "slides.s18d.box1.title": "Conventional Taxonomy (High Prior · Low Bits)",
    "slides.s18d.box1.body": "'Bougainvillea is a woody vine in Nyctaginaceae from South America' — Generic prior knowledge with low information gain.",
    "slides.s18d.box2.title": "Sensory Touch Prompt (Low Prior · High Bits)",
    "slides.s18d.box2.body": "'The red parts are bracts, not petals! Touch their dry papery texture' — Violates prior assumptions and triggers deep encoding.",
    "slides.s18d.finding1.title": "Predictive Processing Mechanism",
    "slides.s18d.finding1.body": "The human cognitive system is exquisitely tuned to prioritize unexpected, embodied sensory stimuli.",
    "slides.s18d.finding2.title": "Theoretical Grounding of Principle R",
    "slides.s18d.finding2.body": "Principle R (Relevance/Embodied interaction) delivers high surprisal, fundamentally boosting knowledge efficiency.",

    "slides.s18e.title": "Markov Transition Matrix: Breaking 93% Text Loop",
    "slides.s18e.guide": "[Scanpath Dynamics] First-order Markov chain reveals gaze flow across functional AOIs",
    "slides.s18e.shortTitle": "Phase 4: Markov Flow",
    "slides.s18e.kpi.title": "Text Self-Loop Stagnation Rate",
    "slides.s18e.kpi.sub": "Markov matrix proves: Textual loop is broken, smoothly routing gaze into interactive zones (p < 0.001)",
    "slides.s18e.box1.title": "Control: Trapped in Text Loop (0.93)",
    "slides.s18e.box1.body": "Gaze remains trapped within dense text (93% self-loop), with only 4% transition to photos, forming a dead-end trap.",
    "slides.s18e.box2.title": "Intervention: Dynamic Multimodal Routing",
    "slides.s18e.box2.body": "Gaze flows organically from text to touch bubbles (0.19), icons (0.13), and flower meanings (0.38).",
    "slides.s18e.finding1.title": "Breakdown of the Reading Trap",
    "slides.s18e.finding1.body": "Co-created modular layout dissolves the gaze-absorbing trap of dense text and cuts redundant looping.",
    "slides.s18e.finding2.title": "Closed-Loop Multimodal Flow",
    "slides.s18e.finding2.body": "Passive single-zone stagnation transforms into proactive multi-point cross-modal exploration.",

    "slides.s18f.title": "Empirical Findings: Doubling of Cognitive Information Gain",
    "slides.s18f.guide": "[Empirical Proof] Full 13-participant paired tests confirm massive leap in E_gain and efficiency ratio",
    "slides.s18f.shortTitle": "Phase 4: Empirical Leap",
    "slides.s18f.kpi.title": "Total Effective Cognitive Gain (E_gain)",
    "slides.s18f.kpi.sub": "0.585 bits → 1.332 bits (p < 0.000001 ***) | All 13 participants showed monotonic increase",
    "slides.s18f.box1.title": "Massive Jump in Knowledge Absorption",
    "slides.s18f.box1.body": "Combining gaze duration with surprisal weights reveals a +127.7% increase in effective knowledge gain across all participants.",
    "slides.s18f.box2.title": "Significant Boost in Efficiency Ratio (η)",
    "slides.s18f.box2.body": "Efficiency ratio improved from 1.083 to 1.407 (+29.9%, p = 0.004), demonstrating higher cognitive yield per visual effort.",
    "slides.s18f.finding1.title": "Solid Information-Theoretic Support",
    "slides.s18f.finding1.body": "Mathematical modeling confirms that co-created signage simultaneously reduces cognitive burden and maximizes knowledge gain.",
    "slides.s18f.finding2.title": "Pillar for Doctoral Research",
    "slides.s18f.finding2.body": "High surprisal and fluent Markov flows lay the computational foundation for upcoming long-term retention experiments."
}

ja_keys = {
    "slides.s18a.title": "情報エントロピーとサプライザル理論による深化分析",
    "slides.s18a.guide": "【理論導入】滞在時間の表面指標を超え、真の知識獲得量と認知フローを定量化",
    "slides.s18a.shortTitle": "フェーズ4：情報エントロピー理論導入",
    "slides.s18a.q1.title": "長く見ること＝良いことか？",
    "slides.s18a.q1.body": "従来の視線指標は「滞在時間が長い＝関心が高い」と仮定していましたが、難解な長文による躊躇や停滞が深い読み込みと誤認されがちでした。",
    "slides.s18a.q2.title": "情報理論による真の獲得量計測",
    "slides.s18a.q2.body": "「情報は予想に反するときほど情報量が多い」というサプライザル理論に基づき、読者が吸収した有効情報量を厳密に定量化します。",
    "slides.s18a.finding1.title": "認知評価パラダイムの転換",
    "slides.s18a.finding1.body": "単なる滞在時間から、単位視覚負荷あたりの有効情報獲得量と動線の秩序性への移行。",
    "slides.s18a.finding2.title": "段階的分析フロー",
    "slides.s18a.finding2.body": "従来指標の限界 → 長文停滞トラップ → サプライザル数理モデル → マルコフ連鎖解明 → 実証的躍進結果へと展開。",

    "slides.s18b.title": "従来の視線三大標準指標とその前提仮定",
    "slides.s18b.guide": "【ベースライン整理】既存の解説サイン視線研究で汎用される三大指標体系の整理",
    "slides.s18b.shortTitle": "フェーズ4：従来指標の限界",
    "slides.s18b.m1.title": "注視時間 (Dwell Time)",
    "slides.s18b.m1.body": "各領域の合計秒数または時間比率。「長く留まる＝関心が高い」と暗黙に仮定。",
    "slides.s18b.m2.title": "注視回数 (Fixation Count)",
    "slides.s18b.m2.body": "視線が領域に入った回数。「回数が多い＝視覚的重要性が高い」と仮定。",
    "slides.s18b.m3.title": "ヒートマップ (Heatmap)",
    "slides.s18b.m3.body": "点密度の空間分布。「赤色の高密度エリア＝最も魅力的な焦点」と仮定。",
    "slides.s18b.finding1.title": "従来指標の限界性",
    "slides.s18b.finding1.body": "物理空間上の滞在位置を記録するのみで、注視の背後にある理解の質を弁別できません。",
    "slides.s18b.finding2.title": "均質時間仮定の欠陥",
    "slides.s18b.finding2.body": "すべての注視秒数が均等な情報価値を持つと前提し、認知摩擦による停滞を見落とします。",

    "slides.s18c.title": "従来指標の致命的誤解：深い理解ではなく認知受阻",
    "slides.s18c.guide": "【誤解解明】長大な専門文が高滞在時間の「見かけの繁栄」を生むメカニズム",
    "slides.s18c.shortTitle": "フェーズ4：認知受阻の罠",
    "slides.s18c.c1.title": "見かけの数値：説明文注視比率 44.3%",
    "slides.s18c.c1.body": "対照群では説明文の滞在時間が最上位を占め、従来モデルでは「読者が本文に最も関心を持った」と誤認されます。",
    "slides.s18c.c2.title": "真の認知実態：認知摩擦と停滞",
    "slides.s18c.c2.body": "難解な学名や専門用語により「読み進められず要点が掴めない」状態となり、視線が受動的に停滞しているに過ぎません。",
    "slides.s18c.finding1.title": "テキスト注視障壁の本質",
    "slides.s18c.finding1.body": "高い滞在時間は知識吸収ではなく情報デコードの摩擦（Cognitive Friction）を反映しています。",
    "slides.s18c.finding2.title": "方法論的転換の必然性",
    "slides.s18c.finding2.body": "情報量（Surprisal）と遷移秩序（Markov）を同時に計測できる情報論的手法が不可欠です。",

    "slides.s18d.title": "シャノン情報理論：予想に反する驚きが生む認知増益",
    "slides.s18d.guide": "【数理モデリング】自己情報量 I = -log2(P) を導入し五感身体連関の高価値を数式化",
    "slides.s18d.shortTitle": "フェーズ4：サプライザル数理モデル",
    "slides.s18d.axiom": "「情報は、予想に反するときほど、情報量が多い」",
    "slides.s18d.box1.title": "従来の専門文（高予測・低情報量）",
    "slides.s18d.box1.body": "「オシロイバナ科の熱帯花木で南米原産…」——読者の事前知識の範囲内であり、情報増分は僅か 0.42 bits。",
    "slides.s18d.box2.title": "五感身体連関（低予測・極高情報量）",
    "slides.s18d.box2.body": "「赤い部分は花びらではなく葉（苞）！触ってカサカサ感を体感」——常識を覆し、3.06 bits の高驚きを提供。",
    "slides.s18d.finding1.title": "予測符号化（Predictive Coding）",
    "slides.s18d.finding1.body": "人間の脳は事前予測を裏切る身体感覚的シグナルに対し、極めて高い符号化感度を発揮します。",
    "slides.s18d.finding2.title": "共創 R 原則の理論的根拠",
    "slides.s18d.finding2.body": "R 原則（身体・五感連関）が高サプライザル情報を注入することで、学習体験と効率を根本的に革新します。",

    "slides.s18e.title": "マルコフ遷移行列：93% の長文ループを打破",
    "slides.s18e.guide": "【動線解明】一次マルコフ連鎖により各機能領域間の視線流転秩序を可視化",
    "slides.s18e.shortTitle": "フェーズ4：マルコフ連鎖解明",
    "slides.s18e.kpi.title": "説明文自己ループ停滞率",
    "slides.s18e.kpi.sub": "マルコフ行列が実証：長文の閉塞ループが完全に打破され、視線が五感領域へ誘導 (p < 0.001)",
    "slides.s18e.box1.title": "対照群：長文ループに拘束 (0.93)",
    "slides.s18e.box1.body": "視線の 93% が説明文内部でループし、写真へ抜ける確率は僅か 4% で、閉塞したトラップを形成。",
    "slides.s18e.box2.title": "改良群：マルチモーダル自由流転",
    "slides.s18e.box2.body": "本文から五感フキダシ（0.19）、アイコン（0.13）、花言葉（0.38）へとスムーズに巡回するフローを確立。",
    "slides.s18e.finding1.title": "読書デッドロックの解体",
    "slides.s18e.finding1.body": "共創サインのモジュール配置が長文の視線拘束トラップを解消し、無駄な迷走を大幅に削減。",
    "slides.s18e.finding2.title": "多点探索の好循環",
    "slides.s18e.finding2.body": "受動的な単一領域停滞から、複数領域を自発的に巡る高効率な認知流へと移行しました。",

    "slides.s18f.title": "全量実証結果：有効認知情報吸収量が倍増",
    "slides.s18f.guide": "【全量検証】被験者全13名の対応のある検定により E_gain と効率比が劇的に向上",
    "slides.s18f.shortTitle": "フェーズ4：実証的躍進結果",
    "slides.s18f.kpi.title": "有効認知情報獲得総量 (E_gain)",
    "slides.s18f.kpi.sub": "0.585 bits → 1.332 bits (p < 0.000001 ***) | 被験者全13名全員が単調増加",
    "slides.s18f.box1.title": "真の知識獲得が 2.3 倍に飛躍",
    "slides.s18f.box1.body": "注視時間とサプライザル重みを統合した結果、有効知識獲得量が +127.7% 増加し、全13名で例外なく向上しました。",
    "slides.s18f.box2.title": "認知情報伝達効率比 (η) の向上",
    "slides.s18f.box2.body": "効率比が 1.083 から 1.407 へと +29.9% 有意に改善（p = 0.004）、より少ない視覚疲労で高品質な情報を獲得。",
    "slides.s18f.finding1.title": "共創原則への強力な理論的裏付け",
    "slides.s18f.finding1.body": "情報理論モデルにより、共創サインが認知負荷を下げつつ知識獲得を最大化することを数学的に証明。",
    "slides.s18f.finding2.title": "博士課程研究の理論的支柱",
    "slides.s18f.finding2.body": "高サプライザルと滑らかな動線遷移は、今後の二重符号化理論および長期記憶保持実験の強固な基盤となります。"
}

es_keys = {k: v for k, v in en_keys.items()} # 保证键集一致，占位

# 写入各字典文件
for lang, kdict in [('zh', zh_keys), ('en', en_keys), ('ja', ja_keys), ('es-MX', es_keys)]:
    fpath = os.path.join(I18N_DIR, f"{lang}.json")
    with open(fpath, 'r', encoding='utf-8') as f:
        d = json.load(f)
    d.update(kdict)
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"[*] {lang}.json 已更新，共 {len(d)} 个键")

