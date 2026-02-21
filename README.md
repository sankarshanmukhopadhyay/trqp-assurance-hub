# TRQP Assurance Hub

[![quality](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/actions/workflows/quality.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/actions/workflows/quality.yml)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

A pragmatic, adopter-first landing zone that makes the TRQP ecosystem feel like **one product** while keeping core components decoupled for independent iteration.

## Quick links

- [Quickstart](QUICKSTART.md)
- [Operating model](#the-operating-model)
- [Combined assurance workflow](docs/guides/combined-assurance.md)
- [Error states](docs/guides/error-states.md)
- [Compatibility policy + matrix](docs/policies/compatibility.md)
- [Issue routing](docs/policies/issue-routing.md)
- [Glossary](docs/glossary.md)

## What this is

This repository is the **front door** for TRQP implementation and assurance work:

- **Core conformance runner & profiles**: `trqp-conformance-suite`  
  <https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite>
- **Security & privacy profile overlay (TSPP)**: `TRQP-TSPP`  
  <https://github.com/sankarshanmukhopadhyay/TRQP-TSPP>

It provides:

- A single onboarding narrative (choose-your-path)
- A shared terminology map (runner vs profile packs)
- Cross-repo compatibility expectations
- A lightweight governance + issue routing model

## Choose your path (start in 60 seconds)

| You are trying to… | Start here | Outcome |
|---|---|---|
| Implement TRQP endpoints and prove protocol conformance | **Conformance Suite** | Test results + evidence bundles |
| Add security & privacy posture checks (AL1/AL2) | **TRQP-TSPP** | AL1/AL2 checks + posture evidence |
| Ship a production registry with both | **Both** | Protocol + posture assurance |

### Quick decision tree

- If you need **“Does my TRQP implementation behave correctly?”** → Conformance Suite
- If you need **“Is my deployment secure enough for the threat model?”** → TSPP
- If you need **“Can I show auditors both behavior + posture?”** → Use both

## The operating model

Think in layers:

- **Runner / Engine (platform):** runs tests, produces evidence, enforces result format
- **Profile Packs (products):** define requirements, mappings, and test plans

```mermaid
flowchart LR
  A["TRQP Implementer"] --> B["Assurance Hub<br/>this repo"];
  B --> C["Conformance Suite<br/>runner + profiles"];
  B --> D["TSPP<br/>security/privacy profile pack"];
  C --> E["Evidence Bundle"];
  D --> E;
  E --> F["Verification / Audit / Procurement"];
```


## Evidence artifact flow

```mermaid
flowchart TB
  A["TRQP Registry (target)"] --> B["Conformance Suite run"]
  A --> C["TSPP run"]
  B --> D["Conformance evidence bundle"]
  C --> E["TSPP evidence bundle"]
  D --> F["Combined Assurance Manifest"]
  E --> F
  F --> G["Auditors / Authorities / Procurement"]
  F --> H["Automated gating in CI/CD"]
```

## How the repos integrate (without merging)

### Integration contract (what must stay aligned)

We treat these as the **shared contracts** between repos:

1. **Requirement identifiers** (stable IDs)
2. **Evidence bundle format** (what an implementer produces)
3. **Result semantics** (pass/fail/skip, severity, rationale)
4. **Version compatibility declaration** (what versions of each tool are known-good together)

See: [`docs/policies/compatibility.md`](docs/policies/compatibility.md)

### What stays independent

- Release cadence
- Roadmaps
- Issue trackers
- Packaging choices

## Recommended “golden path” workflows

### Workflow A: Protocol conformance only

1. Install and run the Conformance Suite
2. Pick a profile (Baseline/Enterprise/High-Assurance)
3. Produce evidence bundle for your build artefacts

### Workflow B: Security & privacy posture only

1. Install and run TRQP-TSPP
2. Choose AL1 or AL2
3. Produce posture evidence bundle

### Workflow C: Combined assurance (recommended for production)

1. Run Conformance Suite profile
2. Run TSPP profile
3. Merge evidence bundles under a single build identifier

See: [`docs/guides/combined-assurance.md`](docs/guides/combined-assurance.md)

## AL-aware evidence artifact expectations

To operationalize audits (and avoid “interpretive dance”), AL3/AL4 are defined as **auditable properties** with a deterministic evidence surface.

### Canonical artifact kinds

Implementations and tools SHOULD use these `kind` values consistently:

- `signed_response_sample`
- `jwks_snapshot`
- `binding_meta_log`
- `replay_window_test_log`
- `change_log_snapshot`
- `key_rotation_evidence`
- `error_response_sample`
- `key_custody_evidence`
- `monitoring_runbook`
- `retention_policy`

### Evidence artifact matrix (normative)

| Artifact kind | What it proves | AL2 | AL3 | AL4 |
|---|---|---:|---:|---:|
| `signed_response_sample` | Successful responses are signed and verifiable | REQUIRED | REQUIRED | REQUIRED |
| `jwks_snapshot` | Signing keys used during the run are discoverable/consistent | REQUIRED | REQUIRED | REQUIRED |
| `binding_meta_log` | Signed envelope includes binding meta (`query_hash`, `iat`, `exp`) and it is enforced | OPTIONAL | REQUIRED | REQUIRED |
| `replay_window_test_log` | Replay window / TTL controls are enforced (`max_ttl_seconds`) | OPTIONAL | REQUIRED | REQUIRED |
| `change_log_snapshot` | Change transparency signals exist and are consumable | OPTIONAL | REQUIRED | REQUIRED |
| `key_rotation_evidence` | Rotation/overlap posture exists and is evidenced | OPTIONAL | REQUIRED | REQUIRED |
| `error_response_sample` | Structured errors are signed and deterministic | OPTIONAL | OPTIONAL | REQUIRED |
| `key_custody_evidence` | Key protection/custody claims are backed by evidence (HSM/KMS/policy attestation) | OPTIONAL | OPTIONAL | REQUIRED |
| `monitoring_runbook` | Monitoring + incident response posture is documented | OPTIONAL | OPTIONAL | REQUIRED |
| `retention_policy` | Evidence/log retention is declared for auditability | OPTIONAL | OPTIONAL | REQUIRED |

**REQUIRED** means a run claiming that AL MUST include the artifact in its evidence bundle (or a clearly referenced equivalent).  
**OPTIONAL** means it MAY be included and, when present, SHOULD be machine-checkable.


For machine-readable provenance across both runs, use the **Combined Assurance Manifest** schema: `schemas/combined-assurance-manifest.schema.json`.

## Issue routing (reduce contributor thrash)

- If the issue is about **test runner behavior, evidence output, CI, profiles in-suite** → file in `trqp-conformance-suite`
- If the issue is about **security/privacy requirements, AL1/AL2, posture checks** → file in `TRQP-TSPP`
- If the issue is about **cross-repo compatibility, documentation, onboarding** → file here

See: [`docs/policies/issue-routing.md`](docs/policies/issue-routing.md)

## Alignment with upstream TRQP

This work is intended as an extension of the Trust over IP TRQP workstream:

- Upstream: <https://github.com/trustoverip/tswg-trust-registry-protocol/tree/main>

## License

- Documentation and original content in this repo: **CC BY-SA 4.0**

See [`LICENSE`](LICENSE).
