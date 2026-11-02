# Runtime Republic — Jurisdiction and Work Board Control

**Status:** DRAFT — PENDING HUMAN ENGINEER REVIEW  
**Version:** 0.1  
**Prepared:** November 2, 2026  
**Formal document ID:** Unassigned; assign through the existing Engineering Office process.  
**Proposed governing home:** Constitutional-Engineering, with implementing references in Legislative-Manager and other participating repositories.  
**Approval authority:** James A. Hodges, Human Engineer, or an explicitly recorded successor/delegate within a defined scope.

## 1. Purpose and effect

Define how Runtime Republic organizes work across countries, states/provinces, and local governments while distinguishing the government being addressed from the team doing the work. Kansas is the first implementation and learning pilot.

This draft creates no active board, delegation, access grant, expenditure, legal authority, or adopted control. Approval of this document and authorization to implement it are separate records. It does not amend a constitution or determine governmental legal powers.

## 2. Core rule: classify work on two independent axes

Every work item identifies:

1. **Target jurisdiction and government level:** Which government, institution, or instrument is the work intended to affect?
2. **Participating team geography:** Where is the Runtime Republic team performing the work organized?

A Kansas team may work on United States federal legislation without making that legislation a Kansas state matter. A Wichita team may contribute to Kansas legislation without making it a city ordinance. Geographic nesting alone grants no decision authority.

A third classification identifies the work domain: legislation, budget, training, community, software, communications, or another approved domain.

## 3. Definitions

| Term | Definition |
|---|---|
| Jurisdiction | An identified governmental territory or legally constituted body, registered by country-specific definition. |
| Target level | National/federal, state/province or equivalent, local, or shared framework with no single governmental target. |
| Local government | A specific county, municipality, township, school district, special district, or equivalent body; overlapping bodies remain distinct. |
| Team geography | The registered geographic scope of the contributing Runtime Republic team. |
| Canonical work item | One issue or other approved authoritative task record with a stable identifier. |
| Work board | A planning and monitoring surface displaying work items; it does not independently confer authority. |
| View | A filtered presentation of a board's items, such as Kansas teams working on federal issues. |
| Accountable owner | One named human responsible for a work item's delivery and evidence. |
| Acceptance authority | The human authorized to accept the specified deliverable; may differ from its owner. |
| Coordination relationship | A dependency or reporting relationship; it is not automatically a delegation. |

“National” and “federal” are country-specific classifications. Do not impose the United States governmental model on other countries. National territories, provinces, autonomous regions, and local bodies use verified registered relationships.

## 4. Board families

The following are logical board families. They may initially be implemented as views on a small number of GitHub Projects rather than separate Projects for every combination.

| Board family | Target | Participating teams | Purpose |
|---|---|---|---|
| Shared Framework and Tools | No single jurisdiction | Any authorized team | Maintain common controls, training, software, templates, and interfaces. |
| Country National/Federal Work | A country's national institutions | National and subnational teams | Maintain the canonical national work portfolio. |
| State/Province — Federal Issues | National/federal institutions | A specified state/province team | Coordinate that team's contribution to national work. |
| State/Province — State Issues | That state/province government | Statewide and local teams | Manage jurisdiction-specific legislation and implementation. |
| Local — Federal Issues | National/federal institutions | A specified local team | Coordinate local participation in national work when active. |
| Local — State/Province Issues | State/province institutions | A specified local team | Coordinate local participation in state/provincial work. |
| Local — Local Issues | A named local governmental body | Relevant local teams | Manage work directed at that body's own decisions and instruments. |
| Organization Overview | Multiple registered scopes | Coordinators | Show selected milestones, dependencies, blockers, and decisions; no pooled approval authority. |

Create a separate physical Project only when distinct access, accountable stewardship, workflow, or sustained workload justifies it. Do not create empty boards for all states and every local body. A board may not expose information beyond its approved visibility.

## 5. Initial Kansas pilot

Proposed initial surfaces:

- Shared Framework and Tools view.
- United States — Federal Work view.
- Kansas — Federal Issues view.
- Kansas — State Issues view, preserving the existing PRJ-002 board and records until an approved mapping or migration exists.
- Local views only for named, active pilots with an owner and defined target body.

Example classification:

