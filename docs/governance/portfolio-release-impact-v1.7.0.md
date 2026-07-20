---
layout: default
title: "Portfolio Release Impact: TRQP Assurance Hub v1.7.0"
nav_exclude: true
---

# Portfolio Release Impact: TRQP Assurance Hub v1.7.0

| Field | Value |
|---|---|
| Repository | `trqp-assurance-hub` |
| Release version | v1.7.0 |
| Release date | 2026-06-29 |
| Primary change type | Assurance + artifact contract alignment |
| Portfolio impact classification | Artifact / Assurance / Documentation |

## Changed surfaces

- [x] Terminology or conceptual model
- [x] Schema or runtime artifact
- [x] Evidence bundle or decision receipt
- [x] Conformance verdict or test fixture
- [x] Assurance level or control mapping
- [x] Registry publication or status/revocation semantics
- [x] README, onboarding, or adoption workflow

## Relationship review

| Source repo | Target repo | Relationship | Impact | Evidence |
|---|---|---|---|---|
| `trust-systems-meta-model` | `trqp-assurance-hub` | `informs` | Hub CAM now carries optional TSMM semantic mapping | `schemas/combined-assurance-manifest.schema.json`, `docs/reference/tsmm-tis-runtime-assurance-contract.md` |
| `trust-infrastructure-schemas` | `trqp-assurance-hub` | `informs` | Hub CAM now references TIS artifact contracts | `tis_artifacts` block in CAM schema and example |
| `trqp-conformance-suite` | `trqp-assurance-hub` | `produces_evidence_for` | CTS v1.4.0 evidence can be referenced as TIS-compatible conformance evidence | compatibility matrix and runtime contract |
| `TRQP-TSPP` | `trqp-assurance-hub` | `profiles` | TSPP v0.12.0 posture evidence can be referenced as TIS-compatible assurance evidence | compatibility matrix and runtime contract |

## Downstream review requirements

| Downstream repo | Required review | Owner | Status |
|---|---|---|---|
| `trqp-conformance-suite` | Add TIS evidence contract references and version pin to Hub v1.7.0 | maintainers | complete in coordinated release |
| `TRQP-TSPP` | Add TIS posture evidence contract references and version pin to Hub v1.7.0 | maintainers | complete in coordinated release |

## Validation evidence

```text
python tools/validate_examples.py
python scripts/doc_tests.py
python tools/validate_operational_stack.py --bundle-dir artifacts/operational-stack
```

## Release note language

Hub v1.7.0 introduces the TSMM/TIS Runtime Assurance Contract Pack. The release adds optional TSMM semantic mapping and TIS artifact references to Combined Assurance Manifests, refreshes compatibility metadata for CTS v1.4.0 and TSPP v0.12.0, and publishes governance records for portfolio drift review.

## Decision

- [ ] Release has no cross-repo impact.
- [ ] Release has documentation impact only.
- [x] Release requires downstream artifact/profile/test updates.
- [ ] Release should be held until downstream compatibility is updated.

