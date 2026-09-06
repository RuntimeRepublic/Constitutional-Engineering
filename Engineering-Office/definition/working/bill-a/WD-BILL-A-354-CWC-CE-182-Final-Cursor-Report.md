# WD-BILL-A-354 — CWC-CE-182 Final Cursor Report

**Document ID:** WD-BILL-A-354  
**Source ID:** SRC-BILL-A-589  
**Governing Work Card:** CWC-CE-182  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / CYCLE RECORD — NOT HUMAN-ACCEPTED — NOT PUBLICATION  
**Version:** 1.0.0  
**Effective Date:** 2026-09-06  
**Repository:** `X:\GitHub\Constitutional-Engineering`

---

## OUTCOME A — BILL A KDOR TRANSACTION-BAND / TAXABLE-SALES DATA INQUIRY AUTHORIZATION AND EVIDENCE-GAP CLOSURE PASS

```text
KDOR DATA INQUIRY
=
READY FOR HUMAN TRANSMISSION.

STOP FOR HUMAN ACTION / RESPONSE.
```

This cycle closed the **preparation** gap identified by CWC-CE-181. It did **not** close the Kansas transaction-band **data** gap. No KDOR result was invented. No request was transmitted.

---

## A. Final Cursor Report (this file)

CWC-CE-182 is an evidence-gap-closure cycle, **not** a rate-selection cycle.

---

## B. CWC-CE-181 baseline verification

Verified from WD-BILL-A-128 / WD-BILL-A-131 / WD-BILL-A-132:

| Finding | Status |
|---|---|
| Authoritative public Kansas transaction-size bands | **NOT LOCATED** |
| Treasury/IRS Kansas taxable-retail receipt-band table | **NOT LOCATED** |
| FY2025 KLRD General Property (levied-for-collection) | **$6.667B** |
| Related PVD/OpenGov construction | **≈$6.823B** — different construction; not conflated |
| FY2025 KLRD Sales/Use combined | **$6.011B** |
| Current Kansas state sales-tax rate | **6.5%** |
| State food sales-tax rate | **0%** effective 1 January 2025 |
| MODEL C Bill A engineered required rate | **NOT YET CALCULABLE** |
| Illustrative property-equivalent models | ~**12.1%** on illustrative $55B; ~**7.4%** on illustrative $90B — **MODELED, not adopted** |
| CWC-CE-181 outcome | **OUTCOME A** — ETR-01–47 ALL PASS |

---

## C. Human authorization record

The Human Engineer authorized **preparation** of an aggregated KDOR evidence inquiry. Not authorized: confidential taxpayer-level records; automatic transmission; rate selection; 5%/5% change; Draft 1.12 mutation; Git mutation. See WD-BILL-A-333.

---

## D–I. Research-question, bands, fields, geography/time, reporting unit, alternatives

Defined in WD-BILL-A-334 through WD-BILL-A-339 and in KDOR-INQ-BILL-A-001.

Primary question: does KDOR possess data that can report, or be aggregated to report, Kansas taxable retail transactions by dollar-size bands for a defined period?

Preferred analytical bands (not tax brackets): $0–$20; $20.01–$30; $30.01–$50; $50.01–$100; $100.01–$250; $250.01–$500; $500.01–$1,000; $1,000.01+.

Statewide data are sufficient for the first model. County data would help later 105-county work and are **not** a condition of usefulness.

If KDOR receives only retailer-period aggregate tax-return amounts, exact receipt-size distribution may not be reconstructable. That limitation is to be recorded, not estimated.

---

## J. Human-transmittable KDOR inquiry

`Engineering-Office/definition/working/bill-a/kdor-inquiry/KDOR-INQ-BILL-A-001-Transaction-Band-Aggregates-READY-FOR-HUMAN-TRANSMISSION.md`

Status: **READY FOR HUMAN TRANSMISSION.** Not sent.

---

## K. Formal-records-request fallback

Initial path: informal technical/data inquiry (mail/phone to published KDOR Policy and Research).  
Fallback only: PR-50 general records. Do **not** start with DO-41. Not filed. See WD-BILL-A-341.

---

## L. Recipient / contact verification

Published KDOR Office of Policy and Research: 109 SW 9th Street; P.O. Box 3506, Topeka, KS 66601-3506; phone 785-296-3081; fax 785-296-7928; https://www.ksrevenue.gov.

