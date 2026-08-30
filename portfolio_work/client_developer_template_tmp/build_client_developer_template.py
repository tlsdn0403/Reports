from __future__ import annotations

from datetime import datetime, timezone
from html import escape as html_escape
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape
import zipfile


ROOT = Path(r"C:\Users\Administrator\Desktop\보고서, 기획서")
TMP_DIR = ROOT / "portfolio_work" / "client_developer_template_tmp"
OUT_DIR = ROOT / "portfolio_work" / "client_developer_template_output"
FINAL_PPTX = OUT_DIR / "클라이언트_개발자_포트폴리오_기본템플릿.pptx"
PREVIEW_HTML = OUT_DIR / "클라이언트_개발자_포트폴리오_기본템플릿_preview.html"

SLIDE_W = 1280
SLIDE_H = 720

PX_TO_EMU = 9525

BG = "F7F4ED"
INK = "111111"
MUTED = "5F5F5F"
ACCENT = "0E5AA7"
GREEN = "2E6A2D"
GREEN_2 = "6BA84F"
BLUE = "3D7FD6"
ORANGE = "F2A541"
RED = "D94F4F"
YELLOW = "F3CE5A"
LINE = "D8D2C5"
SOFT = "EFE9DC"
WHITE = "FFFFFF"


def emu(value: float) -> int:
    return int(round(value * PX_TO_EMU))


def clean_hex(color: str) -> str:
    return color.replace("#", "").upper()


def xml_text(value: str) -> str:
    return xml_escape(value, {'"': "&quot;", "'": "&apos;"})


def fill_xml(fill: str | None) -> str:
    if fill is None or fill == "none":
        return "<a:noFill/>"
    return f'<a:solidFill><a:srgbClr val="{clean_hex(fill)}"/></a:solidFill>'


def line_xml(line: str | None = None, width: float = 1, dash: bool = False) -> str:
    if line is None or line == "none":
        return "<a:ln><a:noFill/></a:ln>"
    dash_xml = '<a:prstDash val="dash"/>' if dash else ""
    return (
        f'<a:ln w="{emu(width)}">'
        f'<a:solidFill><a:srgbClr val="{clean_hex(line)}"/></a:solidFill>'
        f"{dash_xml}</a:ln>"
    )


def para_xml(
    text: str,
    font_size: int,
    color: str = INK,
    bold: bool = False,
    underline: bool = False,
    align: str = "l",
    break_lines: bool = True,
) -> str:
    lines = text.split("\n") if break_lines else [text]
    paragraphs = []
    for line in lines:
        attrs = [f'lang="ko-KR"', f'sz="{font_size * 100}"']
        if bold:
            attrs.append('b="1"')
        if underline:
            attrs.append('u="sng"')
        attrs_joined = " ".join(attrs)
        paragraphs.append(
            f'<a:p><a:pPr algn="{align}"/>'
            f'<a:r><a:rPr {attrs_joined}>'
            f'<a:solidFill><a:srgbClr val="{clean_hex(color)}"/></a:solidFill>'
            f'<a:latin typeface="Malgun Gothic"/><a:ea typeface="Malgun Gothic"/>'
            f"</a:rPr><a:t>{xml_text(line)}</a:t></a:r>"
            f'<a:endParaRPr lang="ko-KR" sz="{font_size * 100}"/></a:p>'
        )
    return "".join(paragraphs)


def text_body(
    text: str,
    font_size: int,
    color: str = INK,
    bold: bool = False,
    underline: bool = False,
    align: str = "l",
    valign: str = "t",
    margin: int = 0,
) -> str:
    anchor = "ctr" if valign == "mid" else valign
    return (
        f'<p:txBody><a:bodyPr wrap="square" anchor="{anchor}" '
        f'lIns="{emu(margin)}" rIns="{emu(margin)}" tIns="{emu(margin)}" bIns="{emu(margin)}">'
        "<a:spAutoFit/></a:bodyPr><a:lstStyle/>"
        f"{para_xml(text, font_size, color, bold, underline, align)}"
        "</p:txBody>"
    )


