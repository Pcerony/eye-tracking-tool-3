import os
import math
from PIL import Image, ImageDraw, ImageFont

os.makedirs('src/assets/images', exist_ok=True)

def get_font(size, bold=False, mono=False):
    if mono:
        candidates = [
            '/Library/Fonts/SF-Mono-Bold.otf' if bold else '/Library/Fonts/SF-Mono-Regular.otf',
            '/System/Library/Fonts/Menlo.ttc',
            '/System/Library/Fonts/Courier.dfont'
        ]
    elif bold:
        candidates = [
            '/System/Library/Fonts/PingFang.ttc',
            '/System/Library/Fonts/Hiragino Sans GB.ttc',
            '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
            '/System/Library/Fonts/Helvetica.ttc'
        ]
    else:
        candidates = [
            '/System/Library/Fonts/PingFang.ttc',
            '/System/Library/Fonts/Hiragino Sans GB.ttc',
            '/System/Library/Fonts/Supplemental/Arial.ttf',
            '/System/Library/Fonts/Helvetica.ttc'
        ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                continue
    return ImageFont.load_default()

im_a1 = Image.open('stimuli/A1.png').convert('RGB')
im_a2 = Image.open('stimuli/A2.png').convert('RGB')
w1, h1 = im_a1.size
w2, h2 = im_a2.size

print("Loaded high-res stimuli A1 & A2:", w1, h1)

def draw_card(draw, xy, fill, outline=None, width=1, radius=6):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=int(width))

# ==============================================================================
# FIG 1: entropy-fig-01-paradigm.jpg
# ==============================================================================
def make_fig_01():
    out_w, out_h = 1060, 460
    bg = Image.new('RGB', (out_w, out_h), '#ffffff')
    draw = ImageDraw.Draw(bg)
    
    # Left Box: A1 Control Crop
    crop_a1 = im_a1.crop((int(w1*0.44), int(h1*0.18), int(w1*0.96), int(h1*0.82))).resize((480, 340), Image.Resampling.LANCZOS)
    bg.paste(crop_a1, (30, 40))
    draw_card(draw, (30, 40, 510, 380), fill=None, outline='#dc2626', width=2, radius=4)
    
    # Left Tag
    draw_card(draw, (40, 50, 240, 82), fill='#fee2e2', outline='#dc2626', width=1, radius=4)
    draw.text((50, 57), "A1 对照组：认知受阻", font=get_font(15, bold=True), fill='#991b1b')
    
    # Left Pin Callout
    draw_card(draw, (40, 300, 500, 370), fill='#ffffff', outline='#dc2626', width=1, radius=4)
    draw.text((52, 308), "• 停留 20 秒 · 视线在生僻分类字中卡顿打转", font=get_font(13, bold=True), fill='#b91c1c')
    draw.text((52, 332), "• 先验常识 (P=0.75) · 真实有效知识增量 ≈ 0", font=get_font(13), fill='#334155')

    # Right Box: A2 Experiment Crop
    crop_a2 = im_a2.crop((int(w2*0.42), int(h2*0.18), int(w2*0.96), int(h2*0.82))).resize((480, 340), Image.Resampling.LANCZOS)
    bg.paste(crop_a2, (550, 40))
    draw_card(draw, (550, 40, 1030, 380), fill=None, outline='#16a34a', width=2, radius=4)
    
    # Right Tag
    draw_card(draw, (560, 50, 760, 82), fill='#dcfce7', outline='#16a34a', width=1, radius=4)
    draw.text((570, 57), "A2 改良组：认知激活", font=get_font(15, bold=True), fill='#166534')
    
    # Right Pin Callout
    draw_card(draw, (560, 300, 1020, 370), fill='#ffffff', outline='#16a34a', width=1, radius=4)
    draw.text((572, 308), "• 停留更短 · 视线平稳导流至触觉感官气泡", font=get_font(13, bold=True), fill='#15803d')
    draw.text((572, 332), "• 反常识线索 (P=0.12) · 激发高深度海马体记忆", font=get_font(13), fill='#334155')

    # Bottom Summary Banner
    draw_card(draw, (30, 398, 1030, 444), fill='#f8fafc', outline='#cbd5e1', width=1, radius=4)
    draw.text((50, 410), "认知范式升级：", font=get_font(14, bold=True), fill='#0f172a')
    draw.text((160, 411), "从『表面物理注视时长（秒）』跃升为『单位视觉负荷下的有效信息吸收量（bits）』", font=get_font(13.5), fill='#475569')

    bg.save('src/assets/images/entropy-fig-01-paradigm.jpg', quality=95)
    print("Generated entropy-fig-01-paradigm.jpg")

