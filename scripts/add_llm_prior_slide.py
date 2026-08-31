# -*- coding: utf-8 -*-
import json
import os
import re

# 1. Update s18-deep-analysis-cover.json (Left-aligned title)
cover_path = "src/content/slides/s18-deep-analysis-cover.json"
cover_data = json.load(open(cover_path, "r", encoding="utf-8"))
cover_data["markup"] = """<div class="canvas-card" style="position:relative;">
    <canvas class="ascii-bg" aria-hidden="true"></canvas>
    <div class="cover-layout">
      <div data-anim="kicker" class="cover-author" style="text-align:left;align-self:flex-start">
        <div>PHASE 05 · DEEP COGNITIVE ANALYSIS</div>
        <div>SHANNON INFORMATION THEORY &amp; SURPRISAL MODEL</div>
        <div>N = 13 PARTICIPANTS · 27 TRIALS · PAIRED EMPIRICAL VALIDATION</div>
        <div>KYUSHU UNIVERSITY</div>
      </div>
      <h1 data-anim="title" style="align-self:flex-start;text-align:left;font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:52px;line-height:1.08;letter-spacing:0;color:#fff;max-width:24ch;hyphens:none" data-i18n="slides.s18cover.title">基于信息熵与惊讶度的深度认知分析<br/><span style="display:block;margin-top:1.8vh;font-size:24px;line-height:1.2;letter-spacing:0;font-weight:300;opacity:0.9" data-i18n="slides.s18cover.desc">超越表面注视时长假象 · 计算认知科学量化模型与全量实证</span></h1>
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
json.dump(cover_data, open(cover_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Updated s18-deep-analysis-cover.json with left-aligned title.")

# 2. Update s18a-entropy-intro.json (Cleaned text & explicit P=0.75 / P=0.12 tags)
s18a_path = "src/content/slides/s18a-entropy-intro.json"
s18a_data = json.load(open(s18a_path, "r", encoding="utf-8"))
s18a_data["markup"] = """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS</div><div class="r">20 / 38</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18a.title">文本信息量对比</h2><div class="analysis-kicker-desc" data-i18n="slides.s18a.guide">控制事实总量一致的前提下，常规表述与反常识表述的信息量差异</div></div><div class="analysis-anim-badge" aria-label="Text Animation"><span class="analysis-anim-label">INFORMATION</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="8" width="40" height="14" rx="2" fill="#eff6ff" stroke="#93c5fd" /><rect x="66" y="8" width="40" height="14" rx="2" fill="#fef2f2" stroke="#ef4444" /></svg></div></div><div class="analysis-body-group"><div class="clean-compare-grid"><div class="clean-compare-col"><span class="clean-compare-tag" style="color:var(--text-secondary)" data-i18n="slides.s18a.c1.tag">对照组 · 常规表述 (先验概率高 P=0.75)</span><p class="clean-text-quote"><span data-i18n="slides.s18a.c1.p1">九重葛为</span><span class="heat-blue" data-i18n="slides.s18a.c1.h1">紫茉莉科木质藤本</span><span data-i18n="slides.s18a.c1.p2">，原产于南美洲，夏季开花。</span></p><div class="clean-stat-row"><span class="clean-stat-num" style="color:#1e40af">0.42<small style="font-size:22px;margin-left:4px">bits</small></span><span class="clean-stat-desc" data-i18n="slides.s18a.c1.desc">司空见惯常识 · 知识增量极低</span></div></div><div class="clean-compare-col"><span class="clean-compare-tag" style="color:var(--accent)" data-i18n="slides.s18a.c2.tag">改良组 · 感官表述 (先验概率低 P=0.12)</span><p class="clean-text-quote"><span data-i18n="slides.s18a.c2.p1">红色的</span><span class="heat-red" data-i18n="slides.s18a.c2.h1">不是花瓣是苞片！</span><span data-i18n="slides.s18a.c2.p2">请用手触摸</span><span class="heat-red" data-i18n="slides.s18a.c2.h2">干爽纸质触感</span>。</p><div class="clean-stat-row"><span class="clean-stat-num" style="color:var(--accent)">3.06<small style="font-size:22px;margin-left:4px">bits</small></span><span class="clean-stat-desc" data-i18n="slides.s18a.c2.desc">颠覆预期反常识 · 知识增量 7.37 倍</span></div></div></div><div style="padding-top:16px;border-top:1px solid var(--border-subtle);display:flex;justify-content:space-between;align-items:center"><div style="font-size:16px;color:var(--ink);font-weight:500" data-i18n="slides.s18a.summary">字数相当、事实受控的前提下，反常识表述所释放的有效信息量激增 7.37 倍。</div><span style="font-family:var(--mono);font-size:12px;color:var(--accent);font-weight:700">7.37x SURPRISAL</span></div></div></div>"""
json.dump(s18a_data, open(s18a_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Updated s18a-entropy-intro.json.")

# 3. Create s18a2-prior-llm-method.json (NEW SLIDE: LLM AI Calculation of P(x))
s18a2_data = {
    "id": "s18a2-prior-llm-method",
    "chapterId": "deep-analysis",
    "layout": "data",
    "chapter": "5",
    "chapterTitle": "深度分析",
    "shortTitle": "阶段五：AI测算先验概率",
    "animation": "statement-rise",
    "legacyLayout": "S06",
    "legacyClass": "slide",
    "assets": [],
    "claims": [],
    "markup": """<div class="canvas-card analysis-data-slide"><div class="chrome-min"><div class="l">PHASE 5 · DEEP COGNITIVE ANALYSIS</div><div class="r">21 / 38</div></div><div class="analysis-header-row"><div class="analysis-header-left"><h2 class="analysis-kicker" data-i18n="slides.s18a2.title">先验预期概率 P(x) 的 AI 测算机制</h2><div class="analysis-kicker-desc" data-i18n="slides.s18a2.guide">依托大语言模型（LLM）自回归概率预测原理，实现客观、秒级的新知意外度量化</div></div><div class="analysis-anim-badge" aria-label="AI Probability Animation"><span class="analysis-anim-label">AI / LLM METHOD</span><svg width="116" height="30" viewBox="0 0 116 30" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M 10 15 Q 35 5 60 15 T 110 15" stroke="var(--accent)" stroke-width="2" fill="none" /><circle cx="60" cy="15" r="4" fill="var(--accent)" /></svg></div></div><div class="analysis-body-group"><div class="hero-formula-wrap"><div class="hero-formula">P(x) = ∏ P_LLM( wₜ | w₁ ... wₜ₋₁ )</div></div><div class="clean-compare-grid"><div class="clean-compare-col"><span class="clean-compare-tag" style="color:var(--accent)" data-i18n="slides.s18a2.c1.tag">LLM 概率建模原理</span><h4 style="font-size:20px;font-weight:600;color:var(--ink);margin:0" data-i18n="slides.s18a2.c1.title">大语言模型天然具备先验概率计算能力</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.55;margin:0" data-i18n="slides.s18a2.c1.body">LLM 的工作原理本身即为自回归预测下一个词元的条件概率分布。海量语料预训练使其沉淀了人类普遍知识的先验基准，能够以极低计算成本秒级输出词与词之间的联结概率。</p></div><div class="clean-compare-col"><span class="clean-compare-tag" style="color:#16a34a" data-i18n="slides.s18a2.c2.tag">本实验中的 AI 应用</span><h4 style="font-size:20px;font-weight:600;color:var(--ink);margin:0" data-i18n="slides.s18a2.c2.title">实验标牌文本的 AI 客观快速标定</h4><p style="font-size:15px;color:var(--text-primary);line-height:1.55;margin:0" data-i18n="slides.s18a2.c2.body">本次实验两组文本的先验概率由 AI 自动测算生成：常识类表述“木质藤本”获得高概率（P=0.75），而反转语句“不是花瓣是苞片”呈现极低先验概率（P=0.12），客观量化了认知打破程度。</p></div></div><div style="padding-top:16px;border-top:1px solid var(--border-subtle)"><p style="font-size:15px;color:var(--ink);line-height:1.45;margin:0" data-i18n="slides.s18a2.summary">传统方法难以客观测定受众心理预期，而 AI 的概率机制为信息熵加权提供了高效、可重复的客观计算底座。</p></div></div></div>"""
}
json.dump(s18a2_data, open("src/content/slides/s18a2-prior-llm-method.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Created src/content/slides/s18a2-prior-llm-method.json.")

# 4. Update deck-manifest.json to insert s18a2-prior-llm-method
manifest_path = "deck-manifest.json"
manifest = json.load(open(manifest_path, "r", encoding="utf-8"))

existing_ids = [s["id"] for s in manifest["slides"]]
if "s18a2-prior-llm-method" not in existing_ids:
    idx = existing_ids.index("s18a-entropy-intro")
    manifest["slides"].insert(idx + 1, {
        "id": "s18a2-prior-llm-method",
        "chapterId": "deep-analysis",
        "layout": "data",
        "content": "src/content/slides/s18a2-prior-llm-method.json",
        "assets": [],
        "claims": []
    })
    json.dump(manifest, open(manifest_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Inserted s18a2-prior-llm-method into deck-manifest.json.")

total_slides = len(manifest["slides"])
print(f"Total slides in deck: {total_slides}")

for i, slide_meta in enumerate(manifest["slides"]):
    c_path = slide_meta["content"]
    if os.path.exists(c_path):
        s_obj = json.load(open(c_path, "r", encoding="utf-8"))
        page_num = i + 1
        if "markup" in s_obj and isinstance(s_obj["markup"], str):
            new_markup = re.sub(r'(<div class="r"[^>]*>)\d+\s*/\s*\d+(</div>)', f'\\g<1>{page_num:02d} / {total_slides}\\g<2>', s_obj["markup"])
            if new_markup != s_obj["markup"]:
                s_obj["markup"] = new_markup
                json.dump(s_obj, open(c_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print("Updated page numbers across all slides.")

