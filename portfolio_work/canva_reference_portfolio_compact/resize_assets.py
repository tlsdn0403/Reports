from pathlib import Path
import shutil

from PIL import Image, ImageOps


SRC = Path("../canva_reference_portfolio/assets")
DST = Path("assets")
MAX_DIM = 1200


def convert_image(path: Path) -> None:
    out = DST / path.name
    try:
        image = Image.open(path)
        image = ImageOps.exif_transpose(image)
        image.thumbnail((MAX_DIM, MAX_DIM), Image.Resampling.LANCZOS)

        ext = path.suffix.lower()
        if ext in {".jpg", ".jpeg"}:
            if image.mode not in {"RGB", "L"}:
                image = image.convert("RGB")
            image.save(out, quality=72, optimize=True, progressive=True)
        elif ext == ".png":
            if image.mode not in {"RGB", "RGBA", "P", "L"}:
                image = image.convert("RGBA")
            image.save(out, optimize=True, compress_level=9)
        else:
            shutil.copy2(path, out)
    except Exception as exc:
        shutil.copy2(path, out)
        print(f"copied {path.name}: {exc}")


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    count = 0
    for path in SRC.iterdir():
        if path.is_file():
            convert_image(path)
            count += 1
    print(f"processed {count} images")


if __name__ == "__main__":
    main()
