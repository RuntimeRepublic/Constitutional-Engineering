# PR-COMMENT-CTRL-001 — Bill A Public-Comment Intake, Classification, Disposition

**Document ID:** PR-COMMENT-CTRL-001  
**Governing Work Card:** CWC-CE-179  
**Status:** CANDIDATE CONTROL — **NOT ACTIVATED**  
**Package:** Bill A LOU-004 / White Paper Draft 1.12 @ SHA `05bedea51c7489441ae411bb5b5b03fe532b1b66`

```text
AI MAY CLASSIFY AND ANALYZE.
AI MAY RECOMMEND.
AI SHALL NOT SILENTLY CHANGE HUMAN INTENT.
PUBLIC COMMENT ≠ HUMAN DECISION.
HUMAN ENGINEER = HUMAN-INTENT AUTHORITY.
```

---

## 1. Comment-channel analysis (existing evidence)

| Channel | Exists in project? | Citizen ease | Traceability | Spam / privacy | Account burden | Phone | Notes |
|---|---|---|---|---|---|---|---|
| GitHub Issues | Available on repo; **not** Bill-A-authorized for this review yet | Medium | High | Medium spam; public identity | Requires GitHub account | OK | Strong audit trail; excludes non-GitHub users |
| GitHub Discussions | Available if enabled; **not** activated here | Medium | High | Similar | GitHub account | OK | Slightly friendlier than Issues |
| BlueprintLiberty.com form | **Not verified as operational** for Bill A | High if built | Depends on backend | Needs anti-spam | Low | High | Best citizen UX **if** Human builds/authorizes |
| Email | Possible; **not** authorized as Bill A channel yet | High | Medium (manual) | Spam / spoof | Low | High | Needs intake discipline + Comment IDs |
| Structured repo intake files | Pattern exists in CE control culture | Low for public | High | Low public spam | N/A for public | Low | Good **internal** register; poor sole public UX |
| Social DMs / comments | Exist socially; **not** controlled intake | High | Poor | High | Low | High | Discovery only — not authoritative intake |

**Current controlled state:** `PUBLIC-REVIEW-README.md` correctly marks comment submission as **TBD / not Human-authorized**.

**Recommendation (not adopted):**  

1. **Primary public intake (preferred if form available):** BlueprintLiberty.com structured form writing into a controlled register.  
2. **Primary public intake (smallest no-new-service path):** GitHub Issues with a Bill A Draft 1.12 issue template + label `bill-a-public-review-1.12`.  
3. **Always:** every accepted comment also copied into a controlled repository comment register (Markdown/JSON) under the Bill A public-review package for engineering disposition.

**Human must choose (PR-04).** Do not activate any channel in this CWC.

---

## 2. Comment record schema

Every valid public-comment record SHOULD preserve:

| Field | Required | Notes |
|---|---|---|
| `comment_id` | Yes | Stable ID, e.g. `PRC-A-1.12-0001` |
| `date_received` | Yes | ISO-8601 date/time |
| `reviewer_name_or_status` | Yes | Name **or** `ANONYMOUS` / `PSEUDONYMOUS` per PR-05 |
| `source_channel` | Yes | form / github-issue / email / other |
| `document` | Yes | LOU-004 / WHITE-PAPER / UNRESOLVED / LANDING / OTHER |
| `version` | Yes | Draft 1.12 |
| `package_sha` | Yes | `05bedea…` (or freeze successor) |
| `section_or_topic` | Yes | Section id, heading, or topic tag |
| `comment_text` | Yes | Verbatim concern |
| `claim_or_concern` | Recommended | Short restatement |
| `supporting_evidence_or_link` | Optional | URLs/attachments metadata only |
| `initial_classification` | Yes | Class A–N below |
| `engineering_disposition` | Yes when closed | Disposition code |
| `disposition_reason` | Yes when closed | Why |
| `human_decision_if_required` | Conditional | Required for Human-Intent / material change |
| `resulting_cwc_if_any` | Conditional | Work-card id |
| `status` | Yes | RECEIVED / CLASSIFIED / IN_REVIEW / REFERRED / CLOSED |

