---
layout: default
title: "AL2 minimal viable evidence bundle"
nav_exclude: true
---

# AL2 minimal viable evidence bundle

This folder shows the **minimum viable** artifact set for an AL2 assurance claim.

AL2 is defined in `docs/guides/assurance-levels.md`. At AL2, the operator MUST
bind claims to evidence in a way that reduces provenance ambiguity. A Combined
Assurance Manifest SHOULD be produced, version declarations SHOULD use explicit
tags, and integrity signals (checksums) SHOULD be present.

## What to produce

| Artifact | Requirement | Notes |
|---|---|---|
| Conformance evidence bundle | Required | CTS baseline profile run |
| TSPP posture evidence bundle | Required | TSPP AL2 harness run |
| Combined Assurance Manifest | Required | Must link both bundles; include `run_id` |
| `version-tuple.json` | Required | Prefer tagged releases; else `main@<sha>` |
| Evidence bundle checksums | Recommended | SHA-256 over key artifact files |
| CI run link / provenance | Recommended | CI URL or SLSA provenance attestation |
| Operator declaration | Optional | Recommended for external-facing registries |

## What you can omit at AL2

At AL2 you do **not** need: an independent assessor, a Lifecycle Assertion, a
Control Satisfaction Declaration, or a Certification Attestation. Those are
AL3+ expectations.

## How to generate this bundle

```bash
# 1. Run CTS baseline with pinned timestamp + run ID
python cts/run.py \
  --profile profiles/baseline.yaml \
  --sut sut.local.yaml \
  --generated-at "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --run-id "run-$(git rev-parse --short HEAD)" \
  --out evidence/conformance

# 2. Run TSPP AL2 harness
TSPP_EXPECT_AL=AL2 \
TSPP_RUN_ID="run-$(git rev-parse --short HEAD)" \
TSPP_REPORT_PATH=evidence/tspp-report.json \
pytest harness/tests

# 3. Generate Combined Assurance Manifest with checksums
python tools/generate-manifest.py \
  --build-id "$(git rev-parse HEAD)" \
  --target "https://registry.example.org" \
  --run-id "run-$(git rev-parse --short HEAD)" \
  --cts-report evidence/conformance/cts-report.json \
  --tspp-report evidence/tspp-report.json \
  --artifact "evidence_checksums:evidence/conformance/checksums.json:trqp_conformance_suite:application/json" \
  --ci-run-url "${CI_RUN_URL:-}" \
  --schema schemas/combined-assurance-manifest.schema.json \
  --out evidence/combined-assurance-manifest.json
```

## File contents

- `version-tuple.json` — version declarations (all tagged releases)
- `combined-assurance-manifest.json` — links conformance + posture bundles with `run_id`
- `operator-declaration.md` — authority, scope, and omission rationale

## Upgrading to AL3

To move to AL3, add: a Control Satisfaction Declaration, a Lifecycle Assertion,
evidence bundle checksums (now Required), an independent assessor record in a
Certification Attestation, and remediation closure records for any detected
nonconformities. See `examples/al3-evidence-bundle/`.
