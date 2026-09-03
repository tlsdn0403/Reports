from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).parent


def contact_sheet(pattern: str, output: str, columns: int, width: int) -> None:
    paths = sorted(ROOT.glob(pattern))
    images = [Image.open(path).convert("RGB") for path in paths]
    thumb_height = round(images[0].height * width / images[0].width)
    label_height = 34
    gap = 18
    rows = (len(images) + columns - 1) // columns
    sheet = Image.new(
        "RGB",
        (
            columns * width + (columns + 1) * gap,
            rows * (thumb_height + label_height) + (rows + 1) * gap,
        ),
        "#111318",
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=18)

    for index, (path, image) in enumerate(zip(paths, images)):
        row, column = divmod(index, columns)
        x = gap + column * (width + gap)
        y = gap + row * (thumb_height + label_height + gap)
        image.thumbnail((width, thumb_height))
        sheet.paste(image, (x, y + label_height))
        draw.text((x, y + 6), path.stem.replace("_", " "), fill="#f2f4f8", font=font)

    sheet.save(ROOT / output, quality=92)


contact_sheet("canva_page_*.png", "canva_contact_sheet.jpg", columns=2, width=596)
contact_sheet("friend_page_*.png", "friend_flickdom_contact_sheet.jpg", columns=2, width=760)
