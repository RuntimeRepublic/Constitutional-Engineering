# PR-RELEASE-ARCH-001 — Bill A Draft 1.12 Public-Review Release Architecture

**Document ID:** PR-RELEASE-ARCH-001  
**Governing Work Card:** CWC-CE-179  
**Status:** CANDIDATE — PUBLICATION-READINESS DEFINITION — **NOT RELEASED**  
**Package canonical SHA:** `05bedea51c7489441ae411bb5b5b03fe532b1b66`  
**Aligns with:** LOU-PR-001 (HG-PR ≠ HG-D1); ECR-006; Option 3 Bill A packet independence  

```text
PUBLICATION = NOT PERFORMED
HG-PR = NOT PASSED (RELEASE NOT AUTHORIZED BY THIS CWC)
HG-D1 = NOT PASSED
MATURITY = 19% UNCHANGED
```

---

## 1. Purpose of public review

Public review tests and improves Human Engineering Intent **before** HG-D1.

It is intended to surface: conflicts; missing Human Intent; unsupported assumptions; economic defects; legal / constitutional / AGCL questions; implementation and transition risks; unintended consequences; ambiguity; internal inconsistency; better alternatives; research requirements.

It is **not** a vote that automatically changes the LOU.  
It is **not** HG-D1.  
It is **not** legislation.

---

## 2. Mandatory public-review authority notice

Every public-facing release surface SHALL display, at minimum:

```text
BILL A — PUBLIC REVIEW DRAFT
LOU-004 DRAFT 1.12
FOR COMMENT
NOT FINAL
NOT HG-D1 ACCEPTED
NOT PROPOSED STATUTORY TEXT

PUBLIC COMMENTS ARE INPUT TO ENGINEERING REVIEW.
COMMENTS DO NOT AUTOMATICALLY CHANGE HUMAN INTENT.

THE CONSTITUTIONAL-ENGINEERING REPOSITORY REMAINS ENGINEERING SOURCE TRUTH.

THE WHITE PAPER IS EXPLANATORY AND DERIVATIVE.
THE LOU CONTROLS THE CURRENT HUMAN ENGINEERING INTENT.
```

---

## 3. Freeze identity (exact package under review)

| Field | Value |
|---|---|
| Bill | Bill A — Comprehensive Kansas Tax-System Replacement |
| LOU | LOU-004 Draft 1.12 |
| White Paper | Draft 1.12 (derivative explanatory) |
| Package canonical SHA | `05bedea51c7489441ae411bb5b5b03fe532b1b66` |
| Render source SHA | `e3151e5ac3f8cdb6fc25ac6b36bf418072f723fb` |
| Renderer | PR-PDF-RENDER-002 / CWC-CE-177 |
| LOU PDF | `Bill-A-LOU-004-Public-Review-Draft-1.12.pdf` — 139 pages — SHA-256 `702BB99EEC20D70DB6C534BEF4F3CBADE0378D6FCFD6140A1247E68232032ADC` |
| White Paper PDF | `Bill-A-Engineering-a-New-Kansas-Tax-System-White-Paper-Draft-1.12.pdf` — 50 pages — SHA-256 `857838630AA07CCB9A1E2571DFDF961C91B3E321349C66CEB053910A942D8EB2` |
| Public-review status | **READY / NOT YET RELEASED** |
| Human visual acceptance | ACCEPTED (CWC-CE-178) |

Historical Draft 1.10 PDFs remain historical and SHALL NOT be presented as current.

---

## 4. Recommended architecture (smallest controlled path)

