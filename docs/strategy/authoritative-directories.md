# Authoritative directories and meta-assurance

TRQP is often introduced as a protocol for querying trust registries. That framing is useful, but incomplete.

This repository positions the TRQP ecosystem as a **meta-assurance framework** capable of evaluating *any authoritative digital trust directory*.

## The claim

An authoritative directory can be evaluated if it exposes:

- a publishable authority surface (entries and lifecycle state)
- governance bindings (admission and removal rules)
- verifiable publication integrity (hashes and signatures)
- operational accountability (auditability, incident response, redress)

TRQP becomes the interoperable **query plane**. The Hub, CTS, and TSPP provide the **assurance plane**.

## Why this matters

Sovereign registries and standards directories frequently ship as:

- policy documents plus PDFs
- published JSON feeds
- signed bundles
- partial APIs

SAD-1 provides a minimum common denominator so evaluations remain comparable across implementations.

## Profiles

- SAD-1: a generic profile for authoritative directories
- GRID: an instance profile aligned to UN/CEFACT patterns

Profiles let the ecosystem adapt without hardcoding assumptions about a single directory model.
