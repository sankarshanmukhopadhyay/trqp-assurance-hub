# Trust Systems Assurance Method (TSAM)

## Purpose

The Trust Systems Assurance Method (TSAM) is a **registry-agnostic** methodology for designing, assessing, and operating **trust-bearing distributed systems**.

TSAM defines how **governance intent**, **assurance levels**, **conformance verification**, **runtime integrity controls**, and **evidence production** are bound into a coherent assurance architecture.

TSAM is **not** a standard and **not** a certification program.  
TSAM is a method for making trust systems **testable**, **observable**, and **upgradeable**.

## Normative language

This repository uses the key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** as described in RFC 2119 and RFC 8174.

## Scope

TSAM applies to systems that:

- publish or resolve trust metadata,
- operate registries, directories, or trust lists,
- enforce policy decisions over distributed interactions,
- validate or verify statements, credentials, or attestations,
- coordinate cross-domain trust relationships.

TSAM is **registry-agnostic** and **protocol-agnostic**.

## Core requirements

A TSAM-aligned system MUST:

1. define explicit assurance levels with **normative, testable** criteria,
2. bind assurance claims to **controls** that can be independently evaluated,
3. provide at least one **conformance verification pathway** per assurance level,
4. define and implement **runtime integrity** controls proportional to risk,
5. produce **machine-verifiable evidence artifacts** for each required claim,
6. publish **upgrade paths** between assurance levels, including required evidence deltas.

## Layered architecture

TSAM structures assurance across five layers:

1. Governance Semantics
2. Assurance Levels
3. Conformance Verification
4. Runtime Integrity Controls
5. Evidence & Observability

Implementations MAY distribute these layers across multiple repositories or artifacts, but MUST preserve coherence across them.

## Relationship to this repository

This repository implements components aligned with TSAM.

TSAM provides the methodological spine.  
The repository provides a concrete instantiation.
