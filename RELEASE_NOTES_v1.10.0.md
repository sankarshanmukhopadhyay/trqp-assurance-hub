---
layout: default
title: "TRQP Assurance Hub v1.10.0"
nav_exclude: true
permalink: /RELEASE_NOTES_v1.10.0/
---

# TRQP Assurance Hub v1.10.0

## Portfolio integration release

This release connects the Assurance Hub to the current executable governance layer provided by Trust Systems Meta-Model v0.24.0 and Trust Infrastructure Schemas v0.14.1.

### Added

- Machine-readable cross-repository integration contract.
- Explicit semantic and schema version pins.
- Declared evidence relationships with TRQP-TSPP and the TRQP Conformance Suite.
- Automated validation of release pins, evidence availability, repository relationships, and invalidation conditions.
- CI-generated portfolio integration evidence artifact.

### Assurance impact

The Hub now has a machine-verifiable boundary for evidence aggregation. Missing source evidence or incompatible shared semantics invalidates the portfolio integration status instead of remaining an implicit documentation concern.

### Compatibility

Existing assurance artifacts remain compatible. This release adds governance and validation around their cross-repository use.
