# UNTP Digital Identity Anchor (DIA) and TRQP Directory Assurance

UN/CEFACT's UN Transparency Protocol (UNTP) defines the Digital Identity Anchor (DIA) credential as a mechanism to verify the identity of credential issuers and bind those identities to verifiable identifiers (typically DIDs).

For authoritative directories (including sovereign registries such as GRID), DIA introduces an additional evaluation surface:

- **Identity anchoring integrity**: is the anchor credential well-formed and referenceable using the declared JSON-LD context?
- **Issuer binding**: does the directory subject link to an issuer identity that can be verified (for example via a DID)?
- **Resolver readiness**: can identifiers be resolved using an identity resolver pattern when required?

This repository treats DIA as an **anchor extension** to the SAD-1 profile. The directory evaluation scope is the **composite trust system**: directory governance + directory publication integrity + identity anchoring.

## Normative references

- DIA specification: https://untp.unece.org/docs/specification/DigitalIdentityAnchor/
- DIA JSON-LD context (0.6.1): https://test.uncefact.org/vocabulary/untp/dia/0.6.1/context/
- Identity Resolver specification: https://untp.unece.org/docs/specification/IdentityResolver/
- UNTP specification overview: https://uncefact.github.io/spec-untp/docs/specification/

## Repository wiring

- Vendored context (tooling convenience): `schemas/contexts/untp/dia/0.6.1/context.jsonld`
- Directory entry schema adds optional `identity_anchor` to bind a subject to a DIA (or other anchor) credential.