```text
ENGINEERING SOURCE TRUTH
= Constitutional-Engineering Git repository @ package SHA

PUBLIC-REVIEW PACKAGE
= controlled directory + accepted PDFs + landing + unresolved + freeze identity

HUMAN-FACING ENTRY (recommended)
= BlueprintLiberty.com “Start here” page
  → authority notice
  → reading order
  → direct links to White Paper PDF + LOU PDF + Unresolved Matters + Comment instructions
  → package SHA / PDF SHA display

OPTIONAL DISTRIBUTION SNAPSHOT (recommended if Human chooses)
= GitHub Release / tag as immutable download bundle ONLY
  → does not create new engineering authority
  → Release notes repeat authority notice + freeze identity

COMMENT INTAKE (Human decision required — see PR-04)
= one primary channel + optional secondary capture into controlled comment register

DISCOVERY (optional, subordinate)
= social posts / email that link ONLY to the Human-facing entry
  → never host competing “truth”
```

**Do not** make website, social media, or GitHub Release upstream of repository engineering truth.

---

## 5. Release-destination analysis

| Destination | Role | Use? | Benefit | Risk |
|---|---|---|---|---|
| A. GitHub repository | Engineering source truth; package files; freeze SHA | **Required** | Stable identity; hashes; history | Navigation hard for non-engineers if used as sole entry |
| B. GitHub Release / tag | Optional immutable public download snapshot | **Recommended optional** | Easy ZIP/PDF grab; version pin | Misread as “final product”; must not replace repo authority |
| C. BlueprintLiberty.com | Human-facing Start Here / explanation / links | **Recommended primary entry** | Citizen-readable; phone-friendly | Must never become source truth |
| D. Direct PDF access | Linked from landing / Release | **Required** | Phone reading of accepted artifacts | Stale copies if URLs not pinned to freeze identity |
| E. Social announcement | Discovery links only | **Optional after HG-PR** | Reach | Drift / overclaim; requires PR-10 |
| F. Existing LOU-PR-001 / PRC signals | Candidate/legislative signal track (separate from citizen comment) | **Preserve separately** | Already controlled | Do not conflate citizen review with candidate outreach |

**Recommendation:** C (entry) + A (truth) + D (PDFs) + optional B (Release snapshot). Activate E only after HG-PR RELEASE and PR-10.

No new external accounts/services are created by this CWC.

---

## 6. GitHub role (detail)

| Mechanism | This CWC recommendation |
|---|---|
| Repository files at SHA `05bedea…` | Authoritative package location |
| Public-review directory landing | `PUBLIC-REVIEW-README.md` + candidate `START-HERE` (refined for release) |
| GitHub Release | Optional **distribution** of exact freeze identity; notes must cite SHA-256s |
| Git tag | Optional alias of freeze SHA (e.g. `bill-a-public-review-1.12`) — **not created here** |

Visibility of files on GitHub alone does **not** open public review (LOU-PR-001). Opening requires Human **HG-PR = RELEASE**.

---

## 7. BlueprintLiberty.com role

```text
PUBLIC ENTRY / EXPLANATION
→ CONTROLLED ARTIFACT LINKS (repo and/or Release)
→ COMMENT INSTRUCTIONS
```

Never: `WEBSITE CONTENT → ENGINEERING TRUTH`.

Site posting is **not** performed in this CWC (PR-03).

---

## 8. Public package hierarchy (reading order)

1. **START HERE** (landing)  
2. **White Paper Draft 1.12 PDF** (plain-language explanation first)  
3. **LOU-004 Draft 1.12 PDF** (controlling intent)  
4. **UNRESOLVED-MATTERS**  
5. **Comment / review instructions**

Reading order ≠ authority order. LOU remains controlling.

---

## 9. Version-freeze architecture

**Principle:** Draft 1.12 is the **frozen review baseline** for the open review period. Comments cite Draft 1.12 / package SHA / PDF SHA.

If defect discovered during review:

| Option | When | Rule |
|---|---|---|
| **A. Continue + defer** | Default for material content issues | Keep collecting against 1.12; schedule post-review revision CWC |
| **B. Close/supersede** | Material defect makes continued review misleading | Human closes 1.12 review; open new version (e.g. 1.13) with new freeze identity |
| **C. Presentational correction** | Pure presentation / broken link / wrong hash display — if Human rules permit | Issue clearly labeled correction record; **do not silently replace** frozen PDF bytes without Human authorization and new identity |

