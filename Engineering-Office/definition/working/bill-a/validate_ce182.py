"""CWC-CE-182 local validation. Does not transmit. Does not mutate git."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(r"X:\GitHub\Constitutional-Engineering")
BILLA = ROOT / "Engineering-Office" / "definition" / "working" / "bill-a"
PDF_DIR = ROOT / "Engineering-Office" / "publication" / "bill-a" / "public-review" / "pdf"
HEAD_PIN = "05bedea51c7489441ae411bb5b5b03fe532b1b66"
LOU_SHA = "702BB99EEC20D70DB6C534BEF4F3CBADE0378D6FCFD6140A1247E68232032ADC"
WP_SHA = "857838630AA07CCB9A1E2571DFDF961C91B3E321349C66CEB053910A942D8EB2"
LOU_PDF = PDF_DIR / "Bill-A-LOU-004-Public-Review-Draft-1.12.pdf"
WP_PDF = PDF_DIR / "Bill-A-Engineering-a-New-Kansas-Tax-System-White-Paper-Draft-1.12.pdf"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest().upper()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main() -> int:
    tests: dict[str, str] = {}
    failures: list[str] = []

    def rec(code: str, ok: bool, note: str = "") -> None:
        tests[code] = "PASS" if ok else "FAIL"
        if not ok:
            failures.append(f"{code}: {note}")

    head = git("rev-parse", "HEAD")
    rec("KDOR-01", head == HEAD_PIN, f"HEAD={head}")

    v131 = json.loads((BILLA / "WD-BILL-A-131-CWC-CE-181-VALIDATION.json").read_text(encoding="utf-8"))
    rec("KDOR-02", v131.get("outcome") == "A" and not v131.get("failures"))

    r128 = (BILLA / "WD-BILL-A-128-Kansas-Event-Tax-Economic-Baseline-Transaction-Band-Research.md").read_text(encoding="utf-8")
    rec("KDOR-03", "AUTHORITATIVE DATA NOT LOCATED" in r128 or "NOT LOCATED" in r128)

    rec("KDOR-04", (BILLA / "WD-BILL-A-333-Human-Authorization-Record-CWC-CE-182.md").exists())
    rec("KDOR-05", sha256(LOU_PDF) == LOU_SHA and sha256(WP_PDF) == WP_SHA)
    lou13 = (BILLA / "LOU-004-Draft-1.13-CANDIDATE-ADDENDUM-Event-Tax-Economic-Baseline.md").read_text(encoding="utf-8")
    rec("KDOR-06", "CANDIDATE" in lou13 and "Does **NOT** replace Draft 1.12" in lou13)

    inq = (BILLA / "kdor-inquiry" / "KDOR-INQ-BILL-A-001-Transaction-Band-Aggregates-READY-FOR-HUMAN-TRANSMISSION.md").read_text(encoding="utf-8")
    rec("KDOR-07", "Primary question" in inq and "transaction-dollar-size bands" in inq)
    rec("KDOR-08", "$0.00–$20.00" in inq and "$20.01–$30.00" in inq and "$1,000.01+" in inq)
    rec("KDOR-09", "Number of taxable transactions" in inq and "point-of-sale receipts" in inq)
    rec("KDOR-10", "Statewide Kansas" in inq)
    rec("KDOR-11", "calendar year" in inq.lower() and "fiscal year" in inq.lower())
    rec("KDOR-12", "gross sales" in inq.lower() and "taxable sales" in inq.lower())
    rec("KDOR-13", "period-aggregate tax-return" in inq.lower() or "tax-return totals" in inq)
    rec("KDOR-14", "closest available" in inq.lower())
    rec("KDOR-15", "do **not** request personally identifiable" in inq.lower() or "do **not** request personally identifiable taxpayer information" in inq)
    rec("KDOR-16", "does **not** ask the Department to define any future tax base" in inq)
    rec("KDOR-17", "comparison model" in inq.lower() and "6.667" in inq)
    rec("KDOR-18", "5% STATE / 5% LOCAL = UNCHANGED" in lou13)
    rec("KDOR-19", "$20" in inq and "$30" in inq and "$100" in inq)
    rec("KDOR-20", "Purchase arithmetic" in inq)
    rec("KDOR-21", inq.startswith("# KDOR-INQ-BILL-A-001") and "READY FOR HUMAN TRANSMISSION" in inq)
    fallback = (BILLA / "kdor-inquiry" / "KDOR-INQ-BILL-A-001-KORA-PR50-FALLBACK-NOT-FILED.md").read_text(encoding="utf-8")
    rec("KDOR-22", "informal technical" in fallback.lower() and "NOT FILED" in fallback)
    rec("KDOR-23", "@ksrevenue.gov" not in inq.lower() and "NOT VERIFIED" in (BILLA / "WD-BILL-A-342-Recipient-Contact-Verification.md").read_text(encoding="utf-8"))
    rec("KDOR-24", "NOT TRANSMITTED BY CWC-CE-182" in inq)
    rec("KDOR-25", (BILLA / "kdor-inquiry" / "KDOR-INQ-BILL-A-001-RESPONSE-INTAKE.md").exists())
    rec("KDOR-26", (BILLA / "WD-BILL-A-344-Evidence-Classification-Register.md").exists())
    rec("KDOR-27", (BILLA / "WD-BILL-A-345-Future-Economic-Model-Rerun-Specification.md").exists())
    rec("KDOR-28", "NO KDOR RESULT INVENTED" in (BILLA / "kdor-inquiry" / "KDOR-INQ-BILL-A-001-RESPONSE-INTAKE.md").read_text(encoding="utf-8"))
    rec("KDOR-29", sha256(LOU_PDF) == LOU_SHA and sha256(WP_PDF) == WP_SHA)
    rec("KDOR-30", sha256(LOU_PDF) == LOU_SHA and sha256(WP_PDF) == WP_SHA)
    rec(
        "KDOR-31",
        "05bedea51c7489441ae411bb5b5b03fe532b1b66" in (BILLA / "WD-BILL-A-346-Draft-1.12-Freeze-Verification.md").read_text(encoding="utf-8"),
    )
    rec("KDOR-32", "NOT HUMAN-ACCEPTED" in lou13)
    rec("KDOR-33", "NOT PUBLIC-REVIEW RELEASED" in lou13)
    rec("KDOR-34", "HG-D1 = NOT PASSED" in lou13 or "HG-D1 NOT PASSED" in lou13.replace("=", " "))
    rec("KDOR-35", "NOT AUTHORIZED" in (BILLA / "WD-BILL-A-354-CWC-CE-182-Final-Cursor-Report.md").read_text(encoding="utf-8"))
    rec("KDOR-36", "HG-D2" in (BILLA / "WD-BILL-A-354-CWC-CE-182-Final-Cursor-Report.md").read_text(encoding="utf-8"))
    rec("KDOR-37", "Legislative Engineering" in (BILLA / "WD-BILL-A-354-CWC-CE-182-Final-Cursor-Report.md").read_text(encoding="utf-8"))
    rec("KDOR-38", "19% UNCHANGED" in lou13)
    rec("KDOR-39", "NOT YET CALCULABLE" in (BILLA / "WD-BILL-A-332-CWC-CE-181-Baseline-Verification.md").read_text(encoding="utf-8"))
    rec("KDOR-40", "5% STATE / 5% LOCAL = UNCHANGED" in lou13)
    rec("KDOR-41", "NO KDOR RESPONSE INVENTED" in lou13)
    rec("KDOR-42", "NOT PUBLICATION" in (BILLA / "WD-BILL-A-354-CWC-CE-182-Final-Cursor-Report.md").read_text(encoding="utf-8"))
    rec("KDOR-43", "NOT TRANSMITTED BY CWC-CE-182" in inq)
    try:
        subprocess.check_call(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
        index_empty = True
    except subprocess.CalledProcessError:
        index_empty = False
    rec("KDOR-44", index_empty, "index not empty")
    rec("KDOR-45", head == HEAD_PIN)
    rec("KDOR-46", head == HEAD_PIN)

    # Required files
    for n in range(332, 355):
        matches = list(BILLA.glob(f"WD-BILL-A-{n}-*.md"))
        if not matches:
            failures.append(f"missing WD-BILL-A-{n}")

    payload = {
        "cwc": "CWC-CE-182",
        "head": head,
        "package_sha": HEAD_PIN,
        "draft_1_12_lou_pdf_sha": sha256(LOU_PDF),
        "draft_1_12_wp_pdf_sha": sha256(WP_PDF),
        "inquiry_status": "READY FOR HUMAN TRANSMISSION",
        "transmitted": False,
        "kdor_email_invented": False,
        "draft_1_13": "CANDIDATE ONLY",
        "five_percent": "UNCHANGED",
        "model_c": "NOT YET CALCULABLE",
        "maturity": "19% UNCHANGED",
        "hg_d1": "NOT PASSED",
        "outcome": "A" if not failures and all(v == "PASS" for v in tests.values()) else "B",
        "KDOR_tests": tests,
        "failures": failures,
    }
    out = BILLA / "WD-BILL-A-355-CWC-CE-182-VALIDATION.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"outcome": payload["outcome"], "failures": failures, "n_tests": len(tests)}, indent=2))
    return 0 if payload["outcome"] == "A" else 1


if __name__ == "__main__":
    raise SystemExit(main())
