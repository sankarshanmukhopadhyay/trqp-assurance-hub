---
layout: default
title: "TSAM — Trust Systems Assurance Method"
nav_order: 3
permalink: /tsam/
---

# TSAM — Trust Systems Assurance Method

The **Trust Systems Assurance Method (TSAM)** is a registry-agnostic and protocol-agnostic methodology for designing, assessing, operating, and evolving **trust-bearing distributed systems**.

TSAM binds five concerns into one assurance architecture:

1. **Governance Semantics**
2. **Assurance Levels**
3. **Conformance Verification**
4. **Runtime Integrity Controls**
5. **Evidence & Observability**

Its purpose is to make trust-system claims **testable, observable, reviewable, and maintainable under change**.

TSAM is **not a standard** and **not a certification programme**. It is a method for converting governance and assurance intent into explicit claims, controls, verification pathways, runtime protections, and evidence that another party can inspect.

This page is the canonical reader-facing introduction to TSAM. Detailed assurance profiles, control catalogues, schemas, examples, and repository-specific implementation material remain authoritative in their existing locations.

## Why TSAM exists

Trust-bearing systems routinely make claims such as:

- this registry is authoritative for a declared scope;
- this implementation conforms to a protocol or profile;
- this delegation is valid;
- this evidence is current;
- this runtime is operating under the expected controls;
- this assurance conclusion can still be relied upon.

Those claims become fragile when governance, implementation, verification, and evidence are designed independently.

A passing test suite alone does not establish:

- that the tested requirements came from the correct authority;
- that the controls correspond to the claimed assurance level;
- that runtime conditions match the tested assumptions;
- that evidence is current, complete, and attributable;
- that a later material change has not invalidated the conclusion.

TSAM therefore treats assurance as a **coherent system**, not as a report produced at the end of implementation.

```text
governance intent
        ↓
assurance claim
        ↓
control requirement
        ↓
verification procedure
        ↓
runtime integrity
        ↓
machine-verifiable evidence
        ↓
assurance conclusion
        ↓
change / invalidation / reassessment
```

## The five TSAM layers

A TSAM-aligned implementation must preserve coherence across all five layers even when they are distributed across repositories, organizations, or tooling.

### 1. Governance Semantics

Governance Semantics defines the meaning of the system being assured.

It should establish enough normative context for an independent implementer or verifier to determine:

- terminology;
- roles and decision rights;
- authority and delegation;
- lifecycle semantics;
- policy obligations;
- revocation or withdrawal behavior;
- scope and applicability;
- responsibility for risk acceptance and change.

Without this layer, a verifier may be able to test software behavior without knowing whether the behavior corresponds to the intended governance proposition.

### 2. Assurance Levels

Assurance Levels define **what must be true** for a declared level of assurance.

A useful level is not a decorative label such as "high assurance." It should identify:

- required claims;
- required controls;
- required verification;
- required evidence;
- applicable independence expectations;
- upgrade requirements from lower levels.

TSAM requires explicit and testable criteria and an identifiable evidence delta between levels.

### 3. Conformance Verification

Conformance Verification defines how relevant claims are tested.

Verification may include:

- protocol or schema conformance;
- contract tests;
- policy validation;
- negative and adversarial tests;
- replay or deterministic comparison;
- independent assessment;
- inspection of required evidence.

At least one meaningful verification pathway should exist for each material assurance claim or level.

Verification should be capable of falsifying a claim, not merely demonstrating that a happy path executes.

### 4. Runtime Integrity Controls

Runtime Integrity Controls address the fact that an implementation can conform in a test environment and still fail operationally.

Controls are selected according to the threat model and deployment posture and may address:

- authentication and authorization;
- key and secret management;
- protected signing;
- software and supply-chain integrity;
- configuration integrity;
- deployment controls;
- segregation of duties;
- availability and failure containment;
- change management;
- revocation enforcement;
- runtime policy integrity.

TSAM does not mandate one technology stack. It requires that runtime controls be proportionate to the system's assurance claims and risk.

### 5. Evidence & Observability

Evidence & Observability defines how assurance claims remain inspectable.

Evidence can include:

- conformance results;
- signed or integrity-bound attestations;
- test artifacts;
- build provenance;
- runtime observations;
- policy and configuration versions;
- change events;
- revocation state;
- audit records;
- evidence-bundle manifests.

Evidence should be machine-verifiable where feasible and reviewable by an independent verifier.

A TSAM implementation should make the relationship between **claim → control → evidence → verification result** explicit.

## Core assurance chain

The smallest useful TSAM reasoning chain is:

```text
claim
  ↓
control
  ↓
verification proposition
  ↓
test / observation
  ↓
evidence
  ↓
assurance conclusion
```

For example:

```text
Claim:
A revoked registry authorization cannot continue to authorize future use.

Control:
The runtime must consult current authorization/revocation state.

Verification proposition:
After revocation becomes effective, an otherwise valid request using the
revoked authorization is denied.

Evidence:
Version-bound test result + target identity + policy/state provenance.

Conclusion:
PASS only for the evaluated scope and evidence state.
```

