---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-SCHOOL-DISTRICT
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
  name: "[CITY] School District"
  legal_entity: "[CITY] School District, a public school district under [STATE] education law"
  related_entities: "[STUDENT-MONITORING VENDOR]; [STAFFING AGENCY] (contracted behavior aides); [CITY] Police Department (school resource officers); [COUNTY] education appeals panel"
  type: government
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: "[CITY]"
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Suspension and expulsion"
    category: employment_or_discipline
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
      visibility: conforming
      floors: not_conforming
      evasion: not_demonstrated
  - power_id: P2
    short_name: "Physical restraint and seclusion"
    category: use_of_force
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
      evasion: not_conforming
  - power_id: P3
    short_name: "Student-device monitoring"
    category: inspection_search_or_surveillance
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: conforming
      remedy: not_conforming
      data_limits: not_conforming
      visibility: not_conforming
      floors: not_conforming
      evasion: not_conforming
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [CITY] School District — Registration (worked example)

## PART A — The institution

A1. **What it is.** A public school district that runs 24 [EX] schools for about 18,000 [EX] students from kindergarten through high school. Attendance is compulsory, so almost every person it acts on is a child who did not choose it.

A2. **Legal basis.** [STATE] education law; the federal disability-education law; federal civil-rights and student-records laws, named generally. [EX]

A3. **Who controls it.** An elected board of 7 [EX] members appoints the superintendent. A county-level education appeals panel, outside the district, hears expulsion appeals; the state education agency writes restraint rules. [EX]

A4. **Related entities.** [STUDENT-MONITORING VENDOR] runs P3. [STAFFING AGENCY] supplies behavior aides who carry out some restraints (P2). School resource officers are employed by the [CITY] Police Department. Figures belong to the district unless stated.

A5. **Adoption.** not_adopted. [EX]

A6. **Powers found.**
- P1 Suspension and expulsion of students.
- P2 Physical restraint and seclusion of students.
- P3 Monitoring of student activity on district-issued devices and accounts.
- Not recorded: truancy referrals, special-education placement, staff discipline, student searches.

---

## Power P1 — Suspension and expulsion

**B1. What it can do to people.** A principal can exclude a student from school for up to 10 [EX] school days. The board can expel a student for up to one calendar year [EX] after a hearing. Exclusion removes instruction, meals, and supervision, and is often paired with a referral to police.

**B2. Who and where.** All enrolled students. About 2,100 [EX] suspensions and 40 [EX] expulsions a year. Parents who must stay home from work are non-participants.

**B3. Authority basis.** `direct`. The district itself excludes the student.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | State education law allows suspension; the district's own board adopts the code of conduct. Self-authorization. | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | The board readopts the code every year [EX], but the board is the district itself and the statute has no expiry. NONE EXISTS. | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | County appeals panel for expulsions; federal civil-rights complaint. None reaches the whole power; none tested. | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS. | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Record cleared after a successful appeal; no make-up instruction or compensation required. | not conforming |
| Data limits | Retention periods; 20-year ceiling; deletion records (2.D.12–2.D.14, 7.6) | Discipline records destroyed 5 years [EX] after the student leaves; destruction logged and audited by the county auditor [EX]. A suspension or expulsion entry is a sanction against a member of the public, not an accountability record (2.D.14), so it follows 2.D.12 and 2.D.6. The records are not periodically re-justified while kept (2.D.6), the power has no term at which retention is re-justified (2.D.12), and whether a student or family can ask for earlier deletion is UNKNOWN. | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9) | Code of conduct sent home each fall in 6 [EX] languages, listing offenses, penalties, hearing rights, the yearly readoption, and year-on-year changes. | conforming |
| Floors | See B6 (Part II) | Disparity; off-campus speech discipline (B6); searches of phones and bags without judicial approval or later review (2.D.15); campus bans on suspension without independent review (2.D.16). | not conforming |
| Evasion | Not split, outsourced, laundered, or using proxies (Part IV) | Some conduct goes to police citations instead of school discipline; whether this avoids hearing rights: UNKNOWN. | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Expulsion appeal | one_case | [COUNTY] education appeals panel | independent | [EX] |
| 2 | Disability review before exclusion beyond 10 [EX] days (is the conduct caused by the disability?) | one_case | student's individualized-education team, which includes district staff and the parent | not_independent | [EX] |
| 3 | Complaint to the federal education civil-rights office, ending in a resolution agreement | one_practice | federal civil-rights office | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Each path reaches one case or one practice; only a change in state law could end the power, and a new law does not count.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Ecological threshold? | not_applicable — no ecological effect | |
| Economic (2.B) | Essentials conditional; growing obligations? | no — exclusion removes school meals, but meals are offered at a pickup site [EX] | [EX] |
| Agency (2.C) | Told plainly; can report; can leave? | yes — written notice with hearing rights; leaving means another school, often far away | [EX] |
| Force (2.D.1) | Force? | not_applicable — this power uses no force (see P2) | |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no detention | |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical treatment | |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes for expulsion (county appeals panel); no for suspension, which is reviewed only by the district | [EX] |
| Expression (2.D.9) | Punishes lawful expression? News reporting or petitioning? Approval before publication? | yes — 12 [EX] suspensions last year for off-campus social-media posts criticizing staff | [EX] |
| Equal treatment (2.D.10) | Unequal burdens; reviewed? | yes — students with disabilities and two racial groups are suspended at 2.8 times [EX] their share; no independent review | [EX] |
| Identification (2.D.11) | Identification without cause? | not_applicable — acts on a named student | |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | no — before a suspension, administrators search students' bags, lockers and phones on reasonable suspicion of a code violation [EX], with no judicial approval and no review afterwards by anyone outside the district; a phone search reaches messages and photos. Confiscated phones are returned to a parent within 1 school day [EX] | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | partly — an excluded student is barred from all district grounds and events for the period [EX]. For an expulsion this is a sanction under published rules after a hearing with an independent appeal; a suspension is imposed by the principal with no independent review (see Due process), so the 2.D.16 sanction ground is not met for it | [EX] |

