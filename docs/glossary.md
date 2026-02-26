# Glossary

## Terms

- **Assurance Hub (this repo)**: the integration surface for onboarding, compatibility, shared schemas, and cross-repo routing.
- **Runner / Engine**: executes tests, produces evidence, enforces result format (e.g., Conformance Suite).
- **Profile Pack**: versioned requirements and test plans (e.g., TSPP assurance profiles).
- **Artifact**: a durable, reviewable object produced by an assurance workflow (e.g., JSON evidence bundle, signed declaration).
- **Evidence bundle**: a machine-readable artifact containing structured results, provenance, and references supporting an assurance claim.
- **Combined Assurance Manifest (CAM)**: a small JSON document linking multiple evidence bundles to one build, target, and scope.
- **Independent verification**: evaluation by an assessor who is not the operator, with assessor identity recorded.
- **Remediation closure**: documented confirmation that a nonconformity has been addressed, linked to evidence.
- **Continuous monitoring**: ongoing collection and review of operational signals (logs/metrics/alerts) relevant to assurance claims.
- **Known-good version set**: validated version tuple across Hub, Conformance Suite, and TSPP.

## Assurance levels (AL1–AL4)

Canonical definitions live in `docs/guides/assurance-levels.md`.

- **AL1**: baseline conformance and hygiene backed by machine-readable evidence.
- **AL2**: evidence-bound self-attestation that reduces provenance ambiguity (e.g., manifests, explicit versioning).
- **AL3**: independently reviewed assurance, requiring control satisfaction, lifecycle assertions, and remediation closure evidence.
- **AL4**: high-consequence assurance with continuous monitoring, operationalized revocation/renewal, and time-bounded validity.

