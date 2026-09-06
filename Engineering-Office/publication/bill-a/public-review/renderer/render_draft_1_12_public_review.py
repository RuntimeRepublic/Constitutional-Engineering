#!/usr/bin/env python3
"""
CWC-CE-177 / PR-PDF-RENDER-002 — Draft 1.12 phone-first public-review PDF renderer.

Candidate identity (does not overwrite historical CWC-CE-161 / PR-PDF-RENDER-001).

Page: 6in × 9in portrait. Selectable/searchable text. Clickable URLs.
SVG diagrams: deterministic PyMuPDF rasterization → PNG embed.
Formatting-only transforms (wide tables → stacked Field/Value). No Human Intent rewrite.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path

import pymupdf
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    HRFlowable,
    Image,
    KeepTogether,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# --- Identity ---
RENDERER_ID = "PR-PDF-RENDER-002"
CWC_ID = "CWC-CE-177"
HISTORICAL_RENDERER_ID = "PR-PDF-RENDER-001 / CWC-CE-161"
CANONICAL_SHA = "e3151e5ac3f8cdb6fc25ac6b36bf418072f723fb"
REPO_URL = "https://github.com/jhodges07/Constitutional-Engineering"
PROJECT_URL_DISPLAY = "BlueprintLiberty.com"
PROJECT_URL_HREF = "https://BlueprintLiberty.com"

PAGE_W = 6 * inch
PAGE_H = 9 * inch
MARGIN = 0.55 * inch
USABLE_W = PAGE_W - 2 * MARGIN
USABLE_H = PAGE_H - 0.55 * inch - 0.65 * inch
SVG_DPI = 180
# Fixed metadata timestamps for content-stable reproducibility evaluation
FIXED_PDF_DATE = "D:20260905210000-05'00'"

INTENTIONAL_DIAGRAM_GAP = "WP-DIAG-008"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[5]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def verify_source_state(root: Path) -> None:
    head = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    origin = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "origin/main"], text=True
    ).strip()
    if head != CANONICAL_SHA or origin != CANONICAL_SHA:
        raise SystemExit(
            f"STOP: source state mismatch. expected={CANONICAL_SHA} HEAD={head} origin/main={origin}"
        )


def escape_xml(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def inline_md(text: str) -> str:
    """Convert limited Markdown inline markup to ReportLab rich text."""
    s = escape_xml(text)
    s = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+|https://BlueprintLiberty\.com|BlueprintLiberty\.com)\)",
        lambda m: (
            f'<link href="{escape_xml(m.group(2) if m.group(2).startswith("http") else "https://" + m.group(2))}" '
            f'color="blue"><u>{m.group(1)}</u></link>'
        ),
        s,
    )
    s = re.sub(
        r"(?<![\"'>])(https://[^\s<>\]]+)",
        lambda m: f'<link href="{escape_xml(m.group(1))}" color="blue"><u>{escape_xml(m.group(1))}</u></link>',
        s,
    )
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"`([^`]+)`", r'<font face="Courier" size="9">\1</font>', s)
    return s


def split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def is_separator_row(cells: list[str]) -> bool:
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) is not None for c in cells if c != "")


def reformat_tables(md: str) -> tuple[str, int]:
    """Wide tables → stacked Field/Value blocks. Returns (md, wide_table_count)."""
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    wide_count = 0
    while i < len(lines):
        if not lines[i].strip().startswith("|"):
            out.append(lines[i])
            i += 1
            continue
        block: list[str] = []
        j = i
        while j < len(lines) and lines[j].strip().startswith("|"):
            block.append(lines[j])
            j += 1
        if len(block) < 2:
            out.extend(block)
            i = j
            continue
        header = split_table_row(block[0])
        sep = split_table_row(block[1])
        if not is_separator_row(sep):
            out.extend(block)
            i = j
            continue
        data_rows = [split_table_row(r) for r in block[2:]]
        max_cell = max((len(c) for row in ([header] + data_rows) for c in row), default=0)
        wide = len(header) >= 3 or max_cell > 42 or any(len(row) > 2 for row in data_rows)
        if not wide and len(header) == 2:
            out.extend(block)
            i = j
            continue
        wide_count += 1
        out.append("")
        out.append("*[Table reformatted for phone-first readability — cell text unchanged]*")
        out.append("")
        for n, row in enumerate(data_rows, start=1):
            cells = list(row) + [""] * max(0, len(header) - len(row))
            cells = cells[: len(header)]
            out.append(f"**Table row {n}**")
            out.append("")
            for h, c in zip(header, cells):
                hh = h if h else "Field"
                out.append(f"- **{hh}:** {c}")
            out.append("")
        i = j
    return "\n".join(out), wide_count


def build_styles():
    base = getSampleStyleSheet()
    return {
        "CoverTitle": ParagraphStyle(
            "CoverTitle",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "CoverSub": ParagraphStyle(
            "CoverSub",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=16,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "CoverWarn": ParagraphStyle(
            "CoverWarn",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "H1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            spaceBefore=14,
            spaceAfter=8,
            textColor=colors.black,
        ),
        "H2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            spaceBefore=11,
            spaceAfter=6,
        ),
        "H3": ParagraphStyle(
            "H3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            spaceBefore=9,
            spaceAfter=5,
        ),
        "Body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=14.5,
            alignment=TA_JUSTIFY,
            spaceBefore=2,
            spaceAfter=6,
        ),
        "Bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=14.5,
            leftIndent=12,
            spaceBefore=1,
            spaceAfter=3,
        ),
        "Meta": ParagraphStyle(
            "Meta",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            spaceBefore=1,
            spaceAfter=3,
        ),
        "Caption": ParagraphStyle(
            "Caption",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=11.5,
            alignment=TA_CENTER,
            spaceBefore=4,
            spaceAfter=10,
        ),
        "Code": ParagraphStyle(
            "Code",
            parent=base["Code"],
            fontName="Courier",
            fontSize=8.5,
            leading=11,
            backColor=colors.Color(0.96, 0.96, 0.96),
            spaceBefore=6,
            spaceAfter=8,
        ),
        "Center": ParagraphStyle(
            "Center",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=14,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "SmallCenter": ParagraphStyle(
            "SmallCenter",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            spaceAfter=3,
        ),
    }


class NumberedCanvas(Canvas):
    def __init__(self, *args, footer_right: str = "", **kwargs):
        self._footer_right = footer_right
        Canvas.__init__(self, *args, **kwargs)

    def showPage(self):
        self._draw_footer()
        Canvas.showPage(self)

    def save(self):
        self._draw_footer()
        Canvas.save(self)

    def _draw_footer(self):
        # Guard against ReportLab drawing the last-page footer twice (showPage + save).
        if getattr(self, "_footer_drawn_for", None) == self._pageNumber:
            return
        self._footer_drawn_for = self._pageNumber
        self.saveState()
        self.setStrokeColor(colors.grey)
        self.setLineWidth(0.4)
        y = 0.38 * inch
        self.line(MARGIN, y + 10, PAGE_W - MARGIN, y + 10)
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.black)
        self.drawString(MARGIN, y, "BlueprintLiberty.com")
        page = self._pageNumber
        self.drawCentredString(PAGE_W / 2, y, str(page))
        self.drawRightString(PAGE_W - MARGIN, y, self._footer_right[:48])
        self.restoreState()


def control_table(rows: list[tuple[str, str]], styles) -> Table:
    data = []
    for k, v in rows:
        if v.startswith("http"):
            val = f'<link href="{escape_xml(v)}" color="blue"><u>{escape_xml(v)}</u></link>'
        else:
            val = inline_md(v)
        data.append(
            [
                Paragraph(f"<b>{escape_xml(k)}</b>", styles["Meta"]),
                Paragraph(val, styles["Meta"]),
            ]
        )
    col_w = [1.55 * inch, PAGE_W - 2 * MARGIN - 1.55 * inch]
    t = Table(data, colWidths=col_w, hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.5, colors.grey),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("BACKGROUND", (0, 0), (0, -1), colors.Color(0.95, 0.95, 0.95)),
            ]
        )
    )
    return t


def cover_flowables(kind: str, styles) -> list:
    if kind == "lou":
        notice = """THIS DOCUMENT IS PROVIDED FOR PUBLIC REVIEW AND COMMENT.