**B7. Data.** Incident reports, witness statements, and outcomes in the student-information system, hosted by a vendor; deletion covers the hosted copy [EX]. Retention: see B4.

**B8. Dependencies and evasion.** School resource officers issue about 300 [EX] citations a year for conduct the code also covers, sending students to a court process without the school hearing. Whether that is functional equivalence (4.1) needs more evidence.

**B9. Harms seen.** agency and generational: lost instruction and higher dropout after exclusion (research finding, allegation for this district). communicative: speech-related suspensions (allegation). A federal resolution agreement on discipline disparity was signed without admission in an earlier year [EX] (settled without admission).

**B10. Decision inputs and oversight.** The code lists offenses and a penalty range; principal discretion within the range is not tracked (5.3). Discipline counts by group are reported to the federal government every 2 [EX] years. No outside audit.

---

## Power P2 — Physical restraint and seclusion

**B1. What it can do to people.** Staff can hold a student so the student cannot move, or put a student alone in a room the student is prevented from leaving. State rules allow this only when there is an imminent danger of serious physical harm.

**B2. Who and where.** Any student; in practice mostly young students with disabilities. About 600 [EX] restraints and 150 [EX] seclusions a year; 80% [EX] involve students with disabilities.

**B3. Authority basis.** `direct`. District staff and contracted aides act on students' bodies.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body, public record (3.A.1, 3.A.2) | A general state regulation allows restraint in all districts. No separate authorization of this power. | not conforming |
| Maximum term | 2 years for force or confinement (3.E.1, 7.2) | NONE EXISTS. | not conforming |
| Harm thresholds | Not dependent on the institution's own findings (3.A.5) | State rule requires a team meeting after the third [EX] restraint of a student in a term. Measurable, set outside the district, but counted only from the district's own reports and it stops nothing. | not conforming |
| Stop paths | Tested, one independent (3.A.7, 3.C.1) | Nothing outside the room can halt a restraint in progress. State complaint reaches one case after the fact. | not conforming |
| Ending plan | Documented (3.A.9) | NONE EXISTS. | not conforming |
| Remedy | Independent, funded (3.A.10) | Tort claim limited by public-entity immunity; state complaints yield corrective action, not compensation. | not conforming |
| Data limits | Accountability records held independently (2.D.14) | Incident reports are kept by the district in the student file. NONE EXISTS for independent custody. | not conforming |
| Visibility | Knowable (3.B.9) | Policy public; parents notified the same day; counts published by the federal government every 2 [EX] years. Whether use has grown between reports: UNKNOWN. | compliance not demonstrated |
| Floors | Part II | Force not externally stoppable; seclusion beyond the threat (B6). | not conforming |
| Evasion | Part IV | The district's own audit found 40 [EX] restraints by contracted aides missing from the reported count. | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | State education agency complaint investigation | one_case | state education agency | independent | [EX] |
| 2 | Federal disability-rights lawsuit | one_practice | federal court | independent | [EX] |

