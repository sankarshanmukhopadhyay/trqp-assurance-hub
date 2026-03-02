# Changelog

All notable changes to this repository will be documented in this file.

## Unreleased

- (nothing yet)



## v0.4.3 (2026-03-02)

### Fixed
- CI: markdown lint now uses a repo-level `.markdownlint.yml` configuration to reduce false negatives for spec-style docs.
- Combined assurance smoke: aligned manifest schema with generator output so validation passes consistently.

### Added
- Schema/manifest contract hardening to support deterministic automation in downstream tooling.


## v0.4.2

### Added
- Program playbook (`docs/PLAYBOOK.md`) and operator runbook (`docs/OPERATOR_RUNBOOK.md`) to make adoption and combined assurance flows legible for non-technical stakeholders.

### Changed
- Updated documentation index and README to point to the playbook and runbook.
- Updated compatibility matrix with supported version pairings for this release line.



## v0.4.1

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
