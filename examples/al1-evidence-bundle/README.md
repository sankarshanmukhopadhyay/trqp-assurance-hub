---
layout: default
title: "AL1 minimal viable evidence bundle"
nav_exclude: true
---

# AL1 minimal viable evidence bundle

This folder shows the **minimum viable** artifact set for an AL1 assurance claim.

AL1 is defined in `docs/guides/assurance-levels.md`. At AL1, the operator MUST
be able to produce machine-readable evidence showing protocol conformance and
minimum deployment posture. Results must be attributable to a specific version
of the artifacts and runner.

## What to produce

| Artifact | Requirement | Notes |
|---|---|---|
| Conformance evidence bundle | Required | CTS baseline profile run |
| TSPP posture evidence bundle | Required | TSPP AL1 harness run |
| `version-tuple.json` | Recommended | Pin tool + profile versions |
| Combined Assurance Manifest | Recommended | Links the two bundles |

## What you can omit at AL1

At AL1 you do **not** need: a Control Satisfaction Declaration, a Lifecycle
Assertion, a Certification Attestation, an independent assessor, or continuous
monitoring artifacts. Those are AL2+ expectations.

If you omit a Recommended artifact, include a short rationale in
`operator-declaration.md` or the manifest `notes` field.

## How to generate this bundle using the toolchain

```bash
# 1. Run CTS baseline profile
python cts/run.py \
  --profile profiles/baseline.yaml \
  --sut sut.local.yaml \
  --generated-at "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --out evidence/conformance

# 2. Run TSPP AL1 harness
TSPP_EXPECT_AL=AL1 \
TSPP_REPORT_PATH=evidence/tspp-report.json \
pytest harness/tests

# 3. Generate Combined Assurance Manifest
python tools/generate-manifest.py \
  --build-id "$(git rev-parse --short HEAD)" \
  --target "https://registry.example.org" \
  --cts-report evidence/conformance/cts-report.json \
  --tspp-report evidence/tspp-report.json \
  --schema schemas/combined-assurance-manifest.schema.json \
  --out evidence/combined-assurance-manifest.json
```

## File contents

- `version-tuple.json` — version declarations for this bundle
- `combined-assurance-manifest.json` — links conformance + posture bundles
- `operator-declaration.md` — authority and scope statement (optional at AL1)

## Upgrading to AL2

To move to AL2, add: explicit version tags (not branch refs), evidence bundle
checksums, a Combined Assurance Manifest (now Required), and a CI run link.
See `examples/al2-evidence-bundle/`.
