---
layout: default
title: TRQP Assurance Hub
owner: maintainers
last_reviewed: 2026-03-10
tier: 0
---

# Documentation Index

This hub is designed to be *role-first*: you should be able to find what you need without reading every file.

## Choose your path

### Operators (registry / trust list operators)
You are responsible for running a service and producing assurance evidence.

- Start with: [Assurance levels (AL1–AL4)](guides/assurance-levels.md)
- Then: [Evidence & artifact expectations matrix](guides/evidence-artifacts.md)
- Worked bundles:
  - [AL3 evidence bundle (example)](../examples/al3-evidence-bundle/README.md)
  - [AL4 evidence bundle (example)](../examples/al4-evidence-bundle/README.md)
- Certification baseline: [Certification baseline](certification-baseline/)
- Ayra Trust Network: [Ayra submission checklist](../tools/ayra-mapping.md)

### Ayra Trust Network operators
You are preparing to join or are operating within the Ayra Trust Network.

- Pre-certification crosswalk: [Ayra control mapping and submission checklists](../tools/ayra-mapping.md)
- CTS profile: `profiles/ayra_baseline.yaml` (in `trqp-conformance-suite`)
- TSPP profile: [TSPP Ayra baseline](../docs/profiles/ayra-baseline.md) (in `TRQP-TSPP`)
- Ayra TRQP Profile: https://ayraforum.github.io/ayra-trust-registry-resources/
- Ayra Implementers Guide: https://ayraforum.github.io/ayra-trust-registry-resources/guides/

### Certifiers / assessors
You are evaluating evidence, validating conformance, and closing remediation.

- Canonical definitions: [Assurance levels (AL1–AL4)](guides/assurance-levels.md)
- What to ask for: [Evidence & artifact expectations matrix](guides/evidence-artifacts.md)
- Example submissions:
  - [AL3 evidence bundle (example)](../examples/al3-evidence-bundle/README.md)
  - [AL4 evidence bundle (example)](../examples/al4-evidence-bundle/README.md)
- Program scaffolding: [Certification baseline](certification-baseline/)

### Implementers / tooling integrators
You are integrating endpoints, schemas, and validation into pipelines.

- Getting started: [Quickstart](../QUICKSTART.md)
- The workflow: [Combined assurance guide](guides/combined-assurance.md)
- Narrative: [Operational Stack narrative](architecture/operational-stack.md)
- Discovery: [Trust Registry reference service](guides/trust-registry-reference-service.md)
- Contracts: [Machine-readable assurance profiles](guides/machine-readable-assurance-profiles.md)
- Schemas: [Schemas](../schemas/)
- Example payloads: [Examples](../examples/)
- Error handling: [Error states](guides/error-states.md)

### Governance / policy designers
You are translating governance intent into implementable and auditable artifacts.

- Canonical model: [Assurance levels (AL1–AL4)](guides/assurance-levels.md)
- Evidence structure: [Evidence & artifact expectations matrix](guides/evidence-artifacts.md)
- Certification baseline: [Certification baseline](certification-baseline/)
- Roadmap: [Roadmap](roadmap.md)

## Canonical references
- [TSAM (Trust Systems Assurance Method)](tsam/README.md)
- [TRACE ↔ TSAM relationship](strategy/TRACE-TSAM-relationship.md)
- [Assurance levels (AL1–AL4)](guides/assurance-levels.md)
- [Evidence & artifact expectations matrix](guides/evidence-artifacts.md)
- [Combined assurance workflow](guides/combined-assurance.md)
- [Operational Stack narrative](architecture/operational-stack.md)
- [Trust Registry reference service](guides/trust-registry-reference-service.md)
- [Machine-readable assurance profiles](guides/machine-readable-assurance-profiles.md)
- [Ayra Trust Network crosswalk](../tools/ayra-mapping.md)

### GRID implementers (directory operators)

- Profile: `../profiles/grid-profile.md`
- Verifier workflow: `how-to-verify-grid.md`
- Crosswalk to GTR: `grid-gtr-crosswalk.md`

### Authoritative directories (SAD-1)

SAD-1 is the **registry-agnostic profile** that lets the TRQP ecosystem evaluate authoritative directories, including sovereign registries.

- Profile: `../profiles/sad-1-profile.md`
- End-to-end workflow: `guides/directory-assurance-workflow.md`
- Strategy note: `strategy/authoritative-directories.md`

## Reference

- [UNTP Digital Identity Anchor (DIA)](reference/untp-digital-identity-anchor.md)

## Supply chain integrity

- OpenSSF-aligned reference: `docs/reference/openssf-supply-chain.md`

## Experimental support

TRQP Assurance Hub includes an **experimental DeDi profile** to map decentralized directory artifacts into the Hub's assurance workflow.

- Profile: `profiles/dedi-experimental-profile.md`
- Upstream: https://github.com/LF-Decentralized-Trust-labs/decentralized-directory-protocol

## Governance

- Documentation freshness policy: [`docs/governance/README.md`](governance/README.md)
