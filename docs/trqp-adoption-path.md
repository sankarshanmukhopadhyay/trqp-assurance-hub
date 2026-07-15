# TRQP Adoption Path

The TRQP portfolio separates protocol definition, security posture, reference implementation, conformance execution, and assurance publication so that authority does not collapse into one repository.

```text
Read the TRQP protocol
    ↓
Select TSPP security and privacy posture
    ↓
Exercise a reference implementation
    ↓
Run the TRQP Conformance Suite
    ↓
Compose and publish evidence through the Assurance Hub
```

## This repository

`trqp-assurance-hub` provides **assurance orchestration and publication** and produces **Combined Assurance Manifest**.

## Stack contracts

| Layer | Repository | Authority | Primary output |
|---|---|---|---|
| Protocol | `tswg-trust-registry-protocol` | Normative TRQP semantics | Protocol specification |
| Security profile | `TRQP-TSPP` | Security and privacy posture | Posture Report |
| Reference implementation | `cawg-trqp-verifier-refimpl` | Executable implementation pattern | Decision receipt and audit bundle |
| Conformance | `trqp-conformance-suite` | Executable protocol verification | Conformance Report |
| Assurance | `trqp-assurance-hub` | Evidence composition and publication | Combined Assurance Manifest |

## Adoption gate

An adopter should be able to identify the governing requirement, execute the documented validation, retain the resulting evidence, and determine which repository has authority over any failed control. Cross-stack use should pin versions or commit SHAs and record them in the evidence bundle.
