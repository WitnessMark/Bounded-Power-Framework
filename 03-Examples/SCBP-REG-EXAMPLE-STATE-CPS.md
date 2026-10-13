---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-STATE-CPS
record_version: 1
supersedes: NONE
form: {name: registration, version: 1.0.0, date: 2026-10-13}
core_requirements: {version: v1, date: 2026-10-13}
bundle: NONE
vocab_version: 1.0.0
prepared_by: person
ai_tool: NONE
prepared_date: 2026-10-13
sources_checked_date: 2026-10-13
institution:
  name: "[STATE] Child Protective Services Agency"
  legal_entity: "[STATE], acting through its child welfare agency"
  related_entities: "[STATE] juvenile court (separate body); [COUNTY] police and sheriff offices; contracted foster care agencies; other [STATE] agencies that supply records to the screening tool"
  type: government
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: NONE
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Emergency removal of children"
    category: removal_custody_or_placement
    authority_basis: direct
    uses_force_or_confinement: "yes"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: not_conforming
      remedy: not_conforming
      data_limits: not_conforming
      visibility: not_demonstrated
      floors: not_conforming
      evasion: not_demonstrated
  - power_id: P2
    short_name: "Central abuse and neglect registry"
    category: data_collection_or_records
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: not_conforming
      remedy: not_conforming
      data_limits: not_conforming
      visibility: not_demonstrated
      floors: not_conforming
      evasion: not_demonstrated
  - power_id: P3
    short_name: "Hotline screening risk tool"
    category: scoring_ranking_or_classification
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: not_demonstrated
      remedy: not_conforming
      data_limits: not_conforming
      visibility: conforming
      floors: not_demonstrated
      evasion: conforming
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [STATE] Child Protective Services Agency — Registration (worked example)

## PART A — The institution

A1. **What it is.** A state agency that takes reports of suspected child abuse and neglect, investigates families, removes children it judges to be at risk, places them in foster care, lists people it finds responsible in a central registry, and asks the juvenile court for custody and termination orders. It receives about 120,000 [EX] reports a year and has about 9,000 [EX] children in out-of-home care on a given day.

A2. **Legal basis.** The [STATE] child welfare code, which has no sunset date, and conditions attached to federal child welfare funding under the federal child abuse prevention law and the federal foster care funding law. [EX]

A3. **Who controls it.** A director appointed by the governor; the legislature sets the budget each year. The juvenile court is a separate branch and decides custody after removal. [EX]

A4. **Related entities.** Police and sheriff offices carry out removals when parents resist. Contracted private agencies run most foster placements. Other state agencies supply records used by the screening tool (P3). Every figure here belongs to the agency unless marked otherwise.

A5. **Adoption.** not_adopted. [EX]

A6. **Powers found.**
- P1 Emergency removal of children without a prior court order.
- P2 Central registry listing people found responsible for abuse or neglect.
- P3 Risk score used to decide which hotline reports are investigated.
- Not recorded: home investigations, foster home licensing, petitions to terminate parental rights.

---

## Power P1 — Emergency removal of children

**B1. What it can do to people.** A caseworker, with a supervisor's approval, can take a child from a parent's home without a court order when the caseworker believes the child is in immediate danger. Physical custody passes to the agency at once. A judge reviews the removal only afterward.

**B2. Who and where.** Any family in [STATE]. About 3,500 [EX] emergency removals a year. Children and parents are affected without choosing to be; siblings and relatives are non-participants.