A parent's refusal to include restraint in the student's plan is not a stop path: the state rule allows emergency restraint regardless.

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Neither path reaches the power as a whole.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Ecological threshold? | not_applicable — no ecological effect | |
| Economic (2.B) | Essentials conditional? | no | [EX] |
| Agency (2.C) | Told plainly; can report? | yes — same-day call and a written report within 1 [EX] school day | [EX] |
| Force (2.D.1) | Separately authorized, never aimed at pain, externally stoppable, independently reviewed? | no — rules bar restraint as punishment and ban face-down holds [EX], but no one outside the room can stop it and review is by the building principal | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds — (a) imminent bodily threat; (b) arrest before a judicial officer; (c) sanction after due process; (d) brief stop on suspicion? | no — seclusion can rest only on (a); the internal audit found 30% [EX] of seclusions began after refusal to follow directions, not an imminent threat, which is outside 2.D.3(a) | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical treatment | |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — after the fact only (state complaint) | [EX] |
| Expression (2.D.9) | Restricts expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens; reviewed? | yes — concentrated on students with disabilities; no independent review | [EX] |
| Identification (2.D.11) | Identification without cause? | not_applicable — acts on a named student | |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — no search under this power |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — seclusion is recorded under Confinement |  |

**B7. Data.** Incident form: student, staff, hold type, duration, injury. Kept in the student file under the discipline schedule. These are accountability records and should be held for 10 years [S1] by a custodian the district does not choose (2.D.14).

**B8. Dependencies and evasion.** About a quarter [EX] of behavior aides come from [STAFFING AGENCY]. Their incidents were partly missing from counts (B4). Under 4.2 and 4.5 the aides' restraints are the district's power.

