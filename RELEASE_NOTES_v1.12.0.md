# TRQP Assurance Hub v1.12.0 — Assurance Lifecycle Recomposition

This release adds executable current-assurance lifecycle handling for TRQP Stack 2026.2.

## Added

- separation of immutable historical assurance outcome from current reliance validity;
- recomposition for material, non-material, and unknown change;
- fail-safe authority-drift detection;
- completed reassessment → explicit supersession lineage;
- machine-readable Stack 2026.2 lifecycle eligibility ledger;
- coordinated release gating that preserves pending evidence rather than treating workflow success as release success.

## Authority boundary

The Hub owns combined assurance validity, recomposition, supersession lineage, and coordinated Stack release judgment. It does not acquire TSPP materiality authority, CTS reassessment authority, TIS contract authority, or TSMM semantic authority.

## Validation

Lifecycle recomposition, authority drift, supersession, combined assurance, portfolio integration, quality, and full Stack release-eligibility workflows provide the executable evidence basis.

## Stack relationship

v1.12.0 is the Hub component candidate for TRQP Stack 2026.2. Coordinated publication remains conditional on an immutable component tuple, clean adopter walkthrough, final eligibility replay, and explicit human release judgment.
