# Certification attestation

CTR-ACB introduces a machine-readable **Certification Attestation** artifact.

This artifact is the *bridge* between:

- assurance artifacts (profiles, assertions, evidence)
- certification governance (who evaluated, what scope, how long it is valid)

## What a certification attestation asserts

At minimum:

- **who** is certified (subject)
- **what** scope is covered (controls + boundaries)
- **which tier** the certification claims (AL1–AL4)
- **who evaluated** (assessor identity)
- **when** it is valid (validity window)
- **what evidence** was used (references)

## Artifact files

- Schema: `schemas/certification-attestation.schema.json`
- Example: `examples/certification-attestation.example.json`

## Relationship to other artifacts

A Certification Attestation SHOULD reference:

- the **Assurance Profile**
- one or more **Control Satisfaction Declarations**
- optional: **Lifecycle Assertion**, **Recognition Assertion(s)**

It MAY also reference:

- combined assurance manifest(s)
- CI run URLs / provenance attestations
- checksum files

See also: [`revocation-renewal.md`](revocation-renewal.md).
