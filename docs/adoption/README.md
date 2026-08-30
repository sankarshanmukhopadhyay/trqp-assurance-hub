---
layout: default
title: "Adoption Kit"
nav_exclude: true
---

# Adoption Kit

The adoption kit helps institutional users convert TRQP assurance artifacts into onboarding, procurement, and audit decisions.

## Start with the coordinated stack

For an end-to-end adopter path across TRQP-TSPP, the TRQP Conformance Suite and the TRQP Assurance Hub, use the [TRQP Stack quickstart](stack-quickstart.md).

The coordinated Stack path verifies immutable tags and commits, bootstraps a clean workspace, executes the declared component assurance surfaces, and retains the evidence required before a coordinated release may be cut. Component repositories retain their own authority over TSPP posture judgments, CTS conformance/replay consequences, and Hub recomposition.

## TRQP Stack 2026.2 clean-room walkthrough

The frozen 2026.2 candidate is:

- TSPP `v0.16.1` → `12315679dd79bcaced5f27a35bfc1d22560de52d`;
- CTS `v1.9.1` → `ea3fed33a1edc3313735405f433a23f9d154d903`;
- Assurance Hub `v1.12.0` → `7f7aae84eb41ffd8ea672dae00955c5714ffd3de`;
- TSMM `v0.24.0`; and
- TIS `v0.15.0` → `edda0e87ced40797d22e3df542099871c57fcb59`.

The TSPP and CTS patch releases repair repository-status-contract defects discovered by clean-room Stack execution; they do not alter the lifecycle/reassessment semantics established in v0.16.0/v1.9.0.

From a clean Hub checkout, run:

```bash
make stack-release-check
python tools/stack_bootstrap.py --clean
python tools/stack_evaluate.py
python scripts/validate_lifecycle_recomposition.py
python scripts/validate_authority_drift_and_supersession.py
python tools/stack_2026_2_lifecycle_eligibility.py
```

The complete `.github/workflows/stack-release-eligibility.yml` then generates correlated CTS/TSPP evidence, deterministic CTS replay evidence, composes combined assurance twice, proves semantic replay equivalence, runs fail-closed cross-stack cases, and publishes candidate evidence.

A successful workflow is evidence that the exact frozen tuple is reproducible; it is **not** by itself the human publication decision. Final publication requires the merged-main replay and explicit release judgment recorded under Hub issue #42.

Use the component repositories directly when you need to customize TSPP posture controls, CTS conformance/replay behavior, or Hub assurance composition. The coordinated stack does not transfer those repository-local authorities.