# ==============================================================================
# FIG 2: entropy-fig-02-metrics-flaw.jpg
# ==============================================================================
def make_fig_02():
    out_w, out_h = 1060, 460
    bg = Image.new('RGB', (out_w, out_h), '#ffffff')
    draw = ImageDraw.Draw(bg)
    
    # Left: High-Res Real Crop of A1 Text
    crop_a1 = im_a1.crop((int(w1*0.45), int(h1*0.22), int(w1*0.95), int(h1*0.78))).resize((520, 380), Image.Resampling.LANCZOS)
    bg.paste(crop_a1, (30, 40))
    draw_card(draw, (30, 40, 550, 420), fill=None, outline='#cbd5e1', width=1, radius=4)
    
    # Text overlay pin
    draw_card(draw, (45, 55, 260, 90), fill='#fef2f2', outline='#dc2626', width=1, radius=4)
    draw.text((55, 63), "A1 传统分类学科普长文本", font=get_font(14, bold=True), fill='#991b1b')

    # Right: 3 Metric breakdown cards
    cards = [
        ("01 注视时长 (DWELL TIME)", "14.2s (占比 44.3%)", "#fee2e2", "#b91c1c", "缺陷：误将长文本的卡顿读不下去判为『最感兴趣』"),
        ("02 注视次数 (FIXATION COUNT)", "48 次落点 (频次最高)", "#fee2e2", "#b91c1c", "缺陷：视线反复在生僻拉丁词间犹疑，实为高负荷困境"),
        ("03 注视热力图 (HEATMAP)", "正文区呈现大片深红高亮", "#fee2e2", "#b91c1c", "缺陷：仅反映空间点云密度，无法辨识知识理解质量")
    ]
    
    y = 40
    for title, metric, bg_col, text_col, flaw in cards:
        draw_card(draw, (570, y, 1030, y + 115), fill='#ffffff', outline='#e2e8f0', width=1, radius=4)
        draw_card(draw, (585, y + 12, 820, y + 38), fill='#f8fafc', outline='#cbd5e1', width=1, radius=3)
        draw.text((595, y + 16), title, font=get_font(12, bold=True, mono=True), fill='#475569')
        
        draw.text((840, y + 15), metric, font=get_font(13.5, bold=True), fill=text_col)
        draw.text((585, y + 50), flaw, font=get_font(13), fill='#334155')
        draw.text((585, y + 78), "➜ 均质化假设缺陷：默认每秒注视具有均等知识价值", font=get_font(12, bold=True), fill='#dc2626')
        y += 130

    bg.save('src/assets/images/entropy-fig-02-metrics-flaw.jpg', quality=95)
    print("Generated entropy-fig-02-metrics-flaw.jpg")

