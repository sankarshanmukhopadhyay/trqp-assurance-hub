#!/usr/bin/env python3
"""Validate that rendered GitHub Pages internal links resolve inside _site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import posixpath
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
CONFIG = (ROOT / "_config.yml").read_text(encoding="utf-8")
match = re.search(r'(?m)^baseurl:\s*["\']?([^"\'\n]*)', CONFIG)
BASEURL = (match.group(1).strip() if match else "").rstrip("/")

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if tag.lower() not in {"a", "link"}:
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.hrefs.append(value)

def resolve_target(page: Path, href: str):
    href = href.strip()
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if not path:
        return None

    if BASEURL and path == BASEURL:
        path = "/"
    elif BASEURL and path.startswith(BASEURL + "/"):
        path = path[len(BASEURL):]

    if path.startswith("/"):
        rel = path.lstrip("/")
    else:
        page_rel = page.relative_to(SITE).as_posix()
        page_dir = posixpath.dirname(page_rel)
        rel = posixpath.normpath(posixpath.join(page_dir, path))

    rel = rel.lstrip("./")
    if rel in {"", "."}:
        return SITE / "index.html"

    target = SITE / rel
    candidates = [target]
    if path.endswith("/"):
        candidates.insert(0, target / "index.html")
    elif not target.suffix:
        candidates.extend([target / "index.html", SITE / f"{rel}.html"])

    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]

if not SITE.exists():
    print("Rendered-site validation failed: _site does not exist.")
    sys.exit(1)

errors = []
html_files = sorted(SITE.rglob("*.html"))

for page in html_files:
    parser = LinkParser()
    try:
        parser.feed(page.read_text(encoding="utf-8"))
    except UnicodeDecodeError:
        continue
    for href in parser.hrefs:
        target = resolve_target(page, href)
        if target is None:
            continue
        if not target.exists():
            rel_page = page.relative_to(SITE).as_posix()
            rel_target = target.relative_to(SITE).as_posix()
            errors.append(f"{rel_page}: {href} -> missing {rel_target}")

if errors:
    print("Rendered-site internal-link validation failed:")
    for error in sorted(set(errors)):
        print(f"- {error}")
    sys.exit(1)

print(f"Rendered-site internal-link validation passed for {len(html_files)} HTML pages.")
