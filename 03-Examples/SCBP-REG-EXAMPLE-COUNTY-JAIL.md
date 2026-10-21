---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-COUNTY-JAIL
record_version: 1
supersedes: NONE
form: {name: registration, version: 1.0.0, date: 2026-10-21}
core_requirements: {version: v1, date: 2026-10-21}
bundle: NONE
vocab_version: 1.0.0
prepared_by: person
ai_tool: NONE
prepared_date: 2026-10-21
sources_checked_date: 2026-10-21
institution:
  name: "[COUNTY] Jail"
  legal_entity: "[COUNTY] (county government), operated by the elected [COUNTY] Sheriff"
  related_entities: "[JAIL MEDICAL CONTRACTOR]; [PHONE VENDOR]; [COMMISSARY VENDOR]; state jail inspection board"
  type: government
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: "[COUNTY]"
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Pretrial custody"
    category: arrest_detention_or_confinement
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
      data_limits: not_demonstrated
      visibility: not_demonstrated
      floors: not_conforming
      evasion: not_demonstrated
  - power_id: P2
    short_name: "Force by jail staff"
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
      visibility: conforming
      floors: not_conforming
      evasion: conforming
  - power_id: P3
    short_name: "Phone, commissary and pay-to-stay fees"
    category: fines_fees_or_charges
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
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_conforming
      evasion: not_conforming
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [COUNTY] Jail — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** The county jail holds people arrested in the county until a court releases them, and people serving short sentences. Most people inside have not been convicted. Staff search, restrain and use force on people held. The jail charges people for phone calls, commissary goods and each day they are held, and keeps the records of deaths and force inside its walls.

A2. **Legal basis.** The [STATE] county jails statute makes the elected Sheriff keeper of the jail. A state jail inspection board sets minimum standards and inspects. Courts order who is held and who is released.

A3. **Who controls it.** The Sheriff, elected for 4-year terms [EX]. The County Board sets the budget. The state inspection board, appointed by the Governor, inspects. A federal court supervises medical care and force under a class settlement (see P2).

A4. **Related entities.** [JAIL MEDICAL CONTRACTOR] provides health care. [PHONE VENDOR] runs calls and video visits. [COMMISSARY VENDOR] sells food and hygiene items. Figures in this record belong to the jail unless stated.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — Pretrial custody: holding people who have not been tried.
- P2 — Force by jail staff, including restraint chairs, chemical spray and cell extractions.
- P3 — Phone, commissary and pay-to-stay fees.
- Records of deaths and force are covered as accountability records under P2 (B4 Data limits, B7).
- Not recorded: custody of sentenced people (2.D.3(c)); booking photos posted online (information_control_or_visibility); medical care decisions.

---

## Power P1 — Pretrial custody

**B1. What it can do to people.** Hold a person in a cell from booking until a court releases them or the case ends. The jail decides housing, classification, segregation and the timing of release once a release order arrives.

**B2. Who and where.** About 1,400 people on an average day [EX], of whom about 75% [EX] await trial. About 30,000 bookings a year [EX]. Families and employers of people held are non-participants.

