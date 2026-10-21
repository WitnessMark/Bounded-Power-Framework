---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-REGIONAL-HEALTH-SYSTEM
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
  name: "[REGION] Health System"
  legal_entity: "[REGION] Health System, a nonprofit corporation"
  related_entities: "[COLLECTION AGENCY]; [DEBT BUYER]; [STATE] mental health agency (designates hold facilities); [STATE] protection and advocacy agency"
  type: nonprofit
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: "[REGION]"
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Involuntary psychiatric hold"
    category: arrest_detention_or_confinement
    authority_basis: direct
    uses_force_or_confinement: "yes"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: conforming
      harm_thresholds: not_conforming
      stop_paths: not_demonstrated
      ending_plan: not_conforming
      remedy: not_conforming
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_conforming
      evasion: not_conforming
  - power_id: P2
    short_name: "Restraint, seclusion and medication without consent"
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
      evasion: conforming
  - power_id: P3
    short_name: "Medical-debt collection"
    category: fines_fees_or_charges
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
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_conforming
      evasion: not_conforming
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [REGION] Health System — Registration (worked example)

## PART A — The institution

A1. **What it is.** A nonprofit system of 4 [EX] hospitals and about 60 [EX] clinics. Most of what it does is care people ask for. Three of its powers are not chosen by the people they act on: it can hold a person for psychiatric evaluation, restrain or medicate a person without consent, and pursue unpaid bills through the courts.

A2. **Legal basis.** State hospital licence; the [STATE] Mental Health Code; designation by the [STATE] mental health agency as a hold facility; federal hospital participation rules; federal tax-exemption rules for nonprofit hospitals, named generally. [EX]

A3. **Who controls it.** A self-perpetuating board of 15 [EX] trustees appoints the chief executive. [EX]

A4. **Related entities.** [COLLECTION AGENCY] collects accounts; [DEBT BUYER] buys older accounts. Security officers are employees of the system [EX]. All figures belong to the system unless stated.

A5. **Adoption.** not_adopted. [EX]

A6. **Powers found.**
- P1 Involuntary psychiatric hold.
- P2 Physical restraint, seclusion, and medication without consent.
- P3 Collection of medical debt, including lawsuits.
- Not recorded: patient data use, price setting, reports to child welfare.

---

## Power P1 — Involuntary psychiatric hold

**B1. What it can do to people.** A designated clinician can hold a person who is judged a danger to self or others, or unable to provide for their own basic needs, for a fixed evaluation period of up to 5 days [EX]. Security officers stop the person leaving. Holding longer needs a court petition.

**B2. Who and where.** People brought to its emergency departments, often by police or family. About 1,800 [EX] holds a year.

**B3. Authority basis.** `direct`. The system's own clinicians decide and its own staff confine.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The state mental health agency designates the system's units after an inspection. It is independent, but it holds no hearing for affected people and makes no findings on each requirement. | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | Designation expires every year [EX] and lapses unless the state renews it. | conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. Designation standards concern staffing and rooms, not harm. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | The state can revoke the designation (whole power here); never tested [EX]. | compliance not demonstrated |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS. | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | An independent patient-rights advocate can investigate; compensation only through a lawsuit. | not conforming |
| Data limits | Retention; accountability records held independently (2.D.12–2.D.14, 7.6) | The hospital retains clinical records and hold documentation in its medical-record system for 10 years [EX]. Clinical information needed for patient care must be distinguished from accountability records documenting the exercise and review of confinement power. Hold orders, statutory grounds, timing, independent-review findings, complaints, and incidents should be assessed for the independent accountability custody required by 2.D.14. The scenario does not demonstrate an independent custodian for those accountability records. It also does not establish that the entire clinical record must be transferred to one. Data-limits compliance is therefore not demonstrated to the extent independent accountability custody is missing, while any separately established retention or deletion violation should be identified on its own evidence. | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9) | Written rights notice at the start of every hold; the state publishes the list of designated units with expiry dates and yearly hold counts by facility [EX]. | conforming |
| Floors | See B6 (Part II) | "Basic needs" ground; fixed duration; danger-to-self risk not confirmed by an independent clinician (B6); blanket search and holding of belongings with no later review (2.D.15). | not conforming |
| Evasion | Not split, outsourced, laundered, or using proxies (Part IV) | Hours held in the emergency department before admission are not counted toward the 5-day [EX] limit; median 30 hours [EX]. | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Revocation or non-renewal of the hold designation | whole_power | [STATE] mental health agency | independent | [EX] |
| 2 | Review hearing before a judicial officer within the hold period | one_case | judicial officer | independent | [EX] |
| 3 | Habeas corpus petition | one_case | state trial court | independent | [EX] |
| 4 | Release by the attending psychiatrist on reassessment | one_case | attending psychiatrist | not_independent | [EX] |

