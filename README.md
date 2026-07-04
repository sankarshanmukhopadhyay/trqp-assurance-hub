---
owner: maintainers
last_reviewed: 2026-07-03
tier: 0
---

## Documentation

- Documentation governance: [`docs/governance/README.md`](docs/governance/README.md)

# TRQP Assurance Hub

📘 **Documentation site (GitHub Pages):** https://sankarshanmukhopadhyay.github.io/trqp-assurance-hub/

**Current version:** v1.8.0

**Downstream release train:** TSPP v0.13.0 · Conformance Suite v1.5.0

TRQP Assurance Hub is the orchestration layer for the TRQP operational trust stack. It binds protocol conformance evidence and deployment posture evidence into a Combined Assurance Manifest, public assurance summary, and adoption workflow that operators, assessors, procurement teams, relying parties, and governance stewards can inspect without reverse-engineering tool output.

## What is new in v1.8.0

v1.8.0 is the **Operational Trust Stack Maturity Release**. It moves the Hub from an integration guide into the adoption front door for the three-repository TRQP assurance stack.

- Adds release governance that blocks low-value version churn and requires evidence, validation, documentation impact, and compatibility review for future releases.
- Publishes a maturity release validation record with the commands adopters and maintainers should expect before accepting a release.
- Adds change-intake guidance so fixes, features, and ecosystem alignment work are batched into meaningful release increments.
- Clarifies the adoption path across CTS, TSPP, and Hub so relying parties can move from conformance evidence to posture evidence to public assurance publication.
- Refreshes compatibility metadata for the coordinated Hub v1.8.0 / CTS v1.5.0 / TSPP v0.13.0 release tuple.

## Prior release: v1.7.0

v1.7.0 adds the **TSMM/TIS Runtime Assurance Contract Pack**. The release aligns Hub assurance orchestration with TSMM v0.21.0 semantics and TIS v0.10.0 executable artifact contracts.

- Combined Assurance Manifests can declare TSMM semantic mappings for authority, delegation, evidence, lifecycle, decision, and effect.
- Manifests can reference TIS artifact contracts for evidence bundle manifests, conformance declarations, decision receipts, registry publication profiles, and status or revocation evidence.
- A new runtime assurance contract guide explains how CTS and TSPP evidence becomes reviewable Hub assurance evidence.
- Compatibility metadata is refreshed for the coordinated v1.7.0 / v1.4.0 / v0.12.0 release tuple.
- Portfolio release-impact and drift-review records are published as governance evidence for cross-repo maintainers.

## Where this fits

| Layer | Repository | Primary output | Consumed by Hub |
|---|---|---|---|
| Protocol verification | TRQP Conformance Suite v1.5.0 | Conformance Report and CTS evidence bundle | Combined Assurance Manifest |
| Posture computation | TRQP-TSPP v0.13.0 | Posture Report and posture evidence bundle | Combined Assurance Manifest |
| Assurance orchestration | TRQP Assurance Hub v1.8.0 | Combined Assurance Manifest and Public Assurance Summary | Relying parties, assessors, ecosystem operators |
| Semantic model | TSMM v0.21.0 | Authority, delegation, evidence, decision, effect vocabulary | Runtime assurance contract |
| Artifact contract layer | TIS v0.10.0 | Evidence, decision, conformance, registry, status schemas | Manifest references and validation targets |

## Runtime assurance flow

```text
CTS Conformance Report + TSPP Posture Report
  -> Combined Assurance Manifest
  -> Public Assurance Summary
  -> Relying-party review, assessor review, procurement intake
```

The current contract makes this flow more explicit:

```text
TSMM semantics -> TIS artifact references -> Hub assurance publication
```

This matters because a passing test run is not enough. A relying party also needs to know who had authority, what scope was evaluated, what evidence was used, whether lifecycle or revocation state can change the result, and which artifacts can be audited later.

## Start here

- Maturity release validation: [`docs/release-validation.md`](docs/release-validation.md)
- Release policy: [`docs/governance/release-policy.md`](docs/governance/release-policy.md)
- Change intake: [`docs/governance/change-intake.md`](docs/governance/change-intake.md)
- Runtime assurance contract: [`docs/reference/tsmm-tis-runtime-assurance-contract.md`](docs/reference/tsmm-tis-runtime-assurance-contract.md)
- Combined assurance guide: [`docs/guides/combined-assurance.md`](docs/guides/combined-assurance.md)
- Evidence artifacts guide: [`docs/guides/evidence-artifacts.md`](docs/guides/evidence-artifacts.md)
- Compatibility matrix: [`docs/reference/compatibility-matrix.md`](docs/reference/compatibility-matrix.md)
- Public assurance publication: [`docs/guides/public-assurance-publication.md`](docs/guides/public-assurance-publication.md)
- Adoption checklists: [`docs/adoption/README.md`](docs/adoption/README.md)

## Evidence artifacts

| Artifact | Purpose | Schema or example |
|---|---|---|
| Combined Assurance Manifest | Binds CTS and TSPP outputs to one target, run, and assurance claim | `schemas/combined-assurance-manifest.schema.json` |
| Public Assurance Summary | Publishes the assurance result for relying-party consumption | `schemas/public-assurance-summary.schema.json` |
| Machine-readable assurance profile | Declares AL1 to AL4 expectations | `schemas/machine-readable-assurance-profile.schema.json` |
| Control satisfaction evidence | Maps controls to evidence artifacts | `schemas/control-satisfaction.schema.json` |
| Certification attestation | Binds assessor, scope, validity, and evidence | `schemas/certification-attestation.schema.json` |

## Validation

Install repository validation dependencies:

```bash
python -m pip install -r cts/requirements.txt
```

Run the local validation set:

```bash
python tools/validate_examples.py
python scripts/doc_tests.py
python tools/validate_operational_stack.py --bundle-dir artifacts/operational-stack
```

## Current release posture

v1.8.0 is additive and governance-focused. Existing v1.7.0 Combined Assurance Manifest consumers remain compatible. Future releases are expected to meet the release policy gate rather than shipping minor documentation or reference updates as standalone releases.