**B3. Authority basis.** `direct`. The agency itself takes physical and legal custody. When a parent resists, police carry out the removal at the agency's request, so the power uses force against persons through a related entity (4.1).

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The child welfare code grants the power in general terms. No body heard affected families or made findings on each requirement. NONE EXISTS. | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS. The code has no sunset; yearly appropriations do not make the power lapse. | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. The agency publishes removal counts and child fatalities each year, but no threshold pauses or narrows removals. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Court review of each removal within 72 hours [EX]. No path reaches the power as a whole; none is tested. | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS. | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Return of the child by court order. Damages only through a federal civil-rights lawsuit, usually blocked by immunity doctrines. No funded compensation process. | not conforming |
| Data limits | Retention periods; 20-year [S1] ceiling; accountability records kept independently (2.D.12–2.D.14, 7.6) | Case records are kept until the youngest child turns 28 [EX], which can exceed the 20-year ceiling [S1]. Deletion records: UNKNOWN. | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9) | Code and policy manual are public; parents receive a written removal notice with the hearing date. Whether the power has grown is not published. | compliance not demonstrated |
| Floors | See B6 (Part II) | Disparity unreviewed; force by police not separately authorized (B6); home entries on consent that is not freely given, and examinations of children without a court order (2.D.15); safety plans that move a parent out without a court order (2.D.16). | not conforming |
| Evasion | Not split, outsourced, laundered, or using proxies (Part IV) | Removals carried out by police; placements by contractors. Whether this avoids limits: UNKNOWN. | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Custody hearing after removal, within 72 hours [EX] | one_case | juvenile court judge | independent | [EX] |
| 2 | Appeal of the custody order | one_case | appellate court | independent | [EX] |
| 3 | Federal civil-rights class action ending in an injunction or consent decree | one_practice | federal court | independent | [EX] |

Only a new statute could end the power as a whole, so that is not counted.

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Irreversible ecological threshold? | not_applicable — no ecological effect | |
| Economic (2.B) | Essentials conditional; growing obligations; path out? | yes — reunification case plans require classes and drug tests that parents often pay for, and missed steps count against return | [EX] |
| Agency (2.C) | Told plainly; can report harm; can leave? | no — notice is given, but the hearing notice uses legal terms and there is no exit from the power | [EX] |
| Force (2.D.1) | Separately authorized, never aimed at pain, externally stoppable, independently reviewed? | no — police force used at removal is authorized only as general police power; not reviewed as part of this power | [EX] |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — removal places a child in custody, not in a locked setting; locked placements are not recorded here | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — the power gives no medical treatment; consent for a child's care in placement is not recorded here |  |
| Due process (2.D.5) | Challenge before someone independent? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — after the fact, at the custody hearing, where parents receive appointed counsel [EX] | [EX] |
| Expression (2.D.9) | Punishes lawful expression? News reporting or petitioning? Approval before publication? | UNKNOWN | |
| Equal treatment (2.D.10) | Unequal burdens; reviewed? | yes — removal rates for two groups are 2.1 times [EX] their population share; no independent review | [EX] |
| Identification (2.D.11) | Compelled identification without cause? | not_applicable — removal acts on a named family | |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | no — investigators enter homes and look through rooms with a parent's agreement, after telling the parent that refusing may lead to removal [EX], so consent is not freely given; children are interviewed and examined for injuries at school without a parent's knowledge or a court order [EX]. No judicial officer approves these searches or reviews them afterwards unless a removal reaches court | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | no — safety plans require a parent to move out of the home or not be alone with the child, without a court order [EX]; parents sign them to avoid removal, and nothing reviews them. That restricts where a person may live on none of the grounds in 2.D.16 | [EX] |

**B7. Data.** Case files hold interviews, medical and school records, photographs, and police reports. Purpose: the custody case. Retention: see B4. Accountability records of removals and complaints are held by the agency itself, not by an independent custodian (2.D.14). [EX]

**B8. Dependencies and evasion.** Police execute contested removals; contracted agencies choose most placements and are paid per bed-day [EX], which ties their revenue to the number of children in care. Whether the agency and the court act as one coordinated system (4.2) would need a Causation Ladder finding; the only evidence visible is that the court approves most removals, which is residual correlation (tier 7) and supports only a recorded concern. [EX]

**B9. Harms seen.** psychological and generational: separation trauma, including in removals later found unwarranted (allegation and research finding, not adjudicated here). agency: notices parents cannot follow. A consent decree on placement conditions was entered in an earlier year without admission [EX] (settled without admission). [EX]

