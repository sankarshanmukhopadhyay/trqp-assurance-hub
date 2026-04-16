# Operational Stack example

This example shows the minimum artifact set required for the Operational Stack baseline.

## Layout

- `demo-input/cts-report.json` — sample CTS machine-readable report used as source input
- `demo-input/tspp-report.json` — sample TSPP posture report used as source input
- `expected-output/combined-assurance-manifest.json` — deterministic reference manifest for the demo input pair
- `../../artifacts/operational-stack/` — checked-in reproducible bundle validated in CI
- `../../profiles/al2-verified.yaml` — example machine-readable assurance profile for publication

## Contract

For the Operational Stack baseline, CTS and TSPP MUST agree on `run_id` and `target_id`.
The Hub manifest generator and bundle validator reject mismatched evidence instead of publishing it.

## Validation

```bash
python tools/run_operational_stack.py \
  --cts-report examples/operational-stack/demo-input/cts-report.json \
  --tspp-report examples/operational-stack/demo-input/tspp-report.json \
  --target https://directory.example.org \
  --build-id opstack-demo-001 \
  --target-id demo-directory \
  --run-id opstack-demo-001 \
  --assurance-profile profiles/al2-verified.yaml \
  --out artifacts/operational-stack

python tools/validate_operational_stack.py --bundle-dir artifacts/operational-stack
```

These files are intentionally small. The point is to make the integrated shape obvious without weakening the evidence contract.