# ==============================================================================
# FIG 3: entropy-fig-03-friction.jpg
# ==============================================================================
def make_fig_03():
    out_w, out_h = 1060, 460
    bg = Image.new('RGB', (out_w, out_h), '#ffffff')
    draw = ImageDraw.Draw(bg)
    
    # Left: A1 High Entropy (Chaotic Gaze Loop)
    crop_a1 = im_a1.crop((int(w1*0.45), int(h1*0.25), int(w1*0.95), int(h1*0.75))).resize((480, 240), Image.Resampling.LANCZOS)
    bg.paste(crop_a1, (30, 50))
    draw_card(draw, (30, 50, 510, 290), fill=None, outline='#dc2626', width=2, radius=4)
    
    # Left Label
    draw_card(draw, (40, 60, 250, 92), fill='#fee2e2', outline='#dc2626', width=1, radius=4)
    draw.text((50, 67), "A1 对照组：高认知摩擦", font=get_font(14, bold=True), fill='#991b1b')
    
    # Left Metrics
    draw_card(draw, (30, 305, 510, 430), fill='#fef2f2', outline='#fca5a5', width=1, radius=4)
    draw.text((45, 318), "信息熵 H(X) = 2.14 bits（混乱分散）", font=get_font(15, bold=True), fill='#991b1b')
    draw.text((45, 345), "• 密集大段长文本引发视线在词句间反复打转", font=get_font(13), fill='#334155')
    draw.text((45, 370), "• 认知阻力大，读者中途放弃率高达 80%", font=get_font(13), fill='#334155')
    draw.text((45, 395), "• 结论：高停留时长反映的是信息解码受阻而非深度阅读", font=get_font(13, bold=True), fill='#b91c1c')

    # Right: A2 Low Entropy (Structured Flow)
    crop_a2 = im_a2.crop((int(w2*0.43), int(h2*0.23), int(w2*0.95), int(h2*0.73))).resize((480, 240), Image.Resampling.LANCZOS)
    bg.paste(crop_a2, (550, 50))
    draw_card(draw, (550, 50, 1030, 290), fill=None, outline='#16a34a', width=2, radius=4)
    
    # Right Label
    draw_card(draw, (560, 60, 770, 92), fill='#dcfce7', outline='#16a34a', width=1, radius=4)
    draw.text((570, 67), "A2 改良组：低认知摩擦", font=get_font(14, bold=True), fill='#166534')
    
    # Right Metrics
    draw_card(draw, (550, 305, 1030, 430), fill='#f0fdf4', outline='#86efac', width=1, radius=4)
    draw.text((565, 318), "信息熵 H(X) = 1.48 bits（有序聚焦）", font=get_font(15, bold=True), fill='#166534')
    draw.text((565, 345), "• 感官气泡与模块化排版将视线精准导流至关键信息", font=get_font(13), fill='#334155')
    draw.text((565, 370), "• 认知阻力骤降，信息加工顺畅度提升 +63.5%", font=get_font(13), fill='#334155')
    draw.text((565, 395), "• 结论：模块化重构彻底消除了阅读死循环与视觉迷失", font=get_font(13, bold=True), fill='#15803d')

    bg.save('src/assets/images/entropy-fig-03-friction.jpg', quality=95)
    print("Generated entropy-fig-03-friction.jpg")

