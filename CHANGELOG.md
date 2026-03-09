# Changelog

## v0.7.1 (2026-03-06)

- Synchronize public-facing documentation and release metadata with TRQP-TSPP v0.5.1 and Assurance Hub v0.8.1.
- Retain Commit 3 and 4 tooling additions while removing stale version drift from README, roadmap, and crosswalk docs.
- Refresh release artifacts for the coordinated patch alignment release.

## v0.3.0 (2026-03-06)

### Added
- Add `--dry-run` flag to `cts/run.py` to validate inputs and list applicable tests without making HTTP requests.
- Add `--list-tests` flag to `cts/run.py` to print tests applicable to the selected profile and exit.
- Add `identifiers` block support to `sut.yaml` config, allowing real SUTs to override `authority_id`, `entity_id`, `subject_authority_id`, and `action` without modifying core test definitions.
- Add `QUICKSTART.md` at the repository root for fast onboarding of new implementers and operators.

### Fixed
- Fix JSONPath wildcard token indexing bug: `tokens.index(tok)` was replaced with `enumerate`-based tracking, preventing incorrect remainder slicing when a wildcard token appeared more than once in a path.

### Changed
- Refactor `cts/run.py` to extract `resolve_identifiers`, `apply_identifier_overrides`, and `list_tests` functions, reducing the size of `main()` and making each concern independently testable.
- Update `examples/sut.local.yaml.example` to document the `identifiers:` override block.
- Expand `SECURITY.md` with threat model references and reporting scope clarification.
- Synchronize roadmap, release notes, and version pins for the coordinated v0.3.0 release.

---

*Prior entries below reflect earlier releases in this series.*

## v0.7.0 (2026-03-06)

- Add machine-verifiable AL contract pin checking using a canonical assurance-level snapshot from the Assurance Hub.
- Synchronize cross-repo version references and public-facing release documentation for the AL3/AL4 hardening release train.

## v0.6.1 (2026-03-06)

### Fixed
- Reset per-test verdict override state in `cts/run.py` so an earlier ERROR does not leak into later passing cases.
- Write `checksums.json.generated_at` with a real timestamp instead of a null value.
- Synchronize README, roadmap, security guidance, and version pins for the current patch release.

### Changed
- Move the example SUT configuration to `examples/sut.local.yaml.example` and require generated local signing keys.
- Add explicit security warnings to the PoC service and example SUT configuration.
- Replace the placeholder GitHub Pages URL in the README with the production repository URL.

### Added
- Extend `.gitignore` to keep generated local SUT configs out of version control.

## v0.6.0 (2026-03-03)

### Added
- DeDi experimental artifact validation (vendored schemas plus validation script).
- `profiles/dedi_experimental.yaml` to enable DeDi profile runs.
- SAD-1 schemas for directory entry, publication manifest, and status feed.
- `scripts/validate_directory_artifacts.py` to validate authoritative directory artifacts as evidence.
- Documentation for directory artifact validation and how it complements API conformance testing.

### Changed
- Documentation updates linking DeDi profile to TRQP Assurance Hub experimental mapping.

## v0.4.4

### Added
- Optional GRID artifact schemas (registrar listing and status feed).
- GRID support documentation with external reference pointers.

### Changed
- Documentation crosswalk updated to reference GRID artifacts.

## v0.4.1

### Added
- `al-contract.json` to pin Assurance Level semantics to the canonical TRQP Assurance Hub definitions.
- `docs/templates/traceability-template.md` for implementer traceability (explicitly non-normative).

### Changed
- Clarified that this repo consumes canonical AL1 to AL4 semantics and does not redefine them.
- Updated documentation to reduce template noise.

## v0.4.0

### Added
- Conformance suite structure: profiles, requirements, tests, runner scaffolding, and evidence bundle patterns.
