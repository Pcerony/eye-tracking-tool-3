const assert = require('assert');
const { chromium } = require('playwright');

const url = process.env.DECK_URL || 'http://127.0.0.1:4174/ppt/index.html';
const viewports = [
  { name: 'wide', width: 2048, height: 1086 },
  { name: 'desktop', width: 1440, height: 1000 },
  { name: 'narrow', width: 900, height: 900 },
  { name: 'mobile', width: 390, height: 844 }
];

function assertVisibleInsideViewport(state, viewport) {
  assert.ok(state.current, `${viewport.name}: runtime should create a current slide`);
  assert.strictEqual(state.currentCount, 1, `${viewport.name}: exactly one current slide is required`);
  assert.strictEqual(state.nextCount, 1, `${viewport.name}: the next slide preview should remain available`);
  assert.ok(Math.abs(state.rect.width / state.rect.height - 4 / 3) < 0.01, `${viewport.name}: current slide should remain 4:3`);

  const epsilon = 1;
  assert.ok(state.rect.left >= -epsilon, `${viewport.name}: current slide should not be clipped on the left`);
  assert.ok(state.rect.top >= -epsilon, `${viewport.name}: current slide should not be clipped on top`);
  assert.ok(state.rect.right <= viewport.width + epsilon, `${viewport.name}: current slide should not be clipped on the right`);
  assert.ok(state.rect.bottom <= viewport.height + epsilon, `${viewport.name}: current slide should not be clipped on bottom`);
  assert.notStrictEqual(state.deckTransform, 'none', `${viewport.name}: carousel positioning should run`);
}

(async () => {
  const browser = await chromium.launch();
  const consoleIssues = [];

  try {
    for (const viewport of viewports) {
      const page = await browser.newPage({ viewport: { width: viewport.width, height: viewport.height } });
      page.on('console', message => {
        if (message.type() === 'error' || message.type() === 'warning') {
          consoleIssues.push(`${viewport.name} console ${message.type()}: ${message.text()}`);
        }
      });
      page.on('pageerror', error => {
        consoleIssues.push(`${viewport.name} pageerror: ${error.message}`);
      });

      await page.goto(url, { waitUntil: 'domcontentloaded' });
      await page.waitForTimeout(1200);

      const state = await page.evaluate(() => {
        const slide = document.querySelector('.slide.is-current');
        const rect = slide?.getBoundingClientRect();
        const deck = document.getElementById('deck');
        return {
          current: Boolean(slide),
          currentCount: document.querySelectorAll('.slide.is-current').length,
          nextCount: document.querySelectorAll('.slide.is-next').length,
          deckTransform: deck ? getComputedStyle(deck).transform : 'missing',
          rect: rect ? {
            left: rect.left,
            top: rect.top,
            right: rect.right,
            bottom: rect.bottom,
            width: rect.width,
            height: rect.height
          } : { left: 0, top: 0, right: 0, bottom: 0, width: 0, height: 0 }
        };
      });

      assertVisibleInsideViewport(state, viewport);
      await page.close();
    }

    assert.deepStrictEqual(consoleIssues, [], `slide display should be free of runtime errors: ${consoleIssues.join('; ')}`);
    console.log('PASS slide display regression contract');
  } finally {
    await browser.close();
  }
})().then(() => process.exit(0)).catch(error => {
  console.error(`FAIL slide display regression contract: ${error.message}`);
  process.exit(1);
});
