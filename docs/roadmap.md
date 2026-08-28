---
layout: default
title: "Roadmap"
nav_exclude: true
owner: maintainers
last_reviewed: 2026-08-28
---

# TRQP Stack Roadmap

This roadmap is the coordinated delivery view for the TRQP Operational Trust Stack. Component repositories retain independent authority and semantic versioning; the Hub coordinates compatibility, integration evidence, and Stack release eligibility.

## Current baseline

**TRQP Stack 2026.1 — Coconut** established an immutable, reproducible coordinated tuple with clean bootstrap, deterministic CTS replay, combined assurance, provenance/integrity checks, fail-closed negative cases, semantic replay equivalence, and an executable adopter walkthrough.

## Target: TRQP Stack 2026.2 — assurance validity under change

**Target publication:** 30 September 2026, subject to capability and evidence readiness.

**Governing issue:** https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/issues/39

### Governing proposition

> A previously valid TRQP assurance conclusion MUST NOT silently survive a material change to its target, evidence, authority, policy, semantic dependency, schema dependency, or component compatibility conditions.

Stack 2026.2 advances the coordinated contract from point-in-time reproducibility to an explicit assurance lifecycle: detect material change, determine impact, invalidate or reassess affected evidence, preserve legitimate non-material reuse, fail safe when impact is unknown, and publish immutable supersession lineage.

## Coordinated workstreams

| Workstream | Repository | Tracking | Intended evidence |
|---|---|---|---|
| Posture evidence validity | TRQP-TSPP | [#69](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP/issues/69) | machine-readable reuse/reassessment decision |
| Bounded conformance reassessment | TRQP Conformance Suite | [#32](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite/issues/32) | impact report, reassessment plan/result |
| Assurance lifecycle composition | TRQP Assurance Hub | [#40](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/issues/40) | validity state, reassessment and supersession lineage |
| Portable lifecycle contracts | Trust Infrastructure Schemas | [Hub #41](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/issues/41) | portable change/invalidation/reassessment contracts where needed |
| Semantic sufficiency | Trust Systems Meta-Model | [#3](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/issues/3) | explicit decision whether existing semantics suffice |
| Coordinated pressure/release test | TRQP Assurance Hub | [#42](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/issues/42) | whole-Stack falsification and eligibility evidence |

## Candidate tuple

The tuple is deliberately provisional. A component is released only when a material capability change warrants it.

| Layer | Candidate |
|---|---|
| TRQP-TSPP | `v0.16.0` if material invalidation capability lands |
| TRQP Conformance Suite | `v1.9.0` if bounded reassessment capability lands |
| TRQP Assurance Hub | `v1.12.0` if assurance lifecycle composition lands |
| TSMM | retain `v0.24.0` unless new canonical semantics are demonstrably required |
| TIS | `v0.15.0` only if new portable lifecycle contracts are required |

## Delivery sequence

| Date | Milestone |
|---|---|
| 28 Aug–6 Sep | Canonical change/invalidation model and roadmap alignment |
| 4–11 Sep | TSPP posture-evidence invalidation |
| 7–14 Sep | CTS impact-aware reassessment |
| 11–18 Sep | Hub assurance lifecycle composition |
| 14–20 Sep | Authority/schema compatibility and drift handling |
| 18–23 Sep | Freshness and supersession lineage |
| 20–25 Sep | Coordinated adversarial pressure tests |
| 22–26 Sep | Executable adopter change/reassessment walkthrough |
| 26 Sep | Release-candidate tuple freeze |
| 27–28 Sep | Full coordinated eligibility replay |
| 29 Sep | Explicit human release judgment |
| 30 Sep | Publish only if evidence supports the proposition |

## Additional Stack 2026.2 gates

All Stack 2026.1 gates remain mandatory. Add:

- `change-event-valid`
- `material-change-detected`
- `non-material-change-bounded`
- `stale-assurance-not-reused`
- `authority-drift-detected`
- `unknown-impact-fails-safe`
- `reassessment-plan-valid`
- `bounded-reassessment-valid`
- `supersession-lineage-complete`
- `post-change-assurance-recomposed`

## Required pressure tests

The release candidate must prove both invalidation and legitimate continuity:

- old evidence reused after a material component/target change → reject;
- provenance or integrity discontinuity → reject;
- authority drift without applicable compatibility evidence → non-current/reassessment, not silent PASS;
- CTS comparison-policy change → replay/reassessment required;
- TSPP posture/target change → old posture evidence non-current;
- documentation-only/non-material change → reuse permitted when justified;
- semantically equivalent volatile output change → semantic conclusion may remain reusable;
- unknown impact → broader reassessment/full rerun;
- unsupported partial reassessment → reject.

## Release judgment

Before publication, the release PR must preserve what was tested, assumptions and counter-cases, falsification evidence, rejected alternatives, residual uncertainty, and the explicit human decision to accept the final tuple. A green workflow is necessary but is not itself the release judgment.

## Machine-readable plan

The synchronized candidate plan is published at [`stack/candidates/2026.2/roadmap.yaml`](../stack/candidates/2026.2/roadmap.yaml). It is an input to implementation and release eligibility, not an immutable release manifest.
