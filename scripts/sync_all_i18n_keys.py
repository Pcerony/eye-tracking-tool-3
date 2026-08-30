import json
import re
import os

# Load all slides and find all data-i18n references
i18n_keys_found = set()

for fn in sorted(os.listdir('src/content/slides')):
    if fn.endswith('.json'):
        with open(os.path.join('src/content/slides', fn), 'r', encoding='utf-8') as f:
            data = json.load(f)
            markup = str(data.get('markup', ''))
            matches = re.findall(r'data-i18n="([^"]+)"', markup)
            for m in matches:
                i18n_keys_found.add(m)

print(f"Total data-i18n keys found in slides: {len(i18n_keys_found)}")

# Load the 4 dictionaries
zh = json.load(open('src/i18n/zh.json', 'r', encoding='utf-8'))
en = json.load(open('src/i18n/en.json', 'r', encoding='utf-8'))
ja = json.load(open('src/i18n/ja.json', 'r', encoding='utf-8'))
es = json.load(open('src/i18n/es-MX.json', 'r', encoding='utf-8'))

# New translations for newly introduced or refined keys
translations = {
    "slides.s18a.title": {
        "zh": "基于信息熵与惊讶度理论的深度分析",
        "en": "In-Depth Analysis Based on Information Entropy and Surprisal Theory",
        "ja": "情報エントロピーとサプライザル理論に基づく詳細分析",
        "es": "Análisis en profundidad basado en entropía de información y teoría de la sorpresa"
    },
    "slides.s18a.guide": {
        "zh": "【理论引入】超越“注视时长”表面假象，量化真实知识吸收与阅读认知流",
        "en": "[Theoretical Introduction] Moving Beyond Dwell Time to Quantify True Knowledge Gain and Cognitive Flow",
        "ja": "【理論的導入】「注視時間」の表面的な錯覚を超え、真の知識獲得と認知的読解フローを定量化",
        "es": "[Introducción teórica] Superar la ilusión del tiempo de fijación para cuantificar la ganancia real de conocimiento"
    },
    "slides.s18a.summary": {
        "zh": "核心范式演进：从“表面物理停留时长”升级为“单位视觉负荷下的有效新知吸收量与流转秩序”。",
        "en": "Core Paradigm Shift: Evolving from superficial physical dwell time to effective information gain per unit visual load and structured cognitive flow.",
        "ja": "中核的パラダイムシフト：「表面的な物理滞在時間」から「視覚負荷あたりの有効な新知識獲得量と遷移秩序」へ進化。",
        "es": "Evolución de paradigma: de la duración física superficial a la ganancia de información efectiva por carga visual."
    },
    "slides.s18b.title": {
        "zh": "传统眼动三大常规指标及其均质化假定缺陷",
        "en": "Three Conventional Eye-Tracking Metrics and the Flaw of the Uniformity Assumption",
        "ja": "従来の視線追跡3大指標と均質化仮定の欠陥",
        "es": "Tres métricas convencionales de seguimiento ocular y el defecto de la suposición de homogeneidad"
    },
    "slides.s18b.guide": {
        "zh": "【基线解构】剖析传统时长、落点与热力图如何将“读不下去的卡顿”误判为“深度阅读”",
        "en": "[Baseline Deconstruction] Analyzing How Conventional Dwell Time, Fixation Count, and Heatmaps Misjudge Reading Stagnation as Deep Engagement",
        "ja": "【ベースライン解剖】従来の滞在時間・注視回数・ヒートマップがいかに「難解さによる読解停滞」を「熟読」と誤認するかを解剖",
        "es": "[Deconstrucción de línea base] Cómo las métricas convencionales confunden el estancamiento lector con el compromiso profundo"
    },
    "slides.s18b.criticalFlaw": {
        "zh": "三大常规指标默认“每秒注视具有均等知识加工价值”，仅记录物理停留坐标，无法辨识注视背后的认知理解质量与晦涩文字带来的无序停滞。",
        "en": "The three conventional metrics implicitly assume that every second of fixation carries equal cognitive value, recording only physical coordinates without distinguishing comprehension quality from stagnation caused by dense text.",
        "ja": "従来の3大指標は「1秒あたりの注視が均等な知識処理価値を持つ」と仮定しており、物理的な滞在座標を記録するだけで、難解な文章による無秩序な停滞と真の理解品質を識別できません。",
        "es": "Las tres métricas convencionales asumen que cada segundo de fijación tiene el mismo valor cognitivo, sin distinguir la calidad de comprensión del estancamiento."
    },
    "slides.s18c.title": {
        "zh": "认知受阻与信息熵：量化视线分布的无序与摩擦",
        "en": "Cognitive Friction and Information Entropy: Quantifying Gaze Disorder and Reading Stagnation",
        "ja": "認知摩擦と情報エントロピー：視線分布の無秩序性と停滞の定量化",
        "es": "Fricción cognitiva y entropía de información: cuantificación del desorden visual y el estancamiento lector"
    },
    "slides.s18c.guide": {
        "zh": "【数学建模】引入视线状态熵 H(X) = -∑ P(x) log2 P(x)，揭示长文本造成的虚假高停留",
        "en": "[Mathematical Modeling] Introducing Gaze Entropy H(X) = -∑ P(x) log2 P(x) to Uncover the Illusion of High Dwell Time in Dense Text",
        "ja": "【数理モデリング】視線状態エントロピー H(X) = -∑ P(x) log2 P(x) を導入し、長文が引き起こす見かけ上の高滞在時間を解明",
        "es": "[Modelado matemático] Introducción de la entropía de fijación H(X) = -∑ P(x) log2 P(x) para revelar la falsa alta permanencia en textos densos"
    },
    "slides.s18c.rethink": {
        "zh": "诊断结论：高停留时长反映的是信息解码受阻（Cognitive Friction）而非有效知识吸收，必须引入度量信息意外度与流转秩序的信息论工具。",
        "en": "Diagnostic Conclusion: Prolonged dwell time reflects cognitive friction during information decoding rather than effective learning, necessitating information-theoretic tools to measure surprisal and flow order.",
        "ja": "診断結論：長い滞在時間は有効な知識獲得ではなく情報解読の停滞（認知摩擦）を反映しており、驚きの度合いと遷移秩序を測定する情報理論的アプローチが不可欠です。",
        "es": "Conclusión diagnóstica: El tiempo de permanencia prolongado refleja fricción cognitiva en la decodificación más que un aprendizaje efectivo."
    },
    "slides.s18d.title": {
        "zh": "香农信息论与惊讶度：违背预期的认知增益",
        "en": "Shannon Information Theory and Surprisal: Cognitive Gain Beyond Expectation",
        "ja": "シャノン情報理論とサプライザル：予想を覆す認知的獲得",
        "es": "Teoría de la información de Shannon y sorpresa: ganancia cognitiva que desafía las expectativas"
    },
    "slides.s18d.guide": {
        "zh": "【数理公式】基于真实九重葛标牌文本，逐个演示自信息量 I = -log2(P) 的变量释义与计算",
        "en": "[Mathematical Formulation] Demonstrating Variable Definitions and Computations of Self-Information I = -log2(P) Using Real Bougainvillea Signage Text",
        "ja": "【数理公式】実際のブーゲンビレア解説板のテキストに基づき、自己情報量 I = -log2(P) の変数定義と計算プロセスを実演",
        "es": "[Formulación matemática] Demostración de definiciones y cálculos de auto-información I = -log2(P) sobre texto real de señalización"
    },
    "slides.s18d.axiom": {
        "zh": "“信息在违背预期时，其承载的信息量最大” —— 解释了为何 3 秒感官触觉互动能够大幅激发深度记忆。",
        "en": "'Information is maximized when expectations are broken' — explaining why a 3-second sensory tactile interaction triggers profound hippocampal memory encoding.",
        "ja": "「情報は予想を覆す時に最大の情報量を持つ」—— 3秒間の感覚・触覚的インタラクションが深層記憶を強力に活性化させる理由を解明。",
        "es": "'La información se maximiza cuando desafía las expectativas' — explicando por qué una interacción táctil de 3 segundos activa la memoria profunda."
    },
    "slides.s18e.title": {
        "zh": "真实标牌各区域信息量权重与案例量化计算",
        "en": "Information Weight Across Signage Regions and Empirical Case Quantification",
        "ja": "解説板各領域の情報量重み付けと実例の定量的計算",
        "es": "Ponderación de información en áreas de señalización y cuantificación de casos reales"
    },
    "slides.s18e.guide": {
        "zh": "【实证剖析】从真实九重葛标牌截选四大功能区切片，对比自信息量数值差异",
        "en": "[Empirical Breakdown] Cropping Four Functional Zones from Real Bougainvillea Signage to Contrast Self-Information Values",
        "ja": "【実証的分析】実際のブーゲンビレア解説板から4つの主要領域を切り出し、自己情報量の数値差を比較検証",
        "es": "[Desglose empírico] Muestreo de cuatro zonas funcionales en señalización real de Bougainvillea para contrastar valores de auto-información"
    },
    "slides.s18e.ticker1": {
        "zh": "触觉互动 (R)：P = 0.12 → I = 3.059 bits (7.37x)",
        "en": "Tactile Bubble (R): P = 0.12 → I = 3.059 bits (7.37x)",
        "ja": "触覚インタラクション (R)：P = 0.12 → I = 3.059 bits (7.37倍)",
        "es": "Burbuja táctil (R): P = 0.12 → I = 3.059 bits (7.37x)"
    },
    "slides.s18e.ticker2": {
        "zh": "拟人化对话：P = 0.15 → I = 2.737 bits",
        "en": "Personified Dialogue: P = 0.15 → I = 2.737 bits",
        "ja": "擬人化対話：P = 0.15 → I = 2.737 bits",
        "es": "Diálogo personificado: P = 0.15 → I = 2.737 bits"
    },
    "slides.s18e.ticker3": {
        "zh": "花语提示：P = 0.25 → I = 2.000 bits",
        "en": "Flower Meaning: P = 0.25 → I = 2.000 bits",
        "ja": "花言葉の提示：P = 0.25 → I = 2.000 bits",
        "es": "Significado de flores: P = 0.25 → I = 2.000 bits"
    },
    "slides.s18e.ticker4": {
        "zh": "传统分类学：P = 0.75 → I = 0.415 bits",
        "en": "Conventional Taxonomy: P = 0.75 → I = 0.415 bits",
        "ja": "従来の分類学説明：P = 0.75 → I = 0.415 bits",
        "es": "Taxonomía tradicional: P = 0.75 → I = 0.415 bits"
    },
    "slides.s18f.title": {
        "zh": "信息加权认知吸收量（E_gain）计算模型",
        "en": "Information-Weighted Cognitive Gain (E_gain) Mathematical Model",
        "ja": "情報加重認知的吸収量（E_gain）計算モデル",
        "es": "Modelo matemático de ganancia cognitiva ponderada por información (E_gain)"
    },
    "slides.s18f.guide": {
        "zh": "【公式推导】在九重葛真实标牌上演示 E_gain = ∑ [ p_i × I(AOI_i) ] 逐区域演算全过程",
        "en": "[Mathematical Derivation] Step-by-Step Demonstration of E_gain = ∑ [ p_i × I(AOI_i) ] Across Real Bougainvillea Signage Zones",
        "ja": "【数式導出】実際のブーゲンビレア解説板上で E_gain = ∑ [ p_i × I(AOI_i) ] の領域別演算プロセスを実演",
        "es": "[Derivación matemática] Demostración paso a paso de E_gain = ∑ [ p_i × I(AOI_i) ] sobre zonas de señalización real"
    },
    "slides.s18f.meaning": {
        "zh": "期望认知吸收总量 = 各功能区注视时间权重 (p_i) × 区域自信息量 (I_i)，实现质与量的统一度量。",
        "en": "Expected Cognitive Gain = Fixation Dwell Proportion (p_i) × Surprisal Self-Information (I_i), unifying quality and quantity.",
        "ja": "期待認知的獲得総量 = 各機能領域の注視時間割合 (p_i) × 領域の自己情報量 (I_i) により、質と量の統合的評価を実現。",
        "es": "Ganancia cognitiva esperada = Proporción de fijación (p_i) × Auto-información de sorpresa (I_i), unificando calidad y cantidad."
    },
    "slides.s18g.title": {
        "zh": "马尔可夫转移矩阵：打破 93% 长文本死循环",
        "en": "Markov Transition Matrix: Breaking the 93% Dense Text Self-Loop",
        "ja": "マルコフ遷移行列：長文テキストにおける93%のループ固定を打破",
        "es": "Matriz de transición de Markov: Rompiendo el bucle del 93% en textos densos"
    },
    "slides.s18g.guide": {
        "zh": "【动线解构】在真实标牌上标注一阶转移概率，量化视线自长文本向感官气泡的良性分流",
        "en": "[Scanpath Deconstruction] Annotating First-Order Markov Transition Probabilities to Quantify Gaze Redistribution into Sensory Bubbles",
        "ja": "【視線動線解体】実際の解説板上に1次マルコフ遷移確率をマッピングし、長文から感覚気泡への健全な分散を定量化",
        "es": "[Deconstrucción de trayectoria] Mapeo de probabilidades de transición de Markov para cuantificar la redistribución hacia burbujas sensoriales"
    },
    "slides.s18g.kpi.sub": {
        "zh": "马尔可夫矩阵证实：长文本自循环死锁从 93% 大幅降至 56%（-39.8%, p < 0.001），构建起顺畅的图文认知流。",
        "en": "Markov matrix confirms: Dense text self-looping drops from 93% to 56% (-39.8%, p < 0.001), establishing a fluent multimodal cognitive stream.",
        "ja": "マルコフ行列が実証：長文テキスト内の自己ループ停滞が93%から56%へと大幅に減少（-39.8%, p < 0.001）、円滑な認知フローを構築。",
        "es": "La matriz de Markov confirma: El bucle en texto denso cae del 93% al 56% (-39.8%, p < 0.001), creando un flujo cognitivo fluido."
    },
    "slides.s18h.title": {
        "zh": "认知信息传递能效比：单位视觉负荷的产出",
        "en": "Cognitive Transmission Efficiency Ratio: Output per Unit Visual Load",
        "ja": "認知情報伝達のエネルギー効率比：視覚負荷あたりの新知識産出",
        "es": "Ratio de eficiencia de transmisión cognitiva: Rendimiento por unidad de carga visual"
    },
    "slides.s18h.guide": {
        "zh": "【能效建模】构建 η = E_gain / (H_GTE + ε) 指标，量化单位视觉搜索努力换取的信息增益",
        "en": "[Efficiency Modeling] Constructing η = E_gain / (H_GTE + ε) to Quantify Cognitive Information Gain per Unit Visual Search Effort",
        "ja": "【効率性モデリング】指標 η = E_gain / (H_GTE + ε) を構築し、単位視覚探索負荷あたりの知識獲得量を定量化",
        "es": "[Modelado de eficiencia] Construcción de η = E_gain / (H_GTE + ε) para cuantificar la ganancia de información por esfuerzo visual"
    },
    "slides.s18h.gainBody": {
        "zh": "实证证实：能效比自 1.083 跃升至 1.407（+29.9%, p=0.004），用更少视觉消耗换取了更高价值知识吸收。",
        "en": "Empirically verified: Efficiency ratio jumps from 1.083 to 1.407 (+29.9%, p=0.004), achieving higher-value learning with reduced visual exertion.",
        "ja": "実証的検証：効率比が 1.083 から 1.407 へと大幅に向上（+29.9%, p=0.004）。より少ない視覚的疲労で高価値な知識吸収を実現。",
        "es": "Verificado empíricamente: El ratio de eficiencia sube de 1.083 a 1.407 (+29.9%, p=0.004), logrando mayor aprendizaje con menor esfuerzo."
    }
}

# Update all keys in the dictionaries
for k, tr in translations.items():
    zh[k] = tr["zh"]
    en[k] = tr["en"]
    ja[k] = tr["ja"]
    es[k] = tr["es"]

# Check for all keys consistency across 4 dictionaries
all_keys = sorted(list(set(list(zh.keys()) + list(en.keys()) + list(ja.keys()) + list(es.keys()))))
print(f"Total union keys in dictionaries: {len(all_keys)}")

for k in all_keys:
    if k not in zh: zh[k] = en.get(k, k)
    if k not in en: en[k] = zh.get(k, k)
    if k not in ja: ja[k] = zh.get(k, k)
    if k not in es: es[k] = en.get(k, k)

# Write back sorted dictionaries
json.dump(zh, open('src/i18n/zh.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(en, open('src/i18n/en.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(ja, open('src/i18n/ja.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(es, open('src/i18n/es-MX.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print("Synchronized all 4 dictionaries successfully!")
