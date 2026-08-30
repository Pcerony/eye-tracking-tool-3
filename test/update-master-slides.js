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
<!-- Chapter 1: 研究背景与目的 -->
<section class="slide accent" data-chapter="1" data-chapter-title="研究背景与目的" data-short-title="研究主题" data-layout="SWISS-COVER-ASCII" data-animate="hero">
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
      <div class="r">MASTER'S REPORT · 2026.06 · 01 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr auto;gap:2.6vh">
      <div data-anim="kicker" class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em">INTERIM RESEARCH REPORT</div>
      <h1 data-anim="title" style="align-self:center;font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(4.7vw,8.2vh);line-height:1.02;letter-spacing:0;color:#fff;max-width:17ch;hyphens:none">关于用于设计解说标识的共创工具的研究<br/><span style="display:block;margin-top:1.1vh;font-size:.46em;line-height:1.08;letter-spacing:0">以福冈市植物园温室区域为例</span></h1>
      <div data-anim="bottom" style="display:grid;grid-template-rows:auto auto;gap:1.6vh;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh">
        <div class="lead" style="max-width:54ch;color:rgba(255,255,255,.86);font-weight:300">植物解说标识的 A/R/S 设计改良与眼动评估实验分析</div>
        <div style="display:flex;gap:1.4vw;align-items:center;color:rgba(255,255,255,.76);font-family:var(--mono);font-size:14px;letter-spacing:.16em;text-transform:uppercase">
          <span style="display:inline-flex;align-items:center;gap:.5em"><i data-lucide="leaf" style="width:18px;height:18px;stroke-width:1.6"></i>Plant</span>
          <span style="display:inline-flex;align-items:center;gap:.5em"><i data-lucide="eye" style="width:18px;height:18px;stroke-width:1.6"></i>Gaze</span>
          <span style="display:inline-flex;align-items:center;gap:.5em"><i data-lucide="signpost" style="width:18px;height:18px;stroke-width:1.6"></i>Signage</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:end">
          <div class="t-meta" style="color:rgba(255,255,255,.6)">PINGCHENG WANG · 2026.06</div>
          <div class="t-meta" style="color:rgba(255,255,255,.6)">KYUSHU UNIVERSITY</div>
        </div>
      </div>
    </div>
</section>

<section class="slide" data-chapter="1" data-chapter-title="研究背景与目的" data-short-title="现实困境" data-layout="S22" data-animate="image-hero">
  <div class="canvas-card" style="padding:0;display:flex;flex-direction:column;overflow:hidden">
    <div data-anim="img" style="position:relative;flex:0 0 58%;overflow:hidden;background:var(--grey-1)">
      <img src="images/01-field-observation.jpg" data-image-slot="s22-hero-21x9" alt="福冈市植物园温室实地环境" loading="eager" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 42%">
      <div class="chrome-min" style="position:absolute;top:0;left:0;right:0;color:rgba(255,255,255,.9);padding:5.6vh 5vw 0">
        <div class="l">CONTEXT & PROBLEM STATEMENT</div><div class="r">02 / 12</div>
      </div>
      <div data-anim="title-block" style="position:absolute;left:5vw;top:11vh;background:var(--paper);padding:3vh 3vw;max-width:42vw">
        <div style="display:flex;align-items:center;gap:1vw;margin-bottom:1.6vh;color:var(--accent)"><i data-lucide="leaf" style="width:28px;height:28px;stroke-width:1.5"></i><i data-lucide="eye" style="width:28px;height:28px;stroke-width:1.5"></i></div>
        <div style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(4.8vw,8.2vh);line-height:1;letter-spacing:-.03em;color:var(--text-primary)">高设置、低阅读：<br/>非正式学习的现实困境</div>
      </div>
    </div>
    <div data-anim="kpi" class="image-hero-body">
      <div style="max-width:48ch;font-family:var(--sans),var(--sans-zh);font-size:max(18px,1.25vw);line-height:1.55;font-weight:400;color:var(--text-primary)">
        作为温室环境中的非正式学习界面，解说标识往往面临“高设置、低阅读”的困境与“低信息记忆”的双重失败。这一困境背后潜藏着两大结构性原因：缺乏基于证据的设计原则，以及缺乏客观的诊断评估工具。
      </div>
      <div class="image-hero-stats" style="gap:3vw">
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">SITE</div><div style="font-family:var(--sans);font-weight:200;font-size:min(4vw,7vh);line-height:.95;letter-spacing:-.035em">福冈市植物园</div><p class="body-sm" style="margin-top:auto">温室区非正式学习环境</p></div>
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">ISSUE 1</div><div style="font-family:var(--sans);font-weight:200;font-size:min(3vw,5vh);line-height:.98;letter-spacing:-.03em">缺乏设计原则</div><p class="body-sm" style="margin-top:auto">导致解说标识在认知上难以被访问</p></div>
        <div style="display:flex;flex-direction:column;gap:.6vh"><div style="height:1px;background:var(--ink)"></div><div class="t-meta">ISSUE 2</div><div style="font-family:var(--sans);font-weight:200;font-size:min(3vw,5vh);line-height:.95;letter-spacing:-.035em">缺乏诊断工具</div><p class="body-sm" style="margin-top:auto">无法客观确定设计干预是否有效</p></div>
      </div>
    </div>
  </div>
