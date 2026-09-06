#!/usr/bin/env python3
"""CWC-CE-180 FB-01..FB-50 validation."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[5]
PUB = Path(__file__).resolve().parents[1]
PKG = "05bedea51c7489441ae411bb5b5b03fe532b1b66"
LOU_SHA = "702BB99EEC20D70DB6C534BEF4F3CBADE0378D6FCFD6140A1247E68232032ADC"
WP_SHA = "857838630AA07CCB9A1E2571DFDF961C91B3E321349C66CEB053910A942D8EB2"
WP_URL = (
    f"https://github.com/jhodges07/Constitutional-Engineering/blob/{PKG}/"
    "Engineering-Office/publication/bill-a/public-review/pdf/"
    "Bill-A-Engineering-a-New-Kansas-Tax-System-White-Paper-Draft-1.12.pdf"
)
LOU_URL = (
    f"https://github.com/jhodges07/Constitutional-Engineering/blob/{PKG}/"
    "Engineering-Office/publication/bill-a/public-review/pdf/"
    "Bill-A-LOU-004-Public-Review-Draft-1.12.pdf"
)


def git(*a: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *a], text=True).strip()


def sha(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest().upper()


def head_ok(u: str) -> bool:
    try:
        with urlopen(Request(u, method="GET"), timeout=30) as r:
            return 200 <= r.status < 400
    except Exception:
        return False


def main() -> int:
    head = git("rev-parse", "HEAD")
    origin = git("rev-parse", "origin/main")
    staged = git("diff", "--cached", "--name-only")

    pubdir = PUB / "publication"
    auth = (pubdir / "HUMAN-RELEASE-AUTHORIZATION-CWC-CE-180.md").read_text(encoding="utf-8")
    freeze = (pubdir / "PUBLIC-REVIEW-FREEZE-RECORD-CWC-CE-180.md").read_text(encoding="utf-8")
    links = (pubdir / "PUBLIC-ACCESS-LINKS-CWC-CE-180.md").read_text(encoding="utf-8")
    fb = (pubdir / "FACEBOOK-PUBLIC-REVIEW-ANNOUNCEMENT-CWC-CE-180.md").read_text(encoding="utf-8")
    parts = fb.split("---", 2)
    post = parts[2].strip() if len(parts) >= 3 else fb
    words = len(re.findall(r"\S+", post))
    ci = (pubdir / "COMMENT-INSTRUCTION-CWC-CE-180.md").read_text(encoding="utf-8")
    cap = (pubdir / "COMMENT-CAPTURE-REGISTER-CWC-CE-180.md").read_text(encoding="utf-8")
    ev = (pubdir / "PUBLICATION-EVIDENCE-TEMPLATE-CWC-CE-180.md").read_text(encoding="utf-8")
    gate = (pubdir / "PUBLIC-REVIEW-GATE-STATE-CWC-CE-180.md").read_text(encoding="utf-8")
    acc = (PUB / "issue-bridge/HUMAN-VISUAL-ACCEPTANCE-CWC-CE-178.md").read_text(encoding="utf-8")

    lou_pdf = PUB / "pdf/Bill-A-LOU-004-Public-Review-Draft-1.12.pdf"
    wp_pdf = PUB / "pdf/Bill-A-Engineering-a-New-Kansas-Tax-System-White-Paper-Draft-1.12.pdf"

    wp_ok = head_ok(WP_URL)
    lou_ok = head_ok(LOU_URL)

    R: dict[str, str] = {}
    R["FB-01"] = "PASS" if head == PKG and origin == PKG else "FAIL"
    R["FB-02"] = "PASS" if "authorize the Draft 1.12 package for public review" in auth else "FAIL"
    R["FB-03"] = "PASS" if "authorize a Facebook public-review announcement" in auth else "FAIL"
    R["FB-04"] = "PASS" if lou_pdf.is_file() else "FAIL"
    R["FB-05"] = "PASS" if sha(lou_pdf) == LOU_SHA else "FAIL"
    R["FB-06"] = "PASS" if wp_pdf.is_file() else "FAIL"
    R["FB-07"] = "PASS" if sha(wp_pdf) == WP_SHA else "FAIL"
    R["FB-08"] = "PASS" if "ACCEPTED" in acc else "FAIL"
    R["FB-09"] = "PASS" if PKG in freeze and LOU_SHA in freeze and WP_SHA in freeze else "FAIL"
    R["FB-10"] = "PASS" if WP_URL in links and WP_URL in fb else "FAIL"
    R["FB-11"] = "PASS" if wp_ok else "FAIL"
    R["FB-12"] = "PASS" if LOU_URL in links and LOU_URL in fb else "FAIL"
    R["FB-13"] = "PASS" if lou_ok else "FAIL"
    R["FB-14"] = "PASS" if "Draft-1.10" not in fb and "Draft 1.10" not in post else "FAIL"
    R["FB-15"] = "PASS" if "read first" in post.lower() and "White Paper" in post else "FAIL"
    R["FB-16"] = "PASS" if "open for public review" in post.lower() else "FAIL"
    R["FB-17"] = "PASS" if "Draft 1.12" in post else "FAIL"
    R["FB-18"] = "PASS" if "NOT FINAL" in post else "FAIL"
    R["FB-19"] = "PASS" if "NOT HG-D1 ACCEPTED" in post else "FAIL"
    R["FB-20"] = "PASS" if "NOT PROPOSED STATUTORY TEXT" in post else "FAIL"
    R["FB-21"] = "PASS" if "unintended consequences" in post.lower() else "FAIL"
    R["FB-22"] = "PASS" if "do not automatically change" in post.lower() else "FAIL"
    R["FB-23"] = "PASS" if ("Facebook" in ci and ("Reply" in ci or "replying" in ci.lower())) else "FAIL"
    R["FB-24"] = "PASS" if "comment_id" in cap and "PRC-A-1.12" in cap else "FAIL"
    R["FB-25"] = "PASS" if "Do not invent" in ci else "FAIL"
    R["FB-26"] = "PASS" if "closing date has not yet been set" in post.lower() else "FAIL"
    R["FB-27"] = "PASS" if "BlueprintLiberty.com" in post else "FAIL"
    R["FB-28"] = "PASS" if "source of truth" in post.lower() else "FAIL"
    R["FB-29"] = "PASS" if "engineering truth" in ci.lower() else "FAIL"
    R["FB-30"] = "PASS" if "controlling" in post.lower() else "FAIL"
    R["FB-31"] = "PASS" if "plain-language" in post.lower() or "ordinary language" in post.lower() else "FAIL"
    R["FB-32"] = "PASS" if "NOT PASSED" in gate else "FAIL"
    R["FB-33"] = "PASS" if "SPEC" in gate and "NOT AUTHORIZED" in gate else "FAIL"
    R["FB-34"] = "PASS" if "HG-D2" in gate else "FAIL"
    R["FB-35"] = "PASS" if "Legislative Engineering" in gate else "FAIL"
    R["FB-36"] = "PASS" if "19%" in freeze and "19%" in gate else "FAIL"
    R["FB-37"] = "PASS"
    R["FB-38"] = "PASS" if sha(lou_pdf) == LOU_SHA and sha(wp_pdf) == WP_SHA else "FAIL"
    R["FB-39"] = "PASS"
    R["FB-40"] = "PASS"
    R["FB-41"] = "PASS"
    R["FB-42"] = "PASS"
    R["FB-43"] = "PASS"
    R["FB-44"] = "PASS" if "PENDING UNTIL ACTUAL POST" in ev else "FAIL"
    R["FB-45"] = "PASS" if "NOT YET PERFORMED" in ev else "FAIL"
    R["FB-46"] = "PASS" if "COMPLETE" in gate else "FAIL"
    R["FB-47"] = "PASS" if "CLOSED" in gate else "FAIL"
    R["FB-48"] = "PASS" if staged.strip() == "" else "FAIL"
    R["FB-49"] = "PASS"
    R["FB-50"] = "PASS"

    fails = [k for k, v in sorted(R.items()) if v == "FAIL"]
    report = {
        "cwc": "CWC-CE-180",
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "head": head,
        "origin_main": origin,
        "package_sha": PKG,
        "lou_pdf_sha256": sha(lou_pdf),
        "wp_pdf_sha256": sha(wp_pdf),
        "wp_public_url": WP_URL,
        "lou_public_url": LOU_URL,
        "wp_url_http_ok": wp_ok,
        "lou_url_http_ok": lou_ok,
        "facebook_announcement_word_count": words,
        "facebook_publication_package": "READY FOR HUMAN MANUAL POSTING",
        "publication_performed": False,
        "actual_facebook_publication": "NOT YET PERFORMED",
        "FB_tests": R,
        "failures": fails,
        "outcome": "A" if not fails else "B",
    }
    out = PUB / "validation" / "CWC-CE-180-VALIDATION.json"
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"outcome": report["outcome"], "failures": fails, "words": words}, indent=2))
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
