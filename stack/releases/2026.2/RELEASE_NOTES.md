---
layout: default
title: "TRQP Stack 2026.2 — Ashoka release notes"
nav_exclude: true
---

# TRQP Stack 2026.2 — Ashoka

TRQP Stack 2026.2 — **Ashoka** (*Saraca asoca*) is the coordinated lifecycle-assurance release of the TRQP Operational Trust Stack.

A coordinated Stack release is a **compatibility and assurance contract**, not a fourth implementation product and not external certification. This release identifies the exact independently governed component tuple that has been exercised together and preserves the evidence supporting that bounded assurance claim.

## Validated release tuple

| Layer | Release | Role |
|---|---:|---|
| TRQP-TSPP | v0.16.1 | Security/privacy posture materiality and affected-control evidence |
| TRQP Conformance Suite | v1.9.1 | Conformance/replay consequence and reassessment planning |
| TRQP Assurance Hub | v1.12.0 | Current-assurance recomposition, supersession, and release coordination |
| TSMM | v0.24.0 | Canonical semantic authority |
| TIS | v0.15.0 | Portable lifecycle-contract authority |

## What changes in 2026.2

Stack 2026.2 closes the assurance change lifecycle end to end. A portable lifecycle event can now travel from a component-local change judgment through reassessment into a recomposed Stack assurance decision without losing authority, provenance, or fail-safe behavior.

The executable lifecycle covers:

- material change that makes prior assurance non-current;
- legitimate non-material change that may preserve current assurance when bounded by evidence;
- unknown impact that fails safe and broadens reassessment;
- explicit security/privacy materiality and affected-control evidence;
- bounded versus full conformance/replay reassessment;
- authority drift that cannot silently inherit compatibility;
- immutable historical assurance outcomes separated from current reliance validity; and
- completed reassessment establishing a successor only through explicit supersession lineage.

## Release assurance

The final `stack-release-eligibility` replay ran on merged `main` at `9731811874e1f9f3e08e8745449e406950f2209e` and completed successfully as workflow run `33296416272`.

The preserved evidence artifact is `trqp-stack-release-candidate-33296416272` with digest:

`sha256:7cb1bc51fb8d3b09a32acceed9be8cea2f9e817c4b64e78c24df30267ab7a463`

The decisive run proved immutable tag/commit resolution, clean-room bootstrap, tagged component assurance execution, correlated TSPP and CTS evidence, deterministic CTS replay, combined-assurance recomposition, whole-Stack semantic replay equivalence, fail-closed negative cases, lifecycle boundary validation, authority-drift detection, bounded reassessment, and supersession lineage.

The clean adopter walkthrough was independently exercised before the final merged-main replay. The release was not authorized merely because workflows were green: an explicit human release judgment was recorded on governing Hub issue #42 before this publication record was created.

## Clean-room defect discovery

The release process itself exposed a useful assurance boundary. Initial TSPP v0.16.0 and CTS v1.9.0 tags passed their component release CI but failed their tagged clean-room `assurance-check` because their README status contracts omitted required governance markers. Those immutable tags were preserved rather than moved. Narrow patch releases v0.16.1 and v1.9.1 repaired the repository-status contract, passed their own CI/Pages/portfolio gates, and then passed the Stack clean-room execution.

This is intentional evidence that component workflow success is not treated as equivalent to Stack assurance success.

## Authority boundaries

The coordinated release does not transfer authority:

- TSMM retains canonical semantic authority;
- TIS retains portable lifecycle schema/contract authority;
- TSPP retains security/privacy posture materiality and affected-control authority;
- CTS retains conformance/replay reassessment authority; and
- the Assurance Hub retains combined current-assurance recomposition, supersession, compatibility-tuple declaration, and coordinated release judgment.

Downstream pressure that requires a semantic or contract change must still be escalated to the layer that owns that authority.

## Fail-safe and revocation behavior

The validated lifecycle does not allow material or unknown change to silently preserve CURRENT assurance. Missing or mismatched lifecycle evidence, run/target mismatch, missing provenance, integrity failure, unsupported authority drift, and incomplete supersession evidence fail closed under the declared gates.

Any later movement in a component version, authority baseline, evidence set, or lifecycle state invalidates reliance on this exact coordinated release where the documented invalidation rules apply and requires fresh evaluation rather than historical-result mutation.

## Assurance scope

TRQP Stack 2026.2 — Ashoka is a reproducible **project assurance and compatibility statement** for the exact tuple above. It is not independent external certification.

The stable machine identity is `trqp-stack-2026.2`. The codename is human-facing identity selected from the established Indian state-tree naming set.
