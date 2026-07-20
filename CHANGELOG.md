## v1.8.0

## 1.9.0 - 2026-07-20

- Added the shared machine-readable project-status contract and validation.
- Added coordinated end-to-end assurance evidence, traceability, and compatibility controls.
- Added material local assurance validation and adoption guidance.


- Publish the Operational Trust Stack Maturity Release for the coordinated Hub v1.8.0 / CTS v1.5.0 / TSPP v0.13.0 release tuple.
- Add `docs/governance/release-policy.md` to define patch, minor, maturity, and no-release thresholds.
- Add `docs/governance/change-intake.md` to require adoption value, evidence impact, validation impact, and cross-repo compatibility review before a change is release-worthy.
- Add `docs/release-validation.md` with the validation commands and release acceptance evidence expected for the maturity train.
- Add GitHub PR and release templates aligned to the maturity gate.
- Refresh README and roadmap language so the Hub is the canonical adoption front door for the Operational Trust Stack.

## v1.7.0

- Add TSMM/TIS Runtime Assurance Contract Pack for cross-repo assurance publication.
- Extend `schemas/combined-assurance-manifest.schema.json` with optional `tsmm_mapping` and `tis_artifacts` blocks.
- Extend `tools/generate-manifest.py` with CLI flags for TSMM authority/decision metadata and TIS artifact references.
- Add `docs/reference/tsmm-tis-runtime-assurance-contract.md` to define authority, delegation, scope, lifecycle, revocation, evidence, decision, and audit expectations.
- Add portfolio release-impact and drift-review records under `docs/governance/`.
- Refresh README and compatibility matrix for the coordinated Hub v1.7.0 / CTS v1.4.0 / TSPP v0.12.0 release tuple.
- Fix validation dependency hygiene by replacing the unavailable `requests==2.33.0` pin with `requests==2.32.5`.

## v1.6.1

- Extend the Combined Assurance Manifest schema with an optional `lifecycle` block covering target state, status feed URI, revocation support, publication SLA, and last-checked timestamp.
- Add lifecycle and revocation publication flags to `tools/generate-manifest.py`, with inference from TSPP report metadata where present.
- Extend public assurance summary generation and schema output so relying parties can see lifecycle status alongside conformance and posture status.
- Update combined assurance guidance and examples to treat lifecycle/revocation publication as part of safe relying-party use.

## v1.6.0

- Add Public Assurance Summary schema, generator, validator, examples, and operational-stack artifact.
- Add business use-case guides, adoption kit, procurement language, and consumer impact documentation.
- Refresh compatibility matrix for CTS v1.3.0 and TSPP v0.11.0.
- Remove stale current-release references from templates and examples.

## v1.5.0

- Enforce fail-closed identity checks in `tools/generate-manifest.py` so CTS and TSPP `run_id` / `target_id` values must align with the Combined Assurance Manifest build block.
- Add `tools/validate_operational_stack.py` and extend `tools/validate_examples.py` to validate the checked-in Operational Stack bundle for schema, identity, artifact existence, and `sha256` integrity.
- Regenerate the checked-in Operational Stack demo artifacts with consistent identifiers and current cross-repo versions.
- Refresh Hub docs, examples, and compatibility references for the hardened Operational Stack contract.

## v1.4.0

- Add `examples/al1-evidence-bundle/` and `examples/al2-evidence-bundle/`: minimal viable bundle templates with README (what to produce, what to omit, toolchain invocation), `version-tuple.json`, `combined-assurance-manifest.json`, and `operator-declaration.md`.
- Add `examples/al3-evidence-bundle/AUDIT_GUIDE.md` and `examples/al4-evidence-bundle/AUDIT_GUIDE.md`: per-artifact verifier checklists mapping evidence artifact → check → expected outcome → failure signal, with AL-level pass criteria.
- Add `templates/combined-assurance-workflow.yml`: copy/paste GitHub Actions workflow template for the combined-assurance workflow, covering CTS run, TSPP run, manifest generation, dry-run validation, and artifact upload. No Hub dependency required.
- Add `schemas/CONTRACT.md`: schema stability contract with per-schema field stability tiers and AL contract pin migration policy.
- Add `docs/guides/al-decision-tree.md`: structured decision tree for AL selection (consequence → external reliance → continuous operation) with quick reference table and upgrade path guidance.
- Add `docs/reference/hub-cts-crosswalk.md`: three-way mapping table from Hub control IDs to CTS test IDs and TSPP requirement IDs, with reverse indexes and coverage gap notes. CI-validated via `tools/validate_crosswalk.py`.
- Extend `tools/validate_examples.py` to validate JSON files in all AL evidence bundle directories (`examples/al*-evidence-bundle/`) against their paired schemas.
- Update cross-repo version references to TRQP-TSPP v0.10.0 and Conformance Suite v1.2.0.

## v1.3.0

- Add `--dry-run` flag to `tools/generate-manifest.py`: validates all inputs and emits a manifest preview to stdout without writing any output files. Schema validation (via `--schema`) is still executed in dry-run mode. Exit 0 on success, non-zero on any validation failure. Added as a CI step in `quality.yml` on every push.
- Add `generated_at` field to the metadata JSON written by `tools/run_operational_stack.py`, completing the operational stack audit trail.
- Update `quality.yml` to include a `validate` job that runs `tools/validate_examples.py`, `scripts/doc_tests.py`, and `generate-manifest.py --dry-run` on every push and pull request.
- Synchronize downstream version references: TRQP-TSPP v0.9.0, Conformance Suite v1.1.0.

## v1.2.0

- Added manifest summary metrics for posture, coverage, completeness, and assurance tier.
- Refreshed Operational Trust Stack documentation and synchronized downstream versions.

## v1.1.0

- Add the Operational Stack baseline with a new `Run the Stack` guide, compatibility matrix, and demo example set.
- Add `tools/run_operational_stack.py` and extend `tools/generate-manifest.py` to ingest CTS and TSPP report metadata directly.
- Add an Operational Stack GitHub Actions smoke workflow and update the combined assurance manifest schema with shared `run_id` and `target_id` fields.

# Changelog

## Unreleased

### Changed

- Establishes a Tier 1 flagship repository contract with explicit authority boundaries, machine-readable portfolio metadata, a common validation entry point, citation metadata, and a documented TRQP adoption path.
- Adds CI enforcement for required governance, adoption, evidence, and documentation artifacts without creating a new release.

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
