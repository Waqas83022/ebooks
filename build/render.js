// Renders the cover (JPEG via PNG) and the 6x9 proof PDF with Playwright.
// Usage: node build/render.js cover <cover.html> <out.png>
//        node build/render.js pdf   <book.html>  <out.pdf>
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [mode, input, output] = process.argv.slice(2);
  const browser = await chromium.launch();
  const url = 'file://' + path.resolve(input);
  if (mode === 'cover') {
    const page = await browser.newPage({ viewport: { width: 1600, height: 2560 }, deviceScaleFactor: 1 });
    await page.goto(url, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: output, clip: { x: 0, y: 0, width: 1600, height: 2560 } });
  } else if (mode === 'pdf') {
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({
      path: output,
      width: '6in',
      height: '9in',
      margin: { top: '0.8in', bottom: '0.85in', left: '0.8in', right: '0.8in' },
      displayHeaderFooter: true,
      headerTemplate: '<div></div>',
      footerTemplate:
        '<div style="width:100%;text-align:center;font-family:Georgia,serif;font-size:9px;color:#555;">' +
        '<span class="pageNumber"></span></div>',
      printBackground: true,
    });
  } else {
    throw new Error('mode must be cover or pdf');
  }
  await browser.close();
})();