class Slide:
    def __init__(self, title: str, bg: str = BG):
        self.title = title
        self.bg = bg
        self.items: list[str] = []
        self.preview: list[dict] = []
        self.next_id = 2

    def _id(self) -> int:
        value = self.next_id
        self.next_id += 1
        return value

    def shape(
        self,
        name: str,
        x: float,
        y: float,
        w: float,
        h: float,
        geometry: str = "rect",
        fill: str | None = None,
        line: str | None = None,
        line_width: float = 1,
        dash: bool = False,
        text: str | None = None,
        font_size: int = 18,
        color: str = INK,
        bold: bool = False,
        underline: bool = False,
        align: str = "l",
        valign: str = "t",
        margin: int = 0,
        opacity: float = 1.0,
    ) -> None:
        sid = self._id()
        tx_box = ' txBox="1"' if geometry == "textbox" or text is not None else ""
        no_text = "" if text is None else text_body(text, font_size, color, bold, underline, align, valign, margin)
        self.items.append(
            f"<p:sp><p:nvSpPr><p:cNvPr id=\"{sid}\" name=\"{xml_text(name)}\"/>"
            f"<p:cNvSpPr{tx_box}/><p:nvPr/></p:nvSpPr>"
            f"<p:spPr><a:xfrm><a:off x=\"{emu(x)}\" y=\"{emu(y)}\"/>"
            f"<a:ext cx=\"{emu(w)}\" cy=\"{emu(h)}\"/></a:xfrm>"
            f"<a:prstGeom prst=\"{geometry if geometry != 'textbox' else 'rect'}\"><a:avLst/></a:prstGeom>"
            f"{fill_xml(fill)}{line_xml(line, line_width, dash)}</p:spPr>{no_text}</p:sp>"
        )
        style = {
            "left": x,
            "top": y,
            "width": w,
            "height": h,
            "fill": f"#{clean_hex(fill)}" if fill and fill != "none" else "transparent",
            "border": f"{line_width}px {'dashed' if dash else 'solid'} #{clean_hex(line)}" if line and line != "none" else "none",
            "borderRadius": "50%" if geometry == "ellipse" else ("12px" if geometry == "roundRect" else "0"),
            "opacity": opacity,
        }
        self.preview.append(
            {
                "type": "shape",
                "geometry": geometry,
                "text": text,
                "font_size": font_size,
                "color": f"#{clean_hex(color)}",
                "bold": bold,
                "underline": underline,
                "align": align,
                "valign": valign,
                "style": style,
            }
        )

    def textbox(
        self,
        name: str,
        x: float,
        y: float,
        w: float,
        h: float,
        text: str,
        font_size: int,
        color: str = INK,
        bold: bool = False,
        underline: bool = False,
        align: str = "l",
        valign: str = "t",
        margin: int = 0,
    ) -> None:
        self.shape(
            name,
            x,
            y,
            w,
            h,
            "textbox",
            "none",
            "none",
            text=text,
            font_size=font_size,
            color=color,
            bold=bold,
            underline=underline,
            align=align,
            valign=valign,
            margin=margin,
        )

    def rect(self, name: str, x: float, y: float, w: float, h: float, fill: str, line: str | None = None) -> None:
        self.shape(name, x, y, w, h, "rect", fill, line)

    def rule(self, x: float, y: float, w: float, color: str = INK, h: float = 3) -> None:
        self.rect("rule", x, y, w, h, color, None)

    def footer(self, page: int) -> None:
        self.textbox("footer-role", 64, 674, 260, 20, "CLIENT DEVELOPER PORTFOLIO", 9, MUTED, True)
        self.textbox("footer-page", 1160, 674, 56, 20, f"{page:02}", 10, MUTED, True, align="r")

    def image_placeholder(
        self,
        name: str,
        x: float,
        y: float,
        w: float,
        h: float,
        label: str,
        circle: bool = False,
    ) -> None:
        self.shape(name, x, y, w, h, "ellipse" if circle else "roundRect", SOFT, LINE, 1.2, True)
        self.textbox(f"{name}-label", x + 16, y + h / 2 - 14, w - 32, 28, label, 16, MUTED, True, align="c", valign="mid")


