---
owner: maintainers
last_reviewed: 2026-08-20
tier: 0
---

# TRQP Assurance Hub

The TRQP Assurance Hub is the **evidence aggregation and assurance publication layer** in the TRQP Operational Trust Stack. It combines protocol-conformance evidence from the TRQP Conformance Suite with security/privacy posture evidence from TRQP-TSPP, evaluates the declared assurance profile, and publishes a machine-readable Combined Assurance Manifest and assurance decision for downstream review.

> **Current release:** v1.10.0  
> **Lifecycle:** Active  
> **Maturity:** Candidate  
> **Operational status:** Active validation  
> **Specification status:** Candidate specification

| Attribute | Value |
|---|---|
| Portfolio tier | Flagship |
| Primary role | Assurance evidence ingestion, composition and publication |
| Portfolio contract role | `assurance-aggregator` |
| Primary output | Combined Assurance Manifest and assurance decision |
| Validation | `make validate` |
| Assurance evidence | `make assurance-check` |
| Evidence output | `artifacts/combined-assurance/combined-assurance-manifest.json`, `artifacts/combined-assurance/assurance-decision.json`, `artifacts/combined-assurance/traceability-report.json` |
| Governance authority | [`GOVERNANCE.md`](GOVERNANCE.md) and [`PROJECT-STATUS.yaml`](PROJECT-STATUS.yaml) |
| Portfolio integration | [`portfolio/integration-contract.json`](portfolio/integration-contract.json) |
| Documentation site | https://sankarshanmukhopadhyay.github.io/trqp-assurance-hub/ |

## What v1.10.0 establishes

v1.10.0 connects the Hub to the current executable governance layer and makes the cross-repository assurance boundary machine-verifiable.

- Pins **Trust Systems Meta-Model (TSMM) v0.24.0** as semantic authority for TRQP assurance interpretation.
- Pins **Trust Infrastructure Schemas (TIS) v0.14.1** as schema and portfolio-authority baseline.
- Declares TRQP-TSPP v0.15.0 as the source of security/privacy posture evidence.
- Declares TRQP Conformance Suite v1.7.0 as the source of executable conformance evidence.
- Validates release pins, required source evidence, repository relationships and integration invalidation conditions in CI.
- Treats missing or incompatible source evidence as an invalid portfolio integration state rather than a documentation warning.

See [`RELEASE_NOTES_v1.10.0.md`](RELEASE_NOTES_v1.10.0.md) for the release record.

## Authority and scope

The Assurance Hub has repository-local authority over:

- assurance evidence ingestion and composition;
- assurance profile evaluation;
- portable assurance publication; and
- combined assurance decision generation.

The Hub **does not** own the TRQP protocol specification, raw conformance execution, TSPP control definitions, or external certification/accreditation. Those boundaries are declared in [`PROJECT-STATUS.yaml`](PROJECT-STATUS.yaml) and [`portfolio/integration-contract.json`](portfolio/integration-contract.json).

## Where this fits

| Layer | Repository role | Primary output |
|---|---|---|
| TRQP-TSPP v0.15.0 | Security/privacy posture computation | Posture Report and control evidence |
| TRQP Conformance Suite v1.7.0 | Executable protocol conformance | Conformance Report and evidence bundle |
| TRQP Assurance Hub v1.10.0 | Evidence aggregation and assurance publication | Combined Assurance Manifest and assurance decision |

Shared authorities:

| Authority | Version | Purpose |
|---|---:|---|
| Trust Systems Meta-Model | 0.24.0 | TRQP semantic binding and semantic concepts |
| Trust Infrastructure Schemas | 0.14.1 | Portfolio relationships, repository authority and validation-result contracts |

The Hub integration becomes invalid when required source evidence is missing, source assurance evidence is invalid, or the declared semantic/schema authority versions are incompatible.

## Runtime assurance flow

```text
TRQP-TSPP Posture Report
            +
TRQP Conformance Suite evidence
            ↓
Combined Assurance Manifest
            ↓
Assurance decision + traceability report
            ↓
Relying-party, assessor, procurement or ecosystem review
```

The machine-readable authority chain is:

```text
TSMM semantic authority
        ↓
TIS schema / portfolio authority
        ↓
TSPP posture evidence + CTS conformance evidence
        ↓
Assurance Hub aggregation
```