</section>

<section class="slide" data-chapter="1" data-chapter-title="研究背景与目的" data-short-title="研究目的" data-layout="S16" data-animate="field-notes">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">OBJECTIVES</div><div class="r">03 / 12</div></div>
    <div style="display:flex;flex-direction:column;gap:1.2vh">
      <h2 class="h-xl-zh" style="font-size:min(4.8vw,8.5vh)">研究目的与核心目标</h2>
    </div>
    <div style="display:flex;flex-direction:column;gap:2vh;margin-top:3vh;flex:1">
      <div class="lead" style="max-width:60ch;color:var(--text-primary);line-height:1.6">本研究旨在通过提出共创导向的设计原则，并开发开源、低成本的非接触式眼动追踪诊断工具，直接弥补当前非正式学习标识设计中的理论与技术双重空白。以此为基础，量化设计原则对标识完读率的实际提升效果。</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:2vw;margin-top:2vh">
        <article class="card-fill" style="padding:2.4vh 2vw;display:flex;flex-direction:column;gap:1.4vh">
          <div style="display:flex;align-items:center;gap:.8vw;color:var(--accent)"><i data-lucide="pen-tool" style="width:24px;height:24px;stroke-width:1.7"></i><div class="t-meta">GOAL 1</div></div>
          <h3 class="t-h-prod">提出共创设计原则</h3>
          <p class="t-body-sm">从自上而下的专家主导转向自下而上的共创设计，提炼能够有效降低认知负荷并吸引注意力的循证设计原则。</p>
        </article>
        <article class="card-fill" style="padding:2.4vh 2vw;display:flex;flex-direction:column;gap:1.4vh">
          <div style="display:flex;align-items:center;gap:.8vw;color:var(--accent)"><i data-lucide="eye" style="width:24px;height:24px;stroke-width:1.7"></i><div class="t-meta">GOAL 2</div></div>
          <h3 class="t-h-prod">开发诊断与评估工具</h3>
          <p class="t-body-sm">开发无需昂贵专用硬件、适用于自然实地场景的低成本眼动追踪系统，以定量分析标识阅读过程中的视觉分配。</p>
        </article>
      </div>
    </div>
  </div>
</section>

<!-- Chapter 2: 研究策略与整体设计 -->
<section class="slide" data-chapter="2" data-chapter-title="研究策略与整体设计" data-short-title="整体设计" data-layout="S05" data-animate="sub-stack">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">RESEARCH STRATEGY AND OVERALL DESIGN</div><div class="r">04 / 12</div></div>
    <div style="display:grid;grid-template-columns:4fr 8fr;gap:4vw;flex:1;min-height:0">
      <div style="display:flex;flex-direction:column;gap:2vh">
        <h2 class="h-xl-zh" style="font-size:min(4.8vw,8.5vh)">基于证据的自下而上范式</h2>
        <p class="t-body">以福冈市植物园温室为研究现场，确立了自下而上的研究范式：发现问题 → 提炼原则 → 定量诊断 → 实验验证。</p>
        <p class="t-body">将“共创设计（Co-creation Design）”作为核心策略：所有的设计干预均源自记录的游客痛点，而非专家的自上而下假设。从而确保每一个设计决策都锚定真实的观众需求。</p>
      </div>
      <div class="stack-row" style="margin-top:0">
        <article class="stack-block b-grey"><div class="layer-nb">PHASE 1&2</div><i data-lucide="search"></i><h3 class="layer-ttl">问题发现</h3><p class="layer-desc">文献综合与共创工作坊调查真实受众痛点。</p></article>
        <article class="stack-block b-accent"><div class="layer-nb">PHASE 3</div><i data-lucide="pen-tool"></i><h3 class="layer-ttl">原则提炼</h3><p class="layer-desc">衍生 A/R/S 设计原则，并执行现存标识基线审查。</p></article>
        <article class="stack-block b-ink"><div class="layer-nb">PHASE 4</div><i data-lucide="crosshair"></i><h3 class="layer-ttl">实验验证</h3><p class="layer-desc">使用自研工具实施 A/B 眼动实验，进行定量诊断。</p></article>
      </div>
    </div>
  </div>
