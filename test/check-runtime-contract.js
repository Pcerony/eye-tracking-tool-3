const assert = require('assert');
const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(
  path.join(__dirname, '..', 'ppt', 'index.html'),
  'utf8'
);

const scripts = [...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)]
  .filter(match => !/\btype=["']module["']/i.test(match[0]))
  .map(match => ({
    source: match[1],
    startLine: html.slice(0, match.index).split('\n').length
  }));

assert.ok(scripts.length > 0, 'deck should contain inline runtime scripts');

scripts.forEach(({ source, startLine }, index) => {
  assert.doesNotThrow(
    () => new Function(source),
    `inline runtime script ${index + 1} (starts at HTML line ${startLine}) should parse without syntax errors`
  );
});

console.log(`PASS ${scripts.length} inline runtime scripts parse`);
