---
layout: default
title: "Roadmap"
nav_exclude: true
owner: maintainers
last_reviewed: 2026-08-28
tier: 0
---

# TRQP Stack Roadmap

This roadmap is the coordinated planning input for the next TRQP Operational Trust Stack release. It complements the permanent release rules in `docs/governance/release-policy.md` and the immutable TRQP Stack 2026.1 release record under `stack/releases/2026.1/`.

The target is **TRQP Stack 2026.2 by 30 September 2026**, but release remains capability-driven. The date is a planning target, not authority to publish an under-evidenced tuple.

## 2026.1 baseline

TRQP Stack 2026.1 — Coconut established a reproducible coordinated assurance contract across:

- TRQP-TSPP v0.15.0;
- TRQP Conformance Suite v1.8.0;
- TRQP Assurance Hub v1.11.0;
- TSMM v0.24.0; and
- TIS v0.14.1.

Its decisive gates include immutable tuple resolution, clean bootstrap, producer-evidence validation, deterministic CTS replay, combined assurance, provenance and integrity checks, fail-closed negative cases, whole-stack semantic replay equivalence, and an executable adopter walkthrough.

## TRQP Stack 2026.2 governing proposition

> A previously valid TRQP assurance conclusion MUST NOT silently survive a material change to its target, evidence, authority, policy, semantic dependency, schema dependency, or component compatibility conditions.

2026.1 answers whether an exact Stack tuple can be reproduced and inspected. 2026.2 should answer whether the Stack can detect when the basis for relying on that assurance has materially changed, invalidate or downgrade the previous conclusion, bound the required reassessment, and produce evidence explaining the resulting decision.

## Intended release capability

The coordinated lifecycle is:

```text
known-good Stack state
        ↓
change observed
        ↓
change impact classified
        ↓
prior assurance validity evaluated
        ↓
CURRENT / STALE / INVALIDATED / REASSESSMENT_REQUIRED / INDETERMINATE
        ↓
bounded or full reassessment
        ↓
new combined assurance decision
        ↓
supersession and traceability evidence
```

A legitimate non-material change must be distinguishable from a material change. Unknown impact must fail toward broader reassessment rather than silent reuse.

## Authority boundaries

The release does not collapse repository authority:

- **TSPP** owns security/privacy posture semantics and whether its evidence remains reusable after a relevant change.
- **CTS** owns conformance, replay-comparison semantics, and any bounded conformance reassessment determination.
- **Assurance Hub** owns combined assurance validity, compatibility coordination, reassessment composition, supersession lineage, and Stack release eligibility.
- **TSMM** remains canonical semantic authority and changes only if the lifecycle requires genuinely new canonical semantics.
- **TIS** owns portable machine-readable contracts required to exchange change, invalidation, reassessment, or supersession evidence.

Component releases remain independently versioned. No component is bumped merely to make the coordinated tuple appear synchronized.

## Coordinated workstreams

### A. Canonical change and invalidation contract — target 1–6 September

Define the minimum machine-operable representation of a change that may affect assurance. Candidate dimensions include target implementation, configuration, policy, CTS comparison policy, TSPP control/posture input, evidence freshness, producer version, schema authority, semantic authority, dependency, integrity, and authority/delegation changes.

**Invariant:** no material change to an assurance dependency may leave the prior assurance decision silently current.

**Required counter-case:** a proven non-material change must not force reassessment merely because bytes changed.

### B. TSPP evidence invalidation — target 4–11 September

TSPP should determine whether previous posture evidence is unchanged/reusable, requires reassessment, or is invalid after relevant change.

Pressure cases should include weakened security configuration, removed required controls, changed provenance, changed target identity, evidence expiry, and deployment-profile change. Documentation-only or other proven non-material change must remain a legitimate counter-case.

### C. CTS bounded reassessment — target 7–14 September

Extend deterministic replay toward impact-aware reassessment. CTS should be able to identify affected tests, reusable tests, and whether a full rerun is required when this can be established safely.

**Fail-safe rule:** unknown impact requires broader/full reassessment; absence of impact evidence must never justify a narrower rerun.

Candidate evidence outputs include `change-impact-report.json`, `reassessment-plan.json`, and `reassessment-result.json`.

### D. Hub assurance lifecycle — target 11–18 September

The Hub should consume the previous assurance decision, change evidence, TSPP impact, CTS impact, and authority/schema/semantic compatibility state and emit explicit lifecycle validity independently of the original PASS/FAIL outcome.

Candidate lifecycle states:

- `CURRENT`;
- `STALE`;
- `INVALIDATED`;
- `REASSESSMENT_REQUIRED`;
- `INDETERMINATE`; and
- `SUPERSEDED`.

Candidate evidence includes assurance-validity, change-impact, reassessment-plan, and supersession records bound into combined assurance.