def add_title(slide: Slide, section: str, title: str, page: int | None = None) -> None:
    slide.textbox("section", 64, 50, 260, 24, section, 16, INK, True)
    slide.textbox("title", 64, 86, 680, 58, title, 40, INK, True)
    slide.rule(64, 154, 128, INK, 4)
    if page is not None:
        slide.footer(page)


def add_info_lines(slide: Slide, x: float, y: float, lines: list[tuple[str, str]]) -> None:
    row_h = 34
    for i, (label, value) in enumerate(lines):
        yy = y + i * row_h
        slide.textbox(f"info-label-{i}", x, yy, 96, 26, label, 15, INK, True)
        slide.textbox(f"info-value-{i}", x + 104, yy, 380, 26, value, 15, INK)


def add_chip(slide: Slide, x: float, y: float, w: float, text: str, fill: str = WHITE, color: str = INK) -> None:
    slide.shape(f"chip-{text}", x, y, w, 32, "roundRect", fill, LINE, text=text, font_size=13, color=color, bold=True, align="c", valign="mid", margin=4)


def add_card(
    slide: Slide,
    x: float,
    y: float,
    w: float,
    h: float,
    heading: str,
    body: str,
    index: str | None = None,
) -> None:
    slide.shape(f"card-{heading}", x, y, w, h, "roundRect", WHITE, LINE)
    if index:
        slide.textbox(f"card-index-{heading}", x + 22, y + 20, 54, 28, index, 18, ACCENT, True)
        tx = x + 76
        ww = w - 98
    else:
        tx = x + 22
        ww = w - 44
    slide.textbox(f"card-heading-{heading}", tx, y + 20, ww, 30, heading, 20, INK, True)
    slide.textbox(f"card-body-{heading}", x + 22, y + 64, w - 44, h - 84, body, 15, MUTED)


def add_table_grid(
    slide: Slide,
    x: float,
    y: float,
    col_widths: list[float],
    row_heights: list[float],
    values: list[list[str]],
    fills: dict[tuple[int, int], str] | None = None,
    font_size: int = 12,
    header_rows: int = 1,
) -> None:
    fills = fills or {}
    yy = y
    for r, rh in enumerate(row_heights):
        xx = x
        for c, cw in enumerate(col_widths):
            fill = fills.get((r, c), GREEN if r < header_rows else WHITE)
            color = WHITE if r < header_rows or fill in {GREEN, BLUE, RED} else INK
            bold = r < header_rows
            slide.shape(
                f"table-r{r}-c{c}",
                xx,
                yy,
                cw,
                rh,
                "rect",
                fill,
                "AFA99E",
                0.8,
                text=values[r][c],
                font_size=font_size,
                color=color,
                bold=bold,
                align="c",
                valign="mid",
                margin=3,
            )
            xx += cw
        yy += rh


