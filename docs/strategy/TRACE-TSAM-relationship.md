# TRACE and TSAM
## Governance Lens and Assurance Spine

## 1. Status and Normative Language

This document defines the architectural relationship between TRACE and TSAM.

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, and “MAY” in this document are to be interpreted as described in RFC 2119 and RFC 8174.

This document is architectural in scope and applies across repositories and implementation artifacts.

Machine-readable companion artifacts:

- Compliance matrix (YAML): `docs/strategy/trace-tsam-compliance-matrix.yaml`
- DPI AI annex templates: see Section 11 and the DPI AI Governance Lab repository.

## 2. Conceptual Separation

TRACE and TSAM operate at distinct abstraction layers.

Implementations adopting both constructs MUST preserve this separation.

- TRACE defines governance analysis.
- TSAM defines assurance implementation discipline.

TRACE MUST NOT prescribe technical enforcement mechanisms.
TSAM MUST NOT redefine governance legitimacy principles.

Collapsing these concerns introduces architectural ambiguity and interpretive drift.

## 3. TRACE — Structural Trust Analysis Layer

TRACE defines the normative governance lens for trust-bearing systems.

TRACE MUST:

- Identify risk concentration and delegation boundaries
- Define legitimacy thresholds
- Define accountability expectations
- Define redress requirements
- Identify systemic externalities

TRACE MAY evolve as governance theory or institutional context evolves.

TRACE artifacts SHOULD inform risk-tier classification and policy intent.

TRACE does not define control mappings, runtime enforcement, or verification workflows.

TRACE answers:

**What MUST be governed, and why?**

## 4. TSAM — Assurance Engineering Layer

TSAM (Trust Systems Assurance Method) defines the operational method for binding governance intent to enforceable system properties.

A TSAM-aligned implementation MUST define and maintain coherence across five layers:

1. Governance Semantics
2. Assurance Levels
3. Conformance Verification
4. Runtime Integrity Controls
5. Evidence & Observability

Each layer MUST reinforce the others. Isolation between layers introduces assurance gaps.

A TSAM-aligned system MUST:

- Define explicit assurance tiers
- Bind assurance tiers to testable controls
- Provide independent conformance verification pathways
- Implement runtime integrity controls appropriate to system risk
- Produce machine-verifiable evidence artifacts

TSAM does not define normative legitimacy criteria.

TSAM answers:

**How MUST governance intent be encoded, tested, and evidenced?**

## 5. Binding TRACE to TSAM

Where both TRACE and TSAM are adopted, the following conditions MUST hold:

1. TRACE risk classifications MUST inform TSAM assurance tier definitions.
2. TRACE-identified delegation thresholds MUST influence TSAM runtime integrity requirements.
3. TRACE redress requirements MUST be instantiated within TSAM governance semantics and evidence layers.
4. TSAM conformance artifacts MUST be capable of demonstrating compliance with TRACE-informed constraints.

TRACE findings that are not instantiated within TSAM assurance or runtime layers SHALL be considered analytically incomplete.

TSAM implementations that do not reflect TRACE-informed risk posture SHALL be considered normatively under-specified.

## 6. DPI AI Systems — Forward Reference Alignment

Digital Public Infrastructure (DPI) AI systems introduce additional scale, delegation, and institutional risk.

In DPI AI contexts:

TRACE MUST define:

- AI risk tiers
- Delegated agent boundaries
- Institutional accountability structures
- Redress and appeal mechanisms
- Cross-agency interoperability risk

TSAM MUST then instantiate these requirements as:

- Assurance level thresholds for AI systems
- Conformance test suites for model evaluation and policy compliance
- Runtime logging and decision traceability controls
- Supply-chain integrity requirements for model artifacts
- Evidence retention and auditability constraints

DPI AI packs SHOULD:

- Explicitly reference TRACE-derived risk categories
- Bind those categories to TSAM assurance tiers
- Provide machine-readable mappings between risk classification and control requirements

Failure to bind DPI AI governance semantics to TSAM runtime and evidence layers SHALL result in policy-only governance without enforceable accountability.

## 7. Architectural Implications

TRACE and TSAM together create a two-layer discipline:

- Layer 1 — Normative Orientation (TRACE)
- Layer 2 — Operational Enforcement (TSAM)

A DPI AI system claiming trustworthiness MUST demonstrate compliance at both layers.

Governance without enforcement SHALL be considered symbolic.
Enforcement without normative orientation SHALL be considered legitimacy-deficient.

## 8. Long-Term Evolution

TRACE MAY evolve as societal risk definitions and institutional legitimacy models evolve.

TSAM MUST remain stable as an assurance machinery layer capable of instantiating evolving governance requirements.

Repositories implementing TSAM SHOULD maintain forward compatibility with evolving TRACE classifications without requiring structural redesign.

