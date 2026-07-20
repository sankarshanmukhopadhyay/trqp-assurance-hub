---
layout: default
title: "How to audit this AL4 evidence bundle"
nav_exclude: true
---

# How to audit this AL4 evidence bundle

AL4 extends AL3 with continuous operational evidence, time-bounded validity,
and explicit key protection and monitoring declarations. This guide maps each
AL4-specific artifact to its verifier check and expected outcome, complementing
the AL3 audit guide (`examples/al3-evidence-bundle/AUDIT_GUIDE.md`).

Perform the full AL3 checklist first, then apply the additional checks below.

## AL4-specific auditor checklist

### 1. Monitoring evidence (`monitoring-evidence/`)

**Verifier check:** Is continuous monitoring evidence present and covering the
assurance claim period? Does the summary reference a declared retention policy?

**Expected outcome:** `monitoring-evidence/monitoring-summary.json` is present
and machine-readable; `monitoring-evidence/monitoring-logs.ndjson` contains at
least one log entry within the assurance period; the summary declares
`retention_days` and `coverage` fields; the `coverage` array includes at minimum
`authorization` and `recognition`.

**Failure signal:** No log entries within the assurance claim period; missing
`retention_days`; `coverage` array empty or not covering the claimed endpoints.

---

### 2. Incident metrics (`incident-metrics.csv`)

**Verifier check:** Does the incident record cover the assurance period? Are
all incidents resolved with documented closure?

**Expected outcome:** CSV contains a `status` column with no open incidents
(`status != resolved`) within the validity window; if incidents exist, each
has a `resolution_date` before the Certification Attestation `issued_at`.

**Failure signal:** Open incidents within the validity window; missing
`resolution_date` for incidents; CSV covers less than the full assurance period.

---

### 3. Key rotation proof (`key-rotation-proof.md`)

**Verifier check:** Has signing key rotation occurred at the declared cadence?
Is evidence of the last rotation present?

**Expected outcome:** Document declares a rotation cadence (e.g., 12 months);
the last rotation date is within the cadence window; the new key's `kid` matches
the `kid` declared in the JWKS at the time of assessment.

**Failure signal:** Last rotation date outside the cadence window; `kid` mismatch;
no declared cadence.

---

### 4. Operational Attestation Statement (`operational-attestation-statement.md`)

**Verifier check:** Does the operator attest to continuous operation within the
claimed validity window? Are the attestation scope and method documented?

**Expected outcome:** Statement covers the full assurance period; operator
identity is consistent with the Certification Attestation `certified_entity`;
method (self-attestation vs. audited) is declared.

**Failure signal:** Period gap between operational attestation and Certification
Attestation `validity.not_before`; identity mismatch with the attestation.

---

### 5. Change log (`change-log.md`)

**Verifier check:** Are all material changes during the assurance period documented?
Is each change linked to a change control record or ticket?

**Expected outcome:** Each entry has a `date`, `description`, and `ref` to a
change control record; entries within the assurance period are complete; no
undocumented deployments relative to the Certification Attestation scope.

**Failure signal:** Gaps in the change log during the assurance period;
deployments recorded in CI without a corresponding change log entry.

---

### 6. Revocation notice (`revocation-notice.json`)

**Verifier check:** If a revocation has occurred, is the structured notice
present and complete? If no revocation, is the field `status: active`?

**Expected outcome:** `status` is `active` (no revocation) or `revoked` with
a `revoked_at` timestamp, `reason`, and `successor_ref` (if applicable); the
`issued_by` identity matches the operator declared in the Certification Attestation.

**Failure signal:** `status: revoked` without a `revoked_at` or `reason`;
`issued_by` identity mismatch; missing `successor_ref` when the registry was
replaced rather than discontinued.

---

### 7. Renewal plan (`renewal-plan.md`)

**Verifier check:** Is there a documented plan for renewing the assurance claim
before `validity.not_after`? Is the renewal cadence consistent with the
monitoring and key rotation cadences?

**Expected outcome:** Plan declares a renewal trigger date (≥ 30 days before
`not_after`); renewal scope and responsible party are identified; plan is
consistent with the key rotation and monitoring cadences declared elsewhere.

**Failure signal:** No renewal trigger date; renewal date is after `not_after`;
no named responsible party.

---

### 8. Certification Attestation (AL4 additions)

At AL4, the Certification Attestation MUST also declare the assessor `method`
explicitly (not just `assessment_type`). Verify:

**Expected outcome:** `assessor.method` is non-empty and describes the evidence
sampling approach used (e.g., "Evidence review + log sampling + key protection
inspection"); `validity.not_after` is within 12 months of `issued_at` for
high-consequence claims.

**Failure signal:** `assessor.method` absent or empty; validity window exceeds
12 months without a documented exception.

---

## Summary: AL4 pass criteria

All AL3 criteria, plus:

1. Monitoring evidence present, covering the full assurance period, with declared retention.
2. All incidents within the validity window are resolved with documented closure.
3. Key rotation evidence shows rotation within the declared cadence.
4. Operational attestation covers the full assurance period with consistent identity.
5. Change log is complete for the assurance period with no undocumented deployments.
6. Revocation notice is present and either `active` or correctly completed for revocations.
7. Renewal plan is present with a trigger date before `validity.not_after`.
8. Certification Attestation includes explicit assessor `method` and validity ≤ 12 months.
