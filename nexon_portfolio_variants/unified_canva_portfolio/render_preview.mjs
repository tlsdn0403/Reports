import path from "node:path";
import { fileURLToPath,pathToFileURL } from "node:url";
import { chromium } from "file:///C:/Users/tlsdn/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs";
const root=path.dirname(fileURLToPath(import.meta.url));
const browser=await chromium.launch({executablePath:"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",headless:true});
const page=await browser.newPage({viewport:{width:1366,height:768},deviceScaleFactor:1});
await page.goto(pathToFileURL(path.join(root,"unified_portfolio_inline.html")).href,{waitUntil:"load"});
const slides=page.locator('[data-document-role="page"]');
for(let i=0;i<await slides.count();i+=1){await slides.nth(i).screenshot({path:path.join(root,`preview-${String(i+1).padStart(2,"0")}.png`)});}
await browser.close();