| Example | Government target | Team geography | Placement |
|---|---|---|---|
| Kansas team's research contribution to a federal consumption-tax proposal | United States / federal | United States / Kansas | National federal work plus Kansas federal-issues view. |
| PRJ-002 Kansas One-Hour Posting Rule | United States / Kansas / state | United States / Kansas | Kansas state-issues view. |
| Wichita team's sourced review of PRJ-002 | United States / Kansas / state | United States / Kansas / Wichita team | Kansas state-issues and Wichita state-issues views. |
| Proposed Wichita spending-visibility ordinance | United States / Kansas / City of Wichita / local | Wichita team | City of Wichita local-issues view. |
| Proposed Sedgwick County process review | United States / Kansas / Sedgwick County / local | Registered county team | Sedgwick County local-issues view. |
| School-district budget review | Named school district / local | Registered contributing team | That district's local-issues view, not automatically a city or county board. |

Examples are classifications, not authorized assignments or claims that projects exist.

## 6. Canonical records and cross-board coordination

One deliverable has one canonical task record, one accountable owner, and one designated source repository. Reuse its link across boards rather than create copies of the same task.

Separate deliverables receive separate issues with explicit parent/dependency links. For example, the national research task and a Kansas evidence contribution may be different deliverables; each needs its own acceptance criteria and owner.

Source-repository selection follows work ownership, not the board displaying it. A board does not require a repository of the same name. Shared controls remain in their governing repository; jurisdiction artifacts remain in their designated manager repository.

Authority, acceptance, and delivery state must be anchored in the canonical issue or referenced approved record. If GitHub Project fields differ across Projects, reconcile them from that record; never assume all field values synchronize automatically. No mirrored card may independently authorize or accept work.

## 7. Minimum item fields

| Field | Requirement |
|---|---|
| Canonical reference | Repository plus issue/PR URL or approved stable record ID. |
| Deliverable and domain | One bounded output and its approved work category. |
| Country and target jurisdiction | Registered target ID; shared-framework items explicitly use not applicable. |
| Target level | National/federal, state/province, local, shared framework; mixed work is decomposed where possible. |
| Target institution/instrument | Relevant legislature, agency, council, district, bill, rule, or other specified target. |
| Team geography | Registered owner-team geography plus contributing teams where applicable. |
| Human ownership | Accountable owner and acceptance authority; unassigned work stays in Backlog. |
| Authorization | Proposed/authorized/suspended/expired, with controlling record and expiry or review date where applicable. |
| Delivery status | Backlog, Ready, In progress, Human review, Done, or Archived. |
| Blocked flag | Reason, dependency, and next responsible person; usable with any delivery status. |
| Acceptance criteria | Observable conditions and required evidence. |
| Dates | Target date if agreed; next review date. Unknown dates remain unknown. |
| Visibility | Public or approved restricted class; no private member details on public items. |

Labels and fields support navigation. They do not replace controlling records.

## 8. Workflow and acceptance

- **Backlog:** Proposal recorded; no execution implied.
- **Ready:** Required scope, ownership, criteria, dependencies, and execution authorization are established.
- **In progress:** Authorized work has actually begun; link the work record.
- **Human review:** Deliverable and evidence submitted; not accepted yet.
- **Done:** Designated human acceptance is linked, with limitations and unresolved follow-up recorded.
- **Archived:** Retained for history with reason; cancellation or expiry is not successful completion.

Authorization status is separate from delivery status. An expired or suspended authorization prevents further execution even if the card still says In progress. A board administrator changing a field is not an acceptance decision. No AI, bot, poll, or elapsed deadline supplies human acceptance.

Routine scheduling or reporting cadence does not impose the NBBF four-month funding cycle on ordinary volunteer tasks. Budget-node rules apply only where adopted and applicable; a work card is not automatically a budget node.

## 9. Authority and stewardship

Each board has a named human steward, recorded purpose, participating scope, visibility, review date, and closure conditions. The steward maintains classification and reporting; additional approval authority requires an explicit delegation record.

National coordinators do not automatically approve state/provincial work. State coordinators do not automatically approve county, city, school-district, or special-district work. Shared technical administration does not create policy authority.

Disputes about scope or acceptance are recorded and referred to the designated Human Engineer or authorized resolver. Dependent work is marked blocked while authority remains unresolved; unrelated authorized work continues.

## 10. Communications, identity, and privacy

