# GRID support (optional)

The Conformance Suite can optionally validate the **shape** of GRID-style artifacts used by directory operators.

What is supported:
- JSON Schema validation of:
  - `schemas/registrar.schema.json`
  - `schemas/grid-status-feed.schema.json`

What is not supported (by design in the baseline runner):
- Signature verification / proof evaluation
- Policy eligibility decisions (AL mapping)
- Key discovery rules

References:
- UN/CEFACT GTR / GRID: https://un.opensource.unicc.org/unece/uncefact/gtr/
- EBSI Trusted Issuers Registry APIs: https://hub.ebsi.eu/apis/pilot/trusted-issuers-registry
- TRQP specification: https://trustoverip.github.io/tswg-trust-registry-protocol/

## UNTP DIA considerations

Where a directory uses UNTP Digital Identity Anchor (DIA) / Identity Resolver (IDR), conformance evidence SHOULD include DIA context references and resolver documentation. The CTS validator includes lightweight checks for DIA context wiring when `identity_anchor.anchor_type` indicates UNTP DIA.
