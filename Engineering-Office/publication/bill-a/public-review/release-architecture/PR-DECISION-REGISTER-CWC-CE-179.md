# PR-DECISION-REGISTER — CWC-CE-179 (PR-01 … PR-12)

**Work card:** CWC-CE-179  
**Status:** HUMAN DECISIONS REQUIRED BEFORE RELEASE EXECUTION  
**Package SHA:** `05bedea51c7489441ae411bb5b5b03fe532b1b66`  

Silence ≠ decision. AI recommendation ≠ Human decision.

---

| ID | Decision | Why Human authority is required | Candidate recommendation (NOT ADOPTED) | Status |
|---|---|---|---|---|
| **PR-01** | Primary public-review entry point | Chooses where citizens first land | BlueprintLiberty.com Start Here page linking to freeze identity + PDFs | **OPEN** |
| **PR-02** | GitHub Release yes/no | Creates public distribution surface | Yes — Release as download snapshot only; notes cite SHA-256s; not engineering authority | **OPEN** |
| **PR-03** | BlueprintLiberty.com role | Publication surface authority | Primary human-facing entry / explanation / comment instructions; never source truth | **OPEN** |
| **PR-04** | Primary comment channel | Activates intake | Prefer site form if available; else GitHub Issues template `bill-a-public-review-1.12` + controlled register copy | **OPEN** |
| **PR-05** | Anonymous / pseudonymous comments | Privacy / abuse tradeoff | Allow anonymous/pseudonymous with spam controls; optional contact for follow-up | **OPEN** |
| **PR-06** | Review opening date | Starts PUBLIC REVIEW clock | Do not invent; set only at HG-PR RELEASE | **OPEN — HUMAN DATE REQUIRED** |
| **PR-07** | Review closing date or duration | Ends collection window | Recommend 30 calendar days, extendable without changing freeze identity | **OPEN — HUMAN DURATION/DATE REQUIRED** |
| **PR-08** | Version-freeze behavior | Protects what was reviewed | Draft 1.12 frozen; comments bind to freeze identity | **OPEN** (architecture defined; adopt/confirm) |
| **PR-09** | Material correction during review | Prevents silent rewrite | Default Option A (continue + defer); Option B if review must supersede; Option C only for presentational Human-approved corrections | **OPEN** |
| **PR-10** | Social-media announcement scope | Discovery vs overclaim | Links-only to Start Here after HG-PR; no HG-D1/maturity claims; no Facebook-as-truth | **OPEN** |
| **PR-11** | Comment disposition visibility | Transparency vs noise/harassment | Publish periodic aggregate summaries; keep verbatim register controlled; redact personal data as needed | **OPEN** |
| **PR-12** | Post-review closure / report format | Closes the loop | Controlled closure report: counts by class, dispositions, open referrals, whether 1.12 remains or successor opens, HG-D1 still not passed | **OPEN** |

---

## Already controlled (do not re-ask)

| Matter | Control |
|---|---|
| Exact PDF identities | CWC-CE-177 / CE-178 |
| Human visual acceptance | ACCEPTED |
| Package Git canonicalize | COMPLETE @ `05bedea…` |
| HG-D1 | NOT PASSED |
| Maturity | 19% |
| Publication this cycle | NOT AUTHORIZED |
| LOU controls; White Paper derivative | Established |
| Comment ≠ automatic LOU change | Established |
| HG-PR ≠ HG-D1 (LOU-PR-001) | Established |

---

## Gate still required before “public review is open”

```text
HUMAN HG-PR = RELEASE
+
PR-01…PR-07 (minimum entry, channel, dates)
+
RELEASE-EXECUTION CWC PASSING VALIDATION SPEC
```

This register does **not** pass HG-PR.

---

Libertas sine lapsu — Liberty without drift.
