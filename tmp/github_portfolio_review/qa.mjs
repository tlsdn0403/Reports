import { chromium } from 'file:///C:/Users/tlsdn/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs';
import {pathToFileURL} from 'node:url';
import fs from 'node:fs/promises';
const root='C:/Users/tlsdn/Desktop/Reports/output/portfolio-prototype';
const shots='C:/Users/tlsdn/Desktop/Reports/tmp/github_portfolio_review';
const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});
const reports=[];
for(const width of [1440,390]){
 const page=await browser.newPage({viewport:{width,height:1000},deviceScaleFactor:1});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(pathToFileURL(root+'/index.html').href);
 await page.evaluate(()=>{for(const i of document.images)i.loading='eager'});
 await page.evaluate(()=>Promise.all([...document.images].map(i=>i.decode().catch(()=>{}))));
 await page.screenshot({path:shots+`/desktop-${width}.png`,fullPage:false});
 for(const id of ['projects','flickdom','about']){
  await page.locator('#'+id).scrollIntoViewIfNeeded();
  await page.locator('#'+id).screenshot({path:shots+`/${id}-${width}.png`});
 }
 const checks=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,brokenImages:[...document.images].filter(x=>!x.complete||x.naturalWidth===0).map(x=>x.alt),missingAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(x=>!document.getElementById(x.getAttribute('href').slice(1))).map(x=>x.href)}));
 await page.locator('summary').first().click();
 checks.detailsOpen=await page.locator('details').first().getAttribute('open')!==null;
 await page.goto(pathToFileURL(root+'/self-introduction.html').href);
 await page.screenshot({path:shots+`/letter-${width}.png`,fullPage:true});
 checks.letterOverflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
 await page.getByRole('link',{name:'포트폴리오',exact:true}).click();
 checks.returnLink=page.url().endsWith('/index.html');
 reports.push({width,...checks,errors});await page.close();
}
await browser.close();
await fs.writeFile(shots+'/qa-results.json',JSON.stringify(reports,null,2));
console.log(JSON.stringify(reports));