### E. Authority drift — target 14–20 September

Version drift in TSMM, TIS, CTS policy, or TSPP control vocabulary must not automatically imply either compatibility or incompatibility. Continued reliance requires applicable compatibility evidence.

**Invariant:** authority-version drift without an applicable compatibility assertion invalidates silent continued reliance on the previous coordinated assurance tuple.

### F. Freshness and supersession — target 18–23 September

Historical assurance evidence remains immutable. New evidence links to prior evidence through explicit supersession lineage rather than rewriting old conclusions.

The lineage must identify the superseded assurance object, successor where known, reason, and triggering change event.

### G. Adversarial pressure testing — target 20–25 September

The coordinated suite must exercise at least:

| Pressure case | Expected disposition |
|---|---|
| Component changes but old evidence is reused | Reject |
| Evidence content changes while claimed identity/integrity is stale | Reject |
| TSMM changes without compatibility evidence | Reassess / indeterminate |
| TIS changes incompatibly | Reject |
| CTS comparison policy changes | Replay/reassessment required |
| TSPP target identity changes | Prior posture evidence invalid |
| Proven cosmetic/non-material change | No unnecessary reassessment |
| Semantically equivalent volatile output change | Reuse may remain valid under policy |
| Impact cannot be determined | Broader reassessment |
| Producer authority changes | Prior evidence stale/invalid |
| Partial rerun lacks impact evidence | Reject |

### H. Executable adopter workflow — target 22–26 September

Extend the clean adopter walkthrough to demonstrate:

1. establish known-good assurance;
2. introduce a non-material change and prove bounded continued validity;
3. introduce a material change and observe reassessment requirement;
4. execute the required reassessment; and
5. obtain a new combined decision with inspectable lineage.

## Candidate component releases

These are planning hypotheses, not mandatory version bumps:

| Component | Candidate | Required reason to release |
|---|---:|---|
| TRQP-TSPP | v0.16.0 | material-change invalidation capability |
| TRQP Conformance Suite | v1.9.0 | impact-aware/bounded reassessment capability |
| TRQP Assurance Hub | v1.12.0 | assurance validity, reassessment, and supersession lifecycle |
| TIS | v0.15.0 | portable lifecycle/change evidence contracts if required |
| TSMM | v0.25.0 only if required | genuinely new canonical lifecycle semantics |

If existing TSMM or TIS authority surfaces are sufficient, the existing release MUST remain pinned rather than being bumped for symmetry.

## Release gates

TRQP Stack 2026.2 inherits every 2026.1 gate and adds, subject to implementation naming:

- `change-event-valid`;
- `material-change-detected`;
- `non-material-change-bounded`;
- `stale-assurance-not-reused`;
- `authority-drift-detected`;
- `unknown-impact-fails-safe`;
- `reassessment-plan-valid`;
- `bounded-reassessment-valid`;
- `supersession-lineage-complete`; and
- `post-change-assurance-recomposed`.

## Release schedule

| Date | Milestone | Evidence expected |
|---|---|---|
| 28–31 Aug | roadmap and governing proposition | synchronized roadmap inputs |
| 1–6 Sep | change/invalidation contract | semantics/contracts + fixtures |
| 4–11 Sep | TSPP invalidation | producer evidence + pressure tests |
| 7–14 Sep | CTS reassessment | impact/reassessment evidence |
| 11–18 Sep | Hub lifecycle | lifecycle decisions + manifests |
| 14–20 Sep | authority drift | compatibility/invalidation evidence |
| 18–23 Sep | freshness/supersession | immutable lineage artifacts |
| 20–25 Sep | adversarial suite | falsification and counter-case evidence |
| 22–26 Sep | adopter workflow | executable lifecycle walkthrough |
| 26 Sep | candidate freeze | exact proposed tuple |
| 27–28 Sep | coordinated replay | release-candidate evidence |
| 29 Sep | release judgment | explicit acceptance/residual uncertainty record |
| 30 Sep | target release | immutable `trqp-stack-2026.2` record |

## Visible release judgment

The release PR must preserve the consequential judgment trail. At minimum it should record:

- the proposition accepted or rejected;
- important assumptions and acceptance criteria;
- pressure tests and legitimate counter-cases;
- evidence capable of falsifying the proposition;
- changed or rejected approaches where they actually occurred;
- residual uncertainty and deliberately deferred work; and
- the human decision to publish or defer the coordinated release.

A green workflow is necessary but is not, by itself, the release judgment.

## Release decision question

Before publication, maintainers must answer:

> Does TRQP Stack 2026.2 provide credible, machine-verifiable evidence that assurance conclusions remain bounded to the conditions under which they were established?

If that proposition cannot be supported by the release evidence, the September target must slip rather than weaken the coordinated-release contract.
