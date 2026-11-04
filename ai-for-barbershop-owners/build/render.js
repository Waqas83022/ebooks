// Renders the cover, the book figures and the 6x9 proof PDF with Playwright.
// Usage: node build/render.js cover   <cover.html> <out.png>
//        node build/render.js figures <html dir>   <out dir>
//        node build/render.js pdf     <book.html>  <out.pdf>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const [mode, input, output] = process.argv.slice(2);
  const browser = await chromium.launch();
  if (mode === 'cover') {
    const page = await browser.newPage({ viewport: { width: 1600, height: 2560 }, deviceScaleFactor: 1 });
    await page.goto('file://' + path.resolve(input), { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: output, clip: { x: 0, y: 0, width: 1600, height: 2560 } });
  } else if (mode === 'figures') {
    fs.mkdirSync(output, { recursive: true });
    const page = await browser.newPage({ viewport: { width: 1000, height: 800 }, deviceScaleFactor: 1.5 });
    for (const f of fs.readdirSync(input).filter((x) => x.endsWith('.html')).sort()) {
      await page.goto('file://' + path.resolve(input, f), { waitUntil: 'load' });
      await page.evaluate(() => document.fonts.ready);
      const el = await page.$('#fig');
      await el.screenshot({ path: path.join(output, f.replace(/\.html$/, '.png')) });
      console.log('rendered', f);
    }
  } else if (mode === 'pdf') {
    const page = await browser.newPage();
    await page.goto('file://' + path.resolve(input), { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({
      path: output,
      width: '6in',
      height: '9in',
      margin: { top: '0.8in', bottom: '0.85in', left: '0.75in', right: '0.75in' },
      displayHeaderFooter: true,
      headerTemplate: '<div></div>',
      footerTemplate:
        '<div style="width:100%;text-align:center;font-family:Georgia,serif;font-size:9px;color:#555;">' +
        '<span class="pageNumber"></span></div>',
      printBackground: true,
    });
  } else {
    throw new Error('mode must be cover, figures or pdf');
  }
  await browser.close();
})();
