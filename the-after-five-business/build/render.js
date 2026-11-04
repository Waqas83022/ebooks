// Renders figures, the cover and the proof PDF with Playwright.
// Usage: node build/render.js figures <figures.html> <outdir>
//        node build/render.js cover   <cover.html>   <out.png>
//        node build/render.js pdf     <book.html>    <out.pdf>
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [mode, input, output] = process.argv.slice(2);
  const browser = await chromium.launch();
  const url = 'file://' + path.resolve(input);
  if (mode === 'figures') {
    const page = await browser.newPage({ viewport: { width: 860, height: 1200 }, deviceScaleFactor: 2 });
    await page.goto(url, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const ids = await page.$$eval('.fig', els => els.map(e => e.id));
    for (const id of ids) {
      await page.locator('#' + id).screenshot({ path: path.join(output, id + '.png') });
    }
    console.log('rendered', ids.length, 'figures');
  } else if (mode === 'cover') {
    const page = await browser.newPage({ viewport: { width: 1600, height: 2560 }, deviceScaleFactor: 1 });
    await page.goto(url, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: output, clip: { x: 0, y: 0, width: 1600, height: 2560 } });
  } else if (mode === 'pdf') {
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({
      path: output, width: '6in', height: '9in',
      margin: { top: '0.75in', bottom: '0.8in', left: '0.75in', right: '0.75in' },
      displayHeaderFooter: true, headerTemplate: '<div></div>',
      footerTemplate: '<div style="width:100%;text-align:center;font-family:Georgia,serif;font-size:9px;color:#555;"><span class="pageNumber"></span></div>',
      printBackground: true,
    });
  } else { throw new Error('unknown mode'); }
  await browser.close();
})();
