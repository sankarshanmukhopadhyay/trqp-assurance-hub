# Quickstart

This repository is the *integration surface* for running TRQP assurance as if it were one product.

## 1) Choose what you are validating

- **Protocol conformance** → use `trqp-conformance-suite`
- **Security/privacy posture** → use `TRQP-TSPP`
- **Production readiness** → run both and produce a **Combined Assurance Manifest**

## 2) Run the Combined Assurance Smoke workflow (recommended)

This repo includes a GitHub Actions workflow that:
- checks out the hub + both tools
- produces a **Combined Assurance Manifest** as an artifact

Go to: **Actions → combined-assurance-smoke → Run workflow**

Inputs you can set:
- `target`: base URL of your TRQP registry
- `conformance_profile`: e.g., `smoke`, `baseline`
- `tspp_assurance_level`: e.g., `AL1`, `AL2`
- refs for each tool (tag/branch/SHA)

## 3) Run full assurance locally (outline)

1. Run Conformance Suite against your target and capture its evidence bundle
2. Run TRQP‑TSPP against the same target and capture its evidence bundle
3. Generate a combined manifest linking both artifacts:

```bash
python tools/generate-manifest.py   --build-id "my-build-2026-02-21"   --target "https://registry.example.org"   --hub-commit "<commit-sha>"   --cs-version "0.4.0" --cs-profile-id "baseline" --cs-run-id "cts-001"   --tspp-version "v0.2" --tspp-assurance-level "AL1" --tspp-run-id "tspp-001"   --artifact "evidence_bundle:path/to/conformance-evidence.json:trqp_conformance_suite"   --artifact "evidence_bundle:path/to/tspp-evidence.json:trqp_tspp"   --out combined-assurance-manifest.json
```

## 4) Next: read the docs

- Combined assurance workflow: `docs/guides/combined-assurance.md`
- Compatibility policy + machine-readable index: `docs/policies/compatibility.md`, `docs/policies/compatibility.json`
- Glossary: `docs/glossary.md`