**B10. Decision inputs and oversight.** A safety checklist and caseworker judgment drive removal; the checklist is published but how often it is overridden is not (5.3). Oversight: federal program reviews every few years, a state ombudsman who can investigate but not stop, and the consent-decree monitor. [EX]

---

## Power P2 — Central abuse and neglect registry

**B1. What it can do to people.** When a caseworker finds an allegation "substantiated", the person found responsible is listed in a central registry. Employers in child care, schools, health care and foster care must check it, and a listing usually bars the person from that work.

**B2. Who and where.** About 60,000 [EX] people listed; about 8,000 [EX] added each year. Job applicants and their employers are affected; most listed people are parents.

**B3. Authority basis.** `direct`. The agency makes the listing and itself discloses it to employers that the law requires to check. Employers' hiring decisions also operationalize it (indirect_a, tier 1: binding directive in statute), but the binding act recorded here is the agency's own.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body, public record (3.A.1, 3.A.2) | Created by statute; no separate authorization. NONE EXISTS. | not conforming |
| Maximum term | Set expiry (3.E.1, 7.2) | NONE EXISTS for the registry. Each listing lasts 25 years [EX], or for life for some findings. | not conforming |
| Harm thresholds | Published, measurable (3.A.5) | NONE EXISTS. | not conforming |
| Stop paths | Tested, one independent (3.A.7, 3.C.1) | Administrative hearing can remove one listing; the agency head may reject the hearing officer's decision. Nothing stops the registry. | not conforming |
| Ending plan | Documented (3.A.9) | NONE EXISTS. | not conforming |
| Remedy | Independent, funded (3.A.10) | Removal of the listing on appeal; no compensation for jobs lost while listed. | not conforming |
| Data limits | 20-year [S1] ceiling; deletion records (2.D.12, 2.D.14, 7.6) | Listings kept 25 years [EX] by the agency, over the 20-year ceiling [S1]. A registry listing against a member of the public is not an accountability record (2.D.14); it follows 2.D.12 and 2.D.6, and the person may ask for its earlier deletion unless a hold applies. Here the only early route is a petition after 7 years [EX], and the retention clock resets on a new report (B7). Deletion records: UNKNOWN. | not conforming |
| Visibility | Knowable to ordinary people (3.B.9) | Listed people get a letter with a 30-day [EX] appeal deadline; the share of letters returned undelivered is UNKNOWN. | compliance not demonstrated |
| Floors | Part II | No periodic review of listings (2.D.6). | not conforming |
| Evasion | Part IV | Listings are shared with other states' registries for out-of-state checks; whether removed listings are purged there (4.6): UNKNOWN. | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Administrative hearing on the listing | one_case | hearing officer in a separate state hearings office; final say with the agency head | partly_independent | [EX] |
| 2 | Judicial review of the final decision | one_case | state trial court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Ecological threshold? | not_applicable — records only | |
| Economic (2.B) | Essentials conditional; path out? | yes — a listing blocks whole fields of work, and the only path off before expiry is a petition after 7 years [EX] | [EX] |
| Agency (2.C) | Told plainly; can challenge? | no — the notice is mailed once; a missed deadline ends the right to a hearing | [EX] |
| Force (2.D.1) | Force? | not_applicable — no force | |
| Confinement (2.D.3) | Only on the four permitted grounds? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | no — the agency head can override the hearing officer; listing takes effect before any hearing | [EX] |
| Expression (2.D.9) | Restricts expression? News reporting or petitioning? Approval before publication? | UNKNOWN | |
| Equal treatment (2.D.10) | Unequal burdens; reviewed? | UNKNOWN — listings are not reported by group | |
| Identification (2.D.11) | Identification without cause? | not_applicable — checks are tied to a job application | |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — listing searches and seizes nothing |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — a listing bars work, not movement; recorded under Economic |  |

**B7. Data.** Name, date of birth, finding type, and case number. Purpose: employment screening. Kept 25 years [EX] from listing, so a person listed at 19 [EX] stays listed until 44 [EX]. The retention clock is reset if a new report is made, which 2.D.12 forbids. [EX]