</section>

<!-- Chapter 3: 研究方法 -->
<section class="slide" data-chapter="3" data-chapter-title="研究方法" data-short-title="文献调查与痛点共创" data-layout="S16" data-animate="field-notes">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">METHODOLOGY · PHASE 1 & 2</div><div class="r">05 / 12</div></div>
    <div style="display:grid;grid-template-columns:5fr 7fr;gap:3vw;flex:1;min-height:0">
      <div style="display:flex;flex-direction:column;gap:1.2vh;min-height:0">
        <div class="t-meta">PHASE 2 现场：Global Goals Jam 九州 2025</div>
        <div class="frame-img fit-cover swiss-lined" style="flex:1;min-height:0">
          <img src="images/05-prototype-sketch.jpg" alt="GGJ 九州工作坊现场记录">
        </div>
      </div>
      <div style="display:flex;flex-direction:column;gap:2vh">
        <h2 class="h-xl-zh" style="font-size:min(4.4vw,7.8vh)">阶段 1 & 2：文献调查与痛点共创</h2>
        <div style="display:flex;flex-direction:column;gap:1.6vh">
          <article class="card-fill" style="padding:2vh 1.6vw;border-left:3px solid var(--grey-3)">
            <h3 class="t-h-prod">Phase 1: 文献综合 (Literature Review)</h3>
            <p class="t-body-sm" style="margin-top:1vh">综合了 Tilden (1957) 解说理论、Ham (2016) EROT 模型与 Serrell (2015) 的标签设计框架，界定了注意分配与认知负荷的经典理论边界。</p>
          </article>
          <article class="card-fill" style="padding:2vh 1.6vw;border-left:3px solid var(--accent)">
            <h3 class="t-h-prod">Phase 2: 共创工作坊与问卷 (Co-creation)</h3>
            <p class="t-body-sm" style="margin-top:1vh">在 Global Goals Jam Kyushu 2025 中，引导市民、设计师与植物园员工进行参与式设计。通过半结构化实地访谈收集受众反馈，进行主题编码，梳理出 <strong>5 大痛点分类</strong>。从实证角度确认了非正式学习场景下的体验障碍。</p>
          </article>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="slide" data-chapter="3" data-chapter-title="研究方法" data-short-title="原则提炼与基线审查" data-layout="S16" data-animate="field-notes">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">METHODOLOGY · PHASE 3</div><div class="r">06 / 12</div></div>
    <div style="display:flex;flex-direction:column;gap:1.4vh">
      <h2 class="h-xl-zh" style="font-size:min(4.8vw,8.5vh)">阶段 3：原则提炼与基线审查</h2>
      <p class="t-body" style="max-width:70ch">基于前期调研，提炼出致力于降低认知负荷的 <strong>A/R/S 标识设计原则</strong>。随后，开发 Signage Annotator 对温室现存 70 块标识进行基线审查，证实了 A/R 原则在现有标识中的结构性缺位。</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:2vw;margin-top:3vh;flex:1">
      <article class="card-fill" style="padding:3vh 2vw;display:flex;flex-direction:column;gap:1.5vh;border-top:2px solid var(--grey-3)">
        <div class="t-meta" style="color:var(--grey-4)">A / ATMOSPHERE</div>
        <h3 class="t-h-prod">启发性氛围</h3>
        <p class="t-body-sm">通过提问或叙事性语言作为信息入口，激发参与者初始的阅读意愿。</p>
      </article>
      <article class="card-fill" style="padding:3vh 2vw;display:flex;flex-direction:column;gap:1.5vh;border-top:2px solid var(--accent)">
        <div class="t-meta" style="color:var(--accent)">R / RELEVANCE</div>
        <h3 class="t-h-prod">观众关联性</h3>
        <p class="t-body-sm">将植物的抽象特征与受众的日常感官经验（触摸、用途、气味）建立强制联结。</p>
      </article>
      <article class="card-fill" style="padding:3vh 2vw;display:flex;flex-direction:column;gap:1.5vh;border-top:2px solid var(--ink)">
        <div class="t-meta" style="color:var(--ink)">S / STRUCTURE</div>
        <h3 class="t-h-prod">结构清晰性</h3>
        <p class="t-body-sm">建立明确的信息层级与视觉排版分区，降低长文本带来的信息过载。</p>
      </article>
    </div>
  </div>
