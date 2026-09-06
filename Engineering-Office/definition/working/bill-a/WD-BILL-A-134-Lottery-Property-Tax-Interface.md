# WD-BILL-A-134 — Lottery / Property-Tax Interface

**Document ID:** WD-BILL-A-134  
**Source ID:** SRC-BILL-A-369  
**Governing Work Card:** CWC-CE-166  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / INTERFACE RECORD — DESTINATION INTENT LATER ANSWERED IN CWC-CE-167 (Q-012 = A) — NOT ACCEPTED  
**Version:** 1.0.0  
**Effective Date:** 2026-09-05  

```text
ARCHITECTURAL QUESTION EXPOSED
NOT A FINAL LOTTERY DISTRIBUTION FORMULA
CURRENT STATUTORY RECEIPT ≠ FUTURE BILL A ENTITLEMENT
BILL A CANNOT SILENTLY DISREGARD BINDING LEGAL OBLIGATIONS
```

## 1. Chain (CWC-CE-165 Human Intent)

```text
LOTTERY PURCHASE
→ PRIZE OBLIGATIONS
→ POST-PRIZE REVENUE
→ INDIVIDUAL RULE-OF-72 PARTITION (planning: 4% of post-prize)
→ REMAINING AVAILABLE GOVERNMENTAL REVENUE
→ PROPERTY-TAX ABATEMENT / RETIREMENT (investigation objective)
```

**SUPERSEDED as Human Intent:** $0.05 per $1 of gross ticket sales.

## 2. Architectural question (not answered in this CWC)

After prizes and the individual Rule-of-72 partition, **what portion of remaining lottery governmental revenue should be available for property-tax abatement / retirement?**

Existing Human Intent is to **investigate capturing remaining available governmental post-prize lottery revenue primarily for property-tax abatement/retirement**. That is an investigation objective. It is **not** a completed destination assignment and **not** a formula.

Presented as **Q-BILL-A-012** (WD-BILL-A-142). This file does **not** answer it.

## 3. Destination audit classes

| Destination concept | Classification |
|---|---|
| Prize obligations paid first | **HUMAN INTENT** (prizes-first) |
| Individual 4% post-prize partition | **HUMAN INTENT** (planning; not statutory rate) |
| Remaining governmental post-prize revenue → PT abatement/retirement | **HUMAN INTENT** (investigation objective) + **HUMAN DECISION REQUIRED** (Q-012) |
| Current Kansas Lottery statutory beneficiaries / earmarks | **CURRENT FACT** (existence of a statutory scheme) + **LEGAL DEPENDENCY** + **RESEARCH REQUIRED** — exact beneficiaries/amounts **UNKNOWN** here; Round 2 PDF **NOT FOUND** |
| Other legally required obligations (contracts, bonds supported by lottery, federal conditions) | **LEGAL DEPENDENCY** + **UNKNOWN** until evidenced |
| Historical lottery collections as future Bill A entitlement | **REJECTED** as automatic entitlement; current receipt ≠ future entitlement |
| Using remaining lottery dollars as both full governmental revenue and individual capital | **FORBIDDEN** by revenue conservation (WD-BILL-A-138) |

## 4. Firewalls

Do not assume existing lottery beneficiaries possess permanent Future-State entitlement.  
Do not assume they possess no legally protected claim.  
Do not establish the final lottery distribution formula.  
Lottery architecture **must not** depend on ALL-OUT surviving (hold: WD-BILL-A-129).

**Later status (CWC-CE-167):** Q-BILL-A-012 = **A**. Remaining **available** lottery governmental revenue is intended **primarily** for property-tax abatement/retirement, subject to later-identified legally required obligations Bill A cannot impair. Source of record: WD-BILL-A-145 / WD-BILL-A-146. This file remains the CWC-CE-166 interface exposure. Availability is a **classification problem** (WD-BILL-A-147 / WD-BILL-A-148), not a completed dollar assignment.

---

Libertas sine lapsu — Liberty without drift.