Statement: *Can anything stop this power as a whole?* — yes, path 1, for this system's units only, held by an independent agency under existing law. It has never been used or tested [EX].

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Ecological threshold? | not_applicable — no ecological effect | |
| Economic (2.B) | Essentials conditional; growing obligations? | yes — people held are billed for the hold, and the bill enters P3 collections | [EX] |
| Agency (2.C) | Told plainly; can report harm; can leave? | yes for notice (written rights form, interpreter on request); no for leaving | [EX] |
| Force (2.D.1) | Force rules? | see P2 — holds are enforced by security officers using P2 | |
| Confinement (2.D.3) | Only on the four permitted grounds — (a) imminent bodily threat to identifiable people; (b) arrest before a judicial officer; (c) sanction after due process; (d) brief stop on suspicion? | no — only (a) could apply. Inability to meet basic needs is not an imminent threat of bodily harm under 2.D.3(a). A danger-to-self hold fits (a) only when an independent clinician confirms the risk, for the shortest time needed, with prompt independent review [S4]; here the system's own clinician decides, the 5-day [EX] period runs whether or not the risk has ended, and a judicial hearing comes only within the hold period, after an uncounted emergency-department wait (median 30 hours [EX]) | [EX] [S3] [S4] |
| Emergency medical care (2.D.2) | Treatment without consent only on incapacity plus imminent serious harm, incapacity found by an independent clinician? | not_applicable — treatment over objection is recorded under P2 | |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes, in part — a judicial review hearing within the hold period and habeas, with a public defender at the hearing [EX]; hearings are closed unless the person asks for an open one [EX]. Whether statements made to the evaluating clinicians, without any warning that they may be used, are used as evidence at the hearing is UNKNOWN | [EX] |
| Expression (2.D.9) | Punishes lawful expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens; reviewed? | UNKNOWN — the state publishes counts by facility, not by group | |
| Identification (2.D.11) | Identification without cause? | not_applicable — acts on a person present | |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | no — on arrival, security searches the person and their bags and keeps phones, clothing and belongings until discharge [EX], with no individualized cause beyond the hold itself; no judicial officer reviews these searches afterwards. Belongings are returned at discharge [EX] | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — the hold is recorded under Confinement |  |

**B7. Data.** Clinical notes, hold forms, police transport forms. Retention: see B4. Clinical notes serve patient care and stay confidential. Hold orders, grounds, timing, review findings, complaints, and incident reports also document the exercise of confinement power, and those are the accountability records assessed under 2.D.14. Hold forms are shared with the state agency and, for longer commitments, with the federal firearm background-check system, which the person may not know. [EX]

**B8. Dependencies and evasion.** Police bring about 45% [EX] of people held. The emergency-department wait before the hold clock starts (B4) is a change of sequence that lengthens confinement without new authority (4.1).

**B9. Harms seen.** agency and psychological: confinement of people later found not to meet criteria (allegation). bodily: see P2. economic: hold bills (admitted; billing is policy). A state inspection found hold forms missing required signatures in 12% [EX] of files (adjudicated, inspection finding).

**B10. Decision inputs and oversight.** Statutory criteria and the clinician's judgment; the system's assessment checklist is not published (5.3). The state agency inspects yearly [EX]; the protection-and-advocacy agency can enter and investigate.

