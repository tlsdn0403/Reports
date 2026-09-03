from PIL import Image, ImageDraw
from pathlib import Path

root = Path(r"C:\Users\tlsdn\Desktop\Reports\tmp\pdfs\im_portfolio")
files = sorted(root.glob("page-*.png"))

for group_idx in range(0, len(files), 5):
    group = files[group_idx : group_idx + 5]
    thumbs = []
    for file in group:
        image = Image.open(file).convert("RGB")
        image.thumbnail((640, 360))
        thumbs.append((file, image.copy()))

    canvas = Image.new("RGB", (660, len(thumbs) * 390), (235, 235, 235))
    draw = ImageDraw.Draw(canvas)
    for index, (file, image) in enumerate(thumbs):
        y = index * 390
        canvas.paste(image, (10, y + 20))
        draw.text((10, y + 3), file.stem, fill=(0, 0, 0))

    canvas.save(root / f"contact-{group_idx // 5 + 1}.jpg", quality=88)
