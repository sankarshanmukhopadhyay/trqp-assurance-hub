# Changelog

All notable changes to this repository will be documented in this file.


## v0.5.0 — GRID readiness kernel (2026-03-02)

- Added GRID profile (docs + machine-readable profile descriptor)
- Added registrar listing schema compatible with GTR registrar-v1 fields plus TRQP assurance extensions
- Added signed status feed schema + examples
- Added verifier-first workflow doc and minimal threat annex

## Unreleased

- (nothing yet)



## v0.5.0

### Added
- `al-contract.json` to provide a machine-readable contract for canonical AL1–AL4 semantics (includes SHA-256 of the normative AL doc).

### Changed
- Clarified normative status of `docs/guides/assurance-levels.md` for cross-repo consumption and audit stability.


## v0.4.0

### Added

- Candidate Trust Registry Assurance & Certification Baseline documentation pack (`docs/certification-baseline/`).
- Certification Attestation artifact (schema + example) to bind assessor identity, scope, validity, and evidence references.
- Normative control framework fields in the control catalog (requirements, evidence, evaluation method, severity, tier applicability).

### Changed

- Evidence artifacts matrix updated to include Certification Attestation.
- CI example cross-checks extended to cover certification attestation evidence references.
- README and TRQP alignment documentation updated to clarify the certification-baseline positioning.


## v0.3.0

### Added

- Recognition Assertion artifact (schema + example + guide).
- Lifecycle Assertion artifact and lifecycle state model guidance.
- Candidate control catalog and Control Satisfaction Declaration artifact.
- Recognition graph semantics and assurance-layer revocation semantics guides.
- JSON Schema validation in CI (examples validated against schemas).

### Changed

- Assurance Profile schema extended to bind controls, lifecycle pointers, and references to standalone recognition assertions.
- Evidence artifacts matrix updated to include control, lifecycle, recognition, and revocation artifacts.
- Combined Assurance Manifest example extended to demonstrate new artifact kinds.

### Added

- Combined assurance smoke workflow that emits a manifest and an artifact checklist.
- Combined Assurance Manifest schema and example.
- Evidence artifacts and expectations guide (includes AL1–AL4 matrix).
- Upstream TRQP RFE alignment document.
- Candidate TRQP Assurance Profile schema and example (machine-readable governance + assurance declarations).

### Fixed

- Documentation formatting and markdownlint compliance for headings, lists, and links.
