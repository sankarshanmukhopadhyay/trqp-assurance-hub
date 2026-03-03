# Changelog


## v0.6.0 (2026-03-03)

- Add SAD-1 (Sovereign Authoritative Directory) profile (md + json) to make directory evaluations portable across sovereign and non-sovereign implementations.
- Add SAD-1 schemas and examples for directory entry, publication manifest, and status feed.
- Add end-to-end directory assurance workflow guide and strategy note framing TRQP as meta-assurance for authoritative directories.
- Clarify GRID as an instance profile implementing SAD-1.

## Unreleased

- Add OpenSSF-aligned supply chain integrity evidence guidance (TSPP-SCI) and documentation cross-links.

- (nothing yet)
- Add UNTP DIA / IDR references and wire SAD-1 identity anchoring extension (vendored DIA JSON-LD context).
## v0.5.0

### Added
- GRID readiness kernel: profile + schemas + verifier workflow + threat annex
- Registrar listing schema and GRID status feed schema (+ examples)
- Crosswalk references to UN/CEFACT GTR/GRID and EBSI registry implementations

### Fixed
- Made `tools/control-catalog.json` valid JSON to keep validation trustworthy

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
