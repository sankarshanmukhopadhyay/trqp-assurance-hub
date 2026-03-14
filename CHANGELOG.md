## v1.1.0

- Add the Operational Stack baseline with a new `Run the Stack` guide, compatibility matrix, and demo example set.
- Add `tools/run_operational_stack.py` and extend `tools/generate-manifest.py` to ingest CTS and TSPP report metadata directly.
- Add an Operational Stack GitHub Actions smoke workflow and update the combined assurance manifest schema with shared `run_id` and `target_id` fields.

# Changelog

## v1.0.0 (2026-03-10)

### Fixed
- Align `README.md` version references with `VERSION` file: README declared v0.8.1 while
  `VERSION` and `al-contract.json` already reflected v0.9.0 from the prior release.
- Update downstream release train reference in README to TSPP v0.6.0 · CTS v0.8.0.

### Added
- `tools/ayra-mapping.md`: end-to-end crosswalk from the five Assurance Hub canonical
  controls (TRQP-CTRL-01 through TRQP-CTRL-07) to Ayra Trust Network conformance
  requirements, evidence artifacts, and sufficiency notes per AL tier. Includes a
  three-tier submission checklist (Basic / Cross-Ecosystem / Sovereign).

## Cross-repo versions

| Repository | Version |
|---|---|
| TRQP-TSPP | v0.6.0 |
| Conformance Suite | v0.8.0 |
| Assurance Hub | v1.0.0 |

## v0.9.0 (2026-03-09)

### Fixed
- Align `schemas/combined-assurance-manifest.schema.json` with the actual output of
  `tools/generate-manifest.py`. The previous schema used a flat shape (`build_id`, `target`,
  `version_tuple` at root; `additionalProperties: false`) that did not match the richer nested
  structure the tool produces (`build: {build_id, target, commit, ci_run_url}`, `tools: {...}`,
  `generator: {...}`). The artifact items schema also blocked `produced_by`, `media_type`,
  `notes`, and `format`. This mismatch caused the `combined-assurance-smoke` CI to fail
  on every push to `main` when schema validation was invoked via `--schema`.
- Update `examples/combined-assurance-manifest.example.json` to match the corrected schema
  shape so `tools/validate_examples.py` passes cleanly.

### Added
- New `validate` job in `.github/workflows/quality.yml` that runs
  `tools/validate_examples.py` (example/schema conformance + cross-checks) and
  `scripts/doc_tests.py` (JSON/YAML parse hygiene, markdown internal links) on every push
  and pull request. Example drift from schemas is now caught in CI.

## v0.8.1 (2026-03-06)

- Synchronize public-facing documentation, release metadata, and compatibility guidance with TRQP-TSPP v0.5.1 and Conformance Suite v0.7.1.
- Update the known-good matrix to reflect the current supported CTS ↔ TSPP pairing after Commit 3 and 4 closure.
- Publish a clean patch release that closes remaining documentation drift from the hardening train.

## v0.2.0 (2026-03-06)

### Added
- Add AL3 combined assurance walkthrough to `docs/guides/combined-assurance.md`, including step-by-step evidence artifact production and independent review guidance.
- Add AL4 combined assurance walkthrough to `docs/guides/combined-assurance.md`, including continuous monitoring artifact requirements, operational attestation, and assessor method recording.
- Add evidence artifact vocabulary table to `docs/guides/combined-assurance.md` mapping AL requirements to concrete schemas and examples.

### Changed
- Expand `SECURITY.md` with threat model references covering `docs/grid-threat-annex.md`, canonical AL definitions, and reporting scope clarification distinguishing Hub guidance vulnerabilities from downstream operator issues.
- Synchronize roadmap, release notes, and version references for the coordinated v0.2.0 release (TSPP v0.5.0, CTS v0.3.0).

---

*Prior entries below reflect earlier releases in this series.*

## v0.8.0 (2026-03-06)

- Reaffirm the canonical AL1 to AL4 contract for the hardening release train used by downstream TSPP and CTS repositories.
- Synchronize roadmap, release, and README metadata with downstream version pins for TSPP v0.5.0 and CTS v0.7.0.

## v0.7.1 (2026-03-06)

### Fixed
- Remove committed Python bytecode from `tools/__pycache__/` and add a repository `.gitignore`.
- Standardize workflow action versions to supported releases for checkout, Python setup, and artifact upload.
- Synchronize README, roadmap, security guidance, and release metadata for the current patch release.

### Added
- Add a repository `SECURITY.md` clarifying the scope for tooling, guidance, schemas, and workflow reports.

## v0.7.0 (2026-03-03)

### Added
- DeDi experimental profile (markdown plus JSON) to support decentralized directory artifacts under the Hub assurance model.
- Vendor DeDi JSON Schemas (non-normative snapshot) under `schemas/dedi/` and add example artifacts under `examples/dedi/`.
- SAD-1 profile (markdown plus JSON) to make directory evaluations portable across sovereign and non-sovereign implementations.
- SAD-1 schemas and examples for directory entry, publication manifest, and status feed.
- End-to-end directory assurance workflow guide and strategy note framing TRQP as meta-assurance for authoritative directories.

### Changed
- Update public docs to explain DeDi mapping and experimental stability posture.
- Clarify GRID as an instance profile implementing SAD-1.

## v0.5.0

### Added
- GRID readiness kernel: profile, schemas, verifier workflow, and threat annex.
- Registrar listing schema and GRID status feed schema with examples.
- Crosswalk references to UN/CEFACT GTR/GRID and EBSI registry implementations.

### Fixed
- Made `tools/control-catalog.json` valid JSON to keep validation trustworthy.

## v0.4.1

### Added
- `al-contract.json` to provide a machine-readable contract for canonical AL1 to AL4 semantics, including the SHA-256 of the normative AL document.

### Changed
- Clarified normative status of `docs/guides/assurance-levels.md` for cross-repo consumption and audit stability.

## v0.4.0

### Added
- Candidate Trust Registry Assurance and Certification Baseline documentation pack (`docs/certification-baseline/`).
- Certification Attestation artifact (schema plus example) to bind assessor identity, scope, validity, and evidence references.
- Normative control framework fields in the control catalog.

### Changed
- Evidence artifacts matrix updated to include Certification Attestation.
- CI example cross-checks extended to cover certification attestation evidence references.
- README and TRQP alignment documentation updated to clarify the certification-baseline positioning.