</section>

<section class="slide" data-chapter="3" data-chapter-title="研究方法" data-short-title="眼动实验与数据工具" data-layout="S16" data-animate="field-notes">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">METHODOLOGY · PHASE 4</div><div class="r">07 / 12</div></div>
    <div style="display:grid;grid-template-columns:5fr 7fr;gap:3vw;flex:1;min-height:0">
      <div style="display:flex;flex-direction:column;gap:1.2vh;min-height:0">
        <div class="t-meta">对照组 (单文本) VS 实验组 (A/R/S)</div>
        <div style="display:flex;gap:1vw;flex:1;min-height:0">
          <img src="images/06-control-sign.jpg" alt="对照组" style="width:48%;object-fit:contain;background:#fff;padding:1vh">
          <img src="images/07-intervention-sign.jpg" alt="实验组" style="width:48%;object-fit:contain;background:#fff;border:2px solid var(--accent);padding:1vh">
        </div>
      </div>
      <div style="display:flex;flex-direction:column;gap:2vh">
        <h2 class="h-xl-zh" style="font-size:min(4.2vw,7.5vh)">阶段 4：A/B 眼动实验与数据工具</h2>
        <p class="t-body-sm" style="line-height:1.6">在自然实地环境中招募 15 名真实游客（20-80岁）。实验采用被试内设计，改良组作为唯一操作变量。开发了开源视觉追踪系统，不干扰游客的自然行走路径。</p>
        <div style="display:flex;flex-direction:column;gap:1.4vh">
          <article class="card-fill" style="padding:1.6vh 1.6vw;border-left:3px solid var(--accent)">
            <h3 class="t-h-prod">SIGN Visual Attention 工具</h3>
            <p class="t-body-sm" style="margin-top:1vh">基于 WebGazer 研发的非接触式眼动分析系统，利用普通网络摄像头采集面部数据，实时生成视线轨迹热力图，极大地降低了实地调研的硬件门槛。</p>
          </article>
          <article class="card-fill" style="padding:1.6vh 1.6vw;border-left:3px solid var(--accent)">
            <h3 class="t-h-prod">AOI 语义关注区分析</h3>
            <p class="t-body-sm" style="margin-top:1vh">将热力图坐标映射回纸面标识上，并对 A区、R区划定明确的边界。通过计算落入 AOI 区域的注视点比例，量化评估文字阅读的完读率。</p>
          </article>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Chapter 4: 结果与讨论 -->
