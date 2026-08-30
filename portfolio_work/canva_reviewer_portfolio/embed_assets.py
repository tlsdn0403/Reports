from __future__ import annotations

import base64
import mimetypes
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
HTML = ROOT / "index.html"
OUT = ROOT / "index_embedded.html"


def to_data_uri(match: re.Match[str]) -> str:
    rel = match.group(1)
    path = ROOT / rel
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f'src="data:{mime};base64,{encoded}"'


def main() -> None:
    html = HTML.read_text(encoding="utf-8")
    embedded = re.sub(r'src="(assets/[^"]+)"', to_data_uri, html)
    OUT.write_text(embedded, encoding="utf-8")
    print(OUT)
    print(OUT.stat().st_size)


if __name__ == "__main__":
    main()
