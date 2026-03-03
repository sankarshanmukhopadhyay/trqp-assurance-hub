# GRID ↔ GTR crosswalk

This repository treats GRID as an implementation pattern that can be aligned with the UN/CEFACT Global Trust Registry (GTR) work.

## Why this crosswalk exists

- TRQP provides a query protocol for authoritative data from trust registries.
- GRID/GTR describe a **global directory** model for authoritative registrars.

This crosswalk highlights field and lifecycle correspondences.

## References

- UN/CEFACT GTR / GRID repository: https://un.opensource.unicc.org/unece/uncefact/gtr/
- GTR issue discussing GRID: https://opensource.unicc.org/un/unece/uncefact/gtr/-/issues/1
- TRQP specification: https://trustoverip.github.io/tswg-trust-registry-protocol/
- EBSI Trusted Issuers Registry / Trusted Entity Registry APIs: https://hub.ebsi.eu/apis/pilot/trusted-issuers-registry

## High-level correspondences

| Concept | GRID artifact | TRQP Assurance Hub artifact |
|---|---|---|
| Registrar identity | Registrar listing | `registrar.schema.json` |
| Listing status | Status feed entry | `grid-status-feed.schema.json` |
| Eligibility rules | Directory policy | `grid-assurance-mapping.md` |
| Auditability | Evidence bundle references | `assurance` object in registrar listing |

This is informative guidance; deployments MUST define their own policies and cryptographic proof formats.

## UNTP DIA considerations

If GRID implementations use UNTP Digital Identity Anchor (DIA) and Identity Resolver (IDR) patterns, assessments MUST treat GRID as a composite trust system (directory governance + publication integrity + identity anchoring). SAD-1 supports this via the `identity_anchor` extension and vendored DIA JSON-LD context.
