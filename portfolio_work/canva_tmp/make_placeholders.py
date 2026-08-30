from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parent
W, H = 1200, 675


def font(size: int, bold: bool = False):
    candidates = [
        r"C:\Windows\Fonts\malgunbd.ttf" if bold else r"C:\Windows\Fonts\malgun.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()


def rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def make_placeholder(filename, eyebrow, title, subtitle, accent):
    img = Image.new("RGB", (W, H), "#111827")
    draw = ImageDraw.Draw(img)

    for y in range(H):
        mix = y / H
        r = int(17 * (1 - mix) + 7 * mix)
        g = int(24 * (1 - mix) + 33 * mix)
        b = int(39 * (1 - mix) + 47 * mix)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    rounded_rect(draw, (56, 56, W - 56, H - 56), 28, "#172033", "#2f3d56", 3)
    rounded_rect(draw, (94, 92, 330, 144), 18, accent)
    draw.text((120, 102), eyebrow, fill="#08111f", font=font(28, True))

    draw.text((94, 230), title, fill="#f8fafc", font=font(74, True))
    draw.text((98, 330), subtitle, fill="#cbd5e1", font=font(34))

    cx, cy = W - 190, H - 170
    draw.ellipse((cx - 64, cy - 64, cx + 64, cy + 64), outline=accent, width=8)
    draw.polygon([(cx - 22, cy - 34), (cx - 22, cy + 34), (cx + 42, cy)], fill=accent)

    draw.text((94, H - 132), "영상 교체 위치", fill="#94a3b8", font=font(30, True))
    img.save(OUT / filename, quality=95)


def make_bubble_project():
    img = Image.new("RGB", (W, H), "#102033")
    draw = ImageDraw.Draw(img)
    for y in range(H):
        mix = y / H
        draw.line(
            [(0, y), (W, y)],
            fill=(int(16 + 4 * mix), int(32 + 54 * mix), int(51 + 68 * mix)),
        )
    rounded_rect(draw, (54, 54, W - 54, H - 54), 30, "#16263c", "#38bdf8", 4)
    draw.text((90, 96), "PROJECT 03", fill="#67e8f9", font=font(32, True))
    draw.text((90, 230), "Bubble Fighter IP", fill="#f8fafc", font=font(72, True))
    draw.text((94, 326), "개인 개발 프로젝트", fill="#cbd5e1", font=font(44, True))
    draw.text((94, 430), "대표 이미지 삽입", fill="#94a3b8", font=font(34))
    for x, y, r in [(850, 170, 72), (1000, 280, 46), (910, 420, 62), (1080, 500, 34)]:
        draw.ellipse((x - r, y - r, x + r, y + r), outline="#7dd3fc", width=6)
    img.save(OUT / "bubble_project_placeholder.png", quality=95)


make_placeholder(
    "truck_item_load_placeholder.png",
    "TRUCK 01",
    "아이템 적재",
    "파밍 아이템을 트럭 적재 공간에 싣는 상호작용",
    "#34d399",
)
make_placeholder(
    "truck_machine_gun_placeholder.png",
    "TRUCK 02",
    "기관총 사용",
    "탑승 상태에서 조준, 발사, 카메라 흐름을 보여줄 영상",
    "#fbbf24",
)
make_placeholder(
    "truck_drive_placeholder.png",
    "TRUCK 03",
    "트럭 운전",
    "Possess 기반 차량 조작과 탑승 이동을 보여줄 영상",
    "#60a5fa",
)
make_bubble_project()
