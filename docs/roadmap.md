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

## Release readiness (v1.1.0)

- Cross-repo release references are synchronized to TSPP v0.7.1 and Conformance Suite v0.9.1.
- Compatibility matrix reflects the current supported pairing for the Operational Stack baseline.
- Combined-assurance smoke workflow and manifest schema are aligned and CI-validated.
- AL3/AL4 combined assurance guidance remains the canonical anchor for downstream repos.

## Workstreams

### 1) Assurance levels and evidence bundles

- ✅ AL3/AL4 definitions and expectations hardened with concrete evidence walkthroughs.
- ✅ Single evidence artifact vocabulary maintained in `docs/guides/evidence-artifacts.md`.
- ✅ Sample evidence bundles (AL3 and AL4) published under `examples/`.
- **Next:** Add a "minimal viable bundle" template for AL1/AL2 adopters who want a structured starting point without the full AL3/AL4 overhead.
- **Next:** Add "how to audit" companion notes to each AL bundle example — mapping evidence artifact → verifier check → expected outcome.

### 2) Combined-assurance workflow (cross-repo)

- ✅ Combined-assurance smoke workflow stable, CI-backed, and `workflow_dispatch`-capable.
- ✅ Manifest schema aligned with `generate-manifest.py` output.
- ✅ Artifact checklist aligned with evidence matrix.
- ✅ `generate-manifest.py --dry-run`: validates inputs and emits a preview to stdout without writing output files. CI step added to `quality.yml`.
- **Next:** Publish a copy/paste adopter template for the combined-assurance workflow, usable in downstream repos without Hub dependency.

### 3) Schemas and machine readability

- ✅ `tools/validate_examples.py` added; example drift from schemas now caught in CI.
- ✅ Schema-backed machine-readable assurance profiles for AL1–AL4.
- **Next:** Publish schema contract guidance: which fields are stable, which are extensible, and upgrade path between minor versions.
- **Next:** Add canonical JSON examples (error path) for the combined-assurance manifest schema.

### 4) Documentation UX and navigation

- ✅ Role-oriented docs index (`docs/index.md`) with operator / certifier / implementer / governance paths.
- ✅ README is the front door; deep operational content is in `docs/`.
- **Next:** Add a one-page "decision tree" to help adopters choose the right assurance level for their deployment context.

### 5) Interop testing and conformance alignment

- ✅ Ayra Trust Network crosswalk and submission checklist published.
- ✅ Interop demo profile available in `trqp-conformance-suite` and `TRQP-TSPP`.
- **Next:** Define a lightweight "interop profile" for repeatable workshop scenarios (fixed SUT, known inputs, expected verdicts).
- **Next:** Add a Hub ↔ CTS mapping table that cross-references Hub control IDs to CTS test IDs.

### 6) Tooling and automation

- ✅ `tools/generate-manifest.py` supports full combined-assurance manifest generation with CTS and TSPP report ingestion.
- ✅ Schema validation CI step in place.
- ✅ `generate-manifest.py --dry-run` CI step added to `quality.yml` — generation path is now verified on every push.
- **Next:** Add a `tools/check-freshness.py` script that reads `last_reviewed` frontmatter and flags docs past their SLA threshold in CI.
- **Next:** Extend `validate_examples.py` to cover AL evidence bundle examples (AL3/AL4 directories under `examples/`).

_Last updated: 2026-03-19_
