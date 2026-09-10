---
layout: default
title: "Adoption Kit"
nav_exclude: true
---

# Adoption Kit

The adoption kit helps institutional users convert TRQP assurance artifacts into onboarding, procurement, and audit decisions.

## Start with the coordinated stack

For an end-to-end adopter path across TRQP-TSPP, the TRQP Conformance Suite and the TRQP Assurance Hub, use the [TRQP Stack quickstart](stack-quickstart.md).

The coordinated Stack path verifies immutable tags and commits, bootstraps a clean workspace, executes the declared component assurance surfaces, and retains the evidence required before a coordinated release may be published. Component repositories retain their own authority over TSPP posture judgments, CTS conformance/replay consequences, and Hub recomposition.

## TRQP Stack 2026.3 — Banyan current release

TRQP Stack 2026.3 — Banyan is the current published coordinated release. It adds **profile-aware compositional assurance** to the Stack and proves that profile conclusions can consume independently produced CTS core-conformance evidence and TSPP posture evidence without transferring producer authority or allowing profile-local success to override producer failure, uncertainty, stale evidence, missing evidence, or other non-current evidence.

Published tuple:

- TSPP `v0.17.0` → `328e19c71f407ebdb2bc92828a3ae037a843f285`;
- CTS `v1.10.0` → `1e5dc2646c75390444d9ae86f3d6136d7c033463`;
- Assurance Hub `v1.13.0` → `5346b83545bf042360eb32691dfc907135d233dd`;
- QBF TSMM `0.24.0` → `8ddfd52c876faf368241bc11101681fb1fe49398`; and
- QBF TIS `0.15.0` → `edda0e87ced40797d22e3df542099871c57fcb59`.

Use the [Stack 2026.3 profile-aware assurance walkthrough](stack-2026.3-walkthrough.md) for the execution path, evidence inventory, negative cases, and authority boundaries. The immutable publication record is under `stack/releases/2026.3/` and the GitHub release is tagged `trqp-stack-2026.3`.

Publication completed only after the frozen tuple passed the decisive Stack eligibility workflow, its evidence artifact and digest were recorded, the required visible human release judgment accepted publication, and a fresh merged-main eligibility run succeeded.

## TRQP Stack 2026.2 — Ashoka historical baseline

Stack 2026.2 — Ashoka is the immediately preceding coordinated release. Its frozen tuple is:

- TSPP `v0.16.1` → `12315679dd79bcaced5f27a35bfc1d22560de52d`;
- CTS `v1.9.1` → `ea3fed33a1edc3313735405f433a23f9d154d903`;
- Assurance Hub `v1.12.0` → `7f7aae84eb41ffd8ea672dae00955c5714ffd3de`;
- TSMM `v0.24.0`; and
- TIS `v0.15.0` → `edda0e87ced40797d22e3df542099871c57fcb59`.

The TSPP and CTS patch releases in that historical tuple repaired repository-status-contract defects discovered by clean-room Stack execution; they did not alter the lifecycle/reassessment semantics established in v0.16.0/v1.9.0.

Those lifecycle guarantees remain inherited by 2026.3: invalidation, reassessment, authority drift, supersession, and post-change recomposition continue to be part of the current release gate.

Use the component repositories directly when you need to customize TSPP posture controls, CTS conformance/replay behavior, or Hub assurance composition. The coordinated stack does not transfer those repository-local authorities.