---

## Power P2 — Restraint, seclusion and medication without consent

**B1. What it can do to people.** Staff can hold a patient down, tie the patient to a bed, lock the patient in a room alone, or inject sedating medication without consent. It is used on psychiatric patients and on agitated patients in the emergency department. Separately, clinicians treat patients who arrive unconscious or without capacity.

**B2. Who and where.** Patients in all 4 [EX] hospitals. About 2,400 [EX] restraint or seclusion episodes and 900 [EX] doses of emergency sedation over objection each year.

**B3. Authority basis.** `direct`. System staff act on patients' bodies.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body, public record (3.A.1, 3.A.2) | Federal hospital rules allow restraint in every hospital. No separate authorization of this power. | not conforming |
| Maximum term | 2 years for force (3.E.1, 7.2) | NONE EXISTS. | not conforming |
| Harm thresholds | Not dependent on the institution's own findings (3.A.5) | NONE EXISTS. Deaths in restraint must be reported to the federal regulator, which does not stop anything. | not conforming |
| Stop paths | Tested, one independent (3.A.7, 3.C.1) | Nothing outside the unit can halt a restraint in progress. | not conforming |
| Ending plan | Documented (3.A.9) | NONE EXISTS. | not conforming |
| Remedy | Independent, funded (3.A.10) | Lawsuit or licensing complaint; no funded remedy. | not conforming |
| Data limits | Accountability records held independently (2.D.14) | Restraint logs held by the system. NONE EXISTS for independent custody. | not conforming |
| Visibility | Knowable (3.B.9) | Policy given to psychiatric patients on admission; counts not published. | compliance not demonstrated |
| Floors | Part II | Not externally stoppable; capacity decided by the treating team (B6). | not conforming |
| Evasion | Part IV | Done only by employed staff; no contracted security or off-duty police [EX]. | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Federal regulator survey after a complaint, with a corrective plan | one_practice | federal health-care regulator | independent | [EX] |
| 2 | State licensing complaint | one_case | state health department | independent | [EX] |
| 3 | Physician ends the order on reassessment | one_case | ordering physician | not_independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Each path reaches one case or one practice.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Ecological threshold? | not_applicable — no ecological effect | |
| Economic (2.B) | Essentials conditional? | no | [EX] |
| Agency (2.C) | Told plainly? | yes for psychiatric patients; no for emergency-department patients | [EX] |
| Force (2.D.1) | Separately authorized, never aimed at pain, externally stoppable, independently reviewed? | no — federal rules require a physician order, a face-to-face check within 1 hour [EX], and orders of 4 hours [EX] at most for adults, which meet "minimum necessary" and "cease when purpose met"; but nothing external can stop it and review is internal | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | yes — seclusion is limited by rule to immediate physical safety, ground (a); logs show average episodes of 2 hours [EX] | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent only on incapacity plus imminent serious harm, incapacity found by an independent clinician, valid refusals honored? | partly — fits for unconscious patients; fails for medication over objection, where the treating team decides capacity (see below) | [EX] [S2] |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — after the fact only | [EX] |
| Expression (2.D.9) | Restricts expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens; reviewed? | UNKNOWN — not analysed by group | |
| Identification (2.D.11) | Identification without cause? | not_applicable | |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — searches on arrival are recorded under P1 |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — seclusion is recorded under Confinement |  |

Emergency care without consent (2.D.2) splits three ways here. (1) Treating an unconscious trauma patient is emergency care: the patient lacks capacity, delay risks serious harm, and treatment is confined to the emergency; the system's policy also requires a search for an advance directive or surrogate [EX]. That part fits 2.D.2. (2) Sedation given to stop a patient striking staff is not medical care but force, and must meet 2.D.1. (3) Medication given over the objection of a patient whom the treating psychiatrist judges to lack capacity fails 2.D.2, because incapacity is decided by the same team seeking the patient's compliance, not by an independent clinician. [EX]

