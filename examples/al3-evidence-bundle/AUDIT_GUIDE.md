# How to audit this AL3 evidence bundle

This guide maps each artifact in the bundle to the verifier check it satisfies
and the expected outcome. Use this as a checklist when reviewing an AL3 submission.

## Auditor checklist

### 1. Combined Assurance Manifest (`combined-assurance-manifest.json`)

**Verifier check:** Does the manifest link both conformance and posture bundles
under a shared `run_id`? Are tool versions pinned to tagged releases?

**Expected outcome:** `manifest_version` present; `build.run_id` matches the
`run_id` in `cts-report.json` and `tspp-report.json`; `tools.trqp_conformance_suite`
and `tools.trqp_tspp` both present with explicit version strings; `summary.assurance_tier`
is `AL3`; `summary.overall_status` is `pass`.

**Failure signal:** Missing `run_id`, mismatched `run_id` across artifacts,
`summary.overall_status` is `fail` or `partial`.

---

### 2. Version tuple (`version-tuple.json`)

**Verifier check:** Are all component version declarations explicit? Are they
tagged releases (not branch refs)?

**Expected outcome:** All `components[*].ref_type` are `tag` or `commit-sha`
(not `branch`). Tool versions match those declared in the Combined Assurance
Manifest.

**Failure signal:** `ref_type: branch` for production claims; version mismatch
with the manifest.

---

### 3. Control Satisfaction Declaration (`control-satisfaction-declaration.json`)

**Verifier check:** Are all in-scope controls listed? Does each control have a
`status` of `satisfied` or documented rationale for `partially_satisfied`? Does
each control entry reference at least one evidence artifact?

**Expected outcome:** All five canonical controls (`TRQP-CTRL-01` through
`TRQP-CTRL-07`) are addressed. `status` is `satisfied` for controls where
evidence is present. Each `evidence` array contains at least one `ref` that
resolves to a real artifact.

**Failure signal:** Missing control entries; `not_satisfied` without remediation
closure; evidence `ref` values that do not resolve.

---

### 4. Lifecycle Assertion (`lifecycle-assertion.json`)

**Verifier check:** Is the `state` `active`? Are transition evidence references
present and resolvable? Is `effective_from` a valid RFC 3339 timestamp?

**Expected outcome:** `state` is `active`; `evidence` array contains at least
one entry with `kind` and `ref`; `issued_at` is a valid RFC 3339 timestamp.

**Failure signal:** `state` is `suspended` or `revoked` without a corresponding
revocation notice; missing `evidence`; `effective_from` after the claimed
assurance period start date.

---

### 5. Certification Attestation (`certification-attestation.json`)

**Verifier check:** Is an independent assessor identified? Is the `assessment_type`
`independent` or `accredited`? Is the `validity` period current? Are all
`in_scope_controls` present in the control catalog?

**Expected outcome:** `assessor.assessment_type` is `independent` or `accredited`;
`assessor.id` is a resolvable identifier; `validity.not_before` ≤ today ≤
`validity.not_after`; all `in_scope_controls` are valid control IDs from
`tools/control-catalog.json`; at least one `evidence_refs` entry of type
`control_satisfaction` is present.

**Failure signal:** `assessment_type: self`; expired validity; control IDs not
in the catalog; no `control_satisfaction` evidence ref.

---

### 6. Independent Assessment Report (`independent-assessment-report.md`)

**Verifier check:** Is the assessor identity consistent with the Certification
Attestation? Is the assessment scope clearly stated? Are any findings documented?

**Expected outcome:** Assessor name/ID matches the Certification Attestation;
scope covers the same endpoints declared in the attestation; any nonconformities
reference a `remediation-closure.*` artifact.

**Failure signal:** Identity mismatch; undocumented nonconformities; scope
narrower than the attestation claims.

---

### 7. Remediation Closure (`remediation-closure.json`)

**Verifier check:** Does the closure record reference the original nonconformity?
Is a resolution description present? Is the `resolved_at` timestamp before the
Certification Attestation `issued_at`?

**Expected outcome:** `nonconformity_ref` resolves to a finding in the
Independent Assessment Report; `resolution` is non-empty; `resolved_at` is
before the attestation `issued_at`.

**Failure signal:** `resolved_at` after attestation issuance; missing
`nonconformity_ref`; no `resolution` description.

---

### 8. Governance Policy (`governance-policy.md`)

**Verifier check:** Does the policy document declare control ownership, evidence
retention, and update cadence?

**Expected outcome:** Policy covers the controls declared in the Control
Satisfaction Declaration; retention period is explicitly stated; policy has a
named owner and a review date.

**Failure signal:** Policy predates the assurance claim period by more than one
review cycle; no retention period declared.

---

## Summary: AL3 pass criteria

All of the following must be true for an AL3 submission to pass audit:

1. Combined Assurance Manifest present with matching `run_id` across all tool reports.
2. All five canonical controls addressed in the Control Satisfaction Declaration.
3. Lifecycle state is `active` with transition evidence.
4. Certification Attestation identifies an independent assessor with current validity.
5. All nonconformities from the independent assessment have a documented remediation closure.
6. No `evidence_refs` in any artifact point to missing files.
