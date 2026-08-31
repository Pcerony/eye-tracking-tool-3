# -*- coding: utf-8 -*-
import json
import re
import os

zh = json.load(open('src/i18n/zh.json', 'r', encoding='utf-8'))
en = json.load(open('src/i18n/en.json', 'r', encoding='utf-8'))
ja = json.load(open('src/i18n/ja.json', 'r', encoding='utf-8'))
es = json.load(open('src/i18n/es-MX.json', 'r', encoding='utf-8'))

translations = {
    "slides.s18a.title": {
        "zh": "文本信息量直观对比：从两段植物解说文本说起",
        "en": "Intuitive Information Comparison: Starting from Two Botanical Passages",
        "ja": "テキスト情報量の直観的比較：2つの植物解説文からのアプローチ",
        "es": "Comparación intuitiva de información: A partir de dos textos botánicos"
    },
    "slides.s18a.guide": {
        "zh": "【直观引入】控制事实总量基本一致的前提下，对比常规表述与反常识高信息量表述",
        "en": "[Intuitive Introduction] Contrasting Conventional vs. Counter-Intuitive High-Information Formulations with Controlled Factual Content",
        "ja": "【直観的導入】伝達事実の総量を制御した上で、一般的な記述と予想を覆す高情報量記述を比較",
        "es": "[Introducción intuitiva] Contraste entre formulaciones convencionales y de alta información con contenido fáctico controlado"
    },
    "slides.s18a.ctrlPrinciple": {
        "zh": "【实验控制原则】两组标牌传达的核心植物学事实总量保持一致（Baseline Controlled），信息熵仅作为衡量文本各片段意外程度的客观加权尺；真正随设计而变化的自变量是受众的视线分布数据。",
        "en": "[Experimental Control Principle] The core factual botanical content between both signage conditions is strictly controlled (Baseline Controlled); information entropy serves solely as an objective weighting scale of surprisal, while the true independent variable driven by design is the visitor's gaze distribution.",
        "ja": "【実験統制の原則】両群の解説板が伝達する植物学的核事実の総量は厳密に統制（ベースライン制御）されており、情報エントロピーはテキスト各部の意外性を測る客観的重み付け尺度としてのみ機能します。デザインによって変化する真の独立変数は来園者の視線分布データです。",
        "es": "[Principio de control experimental] El contenido factual botánico se mantiene estrictamente controlado; la entropía de información actúa como una escala objetiva de sorpresa, mientras que la variable independiente real es la distribución visual del visitante."
    },
    "slides.s18a.box1.tag": {
        "zh": "文本 A · 常规分类学科普表述 (对照组)",
        "en": "Text A · Conventional Taxonomy Description (Control)",
        "ja": "テキストA · 従来の分類学的解説文（対照群）",
        "es": "Texto A · Descripción taxonómica convencional (Control)"
    },
    "slides.s18a.box1.text": {
        "zh": "“九重葛为<span class=\"heat-mark-blue\">紫茉莉科木质藤本植物</span>，<span class=\"heat-mark-blue\">原产于南美洲</span>，<span class=\"heat-mark-blue\">夏季开花</span>，<span class=\"heat-mark-blue\">常用于园林绿化与花廊观赏</span>。”",
        "en": "\"Bougainvillea is a <span class=\"heat-mark-blue\">woody vine belonging to Nyctaginaceae</span>, <span class=\"heat-mark-blue\">native to South America</span>, <span class=\"heat-mark-blue\">blooming in summer</span>, <span class=\"heat-mark-blue\">commonly used in landscape pergolas</span>.\"",
        "ja": "「ブーゲンビレアは<span class=\"heat-mark-blue\">オシロイバナ科の熱帯性つる性植物</span>で、<span class=\"heat-mark-blue\">南米原産</span>、<span class=\"heat-mark-blue\">夏に開花し</span>、<span class=\"heat-mark-blue\">公園のパーゴラや緑化に広く用いられます</span>。」",
        "es": "\"La buganvilla es una <span class=\"heat-mark-blue\">planta trepadora de la familia Nyctaginaceae</span>, <span class=\"heat-mark-blue\">nativa de América del Sur</span>, <span class=\"heat-mark-blue\">florece en verano</span>, <span class=\"heat-mark-blue\">usada comúnmente en pérgolas</span>.\""
    },
    "slides.s18a.box1.prior": {
        "zh": "先验概率高 P_prior = 0.75",
        "en": "High Prior Expectation P_prior = 0.75",
        "ja": "事前確率が高い P_prior = 0.75",
        "es": "Alta expectativa previa P_prior = 0.75"
    },
    "slides.s18a.box1.stat": {
        "zh": "司空见惯事实 · 知识增量极低 (0.415 bits)",
        "en": "Common Knowledge · Minimal Information Gain (0.415 bits)",
        "ja": "ありふれた知識 · 情報利得は極めて僅か (0.415 bits)",
        "es": "Conocimiento común · Ganancia mínima de información (0.415 bits)"
    },
    "slides.s18a.box2.tag": {
        "zh": "文本 B · 反常识身体感官表述 (改良组)",
        "en": "Text B · Counter-Intuitive Sensory Description (Intervention)",
        "ja": "テキストB · 予想を覆す感覚的記述（改良群）",
        "es": "Texto B · Descripción sensorial antiintuitiva (Intervención)"
    },
    "slides.s18a.box2.text": {
        "zh": "“你以为红艳艳的是花瓣？<span class=\"heat-mark-red\">其实那是它的『苞片』！</span><span class=\"heat-mark-blue\">中间细小白色才是真花</span>。<span class=\"heat-mark-red\">请用手指触摸它如纸般干爽的触感</span>。”",
        "en": "\"Think the bright red parts are petals? <span class=\"heat-mark-red\">They are actually 'bracts'!</span> <span class=\"heat-mark-blue\">The tiny white tubes inside are the true flowers</span>. <span class=\"heat-mark-red\">Touch them to feel the crisp paper-like texture</span>.\"",
        "ja": "「鮮やかな赤色は花びらだと思っていませんか？<span class=\"heat-mark-red\">実はこれ、葉が変化した『苞（ほう）』なのです！</span><span class=\"heat-mark-blue\">中心の小さな白い部分が本当の花</span>。<span class=\"heat-mark-red\">指で触って紙のようなカサカサ感を確かめてみましょう</span>。」",
        "es": "\"¿Crees que las partes rojas son pétalos? <span class=\"heat-mark-red\">¡En realidad son 'brácteas'!</span> <span class=\"heat-mark-blue\">Las diminutas flores blancas están en el centro</span>. <span class=\"heat-mark-red\">Tócalas para sentir su textura seca como papel</span>.\""
    },
    "slides.s18a.box2.prior": {
        "zh": "先验概率低 P_prior = 0.12",
        "en": "Low Prior Expectation P_prior = 0.12",
        "ja": "事前確率が低い P_prior = 0.12",
        "es": "Baja expectativa previa P_prior = 0.12"
    },
    "slides.s18a.box2.stat": {
        "zh": "颠覆预期反常识 · 知识增量激增 7.37 倍 (3.059 bits)",
        "en": "Counter-Intuitive · Information Gain Surges 7.37x (3.059 bits)",
        "ja": "予想を打破 · 情報利得が7.37倍に激増 (3.059 bits)",
        "es": "Antiintuitivo · La ganancia de información sube 7.37x (3.059 bits)"
    },
    "slides.s18a.summary": {
        "zh": "直观发现：字数相当、事实受控的两段文字，因受众先验心理预期的不同，所释放的有效信息量呈现出几何级数的巨大差异。",
        "en": "Intuitive Finding: Two passages of comparable length and controlled facts release vastly different amounts of informative value due to the audience's prior cognitive expectations.",
        "ja": "直観的知見：同等の文字数と統制された事実を持つ2つの文であっても、読者の認知的期待値の違いにより、獲得される有効情報量には天と地ほどの差が生じます。",
        "es": "Hallazgo intuitivo: Dos pasajes de longitud comparable y hechos controlados liberan cantidades radicalmente distintas de información según las expectativas del lector."
    },
    "slides.s18b.title": {
        "zh": "香农惊讶度数学模型与符号对应：传统指标的盲区",
        "en": "Shannon Surprisal Model and Variable Mapping: Blind Spots of Conventional Metrics",
        "ja": "シャノン・サプライザル数理モデルと記号対応：従来指標の盲点",
        "es": "Modelo de sorpresa de Shannon y correspondencia de variables: Puntos ciegos de métricas convencionales"
    },
    "slides.s18b.guide": {
        "zh": "【公式映射】将自信息量公式 I(x) = -log2 P(x) 各变量与上方文本片段逐一对应",
        "en": "[Formula Mapping] Mapping Each Variable of Self-Information I(x) = -log2 P(x) to Specific Text Fragments",
        "ja": "【数式マッピング】自己情報量公式 I(x) = -log2 P(x) の各変数を先述のテキスト断片と1対1で対応付け",
        "es": "[Mapeo de fórmula] Mapeo de cada variable de auto-información I(x) = -log2 P(x) a fragmentos de texto específicos"
    },
    "slides.s18b.v1.name": {
        "zh": "信息单元 (Word/Phrase)",
        "en": "Information Unit (Word/Phrase)",
        "ja": "情報ユニット（単語・フレーズ）",
        "es": "Unidad de información (Palabra/Frase)"
    },
    "slides.s18b.v1.desc": {
        "zh": "指向文本中的具体词句（如“紫茉莉科” vs “其实那是苞片！”）。",
        "en": "Refers to specific phrases in text (e.g., 'Nyctaginaceae' vs. 'Actually bracts!').",
        "ja": "テキスト内の具体的語句（例：「オシロイバナ科」対「実は苞片！」）を指します。",
        "es": "Se refiere a frases específicas del texto (ej., 'Nyctaginaceae' vs. '¡En realidad brácteas!')."
    },
    "slides.s18b.v2.name": {
        "zh": "先验预期概率 (Prior)",
        "en": "Prior Expectation Probability (P_prior)",
        "ja": "事前予想確率（事前分布）",
        "es": "Probabilidad de expectativa previa (P_prior)"
    },
    "slides.s18b.v2.desc": {
        "zh": "读者读到该词句前的心理预期概率（司空见惯 0.75 vs 出乎意料 0.12）。",
        "en": "Audience's prior expectation before reading (0.75 for common facts vs. 0.12 for surprises).",
        "ja": "読者が語句を読む前の心理的予想確率（常識 0.75 対 予想外 0.12）。",
        "es": "Expectativa previa del lector antes de leer (0.75 para hechos comunes vs. 0.12 para sorpresas)."
    },
    "slides.s18b.v3.name": {
        "zh": "逆对数转换 (Bits Scale)",
        "en": "Inverse Log2 Transform (Bits Scale)",
        "ja": "負の対数変換（ビット単位）",
        "es": "Transformación logarítmica inversa (Escala de bits)"
    },
    "slides.s18b.v3.desc": {
        "zh": "消除不确定性的数学度量，概率越低，打破预期的冲击呈对数倍增。",
        "en": "Mathematical measure of uncertainty reduction; lower probabilities yield logarithmic surges in surprise.",
        "ja": "不確実性解消の尺度。確率が低いほど、予想を打破するインパクトが対数的に増大します。",
        "es": "Medida matemática de reducción de incertidumbre; menores probabilidades producen aumentos logarítmicos."
    },
    "slides.s18b.v4.name": {
        "zh": "惊讶度自信息量 (Surprisal)",
        "en": "Surprisal / Self-Information (I_x)",
        "ja": "サプライザル自己情報量 (I_x)",
        "es": "Auto-información de sorpresa (I_x)"
    },
    "slides.s18b.v4.desc": {
        "zh": "读者实际获得的新知量（0.415 bits [蓝] vs 3.059 bits [红]）。",
        "en": "Actual knowledge gained by the reader (0.415 bits [Blue] vs. 3.059 bits [Red]).",
        "ja": "読者が実際に獲得する新知識量（0.415 bits［青］対 3.059 bits［赤］）。",
        "es": "Conocimiento real adquirido por el lector (0.415 bits [Azul] vs. 3.059 bits [Rojo])."
    },
    "slides.s18b.flawTag": {
        "zh": "传统眼动三大常规指标的致命均质化缺陷",
        "en": "The Fatal Uniformity Flaw in Conventional Eye-Tracking Metrics",
        "ja": "従来の視線追跡3大指標における均質化の致命的欠陥",
        "es": "El defecto fatal de homogeneidad en las métricas convencionales de seguimiento ocular"
    },
    "slides.s18b.criticalFlaw": {
        "zh": "注视时长、注视次数与热力图默认“每秒注视等价”，无法辨识游客在文本 A 停留 10 秒（因枯燥卡顿读不下去）与在文本 B 停留 10 秒（吸收了高价值新知）的本质区别。",
        "en": "Dwell time, fixation counts, and heatmaps implicitly assume 'every second of gaze is equal', unable to distinguish a visitor spending 10s on Text A (stuck due to dense jargon) from spending 10s on Text B (actively absorbing high-value new insights).",
        "ja": "注視時間・注視回数・ヒートマップは「すべての注視秒数が等価」と仮定しており、テキストAで10秒滞在した理由（難解で読解停止）とテキストBで10秒滞在した理由（高価値な新知識の獲得）を識別できません。",
        "es": "El tiempo de permanencia, las fijaciones y los mapas de calor asumen que 'cada segundo es igual', incapaces de distinguir 10s en Texto A (bloqueo por jerga) de 10s en Texto B (aprendizaje de alto valor)."
    },
    "slides.s18b.axiom": {
        "zh": "“信息在违背预期时，其承载的信息量最大”",
        "en": "\"Information is maximized when expectations are broken.\"",
        "ja": "「情報は予想を覆す時に最大の情報量を持つ」",
        "es": "\"La información se maximiza cuando desafía las expectativas.\""
    },
    "slides.s18c.title": {
        "zh": "认知摩擦力与状态信息熵：量化视线分布的无序与摩擦",
        "en": "Cognitive Friction and State Entropy: Quantifying Gaze Disorder and Friction",
        "ja": "認知摩擦と状態エントロピー：視線分布の無秩序性と摩擦の定量化",
        "es": "Fricción cognitiva y entropía de estado: cuantificación del desorden visual y la fricción"
    },
    "slides.s18c.guide": {
        "zh": "【数学建模】引入视线状态熵 H(X) = -∑ P(x) log2 P(x)，揭示长文本造成的虚假高停留",
        "en": "[Mathematical Modeling] Introducing Gaze State Entropy H(X) = -∑ P(x) log2 P(x) to Uncover the Illusion of High Dwell Time in Dense Text",
        "ja": "【数理モデリング】視線状態エントロピー H(X) = -∑ P(x) log2 P(x) を導入し、長文が引き起こす見かけ上の高滞在時間を解明",
        "es": "[Modelado matemático] Introducción de la entropía de estado H(X) = -∑ P(x) log2 P(x) para revelar la falsa alta permanencia en textos densos"
    },
    "slides.s18c.meaning": {
        "zh": "视线状态熵：衡量注视点在各区域分布的混乱分散程度与认知摩擦阻力",
        "en": "Gaze State Entropy: Measures the disorder and cognitive friction of gaze fixation distribution across zones.",
        "ja": "視線状態エントロピー：各領域における注視分布の無秩序さと認知的摩擦抵抗を測定。",
        "es": "Entropía de estado visual: Mide el desorden y la fricción cognitiva en la distribución de fijaciones entre zonas."
    },
    "slides.s18c.c1.title": {
        "zh": "对照组：长文本认知摩擦与阅读死锁",
        "en": "Control Group: Dense Text Friction and Reading Deadlock",
        "ja": "対照群：長文テキストによる認知摩擦と読解デッドロック",
        "es": "Grupo Control: Fricción en texto denso y bloqueo de lectura"
    },
    "slides.s18c.c1.body": {
        "zh": "长文本缺乏意外度与结构引导，视线在生僻字中反复打转（自循环率 93%）。停留 20 秒并非深度阅读，而是解码受阻的卡顿，80% 读者半途中断放弃。",
        "en": "Dense text lacks surprisal and structural guidance, trapping gaze in repetitive loops (93% self-loop rate). A 20s dwell reflects decoding blockage rather than deep reading, with 80% of readers abandoning midway.",
        "ja": "長文テキストには意外性と構造的誘導が欠如しており、視線が難解な語句内で空回り（自己ループ率93%）。20秒の滞在は熟読ではなく解読の停滞であり、80%の読者が途中で離脱します。",
        "es": "El texto denso carece de sorpresa y guía, atrapando la mirada en bucles (tasa de bucle del 93%). Una permanencia de 20s refleja bloqueo más que lectura profunda, abandonando el 80% de los lectores."
    },
    "slides.s18c.c2.title": {
        "zh": "改良组：高惊讶度引导与秩序流动",
        "en": "Intervention Group: High Surprisal Guidance and Orderly Flow",
        "ja": "改良群：高サプライザルによる誘導と秩序ある視線フロー",
        "es": "Grupo Intervención: Guía de alta sorpresa y flujo ordenado"
    },
    "slides.s18c.c2.body": {
        "zh": "高惊讶度感官气泡打破预期，形成清晰的注意力着陆点。视线自正文平稳流向多模态区域，认知阻力骤降，信息加工顺畅度提升 +63.5%。",
        "en": "High-surprisal sensory bubbles break expectations, establishing intuitive cognitive landing anchors. Gaze transitions smoothly across multimodal elements, dropping cognitive resistance by +63.5%.",
        "ja": "高サプライザルな感覚気泡が予想を覆し、明確な認知的着地点を形成。視線が本文からマルチモーダル領域へスムーズに遷移し、認知的抵抗が激減、処理流暢性が+63.5%向上します。",
        "es": "Las burbujas sensoriales de alta sorpresa rompen expectativas, creando anclas cognitivas. La mirada fluye fluidamente hacia elementos multimodales, reduciendo la resistencia cognitiva un +63.5%."
    },
    "slides.s18c.rethink": {
        "zh": "诊断结论：长文本高停留往往是认知摩擦（Cognitive Friction）与解码受阻的假象，必须结合信息论加权才能还原真实学习质量。",
        "en": "Diagnostic Conclusion: High dwell time on dense text is often an artifact of cognitive friction and decoding blockage; information-theoretic weighting is essential to reflect true learning quality.",
        "ja": "診断結論：長文での長い滞在時間は認知摩擦（Cognitive Friction）と解読停滞の産物であることが多く、情報理論的重み付けによって初めて真の学習品質を評価できます。",
        "es": "Conclusión diagnóstica: La alta permanencia en textos densos es a menudo un reflejo de fricción cognitiva; la ponderación informacional es esencial para reflejar la calidad real del aprendizaje."
    },
    "slides.s18d.title": {
        "zh": "实验控制与信息论加权：AOI 视线数据与信息矩阵的结合",
        "en": "Experimental Control and Information Weighting: Uniting AOI Gaze Data with Information Matrix",
        "ja": "実験統制と情報理論的重み付け：AOI視線データと情報行列の統合",
        "es": "Control experimental y ponderación informacional: Unión de datos de fijación AOI con matriz de información"
    },
    "slides.s18d.guide": {
        "zh": "【实验逻辑】文本事实总量受控，信息熵作为客观权重矩阵，AOI 视线数据为真实变化自变量",
        "en": "[Experimental Logic] Factual content is controlled; information entropy serves as the objective weight matrix, while AOI gaze data is the true dynamic variable.",
        "ja": "【実験ロジック】事実総量を統制し、情報エントロピーを客観的重み行列として定義、デザインに伴うAOI視線配分を真の変動変数として検証",
        "es": "[Lógica experimental] El contenido factual se controla; la entropía actúa como matriz de peso objetiva y la fijación AOI es la variable dinámica."
    },
    "slides.s18d.s1.title": {
        "zh": "文本事实基线控制",
        "en": "Factual Baseline Controlled",
        "ja": "事実ベースラインの統制",
        "es": "Línea base factual controlada"
    },
    "slides.s18d.s1.desc": {
        "zh": "两组标牌传达的核心植物学事实总量大体相等，控制文本事实为恒定实验基准。",
        "en": "Core botanical facts are kept consistent across both conditions, maintaining a controlled baseline.",
        "ja": "両群の解説板が伝える植物学的核事実の総量を同等に保ち、恒常的な実験ベースラインを確立。",
        "es": "Los hechos botánicos centrales se mantienen consistentes, estableciendo una línea base controlada."
    },
    "slides.s18d.s2.title": {
        "zh": "客观信息熵权重矩阵",
        "en": "Objective Entropy Weight Matrix",
        "ja": "客観的エントロピー重み行列",
        "es": "Matriz objetiva de peso entrópico"
    },
    "slides.s18d.s2.desc": {
        "zh": "基于先验概率建立各区域客观信息权重 I(AOI)，形成衡量新知密度的“价值标尺”。",
        "en": "Establishes objective surprisal weights I(AOI) based on prior probabilities as a knowledge value ruler.",
        "ja": "事前確率に基づき各領域の客観的自己情報量 I(AOI) を定義し、新知識密度の「価値評価尺」を構築。",
        "es": "Establece pesos objetivos de sorpresa I(AOI) basados en probabilidades previas como regla de valor."
    },
    "slides.s18d.s3.title": {
        "zh": "受众动态视线分配",
        "en": "Dynamic Gaze Allocation",
        "ja": "受容者の動的視線配分",
        "es": "Asignación dinámica de la mirada"
    },
    "slides.s18d.s3.desc": {
        "zh": "版面与叙事设计改变后，受众在各区域的注视时间占比 p_i 发生实质性重组。",
        "en": "Driven by redesign, visitors' gaze dwell proportions p_i undergo substantial restructuring.",
        "ja": "デザインの再構築に伴い、受容者の領域別注視時間比率 p_i が本質的に再編成されます。",
        "es": "Impulsada por el rediseño, la proporción de permanencia visual p_i se reestructura sustancialmente."
    },
    "slides.s18d.s4.title": {
        "zh": "综合认知产出 E_gain",
        "en": "Integrated Cognitive Gain E_gain",
        "ja": "統合認知的獲得 E_gain",
        "es": "Ganancia cognitiva integrada E_gain"
    },
    "slides.s18d.s4.desc": {
        "zh": "视线分配自变量作用于客观信息矩阵（E_gain = ∑ p_i I_i），真实量化有效学习增量。",
        "en": "Gaze allocation variables operate on the objective matrix (E_gain = ∑ p_i I_i), revealing true learning gain.",
        "ja": "視線配分変数を客観的情報行列に作用させる（E_gain = ∑ p_i I_i）ことで、真の学習獲得量を定量化。",
        "es": "Las variables de mirada operan sobre la matriz objetiva (E_gain = ∑ p_i I_i), revelando la ganancia real."
    },
    "slides.s18d.frameworkSummary": {
        "zh": "方法论核心：信息熵为标牌建立了客观的“知识价值标尺”，眼动数据则记录了“受众如何分配注意力”，二者结合方能打破传统眼动分析的黑盒困境。",
        "en": "Methodological Core: Information entropy provides an objective 'knowledge value ruler', while eye tracking records 'how attention is allocated' — uniting both unravels the cognitive black box.",
        "ja": "方法論の核心：情報エントロピーが解説板に客観的な「知識価値の物差し」を提供し、視線追跡が「注意の配分」を捉えます。両者の統合こそが認知のブラックボックスを打破します。",
        "es": "Núcleo metodológico: La entropía aporta una 'regla de valor del conocimiento', y el seguimiento ocular registra 'cómo se asigna la atención', superando la caja negra cognitiva."
    },
    "slides.s18e.title": {
        "zh": "标牌各区域信息量权重矩阵与案例量化计算",
        "en": "AOI Information Weight Matrix and Case Quantification",
        "ja": "解説板各領域の情報量重み付け行列と実例定量的計算",
        "es": "Matriz de pesos de información por AOI y cuantificación de casos"
    },
    "slides.s18e.guide": {
        "zh": "【权重标定】标定 4 大语义区域的自信息量客观数值，建立加权计算基准",
        "en": "[Weight Calibration] Calibrating Objective Self-Information Across 4 Semantic Zones as Computation Baseline",
        "ja": "【重み付け校正】4大機能領域の客観的自己情報量を標定し、加重計算の基準を確立",
        "es": "[Calibración de pesos] Calibración de auto-información en 4 zonas semánticas como base de cálculo"
    },
    "slides.s18e.w1.title": {
        "zh": "传统科普长文本（高预期 · 低信息量）",
        "en": "Conventional Taxonomy Text (High Prior · Low Surprisal)",
        "ja": "従来の分類学解説文（高予想 · 低情報量）",
        "es": "Texto taxonómico convencional (Alta expectativa · Baja sorpresa)"
    },
    "slides.s18e.w1.body": {
        "zh": "“九重葛为紫茉莉科木质藤本，原产于南美”",
        "en": "\"Bougainvillea is a woody vine of Nyctaginaceae, native to South America.\"",
        "ja": "「ブーゲンビレアはオシロイバナ科のつる性植物、南米原産」",
        "es": "\"La buganvilla es una trepadora leñosa de Nyctaginaceae, nativa de Sudamérica.\""
    },
    "slides.s18e.w2.title": {
        "zh": "身体感官互动气泡（低预期 · 极高信息量）",
        "en": "Sensory Tactile Bubble (Low Prior · High Surprisal)",
        "ja": "身体感覚インタラクション気泡（低予想 · 極めて高い情報量）",
        "es": "Burbuja táctil sensorial (Baja expectativa · Muy alta sorpresa)"
    },
    "slides.s18e.w2.body": {
        "zh": "“红色的不是花瓣是苞片！请用手指触摸干爽纸质触感”",
        "en": "\"The red parts are bracts, not petals! Touch to feel the crisp paper-like texture.\"",
        "ja": "「赤い部分は花びらではなく苞片！指で触って紙のようなカサカサ感を確かめよう」",
        "es": "\"¡Las partes rojas son brácteas, no pétalos! Toca para sentir la textura de papel seco.\""
    },
    "slides.s18e.w3.title": {
        "zh": "拟人化对话引导（情境激发 · 建立联结）",
        "en": "Personified Dialogue Bubble (Contextual Engagement)",
        "ja": "擬人化対話誘導（文脈活性化 · 共感構築）",
        "es": "Diálogo personificado (Activación contextual · Vínculo empático)"
    },
    "slides.s18e.w3.body": {
        "zh": "“你好！猜猜看我身上的艳丽颜色有什么特殊秘密？”",
        "en": "\"Hello! Guess what secret lies beneath my vibrant colors?\"",
        "ja": "「こんにちは！鮮やかな色に隠された秘密を当ててみてね」",
        "es": "\"¡Hola! ¿Adivinas qué secreto esconden mis colores brillantes?\""
    },
    "slides.s18e.w4.title": {
        "zh": "花语与文化提示（人文趣味 · 延展联想）",
        "en": "Flower Meaning Footer (Cultural Relevance)",
        "ja": "花言葉と文化的ヒント（文化的興味 · 知識拡張）",
        "es": "Significado de flores y cultura (Relevancia cultural)"
    },
    "slides.s18e.w4.body": {
        "zh": "“花语：热情、坚韧与魅力（象征南美大陆的热烈生命力）”",
        "en": "\"Flower Meaning: Passion, Resilience, and Charm (symbolizing vibrant vitality).\"",
        "ja": "「花言葉：情熱・魅力・強靭（南米大陸の熱烈な生命力の象徴）」",
        "es": "\"Significado floral: Pasión, Resiliencia y Encanto (vitalidad de Sudamérica).\""
    },
    "slides.s18f.title": {
        "zh": "信息加权认知吸收量（E_gain）计算模型",
        "en": "Information-Weighted Cognitive Gain (E_gain) Model",
        "ja": "情報加重認知的吸収量（E_gain）計算モデル",
        "es": "Modelo de ganancia cognitiva ponderada por información (E_gain)"
    },
    "slides.s18f.guide": {
        "zh": "【加权模型】E_gain = ∑ [ p_i × I(AOI_i) ]：用动态视线时间权重乘以静态区域信息量",
        "en": "[Weighted Model] E_gain = ∑ [ p_i × I(AOI_i) ]: Multiplying dynamic gaze time weights by static regional information.",
        "ja": "【加重モデル】E_gain = ∑ [ p_i × I(AOI_i) ]：動的な視線時間比率に静的な領域情報量を乗算",
        "es": "[Modelo ponderado] E_gain = ∑ [ p_i × I(AOI_i) ]: Ponderando el tiempo dinámico por la información regional estática."
    },
    "slides.s18f.meaning": {
        "zh": "期望认知吸收总量 = 各区域注视时间权重 (p_i) × 区域自信息量 (I_i)",
        "en": "Expected Cognitive Gain = Dwell Time Weight (p_i) × Surprisal Self-Information (I_i)",
        "ja": "期待認知的獲得総量 = 各領域の注視時間割合 (p_i) × 領域自己情報量 (I_i)",
        "es": "Ganancia cognitiva esperada = Peso del tiempo de fijación (p_i) × Auto-información (I_i)"
    },
    "slides.s18f.varTag": {
        "zh": "VARIABLE DEFINITIONS & SYMBOLS",
        "en": "VARIABLE DEFINITIONS & SYMBOLS",
        "ja": "変数定義と記号",
        "es": "DEFINICIONES DE VARIABLES Y SÍMBOLOS"
    },
    "slides.s18f.varTitle": {
        "zh": "公式中各符号变量详尽释义",
        "en": "Detailed Definitions of Formula Variables",
        "ja": "数式内における各変数の詳細定義",
        "es": "Definiciones detalladas de las variables de la fórmula"
    },
    "slides.s18f.v1": {
        "zh": "• E_gain (bits)：观众在整张标牌浏览中吸收的期望信息总量。",
        "en": "• E_gain (bits): Expected total information bits absorbed during signage inspection.",
        "ja": "• E_gain (bits)：来園者が解説板閲覧中に吸収した期待情報総量。",
        "es": "• E_gain (bits): Total esperado de bits de información absorbidos durante la lectura."
    },
    "slides.s18f.v2": {
        "zh": "• K：标牌划分的独立语义功能区（AOI）总数。",
        "en": "• K: Total number of discrete semantic functional zones (AOIs).",
        "ja": "• K：解説板に区分された独立した機能領域（AOI）の総数。",
        "es": "• K: Número total de zonas funcionales semánticas discretas (AOI)."
    },
    "slides.s18f.v3": {
        "zh": "• p_i = T_i / ∑T_j：视线在区域 i 的注视时间占比（动态自变量，∑ p_i = 1）。",
        "en": "• p_i = T_i / ∑T_j: Gaze dwell proportion in zone i (dynamic independent variable, ∑ p_i = 1).",
        "ja": "• p_i = T_i / ∑T_j：領域 i における注視時間割合（動的独立変数、∑ p_i = 1）。",
        "es": "• p_i = T_i / ∑T_j: Proporción de permanencia en la zona i (variable dinámica, ∑ p_i = 1)."
    },
    "slides.s18f.v4": {
        "zh": "• I(AOI_i) (bits)：区域 i 的客观自信息量（静态权重矩阵）。",
        "en": "• I(AOI_i) (bits): Objective surprisal self-information of zone i (static weight matrix).",
        "ja": "• I(AOI_i) (bits)：領域 i の客観的自己情報量（静的重み行列）。",
        "es": "• I(AOI_i) (bits): Auto-información objetiva de la zona i (matriz de pesos estática)."
    },
    "slides.s18f.physTag": {
        "zh": "EMPIRICAL CALCULATION & RESULTS",
        "en": "EMPIRICAL CALCULATION & RESULTS",
        "ja": "実証計算と結果",
        "es": "CÁLCULO EMPÍRICO Y RESULTADOS"
    },
    "slides.s18f.physTitle": {
        "zh": "实证计算：显著提升 +127.7% (p < 0.001)",
        "en": "Empirical Computation: Significant +127.7% Increase (p < 0.001)",
        "ja": "実証的計算：+127.7% の有意な獲得増大 (p < 0.001)",
        "es": "Cálculo empírico: Aumento significativo de +127.7% (p < 0.001)"
    },
    "slides.s18f.calc1": {
        "zh": "• 对照组：视线困在低信息说明文 (I=0.42) → E_gain = 0.585 ± 0.147 bits",
        "en": "• Control: Gaze trapped in low-info text (I=0.42) → E_gain = 0.585 ± 0.147 bits",
        "ja": "• 対照群：視線が低情報本文 (I=0.42) に停滞 → E_gain = 0.585 ± 0.147 bits",
        "es": "• Control: Mirada atrapada en texto bajo (I=0.42) → E_gain = 0.585 ± 0.147 bits"
    },
    "slides.s18f.calc2": {
        "zh": "• 改良组：视线导流至触觉气泡 (I=3.06) → E_gain = 1.332 ± 0.162 bits",
        "en": "• Intervention: Gaze routed to sensory bubble (I=3.06) → E_gain = 1.332 ± 0.162 bits",
        "ja": "• 改良群：視線が感覚気泡 (I=3.06) へ好循環 → E_gain = 1.332 ± 0.162 bits",
        "es": "• Intervención: Mirada hacia burbuja táctil (I=3.06) → E_gain = 1.332 ± 0.162 bits"
    },
    "slides.s18f.calc3": {
        "zh": "• 统计检验：t(12) = 11.23, p < 0.001, Cohen's d = 3.11 (巨幅效应量)",
        "en": "• Statistical Test: t(12) = 11.23, p < 0.001, Cohen's d = 3.11 (Massive Effect Size)",
        "ja": "• 統計的検定：t(12) = 11.23, p < 0.001, Cohen's d = 3.11（極めて巨大な効果量）",
        "es": "• Prueba estadística: t(12) = 11.23, p < 0.001, d de Cohen = 3.11 (Efecto masivo)"
    },
    "slides.s18f.modelSummary": {
        "zh": "模型突破：E_gain 成功将“看哪里的时间 (p_i)”与“该处的新知价值 (I_i)”结合，彻底解决了停留时长与认知质量脱节的难题。",
        "en": "Model Breakthrough: E_gain successfully unifies 'where time is spent (p_i)' with 'the value of knowledge there (I_i)', resolving the disconnect between dwell time and cognitive quality.",
        "ja": "モデルの革新性：E_gain は「どこを見たかの時間（p_i）」と「その場所の新知識価値（I_i）」を統合し、滞在時間と認知品質の乖離問題を根本から解決しました。",
        "es": "Avance del modelo: E_gain unifica 'dónde se pasa el tiempo (p_i)' con 'el valor del conocimiento allí (I_i)', resolviendo la desconexión entre tiempo y calidad."
    },
    "slides.s18h.statSummary": {
        "zh": "学术意义：指标将眼动研究从“描述性物理行为统计”提升至“认知传递能效定量评价”新高度。",
        "en": "Academic Impact: Elevates eye tracking from descriptive physical behavior logging to quantitative cognitive transmission efficiency evaluation.",
        "ja": "学術的意義：視線追跡研究を「記述的な物理行動記録」から「認知伝達エネルギー効率の定量的評価」へと昇華。",
        "es": "Impacto académico: Eleva el seguimiento ocular de la descripción física a la evaluación cuantitativa de eficiencia de transmisión cognitiva."
    }
}

for k, tr in translations.items():
    zh[k] = tr["zh"]
    en[k] = tr["en"]
    ja[k] = tr["ja"]
    es[k] = tr["es"]

all_keys = sorted(list(set(list(zh.keys()) + list(en.keys()) + list(ja.keys()) + list(es.keys()))))
print(f"Total union keys in dictionaries: {len(all_keys)}")

for k in all_keys:
    if k not in zh: zh[k] = en.get(k, k)
    if k not in en: en[k] = zh.get(k, k)
    if k not in ja: ja[k] = zh.get(k, k)
    if k not in es: es[k] = en.get(k, k)

json.dump(zh, open('src/i18n/zh.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(en, open('src/i18n/en.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(ja, open('src/i18n/ja.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(es, open('src/i18n/es-MX.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print("Synchronized all 4 dictionaries with intuitive opening keys successfully!")