def build_slides() -> list[Slide]:
    slides: list[Slide] = []

    s = Slide("cover")
    s.textbox("eyebrow", 64, 58, 320, 28, "CLIENT DEVELOPER", 16, INK, True)
    s.textbox("cover-title", 64, 112, 600, 136, "[이름]\nPortfolio", 56, INK, True)
    s.rule(66, 270, 164, INK, 5)
    s.textbox("subtitle", 64, 300, 520, 72, "Unity / Unreal 기반 게임 클라이언트 개발자 지원용\n프로젝트 중심 포트폴리오 템플릿", 22, MUTED)
    s.image_placeholder("cover-image", 740, 76, 412, 412, "[대표 프로젝트 이미지]", circle=True)
    add_chip(s, 64, 448, 126, "Unity")
    add_chip(s, 204, 448, 126, "C# / C++")
    add_chip(s, 344, 448, 158, "Gameplay")
    add_chip(s, 516, 448, 138, "UI/UX")
    s.textbox("contact", 64, 594, 760, 24, "Email  [email@example.com]    GitHub  [github.com/id]    Blog  [blog-url]", 16, ACCENT, True, underline=True)
    s.textbox("date", 1030, 594, 160, 24, "2026", 16, MUTED, True, align="r")
    slides.append(s)

    s = Slide("profile")
    add_title(s, "Profile", "개발자로서의 방향", 2)
    s.image_placeholder("profile-photo", 82, 210, 236, 236, "[프로필 사진]", circle=True)
    s.textbox("profile-name", 92, 476, 220, 34, "[이름]", 24, INK, True, align="c")
    s.textbox("profile-role", 76, 514, 252, 44, "게임 클라이언트 개발자\n[지원 직무/경력]", 15, MUTED, align="c")
    s.textbox("intro-title", 416, 214, 660, 32, "한 문장 소개", 24, INK, True)
    s.textbox("intro-body", 416, 258, 678, 76, "플레이어 경험을 기준으로 기능을 설계하고, 구현 결과를 영상/코드/수치로 설명하는 개발자입니다.", 21, INK)
    add_card(s, 416, 372, 220, 142, "강점 01", "입력, 카메라, 캐릭터 상태 전환 등 플레이 감각과 직접 닿는 시스템 구현", "01")
    add_card(s, 656, 372, 220, 142, "강점 02", "UI 흐름, 피드백, 사운드 연결처럼 사용자가 체감하는 완성도 개선", "02")
    add_card(s, 896, 372, 220, 142, "강점 03", "협업 기록, 이슈 정리, 일정 공유를 통해 재현 가능한 개발 과정 유지", "03")
    slides.append(s)

    s = Slide("skills")
    add_title(s, "Skills", "클라이언트 개발 역량을 한눈에 보이게", 3)
    headers = ["영역", "주요 기술", "보여줄 근거"]
    values = [
        headers,
        ["Engine", "Unity / Unreal / UMG", "프로젝트명, 씬 구조, 블루프린트 또는 C# 코드"],
        ["Language", "C# / C++ / Python", "핵심 클래스, 알고리즘, 자동화 스크립트"],
        ["Gameplay", "Input / Character / Camera / AI", "플레이 영상, 구현 전후 비교"],
        ["UI/UX", "HUD / Menu / Feedback", "와이어프레임, 이벤트 흐름, 사용성 개선"],
        ["Tools", "Git / Jira / Notion / Figma", "커밋 링크, 이슈 보드, 일정표"],
    ]
    add_table_grid(s, 92, 196, [170, 380, 560], [42, 58, 58, 58, 58, 58], values, font_size=14)
    s.textbox("note", 92, 580, 850, 42, "작성 팁: 단순 나열보다 '어떤 프로젝트에서 어떤 문제를 해결했는지'가 보이도록 근거 칸을 채우세요.", 18, MUTED)
    slides.append(s)

    s = Slide("projects")
    add_title(s, "Projects", "대표 프로젝트는 2~3개만 깊게 보여주기", 4)
    add_card(s, 84, 205, 330, 250, "Project 01", "프로젝트명 / 장르 / 플랫폼\n담당: 플레이어, UI, 사운드\n핵심 성과: [수치 또는 결과]\n링크: 영상 / GitHub", "01")
    add_card(s, 474, 205, 330, 250, "Project 02", "프로젝트명 / 장르 / 플랫폼\n담당: 네트워크, 최적화, 툴\n핵심 성과: [수치 또는 결과]\n링크: 빌드 / GitHub", "02")
    add_card(s, 864, 205, 330, 250, "Project 03", "프로젝트명 / 장르 / 플랫폼\n담당: 콘텐츠 시스템, UI\n핵심 성과: [수치 또는 결과]\n링크: 영상 / 문서", "03")
    s.textbox("project-filter", 84, 505, 900, 42, "선택 기준: 지원 직무와 가장 가까운 기능, 본인 기여도가 큰 기능, 면접에서 코드로 설명 가능한 기능", 18, MUTED)
    slides.append(s)

    s = Slide("project-detail")
    s.textbox("project-num", 64, 52, 220, 42, "Project 01", 30, INK, True)
    s.textbox("project-name", 110, 126, 260, 48, "[프로젝트명]", 32, INK, True, align="c")
    s.image_placeholder("project-thumb", 88, 196, 228, 228, "[게임 이미지]", circle=True)
    s.textbox("project-links", 94, 458, 230, 30, "영상 링크   GitHub 코드", 17, ACCENT, True, underline=True, align="c")
    add_info_lines(
        s,
        72,
        520,
        [
            ("기간", "YYYY.MM ~ YYYY.MM"),
            ("구성", "개인 / 팀  N명"),
            ("역할", "플레이어, UI/UX, Sound"),
            ("엔진", "Unity / Unreal"),
            ("플랫폼", "PC / Mobile / VR"),
        ],
    )
    s.textbox("evidence-title", 454, 54, 640, 38, "핵심 구현 화면 또는 작업 증거", 28, INK, True, align="c")
    s.image_placeholder("project-evidence", 454, 108, 756, 456, "[대표 스크린샷 / 플레이 영상 캡처 / 작업표]", False)
    s.textbox("evidence-caption", 454, 584, 756, 28, "캡션: 어떤 기능을 직접 구현했고, 사용자가 어떻게 체감하는지 한 문장으로 설명", 16, MUTED)
    s.footer(5)
    slides.append(s)

    s = Slide("contribution")
    add_title(s, "Contribution", "내가 만든 기능은 역할보다 결과로 설명하기", 6)
    add_card(s, 92, 205, 330, 300, "기능 01", "문제: [플레이/UX 문제]\n구현: [클래스/시스템]\n결과: [개선된 동작]\n증거: 영상 시간대 또는 코드 링크", "01")
    add_card(s, 474, 205, 330, 300, "기능 02", "문제: [반복 작업/버그]\n구현: [툴/자동화/리팩터링]\n결과: [시간 단축/안정성]\n증거: 커밋 또는 전후 비교", "02")
    add_card(s, 856, 205, 330, 300, "기능 03", "문제: [성능/입력/카메라]\n구현: [알고리즘/상태관리]\n결과: [FPS/응답성/품질]\n증거: 프로파일링 수치", "03")
    s.textbox("contribution-tip", 92, 556, 970, 34, "권장 형식: 문제 -> 구현 판단 -> 결과 -> 증거. 면접관이 바로 질문할 수 있는 단위로 자르세요.", 18, MUTED)
    slides.append(s)

    s = Slide("problem")
    add_title(s, "Problem Solving", "기술 문제는 판단 과정까지 보여주기", 7)
    add_card(s, 74, 214, 300, 220, "Before", "증상: [예: 입력 지연 / 카메라 흔들림 / UI 중복]\n원인 가설: [어디서 병목이 났는지]\n재현 조건: [맵/기기/상황]", None)
    add_card(s, 404, 214, 300, 220, "Approach", "대안 A: [장단점]\n대안 B: [장단점]\n선택 이유: [유지보수/성능/일정]", None)
    add_card(s, 734, 214, 300, 220, "Result", "결과: [수치 또는 동작 변화]\n검증: [테스트/프로파일링]\n남은 개선: [후속 작업]", None)
    s.shape("code-box", 74, 476, 960, 96, "roundRect", "1D1D1D", "1D1D1D")
    s.textbox("code-text", 96, 500, 900, 42, "public void ApplyInput(Vector2 input) { /* 핵심 코드 일부 */ }", 20, "F5F5F5")
    s.textbox("problem-note", 1060, 218, 116, 222, "이미지보다\n원인과 판단을\n더 크게", 22, ACCENT, True, align="c")
    slides.append(s)

    s = Slide("architecture")
    add_title(s, "Architecture", "클라이언트 구조는 책임 단위로 단순화하기", 8)
    nodes = [
        (106, 242, "Input\nSystem"),
        (326, 242, "Player\nController"),
        (546, 242, "Game\nState"),
        (766, 242, "UI / HUD"),
        (986, 242, "Feedback\nSound/VFX"),
    ]
    for x, y, text in nodes:
        s.shape(f"node-{text}", x, y, 150, 96, "roundRect", WHITE, LINE, text=text, font_size=18, color=INK, bold=True, align="c", valign="mid", margin=5)
    for x in [266, 486, 706, 926]:
        s.shape("flow-line", x, 286, 38, 8, "rect", ACCENT, None)
        s.shape("flow-dot", x + 36, 276, 22, 28, "rtTriangle", ACCENT, None)
    s.textbox("arch-desc", 130, 400, 980, 78, "면접용 구조도는 완전한 UML보다 '내 코드가 어디에 있고 어떤 책임을 갖는지'가 빠르게 읽히는 정도가 좋습니다.", 21, MUTED, align="c")
    add_card(s, 176, 508, 260, 86, "데이터 흐름", "입력 -> 상태 -> UI/피드백", None)
    add_card(s, 510, 508, 260, 86, "확장 지점", "스킬, 아이템, 옵션, 저장", None)
    add_card(s, 844, 508, 260, 86, "검증 방법", "플레이 테스트, 로그, 프로파일러", None)
    slides.append(s)

    s = Slide("schedule")
    s.textbox("schedule-title", 360, 50, 560, 40, "팀원간의 간트 차트로 진행 공유", 28, INK, True, align="c")
    s.textbox("schedule-section", 64, 58, 220, 32, "Collaboration", 24, INK, True)
    values = [
        ["작업 내용", "우선도", "W1", "W2", "W3", "W4", "비고"],
        ["플레이어 이동/점프", "매우 높음", "완료", "", "", "", "완료"],
        ["카메라 추적/보정", "높음", "진행", "완료", "", "", "완료"],
        ["HUD/메뉴 UI", "높음", "", "진행", "완료", "", "완료"],
        ["사운드/피드백", "보통", "", "", "진행", "완료", "완료"],
        ["버그 수정/폴리싱", "높음", "", "", "진행", "진행", "개선"],
        ["빌드/발표 준비", "보통", "", "", "", "완료", "완료"],
    ]
    fills = {}
    for r in range(1, len(values)):
        fills[(r, 1)] = RED if values[r][1] == "매우 높음" else ORANGE if values[r][1] == "높음" else YELLOW
        fills[(r, 6)] = GREEN_2 if values[r][6] == "완료" else BLUE
        for c in range(2, 6):
            if values[r][c] == "완료":
                fills[(r, c)] = GREEN_2
            elif values[r][c] == "진행":
                fills[(r, c)] = RED
    add_table_grid(s, 72, 120, [360, 120, 90, 90, 90, 90, 150], [42, 54, 54, 54, 54, 54, 54], values, fills, font_size=12)
    s.textbox("schedule-caption", 72, 540, 970, 40, "작성 팁: 실제 일정표를 그대로 붙이기보다, 본인이 관리한 이슈와 의사소통 방식이 드러나는 핵심 항목만 남기세요.", 18, MUTED)
    s.footer(9)
    slides.append(s)

    s = Slide("closing")
    add_title(s, "Wrap-up", "면접관이 기억할 한 줄로 끝내기", 10)
    s.textbox("closing-statement", 112, 208, 640, 96, "저는 [핵심 강점]을 바탕으로\n[지원 회사/프로젝트]의 클라이언트 완성도에 기여하겠습니다.", 30, INK, True)
    add_card(s, 112, 354, 292, 132, "바로 보여줄 것", "플레이 영상, 실행 빌드, 핵심 코드 링크", "01")
    add_card(s, 444, 354, 292, 132, "바로 설명할 것", "문제, 선택한 구현, 결과, 트레이드오프", "02")
    add_card(s, 776, 354, 292, 132, "바로 답할 것", "내 담당 범위, 협업 방식, 개선 계획", "03")
    s.textbox("closing-links", 112, 552, 810, 34, "GitHub  [github.com/id]    Portfolio  [url]    Email  [email@example.com]", 18, ACCENT, True, underline=True)
    slides.append(s)

    return slides


