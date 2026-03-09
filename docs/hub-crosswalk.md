# Assurance Hub ↔ Conformance Suite Crosswalk

This document maps **Assurance Hub** guidance and evidence expectations to the concrete artifacts emitted by the **TRQP Conformance Suite (CTS)**.

- Assurance Hub “front door”: https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub
- Hub combined workflow guide: https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/blob/main/docs/guides/combined-assurance.md
- Hub evidence artifacts matrix: https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/blob/main/docs/guides/evidence-artifacts.md

## What CTS emits

When you run CTS with `--evidence-out <dir>` (see README), CTS emits an **evidence bundle directory** containing:

| Artifact | Default path | artifact_kind | Notes |
|---|---|---|---|
| Bundle descriptor | `bundle_descriptor.json` | `conformance_evidence_bundle_descriptor` | Machine-readable index (paths + hashes). |
| Checksums | `checksums.json` | `evidence_bundle_checksums` | SHA-256 entries for key artifacts. |
| Run metadata | `run.json` | `conformance_run_metadata` | Run id, timestamp, profile, SUT target. |
| Verdicts | `verdicts.json` | `conformance_verdicts` | Per-test outcomes + reasons. |
| Manifest | `manifest.json` | `conformance_manifest` | Canonical list of run artifacts. |
| Manifest signature (optional) | `manifest.sig` | `conformance_manifest_signature` | Present for high-assurance profiles. |
| Bundle zip (optional) | `bundle.zip` | `conformance_evidence_bundle_zip` | Convenience packaging of the directory. |

## How this aligns to Hub evidence expectations

The Hub evidence matrix uses the “**Conformance evidence bundle**” row as the primary CTS output. CTS implements this as:

- `bundle_descriptor.json` + `checksums.json` as the **index + integrity layer**
- `run.json` + `verdicts.json` + `manifest.json` as the **audit core**
- optional `manifest.sig` for **signed evidence** where required

## Combined-assurance smoke workflow hook

For a fast “is the plumbing alive?” check used by the Hub workflow:

- Use the `smoke` profile (`profiles/smoke.yaml`)
- Ensure `bundle_descriptor.json` and `checksums.json` are present
- Upload `bundle.zip` as an artifact if you want a single portable object for downstream inspection

## Schema references

CTS publishes lightweight schemas for its evidence outputs:

- `schemas/evidence/bundle_descriptor.schema.json`
- `schemas/evidence/checksums.schema.json`


## Assurance Level contract

This repo ships `al-contract.json` which references the canonical AL definitions in the Assurance Hub and includes the canonical doc SHA-256 (61c599c5fa06e0c9110f40ff71c0174db5502105b97f1391dbd9ae8548115f71).

## GRID alignment

This suite includes optional schemas and guidance for GRID-style artifacts.

- `docs/GRID_SUPPORT.md`
- `schemas/registrar.schema.json`
- `schemas/grid-status-feed.schema.json`

## Version pins

- TRQP Assurance Hub: v0.8.1
- TRQP Conformance Suite: v0.7.1
- TRQP TSPP: v0.5.1

## UNTP DIA considerations

Where a directory uses UNTP Digital Identity Anchor (DIA) / Identity Resolver (IDR), conformance evidence SHOULD include DIA context references and resolver documentation. The CTS validator includes lightweight checks for DIA context wiring when `identity_anchor.anchor_type` indicates UNTP DIA.

## Supply chain integrity artifacts (TSPP-SCI)

CTS recognizes optional supply chain integrity evidence artifacts in bundle descriptors:

| artifact_kind | Example | Purpose |
|---|---|---|
| `software_sbom` | SPDX/CycloneDX SBOM | Dependency transparency for deployed artifacts |
| `build_provenance` | provenance attestation | Verifiable build chain for AL3+ |
| `openssf_scorecard_report` | scorecard output | Automated posture checks evidence |

Reference: `docs/reference/openssf-supply-chain.md`.