**B3. Authority basis.** `direct`. The court orders custody; the jail holds the person and runs booking, transport to court and release.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. The statute makes the Sheriff keeper of the jail; no separate authorization of pretrial custody | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | The state board sets a rated capacity of 1,250 beds [EX]; exceeding it leads only to a notice | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | The inspection board can order the jail closed (whole power); never used here and never tested (B5) | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Lawsuits only; no funded process for people held past a release order | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Booking fingerprints and photos go to the state database; retention there UNKNOWN | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Daily population is published; length of stay and over-detention are not | compliance not demonstrated |
| Floors | See B6 (Part II) | Money bail holds; no 30-day review [S1]; over-detention (2.D.3(b)); blanket strip searches and cell searches with no individualized cause or judicial review (2.D.15) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | The jail rents 100 beds [EX] to national immigration authorities; whether rented beds follow the same rules is UNKNOWN | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | State inspection board order closing the jail or capping its population | whole_power (at this facility) | the state jail inspection board | partly_independent (some of its seats [EX] are held by serving sheriffs) | [EX] |
| 2 | Bail review or habeas petition | one_case | a county judge | independent | [EX] |
| 3 | Class-action population cap ordered by a federal court | one_practice | a federal court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — `yes, path 1 — holder partly independent`, for this facility, under an existing statute. The path has never been used or tested, and closing the jail would move people elsewhere unless a minimum essential function is arranged (3.C.5).

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes — about 40% of pretrial people [EX] are held only because they cannot pay money bail of under 1,000 currency units [EX] | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — grievances require a paper form; there is no plain notice of how to seek release | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | see P2 | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 hours [S1], with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | partly. Pretrial custody must fit (b). First appearance happens within 48 hours [S1] in 96% of bookings [EX]. But (b) also requires an individualized finding of flight risk or imminent harm, a less restrictive measure first, a legal maximum, and review at least every 30 days [S1]. People held on unpaid money bail have no such finding; nothing reviews custody every 30 days [S1]; and the jail held 210 people [EX] past their release orders last year, by a median of 9 hours [EX] | [EX] |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm? | not_applicable — medical care by the contractor is not recorded here | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | partly — a public defender is appointed at first appearance [EX], and bail review exists on motion before a judge in open court; segregation decisions, which deepen confinement, are reviewed only by jail staff, with no lawyer | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — allegation that people who filed grievances lost phone access | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — length of stay by group not reviewed | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | no — identification at booking follows an arrest on individualized cause | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | no — everyone booked is strip-searched under a blanket policy, without an individualized finding [EX], and cells are searched at random [EX]; no judicial officer approves or later reviews these searches. Property taken at booking is returned at release; property not claimed within 90 days [EX] is destroyed | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — custody is recorded under Confinement |  |

**B7. Data.** Booking records, classification scores, medical intake, fingerprints and photos. Purpose: custody and identification. Retention UNKNOWN; no deletion record.

**B8. Dependencies and evasion.** Courts send people in; the jail cannot refuse. Rented beds bring income of about 9 million currency units a year [EX], which makes reducing population cost money (3.B.7).

**B9. Harms seen.**
- agency, economic — admitted: the jail's own audit counts the over-detentions in B6.
- economic, non_participant — allegation: people lost jobs and housing while held on small bail amounts.

**B10. Decision inputs and oversight.** Court orders, an internal classification tool for housing (not published, 5.3), staff decisions on segregation. The state board inspects once a year [EX].

---

## Power P2 — Force by jail staff

**B1. What it can do to people.** Hold, take down, handcuff, strap a person into a restraint chair, use chemical spray or an electrical weapon, and remove a person from a cell by force.

**B2. Who and where.** Everyone held. About 1,100 uses of force a year [EX].

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. Sheriff's policy under the jail statute | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | The settlement sets a 4-hour [EX] limit on restraint-chair use and reporting targets, but breaching them leads only to monitor reports | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | The federal court can enforce bans on techniques (one practice) | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Lawsuits; a national law limits suits by people in custody until internal grievances are exhausted | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Force reports kept 3 years [EX] and jail video 60 days [EX] by the Sheriff; death reviews kept by the Sheriff and withheld as "investigative records". Required: 10 years [S1] in custody chosen by an independent body (B7) | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | The monitor's reports and the force policy are published; the jail statute plainly sets no expiry and no renewal, so the absence is knowable (failure recorded under Maximum term) | conforming |
| Floors | See B6 (Part II) | Force not separately authorized or independently reviewed (2.D.1); records of force can be destroyed by the jail (2.D.8). Whether a 3.D.5 pattern exists is not established (B9) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Force is used only by sworn jail staff | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Enforcement of the class settlement, with a court-appointed monitor | one_practice | the federal judge and monitor | independent | [EX] |
| 2 | Criminal charge against a staff member | one_case | the county prosecutor | partly_independent (works with the Sheriff daily) | [EX] |
| 3 | Internal grievance | one_case | jail command staff | not_independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | not_applicable — no charges | |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — reports of force need a grievance form filed within 7 days [EX] | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | no — not separately authorized; reviewed first by jail supervisors; the monitor reviews a sample only | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | see P1 | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, incapacity found by an independent clinician? | UNKNOWN — whether contractor staff medicate people over refusal during force incidents is not reported | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | partly — through the courts, after exhausting grievances | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN | |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | yes, partly reviewed — the monitor found people with serious mental illness were 3 times [EX] as likely to have force used on them | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | not_applicable | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — searches are recorded under P1; cell extractions are recorded under Force |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — custody is recorded under P1 |  |

