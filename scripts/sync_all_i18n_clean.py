# -*- coding: utf-8 -*-
import json
import re
import os

zh = json.load(open('src/i18n/zh.json', 'r', encoding='utf-8'))
en = json.load(open('src/i18n/en.json', 'r', encoding='utf-8'))
ja = json.load(open('src/i18n/ja.json', 'r', encoding='utf-8'))
es = json.load(open('src/i18n/es-MX.json', 'r', encoding='utf-8'))

clean_translations = {
    # Slide 20 (s18a)
    "slides.s18a.title": {
        "zh": "文本信息量对比",
        "en": "Information Density Comparison",
        "ja": "テキスト情報量の比較",
        "es": "Comparación de densidad de información"
    },
    "slides.s18a.guide": {
        "zh": "控制事实总量一致的前提下，常规表述与反常识表述的信息量差异",
        "en": "Information disparity between conventional and counter-intuitive formulations with controlled facts",
        "ja": "事実総量を統制した条件下における、通常記述と予想外記述の情報量格差",
        "es": "Disparidad informacional entre formulaciones convencionales y antiintuitivas con hechos controlados"
    },
    "slides.s18a.c1.tag": {
        "zh": "对照组 · 常规表述",
        "en": "Control · Conventional Formulation",
        "ja": "対照群 · 従来の通常記述",
        "es": "Control · Formulación convencional"
    },
    "slides.s18a.c1.p1": {
        "zh": "九重葛为",
        "en": "Bougainvillea is a ",
        "ja": "ブーゲンビレアは",
        "es": "La buganvilla es "
    },
    "slides.s18a.c1.h1": {
        "zh": "紫茉莉科木质藤本",
        "en": "woody vine of Nyctaginaceae",
        "ja": "オシロイバナ科の熱帯性つる植物",
        "es": "trepadora leñosa de Nyctaginaceae"
    },
    "slides.s18a.c1.p2": {
        "zh": "，原产于南美洲，夏季开花。",
        "en": ", native to South America, blooming in summer.",
        "ja": "で、南米原産、夏に開花します。",
        "es": ", nativa de Sudamérica, florece en verano."
    },
    "slides.s18a.c1.desc": {
        "zh": "先验概率高 P=0.75\n司空见惯事实 · 知识增量极低",
        "en": "High Prior P=0.75\nCommon Fact · Minimal Information Gain",
        "ja": "事前確率が高い P=0.75\nありふれた常識 · 情報獲得量は僅少",
        "es": "Alta expectativa previa P=0.75\nHecho común · Ganancia mínima"
    },
    "slides.s18a.c2.tag": {
        "zh": "改良组 · 感官表述",
        "en": "Intervention · Sensory Formulation",
        "ja": "改良群 · 感覚的記述",
        "es": "Intervención · Formulación sensorial"
    },
    "slides.s18a.c2.p1": {
        "zh": "红色的",
        "en": "The red parts ",
        "ja": "鮮やかな赤色は",
        "es": "Las partes rojas "
    },
    "slides.s18a.c2.h1": {
        "zh": "不是花瓣是苞片！",
        "en": "are bracts, not petals! ",
        "ja": "花ではなく苞片です！",
        "es": "¡son brácteas, no pétalos! "
    },
    "slides.s18a.c2.p2": {
        "zh": "请用手触摸",
        "en": "Touch to feel the ",
        "ja": "指で触って",
        "es": "Tócalas para sentir "
    },
    "slides.s18a.c2.h2": {
        "zh": "干爽纸质触感",
        "en": "crisp paper-like texture",
        "ja": "カサカサした紙の感触",
        "es": "la textura de papel seco"
    },
    "slides.s18a.c2.desc": {
        "zh": "先验概率低 P=0.12\n颠覆预期反常识 · 知识增量 7.37 倍",
        "en": "Low Prior P=0.12\nCounter-Intuitive · 7.37x Information Gain",
        "ja": "事前確率が低い P=0.12\n予想を覆す新知 · 情報獲得量7.37倍",
        "es": "Baja expectativa previa P=0.12\nAntiintuitivo · Ganancia 7.37x"
    },
    "slides.s18a.summary": {
        "zh": "字数相当、事实受控的前提下，反常识表述所释放的有效信息量激增 7.37 倍。",
        "en": "With controlled facts and equal length, counter-intuitive phrasing boosts effective information gain by 7.37x.",
        "ja": "事実総量と文字数が同等であっても、予想を打破する記述により有効情報量は7.37倍に激増します。",
        "es": "Con hechos controlados y longitud igual, la formulación antiintuitiva multiplica la información útil por 7.37x."
    },

    # Slide 21 (s18b)
    "slides.s18b.title": {
        "zh": "香农惊讶度数学模型",
        "en": "Shannon Surprisal Mathematical Model",
        "ja": "シャノン・サプライザル数理モデル",
        "es": "Modelo matemático de sorpresa de Shannon"
    },
    "slides.s18b.guide": {
        "zh": "衡量信息打破读者先验预期的程度，以及传统眼动指标的均质化缺陷",
        "en": "Quantifying expectation reduction and the uniformity flaw in traditional eye-tracking metrics",
        "ja": "読者の事前予想を打破する度合いの測定と、従来の視線追跡指標が抱える均質化の欠陥",
        "es": "Cuantificación de reducción de expectativas y el defecto de uniformidad en métricas tradicionales"
    },
    "slides.s18b.v1.name": {
        "zh": "信息单元",
        "en": "Information Unit (x)",
        "ja": "情報ユニット (x)",
        "es": "Unidad de información (x)"
    },
    "slides.s18b.v1.desc": {
        "zh": "文本具体词句（如“紫茉莉科” vs “其实是苞片”）。",
        "en": "Specific phrasing in text (e.g., 'Taxonomy' vs. 'Actually bracts').",
        "ja": "テキストの具体的語句（例：「オシロイバナ科」対「実は苞片」）。",
        "es": "Frase específica del texto (ej., 'Taxonomía' vs. 'En realidad brácteas')."
    },
    "slides.s18b.v2.name": {
        "zh": "先验预期概率",
        "en": "Prior Probability P(x)",
        "ja": "事前予想確率 P(x)",
        "es": "Probabilidad previa P(x)"
    },
    "slides.s18b.v2.desc": {
        "zh": "读者读到该词前的心理预期（常识 0.75 vs 意外 0.12）。",
        "en": "Prior mental expectation (0.75 for common facts vs. 0.12 for surprises).",
        "ja": "読前の心理的予想（常識 0.75 対 予想外 0.12）。",
        "es": "Expectativa previa (0.75 para hechos comunes vs. 0.12 para sorpresas)."
    },
    "slides.s18b.v3.name": {
        "zh": "逆对数尺度",
        "en": "Inverse Log2 Scale",
        "ja": "負の対数尺度",
        "es": "Escala logarítmica inversa"
    },
    "slides.s18b.v3.desc": {
        "zh": "打破预期的冲击程度呈对数倍增。",
        "en": "Surprisal impact increases logarithmically with lower probability.",
        "ja": "確率が低いほど、予想打破の衝撃が対数的に増大。",
        "es": "El impacto de sorpresa crece logarítmicamente con menor probabilidad."
    },
    "slides.s18b.v4.name": {
        "zh": "自信息量 (bits)",
        "en": "Self-Information I(x)",
        "ja": "自己情報量 I(x)",
        "es": "Auto-información I(x)"
    },
    "slides.s18b.v4.desc": {
        "zh": "读者实际获得的新知量（0.42 b [低] vs 3.06 b [高]）。",
        "en": "Actual knowledge gained (0.42 b [Low] vs. 3.06 b [High]).",
        "ja": "読者が実際に獲得する新知識量（0.42 b［低］対 3.06 b［高］）。",
        "es": "Conocimiento real adquirido (0.42 b [Bajo] vs. 3.06 b [Alto])."
    },
    "slides.s18b.criticalFlaw": {
        "zh": "传统指标盲区：注视时长与热力图默认“每秒注视等价”，无法辨识游客在文本 A 停留 10 秒（因枯燥卡顿）与在文本 B 停留 10 秒（吸收高价值新知）的本质区别。",
        "en": "Conventional Metric Flaw: Dwell time and heatmaps assume every second of gaze is equal, failing to distinguish 10s of gaze on Text A (stuck due to jargon) from 10s on Text B (actively absorbing high-value insights).",
        "ja": "従来指標の盲点：注視時間やヒートマップはすべての注視時間を等価と見なすため、テキストAでの10秒停滞（難解で読解停止）とテキストBでの10秒滞在（高価値な知識吸収）の質的差異を識別できません。",
        "es": "Punto ciego tradicional: El tiempo de permanencia asume que cada segundo es igual, incapaz de distinguir 10s en Texto A (bloqueo por jerga) de 10s en Texto B (absorción de conocimiento valioso)."
    },

    # Slide 22 (s18c)
    "slides.s18c.title": {
        "zh": "视线状态信息熵与认知摩擦",
        "en": "Gaze State Entropy and Cognitive Friction",
        "ja": "視線状態エントロピーと認知摩擦",
        "es": "Entropía de estado visual y fricción cognitiva"
    },
    "slides.s18c.guide": {
        "zh": "衡量注视点在区域间分布的混乱度与停滞阻力",
        "en": "Measuring gaze fixation disorder and reading stagnation resistance across zones",
        "ja": "領域間における注視点分布の無秩序さと読解停滞抵抗の測定",
        "es": "Medición del desorden visual y la resistencia al estancamiento de lectura entre zonas"
    },
    "slides.s18c.c1.tag": {
        "zh": "对照组 · 高认知摩擦",
        "en": "Control · High Cognitive Friction",
        "ja": "対照群 · 高認知摩擦",
        "es": "Control · Alta fricción cognitiva"
    },
    "slides.s18c.c1.body": {
        "zh": "长文本缺乏意外度与结构引导，视线反复自旋（自循环率 93%），80% 读者半途中断放弃。",
        "en": "Dense text lacks surprisal and structure, trapping gaze in repetitive loops (93% self-loop rate); 80% of readers abandon midway.",
        "ja": "長文テキストは意外性と構造的誘導に欠け、視線が空回り（自己ループ率93%）。80%の読者が途中で離脱。",
        "es": "El texto denso carece de sorpresa y estructura, atrapando la mirada en bucles (93% de bucle); el 80% abandona a mitad de camino."
    },
    "slides.s18c.c2.tag": {
        "zh": "改良组 · 低认知摩擦",
        "en": "Intervention · Low Cognitive Friction",
        "ja": "改良群 · 低認知摩擦",
        "es": "Intervención · Baja fricción cognitiva"
    },
    "slides.s18c.c2.body": {
        "zh": "高惊讶度气泡提供清晰着陆点，视线顺畅流转至多模态区域，加工顺畅度提升 +63.5%。",
        "en": "High-surprisal bubbles provide clear anchors; gaze flows smoothly across multimodal zones, improving fluency by +63.5%.",
        "ja": "高サプライザル気泡が明確な着地点を提供し、視線がマルチモーダル領域へスムーズに遷移。処理流暢性が+63.5%向上。",
        "es": "Las burbujas de alta sorpresa ofrecen anclajes claros; la mirada fluye suavemente hacia zonas multimodales (+63.5% de fluidez)."
    },
    "slides.s18c.rethink": {
        "zh": "长文本高停留往往是认知摩擦（Cognitive Friction）与解码受阻的假象，需信息论加权还原真实吸收。",
        "en": "High dwell time on dense text is often an artifact of cognitive friction and decoding blockage; information weighting is required to reveal true absorption.",
        "ja": "長文での長い滞在時間は認知摩擦（Cognitive Friction）による解読停滞であることが多く、情報理論的加重によって真の吸収量を評価する必要があります。",
        "es": "La alta permanencia en textos densos es a menudo un artefacto de fricción cognitiva; se requiere ponderación informacional para revelar la absorción real."
    },

    # Slide 23 (s18d)
    "slides.s18d.title": {
        "zh": "实验控制与信息加权框架",
        "en": "Experimental Control and Weighted Cognitive Model",
        "ja": "実験統制と情報加重認知フレームワーク",
        "es": "Control experimental y marco cognitivo ponderado"
    },
    "slides.s18d.guide": {
        "zh": "文本事实总量受控，信息熵作为客观权重矩阵，AOI 视线数据为真实自变量",
        "en": "Factual content is controlled; information entropy serves as objective weight matrix, with AOI gaze data as the true dynamic variable.",
        "ja": "事実総量を統制し、情報エントロピーを客観的重み行列、デザインに伴うAOI視線データを真の自変数として定義",
        "es": "El contenido factual se controla; la entropía actúa como matriz de peso objetiva y los datos AOI son la variable independiente."
    },
    "slides.s18d.s1.title": {
        "zh": "事实基线控制",
        "en": "Baseline Controlled",
        "ja": "事実ベースライン統制",
        "es": "Línea base controlada"
    },
    "slides.s18d.s1.desc": {
        "zh": "两组标牌传达的核心植物学事实总量大体相等，控制文本事实为恒定实验基准。",
        "en": "Core botanical facts are kept consistent across both conditions as a constant experimental baseline.",
        "ja": "両群の解説板が伝える植物学的核事実の総量を同等に保ち、恒常的な実験ベースラインを確立。",
        "es": "Los hechos botánicos centrales se mantienen consistentes como línea base experimental constante."
    },
    "slides.s18d.s2.title": {
        "zh": "客观信息熵矩阵",
        "en": "Entropy Weight Matrix",
        "ja": "客観的エントロピー行列",
        "es": "Matriz de pesos entrópicos"
    },
    "slides.s18d.s2.desc": {
        "zh": "基于先验概率建立各区域客观信息权重 I(AOI)，形成衡量新知密度的价值标尺。",
        "en": "Establishes objective surprisal weights I(AOI) based on prior probabilities as a knowledge value ruler.",
        "ja": "事前確率に基づき各領域の客観的自己情報量 I(AOI) を定義し、知識密度の評価尺を構築。",
        "es": "Establece pesos objetivos de sorpresa I(AOI) como regla de valor del conocimiento."
    },
    "slides.s18d.s3.title": {
        "zh": "动态视线分配 (pᵢ)",
        "en": "Dynamic Gaze Allocation",
        "ja": "動的視線配分 (pᵢ)",
        "es": "Asignación visual dinámica"
    },
    "slides.s18d.s3.desc": {
        "zh": "版面与叙事改变后，受众在各区域的注视时间占比 p_i 发生实质性重组。",
        "en": "Driven by redesign, visitors' gaze dwell proportions p_i undergo substantial restructuring.",
        "ja": "デザイン再構築に伴い、来園者の領域別注視時間比率 p_i が本質的に再編成されます。",
        "es": "Impulsada por el rediseño, la proporción de permanencia visual p_i se reestructura sustancialmente."
    },
    "slides.s18d.s4.title": {
        "zh": "净认知产出 E_gain",
        "en": "Net Cognitive Gain E_gain",
        "ja": "純認知的獲得 E_gain",
        "es": "Ganancia cognitiva neta"
    },
    "slides.s18d.s4.desc": {
        "zh": "视线分配自变量作用于客观信息矩阵（E_gain = ∑ p_i I_i），量化真实学习增量。",
        "en": "Gaze allocation variables operate on the objective matrix (E_gain = ∑ p_i I_i), quantifying true learning gain.",
        "ja": "視線配分変数を客観的情報行列に作用させる（E_gain = ∑ p_i I_i）ことで、真の学習獲得量を定量化。",
        "es": "Las variables de mirada operan sobre la matriz objetiva (E_gain = ∑ p_i I_i), cuantificando la ganancia real."
    },
    "slides.s18d.frameworkSummary": {
        "zh": "信息熵提供客观“知识价值标尺”，眼动数据记录“注意力分配”，二者结合揭开认知黑盒。",
        "en": "Information entropy provides an objective 'knowledge value ruler', while eye tracking records 'attention allocation' — uniting both unravels the cognitive black box.",
        "ja": "情報エントロピーが客観的な「知識価値の物差し」を提供し、視線追跡が「注意配分」を捉えます。両者の統合が認知のブラックボックスを解明します。",
        "es": "La entropía aporta una 'regla de valor del conocimiento' y el seguimiento ocular registra 'la asignación de atención', revelando la caja negra cognitiva."
    },

    # Slide 24 (s18e)
    "slides.s18e.title": {
        "zh": "四大功能区信息量客观权重",
        "en": "Objective Information Weights across 4 Functional Zones",
        "ja": "4大機能領域における客観的情報量重み",
        "es": "Pesos objetivos de información en 4 zonas funcionales"
    },
    "slides.s18e.guide": {
        "zh": "标定各语义区域的自信息量客观数值，建立加权基准",
        "en": "Calibrating objective self-information values across semantic zones as computation baseline",
        "ja": "各機能領域の客観的自己情報量を標定し、加重計算の基準を確立",
        "es": "Calibración de valores objetivos de auto-información como base de cálculo"
    },
    "slides.s18e.w1.title": {
        "zh": "传统科属长文",
        "en": "Conventional Taxonomy",
        "ja": "従来の分類学解説文",
        "es": "Taxonomía convencional"
    },
    "slides.s18e.w1.desc": {
        "zh": "“紫茉莉科木质藤本”\n先验概率 P=0.75 · 基础常识",
        "en": "\"Nyctaginaceae woody vine\"\nPrior P=0.75 · Common Knowledge",
        "ja": "「オシロイバナ科のつる植物」\n事前確率 P=0.75 · 基礎的常識",
        "es": "\"Trepadora de Nyctaginaceae\"\nExpectativa P=0.75 · Conocimiento común"
    },
    "slides.s18e.w2.title": {
        "zh": "触觉互动气泡 (R)",
        "en": "Tactile Sensory Bubble (R)",
        "ja": "身体感覚気泡 (R)",
        "es": "Burbuja táctil sensorial (R)"
    },
    "slides.s18e.w2.desc": {
        "zh": "“红色的不是花是苞片！”\n先验概率 P=0.12 · 7.37x 驱动",
        "en": "\"Red parts are bracts, not petals!\"\nPrior P=0.12 · 7.37x Core Driver",
        "ja": "「赤い部分は花ではなく苞片！」\n事前確率 P=0.12 · 7.37倍の牽引力",
        "es": "\"¡Las partes rojas son brácteas!\"\nExpectativa P=0.12 · Motor 7.37x"
    },
    "slides.s18e.w3.title": {
        "zh": "拟人对话引导",
        "en": "Personified Dialogue",
        "ja": "擬人化対話誘導",
        "es": "Diálogo personificado"
    },
    "slides.s18e.w3.desc": {
        "zh": "“猜猜我的艳丽秘密？”\n先验概率 P=0.15 · 情境代入",
        "en": "\"Guess my vibrant secret?\"\nPrior P=0.15 · Contextual Hook",
        "ja": "「鮮やかな秘密を当ててみて？」\n事前確率 P=0.15 · 共感の構築",
        "es": "\"¿Adivinas mi secreto?\"\nExpectativa P=0.15 · Conexión empática"
    },
    "slides.s18e.w4.title": {
        "zh": "花语文化提示",
        "en": "Flower Meaning & Culture",
        "ja": "花言葉と文化的ヒント",
        "es": "Significado floral y cultura"
    },
    "slides.s18e.w4.desc": {
        "zh": "“热情、坚韧与魅力”\n先验概率 P=0.25 · 趣味延展",
        "en": "\"Passion, Resilience, Charm\"\nPrior P=0.25 · Cultural Extension",
        "ja": "「情熱・魅力・強靭」\n事前確率 P=0.25 · 文化的興味の拡張",
        "es": "\"Pasión, Resiliencia, Encanto\"\nExpectativa P=0.25 · Extensión cultural"
    },
    "slides.s18e.summary": {
        "zh": "身体触觉互动区（3.06 bits）成为全标牌信息密度最高的核心知识锚点。",
        "en": "The tactile interactive zone (3.06 bits) serves as the primary high-information anchor across the signage.",
        "ja": "身体感覚インタラクション領域（3.06 bits）が解説板全体で最も情報密度の高い中核的知識アンカーとなります。",
        "es": "La zona interactiva táctil (3.06 bits) actúa como el anclaje de conocimiento de mayor densidad de la señal."
    },

    # Slide 25 (s18f)
    "slides.s18f.title": {
        "zh": "认知吸收总量模型 E_gain",
        "en": "Integrated Cognitive Gain Model E_gain",
        "ja": "認知的獲得総量モデル E_gain",
        "es": "Modelo de ganancia cognitiva integrada E_gain"
    },
    "slides.s18f.guide": {
        "zh": "动态视线时间权重乘以静态区域信息量",
        "en": "Multiplying dynamic gaze dwell proportions by static regional surprisal weights",
        "ja": "動的な視線滞在比率に静的な領域情報量を乗算",
        "es": "Ponderación del tiempo de permanencia dinámico por la sorpresa regional estática"
    },
    "slides.s18f.v1": {
        "zh": "• E_gain (bits)：整张标牌吸收的信息总量",
        "en": "• E_gain (bits): Total information absorbed across the signage",
        "ja": "• E_gain (bits)：解説板全体から吸収された期待情報総量",
        "es": "• E_gain (bits): Total de información absorbida de la señal"
    },
    "slides.s18f.v2": {
        "zh": "• p_i = T_i / ∑T_j：区域注视时间权重 (自变量)",
        "en": "• p_i = T_i / ∑T_j: Gaze dwell weight in zone i (independent variable)",
        "ja": "• p_i = T_i / ∑T_j：領域 i の注視時間比率（自変数）",
        "es": "• p_i = T_i / ∑T_j: Proporción de permanencia en zona i (variable)"
    },
    "slides.s18f.v3": {
        "zh": "• I(AOI_i)：区域客观自信息量 (静态权重)",
        "en": "• I(AOI_i): Objective surprisal of zone i (static weight)",
        "ja": "• I(AOI_i)：領域 i の客観的自己情報量（静的重み）",
        "es": "• I(AOI_i): Auto-información objetiva de zona i (peso estático)"
    },
    "slides.s18f.modelSummary": {
        "zh": "成功将“看哪里的时间 (p_i)”与“该处的新知价值 (I_i)”结合，解决停留时长与认知质量脱节难题。",
        "en": "Successfully unifies 'where time is spent (p_i)' with 'the value of knowledge there (I_i)', resolving the disconnect between dwell time and cognitive quality.",
        "ja": "「どこを見たかの時間（p_i）」と「その場所の新知識価値（I_i）」を統合し、滞在時間と認知品質の乖離問題を解決。",
        "es": "Unifica 'dónde se pasa el tiempo (p_i)' con 'el valor del conocimiento allí (I_i)', resolviendo la desconexión entre tiempo y calidad."
    },

    # Slide 26 (s18g)
    "slides.s18g.title": {
        "zh": "马尔可夫转移矩阵",
        "en": "Markov Transition Matrix",
        "ja": "マルコフ遷移確率行列",
        "es": "Matriz de transición de Markov"
    },
    "slides.s18g.guide": {
        "zh": "基于一阶马尔可夫链量化视线在各功能区之间的流转秩序",
        "en": "Quantifying gaze transition order across functional zones via first-order Markov chain",
        "ja": "1次マルコフ連鎖に基づき機能領域間の視線遷移秩序を定量化",
        "es": "Cuantificación del orden de transición visual entre zonas mediante cadena de Markov de primer orden"
    },
    "slides.s18g.kpiTitle": {
        "zh": "长文本自循环停滞率",
        "en": "Dense Text Self-Loop Stagnation Rate",
        "ja": "長文テキスト自己ループ停滞率",
        "es": "Tasa de estancamiento en bucle de texto denso"
    },
    "slides.s18g.box1.title": {
        "zh": "对照组：封闭文本阅读陷阱 (0.93)",
        "en": "Control: Closed Reading Trap (0.93)",
        "ja": "対照群：閉鎖的読解トラップ (0.93)",
        "es": "Control: Trampa de lectura cerrada (0.93)"
    },
    "slides.s18g.box1.body": {
        "zh": "视线在正文内反复自旋，转移至图片的概率仅 4%，无法形成图文互证。",
        "en": "Gaze loops within text; probability of transitioning to image is only 4%, preventing multimodal integration.",
        "ja": "視線が本文内で反復自転し、画像への遷移確率はわずか4%。図文照合が成立しません。",
        "es": "La mirada gira dentro del texto; la probabilidad de pasar a la imagen es solo 4%, impidiendo la integración."
    },
    "slides.s18g.box2.title": {
        "zh": "改良组：多模态导流网络 (0.56)",
        "en": "Intervention: Multimodal Flow Network (0.56)",
        "ja": "改良群：マルチモーダル誘導ネットワーク (0.56)",
        "es": "Intervención: Red de flujo multimodal (0.56)"
    },
    "slides.s18g.box2.body": {
        "zh": "视线平稳分流至触觉气泡 (0.19)、图标 (0.13) 与花语 (0.38)，构建顺畅探索动线。",
        "en": "Gaze smoothly routes to sensory bubbles (0.19), icons (0.13), and flower meanings (0.38), building a fluent exploratory scanpath.",
        "ja": "視線が感覚気泡(0.19)・アイコン(0.13)・花言葉(0.38)へ円滑に分流し、滑らかな探索動線を形成。",
        "es": "La mirada se dirige fluidamente a burbujas (0.19), iconos (0.13) y significados (0.38), creando un recorrido exploratorio fluido."
    },
    "slides.s18g.summary": {
        "zh": "彻底打破长文本自循环死锁，实现图文互证的高效认知流。",
        "en": "Completely breaks the dense text deadlock, establishing an efficient scanpath for multimodal reinforcement.",
        "ja": "長文テキストの自己ループ閉塞を打破し、図と文が相互補完する高効率な認知フローを実現。",
        "es": "Rompe el bloqueo en textos densos, estableciendo un flujo cognitivo eficiente de refuerzo multimodal."
    },

    # Slide 27 (s18h)
    "slides.s18h.title": {
        "zh": "认知传递能效比",
        "en": "Cognitive Transmission Efficiency Ratio",
        "ja": "認知伝達エネルギー効率比",
        "es": "Ratio de eficiencia de transmisión cognitiva"
    },
    "slides.s18h.guide": {
        "zh": "量化单位视觉搜索努力换取的信息增益",
        "en": "Quantifying information gain per unit of visual search effort",
        "ja": "視覚的探索努力単位あたりの情報獲得量を定量化",
        "es": "Cuantificación de la ganancia de información por unidad de esfuerzo de búsqueda visual"
    },
    "slides.s18h.i1": {
        "zh": "• 优化信息结构，降低无序搜索负荷",
        "en": "• Optimizes structure to reduce disordered visual search load",
        "ja": "• 情報構造を最適化し、無秩序な探索負荷を低減",
        "es": "• Optimiza la estructura reduciendo la carga de búsqueda visual"
    },
    "slides.s18h.i2": {
        "zh": "• 每一次注视均产生实质新知增益",
        "en": "• Every gaze fixation produces substantive information gain",
        "ja": "• すべての注視が実質的な新知識獲得に直結",
        "es": "• Cada fijación visual produce una ganancia sustantiva de información"
    },
    "slides.s18h.i3": {
        "zh": "• 真正实现“视觉减负”与“认知增效”",
        "en": "• Realizes both visual effort reduction and cognitive enhancement",
        "ja": "• 「視覚的負荷の軽減」と「認知的獲得の増大」を両立",
        "es": "• Logra la reducción del esfuerzo visual y la mejora cognitiva"
    },
    "slides.s18h.summary": {
        "zh": "将眼动研究从物理行为统计提升至认知传递能效定量评价。",
        "en": "Elevates eye tracking from physical behavior logging to quantitative cognitive transmission efficiency evaluation.",
        "ja": "視線追跡研究を物理的行動の記録から認知伝達エネルギー効率の定量的評価へと昇華。",
        "es": "Eleva el seguimiento ocular de la descripción física a la evaluación cuantitativa de eficiencia de transmisión cognitiva."
    }
}

for k, tr in clean_translations.items():
    zh[k] = tr["zh"]
    en[k] = tr["en"]
    ja[k] = tr["ja"]
    es[k] = tr["es"]

all_keys = sorted(list(set(list(zh.keys()) + list(en.keys()) + list(ja.keys()) + list(es.keys()))))
print(f"Total union keys: {len(all_keys)}")

for k in all_keys:
    if k not in zh: zh[k] = en.get(k, k)
    if k not in en: en[k] = zh.get(k, k)
    if k not in ja: ja[k] = zh.get(k, k)
    if k not in es: es[k] = en.get(k, k)

json.dump(zh, open('src/i18n/zh.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(en, open('src/i18n/en.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(ja, open('src/i18n/ja.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(es, open('src/i18n/es-MX.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print("Synchronized all clean dictionaries successfully!")
