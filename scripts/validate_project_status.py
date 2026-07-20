#!/usr/bin/env python3
from pathlib import Path
import json, yaml
from jsonschema import Draft202012Validator
root=Path(__file__).resolve().parents[1]
doc=yaml.safe_load((root/'PROJECT-STATUS.yaml').read_text())
schema=json.loads((root/'schemas/project-status.schema.json').read_text())
errors=sorted(Draft202012Validator(schema).iter_errors(doc), key=lambda e:list(e.path))
if errors:
    for e in errors: print(f"PROJECT-STATUS.yaml:{'/'.join(map(str,e.path))}: {e.message}")
    raise SystemExit(1)
print('PROJECT-STATUS.yaml: valid')
