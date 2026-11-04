#!/usr/bin/env python3
"""Check local HTML references and required static-site assets."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked = 0
required = [
    ROOT / "index.html",
    ROOT / "404.html",
    ROOT / "download.html",
    ROOT / "support.html",
    ROOT / "advanced.html",
    ROOT / "assets" / "favicon.svg",
    ROOT / "assets" / "site.css",
    ROOT / "assets" / "demo" / "demo.gif",
]
for path in required:
    if not path.exists():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")

for page in ROOT.rglob("*.html"):
    text = page.read_text(encoding="utf-8")
    for target in re.findall(r'(?:href|src)="([^"]+)"', text):
        if target.startswith(("http://", "https://", "#", "mailto:", "data:")):
            continue
        target = target.split("?", 1)[0]
        candidate = (page.parent / target).resolve()
        checked += 1
        if not candidate.exists():
            errors.append(f"{page.relative_to(ROOT)} -> {target}")

if errors:
    print("SITE CHECK FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print(f"SITE CHECK OK: {checked} local references across {len(list(ROOT.rglob('*.html')))} HTML pages")