This structure prevents a common assurance failure: treating a control description, an implementation assertion, or a green CI run as if it were independently sufficient proof.

## Core requirements

A TSAM-aligned system should, at minimum:

1. define explicit assurance claims or levels with normative, testable criteria;
2. bind those claims to controls that can be independently evaluated;
3. provide meaningful conformance-verification pathways;
4. define runtime-integrity controls proportional to risk;
5. produce machine-verifiable evidence artifacts for required claims;
6. keep missing, stale, contradictory, or unavailable evidence distinguishable from PASS;
7. record enough source/version provenance to reproduce the basis of the conclusion; and
8. define how change can invalidate, preserve, or require reassessment of assurance.

## How to implement TSAM

TSAM is intentionally architecture-neutral. A team does not need the TRQP Stack to implement it.

### Minimum viable TSAM implementation

A minimum useful implementation should establish:

1. **System scope** — what system, service, registry, directory, protocol implementation, or trust relationship is being assured.
2. **Authority and governance semantics** — who defines the obligations and which source is authoritative.
3. **Assurance claims** — what relying parties are expected to be able to rely upon.
4. **Controls** — what implementation or operational mechanisms are intended to make each claim true.
5. **Verification** — how each material claim can be tested or independently examined.
6. **Evidence** — what artifacts demonstrate the result and how they are bound to target, version, and time.
7. **Conclusion semantics** — how PASS, FAIL, indeterminate, unavailable, or not-applicable conditions are represented.
8. **Change rules** — which changes invalidate evidence or require reassessment.

This can initially be implemented with documented controls, deterministic tests, and a machine-readable evidence manifest.

### Repeatable implementation

A repeatable TSAM implementation should add:

- defined assurance levels or profiles;
- machine-readable requirement catalogues;
- stable control identifiers;
- schema-validated evidence contracts;
- negative and boundary tests;
- reproducible verification workflows;
- evidence bundles with source and target provenance;
- explicit lifecycle state;
- documented upgrade paths between assurance levels.

### Mature implementation

A mature implementation should additionally support:

- independent or independently reproducible verification where required;
- evidence freshness and validity rules;
- material-change detection;
- bounded reassessment where justified;
- fail-safe handling when impact is unknown;
- assurance supersession rather than historical rewriting;
- compositional profile assurance;
- public or relying-party assurance summaries;
- compatibility and version-bound interoperability evidence;
- explicit human judgment where automation cannot legitimately make the final governance decision.

## Assurance under change

TSAM treats assurance as conditional on the circumstances and evidence under which it was produced.

A useful lifecycle is:

```text
known assurance state
        ↓
change event
        ↓
materiality / impact assessment
        ↓
preserve | invalidate | reassess
        ↓
required verification
        ↓
new evidence
        ↓
recomposed assurance conclusion
        ↓
supersession lineage
```

A previous PASS should not silently remain current after a material change to:

- the target implementation;
- a governing specification or profile;
- policy;
- authority;
- evidence;
- security posture;
- schemas or semantic dependencies;
- relevant component compatibility.

Where impact is unknown, the system should expose that uncertainty rather than optimistically preserving assurance.

Historical evidence remains historical evidence; it should not be rewritten to look as though it was produced under later conditions.

## Profiles and composability

A TSAM implementation may evaluate a core protocol plus one or more ecosystem, deployment, or assurance profiles.

The governing principle is:

> **Profile assurance extends underlying assurance; it does not redefine the authority it depends on.**

A compositional result should preserve independent dimensions rather than flattening them into one opaque "trusted" boolean.

For example:

```text
core protocol conformance
        +
ecosystem profile conformance
        +
operational/security posture
        +
authority/evidence conditions
        ↓
bounded assurance result
```

Each source should retain its own authority. The assurance layer derives a result from those sources; it does not become the source specification.

## Evidence states and indeterminacy

TSAM requires evidence state to remain visible.

Important distinctions include:

- verified;
- failed;
- missing;
- stale;
- unavailable;
- contradictory;
- not applicable;
- not implemented;
- indeterminate.

An implementation should not convert:

```text
no evidence of failure
```

into:

```text
evidence of success
```

This is especially important when assurance results are consumed by automated systems or relying parties that may otherwise treat a boolean output as authoritative.

## The TRQP Stack as a worked implementation

The TRQP Assurance Hub and related TRQP repositories provide a substantial **TSAM-aligned proving environment**.

They demonstrate patterns such as:

- explicit assurance levels;
- conformance and security/privacy evidence from separate producers;
- evidence aggregation without collapsing producer authority;
- profile-aware assurance;
- reproducible evidence bundles;
- deterministic replay;
- missing-evidence and fail-closed semantics;
- lifecycle invalidation and reassessment;
- coordinated compatibility tuples;
- supersession and preserved historical release evidence;
- public assurance summaries.

The implementation flow is approximately:

