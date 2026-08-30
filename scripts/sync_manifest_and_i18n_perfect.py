# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I18N_DIR = os.path.join(BASE_DIR, 'src', 'i18n')

cover_zh = {
    "slides.s18cover.title": "基于信息熵与惊讶度的深度认知分析",
    "slides.s18cover.desc": "超越表面注视时长假象 · 构建计算认知科学量化模型与全量实证检验",
    "slides.s18cover.p1.title": "理论重构：香农惊讶度建模",
    "slides.s18cover.p1.body": "指出传统时长指标将“阅读摩擦”误判为沉浸的缺陷，引入自信息量 I = -log₂(P) 量化反常识感官互动的高知识价值。",
    "slides.s18cover.p2.title": "动力学解构：马尔可夫转移矩阵",
    "slides.s18cover.p2.body": "运用一阶马尔可夫链证实长文本区 93% 自循环停滞陷阱，证明共创标牌成功实现向多模态区域的顺畅导流。",
    "slides.s18cover.p3.title": "全量实证：13人有效吸收量翻倍",
    "slides.s18cover.p3.body": "配对检验证实 E_gain 跃升 +127.7%（p<0.000001, d=3.46），13 位被试全部单调上升，能效比提升 29.9%。"
}

cover_en = {
    "slides.s18cover.title": "Deep Cognitive Analysis: Information Entropy & Surprisal",
    "slides.s18cover.desc": "Transcending Gaze Dwell Illusions · Computational Cognitive Modeling & Empirical Validation",
    "slides.s18cover.p1.title": "Theoretical Advance: Shannon Surprisal",
    "slides.s18cover.p1.body": "Reframing gaze dwell from reading friction to surprisal-weighted knowledge yield (I = -log2 P).",
    "slides.s18cover.p2.title": "Dynamic Gaze Flow: Markov Matrices",
    "slides.s18cover.p2.body": "Exposing the 93% text stagnation trap and verifying fluid multi-modal gaze navigation.",
    "slides.s18cover.p3.title": "Empirical Proof: Doubled Knowledge Yield",
    "slides.s18cover.p3.body": "Paired tests confirm +127.7% leap in E_gain (p<0.000001, d=3.46) with 100% monotonic increase across all 13 participants."
}

cover_ja = {
    "slides.s18cover.title": "情報エントロピーとサプライザルに基づく認知深化分析",
    "slides.s18cover.desc": "表面的な注視時間の錯覚を超えて · 計算論的認知モデルの構築と全量実証検証",
    "slides.s18cover.p1.title": "理論的再構築：シャノンサプライザル",
    "slides.s18cover.p1.body": "長文滞在が読解摩擦であることを見抜き、自己情報量 I = -log2(P) により高価値な感覚獲得を定量化。",
    "slides.s18cover.p2.title": "動線解読：マルコフ遷移行列",
    "slides.s18cover.p2.body": "93%の長文停滞死循環を数理的に解明し、共創サインによる円滑な領域間誘導を証明。",
    "slides.s18cover.p3.title": "全量実証：13名全員の認知獲得倍増",
    "slides.s18cover.p3.body": "対応のある検定により E_gain が+127.7%（p<0.000001, d=3.46）向上し、全13名で例外なき向上を実証。"
}

for lang, extra in [('zh.json', cover_zh), ('en.json', cover_en), ('ja.json', cover_ja), ('es-MX.json', cover_en)]:
    fpath = os.path.join(I18N_DIR, lang)
    with open(fpath, 'r', encoding='utf-8') as f:
        d = json.load(f)
    d.update(extra)
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

print("[*] 封面页多语言字典同步完成！")
