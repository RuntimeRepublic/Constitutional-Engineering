# Phone-First Public-Review PDF Rendering Standard — Draft 1.12 (CWC-CE-177)

**Document ID:** PR-PDF-RENDER-002  
**Governing Work Card:** CWC-CE-177  
**Status:** CANDIDATE (pending Human visual acceptance; not Git-canonicalized by this CWC)  
**Supersedes for Draft 1.12 production only:** PR-PDF-RENDER-001 binding to Draft 1.10 / SHA `9e96c1b…`  
**Does not erase:** Historical CWC-CE-161 / PR-PDF-RENDER-001 / Draft 1.10 PDF identity

---

## 1. Identity firewall

| Item | Value |
|---|---|
| OLD RENDERER IDENTITY | PR-PDF-RENDER-001 / CWC-CE-161 / `render_phone_first_pdf.py` |
| OLD SOURCE SHA (historical) | `9e96c1b96ed46e28ac9515065d9331fd78b62bcf` |
| OLD ARTIFACTS | `Bill-A-LOU-004-Public-Review-Draft-1.10.pdf`, `Bill-A-LOU-004-Review-Summary.pdf` |
| NEW CANDIDATE RENDERER IDENTITY | PR-PDF-RENDER-002 / CWC-CE-177 / `render_draft_1_12_public_review.py` |
| NEW SOURCE BASELINE | `e3151e5ac3f8cdb6fc25ac6b36bf418072f723fb` |
| NEW ARTIFACTS | `Bill-A-LOU-004-Public-Review-Draft-1.12.pdf`, `Bill-A-Engineering-a-New-Kansas-Tax-System-White-Paper-Draft-1.12.pdf` |

Historical Draft 1.10 PDFs and the CE-161 renderer remain historically accurate. Do not overwrite them.

---

## 2. Authority model

```text
CANONICAL DRAFT 1.12 SOURCE (SHA e3151e5…)
→ CONTROLLED RENDERER (PRESENTATION ONLY)
→ DRAFT 1.12 PDF CANDIDATES
→ TECHNICAL VALIDATION
→ HUMAN VISUAL REVIEW
```

The renderer does not govern Human Intent. LOU-004 controls. The White Paper explains the LOU.

---

## 3. Toolchain

| Layer | Choice |
|---|---|
| Layout | ReportLab (phone-first 6×9 in) |
| Inspection | PyMuPDF |
| SVG diagrams | Deterministic rasterization via PyMuPDF `Pixmap` → PNG embed (aspect preserved) |
| Primary entrypoint | `renderer/render_draft_1_12_public_review.py` |
| Validation | `renderer/validate_ce177.py` |

---

## 4. Page / typography (preserved from successful CE-161 phone-first)

| Parameter | Value |
|---|---|
| Page | 6 in × 9 in portrait |
| Margins | ≈ 0.55 in (bottom ≈ 0.65 in) |
| Body | Helvetica 10.5 pt / leading 14.5 |
| H1/H2/H3 | 14 / 12 / 11 pt |

---

## 5. Draft 1.12 remediation vs CE-161

CE-161 could not safely render Draft 1.12 because it:

1. pinned canonical SHA to Draft 1.10 era `9e96c1b…`;
2. emitted Draft 1.10 cover/control text and filenames;
3. rendered LOU + WD-BILL-A-113 only (no White Paper Draft 1.12);
4. had no Markdown image / SVG embedding path for WP-DIAG-* diagrams.

PR-PDF-RENDER-002 remediates presentation capability only.