**B7. Data.** Force reports, incident video, injury records, death reviews, and medical records at death. These are accountability records (Definitions); 2.D.14 requires them kept 10 years [S1] in independent custody, with holds placed by the custodian, not the jail. Today the Sheriff decides what is kept: video sits on the [PHONE VENDOR]'s security platform, which overwrites footage after 60 days [EX] unless staff flag it, and medical records of deaths are held by the contractor, outside public-records law. Only a court preservation order in one case, or the state attorney general's 30-day [EX] death report, reaches these records from outside.

**B8. Dependencies and evasion.** [JAIL MEDICAL CONTRACTOR] clears people for restraint and documents injuries; its staff report to the contractor, not the Sheriff.

**B9. Harms seen.**
- bodily — settled without admission: the county agreed to the class settlement after a lawsuit over force and medical care; it admitted no violation.
- bodily — adjudicated: one staff member convicted of assault on a person held, in the last 3 years [EX].
- bodily — admitted: the jail reported 11 deaths in custody over 3 years [EX], including 2 after restraint [EX].
- informational — admitted: in a lawsuit over a death, the county disclosed that video from the relevant hour had been overwritten.

**3.D.5 review, not a 3.D.5 finding.** Deaths after restraint, force concentrated on people in mental-health crisis, and repeated monitor findings are the kind of facts 3.D.5 treats as structural. But for an authority that has not adopted the Core Requirements, a pattern finding needs established Floor violations (5.2). Here only one conviction is adjudicated; the class settlement admits nothing, and the causes of the 2 deaths [EX] after restraint are not established. The record supports a recorded concern and a request for a 3.D.5 review. If violations are established, settling individual claims would not discharge the pattern, and a new Sheriff would not reset it.

**B10. Decision inputs and oversight.** The force policy and staff judgment. The monitor reports twice a year [EX] to the court.

---

## Power P3 — Phone, commissary and pay-to-stay fees

**B1. What it can do to people.** Charge people held, and their families, for calls, video visits and commissary goods, and bill each person a daily fee for being held. Unpaid daily fees are sent to a collection agency after release.

**B2. Who and where.** Everyone held and the people who call or send them money. Families pay most phone and commissary charges.