**B7. Data.** Order, reason, duration, injuries, and debrief notes in the medical record, kept 10 years [EX]. Deaths reported to the federal regulator. [EX]

**B8. Dependencies and evasion.** Security officers are employees, trained yearly [EX]. No sign of splitting or outsourcing.

**B9. Harms seen.** bodily: 14 [EX] patient injuries during restraint last year (admitted in incident reports). psychological: trauma from seclusion (allegation). A federal survey found a restraint order renewed without a physician exam in 3 [EX] sampled charts (adjudicated, survey finding).

**B10. Decision inputs and oversight.** Clinical judgment under a published nursing protocol (5.3). The federal regulator and an accrediting body survey every 3 [EX] years; the protection-and-advocacy agency can investigate.

---

## Power P3 — Medical-debt collection

**B1. What it can do to people.** For unpaid bills, the system sends accounts to [COLLECTION AGENCY] after 120 [EX] days, sues patients, garnishes wages, and places judgment liens on homes. Judgments carry the state rate of 9% [EX] interest. It may refuse scheduled non-emergency care to patients owing more than 5,000 currency units [EX] unless they sign a payment plan.

**B2. Who and where.** Patients and their families across [REGION]. About 30,000 [EX] accounts in collection and 400 [EX] lawsuits a year.

**B3. Authority basis.** `direct`. The system sets its own charges and enforces them through courts it petitions.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body, public record (3.A.1, 3.A.2) | The system's board sets the charge list and collection policy. Self-authorization. | not conforming |
| Maximum term | Set expiry (3.E.1, 7.2) | NONE EXISTS. | not conforming |
| Harm thresholds | Published, measurable (3.A.5) | NONE EXISTS. | not conforming |
| Stop paths | Tested, one independent (3.A.7, 3.C.1) | Court in each suit; state attorney general for practices. Nothing for the whole power. | not conforming |
| Ending plan | Documented (3.A.9) | NONE EXISTS. | not conforming |
| Remedy | Independent, funded (3.A.10) | A patient may apply for financial assistance up to 240 [EX] days after the first bill and get collection actions reversed and payments refunded; decided by the system, not an independent body. | not conforming |
| Data limits | Retention; deletion records (2.D.12, 7.6) | Account and credit-report data: retention UNKNOWN. | compliance not demonstrated |
| Visibility | Knowable (3.B.9) | Financial assistance policy and plain-language summary posted, printed on bills, and offered at registration, as federal tax-exemption rules require [EX]. | conforming |
| Floors | Part II | Escalating balances; leverage over care (B6). | not conforming |
| Evasion | Part IV | Accounts sold to [DEBT BUYER], which sues without the assistance screening (B8). | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Defense in the collection lawsuit | one_case | state trial court | independent | [EX] |
| 2 | Charitable-trust or consumer-protection action | one_practice | state attorney general | independent | [EX] |
| 3 | Board changes the collection policy | whole_power | system board | not_independent | [EX] |

Loss of tax exemption is not a stop path: it would not stop collections. Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Path 3 is a decision of the system's own board, which does not count because the board is not independent of the system.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Ecological threshold? | not_applicable — no ecological effect | |
| Economic (2.B) | Essentials conditional; growing obligations; path out? | yes — judgment interest and collection fees grow when a patient cannot pay (2.B.2); non-emergency care is withheld until a payment plan is signed (2.B.3); free care below 200% [EX] of the poverty line is a path out for some | [EX] |
| Agency (2.C) | Told plainly; can report; can leave? | yes for notice of the assistance policy; no for exit once sued | [EX] |
| Force (2.D.1) | Force? | not_applicable — no force | |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no detention | |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — billing only | |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — in court, though 70% [EX] of suits end in default judgments | [EX] |
| Expression (2.D.9) | Restricts expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens; reviewed? | UNKNOWN — suits are concentrated in 5 [EX] postal codes; not reviewed by group | [EX] |
| Identification (2.D.11) | Identification without cause? | not_applicable | |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | yes — wages are garnished and liens placed only after a court judgment [EX], though most suits end in default (see Due process) | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Names, addresses, employers, balances, and income documents from assistance applications. Shared with the collection agency, the debt buyer, and credit bureaus. Data passed to the debt buyer stays covered by the system's limits (4.4). [EX]

