# Roadmap

This roadmap is a *directional backlog* for the TRQP Assurance Hub. It captures intent and sequencing, not calendar promises.
Items move as upstream TRQP work evolves, implementer feedback lands, and cross-repo dependencies stabilize.

## Guiding principles

- **Operational first:** every addition should reduce adopter ambiguity and audit “interpretive dance”.
- **Machine-operable by default:** prefer schemas, manifests, and CI checks over prose-only guidance.
- **Traceable:** link roadmap items to concrete artifacts (docs, schemas, tools, examples) and control IDs where relevant.
- **Composable:** keep the Hub focused on *assurance orchestration* and cross-repo integration, not protocol bikeshedding.

## Workstreams

### 1) Assurance levels and evidence bundles

- Expand and harden **AL3 / AL4** definitions and expectations.
- Maintain a **single evidence artifact vocabulary** (artifact kinds, required/optional by level).
- Add “how to audit” walkthroughs that map:
  - assurance level → evidence bundle → verification steps → expected outputs.
- Provide sample evidence bundles (minimal, typical, maximal) for implementers.

### 2) Combined-assurance workflow (cross-repo)

- Stabilize a **combined-assurance smoke workflow** that:
  - checks repo structure and doc invariants,
  - emits a **manifest**,
  - includes an **artifact checklist** aligned with the evidence matrix.
- Make the workflow usable in both:
  - the Hub repo itself, and
  - downstream adopters’ repos (copy/paste friendly).

### 3) Schemas and machine readability

- Tighten schema validation and versioning policy for:
  - manifests,
  - conformance declarations,
  - evidence bundle descriptors.
- Add canonical JSON examples for each schema (happy path + error path).
- Publish “schema contract” guidance: what is stable, what may change, how to upgrade.

### 4) Documentation UX and navigation

- Keep the README as the “front door” and move deep operational content to `docs/`.
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
- Define a lightweight “interop profile” for repeatable demos and workshops.

### 6) Tooling and automation

- Improve `tools/` scripts for:
  - generating manifests,
  - validating evidence bundle structure,
  - verifying schema conformance locally.
- Add consistent developer ergonomics:
  - Make targets / task runner,
  - pre-commit hooks (optional),
  - CI checks that fail fast with actionable errors.

### 7) Examples and reference implementations

- Expand `examples/` with realistic, end-to-end scenarios:
  - minimal adopter repo,
  - mature adopter repo,
  - audit-ready AL3/AL4 bundle.
- Include “expected outputs” for each example (manifest, validation report, checklist result).
### 6) TSAM consolidation (method layer)

- Treat TSAM as the **registry-agnostic** method layer that frames this repository and linked work (CTS, TSPP).
- Maintain TSAM documents under `docs/tsam/` as a stable reference:
  - definition, principles, layers, and repo mapping.
- Ensure AL definitions and evidence requirements remain consistent with TSAM principles.
- Add cross-repo pointers where TSAM concepts are implemented (informative).

## Near-term focus

This is the current best guess of the most leverage-positive sequence (subject to change):

1. ✅ **Lock AL3/AL4 artifact expectations** (vocabulary + matrix + examples).
   - Canonical definitions: `docs/guides/assurance-levels.md`
   - Matrix: `docs/guides/evidence-artifacts.md`
   - Examples: `examples/al3-evidence-bundle/`, `examples/al4-evidence-bundle/`
2. **Make combined-assurance workflow deterministic** (manifest + checklist emission).
3. **Ship schema examples and validation docs** (reduce implementer confusion).
4. ✅ **Improve docs navigation** (role-based index, fewer dead ends).

## How we will track progress

- Roadmap items should be converted into GitHub Issues with clear acceptance criteria.
- Each closed item should point to the commit, PR, or release note that landed it.
- If an item is blocked, document the dependency explicitly (upstream issue, spec decision, or repo coupling).

## Non-goals

- Redefining TRQP protocol semantics (handled upstream).
- Creating a general-purpose governance framework unrelated to TRQP assurance.
- Overfitting to a single ecosystem’s tooling or CI platform.


## Recently completed

- Cross-repo evidence bundle normalization:
  - CTS emits `bundle_descriptor.json` + `checksums.json` and publishes portable bundles via CI
  - TSPP packages posture evidence bundles (`bundle_descriptor.json` + `checksums.json` + `bundle.zip`) and publishes via CI
- Combined-assurance producer interface documentation:
  - Hub guide updated with concrete producer expectations and crosswalk links


## Completed

- ✅ AL1–AL4 canonical lock and cross-repo contract (`docs/guides/assurance-levels.md`, `al-contract.json`).


## Release readiness (v0.7.1)

- ✅ Security and correctness stabilization completed for workflow versions, security policy coverage, and repository hygiene.
- ✅ Public documentation, release notes, and cross-repo version pins synchronized for the patch release.

_Last updated: 2026-03-06_

## GRID readiness kernel

Status: **Done**

- Add GRID profile (md + machine-readable json)
- Add registrar listing and status feed schemas + examples
- Add assurance mapping, threat annex, verifier-first workflow
- Add crosswalk references to UN/CEFACT GTR/GRID and EBSI registry implementations


## SAD-1 readiness kernel (authoritative directories)

Status: **Done**

- Add SAD-1 profile (md + machine-readable json)
- Add generic directory entry, publication manifest, and status feed schemas + examples
- Add an end-to-end directory assurance workflow guide
- Add a strategy note framing TRQP as meta-assurance for authoritative directories
- Mark GRID as an instance profile implementing SAD-1

## UNTP DIA considerations

If GRID implementations use UNTP Digital Identity Anchor (DIA) and Identity Resolver (IDR) patterns, assessments MUST treat GRID as a composite trust system (directory governance + publication integrity + identity anchoring). SAD-1 supports this via the `identity_anchor` extension and vendored DIA JSON-LD context.

### Supply chain integrity

- Add stronger evidence patterns and scoring guidance for SBOM, provenance, and automated posture checks (TSPP-SCI aligned).
