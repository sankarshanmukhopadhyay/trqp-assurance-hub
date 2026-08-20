#!/usr/bin/env python3
"""Validate documentation inputs required by the GitHub Pages build."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PREFIXES = (".github/", "vendor/", "node_modules/", "external/")
errors = []
public_docs = []
catalog_required = []

for path in sorted(ROOT.rglob("*.md")):
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith(EXCLUDED_PREFIXES):
        continue
    public_docs.append(rel)
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{rel}: missing Jekyll front matter")
        front_matter = ""
    elif "\n---\n" not in text[4:]:
        errors.append(f"{rel}: unterminated Jekyll front matter")
        front_matter = ""
    else:
        front_matter = text.split("\n---\n", 1)[0]
    if not re.search(r"(?mi)^nav_exclude:\s*true\s*$", front_matter):
        catalog_required.append(rel)
    if text.count("```mermaid") > text.count("```") // 2:
        errors.append(f"{rel}: Mermaid fence appears unterminated")

catalog = ROOT / "documentation.md"
if not catalog.exists():
    errors.append("documentation.md: missing documentation catalogue")
else:
    catalog_text = catalog.read_text(encoding="utf-8")
    for rel in catalog_required:
        if rel in {"documentation.md", "index.md"}:
            continue
        if f"`/{rel}`" not in catalog_text:
            errors.append(f"documentation.md: missing catalogue entry for {rel}")

head = ROOT / "_includes" / "head_custom.html"
script = ROOT / "assets" / "js" / "mermaid-init.js"
if not head.exists() or "mermaid-init.js" not in head.read_text(encoding="utf-8"):
    errors.append("_includes/head_custom.html: Mermaid loader is missing")
if not script.exists() or "mermaid.run" not in script.read_text(encoding="utf-8"):
    errors.append("assets/js/mermaid-init.js: Mermaid renderer is missing")

if errors:
    print("Documentation site validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Documentation site validation passed for {len(public_docs)} Markdown files.")