**B8. Dependencies and evasion.** Employers and licensing boards rely on the registry by law. Background-check firms receive results and may keep copies; whether those copies are purged when a listing is removed is UNKNOWN (4.4, 4.6). [EX]

**B9. Harms seen.** economic: loss of child-care and health-care jobs (allegation in public comments; reversal rate on appeal of 30% [EX] suggests error). informational: listings outlast the facts. Adjudicated: a state appellate court held that listing before a hearing violated due process for one class of cases [EX] (adjudicated fact).

**B10. Decision inputs and oversight.** The standard is a caseworker's judgment that the allegation is more likely than not true; the factors are in the policy manual (5.3). No outside body audits listings as a whole. [EX]

---

## Power P3 — Hotline screening risk tool

**B1. What it can do to people.** Each hotline report is placed in a low, medium, or high risk band [EX]. A report in the high band must be investigated unless a supervisor overrides. The score decides whether a family gets a home visit from an investigator.

**B2. Who and where.** Every family reported to the hotline, about 120,000 [EX] reports a year. Most families never learn a score was used.

**B3. Authority basis.** `direct`. The agency's own model drives the agency's own screening decision. It is not indirect authority, because no other party relies on it.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body, public record (3.A.1, 3.A.2) | Adopted by the agency director after an internal policy review [EX]. No independent authorizing body. | not conforming |
| Maximum term | Set expiry (3.E.1, 7.2) | Policy requires re-validation every 2 years [EX] by the agency's contractor; the tool keeps running if it is late. Not an expiry. | not conforming |
| Harm thresholds | Not dependent on the institution's own findings (3.A.5) | A disparity check exists but is computed and judged by the agency. | not conforming |
| Stop paths | Tested, one independent (3.A.7, 3.C.1) | The director can switch it off; screeners can override one case. Neither is independent. | not conforming |
| Ending plan | Documented (3.A.9) | Policy says screeners return to the earlier checklist if the tool is withdrawn [EX]; stored past scores are not addressed. | compliance not demonstrated |
| Remedy | Independent, funded (3.A.10) | NONE EXISTS. A family cannot learn or contest its score. | not conforming |
| Data limits | Retention; 20-year [S1] ceiling (2.D.12) | Scores are stored with the case record and follow its schedule (see P1). | not conforming |
| Visibility | Knowable (3.B.9); inputs declared (5.3) | A plain-language description of the tool, the variable list, validation results, and the re-validation schedule are published [EX]; the policy shows plainly that the tool has no expiry (that failure is recorded under Maximum term). | conforming |
| Floors | Part II | Disparity reviewed by the agency's contractor only (B6). | compliance not demonstrated |
| Evasion | Part IV | Built and run by the agency's own analytics unit on government records; no bought data [EX]. | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Supervisor override of one score | one_case | screening supervisor | not_independent | [EX] |
| 2 | Lawsuit under state data-privacy law | one_practice | state trial court | independent | [EX] |

Not counted: the director withdrawing the tool. That would end the power, but the director is the institution itself (form B5).

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Ecological threshold? | not_applicable — software only | |
| Economic (2.B) | Essentials conditional? | no — the score does not condition benefits | [EX] |
| Agency (2.C) | Told plainly without asking? | no — families are not told a score was used (2.C.1) | [EX] |
| Force (2.D.1) | Force? | not_applicable — no force | |
| Confinement (2.D.3) | Only on the four permitted grounds? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | NONE EXISTS | [EX] |
| Expression (2.D.9) | Restricts expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens; reviewed? | yes — high scores fall 1.6 times [EX] more often on one group; reviewed only by the agency's contractor | [EX] |
| Identification (2.D.11) | Identification without cause? | not_applicable — acts on a named report | |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — the score triggers home visits, which are recorded under P1 |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** The model draws on the agency's prior reports and on records from other state agencies. Data received from other agencies counts as collected by this agency (4.4). Retention follows the case record. [EX]

**B8. Dependencies and evasion.** The other agencies' records arrive under a data-sharing agreement renewed every 3 years [EX]. No vendor. Race is excluded as an input, but prior reports and some other-agency records may stand in for it (4.7); see B9.

