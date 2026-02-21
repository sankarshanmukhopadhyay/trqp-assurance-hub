# Error states and how to interpret them

Assurance tooling is useful only when failures are **deterministic** and **actionable**.

This guide standardizes how this repo (and the combined assurance manifest) expects errors to be categorized and communicated.

## Error classes

### 1) Target / connectivity errors

**Symptoms**
- Cannot resolve DNS / TLS handshake fails
- 401/403 from endpoints that are expected to be reachable
- Timeouts

**What to do**
- Confirm base URL and network reachability
- Confirm any auth requirements and environment variables
- Capture a minimal reproduction: endpoint + method + headers (secrets redacted)

### 2) Protocol conformance failures (Conformance Suite)

**Symptoms**
- Response shape violates spec
- Mandatory headers or fields missing
- Wrong status codes / wrong caching semantics

**What to do**
- Treat as a product defect in the TRQP implementation
- Link to the failing control / requirement identifier
- Attach the conformance evidence bundle (or the relevant excerpt)

### 3) Posture failures (TSPP)

**Symptoms**
- Missing signing, weak authn/z, insecure defaults
- Insufficient auditing / logging expectations for the assurance level
- Required security headers not present

**What to do**
- Treat as an engineering hardening task
- If the issue is “policy vs implementation”, file it in TRQP‑TSPP with:
  - the AL level
  - the control ID
  - the observed vs expected behavior

### 4) Orchestration / integration errors (Hub)

**Symptoms**
- Combined manifest fails schema validation
- Artifacts referenced in manifest are missing
- Version set not in compatibility matrix

**What to do**
- Validate the manifest against `schemas/combined-assurance-manifest.schema.json`
- Ensure the build_id is stable across the two tool runs
- Confirm your version set is “known-good” or provide evidence for an unlisted set

## Recommended minimal error payload (machine-consumable)

When possible, errors should be represented as structured JSON with:

- `error_code` (stable identifier)
- `class` (one of the classes above)
- `message` (human-readable)
- `context` (target URL, endpoint family, tool name/version)
- `remediation_hint` (one actionable next step)

This enables deterministic client behavior and reliable issue triage.
