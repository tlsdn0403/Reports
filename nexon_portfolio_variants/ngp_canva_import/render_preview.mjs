import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "file:///C:/Users/tlsdn/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs";

const root = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch({
  executablePath: "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  headless: true,
});
const page = await browser.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(path.join(root, "ngp_portfolio_inline.html")).href, { waitUntil: "load" });
const slides = page.locator('[data-document-role="page"]');
for (let index = 0; index < await slides.count(); index += 1) {
  await slides.nth(index).screenshot({ path: path.join(root, `preview-${index + 1}.png`) });
}
await browser.close();
