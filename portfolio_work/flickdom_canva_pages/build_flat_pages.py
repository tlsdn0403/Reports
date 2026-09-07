from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "out"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1366, 768
PURPLE = "#6254f3"
INK = "#111827"
MUTED = "#334155"
LINE = "#1f2937"

FONT_DIR = Path("C:/Windows/Fonts")


def font(size, bold=False):
    name = "malgunbd.ttf" if bold else "malgun.ttf"
    return ImageFont.truetype(str(FONT_DIR / name), size)


def multiline(draw, xy, text, fill, size, bold=False, spacing=5, anchor=None, align="left"):
    draw.multiline_text(xy, text, fill=fill, font=font(size, bold), spacing=spacing, anchor=anchor, align=align)


def crop_cover(path, size):
    img = Image.open(path).convert("RGB")
    sw, sh = img.size
    dw, dh = size
    sr, dr = sw / sh, dw / dh
    if sr > dr:
        nh = sh
        nw = int(nh * dr)
        left = (sw - nw) // 2
        box = (left, 0, left + nw, sh)
    else:
        nw = sw
        nh = int(nw / dr)
        top = (sh - nh) // 2
        box = (0, top, sw, top + nh)
    return img.crop(box).resize(size, Image.Resampling.LANCZOS)


def paste_rounded(base, path, box, radius=8):
    x, y, w, h = box
    img = crop_cover(path, (w, h)).convert("RGBA")
    mask = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, w, h), radius=radius, fill=255)
    base.paste(img, (x, y), mask)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((x, y, x + w, y + h), radius=radius, outline="#dbe3ee", width=1)


def header(draw, eyebrow, title, sub=None):
    draw.text((28, 22), eyebrow, fill=PURPLE, font=font(17, True))
    draw.text((28, 48), title, fill=PURPLE, font=font(54, True))
    if sub:
        draw.text((286, 62), sub, fill=PURPLE, font=font(28, True))
    draw.line((28, 112, 1332, 112), fill=LINE, width=3)


def pill(draw, xy, text, color=INK, w=100):
    x, y = xy
    draw.rounded_rectangle((x, y, x + w, y + 32), radius=16, fill="#ffffff", outline="#cbd5e1", width=1)
    tw = draw.textlength(text, font=font(14, True))
    draw.text((x + (w - tw) / 2, y + 7), text, fill=color, font=font(14, True))


def page1():
    img = Image.new("RGB", (W, H), "#f8fafc")
    d = ImageDraw.Draw(img)
    header(d, "FlickDom / PAGE 01", "FlickDom", "(AI VIBE CODING)")
    pill(d, (1118, 24), "GITHUB", INK, 112)
    pill(d, (1242, 24), "VIDEO", "#dc2626", 92)
    d.rounded_rectangle((1242, 64, 1334, 96), radius=8, fill=PURPLE)
    d.text((1252, 72), "Team Project", fill="#ffffff", font=font(12, True))

    paste_rounded(img, ASSETS / "flickdom-cover.png", (28, 156, 744, 416), 8)
    d.rounded_rectangle((796, 132, 1332, 646), radius=12, fill="#ffffff", outline="#d7dee8", width=1)
    d.line((944, 178, 944, 606), fill="#0ea5e9", width=4)

    rows = [
        ("프로젝트\n이름", "FlickDom (AI VIBE CODING)", 42),
        ("장르", "1 VS 1 전략 플릭 보드게임", 42),
        ("설명", "디스크를 튕겨 보드 칸을 차지하고\n카드 패턴을 완성해 점수를 겨루는\n물리 기반 파티 게임", 70),
        ("개발 인원", "팀 프로젝트", 38),
        ("담당 역할", "Unity MCP 기반 구현 반복,\n멀티플레이 흐름, UI/UX,\n사운드 제작 및 적용", 72),
        ("개발 언어", "C#", 38),
        ("사용 IDE", "Unity 6 Editor, VS Code,\nBlender, Substance 3D Designer", 58),
        ("AI 모델", "GPT-5 Codex, Unity MCP,\nBlender MCP, Substance MCP,\nVARCO AI Sound", 76),
        ("제작 기간", "2026.07.01 ~ 2026.08.10", 42),
    ]
    y = 166
    for label, value, row_h in rows:
        multiline(d, (916, y), label, INK, 15, True, spacing=3, anchor="ra", align="right")
        multiline(d, (982, y), value, INK, 15, True, spacing=4)
        y += row_h

    d.text((28, 684), "GitHub  github.com/AACHANJINAA/FlickDom", fill=MUTED, font=font(16, True))
    d.text((28, 712), "Video  youtube.com/watch?v=ddM9ggItGwQ", fill=MUTED, font=font(16, True))
    img.save(OUT / "flickdom-page-01.png")


def card(draw, base, x, image, title, body):
    draw.rounded_rectangle((x, 132, x + 420, 502), radius=8, fill="#ffffff", outline="#d7dee8", width=1)
    paste_rounded(base, ASSETS / image, (x, 132, 420, 228), 8)
    draw.text((x + 18, 380), title, fill=PURPLE, font=font(22, True))
    multiline(draw, (x + 18, 418), body, INK, 15, True, spacing=4)


def page2():
    img = Image.new("RGB", (W, H), "#f8fafc")
    d = ImageDraw.Draw(img)
    header(d, "FlickDom / PAGE 02", "게임 시스템")
    card(d, img, 28, "flickdom-goal.png", "목표", "3개의 디스크로 보드 칸을 점령하고\n카드 패턴을 완성합니다.")
    card(d, img, 466, "flickdom-control.png", "조작", "디스크를 선택한 뒤 드래그 방향과\n힘으로 발사해 다음 턴 전략을 만듭니다.")
    card(d, img, 904, "flickdom-multi.png", "멀티플레이", "Host가 방을 생성하고 Join Code를\n공유하면 Client가 접속합니다.")

    flows = [
        ("flickdom-multi.png", "시작 전 준비", "Host / Client 역할 확인"),
        ("flickdom-multi.png", "Join Code 입력", "초대를 코드로 교환 및 접속"),
        ("flickdom-goal.png", "상태 표시", "점수 및 역할 상태 확인"),
        ("flickdom-control.png", "결과 전파", "최신 보드 공유 후 시작"),
    ]
    x = 28
    for image, title, body in flows:
        d.rounded_rectangle((x, 516, x + 310, 602), radius=8, fill="#ffffff", outline="#d7dee8", width=1)
        paste_rounded(img, ASSETS / image, (x + 10, 534, 82, 50), 4)
        d.text((x + 108, 532), title, fill=PURPLE, font=font(14, True))
        d.text((x + 108, 554), body, fill=INK, font=font(12, True))
        x += 328

    d.rounded_rectangle((28, 622, 1332, 702), radius=8, fill="#f1f8ff", outline="#dbeafe", width=1)
    d.line((34, 630, 34, 694), fill="#0ea5e9", width=8)
    multiline(d, (56, 640), "AI/MCP 활용 제작\n과정", "#0ea5e9", 21, True, spacing=4)
    multiline(d, (330, 642), "Unity MCP, Blender MCP, Substance MCP와 AI 사운드 제작 흐름을 함께 활용해\n리소스 정리와 구현 반복 속도를 높였습니다.", INK, 17, True, spacing=5)
    img.save(OUT / "flickdom-page-02.png")


page1()
page2()
