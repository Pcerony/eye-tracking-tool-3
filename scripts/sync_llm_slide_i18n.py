# -*- coding: utf-8 -*-
import json
import os

zh = json.load(open('src/i18n/zh.json', 'r', encoding='utf-8'))
en = json.load(open('src/i18n/en.json', 'r', encoding='utf-8'))
ja = json.load(open('src/i18n/ja.json', 'r', encoding='utf-8'))
es = json.load(open('src/i18n/es-MX.json', 'r', encoding='utf-8'))

new_keys = {
    "slides.s18a.c1.tag": {
        "zh": "对照组 · 常规表述 (先验概率高 P=0.75)",
        "en": "Control · Conventional Formulation (High Prior P=0.75)",
        "ja": "対照群 · 従来の通常記述（事前確率高 P=0.75）",
        "es": "Control · Formulación convencional (Alta expectativa P=0.75)"
    },
    "slides.s18a.c2.tag": {
        "zh": "改良组 · 感官表述 (先验概率低 P=0.12)",
        "en": "Intervention · Sensory Formulation (Low Prior P=0.12)",
        "ja": "改良群 · 感覚的記述（事前確率低 P=0.12）",
        "es": "Intervención · Formulación sensorial (Baja expectativa P=0.12)"
    },
    "slides.s18a2.title": {
        "zh": "先验预期概率 P(x) 的 AI 测算机制",
        "en": "AI-Driven Computation of Prior Probability P(x)",
        "ja": "事前予想確率 P(x) の AI 算定メカニズム",
        "es": "Mecanismo de cálculo por IA de la probabilidad previa P(x)"
    },
    "slides.s18a2.guide": {
        "zh": "依托大语言模型（LLM）自回归概率预测原理，实现客观、秒级的新知意外度量化",
        "en": "Leveraging LLM autoregressive token probability distribution for objective, rapid surprisal quantification",
        "ja": "大規模言語モデル（LLM）の自己回帰的確率予測原理に基づき、新知識の意外性を客観的かつ瞬時に定量化",
        "es": "Aprovechamiento de la predicción probabilística autorregresiva de LLM para cuantificar la sorpresa de forma objetiva e instantánea"
    },
    "slides.s18a2.c1.tag": {
        "zh": "LLM 概率建模原理",
        "en": "LLM Probability Principle",
        "ja": "LLM 確率モデリング原理",
        "es": "Principio de modelado probabilístico de LLM"
    },
    "slides.s18a2.c1.title": {
        "zh": "大语言模型天然具备先验概率计算能力",
        "en": "Large Language Models Natively Compute Prior Probabilities",
        "ja": "大規模言語モデルは生来的に事前確率の計算能力を保持",
        "es": "Los modelos de lenguaje calculan de forma nativa probabilidades previas"
    },
    "slides.s18a2.c1.body": {
        "zh": "LLM 的工作原理本身即为自回归预测下一个词元的条件概率分布。海量语料预训练使其沉淀了人类普遍知识的先验基准，能够以极低计算成本秒级输出词与词之间的联结概率。",
        "en": "The foundational working mechanism of LLMs is predicting the conditional probability distribution of the next token. Massive pre-training embeds universal human knowledge priors, enabling instantaneous, objective calculation of transitional word probabilities at near-zero computation cost.",
        "ja": "LLMの基本作動原理は次のトークンの条件付き確率分布を自己回帰的に予測することです。膨大なコーパスによる事前学習により人類の普遍的知識の事前確率分布が蓄積されており、単語間の遷移確率を極めて低いコストで瞬時に出力できます。",
        "es": "El mecanismo de los LLM predice la distribución de probabilidad condicional del siguiente token. El preentrenamiento masivo almacena el conocimiento universal humano, calculando instantáneamente probabilidades de transición entre palabras."
    },
    "slides.s18a2.c2.tag": {
        "zh": "本实验中的 AI 应用",
        "en": "AI Calibration in This Study",
        "ja": "本実験における AI 適用",
        "es": "Aplicación de IA en este estudio"
    },
    "slides.s18a2.c2.title": {
        "zh": "实验标牌文本的 AI 客观快速标定",
        "en": "Rapid Objective Text Calibration for Signage Stimuli",
        "ja": "実験解説文の AI による客観的・迅速な校正",
        "es": "Calibración objetiva y rápida de los textos experimentales"
    },
    "slides.s18a2.c2.body": {
        "zh": "本次实验两组文本的先验概率由 AI 自动测算生成：常识类表述“木质藤本”获得高概率（P=0.75），而反转语句“不是花瓣是苞片”呈现极低先验概率（P=0.12），客观量化了认知打破程度。",
        "en": "Prior probabilities in our study were directly computed by AI: common taxonomy ('woody vine') yielded high probability (P=0.75), whereas counter-intuitive reversals ('bracts, not petals') yielded low prior probability (P=0.12), objectively measuring the degree of cognitive disruption.",
        "ja": "本実験における両群の解説文の事前確率はAIにより自動算出されました。常識的記述「オシロイバナ科つる植物」は高い確率（P=0.75）を示し、意外な反転記述「花ではなく苞片」は極めて低い事前確率（P=0.12）を記録し、認知打破の度合いを客観的に数値化しました。",
        "es": "Las probabilidades previas fueron calculadas directamente por IA: descripciones comunes ('trepadora leñosa') obtuvieron alta probabilidad (P=0.75), mientras que giros antiintuitivos ('brácteas, no pétalos') arrojaron baja probabilidad (P=0.12), midiendo objetivamente la sorpresa."
    },
    "slides.s18a2.summary": {
        "zh": "传统方法难以客观测定受众心理预期，而 AI 的概率机制为信息熵加权提供了高效、可重复的客观计算底座。",
        "en": "While traditional methods struggle to objectively gauge human psychological expectation, AI's probabilistic modeling provides an efficient, reproducible, and objective computational foundation for entropy weighting.",
        "ja": "従来手法では来園者の認知的期待値を客観的に測定することは困難でしたが、AIの確率モデリング機構により、情報エントロピー加重のための高効率かつ再現性の高い客観的計算基盤が確立されました。",
        "es": "Mientras que los métodos tradicionales tienen dificultades para medir objetivamente la expectativa previa, el modelado probabilístico de la IA proporciona una base objetiva y reproducible para la ponderación entrópica."
    }
}

for k, tr in new_keys.items():
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

print("Synchronized all dictionaries with LLM slide keys successfully!")
