import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import { chromium } from 'playwright';

const url = process.env.DECK_URL || 'http://127.0.0.1:4174';

const translations = [
  {
    button: 'ZH',
    lang: 'zh',
    title: '关于用于设计解说标识的共创工具的研究',
    subtitle: '以福冈市植物园温室区域为例',
    lead: '植物解说标识的 A/R/S 设计改良与眼动评估实验分析'
  },
  {
    button: 'EN',
    lang: 'en',
    title: 'A Study on Co-creation Tools for Designing Interpretive Signage',
    subtitle: 'Case Study of Fukuoka City Botanical Garden Greenhouse',
    lead: 'Eye-tracking evaluation of A/R/S design improvements for interpretive plant signage'
  },
  {
    button: 'JA',
    lang: 'ja',
    title: '解説サインのための共創ツールに関する研究',
    subtitle: '福岡市植物園温室エリアを事例として',
    lead: '植物解説サインの A/R/S デザイン改良と視線計測評価実験分析'
  },
  {
    button: 'ES',
    lang: 'es-MX',
    title: 'Un estudio sobre herramientas de co-creación para el diseño de señalización interpretativa',
    subtitle: 'Caso de estudio del invernadero del Jardín Botánico de la Ciudad de Fukuoka',
    lead: 'Análisis experimental del diseño mejorado A/R/S de señalización interpretativa de plantas y evaluación ocular'
  }
];

const viewports = [
  { width: 1440, height: 1000 },
  { width: 390, height: 844 }
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: viewports[0] });
  const consoleIssues = [];

  page.on('console', message => {
    if (message.type() === 'error') consoleIssues.push(message.text());
  });
  page.on('pageerror', error => consoleIssues.push(error.message));

  try {
    await page.goto(url, { waitUntil: 'domcontentloaded' });
    await mkdir('output/qa', { recursive: true });

    const cover = page.locator('.slide.is-current[data-slide-id="s01-cover"]');
    await cover.waitFor({ state: 'visible' });

    const languages = await cover.locator('button.lang-top-btn').evaluateAll(buttons =>
      buttons.map(button => button.dataset.language)
    );

    assert.deepStrictEqual(
      languages,
      ['zh', 'en', 'ja', 'es-MX'],
      's01-cover should expose one complete language-button set'
    );

    const qr = cover.locator('img[alt="QR Code"]');
    await qr.waitFor({ state: 'visible' });
    assert.strictEqual(
      await qr.getAttribute('loading'),
      'eager',
      's01-cover should eagerly load its visible QR code'
    );
    assert.ok(
      await qr.evaluate(image => image.complete && image.naturalWidth > 0),
      's01-cover QR code should load successfully'
    );

    for (const viewport of viewports) {
      await page.setViewportSize(viewport);

      for (const translation of translations) {
        await page.getByRole('button', { name: translation.button }).click();
        await page.locator(`html[lang="${translation.lang}"]`).waitFor({ state: 'attached' });
        await page.waitForFunction(() => {
          const slide = document.querySelector('.slide.is-current[data-slide-id="s01-cover"]');
          const title = slide?.querySelector('h1');
          const lead = slide?.querySelector('.lead');
          const switcher = slide?.querySelector('.cover-lang-switch');
          const image = slide?.querySelector('img[alt="QR Code"]');
          return [slide, title, lead, switcher, image].every(node => node?.getBoundingClientRect().width > 0);
        });

        const heading = (await cover.locator('h1').textContent()).trim();
        assert.ok(heading.startsWith(translation.title), `${translation.lang} title should match`);
        assert.strictEqual(
          (await cover.locator('h1 span').textContent()).trim(),
          translation.subtitle,
          `${translation.lang} subtitle should match`
        );
        assert.strictEqual(
          (await cover.locator('.lead').textContent()).trim(),
          translation.lead,
          `${translation.lang} lead should match`
        );

        if (translation.lang === 'en' || translation.lang === 'es-MX') {
          assert.ok(
            !/[\u3400-\u9fff]/.test(await cover.innerText()),
            `${translation.lang} cover should not leak Chinese text`
          );
        }

        const layout = await cover.evaluate(slide => {
          const rect = slide.getBoundingClientRect();
          const positions = Object.fromEntries(
            ['h1', '.lead', '.cover-lang-switch', 'img[alt="QR Code"]'].map(selector => {
              const node = slide.querySelector(selector);
              const box = node.getBoundingClientRect();
              return [selector, { left: box.left, right: box.right, top: box.top, bottom: box.bottom }];
            })
          );
          return {
            rect: { left: rect.left, right: rect.right, top: rect.top, bottom: rect.bottom },
            positions,
            noHorizontalOverflow: slide.scrollWidth <= slide.clientWidth + 1
          };
        });

        assert.ok(layout.noHorizontalOverflow, `${translation.lang} cover should not overflow horizontally`);
        for (const [selector, box] of Object.entries(layout.positions)) {
          assert.ok(box.left >= layout.rect.left - 1, `${selector} should stay within the cover`);
          assert.ok(box.right <= layout.rect.right + 1, `${selector} should stay within the cover`);
          assert.ok(box.top >= layout.rect.top - 1, `${selector} should stay within the cover`);
          assert.ok(box.bottom <= layout.rect.bottom + 1, `${selector} should stay within the cover`);
        }
        const title = layout.positions.h1;
        const qrBox = layout.positions['img[alt="QR Code"]'];
        const titleOverlapsQr = !(
          title.right <= qrBox.left ||
          qrBox.right <= title.left ||
          title.bottom <= qrBox.top ||
          qrBox.bottom <= title.top
        );
        assert.ok(!titleOverlapsQr, `${translation.lang} title should not overlap the QR code`);

        await page.screenshot({
          path: `output/qa/s01-cover-${translation.lang}-${viewport.width}x${viewport.height}.png`
        });
      }
    }

    assert.deepStrictEqual(consoleIssues, [], 's01-cover should not emit browser errors');

  } finally {
    await browser.close();
  }

  console.log('PASS s01-cover exposes one complete language-button set');
})().catch(error => {
  console.error(`FAIL s01-cover browser contract: ${error.message}`);
  process.exitCode = 1;
});
