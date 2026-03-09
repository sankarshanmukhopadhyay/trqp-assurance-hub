#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'al-contract.json').read_text(encoding='utf-8'))
pinned = contract['canonical_source']['canonical_doc_sha256']
snapshot = ROOT / 'docs' / 'assurance-levels.canonical.md'
actual = hashlib.sha256(snapshot.read_bytes()).hexdigest()
if actual != pinned:
    raise SystemExit(f'AL contract verification failed: expected {pinned}, got {actual}')
print('AL contract verification passed.')