Silent in-place replacement of frozen public files is **forbidden**.

Default recommendation pending Human PR-08 / PR-09: **Option A** for material issues; **Option C** only for proven presentational defects with Human approval.

---

## 10. Review period

| Decision | Status |
|---|---|
| Open date | **HUMAN DECISION REQUIRED (PR-06)** |
| Close date / duration | **HUMAN DECISION REQUIRED (PR-07)** |

**Recommendation only (not adopted):** 30 calendar days citizen comment window, with Human option to extend without changing freeze identity. Do not invent dates in release materials until Human supplies them.

---

## 11. Feedback loop (controlled)

```text
PUBLIC COMMENT
→ RECORD (schema)
→ CLASSIFY (bounded classes)
→ VERIFY EVIDENCE WHERE REQUIRED
→ DETERMINE ENGINEERING MATERIALITY
→ ROUTE TO CORRECT AUTHORITY
→ HUMAN DECISION WHERE REQUIRED
→ CONTROLLED CWC
→ LOU REVISION IF AUTHORIZED
→ WHITE PAPER RECONCILIATION
→ VALIDATION
→ NEW REVIEW VERSION OR REVIEW CLOSURE
```

Forbidden: `PUBLIC COMMENT → LOU CHANGE` (direct).

---

## 12. PDCA relationship

| Phase | Public-review meaning |
|---|---|
| PLAN | Draft 1.12 Human Intent architecture |
| DO | Expose controlled draft after HG-PR RELEASE |
| CHECK | Collect/evaluate comments, evidence, conflicts |
| ACT | Human-authorized revise / research / clarify / no-change |

PDCA ≠ autonomous governance. PDCA ≠ taxing authority.

---

## 13. HG-D1 relationship

```text
HUMAN INTENT
→ LOU DRAFT
→ PUBLIC REVIEW (after HG-PR RELEASE)
→ COMMENT DISPOSITION
→ LOU RECONCILIATION
→ HUMAN REVIEW
→ HG-D1 DECISION
```

Public review is input/evidence for the later Human gate. It does not pass HG-D1.

---

## 14. Engineering / publication authority map

| Layer | Authority |
|---|---|
| Controlled repository | Engineering source truth |
| Public-review package | Controlled derivative release package |
| Website | Access / communication |
| Social media | Discovery / distribution |
| Public comment | Engineering input |
| Human Engineer | Human-Intent authority |
| AI / agents | Classify/analyze/recommend only |

---

## 15. Later release-execution validation (for a future CWC)

A release-execution CWC SHALL pass at least:

1. Correct Draft 1.12 version labels  
2. Exact LOU / WP PDF SHA-256 match freeze identity  
3. Package SHA `05bedea…` (or Human-authorized successor freeze)  
4. Authority notice present on all public surfaces  
5. Reading-order links correct  
6. Comment channel operational **and** Human-authorized  
7. Open/close dates present  
8. Freeze identity published  
9. Unresolved matters accessible  
10. No Draft 1.10 presented as current  
11. No HG-D1 / maturity / SPEC claims  
12. No broken links; mobile check of landing + PDFs  
13. HG-PR RELEASE recorded; LOU-PR-001 state = PUBLIC REVIEW  

**Not executed in CWC-CE-179.**

---

## 16. Relationship to LOU-PR-001

This architecture prepares Bill A Draft 1.12 for the LOU-PR-001 state **READY FOR PUBLIC-REVIEW DECISION / HG-PR PENDING**.

This CWC does **not** pass HG-PR. Human must later choose RELEASE / MODIFY / REJECT.

Citizen comment architecture here is complementary to LOU-PR-001’s candidate-signal schema; do not merge them into one undifferentiated stream without Human decision.

---

Libertas sine lapsu — Liberty without drift.