**B8. Dependencies and evasion.** Selling accounts to [DEBT BUYER] moves collection outside the system's own assistance screening; the buyer's suits are the system's power by functional equivalence (4.1, 4.5). [EX]

**B9. Harms seen.** economic: wage garnishment and liens (admitted in court records). bodily: patients delaying care over debt (allegation). A state attorney general settlement required the system to screen accounts before suing, without admission [EX] (settled without admission).

**B10. Decision inputs and oversight.** Balance, days outstanding, and a vendor "propensity to pay" score [EX], which is not published (5.3). The state attorney general and the federal tax regulator review charity spending, not collection outcomes.

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it | Quote | Verified? |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.D.14 (10 years), 7.2 (2 years) | | yes |
| S2 | quote | Core Requirements v1 | BPF: Core Requirements v1 | 2.D.2 | Incapacity must be determined by a clinician independent of any authority seeking the person's compliance. | yes |
| S3 | quote | Core Requirements v1 | BPF: Core Requirements v1 | 2.D.3(a) | to stop an imminent threat of bodily harm to identifiable people, for no longer than the threat lasts | yes |
| S4 | quote | Core Requirements v1 | BPF: Core Requirements v1 | 2.D.3(a) | holding a person at imminent risk of death or serious bodily harm to themself, when an independent clinician confirms the risk, for the shortest time needed, with prompt independent review | yes |

Figures tagged [EX] are illustrative and have no source.

## PART D — Honesty assertions

- [x] Every number has a source tag or an [EX] tag.
- [x] Nothing was presented as a real institution's data.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] Made in good faith, as a structural description.

Preparer: BPF examples working group (worked example).

## Teaching notes (non-binding)

- A private nonprofit can hold force and confinement powers. The test is function, not legal form (1.3).
- An emergency hold fits 2.D.3(a) only for an imminent threat of bodily harm and only while it lasts [S3]. A "basic needs" ground and a fixed 5-day [EX] clock both go beyond it.
- 2.D.3(a) covers a danger-to-self hold, but only on its own conditions: imminent risk of death or serious bodily harm, confirmed by an independent clinician, for the shortest time needed, with prompt independent review [S4]. P1's holds are decided by the system's own clinicians and run a fixed 5 days [EX], so the rule does not cure them; the Floors finding stays not conforming.
- A yearly designation by an independent state agency gives a conforming maximum term (3.E.1, 7.2) and a real whole-power stop path. It still fails authorization because no one affected is heard and no findings are made on each requirement (3.A.2), and the stop path counts fully only once tested (3.A.7).
- Emergency care without consent (2.D.2) and force (2.D.1) must be kept apart. Treating an unconscious patient is care. Sedating a patient to stop violence is force. Medicating over objection after a capacity call by the treating team fails 2.D.2 [S2].
- Evidence of how coercive power was used is an accountability record: hold orders, grounds, timing, review findings, complaints, incidents, and restraint logs are kept 10 years [S1] in custody the institution does not choose (2.D.14). That does not mean the patient's whole confidential medical file goes to an outside custodian. Clinical records keep their confidentiality protections. For P1 the scenario shows no independent custodian, but does not show which records the hospital alone holds, so data limits are not demonstrated rather than not conforming.
- Medical debt shows the Economic Floor: interest and fees that grow because a person cannot pay (2.B.2), and withholding care to secure a payment plan (2.B.3). A published assistance policy makes visibility conforming without curing either.
- Clock-starting rules and debt sales are ordinary evasion patterns: a change of sequence or intermediary that keeps the same effect (4.1, 4.5).
- Searching every person held and keeping their phone until discharge is a search and seizure under 2.D.15. A hold is not individualized cause for a search; a search for an item that could cause imminent harm may go ahead without approval, but must be reviewed promptly afterwards. Garnishment after a court judgment (P3) meets the judicial-approval part of the rule.
