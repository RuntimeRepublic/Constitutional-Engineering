# RENDER / PUBLICATION HANDOFF — CWC-CE-164 → CE — Engineer

**From:** CE — Bill A Definition Engineer  
**To:** CE — Engineer  
**Status:** Candidate white-paper package ready for later phone-first PDF rendering  
**Date:** 2026-09-05  
**Baseline HEAD (unchanged by Definition Engineer):** `9eed44b47f2802a426106b4f3fb4b2d5b55be59a`

## Why this handoff exists

CWC-CE-164 authorized Definition Engineer to create substantive white-paper content and controlled SVG diagrams. Safe reuse of the CWC-CE-161 ReportLab renderer was **not** available without meaningful changes:

- CE-161 renderer hard-pins `CANONICAL_SHA = 9e96c1b…` (pre-CE-163);
- CE-161 renderer is built for LOU-004 / WD-113 markdown, not white-paper + SVG embedding;
- SVG diagram embedding and phone-first diagram pagination require publication engineering.

Definition Engineer therefore did **not** improvise renderer changes and did **not** produce a candidate PDF under CWC-CE-164.

## Source package to render (later CWC)

Root:

`Engineering-Office/publication/bill-a/public-review/white-paper/`

Primary markdown:

`source/Bill-A-Engineering-a-New-Kansas-Tax-System-White-Paper.md`

Diagrams (SVG source of truth):

- `diagrams/svg/WP-DIAG-001-Bill-A-Engineering-Idea.svg`
- `diagrams/svg/WP-DIAG-002-Current-Transition-Future.svg`
- `diagrams/svg/WP-DIAG-003-All-In-All-Out.svg`
- `diagrams/svg/WP-DIAG-004-TRR-ARR.svg`
- `diagrams/svg/WP-DIAG-005-Government-Claim-Degradation.svg`
- `diagrams/svg/WP-DIAG-006-Property-Tax-Elimination.svg`
- `diagrams/svg/WP-DIAG-007-Sinking-Fund-Future-State.svg`

Validation / traceability:

- `validation/CWC-CE-164-VALIDATION.md`
- `validation/WP-Source-Traceability.md`
- `validation/WP-DIAG-Traceability-Register.md`

## Rendering requirements (for later CWC)

Reuse CE-161 phone-first principles where practical:

- ~6 × 9 portrait;
- readable body text / spacing / hierarchy;
- minimal tables (essay already uses 3 public tables);
- diagrams legible on phone (own page if needed);
- clickable BlueprintLiberty.com and full GitHub URL;
- page numbers;
- clear artifact status banners (derivative; not LOU; not accepted; HG-D1 not passed; maturity 19%).

Do **not** alter Human Intent while formatting.

Do **not** regenerate or invent diagrams outside the SVG sources.

## Boundaries

COMMIT/PUSH by Definition Engineer: NONE  
CE-162: NOT RELEASED BY THIS HANDOFF  
Facebook / ElevenLabs / AI interpretation tests: NONE  

Libertas sine lapsu — Liberty without drift.