IT IS NOT ENACTED LAW.
IT IS NOT PROPOSED LEGISLATIVE TEXT.
IT IS NOT FINAL.
IT IS NOT HG-D1 ACCEPTED.

LOU-004 DRAFT 1.12 IS A PUBLIC REVIEW DRAFT CANDIDATE.
IT HAS NOT YET BEEN HUMAN-ACCEPTED.

HG-D1 HAS NOT PASSED.
BILL A MATURITY = 19% UNCHANGED.

COMMENTS AND PROPOSALS FROM REVIEWERS DO NOT AUTOMATICALLY ALTER THE CONTROLLED LOU.
THE HUMAN ENGINEER RETAINS FINAL AUTHORITY OVER HUMAN INTENT.
PUBLICATION FOR COMMENT IS NOT AUTHORIZED BY THIS RENDER CYCLE."""
    else:
        notice = """THIS WHITE PAPER IS A DERIVATIVE EXPLANATORY ARTIFACT.

PUBLIC REVIEW DRAFT — FOR COMMENT.
NOT FINAL.
NOT HG-D1 ACCEPTED.
NOT PROPOSED STATUTORY TEXT.
NOT SOURCE TRUTH.

LOU-004 DRAFT 1.12 CONTROLS HUMAN INTENT.
WHERE THIS WHITE PAPER AND THE LOU DIFFER, THE LOU GOVERNS.

