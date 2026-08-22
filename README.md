---
owner: maintainers
last_reviewed: 2026-08-22
tier: 0
---

# TRQP Assurance Hub

The TRQP Assurance Hub is the **evidence aggregation and assurance publication layer** in the TRQP Operational Trust Stack. It combines protocol-conformance evidence from the TRQP Conformance Suite with security/privacy posture evidence from TRQP-TSPP, evaluates the declared assurance profile, and publishes a machine-readable Combined Assurance Manifest and assurance decision for downstream review.

> **Current release:** v1.11.0  
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

## What v1.11.0 establishes

v1.11.0 promotes CTS evidence reproducibility into the Hub's executable assurance boundary.

- Consumes **TRQP Conformance Suite v1.8.0** conformance evidence and replay-determinism evidence.
- Pins **TRQP-TSPP v0.15.0** for the coordinated August 2026 release tuple.
- Preserves the CTS replay comparison policy ID, version and SHA-256 in the combined assurance evidence chain.
- Fails closed when CTS replay determinism is missing, malformed, false, or contains prohibited semantic differences.
- Distinguishes a conformance failure from an evidence-reproducibility failure; both are material assurance signals but they are not the same condition.
- Pins **Trust Systems Meta-Model (TSMM) v0.24.0** as semantic authority and **Trust Infrastructure Schemas (TIS) v0.14.1** as schema/portfolio authority.

## Authority and scope

The Assurance Hub has repository-local authority over:

- assurance evidence ingestion and composition;
- assurance profile evaluation;
- portable assurance publication;
- combined assurance decision generation; and
- interpretation of CTS replay-determinism evidence for Hub assurance decisions.

The Hub **does not** own the TRQP protocol specification, raw conformance execution, the CTS replay comparison policy, TSPP control definitions, or external certification/accreditation. Those boundaries are declared in [`PROJECT-STATUS.yaml`](PROJECT-STATUS.yaml) and [`portfolio/integration-contract.json`](portfolio/integration-contract.json).

## Where this fits

| Layer | Repository role | Primary output |
|---|---|---|
| TRQP-TSPP v0.15.0 | Security/privacy posture computation | Posture Report and control evidence |
| TRQP Conformance Suite v1.8.0 | Executable protocol conformance + reproducibility | Conformance evidence + replay determinism report |
| TRQP Assurance Hub v1.11.0 | Evidence aggregation and assurance publication | Combined Assurance Manifest and assurance decision |

Shared authorities:

| Authority | Version | Purpose |
|---|---:|---|
| Trust Systems Meta-Model | 0.24.0 | TRQP semantic binding and semantic concepts |
| Trust Infrastructure Schemas | 0.14.1 | Portfolio relationships, repository authority and validation-result contracts |

The Hub integration becomes invalid when required source evidence is missing, source assurance evidence is invalid, CTS replay determinism is invalid or policy-incompatible, or the declared semantic/schema authority versions are incompatible.

## Runtime assurance flow

```text
TRQP-TSPP Posture Report
            +
TRQP Conformance Suite evidence
            +
CTS replay determinism report + comparison-policy identity
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
TSPP posture evidence + CTS conformance/reproducibility evidence
        ↓
Assurance Hub aggregation
```

A passing test run alone is not an assurance conclusion. The Hub preserves who had authority, what scope was evaluated, which evidence was consumed, whether CTS evidence was reproducible under its declared comparison policy, what lifecycle/revocation state applies, and what condition would invalidate the combined result.

## Evidence artifacts

| Artifact | Purpose | Schema or source |
|---|---|---|
| Combined Assurance Manifest | Binds CTS, CTS replay determinism and TSPP evidence to one assurance chain | `artifacts/combined-assurance/combined-assurance-manifest.json` |
| Assurance decision | Machine-readable combined assurance outcome | `schemas/assurance-decision.schema.json` |
| Traceability report | Cross-repository evidence/control/reproducibility traceability | `artifacts/combined-assurance/traceability-report.json` |
| CTS replay determinism report | Evidence-equivalence result consumed from CTS v1.8.0 | CTS `schemas/evidence/replay-determinism-report.schema.json` |
| CTS replay comparison policy | Declared semantic/volatile comparison boundary | CTS `policies/replay-determinism.v1.json` |
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

The coordinated smoke workflow additionally generates CTS v1.8.0 fixture-pinned replay evidence, verifies its determinism report, then requires that report during Hub composition.

## Operational stack integration

CTS and TSPP evidence must share the same `run_id` and `target_id` before aggregation. For the v1.11.0 release tuple, CTS replay determinism evidence is also mandatory and is preserved in the Combined Assurance Manifest with policy identity and semantic hashes.

The synchronized release tuple is:

```text
TRQP-TSPP              v0.15.0
TRQP Conformance Suite v1.8.0
TRQP Assurance Hub     v1.11.0
TSMM                    v0.24.0
TIS                     v0.14.1
```

The CI smoke test checks out the tagged CTS/TSPP releases rather than mutable `main` branches.

## Repository map

| Path | Purpose |
|---|---|
| `schemas/` | Combined assurance, profile, control-satisfaction and publication schemas |
| `profiles/` | Machine-readable assurance profiles |
| `tools/` | Manifest generation, CTS determinism validation and operational-stack tooling |
| `artifacts/combined-assurance/` | Current combined assurance evidence |
| `examples/` | Example source and output artifacts |
| `portfolio/` | Cross-repository integration contract |
| `docs/guides/` | Operational assurance guidance |
| `docs/reference/` | Compatibility and semantic/artifact contract references |
| `docs/adoption/` | Adoption and implementation checklists |

## Invalidation, supersession and auditability

Combined assurance is explicitly conditional. It can be invalidated by incompatible semantic/schema authority versions, missing required source evidence, invalid source assurance evidence, failed CTS replay determinism, or a CTS replay comparison policy that the Hub release tuple does not recognise as compatible. Releases and status claims are superseded through versioned repository artifacts rather than silently rewriting historical evidence.

Example or self-generated evidence does not constitute independent assurance, certification or accreditation.

## Documentation site

GitHub Pages uses Just the Docs and is deployed from `main` through GitHub Actions. Repository administrators should configure **Settings → Pages → Source: GitHub Actions**.

Documentation governance: [`docs/governance/README.md`](docs/governance/README.md).

## License

See [`LICENSE`](LICENSE).