Do not require unnecessary personal information. Do not invent reviewer identity.

---

## 3. Classification system

| Code | Class | AI may auto-suggest? | Human required before LOU change? |
|---|---|---|---|
| A | SUPPORT / NO CHANGE REQUESTED | Yes | No (unless converting to endorsement claim) |
| B | CLARIFICATION REQUEST | Yes | Only if answer would invent Intent |
| C | TYPOGRAPHICAL / PRESENTATION DEFECT | Yes | Human for public freeze correction (Option C) |
| D | HUMAN-INTENT QUESTION | Suggest only | Yes to bind answer |
| E | HUMAN-INTENT CHANGE PROPOSAL | Suggest only | **Always** |
| F | RESEARCH REQUIREMENT | Yes | Human prioritization |
| G | LEGAL / CONSTITUTIONAL ISSUE | Suggest only | Human + referred review |
| H | AGCL CONFORMANCE ISSUE | Suggest only | Human + AGCL referral |
| I | ECONOMIC / FISCAL ISSUE | Suggest only | Human if Intent/parameters affected |
| J | TRANSITION / IMPLEMENTATION ISSUE | Suggest only | Human if Intent affected |
| K | INTERNAL CONFLICT / INCONSISTENCY | Suggest only | Human if Intent resolution needed |
| L | OUT OF SCOPE | Suggest only | Human confirmation recommended |
| M | DUPLICATE | Yes (with link) | No |
| N | OTHER — HUMAN REVIEW REQUIRED | Default when unsure | Yes |

---

## 4. Disposition architecture

| Code | Disposition | Changes Human Intent? |
|---|---|---|
| ACCEPT-EDITORIAL | Fix presentation/typo under controlled rules | No |
| ACCEPT-CLARIFICATION | Clarify wording without Intent change | No (confirm) |
| REFER-RESEARCH | Open/continue research CWC | No until later |
| REFER-HUMAN-INTENT | Queue Human Intent question | Pending Human |
| REFER-AGCL | Route AGCL conformance review | Pending |
| REFER-LEGAL-CONSTITUTIONAL | Route legal/constitutional review | Pending |
| DEFER-REQUIREMENTS-SPEC | After HG-D1 / SPEC phase | No now |
| DEFER-LEGISLATIVE-ENGINEERING | After legislative authorization | No now |
| DUPLICATE | Point to prior comment | No |
| NO-CHANGE | Record reasoned refusal | No |
| OUT-OF-SCOPE | Record reason | No |
| UNRESOLVED | Remains open after review window | No |

Any disposition that would change Human Intent requires **Human Engineer authority** before LOU edit.

---

## 5. Processing workflow

1. Receive via authorized channel only.  
2. Assign `comment_id`; store verbatim.  
3. Confirm `version` / package SHA cited (default Draft 1.12).  
4. Classify (A–N); mark N if uncertain.  
5. Evidence check where claims require it.  
6. Materiality: presentation vs Intent vs research vs legal.  
7. Route; obtain Human decision when required.  
8. If change authorized → bounded CWC → LOU → White Paper reconciliation → validation.  
9. Close with disposition reason; optional public summary per PR-11.  
10. At review close → closure report per PR-12.

---

## 6. Accessibility notes for comment UX

Whatever channel Human selects SHALL:

- work on a phone;  
- not require Git literacy to **read** Bill A;  
- explain in plain language what happens to comments;  
- show Draft 1.12 freeze identity;  
- allow anonymous/pseudonymous mode only if PR-05 allows.

If GitHub Issues are primary, the landing page MUST still provide Start Here + PDF links without forcing repository browsing.

---

Libertas sine lapsu — Liberty without drift.
