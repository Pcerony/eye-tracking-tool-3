const fs = require('fs');
const path = require('path');

const indexHtmlPath = path.join(__dirname, '../ppt/index.html');
let content = fs.readFileSync(indexHtmlPath, 'utf8');

const startMarker = '<section class="slide accent" data-chapter="1"';
const endMarker = '</div>\n</main>';

const startIndex = content.indexOf(startMarker);
const endIndex = content.indexOf(endMarker);

if (startIndex === -1 || endIndex === -1) {
  console.error("Could not find markers");
  process.exit(1);
}

const newSlides = `
<section class="slide accent" data-chapter="1" data-chapter-title="研究背景" data-short-title="研究主题" data-layout="SWISS-COVER-ASCII" data-animate="hero">
  <div class="canvas-card">
    <canvas class="ascii-bg" aria-hidden="true"></canvas>
    <div class="chrome-min">
      <div class="l" style="pointer-events: auto; display: flex; align-items: center; gap: 8px;">
        <span class="lang-top-label" style="opacity: 0.6; font-size: 11px;">Language:</span>
        <button class="lang-top-btn" onclick="applyLanguage('zh')">ZH</button>
        <button class="lang-top-btn" onclick="applyLanguage('en')">EN</button>
        <button class="lang-top-btn" onclick="applyLanguage('ja')">JA</button>
        <button class="lang-top-btn" onclick="applyLanguage('es-MX')">ES</button>
      </div>
      <div class="r">INTERIM RELEASE · 2026.06 · 01 / 09</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr auto;gap:2.6vh">
      <div data-anim="kicker" class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em">INTERIM REPORT · A/R DESIGN & EYE-TRACKING</div>
      <h1 data-anim="title" style="align-self:center;font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(4.7vw,8.2vh);line-height:1.02;letter-spacing:0;color:#fff;max-width:17ch;hyphens:none">关于用于设计解说标识的共创工具的研究<br/><span style="display:block;margin-top:1.1vh;font-size:.46em;line-height:1.08;letter-spacing:0">以福冈市植物园温室区域为例</span></h1>
      <div data-anim="bottom" style="display:grid;grid-template-rows:auto auto;gap:1.6vh;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh">
        <div class="lead" style="max-width:54ch;color:rgba(255,255,255,.86);font-weight:300">植物解说标识的 A/R/S 设计改良与眼动评估实验分析 (中间发表)</div>
        <div style="display:flex;gap:1.4vw;align-items:center;color:rgba(255,255,255,.76);font-family:var(--mono);font-size:14px;letter-spacing:.16em;text-transform:uppercase">
          <span style="display:inline-flex;align-items:center;gap:.5em"><i data-lucide="leaf" style="width:18px;height:18px;stroke-width:1.6"></i>Plant</span>
          <span style="display:inline-flex;align-items:center;gap:.5em"><i data-lucide="eye" style="width:18px;height:18px;stroke-width:1.6"></i>Gaze</span>
          <span style="display:inline-flex;align-items:center;gap:.5em"><i data-lucide="signpost" style="width:18px;height:18px;stroke-width:1.6"></i>Signage</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:end">
          <div class="t-meta" style="color:rgba(255,255,255,.6)">PINGCHENG WANG · 2026.06</div>
          <div class="t-meta" style="color:rgba(255,255,255,.6)">INTERIM RESEARCH REPORT</div>
        </div>
      </div>
    </div>
</section>

<section class="slide" data-chapter="1" data-chapter-title="研究背景" data-short-title="现实课题" data-layout="S22" data-animate="image-hero">
  <div class="canvas-card" style="padding:0;display:flex;flex-direction:column;overflow:hidden">
    <div data-anim="img" style="position:relative;flex:0 0 58%;overflow:hidden;background:var(--grey-1)">
      <img src="images/01-field-observation.jpg" data-image-slot="s22-hero-21x9" alt="福冈市植物园温室实地环境" loading="eager" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 42%">
      <div class="chrome-min" style="position:absolute;top:0;left:0;right:0;color:rgba(255,255,255,.9);padding:5.6vh 5vw 0">
        <div class="l">CONTEXT & PROBLEM STATEMENT</div><div class="r">02 / 09</div>
      </div>
      <div data-anim="title-block" style="position:absolute;left:5vw;top:11vh;background:var(--paper);padding:3vh 3vw;max-width:42vw">
        <div style="display:flex;align-items:center;gap:1vw;margin-bottom:1.6vh;color:var(--accent)"><i data-lucide="leaf" style="width:28px;height:28px;stroke-width:1.5"></i><i data-lucide="eye" style="width:28px;height:28px;stroke-width:1.5"></i></div>
        <div style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(4.8vw,8.2vh);line-height:1;letter-spacing:-.03em;color:var(--text-primary)">高设置、低阅读：<br/>非正式学习的现实困境</div>
      </div>
    </div>
    <div data-anim="kpi" class="image-hero-body">
      <div style="max-width:48ch;font-family:var(--sans),var(--sans-zh);font-size:max(18px,1.25vw);line-height:1.55;font-weight:400;color:var(--text-primary)">
        <strong>研究目的：</strong>作为温室环境中的非正式学习界面，解说标识往往面临“高设置、低阅读”的困境。大量长文本信息未被视线有效覆盖。本研究旨在探讨如何通过设计干预，重新组织视觉注意力，缩短阅读决策路径。
      </div>
      <div class="image-hero-stats" style="gap:3vw">
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">SITE</div><div style="font-family:var(--sans);font-weight:200;font-size:min(4vw,7vh);line-height:.95;letter-spacing:-.035em">福冈市植物园</div><p class="body-sm" style="margin-top:auto">温室区非正式学习环境</p></div>
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">ISSUE</div><div style="font-family:var(--sans);font-weight:200;font-size:min(3vw,5vh);line-height:.98;letter-spacing:-.03em">被设置 ≠ 被阅读</div><p class="body-sm" style="margin-top:auto">来园者多处于随机浏览状态</p></div>
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">APPROACH</div><div style="font-family:var(--sans);font-weight:200;font-size:min(3vw,5vh);line-height:.95;letter-spacing:-.035em;color:var(--accent)">眼动分析</div><p class="body-sm" style="margin-top:auto">通过视线追踪获取客观数据</p></div>
      </div>
    </div>
  </div>
</section>

<section class="slide" data-chapter="2" data-chapter-title="研究方法" data-short-title="A/R/S 原则" data-layout="S05" data-animate="sub-stack">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">METHODOLOGY · A/R/S DESIGN PRINCIPLES</div><div class="r">03 / 09</div></div>
    <div style="display:grid;grid-template-columns:4fr 8fr;gap:4vw;flex:1;min-height:0">
      <div style="display:flex;flex-direction:column;gap:2vh">
        <h2 class="h-xl-zh" style="font-size:min(4.8vw,8.5vh)">A/R/S 解说标识设计原则假说</h2>
        <p class="t-body">A/R/S 是一套基于先前阶段研究提炼而成的解说标识设计原则，旨在通过氛围、关联与结构的维度改良，预期能够显著提升来园者的标识阅读意愿与非正式学习体验。这些原则构成了本研究中<strong>改良组标识</strong>的设计基础。</p>
      </div>
      <div class="stack-row" style="margin-top:0">
        <article class="stack-block b-grey"><div class="layer-nb">A · 01</div><i data-lucide="leaf"></i><h3 class="layer-ttl">启发性氛围</h3><p class="layer-desc">通过提问、叙事和植物情境提示，建立“为什么值得看”的入口。</p><div class="layer-tag">Plant Atmosphere</div></article>
        <article class="stack-block b-accent"><div class="layer-nb">R · 02</div><i data-lucide="users"></i><h3 class="layer-ttl">观众关联性</h3><p class="layer-desc">把植物特征连接到触摸、用途、感官经验和行动可能性。</p><div class="layer-tag">Audience Relevance</div></article>
        <article class="stack-block b-ink"><div class="layer-nb">S · 03</div><i data-lucide="signpost"></i><h3 class="layer-ttl">结构清晰性</h3><p class="layer-desc">用标识层级与视觉分区降低读解负荷，支撑关键区域可达。</p><div class="layer-tag">Signage Structure</div></article>
      </div>
    </div>
  </div>
</section>

<section class="slide" data-chapter="2" data-chapter-title="研究方法" data-short-title="实验刺激" data-layout="S16" data-animate="field-notes">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">METHODOLOGY · STIMULUS MATERIAL</div><div class="r">04 / 09</div></div>
    <div style="display:flex;justify-content:space-between;align-items:end;gap:3vw">
      <div style="display:flex;flex-direction:column;gap:1.2vh">
        <h2 class="h-xl-zh" style="font-size:min(4.4vw,7.8vh)">实验组与对照组</h2>
      </div>
    </div>
    <div class="slide5-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:1.6vw;flex:1;min-height:0;margin-top:2.6vh">
      <article class="card-fill" style="padding:1.4vh 1.1vw 1.2vh;display:flex;flex-direction:column;gap:1vh;min-height:0">
        <div style="display:flex;justify-content:space-between;align-items:center"><div class="t-meta">对照组</div><div class="t-body-sm">信息混杂在单一长文本中</div></div>
        <div style="flex:1;min-height:0;position:relative;background:#fff">
          <div style="position:absolute;top:0;left:0;right:0;bottom:0;display:flex;justify-content:center;align-items:center">
            <div class="frame-img sign-aoi fit-contain" style="position:relative;width:100%;max-height:100%">
              <img src="images/06-control-sign.jpg" data-image-slot="s16-brief-16x10" alt="对照版标识">
            </div>
          </div>
        </div>
      </article>
      <article class="card-fill" style="padding:1.4vh 1.1vw 1.2vh;display:flex;flex-direction:column;gap:1vh;min-height:0;border-top:2px solid var(--accent)">
        <div style="display:flex;justify-content:space-between;align-items:center"><div class="t-meta">实验组 (A/R/S)</div><div class="t-body-sm">应用 A/R 原则进行独立分区设计</div></div>
        <div style="flex:1;min-height:0;position:relative;background:#fff">
          <div style="position:absolute;top:0;left:0;right:0;bottom:0;display:flex;justify-content:center;align-items:center">
            <div class="frame-img sign-aoi fit-contain" style="position:relative;width:100%;max-height:100%">
              <img src="images/07-intervention-sign.jpg" data-image-slot="s16-brief-16x10" alt="实验版标识">
            </div>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="slide" data-chapter="2" data-chapter-title="研究方法" data-short-title="视线工具" data-layout="S16" data-animate="field-notes">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">METHODOLOGY · NON-CONTACT GAZE TRACKING TOOL & AOI</div><div class="r">05 / 09</div></div>
    <div style="display:grid;grid-template-columns:5fr 7fr;gap:2.4vw;flex:1;min-height:0">
      <div style="display:flex;flex-direction:column;gap:1.2vh;min-height:0">
        <div class="t-meta">实验现场 · 福冈市植物园温室</div>
        <div class="frame-img fit-contain swiss-lined" style="flex:1;min-height:0">
          <img src="images/02-experiment-scene.jpg" alt="实验现场中的非接触眼动记录">
        </div>
        <div class="t-body-sm" style="border-top:1px solid var(--border-subtle);padding-top:.8vh">基于 WebGazer 开发的 SIGN Visual Attention v3。样本：9名有效受试者。</div>
      </div>
      <div style="display:flex;flex-direction:column;gap:1.8vh">
        <h2 class="h-xl-zh" style="font-size:min(4vw,7vh)">数据采集：从视线轨迹到数据分析</h2>
        <div style="display:flex;flex-direction:column;gap:1.4vh;flex:1">
          <article class="card-fill" style="padding:1.6vh 1.2vw;display:flex;flex-direction:column;gap:.8vh">
            <div style="display:flex;align-items:center;gap:.8vw;color:var(--accent)"><i data-lucide="camera" style="width:20px;height:20px;stroke-width:1.7"></i><div class="t-meta">非接触式记录</div></div>
            <p class="t-body-sm">用普通网络摄像头实时捕获面部图像，AI推算视线在屏幕上的坐标。无需佩戴沉重设备，还原自然阅读状态。</p>
          </article>
          <article class="card-fill" style="padding:1.6vh 1.2vw;display:flex;flex-direction:column;gap:.8vh">
            <div style="display:flex;align-items:center;gap:.8vw;color:var(--accent)"><i data-lucide="palette" style="width:20px;height:20px;stroke-width:1.7"></i><div class="t-meta">热力图生成 (Heatmap)</div></div>
            <p class="t-body-sm">将视线坐标映射回纸面标识上，视线密集停留的地方显示为暖色（红/橙），快速扫过的地方显示为冷色。</p>
          </article>
          <article class="card-accent" style="padding:1.6vh 1.2vw;display:flex;flex-direction:column;gap:.8vh">
            <div style="display:flex;align-items:center;gap:.8vw;color:var(--accent-on)"><i data-lucide="crosshair" style="width:20px;height:20px;stroke-width:1.7"></i><div class="t-meta" style="color:var(--accent-on)">AOI (关注区域) 分析</div></div>
            <p class="t-body-sm" style="color:var(--accent-on);opacity:.9">在标识上划定特定语义区域（如氛围区、关联区），统计落入该区域的注视点比例。所有结果的定量分析均基于 AOI 的百分比数据。</p>
          </article>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="slide" data-chapter="3" data-chapter-title="初步分析结果" data-short-title="早期覆盖与注意重组" data-layout="S06" data-animate="tower-grow">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">QUICK DATA · Q1 & Q2 EARLY COVERAGE AND REORGANIZATION</div><div class="r">06 / 09</div></div>
    <div style="display:flex;flex-direction:column;gap:1.4vh">
      <h2 class="h-xl-zh" style="font-size:min(4.4vw,7.8vh)">初步分析 (1)：前10秒完读率与注意重组</h2>
    </div>
    <div class="chart-box" style="flex:1;display:flex;gap:3vw;margin-top:2vh">
      <div style="flex:1;display:flex;flex-direction:column">
        <h3 class="t-h-prod" style="margin-bottom:1.4vh">Q1: 完读率提升（前10秒）</h3>
        <p class="t-body-sm" style="margin-bottom:2vh">改良版在早期的阅读窗口中提升了文字区域覆盖率，有效缩短了阅读决策路径。</p>
        <div class="bar-chart vert" style="flex:1;display:flex;align-items:flex-end;gap:2vw;justify-content:center;padding-bottom:4vh">
          <div class="bar-col" style="height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:1vh">
            <div class="bar-val" style="font-family:var(--mono);font-size:1.8vw">38.6%</div>
            <div class="bar-fill" style="width:4vw;height:38%;background:var(--grey-3)"></div>
            <div class="t-meta">对照组</div>
          </div>
          <div class="bar-col" style="height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:1vh">
            <div class="bar-val" style="font-family:var(--mono);font-size:1.8vw;color:var(--accent)">45.3%</div>
            <div class="bar-fill" style="width:4vw;height:45%;background:var(--accent)"></div>
            <div class="t-meta">实验组 (A/R/S)</div>
          </div>
        </div>
      </div>
      <div style="width:1px;background:var(--border-subtle)"></div>
      <div style="flex:1;display:flex;flex-direction:column">
        <h3 class="t-h-prod" style="margin-bottom:1.4vh">Q2: 注意力重组到目标区域（全程）</h3>
        <p class="t-body-sm" style="margin-bottom:2vh">全程文字覆盖率虽略有下降，但视线成功从无关区域转移至 A/R 目标语义区。</p>
        <div class="bar-chart vert" style="flex:1;display:flex;align-items:flex-end;gap:2vw;justify-content:center;padding-bottom:4vh">
          <div class="bar-col" style="height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:1vh">
            <div class="bar-val" style="font-family:var(--mono);font-size:1.8vw">45.0%</div>
            <div class="bar-fill" style="width:4vw;height:45%;background:var(--grey-3)"></div>
            <div class="t-meta">对照组 A/R区占比</div>
          </div>
          <div class="bar-col" style="height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:1vh">
            <div class="bar-val" style="font-family:var(--mono);font-size:1.8vw;color:var(--accent)">60.2%</div>
            <div class="bar-fill" style="width:4vw;height:60%;background:var(--accent)"></div>
            <div class="t-meta">实验组 A/R区占比</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="slide" data-chapter="3" data-chapter-title="初步分析结果" data-short-title="R 原则效应" data-layout="S20" data-animate="stacked-ledger">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">QUICK DATA · Q3 R-PRINCIPLE EFFICACY</div><div class="r">07 / 09</div></div>
    <div style="display:flex;flex-direction:column;gap:1.4vh">
      <h2 class="h-xl-zh" style="font-size:min(4.8vw,8.5vh)">初步分析 (2)：R 原则产生最强、最稳定效应</h2>
    </div>
    <div style="display:grid;grid-template-columns:4fr 8fr;gap:4vw;margin-top:3vh;flex:1">
      <div style="display:flex;flex-direction:column;gap:1.4vh">
        <p class="t-body">通过单独分析各区域的注意力增幅，我们发现 <strong>R 原则（观众关联性）</strong> 在设计干预中发挥了核心作用。</p>
        <div style="background:var(--grey-1);padding:2vh 1.4vw;margin-top:1vh">
          <div class="t-meta" style="color:var(--accent)">FINDING</div>
          <p class="t-body-sm" style="margin-top:1vh">前 10 秒窗口内，R 区的注视占比从 5.0% 激增至 21.4%。同时，9 名有效样本的个体数据显示，R 原则具有极高的普适性和稳定性，其效应在不同来园者群体中一致出现。</p>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;gap:2vh">
        <div class="ledger-row" style="display:grid;grid-template-columns:3fr 1fr 1fr;gap:2vw;border-bottom:1px solid var(--border-subtle);padding-bottom:1vh">
          <div class="t-meta">评估指标 (全程 R 区占比)</div>
          <div class="t-meta" style="text-align:right">对照组</div>
          <div class="t-meta" style="text-align:right;color:var(--accent)">实验组</div>
        </div>
        <div class="ledger-row" style="display:grid;grid-template-columns:3fr 1fr 1fr;gap:2vw;padding:1vh 0">
          <div class="t-body-sm" style="font-weight:600">全程 R 区注意力占比平均值</div>
          <div class="t-body-sm" style="text-align:right;font-family:var(--mono)">8.5%</div>
          <div class="t-body-sm" style="text-align:right;font-family:var(--mono);color:var(--accent);font-weight:600">35.1% (+26.6%)</div>
        </div>
        <div class="ledger-row" style="display:grid;grid-template-columns:3fr 1fr 1fr;gap:2vw;padding:1vh 0;border-top:1px dashed var(--border-subtle)">
          <div class="t-body-sm" style="font-weight:600">前 10 秒 R 区注意力占比</div>
          <div class="t-body-sm" style="text-align:right;font-family:var(--mono)">5.0%</div>
          <div class="t-body-sm" style="text-align:right;font-family:var(--mono);color:var(--accent);font-weight:600">21.4% (+16.4%)</div>
        </div>
        <div class="ledger-row" style="display:grid;grid-template-columns:3fr 1fr 1fr;gap:2vw;padding:1vh 0;border-top:1px solid var(--border-subtle)">
          <div class="t-body-sm" style="font-weight:600">9 名样本中呈现 R 区上升的人数</div>
          <div class="t-body-sm" style="text-align:right;font-family:var(--mono)">-</div>
          <div class="t-body-sm" style="text-align:right;font-family:var(--mono);color:var(--accent);font-weight:600">9 / 9 (100%)</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="slide split" data-chapter="4" data-chapter-title="后续计划" data-short-title="Future Plan" data-layout="SWISS-CLOSING-ASCII" data-animate="split-statement">
  <div class="canvas-card">
    <div class="split-half">
      <div class="half b-accent" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between;position:relative;overflow:hidden">
        <canvas class="ascii-bg" aria-hidden="true"></canvas>
        <div class="chrome-min" style="margin-bottom:0;position:relative;z-index:1"><div class="l">08 / 09</div><div class="r">FUTURE PLAN</div></div>
        <div data-anim="manifesto" style="display:flex;flex-direction:column;gap:2vh;position:relative;z-index:1">
          <h2 class="slide16-title" style="font-family:var(--sans),var(--sans-zh);font-size:min(7.4vw,13vh);line-height:.96;letter-spacing:-.025em;font-weight:200;color:#fff">研究展望：<br/>从<span style="font-style:italic;font-weight:300">Quick Data</span>到最终论文</h2>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(16px,1vw);line-height:1.6;color:rgba(255,255,255,.82);font-weight:400;max-width:38ch;margin-top:1.4vh">本次中间发表展示的 A/R/S 的核心价值并非修饰版面，而是系统性重构注意力。目前的 Quick Data 证实了早期的研究干预是有效的。</div>
        </div>
        <div data-anim="signature" style="display:flex;justify-content:space-between;align-items:end;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh;position:relative;z-index:1"><div class="t-meta" style="color:rgba(255,255,255,.62)">INTERIM REPORT</div><div class="t-meta" style="color:rgba(255,255,255,.62)">2026.06</div></div>
      </div>
      <div class="half" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between">
        <div class="chrome-min"><div class="l">NEXT STEPS</div><div class="r">FUTURE RESEARCH PLAN</div></div>
        <div data-anim="rules" style="display:flex;flex-direction:column;gap:2.2vh">
          <div style="display:grid;grid-template-columns:4em 1fr;gap:1.4vw;border-top:1px solid var(--border-subtle);padding-top:2vh"><div class="t-meta">STEP 1</div><div><h3 class="t-h-prod">全面数据分析 (2026.08)</h3><p class="t-body-sm">基于剩余受试者的数据扩大有效样本量。执行严谨的统计学假设检验（ANOVA 等），将探索性发现转化为统计推断结论。</p></div></div>
          <div style="display:grid;grid-template-columns:4em 1fr;gap:1.4vw;border-top:1px solid var(--border-subtle);padding-top:2vh"><div class="t-meta">STEP 2</div><div><h3 class="t-h-prod">指标细化与模型构建 (2026.09)</h3><p class="t-body-sm">引入 Fixation Duration 和 Saccade Amplitude 等更细致的眼动指标，结合受试者的个体差异（年龄等）构建更全面的认知模型。</p></div></div>
          <div style="display:grid;grid-template-columns:4em 1fr;gap:1.4vw;border-top:1px solid var(--accent);padding-top:2vh"><div class="t-meta" style="color:var(--accent)">STEP 3</div><div><h3 class="t-h-prod" style="color:var(--accent)">修士论文撰写 (2026.10)</h3><p class="t-body-sm">将从 GGJ 课题发掘、工具研发、到最终眼动评估实验的完整流程整理成学术论文，完成最终的修士论文档案与最终发表。</p></div></div>
        </div>
        <div data-anim="foot" class="t-meta" style="color:var(--text-helper);text-align:right">RESEARCH ROADMAP</div>
      </div>
    </div>
  </div>
</section>

<section class="slide" data-chapter="5" data-chapter-title="参考文献" data-short-title="References" data-layout="S16" data-animate="field-notes">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">REFERENCES</div><div class="r">09 / 09</div></div>
    <div style="display:flex;flex-direction:column;gap:1.4vh">
      <h2 class="h-xl-zh" style="font-size:min(4.8vw,8.5vh)">参考文献 (References)</h2>
    </div>
    <div style="display:flex;flex-direction:column;gap:1.6vh;margin-top:3vh;flex:1">
      <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:2vh">
        <li style="padding-bottom:1.5vh;border-bottom:1px solid var(--border-subtle)">
          <p class="t-body-sm" style="line-height:1.6"><strong>Papoutsaki, A., Sangkloy, P., Laskey, J., Alqassab, N., D'Alessandro, A., & Hays, J. (2016).</strong> WebGazer: Scalable Webcam Eye Tracking Using User Interactions. <i>Proceedings of the 25th International Joint Conference on Artificial Intelligence (IJCAI)</i>, 3839-3845.</p>
        </li>
        <li style="padding-bottom:1.5vh;border-bottom:1px solid var(--border-subtle)">
          <p class="t-body-sm" style="line-height:1.6"><strong>Bitgood, S. (2014).</strong> Engaging the Visitor: Designing Exhibits That Work. <i>MuseumsEtc</i>. Edinburgh, UK.</p>
        </li>
        <li style="padding-bottom:1.5vh;border-bottom:1px solid var(--border-subtle)">
          <p class="t-body-sm" style="line-height:1.6"><strong>Falk, J. H., & Dierking, L. D. (2000).</strong> Learning from Museums: Visitor Experiences and the Making of Meaning. <i>AltaMira Press</i>.</p>
        </li>
        <li style="padding-bottom:1.5vh;border-bottom:1px solid var(--border-subtle)">
          <p class="t-body-sm" style="line-height:1.6"><strong>Holmqvist, K., Nyström, M., Andersson, R., Dewhurst, R., Jarodzka, H., & Van de Weijer, J. (2011).</strong> Eye Tracking: A Comprehensive Guide to Methods and Measures. <i>Oxford University Press</i>.</p>
        </li>
        <li style="padding-bottom:1.5vh">
          <p class="t-body-sm" style="line-height:1.6;color:var(--text-secondary)"><i>* 其他相关文献及调查资料将在最终论文附录中详细列出。</i></p>
        </li>
      </ul>
    </div>
  </div>
</section>
`;

const newContent = content.substring(0, startIndex) + newSlides + content.substring(endIndex);
fs.writeFileSync(indexHtmlPath, newContent, 'utf8');
console.log('Slides successfully updated!');
