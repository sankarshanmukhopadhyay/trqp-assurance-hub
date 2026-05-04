# Roadmap

This roadmap is a *directional backlog* for the TRQP Assurance Hub. It captures intent and sequencing, not calendar promises.
Items move as upstream TRQP work evolves, implementer feedback lands, and cross-repo dependencies stabilize.

## Guiding principles

- **Operational first:** every addition should reduce adopter ambiguity and audit "interpretive dance".
- **Machine-operable by default:** prefer schemas, manifests, and CI checks over prose-only guidance.
- **Traceable:** link roadmap items to concrete artifacts (docs, schemas, tools, examples) and control IDs where relevant.
- **Composable:** keep the Hub focused on *assurance orchestration* and cross-repo integration, not protocol bikeshedding.

## Completed

- ✅ AL3/AL4 combined assurance walkthroughs added to `docs/guides/combined-assurance.md`
- ✅ Evidence artifact vocabulary table with schema and example cross-links
- ✅ `SECURITY.md` expanded with threat model references and reporting scope clarification
- ✅ Cross-repo version references synchronized for High-Assurance Hardening release
- ✅ Combined-assurance smoke workflow stabilized: emits signed manifest, validates against schema, supports both push and `workflow_dispatch`
- ✅ `tools/generate-manifest.py` extended to ingest CTS and TSPP report metadata directly
- ✅ Schema validation CI step added for `examples/` artifacts (`tools/validate_examples.py`)
- ✅ Role-oriented docs index published at `docs/index.md` (operator / certifier / implementer / governance paths)
- ✅ Operational Stack narrative published as a first-class architecture note (`docs/architecture/operational-stack.md`)
- ✅ Trust Registry reference service added for local discovery and demo flows
- ✅ Machine-readable assurance profiles for AL1–AL4 added with schema-backed validation
- ✅ Ayra Trust Network control mapping and submission checklist (`tools/ayra-mapping.md`)
- ✅ Compatibility matrix published at `docs/reference/compatibility-matrix.md`

## Release readiness and adoption focus

- Cross-repo release references are synchronized to TSPP v0.11.0 and Conformance Suite v1.3.0.
- Compatibility matrix reflects the current supported pairing for the Public Assurance and Adoption Readiness release.
- Combined-assurance manifest generation, public assurance summary generation, and validation tooling are aligned.
- AL3/AL4 guidance remains the canonical anchor for high-reliance adoption, auditability, and consumer impact evidence.

## Workstreams

### 1) Assurance levels and evidence bundles

- ✅ AL3/AL4 definitions and expectations hardened with concrete evidence walkthroughs.
- ✅ Single evidence artifact vocabulary maintained in `docs/guides/evidence-artifacts.md`.
- ✅ Sample evidence bundles (AL3 and AL4) published under `examples/`.
- ✅ AL1 and AL2 minimal viable bundle templates added under `examples/al1-evidence-bundle/` and `examples/al2-evidence-bundle/` with README, version-tuple, manifest, and operator declaration.
- ✅ `AUDIT_GUIDE.md` added to `examples/al3-evidence-bundle/` and `examples/al4-evidence-bundle/`, mapping each artifact to its verifier check and pass/fail criteria.

### 2) Combined-assurance workflow (cross-repo)

- ✅ Combined-assurance smoke workflow stable, CI-backed, and `workflow_dispatch`-capable.
- ✅ Manifest schema aligned with `generate-manifest.py` output.
- ✅ Artifact checklist aligned with evidence matrix.
- ✅ `generate-manifest.py --dry-run`: validates inputs and emits a preview to stdout without writing output files. CI step added to `quality.yml`.
- ✅ `templates/combined-assurance-workflow.yml`: copy/paste GitHub Actions workflow template covering CTS run, TSPP run, manifest generation, dry-run validation, and artifact upload.

### 3) Schemas and machine readability

- ✅ `tools/validate_examples.py` added; example drift from schemas now caught in CI.
- ✅ Schema-backed machine-readable assurance profiles for AL1–AL4.
- ✅ `schemas/CONTRACT.md`: stability tiers (Stable / Extensible / Experimental) with per-schema field table and AL contract pin upgrade policy.
- Planned: Add canonical JSON examples (error path) for the combined-assurance manifest schema.

### 4) Documentation UX and navigation

- ✅ Role-oriented docs index (`docs/index.md`) with operator / certifier / implementer / governance paths.
- ✅ README is the front door; deep operational content is in `docs/`.
- ✅ `docs/guides/al-decision-tree.md`: structured decision tree (consequence → external reliance → continuous operation) with AL selection quick reference and upgrade paths.

### 5) Interop testing and conformance alignment

- ✅ Ayra Trust Network crosswalk and submission checklist published.
- ✅ Interop demo profile available in `trqp-conformance-suite` and `TRQP-TSPP`.
- **Next:** Define a lightweight "interop profile" for repeatable workshop scenarios (fixed SUT, known inputs, expected verdicts).
- ✅ `docs/reference/hub-cts-crosswalk.md`: three-way mapping table (control → CTS test → TSPP requirement) with reverse indexes and coverage gap notes.

### 6) Tooling and automation

- ✅ `tools/generate-manifest.py` supports full combined-assurance manifest generation with CTS and TSPP report ingestion.
- ✅ Schema validation CI step in place.
- ✅ `generate-manifest.py --dry-run` CI step added to `quality.yml` — generation path is now verified on every push.
- **Next:** Add a `tools/check-freshness.py` script that reads `last_reviewed` frontmatter and flags docs past their SLA threshold in CI.
- ✅ `tools/validate_examples.py` extended to validate JSON files in all AL bundle directories (`examples/al*-evidence-bundle/`) against their paired schemas.

_Last updated: 2026-03-19_
