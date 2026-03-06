# Combined Assurance Guide

This guide gives implementers a repeatable workflow to generate **one coherent assurance story** using both:

- TRQP Conformance Suite (protocol correctness)
- TRQP-TSPP (security & privacy posture)

## Why combined assurance

Conformance answers: **"Does it behave according to TRQP expectations?"**

Posture answers: **"Is it deployed in a way that's resilient under realistic threats?"**

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

- Keep each tool's evidence bundle intact
- Add a thin "index" manifest that references both

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



## Producer interfaces (what the Hub expects)

This guide assumes the producer repos emit **portable evidence bundles** with a stable surface:

### Conformance Suite (CTS)

- Recommended profile for "plumbing check": `profiles/smoke.yaml`
- Evidence output directory contains:
  - `bundle_descriptor.json`
  - `checksums.json`
  - `bundle.zip` (optional convenience package)

Crosswalk: https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite/blob/main/docs/hub-crosswalk.md

### TSPP

- Harness produces a conformance report via `TSPP_REPORT_PATH=...`
- Package a posture evidence bundle:

```bash
python scripts/create_evidence_bundle.py --report <report.json> --out <bundle_dir>
```

Evidence output directory contains:
- `bundle_descriptor.json`
- `checksums.json`
- `bundle.zip`
- `tspp_posture_report.json`

Crosswalk: https://github.com/sankarshanmukhopadhyay/TRQP-TSPP/blob/main/docs/hub-crosswalk.md

---

## AL3 combined assurance walkthrough

At AL3, both tools must run and their outputs must be linked in a Combined Assurance Manifest (CAM).

### Step 1 — Run the Conformance Suite

```bash
python cts/run.py \
  --profile profiles/baseline.yaml \
  --sut examples/sut.local.yaml \
  --out reports/cts-run-al3
```

Collect: `bundle_descriptor.json`, `checksums.json`, `verdicts.json`.

### Step 2 — Run TSPP at AL3

```bash
export TRQP_BASE_URL="https://your-registry.example"
export TSPP_EXPECT_AL="AL3"
export TSPP_REPORT_PATH=./tspp_report_al3.json
pytest harness/ -q
python scripts/create_evidence_bundle.py --report tspp_report_al3.json --out reports/tspp-run-al3
```

Collect: `bundle_descriptor.json`, `checksums.json`, `tspp_posture_report.json`.

### Step 3 — Produce evidence artifacts

AL3 requires the following artifacts (see `examples/al3-evidence-bundle/` for worked examples):

- **Combined Assurance Manifest** — links both bundles to one build scope
- **Control Satisfaction Declaration** — maps AL3 control objectives to evidence artifacts
- **Lifecycle Assertion** — declares lifecycle state and transition evidence
- **Remediation Closure** — records closure for any nonconformities found

### Step 4 — Independent review

An independent assessor reviews the evidence bundle. Assessor identity MUST be recorded in the Certification Attestation (where certification is claimed).

See `examples/al3-evidence-bundle/` for complete file examples.

---

## AL4 combined assurance walkthrough

AL4 extends AL3 with continuous monitoring requirements and operationalized revocation and renewal.

### Step 1 and Step 2 — Same as AL3

Run both tools as above. Use AL4-specific TSPP mode:

```bash
export TSPP_EXPECT_AL="AL4"
```

### Step 3 — Produce AL4 evidence artifacts

In addition to all AL3 artifacts, AL4 requires:

- **Continuous monitoring artifacts** — logs/metrics/alerts per declared retention policy
- **Incident metrics export** — operational incident evidence (CSV or structured format)
- **Key rotation proof** — evidence of key rotation cadence
- **Operational attestation statement** — operator attestation of ongoing control performance
- **Revocation notice** — structured notice (if any revocation event has occurred)
- **Renewal plan** — declared cadence and procedure for renewal

See `examples/al4-evidence-bundle/` for complete file examples.

### Step 4 — Assessor review with method recording

At AL4, assessor identity **and method** MUST be recorded in the Certification Attestation.

```json
{
  "assessor_id": "...",
  "assessment_method": "remote-document-review",
  "validity_period": { "not_before": "...", "not_after": "..." }
}
```

---

## Evidence artifact vocabulary

Both AL3 and AL4 share the same core evidence kinds. The following table maps AL expectations to concrete artifact paths and schema references.

| Artifact | Required at | Schema / Example |
|---|---|---|
| Combined Assurance Manifest | AL3+ | `schemas/combined-assurance-manifest.schema.json` |
| Control Satisfaction Declaration | AL3+ | `schemas/control-satisfaction.schema.json` |
| Lifecycle Assertion | AL3+ | `schemas/lifecycle-assertion.schema.json` |
| Remediation Closure | AL3+ (if nonconformity found) | `examples/al3-evidence-bundle/remediation-closure.json` |
| Certification Attestation | AL3 optional / AL4 required | `schemas/certification-attestation.schema.json` |
| Monitoring evidence | AL4+ | `examples/al4-evidence-bundle/monitoring-evidence/` |
| Revocation Notice | AL4+ | `schemas/recognition-assertion.schema.json` |

---

## Cross-repo links

- AL3 evidence bundle walkthrough: `examples/al3-evidence-bundle/README.md`
- AL4 evidence bundle walkthrough: `examples/al4-evidence-bundle/README.md`
- Assurance levels canonical definitions: `docs/guides/assurance-levels.md`
- Evidence artifacts expectations matrix: `docs/guides/evidence-artifacts.md`