**B3. Authority basis.** `direct`. The county sets the fees; vendors collect them under contract.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The County Board approved the fee schedule at a public meeting. It also receives the revenue, so it is not independent of the power | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | NONE EXISTS for the fees. Vendor contracts run 5 years [EX] | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | The national communications regulator caps call rates; a state court can rule on the daily fee in one case | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | Contracts can be ended; what happens to balances owed is UNKNOWN | compliance not demonstrated |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | The phone vendor records all calls and keeps them; length UNKNOWN; whether voiceprints are taken UNKNOWN | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Fee schedule, vendor contracts and commission amounts are published on the county site | conforming |
| Floors | See B6 (Part II) | Daily fees grow while people cannot pay (2.B.2); all non-legal calls recorded and searchable without individualized cause, and cash taken at booking applied to fees without a hearing (2.D.15) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | The county receives a 40% commission [EX] on phone revenue and 25% [EX] on commissary sales; vendors carry out the charge | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | National regulator's rate cap on calls | one_practice | the national communications regulator | independent | [EX] |
| 2 | Court ruling that the daily fee cannot be collected from one person | one_case | a state court | independent | [EX] |
| 3 | County Board repeals the fee schedule | whole_power | the County Board | not_independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Path 3 is a vote of the county's own governing board, which also receives the revenue; under the B5 definition it does not count.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes — the daily fee of 20 currency units [EX] accrues for every day held, including days held because the person could not pay bail; collection adds a 30% charge [EX]; there is no waiver for inability to pay. Contact with family depends on paying for calls | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — the daily fee is explained in the inmate handbook only | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable directly; 2.D.3 bars using confinement for economic extraction, which the daily fee and commissions approach | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical treatment | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | partly — in a collection case in court | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | UNKNOWN — whether the phone vendor builds voiceprints of callers is not disclosed | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | no — every call except calls to lawyers is recorded and can be searched by staff and the phone vendor [EX], with no individualized cause or judicial approval, as the price of contact with family. Cash a person carries at booking is applied to booking and daily fees [EX] with no hearing | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — custody is recorded under P1 |  |

**B7. Data.** Call recordings, called numbers, payment records of family members. Family members are non-participants whose data are collected.

**B8. Dependencies and evasion.** [PHONE VENDOR] and [COMMISSARY VENDOR] pay commissions to the county. Under the Definitions, a commission from a vendor serving people subject to the power is economic extraction, whoever collects it (4.1).

**B9. Harms seen.**
- economic — admitted: county reports show about 2.5 million currency units [EX] in commissions last year and 4 million [EX] in unpaid daily fees sent to collection.
- psychological, non_participant — allegation: families reduced calls because of cost.

**B10. Decision inputs and oversight.** The Board's fee schedule. Contracts are published. No outside audit of whether fees exceed cost.

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.D.3(b) (48 hours, 30 days), 2.D.14 (10 years) | | yes |

---

## PART D — Honesty assertions

- [x] Every number has a source tag. In this worked example, institutional figures carry [EX] and are illustrative.
- [x] Nothing was invented as fact about a real institution. This is a composite example.
- [x] Public sources and first-hand observation only. Nothing private, leaked, or speculative.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] I made this record in good faith, as a structural description, not an accusation.

Preparer: BPF examples working group (worked example).

---

## Teaching notes (non-binding)

- Pretrial custody must fit 2.D.3(b) in full: a judge within 48 hours [S1] is only the first step. An individualized finding, a less restrictive measure first, a legal maximum, and review every 30 days [S1] are also required.
- Holding someone only because they cannot pay bail is confinement without the 2.D.3(b) finding, and also a 2.B.1 problem.
- Holding people past a release order is the jail's own failing, separate from the court's decision (3.A.1: each power answers for itself).
- Deaths after restraint and a settlement without admission support a recorded concern and a request for a 3.D.5 review, not a 3.D.5 finding: for a non-adopting authority, a pattern finding needs established Floor violations (5.2).
- Death and force records are accountability records. 2.D.14 puts them in independent custody for 10 years [S1], with holds placed by the custodian. A video system that overwrites by default fails this even without bad intent (1.2).
- Phone and commissary commissions are economic extraction by definition, and pay-to-stay fees that grow while a person cannot pay break 2.B.2.
- A state inspection board that can close a jail under an existing statute is a real whole-power stop path. It still fails 3.A.7 here: it is only partly independent and has never been tested.
- An authorizing vote by the body that receives the revenue (County Board on fees) is a public decision but not an independent one (3.A.2), and its power to repeal the fees is not a whole-power stop path (B5 definition).
- 2.D.15 applies inside a jail. Being lawfully held is not individualized cause for a strip search, a cell search, or recording every call; each needs its own cause and a judicial officer's approval or prompt review. The blanket booking strip search (P1) and universal call recording (P3) are recorded as Floor gaps.