def slide_xml(slide: Slide) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg><p:bgPr>{fill_xml(slide.bg)}<a:effectLst/></p:bgPr></p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      {"".join(slide.items)}
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>'''


def presentation_xml(slide_count: int) -> str:
    ids = "\n".join(
        f'    <p:sldId id="{255 + i}" r:id="rId{i + 1}"/>' for i in range(1, slide_count + 1)
    )
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>
  <p:sldIdLst>
{ids}
  </p:sldIdLst>
  <p:sldSz cx="{emu(SLIDE_W)}" cy="{emu(SLIDE_H)}" type="screen16x9"/>
  <p:notesSz cx="6858000" cy="9144000"/>
  <p:defaultTextStyle>
    <a:defPPr><a:defRPr lang="ko-KR"><a:latin typeface="Malgun Gothic"/><a:ea typeface="Malgun Gothic"/></a:defRPr></a:defPPr>
  </p:defaultTextStyle>
</p:presentation>'''


def presentation_rels(slide_count: int) -> str:
    rels = [
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>'
    ]
    for i in range(1, slide_count + 1):
        rels.append(
            f'<Relationship Id="rId{i + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>'
        )
    rels.append(
        f'<Relationship Id="rId{slide_count + 2}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>'
    )
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  {"".join(rels)}
</Relationships>'''


def content_types(slide_count: int) -> str:
    overrides = [
        '<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>',
        '<Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>',
        '<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>',
        '<Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>',
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
        '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>',
    ]
    for i in range(1, slide_count + 1):
        overrides.append(
            f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        )
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  {"".join(overrides)}
</Types>'''


