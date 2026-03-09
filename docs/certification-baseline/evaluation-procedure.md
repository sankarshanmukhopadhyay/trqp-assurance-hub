# Evaluation procedure

This document provides a repeatable evaluation flow for CTR-ACB.

The procedure is designed to be:

- **artifact-driven**
- **incrementally automatable**
- **compatible with multiple governance models** (self-attestation, peer review, accredited audit)

## Inputs

An evaluation consumes:

- an **Assurance Profile** (candidate, machine-readable)
- the **Control catalog** (stable IDs)
- one or more **Control Satisfaction Declarations**
- optional: **Lifecycle Assertion**, **Recognition Assertion(s)**
- supporting evidence bundles and/or manifests

## Steps

1. **Scope definition**
   - Identify the certified entity and scope (which registry deployment, which endpoints, which trust domain).
   - Select target tier (AL1–AL4).

2. **Artifact collection**
   - Collect the Assurance Profile and referenced artifacts.
   - Verify JSON schema validity (automatable).

3. **Integrity checks**
   - Verify checksums / manifests / provenance URLs as required by tier.
   - Record failures as control failures where applicable.

4. **Control evaluation**
   - For each in-scope control, determine status (`pass` / `fail` / `n/a`).
   - Record evidence references in the Control Satisfaction Declaration.

5. **Lifecycle + revocation review**
   - Confirm lifecycle state is consistent with evidence.
   - Confirm revocation signals exist and are actionable at the target tier.

6. **Recognition review (if applicable)**
   - Validate recognition assertions (scope, subject, issuer).
   - Confirm recognition edges are consistent with the stated trust domain.

7. **Issue Certification Attestation**
   - Produce a `TRQPCertificationAttestation` artifact.
   - Bind it to the control satisfaction declarations and key evidence references.
   - Sign it where applicable.

## Outputs

- Certification Attestation artifact
- Updated Control Satisfaction Declaration(s) (if needed)
- Optional evaluator report (human-readable)
