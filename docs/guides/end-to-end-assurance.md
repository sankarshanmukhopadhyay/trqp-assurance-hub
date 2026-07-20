---
layout: default
title: "End-to-End Assurance Execution"
nav_exclude: true
---

# End-to-End Assurance Execution

The Hub composes authentic CTS and TSPP evidence only when both reports bind to the same `run_id` and `target_id` and the producer versions belong to a supported compatibility tuple. Mismatch, unsupported tuples, malformed decisions, and tampering are fail-closed conditions.

```bash
python tools/run_combined_assurance.py \
  --cts-report ../trqp-conformance-suite/artifacts/validation/cts-report.json \
  --tspp-report ../TRQP-TSPP/artifacts/validation/tspp-report.json
```

The output is an evidence manifest, assurance decision, and traceability report. The conclusion evaluates supplied evidence and does not constitute external certification.
