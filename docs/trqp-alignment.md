# Upstream TRQP RFE alignment

This repository is positioned as a **candidate Assurance Profile and Governance Hardening Layer** for the Trust over IP Trust Registry Query Protocol (TRQP).

The intent is not to redefine TRQP transport or endpoint semantics.
The intent is to make TRQP **operationally adoptable** by turning open questions into:

- **Profiles** (what must hold)
- **Artifacts** (what must be produced)
- **Evidence** (what can be independently verified)

Upstream issue list: <https://github.com/trustoverip/tswg-trust-registry-protocol/issues>

## What this repo contributes

The core contributions are:

- **Assurance level framing (AL1–AL4)** with explicit evidence artifact expectations.
- A **Combined Assurance Manifest** schema that binds conformance and posture evidence under a single build identifier.
- A **candidate assurance profile format** for publishing governance and assurance expectations in a machine-readable way.
- A pragmatic **operating model** (compatibility policy, issue routing, and “one product” onboarding across repos).

## What this repo does not try to solve

To avoid accidental scope-creep, this repo intentionally does **not** attempt to:

- Specify TRQP endpoint discovery mechanisms.
- Define transport extensibility roadmaps.
- Replace upstream protocol normative text.

Instead, it provides an execution-oriented layer that can be adopted today and referenced by upstream as a candidate profile.

## Mapping: RFEs → Hub artifacts

The mapping below is deliberately practical: it points to **concrete artifacts** that implementers can produce and verifiers can evaluate.

### 1) Security Profile Definitions (Minimal, Standard, High-Assurance)

**Coverage:** Direct.

How this repo helps:

- The evidence matrix in [`docs/guides/evidence-artifacts.md`](guides/evidence-artifacts.md) provides a tiered structure (AL1–AL4).
- The candidate profile format in [`docs/guides/assurance-profile.md`](guides/assurance-profile.md) provides a way to publish tier expectations.

Operational effect:

- Minimal/Standard/High-Assurance can be expressed as **profile IDs** or as AL bundles with explicit artifact requirements.

### 2) Clarify Recognition Relationship Modeling and Proofs

**Coverage:** Partial (governance hardening + evidence model).

How this repo helps:

- Provides a place to define and publish **recognition assertions** as auditable artifacts (candidate structure in the assurance profile).
- Provides the cross-run binding mechanism (Combined Assurance Manifest) so recognition claims can point to evidence.

Gap (deliberate):

- This repo does not yet define a full recognition graph model.
  The intended next increment is a lightweight **Recognition Assertion** artifact schema that can be signed and evidence-linked.

### 3) Define Baseline and High-Assurance Governance Metadata Profiles

**Coverage:** Strong alignment.

How this repo helps:

- Encodes governance expectations as **profile metadata** rather than prose-only guidance.
- Encourages stable identifiers, compatibility declarations, and evidence retention/redaction controls.

See:

- [`docs/guides/assurance-profile.md`](guides/assurance-profile.md)
- [`docs/policies/compatibility.md`](policies/compatibility.md)

### 4) Non-Functional Operational Guidance Appendix

**Coverage:** Indirect (operational guidance through artifacts).

How this repo helps:

- Provides operationally useful guidance via:
  - issue routing,
  - compatibility matrix,
  - evidence artifacts and provenance binding,
  - error state documentation.

See:

- [`docs/policies/issue-routing.md`](policies/issue-routing.md)
- [`docs/guides/error-states.md`](guides/error-states.md)

### 5) Optional Mapping Profile for Credential Ecosystem Integration

**Coverage:** Not implemented (yet).

How this repo can evolve:

- Add a **Mapping Profile** section to the assurance profile format that declares:
  - credential ecosystem assumptions,
  - mapping constraints,
  - interoperability commitments.

This is intentionally separated from protocol semantics.

### 6) Outline Transport Extensibility Roadmap

**Coverage:** No.

Reason:

- Transport extensibility is upstream protocol scope.
  This repo focuses on assurance, governance, and operational evidence.

### 7) Define TRQP Endpoint Discovery Convention

**Coverage:** Minimal (only as publishable metadata).

How this repo helps:

- The assurance profile can publish **discovery pointers** and capability descriptors.

What remains upstream:

- Normative endpoint discovery conventions and semantics.

### 8) Define Lifecycle Metadata and Revocation Query Semantics

**Coverage:** Partial (lifecycle metadata via evidence and governance).

How this repo helps:

- Encourages implementers to produce lifecycle and revocation-related evidence artifacts.
- Provides a place to publish lifecycle policy pointers and operational commitments.

What remains upstream:

- Protocol-level query semantics.

## Recommended next increments (to increase upstream usefulness)

These are “high leverage, low drama” additions that strengthen alignment without dragging the repo into transport-layer bikeshedding:

1. **Recognition Assertion artifact schema** (signable, evidence-linked).
2. **Lifecycle state model** (minimal state machine + evidence hooks) expressed as profile metadata.
3. **Mapping profile extension** for VC ecosystem integration (optional, external-facing).
