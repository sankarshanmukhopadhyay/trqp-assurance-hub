# UNTP Digital Identity Anchor (DIA) support

Some authoritative directories (including sovereign registries) may use the UN/CEFACT UN Transparency Protocol (UNTP) **Digital Identity Anchor (DIA)** credential and related **Identity Resolver (IDR)** patterns.

This Conformance Suite supports **evidence-grade validation** for directory artifacts that include DIA wiring:

- The SAD-1 `authoritative-directory-entry` schema includes an optional `identity_anchor` object.
- If `identity_anchor.anchor_type` indicates UNTP DIA, the validator performs lightweight checks to ensure a DIA JSON-LD context pointer is present.

## Vendored context

For reproducible offline checks, this repo vendors the DIA JSON-LD context:

- `schemas/contexts/untp/dia/0.6.1/context.jsonld`

Normative references:
- DIA specification: https://untp.unece.org/docs/specification/DigitalIdentityAnchor/
- DIA JSON-LD context (0.6.1): https://test.uncefact.org/vocabulary/untp/dia/0.6.1/context/
- Identity Resolver specification: https://untp.unece.org/docs/specification/IdentityResolver/
