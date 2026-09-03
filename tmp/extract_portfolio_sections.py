from html.parser import HTMLParser
from pathlib import Path

FILES = [
    Path(r"C:\Users\tlsdn\Desktop\Reports\portfolio_work\canva_reference_portfolio_compact\index.html"),
    Path(r"C:\Users\tlsdn\Desktop\Reports\portfolio_work\new_portfolio\박신우_게임클라이언트_포트폴리오.html"),
]

class PortfolioParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pages = []
        self.section_depth = 0
        self.page = None
        self.capture_depth = 0
        self.capture_tag = None
        self.buffer = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if tag == "section" and "page" in classes:
            self.section_depth = 1
            self.page = {"label": attrs.get("data-label", ""), "items": [], "images": []}
            self.pages.append(self.page)
            return
        if self.section_depth:
            if tag == "section":
                self.section_depth += 1
            if tag == "img" and attrs.get("src"):
                self.page["images"].append((attrs["src"], attrs.get("alt", "")))
            capture_classes = {"metric", "scope-item", "evidence-item", "question-item", "step", "panel", "note"}
            if not self.capture_depth and (tag in {"h1", "h2", "h3", "p", "li", "a"} or capture_classes.intersection(classes)):
                self.capture_depth = 1
                self.capture_tag = tag
                self.buffer = []
                if tag == "a" and attrs.get("href"):
                    self.buffer.append(f"[LINK {attrs['href']}] ")
            elif self.capture_depth:
                self.capture_depth += 1

    def handle_endtag(self, tag):
        if self.capture_depth:
            self.capture_depth -= 1
            if self.capture_depth == 0:
                text = " ".join("".join(self.buffer).split())
                if text:
                    self.page["items"].append(text)
                self.capture_tag = None
                self.buffer = []
        if self.section_depth and tag == "section":
            self.section_depth -= 1
            if self.section_depth == 0:
                self.page = None

    def handle_data(self, data):
        if self.capture_depth:
            self.buffer.append(data)


for file in FILES:
    print(f"\n===== {file.name} =====")
    parser = PortfolioParser()
    parser.feed(file.read_text(encoding="utf-8"))
    for index, page in enumerate(parser.pages, start=1):
        print(f"\n--- PAGE {index}: {page['label']} ---")
        seen = set()
        for item in page["items"]:
            if item not in seen:
                print(item)
                seen.add(item)
        for src, alt in page["images"]:
            print(f"IMAGE: {src} | {alt}")
