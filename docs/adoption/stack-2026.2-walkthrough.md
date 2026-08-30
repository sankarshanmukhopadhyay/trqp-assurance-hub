# TRQP Stack 2026.2 adopter walkthrough

This walkthrough verifies the frozen Stack 2026.2 candidate from a clean bootstrap through lifecycle change, reassessment, recomposition, and supersession.

## Preconditions

Use the candidate manifest at `stack/releases/candidate/manifest.json`. The manifest MUST resolve the frozen RC refs and exact commit SHAs recorded in `stack/candidates/2026.2/release-candidate.md`.

## Clean bootstrap

```bash
python tools/stack_bootstrap.py --clean
```

Expected result: each component is checked out at the exact frozen commit and `.stack-work/bootstrap-manifest.json` records the same tuple.

## Execute component assurance

```bash
python tools/stack_evaluate.py
```

Then generate CTS and TSPP evidence using the same commands exercised by `.github/workflows/stack-release-eligibility.yml`.

## Lifecycle pressure path

Validate the existing lifecycle boundary suite:

```bash
python scripts/validate_lifecycle_recomposition.py
python scripts/validate_authority_drift_and_supersession.py
python tools/stack_2026_2_lifecycle_eligibility.py
```

The walkthrough must demonstrate:

1. a material change makes historical assurance non-current;
2. a legitimate non-material documentation change may preserve current assurance;
3. unknown impact fails safe and broadens reassessment;
4. unreviewed authority drift cannot inherit compatibility or remain current;
5. completed attributable reassessment may establish a new current state only with explicit predecessor/successor supersession lineage.

## Full release eligibility replay

```bash
make stack-release-check
python tools/stack_bootstrap.py --clean
```

Then execute the complete `stack-release-eligibility` workflow sequence. A successful workflow proves that the frozen tuple is reproducible and all declared machine gates pass. It does not replace the explicit human release decision.

## Acceptance evidence

The release judgment MUST cite:

- the frozen tuple and commits;
- the clean bootstrap result;
- the successful full eligibility run ID;
- the ten lifecycle gate results;
- residual uncertainty and any rejected alternatives;
- the explicit human decision to publish or withhold the Stack release.
