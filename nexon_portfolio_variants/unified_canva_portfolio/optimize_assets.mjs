import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import sharp from "file:///C:/Users/tlsdn/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp/dist/index.mjs";

const root=path.dirname(fileURLToPath(import.meta.url));
const sourceDir=path.join(root,"assets");
const outputDir=path.join(root,"assets-optimized");
fs.mkdirSync(outputDir,{recursive:true});

for(const name of fs.readdirSync(sourceDir)){
  const input=path.join(sourceDir,name);
  const output=path.join(outputDir,name);
  const ext=path.extname(name).toLowerCase();
  let pipeline=sharp(input).resize({width:1366,height:768,fit:"inside",withoutEnlargement:true});
  if(ext===".png") pipeline=pipeline.png({compressionLevel:9,palette:true,quality:82,effort:10});
  else pipeline=pipeline.jpeg({quality:76,mozjpeg:true});
  await pipeline.toFile(output);
}
console.log(outputDir);