def root_rels() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''


def slide_rel() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>'''


def slide_master_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld><p:bg><p:bgPr>{fill_xml(BG)}<a:effectLst/></p:bgPr></p:bg><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
  <p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst>
  <p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles>
</p:sldMaster>'''


def slide_master_rel() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>'''


def slide_layout_xml() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1">
  <p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>'''


def slide_layout_rel() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>'''


def theme_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Client Developer Portfolio">
  <a:themeElements>
    <a:clrScheme name="Portfolio">
      <a:dk1><a:srgbClr val="{INK}"/></a:dk1><a:lt1><a:srgbClr val="{BG}"/></a:lt1>
      <a:dk2><a:srgbClr val="{MUTED}"/></a:dk2><a:lt2><a:srgbClr val="{WHITE}"/></a:lt2>
      <a:accent1><a:srgbClr val="{ACCENT}"/></a:accent1><a:accent2><a:srgbClr val="{GREEN}"/></a:accent2>
      <a:accent3><a:srgbClr val="{ORANGE}"/></a:accent3><a:accent4><a:srgbClr val="{RED}"/></a:accent4>
      <a:accent5><a:srgbClr val="{YELLOW}"/></a:accent5><a:accent6><a:srgbClr val="{BLUE}"/></a:accent6>
      <a:hlink><a:srgbClr val="{ACCENT}"/></a:hlink><a:folHlink><a:srgbClr val="6A4C93"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="Malgun Gothic">
      <a:majorFont><a:latin typeface="Malgun Gothic"/><a:ea typeface="Malgun Gothic"/><a:cs typeface="Malgun Gothic"/></a:majorFont>
      <a:minorFont><a:latin typeface="Malgun Gothic"/><a:ea typeface="Malgun Gothic"/><a:cs typeface="Malgun Gothic"/></a:minorFont>
    </a:fontScheme>
    <a:fmtScheme name="Portfolio"><a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst><a:lnStyleLst><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst><a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst><a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst></a:fmtScheme>
  </a:themeElements>
  <a:objectDefaults/><a:extraClrSchemeLst/>
</a:theme>'''


