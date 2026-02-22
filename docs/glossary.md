# Glossary

## Terms

- **Assurance Hub (this repo)**: the integration surface for onboarding, compatibility, and shared schemas.
- **Runner / Engine**: executes tests, produces evidence, enforces result format (e.g., Conformance Suite).
- **Profile Pack**: versioned requirements and test plans (e.g., TSPP AL profiles).
- **Evidence bundle**: machine-readable artifact enabling audit and verification.
- **Combined Assurance Manifest**: small JSON document linking multiple evidence bundles to one build and target.
- **Known-good version set**: validated version tuple across Hub, Conformance Suite, and TSPP.

## Assurance levels (AL1–AL4)

AL1 and AL2 are implemented in TRQP-TSPP. AL3 and AL4 are reserved; this hub documents draft intent only.

- **AL1**: baseline internet hygiene.
- **AL2**: hardened posture for higher-value deployments.
- **AL3 (draft/reserved)**: higher assurance with stronger provenance and audit expectations.
- **AL4 (draft/reserved)**: critical assurance for high-consequence environments.
