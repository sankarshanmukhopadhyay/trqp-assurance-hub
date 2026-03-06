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


## Release readiness (v0.8.1)

- Cross-repo release references are synchronized to TSPP v0.5.1 and Conformance Suite v0.7.1.
- Compatibility matrix is updated to reflect the current supported TSPP ↔ CTS pairing used in the coordinated release train.
- AL3/AL4 combined assurance guidance remains the canonical anchor for downstream repos.

## Workstreams

### 1) Assurance levels and evidence bundles

- Expand and harden **AL3 / AL4** definitions and expectations.
- Maintain a **single evidence artifact vocabulary** (artifact kinds, required/optional by level).
- Add "how to audit" walkthroughs that map:
  - assurance level → evidence bundle → verification steps → expected outputs.
- Provide sample evidence bundles (minimal, typical, maximal) for implementers.

### 2) Combined-assurance workflow (cross-repo)

- Stabilize a **combined-assurance smoke workflow** that:
  - checks repo structure and doc invariants,
  - emits a **manifest**,
  - includes an **artifact checklist** aligned with the evidence matrix.
- Make the workflow usable in both:
  - the Hub repo itself, and
  - downstream adopters' repos (copy/paste friendly).

### 3) Schemas and machine readability

- Tighten schema validation and versioning policy for:
  - manifests,
  - conformance declarations,
  - evidence bundle descriptors.
- Add canonical JSON examples for each schema (happy path + error path).
- Publish "schema contract" guidance: what is stable, what may change, how to upgrade.

### 4) Documentation UX and navigation

- Keep the README as the "front door" and move deep operational content to `docs/`.
- Add a **docs index** that orients newcomers by role:
  - implementer,
  - auditor,
  - governance/assurance lead.
- Ensure all tables render cleanly on GitHub and avoid brittle formatting.

### 5) Interop testing and conformance alignment

- Align Hub artifacts with the TRQP Conformance Suite and TSPP expectations.
- Add cross-repo mapping documents:
  - Hub guidance ↔ CTS tests,
  - Hub evidence artifacts ↔ TSPP evidence bundle specs.
- Define a lightweight "interop profile" for repeatable demos and workshops.

### 6) Tooling and automation

- Expand `tools/generate-manifest.py` to support combined assurance manifest generation.
- Add schema validation CI step for `examples/` artifacts.

_Last updated: 2026-03-06_
