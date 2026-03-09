# Certification Baseline Alignment (CTR-ACB)

This document explains how **TRQP Conformance Suite (CTS)** supports the *Candidate Trust Registry Assurance & Certification Baseline (CTR-ACB)* published in the TRQP Assurance Hub.

## Role in the stack

- **TRQP Assurance Hub**: defines a transport-neutral *assurance + governance + certification baseline* model using machine-readable artifacts (profiles, controls, lifecycle, recognition, certification attestation).
- **TRQP-TSPP**: defines a security & privacy posture profile layer (what “good” looks like for registry endpoints and responses).
- **TRQP Conformance Suite (this repo)**: executes tests and produces **deterministic evidence outputs**.

CTS is deliberately **not** a certification authority. It is an evidence-producing verification component.

## How CTS outputs are used

CTS outputs can be referenced as `evidence_refs` in baseline artifacts such as:

- Control Satisfaction Declarations
- Certification Attestations (CTR-ACB)

A typical flow:

1. Registry publishes an Assurance Profile (and related artifacts).
2. CTS runs conformance tests against registry endpoints / responses.
3. CTS emits evidence artifacts (reports, logs, result manifests).
4. A Control Satisfaction Declaration references the CTS evidence outputs.
5. Optionally, an assessor issues a Certification Attestation referencing those declarations.

## Recommended integration pattern

- Treat CTS output artifacts as **immutable evidence snapshots** (content-addressed or versioned).
- Keep test configuration and versions with the evidence output.
- Ensure evidence artifacts are accessible to auditors/verifiers (or escrowed appropriately).

## Non-goals

- CTS does not define accreditation criteria for assessors.
- CTS does not issue certificates.
- CTS does not set policy for renewal cadence or certification revocation.

Those belong to the baseline layer.
