import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const { SKILL_DIR, TMP_DIR, FINAL_PPTX, RUNTIME_PYTHON } = process.env;
if (!path.isAbsolute(SKILL_DIR ?? "") || !path.isAbsolute(TMP_DIR ?? "") || !path.isAbsolute(FINAL_PPTX ?? "")) {
  throw new Error("Set absolute SKILL_DIR, TMP_DIR, and FINAL_PPTX");
}

const workspaceDir = "C:\\Users\\Administrator\\Desktop\\보고서, 기획서";
const sourceDir = path.join(workspaceDir, "portfolio_work", "flickdom_canva_pages", "out");
const pageImages = [
  path.join(sourceDir, "flickdom-page-01.png"),
  path.join(sourceDir, "flickdom-page-02.png"),
];

const { resolvePresentationFont, finalizePresentation } = await import(
  pathToFileURL(path.join(SKILL_DIR, "container_tools", "artifact_tool_utils.mjs")).href,
);

await fs.mkdir(TMP_DIR, { recursive: true });
await fs.mkdir(path.dirname(FINAL_PPTX), { recursive: true });

const family = resolvePresentationFont();
const presentation = Presentation.create({
  slideSize: { width: 1280, height: 720 },
});
const slides = [];

function scaleRect({ x, y, w, h }) {
  return {
    left: Math.round((x / 1366) * 1280),
    top: Math.round((y / 768) * 720),
    width: Math.round((w / 1366) * 1280),
    height: Math.round((h / 768) * 720),
  };
}

function addLinkHotspot(slide, name, frame) {
  const linkBox = slide.shapes.add({
    geometry: "rect",
    name,
    position: frame,
    fill: "transparent",
    line: { fill: "none", width: 0 },
  });
  linkBox.bringToFront();
}

for (const [index, imagePath] of pageImages.entries()) {
  const slide = presentation.slides.add();
  slides.push(slide);
  slide.background.fill = "#FFFFFF";
  const imageBytes = await fs.readFile(imagePath);
  slide.images.add({
    blob: imageBytes,
    contentType: "image/png",
    alt: `FlickDom portfolio page ${index + 1}`,
    fit: "cover",
    position: { left: 0, top: 0, width: 1280, height: 720 },
  });

  if (index === 0) {
    addLinkHotspot(slide, "github-link-hotspot", scaleRect({ x: 1121, y: 23, w: 106, h: 34 }));
    addLinkHotspot(slide, "video-link-hotspot", scaleRect({ x: 1239, y: 23, w: 89, h: 34 }));
  }
}

const stagingDir = path.join(workspaceDir, "portfolio_work", "flickdom_canva_pages", ".codex-finalizer-linked");
await fs.mkdir(stagingDir, { recursive: true });
const candidatePath = path.join(stagingDir, "candidate-linked-flickdom.pptx");
await (await PresentationFile.exportPptx(presentation)).save(candidatePath);

const previewDir = path.join(TMP_DIR, "previews");
await fs.mkdir(previewDir, { recursive: true });
for (const [index, slide] of slides.entries()) {
  const preview = await presentation.export({ slide, format: "png", scale: 1 });
  await fs.writeFile(path.join(previewDir, `slide-${index + 1}.png`), new Uint8Array(await preview.arrayBuffer()));
}

const result = await finalizePresentation({
  explicitTotalSlideCount: 2,
  requiredNativeTableOwnerSlides: [],
  requiredNativeChartOwnerSlides: [],
  workspaceDir,
  candidatePath,
  finalPath: FINAL_PPTX,
  pythonExecutable: RUNTIME_PYTHON,
  integrityValidatorPath: path.join(SKILL_DIR, "container_tools", "inspect_presentation_package_integrity.py"),
  layoutValidatorPath: path.join(SKILL_DIR, "container_tools", "inspect_presentation_layout_geometry.py"),
  layoutArgs: [
    "--expected-slide-size-emu",
    "12192000,6858000",
    "--validate-heading-fit",
  ],
  fontPolicy: { basis: "design", families: [family] },
  verifyArtifactToolImport: true,
  receiptPath: path.join(stagingDir, `${path.basename(FINAL_PPTX)}.validation.json`),
});

console.log(JSON.stringify({
  finalPath: FINAL_PPTX,
  candidatePath,
  previewDir,
  warnings: result.warnings ?? [],
}, null, 2));