# ==============================================================================
# FIG 4: entropy-fig-04-surprisal.jpg
# ==============================================================================
def make_fig_04():
    out_w, out_h = 1060, 460
    bg = Image.new('RGB', (out_w, out_h), '#ffffff')
    draw = ImageDraw.Draw(bg)
    
    # Formula Bar at Top
    draw_card(draw, (30, 20, 1030, 90), fill='#f8fafc', outline='#cbd5e1', width=1.5, radius=4)
    draw.text((50, 32), "核心数学模型：", font=get_font(15, bold=True), fill='#0f172a')
    draw.text((170, 28), "I(x) = - log₂( P_prior(x) )", font=get_font(26, bold=True, mono=True), fill='#16a34a')
    draw.text((640, 38), "［ 自信息量 / 惊讶度（bits）：先验概率越低，消除的不确定性越大 ］", font=get_font(12), fill='#64748b')

    # Top Crop: A1 Conventional Taxonomy
    crop_a1 = im_a1.crop((int(w1*0.46), int(h1*0.30), int(w1*0.94), int(h1*0.55))).resize((480, 140), Image.Resampling.LANCZOS)
    bg.paste(crop_a1, (30, 110))
    draw_card(draw, (30, 110, 510, 250), fill=None, outline='#dc2626', width=1.5, radius=4)
    
    # Annotation for A1
    draw_card(draw, (530, 110, 1030, 250), fill='#fef2f2', outline='#fca5a5', width=1, radius=4)
    draw.text((550, 122), "示例文本 1：传统植物学科普说明", font=get_font(14, bold=True), fill='#991b1b')
    draw.text((550, 146), "“オシロイバナ科ブーゲンビレア属の熱帯性低木...” / “紫茉莉科木质藤本...”", font=get_font(13), fill='#334155')
    draw.text((550, 175), "• 变量演算：先验预期概率 P_prior = 0.75 (司空见惯)", font=get_font(13, bold=True), fill='#475569')
    draw.text((550, 202), "• 惊讶度 I = -log₂(0.75) = 0.415 bits  (低惊讶度 · 知识获得极低)", font=get_font(14, bold=True), fill='#dc2626')

    # Bottom Crop: A2 Tactile Sensory Bubble
    crop_a2 = im_a2.crop((int(w2*0.44), int(h2*0.24), int(w2*0.95), int(h2*0.58))).resize((480, 160), Image.Resampling.LANCZOS)
    bg.paste(crop_a2, (30, 280))
    draw_card(draw, (30, 280, 510, 440), fill=None, outline='#16a34a', width=2, radius=4)
    
    # Annotation for A2
    draw_card(draw, (530, 280, 1030, 440), fill='#f0fdf4', outline='#86efac', width=1.5, radius=4)
    draw.text((550, 292), "示例文本 2：身体感官触觉互动气泡 (R 原则)", font=get_font(14, bold=True), fill='#166534')
    draw.text((550, 316), "“赤い部分は花ではなく『苞』です！指で触ってカサカサ感を確かめよう”", font=get_font(13), fill='#334155')
    draw.text((550, 345), "• 变量演算：先验预期概率 P_prior = 0.12 (打破预期 · 反常识线索)", font=get_font(13, bold=True), fill='#475569')
    draw.text((550, 372), "• 惊讶度 I = -log₂(0.12) = 3.059 bits  (提高 7.37 倍！)", font=get_font(16, bold=True), fill='#16a34a')
    draw.text((550, 406), "➜ 彻底解答：为何观众即便只看 3 秒，也能牢牢记住核心植物知识！", font=get_font(12.5, bold=True), fill='#15803d')

    bg.save('src/assets/images/entropy-fig-04-surprisal.jpg', quality=95)
    print("Generated entropy-fig-04-surprisal.jpg")

