# TRQP Assurance Program Playbook

This document explains **why the TRQP assurance toolchain exists**, who it is for, and how to adopt it without needing to become a protocol historian.

It is written for **program owners, product leaders, platform teams, and governance functions**. Technical details live elsewhere.

## The problem this solves

TRQP enables interoperable discovery and use of authoritative registries, trust lists, and recognition assertions.

In practice, deployments fail to scale for three predictable reasons:

1. **Interoperability is underspecified in production**: teams pass a “demo conformance” bar but drift on edge cases, error semantics, and profile expectations.
2. **Security and privacy posture is not comparable**: two implementations can both “support TRQP” while producing radically different risk surfaces.
3. **Evidence is not portable**: adopters cannot produce the same audit-ready artifacts across environments, vendors, and change cycles.

The result is avoidable friction: stalled procurement, slow onboarding, repeated assessments, and expensive incident response.

## The outcome

The TRQP assurance toolchain turns protocol intent into a **repeatable assurance program**:

- **Comparable conformance** results across implementations and profiles
- **Security and privacy baseline** checks that can be run, evidenced, and audited
- **Portable evidence bundles** that are machine-checkable and suitable for review, certification, and governance reporting

The aim is not bureaucracy. The aim is **cost containment** and **trust at scale**.

## Who this is for

- **Operators** (registry / trust list operators): run checks, publish evidence, stay compatible as you evolve.
- **Implementers** (vendors, product teams): prove compatibility and reduce buyer friction.
- **Certifiers / assessors**: evaluate evidence consistently, reduce bespoke questionnaires.
- **Governance, risk, and procurement**: make decisions based on verifiable artifacts rather than slide decks.

## What you get (repo map)

The TRQP assurance toolchain is intentionally **decentralized** (not a monorepo). Each repo has a clear job.

1. **TRQP Assurance Hub** (this repo)
   - The “front door” and operating model
   - Canonical **Assurance Levels (AL1–AL4)**
   - Cross-repo guidance: profiles, evidence expectations, compatibility policy

2. **TRQP Conformance Suite (CTS)**
   - Conformance profiles and tests
   - Evidence bundle outputs for interoperability results

3. **TRQP Security & Privacy Baseline (TSPP)**
   - Security and privacy baseline requirements and checks
   - Evidence bundle outputs for baseline posture

## How to adopt (30 / 60 / 90 day path)

### First 30 days: baseline proof
- Pick a target: an existing TRQP deployment or reference implementation.
- Run **CTS** against a baseline profile and generate an evidence bundle.
- Run **TSPP** against the same target and generate an evidence bundle.
- Use the Hub guidance to interpret results and communicate gaps.

### Next 60 days: make it operational
- Integrate CTS and TSPP runs into CI/CD (or scheduled operations).
- Track deltas across releases using consistent run metadata.
- Start publishing a minimum evidence set to partners or procurement.

### Next 90 days: raise assurance
- Adopt higher assurance expectations (AL2 → AL3 → AL4) where needed.
- Expand evidence bundles, error state handling, and incident learnings.
- Use the certification baseline as a scaffold if formal certification is required.

## Where to start

- Hub documentation index (role-based): `docs/index.md`
- Hub operator runbook: `docs/OPERATOR_RUNBOOK.md`
- Hub combined assurance guide: `docs/guides/combined-assurance.md`
- Compatibility policy and matrix: `docs/policies/compatibility.md`

## Compatibility snapshot

As of this release line:

- Assurance Hub: **v0.4.x**
- Conformance Suite (CTS): **v0.4.x**
- TSPP: **v0.2.x**

For “known-good” pairings, see `docs/policies/compatibility.md`.