**B9. Harms seen.** agency and psychological: investigations of families who would not otherwise be visited (allegation). On proxies: the outcome gap in B6 is residual correlation (tier 7), so it supports only a recorded concern under 4.7 and a request for evidence. It does, without any tier, require independent disparity review under 2.D.10 within 90 days [S1]. [S4]

**B10. Decision inputs and oversight.** All inputs and weights are declared (5.3). Validation is done by the contractor that built the model, which is not independent (5.1). [EX]

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it | Quote | Verified? |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 1.6 (90 days), 2.D.3 (48 hours), 2.D.10 (90 days), 2.D.12 (20 years), 2.D.14 (10 years), 7.2 (2 years) | | yes |
| S2 | quote | Core Requirements v1 | BPF: Core Requirements v1 | 3.D.2 | A change of legal status is containment only if it is temporary and protective — for example, emergency protective custody of a child in imminent danger: reversible by default, limited in time, confined to the danger, and reviewed by an independent decision-maker within a short fixed period. | yes |
| S3 | quote | Core Requirements v1 | BPF: Core Requirements v1 | 1.6 | A standing power that can be activated without a declared emergency is an ordinary power subject to every requirement. | yes |
| S4 | quote | Core Requirements v1, Causation Ladder | BPF: Core Requirements v1 | Definitions, Causation Ladder | A review of disparity under 2.D.10 is a review, not a proxy finding, and requires no tier. | yes |

Figures tagged [EX] are illustrative and have no source.

## PART D — Honesty assertions

- [x] Every number has a source tag or an [EX] tag.
- [x] Nothing was presented as a real institution's data.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] Made in good faith, as a structural description.

Preparer: BPF examples working group (worked example).

## Teaching notes (non-binding)

- Under 3.D.2 a temporary, protective change of legal status can be containment [S2]. An emergency removal qualifies only case by case: it must be reversible by default, limited in time, confined to the danger, and reviewed by an independent decision-maker within a short fixed period. P1 meets the review condition (a judge within 72 hours [EX]); whether a child returns by default when the hearing is late, and whether less harmful means such as an in-home safety plan are tried first, is not shown. Containment also covers only the emergency act. The standing power to remove still needs authorization, a term and stop paths, so no P1 finding changes.
- "Emergency" in the name does not make P1 an emergency power with a 90-day clock (1.6) [S1]. It can be used any day without a declaration, so it is an ordinary power [S3] and needs a term under 7.2.
- Court review after removal is a real, independent stop path, but it reaches one case. Recording it as `one_case` and the whole-power answer as NONE EXISTS is the honest result (3.A.7, 3.C.1).
- Force carried out by a related entity (the police) still counts for the power that directs it (4.1, 2.D.1).
- A registry listing is a sanction against a member of the public, not an accountability record (2.D.14). It follows 2.D.12 (stated retention, 20-year ceiling [S1], no reset) and 2.D.6 (periodic justification), and the listed person may ask for earlier deletion unless a hold applies. P2's 25-year [EX] listing with a petition only after 7 years [EX] fails on each point.
- The registry (P2) shows three data rules at once: the 20-year ceiling and no-reset rule (2.D.12) [S1], the duty to purge copies downstream (4.6), and structural entrapment when no periodic review exists (2.D.6).
- The screening tool (P3) can be conforming on visibility and evasion while failing on authorization and remedy. Publishing a model is not the same as authorizing it (3.A.2, 5.3).
- Disparity review and proxy findings differ: 2.D.10 review needs no Causation Ladder tier; a 4.7 proxy finding needs tier 5 or stronger (tiers 1–5) [S4].
- A re-validation schedule run by the institution's own contractor is not a maximum term (3.E.1, 3.A.2).
- A parent's agreement to a home search, given after being told that refusing may lead to removal, is not consent freely given (2.D.15). A safety plan that moves a parent out of the home without a court order restricts where the parent may live on none of the grounds 2.D.16 allows. Both are part of P1's Floors finding.
