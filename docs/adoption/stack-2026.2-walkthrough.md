# TRQP Stack 2026.2 adopter walkthrough

This walkthrough verifies the frozen Stack 2026.2 candidate from a clean bootstrap through lifecycle change, reassessment, recomposition, and supersession.

## Preconditions

Use `stack/releases/candidate/manifest.json`. It MUST resolve this immutable tuple:

- TSPP `v0.16.0` → `2f74a01fe22c346c11d9eb8feb8101d39ef68e17`
- CTS `v1.9.0` → `4395745d530df867329a312c58908a9d73f1c430`
- Assurance Hub `v1.12.0` → `7f7aae84eb41ffd8ea672dae00955c5714ffd3de`
- TSMM `v0.24.0`
- TIS `v0.15.0` → `edda0e87ced40797d22e3df542099871c57fcb59`

The release validator remotely verifies that each component version tag resolves to the declared commit before execution.

## Clean bootstrap

```bash
python tools/stack_bootstrap.py --clean
```

Expected result: each component is checked out at the exact frozen tagged commit and `.stack-work/bootstrap-manifest.json` records the same tuple.

## Execute component assurance

```bash
python tools/stack_evaluate.py
```

Then generate CTS and TSPP evidence using the same commands exercised by `.github/workflows/stack-release-eligibility.yml`.

## Lifecycle pressure path

```bash
python scripts/validate_lifecycle_recomposition.py
python scripts/validate_authority_drift_and_supersession.py
python tools/stack_2026_2_lifecycle_eligibility.py
```

The walkthrough demonstrates that material change makes historical assurance non-current; legitimate non-material documentation change may preserve current assurance; unknown impact broadens reassessment; unreviewed authority drift cannot inherit compatibility or remain current; and completed attributable reassessment establishes a new current state only with explicit predecessor/successor supersession lineage.

## Full release eligibility replay

```bash
make stack-release-check
python tools/stack_bootstrap.py --clean
```

Then execute the complete `stack-release-eligibility` workflow sequence. A successful workflow proves that the immutable tuple is reproducible and all declared machine gates pass. It does not replace the explicit human release decision.

## Acceptance evidence

The release judgment MUST cite the frozen tuple and commits, clean bootstrap result, successful full eligibility run ID and artifact digest, ten lifecycle gate results, residual uncertainty and rejected alternatives, and the explicit human decision to publish or withhold the Stack release.