# ==============================================================================
# FIG 5: entropy-fig-05-aoi-weights.jpg
# ==============================================================================
def make_fig_05():
    out_w, out_h = 1060, 460
    bg = Image.new('RGB', (out_w, out_h), '#ffffff')
    draw = ImageDraw.Draw(bg)
    
    # 4 Real Crops in 2x2 Grid
    # 1. A1 Text: (w1*0.46, h1*0.28, w1*0.94, h1*0.52)
    c1 = im_a1.crop((int(w1*0.46), int(h1*0.28), int(w1*0.94), int(h1*0.52))).resize((230, 140), Image.Resampling.LANCZOS)
    bg.paste(c1, (30, 40))
    draw_card(draw, (30, 40, 260, 180), fill=None, outline='#cbd5e1', width=1, radius=4)
    draw_card(draw, (270, 40, 520, 180), fill='#f8fafc', outline='#e2e8f0', width=1, radius=4)
    draw.text((282, 50), "传统分类学长文", font=get_font(14, bold=True), fill='#0f172a')
    draw.text((282, 75), "P_prior = 0.75", font=get_font(13, mono=True), fill='#64748b')
    draw.text((282, 100), "I = 0.415 bits", font=get_font(20, bold=True), fill='#64748b')
    draw.text((282, 140), "基础科属事实 · 泛化已知", font=get_font(12), fill='#94a3b8')

    # 2. A2 Tactile Bubble: (w2*0.44, h2*0.24, w2*0.95, h2*0.58)
    c2 = im_a2.crop((int(w2*0.44), int(h2*0.24), int(w2*0.95), int(h2*0.58))).resize((230, 140), Image.Resampling.LANCZOS)
    bg.paste(c2, (550, 40))
    draw_card(draw, (550, 40, 780, 180), fill=None, outline='#16a34a', width=2, radius=4)
    draw_card(draw, (790, 40, 1030, 180), fill='#f0fdf4', outline='#86efac', width=1.5, radius=4)
    draw.text((802, 50), "身体感官触觉气泡 (R)", font=get_font(14, bold=True), fill='#166534')
    draw.text((802, 75), "P_prior = 0.12", font=get_font(13, mono=True), fill='#15803d')
    draw.text((802, 100), "I = 3.059 bits", font=get_font(20, bold=True), fill='#16a34a')
    draw.text((802, 140), "提高 7.37 倍 · 核心认知驱动", font=get_font(12, bold=True), fill='#15803d')

    # 3. A2 Dialogue: (w2*0.05, h2*0.22, w2*0.44, h2*0.55)
    c3 = im_a2.crop((int(w2*0.05), int(h2*0.22), int(w2*0.44), int(h2*0.55))).resize((230, 140), Image.Resampling.LANCZOS)
    bg.paste(c3, (30, 240))
    draw_card(draw, (30, 240, 260, 380), fill=None, outline='#cbd5e1', width=1, radius=4)
    draw_card(draw, (270, 240, 520, 380), fill='#f8fafc', outline='#e2e8f0', width=1, radius=4)
    draw.text((282, 250), "拟人化对话引导", font=get_font(14, bold=True), fill='#0f172a')
    draw.text((282, 275), "P_prior = 0.15", font=get_font(13, mono=True), fill='#64748b')
    draw.text((282, 300), "I = 2.737 bits", font=get_font(20, bold=True), fill='#0f172a')
    draw.text((282, 340), "情境代入 · 建立情感联结", font=get_font(12), fill='#64748b')

    # 4. A2 Footer: (w2*0.05, h2*0.85, w2*0.50, h2*0.96)
    c4 = im_a2.crop((int(w2*0.05), int(h2*0.85), int(w2*0.50), int(h2*0.96))).resize((230, 140), Image.Resampling.LANCZOS)
    bg.paste(c4, (550, 240))
    draw_card(draw, (550, 240, 780, 380), fill=None, outline='#cbd5e1', width=1, radius=4)
    draw_card(draw, (790, 240, 1030, 380), fill='#f8fafc', outline='#e2e8f0', width=1, radius=4)
    draw.text((802, 250), "底部花语文化提示", font=get_font(14, bold=True), fill='#0f172a')
    draw.text((802, 275), "P_prior = 0.25", font=get_font(13, mono=True), fill='#64748b')
    draw.text((802, 300), "I = 2.000 bits", font=get_font(20, bold=True), fill='#0f172a')
    draw.text((802, 340), "人文趣味 · 补充知识延展", font=get_font(12), fill='#64748b')

    # Bottom Summary
    draw_card(draw, (30, 400, 1030, 444), fill='#f0fdf4', outline='#bbf7d0', width=1, radius=4)
    draw.text((50, 412), "量化发现：", font=get_font(14, bold=True), fill='#166534')
    draw.text((130, 413), "身体感官互动气泡以 3.059 bits 成为全标牌信息量密度最高的 Hero 知识锚点！", font=get_font(13.5), fill='#15803d')

    bg.save('src/assets/images/entropy-fig-05-aoi-weights.jpg', quality=95)
    print("Generated entropy-fig-05-aoi-weights.jpg")