## 9. Summary

TRACE expands the definition of what must be governed.
TSAM constrains how governance MUST be instantiated.

Together they convert trust from policy narrative into engineered property.

---

## 10. TRACE → TSAM Compliance Matrix

The following matrix defines the REQUIRED binding between TRACE analytical axes and TSAM assurance layers.

A system adopting TRACE and TSAM SHALL NOT claim full alignment unless each TRACE axis is instantiated across all five TSAM layers.

Failure to instantiate a TRACE axis across layers SHALL constitute partial compliance and MUST be explicitly documented.

| TRACE Axis | Governance Semantics | Assurance Levels | Conformance Verification | Runtime Integrity Controls | Evidence & Observability |
|-------------|---------------------|------------------|--------------------------|----------------------------|--------------------------|
| Risk Concentration | MUST define affected roles and impact domains | MUST reflect elevated tier where concentration exceeds threshold | MUST include tests validating role separation and control enforcement | MUST implement isolation and least-privilege mechanisms | MUST log access and decision boundaries |
| Delegation & Agency | MUST define delegation boundaries and authority limits | MUST escalate tier where automated delegation expands | MUST test override, appeal, and human-in-loop workflows | MUST enforce decision traceability and authority validation | MUST produce decision lineage artifacts |
| Legitimacy | MUST define institutional authority and scope | MUST align tier with public impact exposure | MUST validate policy enforcement consistency | SHOULD implement policy integrity protections | MUST retain auditable policy change records |
| Redress | MUST define appeal and remediation pathways | MUST require redress workflows at defined tiers | MUST test appeal execution and rollback mechanisms | MUST protect audit logs from tampering | MUST preserve redress outcome artifacts |
| Systemic Externality | MUST define cross-system dependency assumptions | SHOULD elevate tier for systemic risk exposure | SHOULD validate interoperability and failure containment | MUST implement resilience and containment controls | MUST capture cross-system interaction telemetry |

See `docs/strategy/trace-tsam-compliance-matrix.yaml` for the machine-readable form of these bindings.

---

## 11. DPI AI Annex Template

DPI AI packs adopting TRACE and TSAM SHOULD include a DPI AI annex aligned to this spine.

Template location (recommended):

- DPI AI Governance Lab: `docs/annexes/dpi-ai-trace-tsam-annex.md`
- DPI AI Governance Lab: `docs/annexes/dpi-ai-trace-tsam-annex.yaml`

### DPI AI TRACE–TSAM Annex

#### 1. System Scope

- AI System Name:
- Deployment Context:
- Public Impact Domain:
- Delegation Level (Human-in-loop / Human-on-loop / Fully delegated):

#### 2. TRACE Risk Classification

##### 2.1 Risk Concentration
- Impact scope:
- Affected population:
- Institutional exposure:

##### 2.2 Delegation & Agency
- Delegated decision boundaries:
- Override mechanisms:
- Escalation pathways:

##### 2.3 Legitimacy
- Authorizing statute or mandate:
- Policy basis:
- Institutional accountability structure:

##### 2.4 Redress
- Appeal pathway:
- Remediation timeline:
- Responsible authority:

##### 2.5 Systemic Externality
- Cross-agency dependencies:
- Model dependency chains:
- External data reliance:

#### 3. TSAM Instantiation

##### 3.1 Governance Semantics
Describe how the above TRACE classifications are encoded in policy artifacts.

##### 3.2 Assurance Level
- Declared TSAM Assurance Tier:
- Justification:
- Required evidence delta (if upgrade from lower tier):

##### 3.3 Conformance Verification
- Test suites executed:
- Independent verification entity:
- Results summary:

##### 3.4 Runtime Integrity Controls
- Zero Trust posture:
- Model supply-chain integrity controls:
- Logging and monitoring architecture:
- API security posture:

##### 3.5 Evidence & Observability
- Decision trace artifacts:
- Model lineage artifacts:
- Redress records:
- Telemetry retention policy:

#### 4. Compliance Declaration

The implementing authority SHALL declare:

- TRACE axes have been instantiated across all TSAM layers.
- Conformance artifacts are reproducible.
- Evidence artifacts are retained for independent audit.

Non-instantiated axes MUST be documented with justification.

---

## 12. Repository Placement

Canonical source of truth:

- TRQP Assurance Hub: `docs/strategy/TRACE-TSAM-relationship.md`

Mirrors:

- DPI AI Governance Lab: include DPI AI annex templates and a short pointer to the canonical doc.
- TRQP Conformance Suite: include a short pointer to the canonical doc in the docs set.
- TRQP-TSPP: include a short pointer to the canonical doc in the docs set.

Repositories MUST NOT fork divergent versions of this document. Changes SHOULD be made in the canonical source and propagated as synchronized mirrors where required.
