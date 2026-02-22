# Revocation semantics (assurance layer)

Revocation is where trust systems go to either become real… or become theater.

This repository defines **assurance-layer** revocation semantics for:

- recognition relationships,
- lifecycle state,
- control satisfaction assertions.

It does **not** redefine protocol query endpoints.
It defines what operators should publish so revocation can be evaluated consistently.

## Revocation causes

Publishers should use a small, stable taxonomy for revocation causes (non-normative):

- `compromise` — keys, infrastructure, or operator control compromised
- `policy_violation` — non-compliance with declared controls/policies
- `audit_failure` — failed or materially qualified audit
- `operational_outage` — sustained unavailability impacting verifier reliance
- `superseded` — replaced by a newer assertion/profile

## Where revocation appears

Revocation can be expressed in multiple places:

- Recognition Assertion: `recognition.revocation`
- Lifecycle Assertion: state transition to `revoked`
- Control Satisfaction Declaration: control status downgraded or declaration expired

## Propagation expectations

This repo does not force ecosystem-wide propagation rules.
It provides practical expectations to reduce ambiguity:

- A revoked recognition assertion should trigger re-evaluation of dependent claims.
- If a registry enters `revoked` lifecycle state, recognition edges pointing to it should be treated as effectively invalid within the impacted scope.
- If control satisfaction expires, conditional recognition that depends on it should be treated as inactive until refreshed.

## Time and caching

Because TRQP outputs may be cached by verifiers, revocation artifacts should be:

- timestamped (`issued_at`, `revoked_at`),
- published at stable locations,
- retained per declared retention policy.
