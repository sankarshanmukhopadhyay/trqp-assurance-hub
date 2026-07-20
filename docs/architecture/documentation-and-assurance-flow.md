---
layout: default
title: "Combined assurance composition and publication"
parent: Architecture
nav_order: 1
---

# Combined assurance composition and publication

The hub coordinates evidence from the other two repositories, but its core composition, policy-decision, conditional-assurance, and publication paths were not shown in one place. This diagram establishes those boundaries and makes non-pass outcomes auditable.

```mermaid
flowchart TB
    CTS[Conformance Suite evidence] --> Intake[Evidence intake and schema validation]
    TSPP[TSPP posture evidence] --> Intake
    Profile[Assurance profile and policy] --> Decision[Assurance decision engine]
    Intake --> Decision
    Registry[Compatibility and recognition registry] --> Decision
    Decision --> Status{Decision status}
    Status -- Pass --> Manifest[Combined assurance manifest]
    Status -- Conditional --> Conditions[Conditions and residual-risk record]
    Status -- Fail --> Findings[Failure findings and remediation evidence]
    Manifest --> Summary[Public and relying-party summaries]
    Conditions --> Summary
    Summary --> Directory[Directory or trust-registry publication]
    Directory --> RelyingParty[Relying-party evaluation]
    Findings --> Producer[Evidence producer remediation]
```

## Assurance interpretation

The diagram is normative only where it links to an identified specification, schema, profile, or executable test. Each transition should produce inspectable evidence: selected profile identifiers, test inputs, result artifacts, decision records, and publication manifests. Revocation or supersession must be represented by lifecycle data rather than by silently replacing prior evidence.
