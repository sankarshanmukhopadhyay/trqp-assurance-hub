#!/usr/bin/env python3
from pathlib import Path
import json,yaml
from jsonschema import Draft202012Validator
r=Path(__file__).resolve().parents[1]; d=yaml.safe_load((r/'data/compatibility-registry.yaml').read_text()); s=json.loads((r/'schemas/compatibility-registry.schema.json').read_text()); errs=list(Draft202012Validator(s).iter_errors(d));
if errs:
 [print(e.message) for e in errs]; raise SystemExit(1)
print('compatibility registry: valid')