<section class="slide" data-chapter="4" data-chapter-title="结果与讨论" data-short-title="初期阅读率提升" data-layout="S06" data-animate="tower-grow">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">RESULTS & DISCUSSION · OVERALL READ-THROUGH</div><div class="r">08 / 12</div></div>
    <div style="display:flex;flex-direction:column;gap:1.4vh">
      <h2 class="h-xl-zh" style="font-size:min(4.4vw,7.8vh)">结果 (1)：初期文字区域完读率提升</h2>
    </div>
    <div class="chart-box" style="flex:1;display:flex;flex-direction:column;align-items:center;margin-top:4vh">
      <p class="t-body-sm" style="margin-bottom:4vh;max-width:60ch;text-align:center">A/B 实验在 15 名有效参与者中产生了稳定且一致的积极效应。改良版在最早期的阅读窗口内（前10秒），有效提升了整体文字区域的阅读覆盖率。</p>
      <div class="bar-chart vert" style="height:35vh;display:flex;align-items:flex-end;gap:4vw;justify-content:center">
        <div class="bar-col" style="height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:1.5vh">
          <div class="bar-val" style="font-family:var(--mono);font-size:2.4vw">38.6%</div>
          <div class="bar-fill" style="width:6vw;height:38.6%;background:var(--grey-3)"></div>
          <div class="t-meta">对照组 (前10秒完读率)</div>
        </div>
        <div class="bar-col" style="height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:1.5vh">
          <div class="bar-val" style="font-family:var(--mono);font-size:2.4vw;color:var(--accent)">45.3%</div>
          <div class="bar-fill" style="width:6vw;height:45.3%;background:var(--accent)"></div>
          <div class="t-meta">实验组 (前10秒完读率)</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="slide" data-chapter="4" data-chapter-title="结果与讨论" data-short-title="R 原则的决定性效应" data-layout="S20" data-animate="stacked-ledger">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">RESULTS & DISCUSSION · R-PRINCIPLE EFFICACY</div><div class="r">09 / 12</div></div>
    <div style="display:flex;flex-direction:column;gap:1.4vh">
      <h2 class="h-xl-zh" style="font-size:min(4.8vw,8.5vh)">结果 (2)：R 原则发挥核心决定性效应</h2>
    </div>
    <div style="display:grid;grid-template-columns:5fr 7fr;gap:4vw;margin-top:3vh;flex:1">
      <div style="display:flex;flex-direction:column;gap:1.4vh">
        <p class="t-body">通过将效应分解，我们发现 R 原则（将植物知识与感官体验经验相连接）是捕获并维持视线的最关键变量。</p>
        <div style="background:var(--grey-1);padding:2vh 1.4vw;margin-top:1vh">
          <div class="t-meta" style="color:var(--accent)">FINDING</div>
          <p class="t-body-sm" style="margin-top:1vh">R 区域的前 10 秒占比从 5.0% 激增至 21.4%。全程驻留时间更是发生了质的跃升（四倍增长），且这种上升趋势出现在所有 15 名测试者中。这证实了共创干预应当优先考虑观众的经验锚点，而非单纯的修辞包装。</p>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;gap:2vh;justify-content:center">
        <div class="ledger-row" style="display:grid;grid-template-columns:3fr 1fr 1fr;gap:2vw;border-bottom:1px solid var(--border-subtle);padding-bottom:1vh">
          <div class="t-meta">R 区域关注占比</div>
          <div class="t-meta" style="text-align:right">对照组</div>
          <div class="t-meta" style="text-align:right;color:var(--accent)">实验组</div>
        </div>
        <div class="ledger-row" style="display:grid;grid-template-columns:3fr 1fr 1fr;gap:2vw;padding:1.5vh 0;border-bottom:1px dashed var(--border-subtle)">
          <div class="t-body-sm" style="font-weight:600">前 10 秒初期占比</div>
          <div class="t-body-sm" style="text-align:right;font-family:var(--mono)">5.0%</div>
          <div class="t-body-sm" style="text-align:right;font-family:var(--mono);color:var(--accent);font-weight:600">21.4%</div>
        </div>
        <div class="ledger-row" style="display:grid;grid-template-columns:3fr 1fr 1fr;gap:2vw;padding:1.5vh 0">
          <div class="t-body-sm" style="font-weight:600">全程驻留时间 (Dwell Time)</div>
          <div class="t-body-sm" style="text-align:right;font-family:var(--mono)">8.5%</div>
          <div class="t-body-sm" style="text-align:right;font-family:var(--mono);color:var(--accent);font-weight:600">35.1% (4X)</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Chapter 5: 结论与未来展望 -->