# ==============================================================================
# FIG 6: entropy-fig-06-egain-walkthrough.jpg
# ==============================================================================
def make_fig_06():
    out_w, out_h = 1060, 460
    bg = Image.new('RGB', (out_w, out_h), '#ffffff')
    draw = ImageDraw.Draw(bg)
    
    # Left: Full A2 Real Sign with AOI Overlays
    crop_a2 = im_a2.resize((480, 340), Image.Resampling.LANCZOS)
    bg.paste(crop_a2, (30, 40))
    draw_card(draw, (30, 40, 510, 380), fill=None, outline='#16a34a', width=2, radius=4)
    
    # Overlay badges on top of A2
    draw_card(draw, (50, 55, 170, 85), fill='#16a34a', outline='#ffffff', width=1, radius=3)
    draw.text((60, 62), "① 标题区 (p1)", font=get_font(12, bold=True), fill='#ffffff')

    draw_card(draw, (50, 140, 170, 170), fill='#16a34a', outline='#ffffff', width=1, radius=3)
    draw.text((60, 147), "② 照片区 (p2)", font=get_font(12, bold=True), fill='#ffffff')

    draw_card(draw, (260, 140, 490, 170), fill='#dc2626', outline='#ffffff', width=1, radius=3)
    draw.text((270, 147), "③ 触觉感官气泡 (p3)", font=get_font(12, bold=True), fill='#ffffff')

    draw_card(draw, (50, 320, 170, 350), fill='#16a34a', outline='#ffffff', width=1, radius=3)
    draw.text((60, 327), "④ 花语区 (p4)", font=get_font(12, bold=True), fill='#ffffff')

    # Right: Step-by-Step E_gain Calculation
    draw_card(draw, (530, 40, 1030, 380), fill='#f8fafc', outline='#cbd5e1', width=1.5, radius=4)
    draw.text((550, 52), "逐区域加权演算过程：", font=get_font(15, bold=True), fill='#0f172a')
    
    steps = [
        ("① 标题区：", "p₁ = 15% × I₁ (1.80 bits)", "= 0.270 bits", "#334155"),
        ("② 植物照片：", "p₂ = 30% × I₂ (0.80 bits)", "= 0.240 bits", "#334155"),
        ("③ 触觉气泡 (R)：", "p₃ = 35% × I₃ (3.06 bits)", "= 1.071 bits", "#16a34a"),
        ("④ 花语提示：", "p₄ = 20% × I₄ (2.00 bits)", "= 0.400 bits", "#334155")
    ]
    
    y = 88
    for label, formula, result, col in steps:
        draw.text((550, y), label, font=get_font(13.5, bold=True), fill='#0f172a')
        draw.text((670, y), formula, font=get_font(13.5, mono=True), fill='#475569')
        draw.text((890, y), result, font=get_font(14, bold=True, mono=True), fill=col)
        y += 38

    draw.line((550, 246, 1010, 246), fill='#cbd5e1', width=1)
    
    draw.text((550, 260), "改良组 E_gain 总量 =", font=get_font(15, bold=True), fill='#166534')
    draw.text((740, 255), "1.981 bits", font=get_font(24, bold=True, mono=True), fill='#16a34a')
    draw.text((550, 298), "对照组 E_gain 总量 = 0.585 bits（低质自循环）", font=get_font(13.5), fill='#64748b')
    draw.text((550, 328), "➜ 净认知增益提升 +127.7% ~ +241.0% (p < 0.001)", font=get_font(14, bold=True), fill='#15803d')

    # Bottom Banner
    draw_card(draw, (30, 398, 1030, 444), fill='#f0fdf4', outline='#bbf7d0', width=1, radius=4)
    draw.text((50, 410), "核心结论：", font=get_font(14, bold=True), fill='#166534')
    draw.text((130, 411), "E_gain 成功将『看哪里的时间』与『该处的新知价值』结合，真实度量了知识获取的质与量！", font=get_font(13.5), fill='#15803d')

    bg.save('src/assets/images/entropy-fig-06-egain-walkthrough.jpg', quality=95)
    print("Generated entropy-fig-06-egain-walkthrough.jpg")