def core_xml() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>클라이언트 개발자 포트폴리오 기본템플릿</dc:title>
  <dc:creator>Codex</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>'''


def app_xml(slide_count: int) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Codex</Application><PresentationFormat>On-screen Show (16:9)</PresentationFormat><Slides>{slide_count}</Slides><Company></Company><AppVersion>16.0000</AppVersion>
</Properties>'''


def write_pptx(slides: list[Slide]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(FINAL_PPTX, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types(len(slides)))
        z.writestr("_rels/.rels", root_rels())
        z.writestr("docProps/core.xml", core_xml())
        z.writestr("docProps/app.xml", app_xml(len(slides)))
        z.writestr("ppt/presentation.xml", presentation_xml(len(slides)))
        z.writestr("ppt/_rels/presentation.xml.rels", presentation_rels(len(slides)))
        z.writestr("ppt/theme/theme1.xml", theme_xml())
        z.writestr("ppt/slideMasters/slideMaster1.xml", slide_master_xml())
        z.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", slide_master_rel())
        z.writestr("ppt/slideLayouts/slideLayout1.xml", slide_layout_xml())
        z.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", slide_layout_rel())
        for idx, slide in enumerate(slides, 1):
            z.writestr(f"ppt/slides/slide{idx}.xml", slide_xml(slide))
            z.writestr(f"ppt/slides/_rels/slide{idx}.xml.rels", slide_rel())


def preview_html(slides: list[Slide]) -> str:
    html_slides = []
    for idx, slide in enumerate(slides, 1):
        elements = []
        for item in slide.preview:
            st = item["style"]
            flex = "center" if item["valign"] == "mid" else "flex-start"
            text_align = {"c": "center", "r": "right"}.get(item["align"], "left")
            weight = "700" if item["bold"] else "400"
            deco = "text-decoration: underline;" if item["underline"] else ""
            text = ""
            if item["text"] is not None:
                text = html_escape(item["text"]).replace("\n", "<br>")
            elements.append(
                f'<div class="el" style="left:{st["left"]}px;top:{st["top"]}px;width:{st["width"]}px;height:{st["height"]}px;'
                f'background:{st["fill"]};border:{st["border"]};border-radius:{st["borderRadius"]};'
                f'font-size:{item["font_size"]}px;color:{item["color"]};font-weight:{weight};text-align:{text_align};'
                f'align-items:{flex};justify-content:{flex};{deco}">{text}</div>'
            )
        html_slides.append(f'<section class="slide"><div class="page-num">{idx:02}</div>{"".join(elements)}</section>')
    return f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>클라이언트 개발자 포트폴리오 기본템플릿 Preview</title>
<style>
body {{ margin: 0; background: #2b2b2b; font-family: "Malgun Gothic", Arial, sans-serif; }}
.wrap {{ display: grid; gap: 28px; padding: 28px; justify-content: center; }}
.slide {{ position: relative; width: {SLIDE_W}px; height: {SLIDE_H}px; background: #{BG}; overflow: hidden; box-shadow: 0 8px 28px rgba(0,0,0,.25); transform: scale(.82); transform-origin: top center; margin-bottom: -104px; }}
.el {{ position: absolute; box-sizing: border-box; display: flex; padding: 0; line-height: 1.25; white-space: normal; overflow: hidden; }}
.page-num {{ position:absolute; right: 28px; top: 18px; color:#AAA; font-size:12px; }}
</style>
</head>
<body><main class="wrap">{"".join(html_slides)}</main></body></html>'''


def validate_package() -> None:
    required = {
        "[Content_Types].xml",
        "_rels/.rels",
        "ppt/presentation.xml",
        "ppt/_rels/presentation.xml.rels",
        "ppt/theme/theme1.xml",
    }
    with zipfile.ZipFile(FINAL_PPTX, "r") as z:
        names = set(z.namelist())
        missing = required - names
        if missing:
            raise RuntimeError(f"Missing required pptx parts: {sorted(missing)}")
        slide_names = sorted(n for n in names if n.startswith("ppt/slides/slide") and n.endswith(".xml"))
        if len(slide_names) != 10:
            raise RuntimeError(f"Expected 10 slides, found {len(slide_names)}")
        for name in slide_names:
            data = z.read(name).decode("utf-8")
            if "<p:spTree>" not in data or "<p:sp>" not in data:
                raise RuntimeError(f"Slide has no editable shapes: {name}")


def main() -> None:
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    slides = build_slides()
    write_pptx(slides)
    PREVIEW_HTML.write_text(preview_html(slides), encoding="utf-8")
    validate_package()
    print(f"PPTX={FINAL_PPTX}")
    print(f"PREVIEW={PREVIEW_HTML}")
    print(f"SLIDES={len(slides)}")


if __name__ == "__main__":
    main()
