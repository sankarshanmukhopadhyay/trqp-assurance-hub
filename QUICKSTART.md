# Quickstart

This hub is the front door for combined TRQP assurance.

## Pick your starting point

- Protocol correctness → use the **TRQP Conformance Suite**
- Security and privacy posture → use **TRQP‑TSPP**
- Production and procurement → use **both** and bind outputs with a Combined Assurance Manifest

## Use the CI “golden path”

This repo includes a minimal workflow that checks out the companion repos and emits:

- a Combined Assurance Manifest
- an artifact checklist aligned to the evidence artifacts matrix

Workflow:

- `.github/workflows/combined-assurance-smoke.yml`

Artifacts are uploaded under the name:

- `combined-assurance-smoke-artifacts`
