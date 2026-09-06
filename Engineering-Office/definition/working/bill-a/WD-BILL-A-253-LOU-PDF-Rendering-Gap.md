# WD-BILL-A-253 — LOU PDF Candidate / Rendering-Gap Record

**Document ID:** WD-BILL-A-253  
**Source ID:** SRC-BILL-A-488  
**Governing Work Card:** CWC-CE-172  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** RENDERING GAP — CONTROLLED REMEDIATION REQUIRED  
**Version:** 1.0.0  
**Effective Date:** 2026-09-05  

```text
RENDERING GAP — CONTROLLED REMEDIATION REQUIRED
DO NOT TREAT HISTORICAL DRAFT 1.10 PDFs AS DRAFT 1.11
```

Existing CWC-CE-161 renderer (`render_phone_first_pdf.py` / `render_bill_a_public_review.py`):

- hard-pins `CANONICAL_SHA = 9e96c1b…` (pre-CE-163);
- labels / filenames still Draft 1.10;
- SHA check would fail against current HEAD `9eed44b…` and against uncommitted Draft 1.11 working-tree source.

Updating SHA pins, filenames, and Draft 1.11 banners would be a **meaningful renderer change**. CWC-CE-172 prohibits silent renderer-architecture improvisation.

| Field | Value |
|---|---|
| Filename | NONE produced |
| Page count | N/A |
| Dimensions | Intended ~6 × 9 portrait (CE-161 standard) — not rendered |
| SHA-256 | N/A |
| Renderer identity | CE-161 ReportLab / optional pandoc path — **not safely reusable without remediation** |
| Validation | GAP |

Content of LOU-004 Draft 1.11 Markdown remains the LOU source. PDF absence is not a content-validation failure.

---

Libertas sine lapsu — Liberty without drift.
