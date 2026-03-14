# Operational Stack Narrative

The TRQP stack is easiest to understand when treated as an **operational pipeline** rather than as three adjacent repositories.

At a high level, the system does four things:

1. evaluates protocol behavior using the **TRQP Conformance Suite**,
2. evaluates deployment posture using **TRQP-TSPP**,
3. binds both outputs into a **Combined Assurance Manifest**,
4. publishes the resulting evidence into a **Trust Registry reference service** for discovery.

## Why this matters

A standards stack that stops at specification text leaves implementers doing interpretive gymnastics. The Operational Stack turns that into a concrete workflow:

```text
Implementation
    ↓
Conformance evaluation (CTS)
    ↓
Posture evaluation (TSPP)
    ↓
Combined Assurance Manifest
    ↓
Trust Registry publication / discovery
```

This creates a portable evidence bundle that can be consumed by:

- implementers,
- ecosystem operators,
- assessors and auditors,
- procurement and governance teams.

## Stack components

### 1. TRQP Conformance Suite

The Conformance Suite answers the question:

> Does the target service behave according to the selected TRQP profile?

Operationally, CTS produces machine-readable reports with a shared `run_id`, `target_id`, profile identifier, summary, and test results.

### 2. TRQP-TSPP

TRQP-TSPP answers the question:

> Does the target deployment exhibit the posture required for the declared assurance level?

Operationally, TSPP produces a machine-readable report with the declared `assurance_level`, shared `run_id`, `target_id`, control-level evidence, and a summary.

### 3. Assurance Hub

The Assurance Hub binds CTS and TSPP outputs into one coherent object:

- a **Combined Assurance Manifest**, and
- optional **machine-readable assurance profiles** that state what evidence is expected at AL1-AL4.

This is where the stack becomes legible to humans and machines at the same time.

### 4. Trust Registry reference service

The Trust Registry reference service is a deliberately small service for **publishing and discovering** trust-service metadata and associated evidence artifacts.

It is not trying to be the final ecosystem architecture. It is a **reference service** whose job is to make discovery, interop testing, and demonstration flows possible.

## Architectural view

```text
+---------------------------+
| Implemented TRQP service  |
+---------------------------+
             |
             v
+---------------------------+
| TRQP Conformance Suite    |
| - protocol checks         |
| - profile-scoped tests    |
+---------------------------+
             |
             v
+---------------------------+
| TRQP-TSPP                 |
| - posture checks          |
| - assurance level checks  |
+---------------------------+
             |
             v
+---------------------------+
| Assurance Hub             |
| - combined manifest       |
| - assurance profiles      |
+---------------------------+
             |
             v
+---------------------------+
| Trust Registry            |
| - trust service listing   |
| - evidence discovery      |
+---------------------------+
```

## Operator path

The intended operator path is:

1. run CTS against the target service,
2. run TSPP against the same target,
3. generate a combined manifest,
4. validate the chosen machine-readable assurance profile,
5. publish the outputs through a trust registry service.

That gives the ecosystem an answer to the hard question:

> not merely "what does the service claim?" but "what evidence exists, under what assurance level, and where can it be discovered?"

## Reference artifacts

- Run guide: `docs/guides/run-the-stack.md`
- Compatibility matrix: `docs/reference/compatibility-matrix.md`
- Machine-readable assurance profiles: `profiles/al*.yaml`
- Trust Registry reference service: `services/trust-registry-reference/`

## Design stance

The Operational Stack is intentionally modest in form and ambitious in consequence.

It does not merge all concerns into one repo. It keeps protocol, posture, and assurance concerns separate. But it **does** establish a stable integration surface so that the ecosystem behaves like one stack rather than three essays with badges.
