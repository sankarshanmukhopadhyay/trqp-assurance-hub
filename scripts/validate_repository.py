#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
required=["README.md","LICENSE","CHANGELOG.md","ROADMAP.md","GOVERNANCE.md","CONTRIBUTING.md","SECURITY.md","CODE_OF_CONDUCT.md","CITATION.cff","QUICKSTART.md","data/repository-metadata.yaml","docs/trqp-adoption-path.md"]
errors=[]
for rel in required:
    if not (root/rel).is_file(): errors.append(f"missing required flagship artifact: {rel}")
readme=(root/'README.md').read_text(encoding='utf-8')
for marker in ['Portfolio tier','Validation','Evidence output','Governance authority']:
    if marker not in readme: errors.append(f"README missing status contract marker: {marker}")
for md in root.rglob('*.md'):
    text=md.read_text(encoding='utf-8',errors='replace')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        t=target.split('#',1)[0].strip()
        if not t or '://' in t or t.startswith(('mailto:','data:','#')): continue
        dest=(md.parent/t).resolve()
        try: dest.relative_to(root.resolve())
        except ValueError: continue
        if not dest.exists(): errors.append(f"broken local link: {md.relative_to(root)} -> {target}")
if errors:
    print('Flagship repository validation failed:')
    for e in sorted(set(errors)): print(f'- {e}')
    sys.exit(1)
print('Flagship repository contract: PASS')