<section class="slide split" data-chapter="5" data-chapter-title="结论与未来展望" data-short-title="研究结论" data-layout="SWISS-CLOSING-ASCII" data-animate="split-statement">
  <div class="canvas-card">
    <div class="split-half">
      <div class="half b-accent" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between;position:relative;overflow:hidden">
        <canvas class="ascii-bg" aria-hidden="true"></canvas>
        <div class="chrome-min" style="margin-bottom:0;position:relative;z-index:1"><div class="l">10 / 12</div><div class="r">CONCLUSIONS</div></div>
        <div data-anim="manifesto" style="display:flex;flex-direction:column;gap:2vh;position:relative;z-index:1">
          <h2 class="slide16-title" style="font-family:var(--sans),var(--sans-zh);font-size:min(7.4vw,13vh);line-height:.96;letter-spacing:-.025em;font-weight:200;color:#fff">结论：解决非正式<br/><span style="font-style:italic;font-weight:300">学习中的结构性失败</span></h2>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(16px,1vw);line-height:1.6;color:rgba(255,255,255,.82);font-weight:400;max-width:38ch;margin-top:1.4vh">本研究不仅验证了经验锚点对吸引视觉注意的决定性作用，更构建了连接设计干预与客观数据验证的循环框架。</div>
        </div>
        <div data-anim="signature" style="display:flex;justify-content:space-between;align-items:end;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh;position:relative;z-index:1"><div class="t-meta" style="color:rgba(255,255,255,.62)">MASTER'S REPORT</div><div class="t-meta" style="color:rgba(255,255,255,.62)">KYUSHU UNIVERSITY</div></div>
      </div>
      <div class="half" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between">
        <div class="chrome-min"><div class="l">CONTRIBUTIONS</div><div class="r">THREE PILLARS</div></div>
        <div data-anim="rules" style="display:flex;flex-direction:column;gap:2.2vh">
          <div style="display:grid;grid-template-columns:4em 1fr;gap:1.4vw;border-top:1px solid var(--border-subtle);padding-top:2vh"><div class="t-meta">1</div><div><h3 class="t-h-prod">方法论贡献 (Methodological)</h3><p class="t-body-sm">提供了一个标准框架，将零散的用户痛点有效地组织、过滤，并转化为可执行的解说标识设计规范。</p></div></div>
          <div style="display:grid;grid-template-columns:4em 1fr;gap:1.4vw;border-top:1px solid var(--border-subtle);padding-top:2vh"><div class="t-meta">2</div><div><h3 class="t-h-prod">应用贡献 (Applied)</h3><p class="t-body-sm">A/R/S 原则可直接作为植物园、科学博物馆等非正式学习环境的通用指导方针。</p></div></div>
          <div style="display:grid;grid-template-columns:4em 1fr;gap:1.4vw;border-top:1px solid var(--accent);padding-top:2vh"><div class="t-meta" style="color:var(--accent)">3</div><div><h3 class="t-h-prod" style="color:var(--accent)">工具贡献 (Instrumental)</h3><p class="t-body-sm">开源系统 SIGN Visual Attention 证明了在无需专用仪器和专家的前提下，于自然实地开展眼动评估的可行性与低成本优势。</p></div></div>
        </div>
        <div data-anim="foot" class="t-meta" style="color:var(--text-helper);text-align:right">RESEARCH CONCLUSIONS</div>
      </div>
    </div>
  </div>
</section>

<section class="slide split" data-chapter="5" data-chapter-title="结论与未来展望" data-short-title="博士阶段展望" data-layout="SWISS-CLOSING-ASCII" data-animate="split-statement">
  <div class="canvas-card">
    <div class="split-half">
      <div class="half b-accent" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between;position:relative;overflow:hidden;background-color:var(--ink)">
        <canvas class="ascii-bg" aria-hidden="true"></canvas>
        <div class="chrome-min" style="margin-bottom:0;position:relative;z-index:1;color:#fff"><div class="l">11 / 12</div><div class="r">FUTURE AGENDA</div></div>
        <div data-anim="manifesto" style="display:flex;flex-direction:column;gap:2vh;position:relative;z-index:1">
          <h2 class="slide16-title" style="font-family:var(--sans),var(--sans-zh);font-size:min(6.5vw,11.5vh);line-height:.96;letter-spacing:-.025em;font-weight:200;color:#fff">博士阶段展望：<br/>从<span style="font-style:italic;font-weight:300">视觉捕获</span>到信息提取</h2>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(16px,1vw);line-height:1.6;color:rgba(255,255,255,.82);font-weight:400;max-width:38ch;margin-top:1.4vh">在解决了“视觉完读率”的基础障碍之后，下一步研究将深入人类学习的第二个维度：信息的长效记忆与学习路径的构建。</div>
        </div>
        <div data-anim="signature" style="display:flex;justify-content:space-between;align-items:end;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh;position:relative;z-index:1;color:#fff"><div class="t-meta" style="color:rgba(255,255,255,.62)">DOCTORAL RESEARCH AGENDA</div></div>
      </div>
      <div class="half" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between">
        <div class="chrome-min"><div class="l">NEXT STEPS</div><div class="r">TARGETING PROBLEM 2</div></div>
        <div data-anim="rules" style="display:flex;flex-direction:column;gap:2.2vh">
          <div style="display:grid;grid-template-columns:4em 1fr;gap:1.4vw;border-top:1px solid var(--border-subtle);padding-top:2vh"><div class="t-meta">STEP 1</div><div><h3 class="t-h-prod">解决信息记忆衰退</h3><p class="t-body-sm">以认知负荷理论 (Sweller, 1988) 与双重编码理论为基础，解决植物园长动线环境中的严重空间不连续性导致的信息遗忘问题。</p></div></div>
          <div style="display:grid;grid-template-columns:4em 1fr;gap:1.4vw;border-top:1px solid var(--border-subtle);padding-top:2vh"><div class="t-meta">STEP 2</div><div><h3 class="t-h-prod">全过程眼动与延迟记忆测试</h3><p class="t-body-sm">结合全程眼动仪与延迟记忆提取测试，探索标识系统的空间布局、主题连贯性如何调节记忆编码的质量。</p></div></div>
          <div style="display:grid;grid-template-columns:4em 1fr;gap:1.4vw;border-top:1px solid var(--ink);padding-top:2vh"><div class="t-meta" style="color:var(--ink)">STEP 3</div><div><h3 class="t-h-prod" style="color:var(--ink)">构建连续学习路径</h3><p class="t-body-sm">旨在消除非正式学习场景中的结构性障碍，在温室中串联起稳定、具连贯意义的学习叙事空间。</p></div></div>
        </div>
        <div data-anim="foot" class="t-meta" style="color:var(--text-helper);text-align:right">DOCTORAL AGENDA</div>
      </div>
    </div>
  </div>