A passing test run alone is not an assurance conclusion. The Hub preserves who had authority, what scope was evaluated, which evidence was consumed, what lifecycle/revocation state applies, and what condition would invalidate the combined result.

## Evidence artifacts

| Artifact | Purpose | Schema or example |
|---|---|---|
| Combined Assurance Manifest | Binds CTS and TSPP evidence to one target/run/claim | `schemas/combined-assurance-manifest.schema.json` |
| Assurance decision | Machine-readable combined assurance outcome | `artifacts/combined-assurance/assurance-decision.json` |
| Traceability report | Cross-repository evidence and control traceability | `artifacts/combined-assurance/traceability-report.json` |
| Public Assurance Summary | Relying-party-facing assurance publication | `schemas/public-assurance-summary.schema.json` |
| Machine-readable assurance profile | Declares AL1–AL4 expectations | `schemas/machine-readable-assurance-profile.schema.json` |
| Control satisfaction evidence | Maps controls to evidence artifacts | `schemas/control-satisfaction.schema.json` |
| Certification attestation | Binds assessor, scope, validity and evidence when used | `schemas/certification-attestation.schema.json` |

## Start here

- [`docs/guides/combined-assurance.md`](docs/guides/combined-assurance.md) — compose CTS and TSPP evidence.
- [`docs/guides/evidence-artifacts.md`](docs/guides/evidence-artifacts.md) — evidence artifact model.
- [`docs/guides/public-assurance-publication.md`](docs/guides/public-assurance-publication.md) — publish relying-party-facing assurance.
- [`docs/adoption/README.md`](docs/adoption/README.md) — adoption checklists.
- [`docs/reference/compatibility-matrix.md`](docs/reference/compatibility-matrix.md) — supported release relationships.
- [`docs/reference/tsmm-tis-runtime-assurance-contract.md`](docs/reference/tsmm-tis-runtime-assurance-contract.md) — semantic/artifact contract background.
- [`docs/portfolio-integration.md`](docs/portfolio-integration.md) — synchronized TRQP portfolio integration.
- [`docs/governance/release-policy.md`](docs/governance/release-policy.md) — release governance.
- [`docs/governance/change-intake.md`](docs/governance/change-intake.md) — change intake criteria.

## Quick validation

Run the repository validation gate:

```bash
make validate
```

Run the cross-stack negative-case assurance checks:

```bash
make assurance-check
```

The validation surface includes project-status validation, compatibility-registry validation, examples, documentation tests and operational-stack artifact checks.

## Operational stack integration

CTS and TSPP evidence should share the same `run_id` and `target_id` before aggregation. The Hub then binds those source artifacts into the Combined Assurance Manifest and preserves producer version, checksums and traceability.

The synchronized release tuple is:

```text
TRQP-TSPP             v0.15.0
TRQP Conformance Suite v1.7.0
TRQP Assurance Hub     v1.10.0
TSMM                    v0.24.0
TIS                     v0.14.1
```

The CI manifest-generation smoke test uses the current CTS/TSPP tuple rather than obsolete example versions.

## Repository map

| Path | Purpose |
|---|---|
| `schemas/` | Combined assurance, profile, control-satisfaction and publication schemas |
| `profiles/` | Machine-readable assurance profiles |
| `tools/` | Manifest generation and operational-stack tooling |
| `artifacts/combined-assurance/` | Current combined assurance evidence |
| `examples/` | Example source and output artifacts |
| `portfolio/` | Cross-repository integration contract |
| `docs/guides/` | Operational assurance guidance |
| `docs/reference/` | Compatibility and semantic/artifact contract references |
| `docs/adoption/` | Adoption and implementation checklists |

## Invalidation, supersession and auditability

Combined assurance is explicitly conditional. It can be invalidated by incompatible semantic/schema authority versions, missing required source evidence, or invalid source assurance evidence. Releases and status claims are superseded through versioned repository artifacts rather than silently rewriting historical evidence.

Example or self-generated evidence does not constitute independent assurance, certification or accreditation.

## Documentation site

GitHub Pages uses Just the Docs and is deployed from `main` through GitHub Actions. Repository administrators should configure **Settings → Pages → Source: GitHub Actions**.

Documentation governance: [`docs/governance/README.md`](docs/governance/README.md).

## License

See [`LICENSE`](LICENSE).