**KDOR email: NOT VERIFIED — not invented.** Bounded delivery gap.

Optional published KLRD copy: 785-296-3181; kslegres@klrd.ks.gov; Room 68-West, State Capitol.

---

## M–N. Response intake and evidence classification

Intake template: `KDOR-INQ-BILL-A-001-RESPONSE-INTAKE.md`  
Incoming path: `kdor-inquiry/incoming/` (empty; no invented files).  
Classification register: WD-BILL-A-344. No response classified.

---

## O. Future model re-run

Later bounded CWC after a real response: ingest exact response; preserve provenance; validate definitions; reconcile periods; re-run band analysis; re-test 5%/5%; update Draft 1.13 **candidate** only. **Not fabricated now.** See WD-BILL-A-345.

---

## P. Draft 1.12 freeze

HEAD / package SHA: `05bedea51c7489441ae411bb5b5b03fe532b1b66`

| Artifact | SHA-256 |
|---|---|
| LOU PDF Draft 1.12 | `702BB99EEC20D70DB6C534BEF4F3CBADE0378D6FCFD6140A1247E68232032ADC` |
| White Paper PDF Draft 1.12 | `857838630AA07CCB9A1E2571DFDF961C91B3E321349C66CEB053910A942D8EB2` |

PDFs unmodified. Public SHA-pinned links unmodified.

---

## Q. Draft 1.13 candidate-state

LOU-004 Draft 1.13 = CANDIDATE addendum.  
White Paper Draft 1.13 = CANDIDATE addendum.  
Not Human-accepted. Not released. Does not replace Draft 1.12.

---

## R. 5% / 5% planning-value status

UP TO 5% STATE and UP TO 5% LOCAL remain planning ceilings / candidate values.

CWC-CE-181 **tested** them. CWC-CE-182 did **not** establish required / sufficient / insufficient / should-change. Values **unchanged**.

---

## S. Senator Murphy / Kimmie traceability

RQ-BILL-A-ETR-001 preserved: actual Kansas collections around $20, $30, $100, and larger. PURCHASE ARITHMETIC ≠ TRANSACTION DISTRIBUTION.

---

## T. KDOR-01 through KDOR-46

ALL PASS. See WD-BILL-A-350 and `WD-BILL-A-355-CWC-CE-182-VALIDATION.json`.

---

## U. Working-tree change manifest

See WD-BILL-A-351. HEAD remains `05bedea…`. Nothing staged / committed / pushed. Unrelated dirt preserved. `move_agent_to_root` aborted (non-blocking).

---

## V. Recommended next bounded CWC

**CWC-CE-183 — KDOR RESPONSE INTAKE / TRANSACTION-BAND MODEL RE-RUN**

Start only after Human transmission and/or an agency response. Do not start automatically. Silence is not “not maintained.”

If KDOR later reports NOT MAINTAINED: later research may evaluate CES microdata, Federal Reserve payment studies, private payment-network aggregates, merchant or academic datasets — all **ESTIMATED / MODELED** unless they become observed Kansas evidence.

---

## W. Outcome

**OUTCOME A.**

```text
OBSERVED KANSAS DATA
→ CONTROLLED ANALYSIS
→ MODEL RE-RUN
→ HUMAN EVALUATION
→ DRAFT RECONCILIATION
→ HG-D1 LATER.
```

Ask Kansas what data exist. Do not ask the data to prove the plan.

---

## Gates preserved

| Gate | Status |
|---|---|
| Draft 1.12 | FROZEN PUBLIC-REVIEW BASELINE |
| Draft 1.13 | CANDIDATE ONLY |
| Property tax → zero statewide | UNCHANGED HUMAN-INTENT INVARIANT |
| 5% state / 5% local | PLANNING CEILINGS / VALUES UNDER EVIDENCE TEST |
| MODEL C | NOT YET CALCULABLE |
| HG-D1 | NOT PASSED |
| SPEC | NOT AUTHORIZED |
| HG-D2 | NOT PASSED |
| Legislative Engineering | NOT AUTHORIZED |
| Bill A maturity | **19% UNCHANGED** |

---

Libertas sine lapsu — Liberty without drift.