# ==============================================================================
# FIG 7: entropy-fig-07-markov-flow.jpg
# ==============================================================================
def make_fig_07():
    out_w, out_h = 1060, 460
    bg = Image.new('RGB', (out_w, out_h), '#ffffff')
    draw = ImageDraw.Draw(bg)
    
    # Left: A1 93% Loop
    crop_a1 = im_a1.crop((int(w1*0.44), int(h1*0.18), int(w1*0.96), int(h1*0.82))).resize((480, 270), Image.Resampling.LANCZOS)
    bg.paste(crop_a1, (30, 40))
    draw_card(draw, (30, 40, 510, 310), fill=None, outline='#dc2626', width=2, radius=4)
    
    # 93% Loop Overlay
    draw_card(draw, (180, 110, 360, 180), fill='#fee2e2', outline='#dc2626', width=2, radius=8)
    draw.text((200, 122), "P(Text|Text) =", font=get_font(13, bold=True), fill='#991b1b')
    draw.text((220, 142), "93% 死循环", font=get_font(20, bold=True), fill='#b91c1c')

    draw_card(draw, (30, 325, 510, 435), fill='#fef2f2', outline='#fca5a5', width=1, radius=4)
    draw.text((45, 338), "A1 对照组：长文本阅读陷阱 (93%)", font=get_font(14, bold=True), fill='#991b1b')
    draw.text((45, 365), "• 视线在正文内反复自旋转移，跳出正文去往图片的概率仅 4%", font=get_font(13), fill='#334155')
    draw.text((45, 390), "• 形成封闭的信息孤岛，无法形成图文互证的联想学习", font=get_font(13), fill='#334155')

    # Right: A2 Branching Flow
    crop_a2 = im_a2.crop((int(w2*0.42), int(h2*0.18), int(w2*0.96), int(h2*0.82))).resize((480, 270), Image.Resampling.LANCZOS)
    bg.paste(crop_a2, (550, 40))
    draw_card(draw, (550, 40, 1030, 310), fill=None, outline='#16a34a', width=2, radius=4)
    
    # 56% Drop Overlay
    draw_card(draw, (700, 110, 880, 180), fill='#dcfce7', outline='#16a34a', width=2, radius=8)
    draw.text((720, 122), "自循环停滞率降至", font=get_font(13, bold=True), fill='#166534')
    draw.text((740, 142), "56% (多向导流)", font=get_font(20, bold=True), fill='#15803d')

    draw_card(draw, (550, 325, 1030, 435), fill='#f0fdf4', outline='#86efac', width=1, radius=4)
    draw.text((565, 338), "A2 改良组：多模态认知导流网络 (56%)", font=get_font(14, bold=True), fill='#166534')
    draw.text((565, 365), "• 视线平稳自正文分流至感官气泡 (0.19)、图标 (0.13) 与花语 (0.38)", font=get_font(13), fill='#334155')
    draw.text((565, 390), "• 停滞率显著下降 -39.8% (p < 0.001)，构建良性探索生态", font=get_font(13, bold=True), fill='#15803d')

    bg.save('src/assets/images/entropy-fig-07-markov-flow.jpg', quality=95)
    print("Generated entropy-fig-07-markov-flow.jpg")

