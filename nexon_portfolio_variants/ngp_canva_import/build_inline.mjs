import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const sourcePath = path.join(root, "index.html");
const cssPath = path.join(root, "style.css");
const outputPath = path.join(root, "ngp_portfolio_inline.html");

let html = fs.readFileSync(sourcePath, "utf8");
const css = fs.readFileSync(cssPath, "utf8");

html = html.replace(
  '<link rel="stylesheet" href="style.css">',
  `<style>\n${css}\n</style>`,
);

html = html.replace(/src="(assets\/[^\"]+)"/g, (_match, relativePath) => {
  const filePath = path.join(root, relativePath.replaceAll("/", path.sep));
  const extension = path.extname(filePath).toLowerCase();
  const mime = extension === ".png" ? "image/png" : "image/jpeg";
  const data = fs.readFileSync(filePath).toString("base64");
  return `src="data:${mime};base64,${data}"`;
});

fs.writeFileSync(outputPath, html, "utf8");
console.log(outputPath);
