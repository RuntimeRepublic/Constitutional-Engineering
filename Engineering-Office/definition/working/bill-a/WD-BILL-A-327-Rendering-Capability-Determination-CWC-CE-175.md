# WD-BILL-A-327 — Rendering Capability Determination A / B

**Document ID:** WD-BILL-A-327  
**Source ID:** SRC-BILL-A-562  
**Governing Work Card:** CWC-CE-175  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / CYCLE RECORD — NOT HUMAN-ACCEPTED — NOT PUBLICATION  
**Version:** 1.0.0  
**Effective Date:** 2026-09-05  

```text
PDF = RENDERING REMEDIATION REQUIRED
CLASSIFICATION B
```

Current CWC-CE-161 renderer (`render_phone_first_pdf.py` / `validate_ce161.py`) still pins:

- CANONICAL_SHA = 9e96c1b... (pre-CE-163);
- Draft 1.10 filenames, banners, and validation checks;
- SHA check would fail against HEAD 9eed44b and against uncommitted Draft 1.12 working-tree source;
- White Paper diagrams are not safely embeddable under the existing renderer architecture.

Updating those pins would be a meaningful renderer change. CWC-CE-175 prohibits improvisation.

Historical Draft 1.10 PDFs do **not** represent Draft 1.12. PDF absence is not a source-truth failure. Source remains Markdown.

---

Libertas sine lapsu — Liberty without drift.