HG-D1 HAS NOT PASSED.
BILL A MATURITY = 19% UNCHANGED.
HUMAN SILENCE IS NOT ACCEPTANCE.
PUBLICATION FOR COMMENT IS NOT AUTHORIZED BY THIS RENDER CYCLE."""

    story: list = []
    story.append(Spacer(1, 0.28 * inch))
    story.append(Paragraph("BILL A", styles["CoverTitle"]))
    story.append(Paragraph("COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT", styles["CoverSub"]))
    story.append(Spacer(1, 0.12 * inch))

    if kind == "lou":
        story.append(Paragraph("LETTER OF UNDERSTANDING", styles["Center"]))
        story.append(Paragraph("LOU-004", styles["CoverTitle"]))
        story.append(Paragraph("DRAFT 1.12", styles["CoverSub"]))
        story.append(Paragraph("PUBLIC REVIEW DRAFT CANDIDATE", styles["CoverWarn"]))
    else:
        story.append(Paragraph("BILL A: ENGINEERING A NEW KANSAS TAX SYSTEM", styles["CoverSub"]))
        story.append(
            Paragraph(
                "A Plain-Language White Paper Explaining LOU-004 Draft 1.12",
                styles["Center"],
            )
        )
        story.append(Spacer(1, 0.08 * inch))
        story.append(Paragraph("WHITE PAPER — DRAFT 1.12", styles["CoverSub"]))
        story.append(Paragraph("DERIVATIVE EXPLANATORY ARTIFACT", styles["CoverWarn"]))

    story.append(Spacer(1, 0.08 * inch))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.12 * inch))
    story.append(Paragraph("PUBLIC REVIEW DRAFT — FOR COMMENT", styles["CoverWarn"]))
    story.append(Paragraph("NOT FINAL", styles["CoverWarn"]))
    story.append(Paragraph("NOT HUMAN-ACCEPTED", styles["CoverWarn"]))
    story.append(Paragraph("NOT PROPOSED STATUTORY TEXT", styles["CoverWarn"]))
    story.append(Paragraph("HG-D1 NOT PASSED", styles["CoverWarn"]))
    if kind == "whitepaper":
        story.append(Paragraph("LOU-004 CONTROLS HUMAN INTENT", styles["CoverWarn"]))
    story.append(Spacer(1, 0.18 * inch))
    story.append(
        Paragraph(
            f'Project URL: <link href="{PROJECT_URL_HREF}" color="blue"><u>{PROJECT_URL_DISPLAY}</u></link>',
            styles["Center"],
        )
    )
    story.append(
        Paragraph(
            f'Canonical repository:<br/><link href="{REPO_URL}" color="blue"><u>{REPO_URL}</u></link>',
            styles["SmallCenter"],
        )
    )
    story.append(Spacer(1, 0.14 * inch))
    story.append(Paragraph("Document-control block", styles["H2"]))

    if kind == "lou":
        rows = [
            ("Document", "LOU-004"),
            ("Bill", "Bill A — Comprehensive Kansas Tax-System Replacement"),
            ("Draft", "1.12"),
            ("Review status", "PUBLIC REVIEW DRAFT CANDIDATE"),
            ("Human acceptance", "NOT HUMAN-ACCEPTED"),
            ("HG-D1", "NOT PASSED"),
            ("Bill A maturity", "19% UNCHANGED"),
            ("Renderer", f"{RENDERER_ID} / {CWC_ID}"),
            ("Canonical repository", "Constitutional-Engineering"),
            ("Canonical Git SHA", CANONICAL_SHA),
            ("Repository URL", REPO_URL),
            ("Project URL", PROJECT_URL_DISPLAY),
        ]
    else:
        rows = [
            ("Document", "Bill A White Paper"),
            ("Title", "BILL A: ENGINEERING A NEW KANSAS TAX SYSTEM"),
            ("Subtitle", "A Plain-Language White Paper Explaining LOU-004 Draft 1.12"),
            ("Draft", "1.12"),
            ("Role", "DERIVATIVE EXPLANATORY ARTIFACT — NOT SOURCE TRUTH"),
            ("Governing LOU", "LOU-004 Draft 1.12"),
            ("Review status", "PUBLIC REVIEW DRAFT — FOR COMMENT"),
            ("Human acceptance", "NOT HUMAN-ACCEPTED"),
            ("HG-D1", "NOT PASSED"),
            ("Bill A maturity", "19% UNCHANGED"),
            ("Renderer", f"{RENDERER_ID} / {CWC_ID}"),
            ("Canonical Git SHA", CANONICAL_SHA),
            ("Repository URL", REPO_URL),
            ("Project URL", PROJECT_URL_DISPLAY),
        ]
    story.append(control_table(rows, styles))
    story.append(Spacer(1, 0.14 * inch))
    story.append(Paragraph("Authority notice", styles["H2"]))
    story.append(Preformatted(notice, styles["Code"]))
    story.append(PageBreak())
    return story


def rasterize_svg_to_png_path(svg_path: Path, cache_dir: Path) -> Path:
    """Deterministic SVG → PNG via PyMuPDF. Preserves aspect; no generative transform."""
    out = cache_dir / (svg_path.stem + f"-dpi{SVG_DPI}.png")
    if out.is_file() and out.stat().st_mtime >= svg_path.stat().st_mtime:
        return out
    doc = pymupdf.open(svg_path)
    try:
        pix = doc[0].get_pixmap(dpi=SVG_DPI)
        out.parent.mkdir(parents=True, exist_ok=True)
        pix.save(str(out))
    finally:
        doc.close()
    return out


def make_diagram_flowables(
    img_path: Path,
    alt: str,
    styles,
    resolved_diagrams: list[dict],
) -> list:
    """Embed diagram at readable size; KeepTogether to avoid mid-diagram page splits."""
    # Scale to usable width; if still taller than ~0.85 usable height, scale to height.
    # ReportLab Image uses points.
    from PIL import Image as PILImage

    with PILImage.open(img_path) as im:
        pw, ph = im.size
    aspect = ph / float(pw) if pw else 1.0
    w = USABLE_W
    h = w * aspect
    max_h = USABLE_H * 0.88
    if h > max_h:
        h = max_h
        w = h / aspect if aspect else USABLE_W

    flow = Image(str(img_path), width=w, height=h)
    flow.hAlign = "CENTER"
    caption = Paragraph(escape_xml(alt) if alt else escape_xml(img_path.stem), styles["Caption"])
    block = KeepTogether([Spacer(1, 0.08 * inch), flow, caption])
    resolved_diagrams.append(
        {
            "alt": alt,
            "source": str(img_path),
            "embed_width_pt": round(w, 2),
            "embed_height_pt": round(h, 2),
            "pixel_w": pw,
            "pixel_h": ph,
            "conversion": f"PyMuPDF pixmap dpi={SVG_DPI} → PNG",
        }
    )
    return [block]


IMG_RE = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$")


def parse_md_to_flowables(
    md: str,
    styles,
    *,
    source_dir: Path,
    cache_dir: Path,
    resolved_diagrams: list[dict],
) -> tuple[list, dict]:
    md, wide_tables = reformat_tables(md)
    lines = md.splitlines()
    story: list = []
    i = 0
    para_buf: list[str] = []
    in_code = False
    code_buf: list[str] = []
    headings: list[tuple[int, str]] = []
    stats = {
        "wide_tables_reformatted": wide_tables,
        "compact_tables_kept": 0,
        "images_embedded": 0,
        "images_skipped_intentional_gap": 0,
    }

    def flush_para():
        nonlocal para_buf
        if not para_buf:
            return
        text = " ".join(x.strip() for x in para_buf)
        if text:
            if text.startswith("**") and ":**" in text[:80]:
                story.append(Paragraph(inline_md(text), styles["Meta"]))
            else:
                story.append(Paragraph(inline_md(text), styles["Body"]))
        para_buf = []

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            if in_code:
                flush_para()
                story.append(Preformatted("\n".join(code_buf), styles["Code"]))
                code_buf = []
                in_code = False
            else:
                flush_para()
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue

        m_img = IMG_RE.match(line.strip())
        if m_img:
            flush_para()
            alt, rel = m_img.group(1), m_img.group(2)
            if INTENTIONAL_DIAGRAM_GAP in rel or INTENTIONAL_DIAGRAM_GAP in alt:
                stats["images_skipped_intentional_gap"] += 1
                story.append(
                    Paragraph(
                        f"<i>[Intentional diagram gap — {INTENTIONAL_DIAGRAM_GAP} not created; "
                        "no substitute image used.]</i>",
                        styles["Caption"],
                    )
                )
                i += 1
                continue
            target = (source_dir / rel).resolve()
            if not target.is_file():
                raise SystemExit(f"STOP: diagram path not found: {rel} → {target}")
            if target.suffix.lower() == ".svg":
                png = rasterize_svg_to_png_path(target, cache_dir)
            else:
                png = target
            story.extend(make_diagram_flowables(png, alt, styles, resolved_diagrams))
            stats["images_embedded"] += 1
            i += 1
            continue

        if line.strip().startswith("|"):
            flush_para()
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            if len(block) >= 2 and is_separator_row(split_table_row(block[1])):
                header = split_table_row(block[0])
                rows = [split_table_row(r) for r in block[2:]]
                data = [[Paragraph(inline_md(c), styles["Meta"]) for c in header]]
                for r in rows:
                    cells = list(r) + [""] * max(0, len(header) - len(r))
                    data.append(
                        [Paragraph(inline_md(c), styles["Meta"]) for c in cells[: len(header)]]
                    )
                usable = USABLE_W
                if len(header) == 2:
                    widths = [usable * 0.38, usable * 0.62]
                else:
                    widths = [usable / len(header)] * len(header)
                t = Table(data, colWidths=widths, hAlign="LEFT", repeatRows=1)
                t.setStyle(
                    TableStyle(
                        [
                            ("BOX", (0, 0), (-1, -1), 0.5, colors.grey),
                            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
                            ("BACKGROUND", (0, 0), (-1, 0), colors.Color(0.93, 0.93, 0.93)),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 3),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                            ("TOPPADDING", (0, 0), (-1, -1), 3),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                        ]
                    )
                )
                story.append(t)
                story.append(Spacer(1, 0.08 * inch))
                stats["compact_tables_kept"] += 1
            else:
                for b in block:
                    story.append(Paragraph(inline_md(b), styles["Meta"]))
            continue

        if not line.strip():
            flush_para()
            i += 1
            continue

        if line.startswith("# "):
            flush_para()
            t = line[2:].strip()
            headings.append((1, t))
            story.append(Paragraph(inline_md(t), styles["H1"]))
            i += 1
            continue
        if line.startswith("## "):
            flush_para()
            t = line[3:].strip()
            headings.append((2, t))
            story.append(Paragraph(inline_md(t), styles["H2"]))
            i += 1
            continue
        if line.startswith("### "):
            flush_para()
            t = line[4:].strip()
            headings.append((3, t))
            story.append(Paragraph(inline_md(t), styles["H3"]))
            i += 1
            continue
        if line.startswith("#### "):
            flush_para()
            t = line[5:].strip()
            headings.append((3, t))
            story.append(Paragraph(inline_md(t), styles["H3"]))
            i += 1
            continue

        if re.match(r"^[-*]\s+", line.strip()):
            flush_para()
            text = re.sub(r"^[-*]\s+", "", line.strip())
            story.append(Paragraph("• " + inline_md(text), styles["Bullet"]))
            i += 1
            continue
        if re.match(r"^\d+\.\s+", line.strip()):
            flush_para()
            story.append(Paragraph(inline_md(line.strip()), styles["Bullet"]))
            i += 1
            continue
        if line.strip() == "---":
            flush_para()
            story.append(
                HRFlowable(width="100%", thickness=0.6, color=colors.grey, spaceBefore=6, spaceAfter=6)
            )
            i += 1
            continue

        para_buf.append(line)
        i += 1

    flush_para()
    if in_code and code_buf:
        story.append(Preformatted("\n".join(code_buf), styles["Code"]))
    stats["headings"] = headings
    return story, stats


def deterministic_pdf_ids(artifact_key: str) -> tuple[str, str]:
    """Stable trailer /ID pair derived from source SHA + renderer + artifact key (not wall-clock)."""
    seed = f"{CANONICAL_SHA}|{RENDERER_ID}|{CWC_ID}|{artifact_key}".encode("utf-8")
    h = hashlib.sha256(seed).hexdigest().upper()
    return h[:32], h[32:64]


def stabilize_pdf_metadata(out_pdf: Path, title: str, subject: str, artifact_key: str) -> None:
    """Normalize PDF metadata dates and trailer /ID for byte-stable reproducibility."""
    doc = pymupdf.open(out_pdf)
    try:
        doc.set_metadata(
            {
                "title": title,
                "author": "Constitutional Engineering Office / BlueprintLiberty",
                "subject": subject,
                "creator": f"{CWC_ID} / {RENDERER_ID} phone-first renderer (ReportLab)",
                "producer": f"{RENDERER_ID}",
                "creationDate": FIXED_PDF_DATE,
                "modDate": FIXED_PDF_DATE,
                "keywords": (
                    f"Bill A, LOU-004, Draft 1.12, Public Review Draft Candidate, "
                    f"NOT HUMAN-ACCEPTED, HG-D1 NOT PASSED, {CANONICAL_SHA}"
                ),
            }
        )
        tmp = out_pdf.with_suffix(".tmp.pdf")
        doc.save(tmp, garbage=4, deflate=True)
    finally:
        doc.close()
    # Rewrite trailer /ID (ReportLab/MuPDF emit random IDs — sole prior reproducibility gap).
    id1, id2 = deterministic_pdf_ids(artifact_key)
    raw = tmp.read_bytes()
    new_raw, n = re.subn(
        rb"/ID\s*\[\s*<[0-9A-Fa-f]+>\s*<[0-9A-Fa-f]+>\s*\]",
        f"/ID[<{id1}><{id2}>]".encode("ascii"),
        raw,
        count=1,
    )
    if n != 1:
        raise SystemExit(f"STOP: could not stabilize PDF /ID in {out_pdf.name} (replacements={n})")
    tmp.write_bytes(new_raw)
    tmp.replace(out_pdf)


def render_pdf(
    *,
    kind: str,
    source: Path,
    out_pdf: Path,
    footer_right: str,
    title: str,
    subject: str,
    cache_dir: Path,
    artifact_key: str | None = None,
) -> dict:
    styles = build_styles()
    body = source.read_text(encoding="utf-8")
    resolved: list[dict] = []
    body_flows, stats = parse_md_to_flowables(
        body,
        styles,
        source_dir=source.parent,
        cache_dir=cache_dir,
        resolved_diagrams=resolved,
    )
    story = cover_flowables(kind, styles) + body_flows

    out_pdf.parent.mkdir(parents=True, exist_ok=True)

    def make_canvas(filename, **kwargs):
        return NumberedCanvas(filename, footer_right=footer_right, **kwargs)

    doc = SimpleDocTemplate(
        str(out_pdf),
        pagesize=(PAGE_W, PAGE_H),
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=0.55 * inch,
        bottomMargin=0.65 * inch,
        title=title,
        author="Constitutional Engineering Office / BlueprintLiberty",
        subject=subject,
        creator=f"{CWC_ID} / {RENDERER_ID} phone-first public-review renderer (ReportLab)",
        keywords=(
            "Bill A, LOU-004, Draft 1.12, Public Review Draft Candidate, "
            "NOT HUMAN-ACCEPTED, HG-D1 NOT PASSED, " + CANONICAL_SHA
        ),
    )
    doc.build(story, canvasmaker=make_canvas)
    key = artifact_key or out_pdf.name
    stabilize_pdf_metadata(out_pdf, title, subject, artifact_key=key)

    pdf = pymupdf.open(out_pdf)
    page_count = pdf.page_count
    r = pdf[0].rect
    pdf.close()
    return {
        "filename": out_pdf.name,
        "path": str(out_pdf),
        "pdf_sha256": sha256_file(out_pdf),
        "file_size_bytes": out_pdf.stat().st_size,
        "page_count": page_count,
        "page_width_pt": round(r.width, 2),
        "page_height_pt": round(r.height, 2),
        "parse_stats": {
            k: v for k, v in stats.items() if k != "headings"
        },
        "heading_count": len(stats.get("headings", [])),
        "diagrams": resolved,
    }


def main() -> int:
    root = repo_root()
    pub = Path(__file__).resolve().parents[1]
    pdf_dir = pub / "pdf"
    cache_dir = Path(__file__).resolve().parent / "_build" / "ce177-diagram-cache"
    verify_source_state(root)

    lou_src = root / (
        "Engineering-Office/definition/LOU-004-Bill-A-Comprehensive-Kansas-Tax-System-Replacement.md"
    )
    wp_src = root / (
        "Engineering-Office/publication/bill-a/public-review/white-paper/source/"
        "Bill-A-Engineering-a-New-Kansas-Tax-System-White-Paper.md"
    )
    for p, label in ((lou_src, "LOU"), (wp_src, "White Paper")):
        if not p.is_file():
            raise SystemExit(f"STOP: missing {label} source: {p}")
        text = p.read_text(encoding="utf-8")
        if "Draft 1.12" not in text and "DRAFT 1.12" not in text and "Version:** Draft 1.12" not in text:
            # soft check — LOU uses Version: Draft 1.12
            if "1.12" not in text[:2500]:
                raise SystemExit(f"STOP: {label} does not appear to be Draft 1.12: {p}")

    # Historical Draft 1.10 PDFs must remain
    hist = [
        pdf_dir / "Bill-A-LOU-004-Public-Review-Draft-1.10.pdf",
        pdf_dir / "Bill-A-LOU-004-Review-Summary.pdf",
    ]
    hist_sha = {h.name: sha256_file(h) if h.is_file() else None for h in hist}

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    artifacts = []

    lou_name = "Bill-A-LOU-004-Public-Review-Draft-1.12.pdf"
    a = render_pdf(
        kind="lou",
        source=lou_src,
        out_pdf=pdf_dir / lou_name,
        footer_right="LOU-004 Draft 1.12 | Public Review Candidate",
        title="Bill A LOU-004 Public Review Draft 1.12",
        subject=(
            f"Public-review PDF from LOU-004 Draft 1.12 @ {CANONICAL_SHA} — "
            "NOT HUMAN-ACCEPTED — NOT HG-D1"
        ),
        cache_dir=cache_dir,
        artifact_key=lou_name,
    )
    a["source_markdown"] = str(lou_src.relative_to(root)).replace("\\", "/")
    a["source_git_sha"] = CANONICAL_SHA
    a["path"] = str(Path(a["path"]).relative_to(root)).replace("\\", "/")
    a["kind"] = "lou"
    artifacts.append(a)
    print("LOU PDF", a["page_count"], "pages", a["pdf_sha256"])

    wp_name = "Bill-A-Engineering-a-New-Kansas-Tax-System-White-Paper-Draft-1.12.pdf"
    b = render_pdf(
        kind="whitepaper",
        source=wp_src,
        out_pdf=pdf_dir / wp_name,
        footer_right="White Paper Draft 1.12 | Derivative ≠ LOU",
        title="Bill A White Paper Draft 1.12 — Engineering a New Kansas Tax System",
        subject=(
            f"Derivative explanatory White Paper for LOU-004 Draft 1.12 @ {CANONICAL_SHA} — "
            "NOT SOURCE TRUTH — NOT HUMAN-ACCEPTED"
        ),
        cache_dir=cache_dir,
        artifact_key=wp_name,
    )
    b["source_markdown"] = str(wp_src.relative_to(root)).replace("\\", "/")
    b["source_git_sha"] = CANONICAL_SHA
    b["path"] = str(Path(b["path"]).relative_to(root)).replace("\\", "/")
    b["kind"] = "whitepaper"
    artifacts.append(b)
    print("White Paper PDF", b["page_count"], "pages", b["pdf_sha256"], "diagrams", len(b["diagrams"]))

    # Confirm historical PDFs untouched
    hist_after = {h.name: sha256_file(h) if h.is_file() else None for h in hist}
    if hist_sha != hist_after:
        raise SystemExit(f"STOP: historical Draft 1.10 PDFs changed: before={hist_sha} after={hist_after}")

    identity = {
        "cwc": CWC_ID,
        "renderer_identity": RENDERER_ID,
        "historical_renderer_identity": HISTORICAL_RENDERER_ID,
        "canonical_git_sha": CANONICAL_SHA,
        "render_timestamp_utc": stamp,
        "toolchain": (
            "Python ReportLab + PyMuPDF SVG→PNG (dpi=180) + Pillow size probe; "
            "phone-first table reformatting; fixed PDF metadata dates for reproducibility eval"
        ),
        "svg_conversion_method": f"pymupdf.open(svg).get_pixmap(dpi={SVG_DPI}).save(png)",
        "page_size": "6in x 9in portrait (432pt x 648pt)",
        "fixed_pdf_metadata_date": FIXED_PDF_DATE,
        "historical_draft_1_10_pdf_sha256": hist_after,
        "artifacts": artifacts,
        "human_visual_acceptance": "PENDING",
        "publication": "NOT AUTHORIZED",
        "git": "NOT STAGED / NOT COMMITTED / NOT PUSHED BY THIS RENDERER",
    }
    out_id = pub / "validation" / "CWC-CE-177-ARTIFACT-IDENTITY.json"
    out_id.parent.mkdir(parents=True, exist_ok=True)
    out_id.write_text(json.dumps(identity, indent=2) + "\n", encoding="utf-8")
    print("wrote", out_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
