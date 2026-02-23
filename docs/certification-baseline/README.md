# Candidate Trust Registry Assurance & Certification Baseline

This package defines a **Candidate Trust Registry Assurance & Certification Baseline** (CTR-ACB).

It is **not** a certification authority, and it does **not** modify TRQP transport semantics.
It is a **transport-neutral, implementation-neutral baseline** for how a trust registry (and its operators) can be assessed and certified using **machine-readable artifacts**.

The baseline builds on the existing assurance artifacts in this repository:

- **TRQP Assurance Profile** (public posture + governance commitments)
- **Control Satisfaction Declaration** (control-level evidence binding)
- **Lifecycle Assertion** (state + transition evidence)
- **Recognition Assertion** (scoped recognition edges + evidence)
- **Revocation semantics** (how trust-impacting changes are signaled)

## What this enables

CTR-ACB provides the foundations for an eventual trust registry software certification program by defining:

- A **normative control framework** (testable requirements + evidence expectations)
- A **tier model** aligned to AL1–AL4
- A repeatable **evaluation procedure**
- A machine-readable **Certification Attestation** artifact

Different ecosystems can operationalize this baseline in different ways (self-attestation, industry peer review, accredited assessor), while still producing interoperable artifacts.

## Non-goals

CTR-ACB does **not**:

- define who the assessor is (that is ecosystem governance)
- accredit assessors
- define transport extensions or endpoint discovery conventions
- replace TRQP-TSPP or the TRQP conformance suite

## Where to start

1. Read the tier model: [`assurance-tier-model.md`](assurance-tier-model.md)
2. Understand controls: [`control-framework.md`](control-framework.md)
3. Follow the evaluation flow: [`evaluation-procedure.md`](evaluation-procedure.md)
4. Review the attestation artifact: [`certification-attestation.md`](certification-attestation.md)