# ==============================================================================
# FIG 8: entropy-fig-08-eta-efficiency.jpg
# ==============================================================================
def make_fig_08():
    out_w, out_h = 1060, 460
    bg = Image.new('RGB', (out_w, out_h), '#ffffff')
    draw = ImageDraw.Draw(bg)
    
    # Formula Top Card
    draw_card(draw, (30, 20, 1030, 85), fill='#f8fafc', outline='#cbd5e1', width=1.5, radius=4)
    draw.text((50, 30), "认知能效比模型：", font=get_font(15, bold=True), fill='#0f172a')
    draw.text((180, 26), "η = E_gain / ( H_GTE + ε )", font=get_font(24, bold=True, mono=True), fill='#16a34a')
    draw.text((620, 36), "［ 单位视觉搜索努力换取的净知识增量（bits/bit）］", font=get_font(13), fill='#64748b')

    # Left: Comparison Bar Chart / Visual
    draw_card(draw, (30, 105, 510, 380), fill='#ffffff', outline='#e2e8f0', width=1.5, radius=4)
    draw.text((50, 120), "实证能效比对比 (Group A & B, N=13)", font=get_font(15, bold=True), fill='#0f172a')
    
    # Control Bar
    draw.text((50, 160), "A1 对照组：η = 1.083", font=get_font(14, bold=True), fill='#64748b')
    draw_card(draw, (50, 185, 280, 220), fill='#cbd5e1', outline='#94a3b8', width=1, radius=4)
    draw.text((290, 192), "1.083 ± 0.439", font=get_font(13, mono=True), fill='#64748b')

    # Experiment Bar
    draw.text((50, 245), "A2 改良组：η = 1.407 (+29.9% 提升)", font=get_font(14, bold=True), fill='#166534')
    draw_card(draw, (50, 270, 370, 305), fill='#16a34a', outline='#15803d', width=1, radius=4)
    draw.text((380, 277), "1.407 ± 0.347", font=get_font(13, bold=True, mono=True), fill='#16a34a')

    draw.text((50, 335), "配对 t 检验：t(12) = 3.540, p = 0.004, Cohen's d = 0.982", font=get_font(13, bold=True), fill='#0f172a')

    # Right: Insight Explanation Card
    draw_card(draw, (530, 105, 1030, 380), fill='#f0fdf4', outline='#86efac', width=1.5, radius=4)
    draw.text((550, 120), "能效跃升的核心学术意义：", font=get_font(15, bold=True), fill='#166534')
    
    insights = [
        ("• 并非单纯堆砌信息：", "改良组并没有增加游客的阅读负担，而是优化了信息组织"),
        ("• 减少无序搜索负荷：", "分母 H_GTE 保持在合理水平，避免了视线迷失与认知超载"),
        ("• 显著提升有效吸收：", "分子 E_gain 大幅提升，让每一次注视都产生实质知识增益"),
        ("• 真正实现『减负增效』：", "用更少、更舒适的视觉消耗，换取更高价值的新知体验！")
    ]
    
    y = 160
    for h_txt, b_txt in insights:
        draw.text((550, y), h_txt, font=get_font(13.5, bold=True), fill='#15803d')
        draw.text((550, y + 22), b_txt, font=get_font(13), fill='#334155')
        y += 50

    # Bottom Summary
    draw_card(draw, (30, 398, 1030, 444), fill='#f8fafc', outline='#cbd5e1', width=1, radius=4)
    draw.text((50, 410), "学术评价：", font=get_font(14, bold=True), fill='#0f172a')
    draw.text((130, 411), "该指标成功将眼动研究从『描述性行为统计』提升至『认知能效定量评价』新高度。", font=get_font(13.5), fill='#475569')

    bg.save('src/assets/images/entropy-fig-08-eta-efficiency.jpg', quality=95)
    print("Generated entropy-fig-08-eta-efficiency.jpg")

make_fig_01()
make_fig_02()
make_fig_03()
make_fig_04()
make_fig_05()
make_fig_06()
make_fig_07()
make_fig_08()
