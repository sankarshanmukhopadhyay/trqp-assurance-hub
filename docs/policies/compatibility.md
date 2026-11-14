---
layout: default
title: "Compatibility Policy"
nav_exclude: true
---

# Compatibility Policy

The Hub has two deliberately different compatibility surfaces. `data/compatibility-registry.yaml` records supported legacy Operational Trust Stack release sets; `stack/releases/YYYY.N/manifest.json` is authoritative for an immutable **coordinated Stack release**. A development tuple in `data/component-compatibility.yaml` does not become a coordinated release merely because the underlying component versions are later published.

## Current coordinated release

[TRQP Stack 2026.4 — Lotus](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/releases/tag/trqp-stack-2026.4) is the current published coordinated baseline:

| Release | Hub | CTS | TSPP | Evidence |
|---|---|---|---|---|
| Lotus 2026.4 | v1.14.0 | v1.11.1 | v0.18.1 | [Immutable manifest](../../stack/releases/2026.4/manifest.json) |
| Banyan 2026.3 (historical) | v1.13.0 | v1.10.0 | v0.17.0 | [Immutable manifest](../../stack/releases/2026.3/manifest.json) |

The release identity also pins TSMM/TIS authorities and the decisive merged-main eligibility evidence; it does not transfer protocol, control, ecosystem-profile or certification authority. Target-state digest correlation establishes agreement about supplied snapshot identity, not independent deployment authenticity.

## Legacy supported release sets

The older `ots-2026-07`, `ots-2026-08`, and `ots-2026-09-profile-aware` entries remain in `data/compatibility-registry.yaml` for their respective consumers. They must not override the current coordinated Stack declaration or bypass Lotus state-bound validation. Release claims require an immutable tuple, complete execution evidence and governed publication.