</section>

<!-- Chapter 6: 参考文献 -->
<section class="slide" data-chapter="6" data-chapter-title="参考文献" data-short-title="References" data-layout="S16" data-animate="field-notes">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">REFERENCES</div><div class="r">12 / 12</div></div>
    <div style="display:flex;flex-direction:column;gap:1.4vh">
      <h2 class="h-xl-zh" style="font-size:min(4.8vw,8.5vh)">参考文献 (References)</h2>
    </div>
    <div style="display:flex;flex-direction:column;gap:1.6vh;margin-top:3vh;flex:1">
      <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:1.5vh">
        <li style="padding-bottom:1.5vh;border-bottom:1px solid var(--border-subtle)">
          <p class="t-body-sm" style="line-height:1.6"><strong>Bitgood, S. (2013).</strong> Attention and value: Keys to understanding museum visitors. <i>Left Coast Press</i>.</p>
        </li>
        <li style="padding-bottom:1.5vh;border-bottom:1px solid var(--border-subtle)">
          <p class="t-body-sm" style="line-height:1.6"><strong>Ham, S. (2016).</strong> Interpretation: Making a difference on purpose. <i>Fulcrum Publishing</i>.</p>
        </li>
        <li style="padding-bottom:1.5vh;border-bottom:1px solid var(--border-subtle)">
          <p class="t-body-sm" style="line-height:1.6"><strong>Paivio, A. (1971).</strong> Imagery and verbal processes. <i>Holt, Rinehart, and Winston</i>.</p>
        </li>
        <li style="padding-bottom:1.5vh;border-bottom:1px solid var(--border-subtle)">
          <p class="t-body-sm" style="line-height:1.6"><strong>Serrell, B. (2015).</strong> Exhibit labels: An interpretive approach. <i>Bloomsbury Publishing</i>.</p>
        </li>
        <li style="padding-bottom:1.5vh;border-bottom:1px solid var(--border-subtle)">
          <p class="t-body-sm" style="line-height:1.6"><strong>Spooner, S. L., et al. (2024).</strong> Using eye-tracking to create impactful interpretation signage for botanic gardens. <i>Journal of Zoological and Botanical Gardens, 5(3)</i>, 434-454.</p>
        </li>
        <li style="padding-bottom:1.5vh;border-bottom:1px solid var(--border-subtle)">
          <p class="t-body-sm" style="line-height:1.6"><strong>Sweller, J. (1988).</strong> Cognitive load during problem solving: Effects on learning. <i>Cognitive Science, 12(2)</i>, 257-285.</p>
        </li>
        <li style="padding-bottom:1.5vh;border-bottom:1px solid var(--border-subtle)">
          <p class="t-body-sm" style="line-height:1.6"><strong>Tilden, F. (1957).</strong> Interpreting our heritage. <i>University of North Carolina Press</i>.</p>
        </li>
      </ul>
    </div>
  </div>
</section>
\n`;

const newContent = content.substring(0, startIndex) + newSlides + content.substring(endIndex);
fs.writeFileSync(indexHtmlPath, newContent, 'utf8');
console.log('Master Slides successfully updated!');