Discord, Facebook, email, GETTR, YouTube, and Rumble are communication surfaces. Relevant proposals are linked or transcribed into their canonical work record before entering controlled execution. Social reactions are not votes granting project authority.

Google, GitHub, Discord, and other account identities may be linked to an internal member ID after verification. Login, residence, a channel role, or a geographic subscription does not itself grant contributor level or approval authority.

Public boards show only approved public identity and work information. Private contacts, home addresses, credentials, readiness-check responses, and sensitive moderation records stay in approved private systems. Do not publish a member's location merely because internal classification uses it. Preserve existing officeholder and public-records cautions through links to governing documents; this control makes no legal compliance determination.

## 11. Automation and future UNBKE

Begin with manual classification and evidence links. Add automation only for a demonstrated repeated task and with recorded scope, owner, permissions, failure reporting, and disable procedure.

The daily Human Engineer report should group decisions, waiting reviews/merges, blockers, and upcoming dates by target jurisdiction and participating team. Deduplicate by canonical item reference. Report inaccessible or stale evidence; never mark work complete from an issue count, merge alone, or inferred progress percentage.

Proposed future UNBKE mapping: jurisdictions, teams, work items, and boards are entities; participates-in, targets, depends-on, and displayed-on are relationships; authorization, submission, acceptance, suspension, and publication are events. This is a candidate mapping requiring reconciliation with UNBKE's approved model. Applications use verified APIs and LogicMachine authority; they do not write directly to its database. UNBKE availability is not required for this pilot.

## 12. Activation, review, and closure

Before activation, record the approved control revision, board charter, field mappings, source repositories, steward, approval/delegation records, visibility, pilot measures, and review date. Existing boards and historical approvals must be mapped without rewriting their meaning.

Pilot acceptance checks:

1. Classify each example in Section 5 without confusing team geography and target authority.
2. Display one canonical issue on multiple views without duplicate delivery records.
3. Demonstrate distinct state and local deliverables with explicit dependencies.
4. Confirm unaccepted work cannot be reported as accepted merely by moving a card.
5. Confirm public views disclose no restricted member data.
6. Produce one deduplicated decision report with accurate source links and coverage limits.

Evaluate misclassified items, duplicate records, missing owners, inconsistent statuses, and time needed to find the next decision. Set numeric thresholds before the pilot starts. Capture lessons, revise the control, and authorize additional jurisdictions only when needed.

Close or consolidate inactive boards by recorded human decision. Preserve canonical records and redirects/mappings; remove unnecessary integrations and access. Closing a view does not cancel its underlying tasks or destroy evidence.

## 13. Open decisions for Human Engineer review

- Accept the two-axis classification and logical board families.
- Select the first local pilot, if any; no city/county/district is presumed selected.
- Decide which logical views share a Project and which need separate Projects after checking current GitHub capabilities and permissions.
- Assign formal document classification/ID and approved repository path through existing governance; this draft claims none.
- Set the Kansas pilot owner, review date, acceptance thresholds, and execution authorization.

## 14. Source basis and limits

Prepared from James's directions in this conversation, the reviewed Engineering Office Master Index, the Legislative-Manager roadmap/onboarding previously read in this session, and attached foundational controls. The Master Index establishes an existing architecture/policy/standard/workflow hierarchy and separate definition, execution, and acceptance records. This draft does not assign a competing control series or supersede that hierarchy.

Sources:

- https://github.com/RuntimeRepublic/Constitutional-Engineering/blob/main/Engineering-Office/IDX-001-Engineering-Office-Master-Index.md (reviewed November 2, 2026; file blob 89a11b11533fd198d49be6eba127cd468942d73b)
- https://github.com/RuntimeRepublic/Legislative-Manager/blob/main/ROADMAP.md (reviewed in this session; November 2 revision)
- https://github.com/RuntimeRepublic/Legislative-Manager/blob/main/ONBOARDING.md (reviewed in this session)
- Attached 01_Node_Ontology, version 1.1, and 00A Authority and Expiration Control: informative compatibility review; not a declaration that all budget-node requirements govern volunteer boards.

This is a proposed operating design, not a verification of GitHub Projects configuration or installed automation. Formal adoption requires compatibility review against the full current governing documents.

## Version history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-02 | Initial draft for Human Engineer review; no deployment or adoption. |

BlueprintLiberty.com