```text
governing protocol / profile / semantic sources
        ↓
conformance + posture propositions
        ↓
independently owned verification/evidence producers
        ↓
Assurance Hub composition
        ↓
machine-readable evidence bundle
        ↓
bounded assurance decision
        ↓
relying-party / assessor / procurement review
```

**TSAM is not TRQP.** TRQP is one concrete and comparatively mature implementation environment in which TSAM concepts have been exercised. Other trust systems can implement TSAM using different protocols, repositories, tools, and controls.

## Relationship to TRACE

TSAM can be used independently, but it has a defined architectural relationship with **TRACE (Trust, Risk, Architecture & Conformance Evaluation)**.

- **TRACE defines governance analysis:** what must be governed, where risk or authority is concentrated, what redress or legitimacy requirements exist, and what gaps need remediation.
- **TSAM defines assurance implementation discipline:** how those requirements become assurance levels, controls, verification, runtime integrity, and evidence.

```text
TRACE
what must be governed, and why?
        ↓
governance / risk requirements
        ↓
TSAM
how is that intent encoded, tested, operated, and evidenced?
```

TRACE must not prescribe one technical enforcement mechanism. TSAM must not invent the governance legitimacy it is asked to assure.

See [TRACE and TSAM](../strategy/TRACE-TSAM-relationship.md) for the canonical architectural relationship maintained in this repository.

## Business and operational value

TSAM is intended to reduce ambiguity and repeated assurance reconstruction across implementation, procurement, operations, ecosystem onboarding, and audit.

| Common condition | TSAM contribution |
| --- | --- |
| "We comply" is a narrative assertion | Connects assurance claims to controls, verification, and evidence |
| Assurance is a point-in-time report | Adds evidence validity, change, invalidation, reassessment, and supersession semantics |
| Different parties use different meanings of "high assurance" | Requires defined, testable assurance levels or profiles |
| Auditors reconstruct evidence after the fact | Makes evidence production part of the operating architecture |
| A green test suite is treated as sufficient assurance | Preserves governance authority, runtime posture, provenance, and evidence state |
| Component or profile changes silently invalidate assumptions | Makes material change and reassessment first-class |
| Ecosystem participants cannot compare assurance claims | Provides shared claim/evidence structures and version-bound profiles |
| Missing evidence is treated optimistically | Keeps missing or indeterminate evidence explicit |
| Procurement asks for broad trust claims | Enables bounded requirements for evidence, conformance, lifecycle, and assurance level |

The practical value is therefore not a generic promise that a system is "more trustworthy." TSAM aims to **reduce the cost of proving assurance, reduce the cost of maintaining that assurance under change, and make reliance decisions more inspectable and reproducible.**

Actual commercial, regulatory, safety, or operational outcomes depend on the adopting system and must be established with deployment-specific evidence.

## Typical adoption contexts

TSAM is applicable where a relying party needs more than an implementation's self-description, including:

- ecosystem or registry onboarding;
- public-sector authoritative directories;
- supply-chain participant registries;
- content-authenticity verifier registries;
- AI-agent service registries;
- procurement of trust-bearing infrastructure;
- cross-domain recognition and interoperability;
- systems where revocation, evidence freshness, or authority provenance materially affect reliance.

The Hub's [business use-case library](../use-cases/README.md) illustrates several of these patterns in the TRQP context.

## What TSAM does not claim

TSAM is not:

- a universal certification scheme;
- an accreditation authority;
- a replacement for legal, regulatory, or institutional authority;
- a guarantee that a system is safe because its schemas validate;
- a requirement to centralize assurance in one repository or service;
- an assertion that one assurance level is appropriate for every risk context;
- a substitute for independent assessment where independence is required.

A TSAM result is bounded by its scope, evidence, authority sources, versions, lifecycle state, and declared limitations.

## Normative language and conformance

This repository uses the key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** as described in RFC 2119 and RFC 8174.

Detailed TSAM principles and layer requirements remain authoritative in the linked supporting documents. A project should not claim TSAM alignment merely because it uses the terminology; alignment requires demonstrable coherence across the relevant layers and evidence for material claims.

## Implementation and reference links

- [TSAM conceptual architecture](architecture.md)
- [TSAM layers](layers.md)
- [TSAM principles](principles.md)
- [TSAM mapping to this repository](mapping-repo.md)
- [TRACE ↔ TSAM relationship](../strategy/TRACE-TSAM-relationship.md)
- [Assurance levels](../guides/assurance-levels.md)
- [Evidence artifacts and expectations](../guides/evidence-artifacts.md)
- [End-to-end assurance execution](../guides/end-to-end-assurance.md)
- [Combined assurance guide](../guides/combined-assurance.md)
- [Machine-readable assurance profiles](../guides/machine-readable-assurance-profiles.md)
- [Public assurance publication](../guides/public-assurance-publication.md)
- [Business use cases](../use-cases/README.md)
- [Adoption kit](../adoption/README.md)

## In one sentence

> **TSAM turns trust-system assurance from a point-in-time assertion into a lifecycle of explicit claims, testable controls, reproducible evidence, and bounded conclusions that remain accountable under change.**
