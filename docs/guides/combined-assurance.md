# Combined Assurance Guide

This guide gives implementers a repeatable workflow to generate **one coherent assurance story** using both:

- TRQP Conformance Suite (protocol correctness)
- TRQP-TSPP (security & privacy posture)

## Why combined assurance

Conformance answers: **“Does it behave according to TRQP expectations?”**

Posture answers: **“Is it deployed in a way that’s resilient under realistic threats?”**

In most procurement/audit contexts you need both—behavior and posture—because failures in either become exploitable system risk.

## Recommended run order

1. Run conformance first (protocol failures can invalidate posture assumptions)
2. Run TSPP second (posture checks assume endpoints exist and are reachable)

## Evidence normalization

The key to a combined story is a shared build identifier.

### Minimum metadata to capture

Record this in both runs:

- Build identifier (git SHA or artifact version)
- Target environment (dev/stage/prod)
- Tool + version
- Profile name + version
- Timestamp

## Bundle merge strategy

Do **not** physically merge tool outputs unless you must.

Preferred approach:

- Keep each tool’s evidence bundle intact
- Add a thin “index” manifest that references both

### Example folder layout (implementer side)

```text
assurance/
  build-<ID>/
    conformance-suite/
      evidence-bundle.json
      reports/
    tspp/
      evidence-bundle.json
      reports/
    combined-manifest.json
```

## Combined manifest (concept)

Your combined manifest should be dead simple:

- Build identifier
- References (paths/URIs) to each bundle
- High-level summary fields (counts, pass/fail totals)

This hub repo will eventually host a small JSON schema for `combined-manifest.json` once both underlying bundle formats are stable.
## Combined Assurance Manifest (optional but recommended)

To make combined runs portable across CI systems and audits, this Hub defines a minimal machine-readable manifest:

- Schema: `schemas/combined-assurance-manifest.schema.json`
- Example: `examples/combined-assurance-manifest.example.json`

The manifest’s job is boring but critical: bind **one build identifier** to **both tool runs** and the **evidence artifacts** they produced, so downstream verification and procurement teams can reason about provenance without guesswork.