**B9. Harms seen.** bodily: 9 [EX] student injuries last year (admitted in the district's own reports). psychological: trauma after seclusion (allegation). One staff injury claim [EX].

**B10. Decision inputs and oversight.** Staff judgment of imminent danger, after crisis-intervention training renewed every 2 [EX] years. No outside body audits incidents; the state reviews only complaints.

---

## Power P3 — Student-device monitoring

**B1. What it can do to people.** Software from [STUDENT-MONITORING VENDOR] scans everything students type, search, and store on district laptops and school accounts, at all hours, including at home. It flags content about self-harm, violence, sex, and drugs. Counselors contact flagged students; after school hours, "urgent" flags go to police for welfare checks.

**B2. Who and where.** Every student with a district device or account: about 14,000 [EX]. Family members who use the laptop at home are non-participants.

**B3. Authority basis.** `direct`. The district chose the tool and acts on the alerts. The vendor's flags are operationalized by the district; the vendor is in scope as part of the district's power (4.5).

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body, public record (3.A.1, 3.A.2) | Contract approved by the board on its consent agenda without discussion [EX]. | not conforming |
| Maximum term | 2 years for broad-reach or first-time powers (3.E.1, 7.2) | The contract runs 3 years [EX] and needs board approval to renew. It does expire, but the term exceeds 2 years [S1] and renewal is by the district itself. | not conforming |
| Harm thresholds | Published, measurable (3.A.5) | NONE EXISTS. | not conforming |
| Stop paths | Tested, one independent (3.A.7, 3.C.1) | Only the board can cancel. | not conforming |
| Ending plan | Documented (3.A.9) | The contract has a termination clause, return of district data within 60 [EX] days, and a certificate of deletion. | conforming |
| Remedy | Independent, funded (3.A.10) | NONE EXISTS. | not conforming |
| Data limits | Retention; deletion covers contractors (2.D.12, 7.6) | Vendor keeps flagged content 1 year [EX]; contract lets it keep "de-identified" data indefinitely for product work. | not conforming |
| Visibility | Knowable (3.B.9); inputs declared (5.3) | The acceptable-use form mentions monitoring; the flag categories and keyword lists are vendor secrets. | not conforming |
| Floors | Part II | Suspicionless monitoring; speech flags (B6); search of students' communications and devices without cause or judicial approval (2.D.15). | not conforming |
| Evasion | Part IV | Vendor reuse of data and police referral (B8). | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Board cancels or declines to renew the contract | whole_power | school board | not_independent | [EX] |
| 2 | Complaint to the federal student-records office | one_practice | federal education department | independent | [EX] |
| 3 | Lawsuit under the [STATE] student-privacy act | one_practice | state court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Path 1 is a vote of the district's own board, which does not count because the board is not independent of the district.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Ecological threshold? | not_applicable — software only | |
| Economic (2.B) | Essentials conditional on compliance? | yes — a family must sign the monitoring form to get the device needed for schoolwork (2.B.3) | [EX] |
| Agency (2.C) | Told plainly; can leave? | no — one line in an enrollment form; no opt-out that keeps a device | [EX] |
| Force (2.D.1) | Force? | not_applicable — no force by the district; police welfare checks are police power | |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no detention | |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical treatment | |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | no — a student cannot see or contest a flag | [EX] |
| Expression (2.D.9) | Restricts expression? News reporting or petitioning? Approval before publication? | yes — searches about sexual orientation and gender identity were flagged and led to counselor calls home [EX] | [EX] |
| Equal treatment (2.D.10) | Unequal burdens; reviewed? | yes — students who cannot afford a personal device are monitored for all their computing; not reviewed | [EX] |
| Identification (2.D.11) | Identified by surveillance without cause? | yes — every student is monitored with no individualized cause; school is an essential service, not a chosen activity | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | no — the software reads every document, chat, search and page on district devices and accounts, at home and at all hours [EX], with no individualized cause and no judicial approval. Signing the monitoring form is the price of the laptop needed for school (see Economic), so it is not consent freely given; and no inspection condition can reach communications or an essential service such as school | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | no — after-hours flags can bring a police welfare check to a student's home [EX], but the power bars no one from any place | [EX] |

**B7. Data.** Full text of documents, chats, searches, and browsing on district accounts, plus screenshots when flagged. About 9,000 [EX] alerts a year, of which 92% [EX] were closed as not actionable. Flags are stored by the vendor and in counselor notes. [EX]

**B8. Dependencies and evasion.** The vendor's de-identified data use survives contract end, which 4.4 treats as a derived output that must end with the source. After-hours flags sent to police move a district power into a power that uses force. [EX]

**B9. Harms seen.** psychological and communicative: students report avoiding help-seeking searches (allegation, district survey [EX]). informational: one student's identity disclosed to family through a flag (allegation). non_participant: siblings' use captured.

**B10. Decision inputs and oversight.** Vendor model and keyword lists, undeclared (5.3). No independent audit; the vendor reports its own accuracy. [EX]

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it | Quote | Verified? |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.D.14 (10 years), 7.2 (2 years) | | yes |
| S2 | quote | Core Requirements v1 | BPF: Core Requirements v1 | 2.D.11 | presence in public space, use of public transit, assembly, expression, or access to essential services is never such an activity | yes |
| S3 | quote | Core Requirements v1 | BPF: Core Requirements v1 | 3.A.5 | No threshold or stop condition may depend on any finding, classification, count, or process that the authority itself controls, produces, or can delay. | yes |

Figures tagged [EX] are illustrative and have no source.

## PART D — Honesty assertions

- [x] Every number has a source tag or an [EX] tag.
- [x] Nothing was presented as a real institution's data.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] Made in good faith, as a structural description.

Preparer: BPF examples working group (worked example).

## Teaching notes (non-binding)

- When nearly everyone affected is a child under compulsory attendance, exit (2.C.3) is not a real check, so the other paths carry more weight.
- Yearly readoption of a code of conduct by the district's own board is not a maximum term or an authorization: no authority may authorize or renew its own powers (3.A.2, 3.E.1).
- A threshold can be published, measurable, and set by an outside regulator, and still fail if it counts only what the district reports [S3]. P2's "third restraint" rule fails 3.A.5 on that point.
- Seclusion is confinement. It is allowed only under 2.D.3(a), for an imminent threat and no longer than the threat lasts; using it for non-compliance fails.
- Restraint shows the force test of 2.D.1 at a small scale: written limits can be good while nothing outside the room can stop a restraint in progress. Incident reports are accountability records that belong in independent custody (2.D.14) [S1].
- Contracted aides and the monitoring vendor are inside the district's powers, not outside them (4.1, 4.2, 4.5). Missing contractor incidents are an evasion finding even without any intent.
- Device monitoring identifies every student by surveillance without individualized cause. School is an essential service, so it cannot be treated as a chosen, licensed activity [S2] (2.D.11). Requiring consent to monitoring as the price of a school laptop is leverage over an essential (2.B.3).
- A good exit clause in a vendor contract can make the ending plan conforming (3.A.9) while data limits still fail because de-identified copies survive (4.4, 7.6).
- A suspension or expulsion entry is a sanction against a student, not an accountability record (2.D.14). It follows 2.D.12 and 2.D.6, and the student may ask for its earlier deletion unless a hold applies; it is not kept 10 years [S1] like P2's restraint reports, which record what staff did. The 5-year [EX] schedule with logged destruction is a good start, but without periodic re-justification or a known early-deletion route, P1's data limits stay not conforming.
- Searching a student's phone or bag for a code violation is a search under 2.D.15: reasonable suspicion supplies individualized cause, but nothing supplies judicial approval or prompt review afterwards. Device monitoring fails 2.D.15 more plainly: no cause, no approval, and a consent form that is the price of a school laptop.
