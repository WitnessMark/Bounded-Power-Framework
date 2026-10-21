---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-COUNTY-FAMILY-COURT
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
  name: "[COUNTY] Family Court"
  legal_entity: "[STATE] judicial branch, [COUNTY] trial court, family division"
  related_entities: "[STATE] child support enforcement agency; [COUNTY] Sheriff (executes jail orders); court-appointed custody evaluators"
  type: government
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: "[COUNTY]"
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Custody and parenting-time orders"
    category: removal_custody_or_placement
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
      floors: not_demonstrated
      evasion: conforming
  - power_id: P2
    short_name: "Contempt jail for unpaid support"
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
      data_limits: not_conforming
      visibility: not_demonstrated
      floors: not_conforming
      evasion: not_demonstrated
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [COUNTY] Family Court — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** The family division of the county trial court. Judges decide which parent a child lives with, who makes decisions for the child, and when each parent sees the child. The same court enforces child-support orders, and can jail a parent for contempt when support is not paid. This record does not cover child protection cases, which a separate record would treat.

A2. **Legal basis.** The [STATE] Family Code, the [STATE] court rules, and the state and national constitutions, which courts have read to protect a parent's right to raise a child. A national interstate custody law decides which state's court may hear a case.

A3. **Who controls it.** Judges are elected for 6-year terms [EX]. The state high court sets rules and supervises judges through a judicial conduct commission. The state appeals court hears appeals.

A4. **Related entities.** The [STATE] child support enforcement agency files contempt motions and runs income withholding, licence suspension and tax-refund interception; those are its own powers and are not recorded here. The [COUNTY] Sheriff carries out jail orders. Private custody evaluators, paid by the parents, prepare reports for the judge.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — Custody and parenting-time orders.
- P2 — Contempt jail for unpaid child support.
- Not recorded: protective orders; fees for evaluators and supervised visits (fines_fees_or_charges); termination of parental rights in adoption cases.

---

## Power P1 — Custody and parenting-time orders

**B1. What it can do to people.** Decide where a child lives, which parent decides on school, health care and religion, how often the other parent sees the child, and whether visits must be supervised. It can bar a parent from moving away with the child. Orders last until the child is an adult and can be reopened when circumstances change.

**B2. Who and where.** About 3,000 new custody cases a year [EX] in the county. Children are affected in every case and choose nothing; so are grandparents and new partners. In about 60% of cases at least one parent has no lawyer [EX].

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The state legislature granted the jurisdiction in the Family Code. It is a general grant to the court system, not a separate authorization of this power after hearing affected people | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | NONE EXISTS for the power. Individual orders end when the child turns 18 [EX] | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. The "best interest of the child" standard lists factors but no measurable condition | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Appeal of one order; conduct complaint about one judge (B5). NONE EXISTS for the whole power: the legislature's general power to alter or remove custody jurisdiction does not count, and no independent body has an existing procedure to end the power within a defined time | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Appeal or a motion to modify can correct an order going forward; judicial immunity bars compensation; lost time with a child is not compensated | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Case files, including evaluators' reports on mental health, are kept 25 years [EX] after the case closes. The custody judgment itself may be kept as a status register while the custody status lasts, with access limited to confirming it (2.D.12). The rest of the file is not a status register and is held past the 20-year [S1] ceiling from first collection | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | The Family Code factors are public; the court publishes self-help guides. Whether outcomes have changed over time is not published | compliance not demonstrated |
| Floors | See B6 (Part II) | Disparity by income, sex and disability not reviewed; whether relocation limits fit 2.D.16 not shown | compliance not demonstrated |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Evaluators advise; the judge decides and must state reasons. No sign of splitting or laundering | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Appeal to the state appeals court | one_case | the appeals court | independent | [EX] |
| 2 | Emergency stay of an order pending appeal | one_case | the appeals court | independent | [EX] |
| 3 | Complaint to the judicial conduct commission | one_case (discipline of one judge, not reversal of an order) | the commission | independent | [EX] |
| 4 | High court rule change on evaluators or procedure | one_practice | the state high court | partly_independent (it supervises the same court system) | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. The legislature can alter or remove the court's custody jurisdiction, but that is the general ability to pass a new law, which does not count. The scenario shows no sunset vote and no standing review body with power to end the power. Appeals, stays, and judicial-conduct proceedings provide meaningful protections for individual cases or practices, not suspension of the power as a whole. Any suspension or transfer of jurisdiction would need to preserve a minimum essential means of resolving custody disputes safely (3.C.5).

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | UNKNOWN — evaluators charge about 4,000 currency units [EX] and supervised visits cost about 60 per hour [EX]; parents who cannot pay may see a child less. No fee waiver for evaluators | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | partly — self-help centers explain forms; orders do not explain how to appeal; there is no appointed lawyer in custody cases | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — this power uses no force; enforcement by contempt is P2 | |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — see P2 | |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical treatment | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | yes — appeal to a separate court | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — some orders bar parents from posting about the case online, a limit set before anything is published; not reviewed | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — no outcome data by group are collected | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | not_applicable | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | yes — drug tests of a parent and home studies are ordered by the judge on a party's specific allegation, and the order states what is to be tested or visited [EX]. Whether evaluators' home visits go beyond the order is not reviewed | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | UNKNOWN — the court can bar a parent from moving away with the child (B1); about 120 relocation requests a year [EX] are decided after a hearing on the child's interests. That matches none of the grounds in 2.D.16 by its terms. Whether an order deciding where a child lives restricts the parent's movement under 2.D.16, or only allocates custody, is for independent interpretation (7.3) | [EX] |

**B7. Data.** Pleadings, evaluators' reports with mental-health and substance-use details, school and medical records. Files are confidential but kept 25 years [EX] after closing. No deletion record.

**B8. Dependencies and evasion.** Custody evaluators and parenting coordinators are private, appointed from a court list, and paid by the parents. Their methods are not standardized by rule.

**B9. Harms seen.**
- psychological, generational — allegation: children in long contested cases report lasting harm; the court collects no follow-up data.
- economic — allegation: parents spent savings on evaluators to keep contact.
- agency — adjudicated: the appeals court reversed 9 custody orders last year [EX] for failure to state findings on the statutory factors.

**B10. Decision inputs and oversight.** Statutory best-interest factors, evaluator reports, guardian reports, testimony. Factors are declared; how they are weighed is left to each judge. Appeals courts review a small share of orders.

---

## Power P2 — Contempt jail for unpaid support

**B1. What it can do to people.** Jail a parent who has not paid court-ordered child support. Civil contempt holds the parent until they pay a "purge" amount the judge sets. Criminal contempt imposes a fixed sentence for past willful non-payment.

**B2. Who and where.** About 250 parents a year [EX] are jailed for support contempt in the county. Most owe arrears to the other parent; some owe the state, which collects them to repay public assistance. The children receiving support are non-participants.

**B3. Authority basis.** `direct`. The judge orders; the Sheriff carries out the order.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. Contempt is an inherent power of courts, confirmed by statute | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Habeas petition and appeal in single cases | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS for a parent jailed who could not pay | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | A contempt order is a sanction against the parent, not an accountability record (2.D.14); it follows 2.D.12 and 2.D.6, and the parent may ask for its earlier deletion unless a hold applies; whether such a route exists is UNKNOWN. Jail records of the confinement record what the authority did and are accountability records, but the court clerk keeps them, not an independent custodian. Booking fingerprints go to the state database with no stated limit | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | The contempt statute is public; the number of jailings is not published | compliance not demonstrated |
| Floors | See B6 (Part II) | Civil contempt confines to coerce payment (2.D.3); interest grows on unpaid arrears (2.B.2); no appointed lawyer for a parent facing civil contempt jail (2.D.5) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | The enforcement agency, not the court, chooses whom to bring in; whether its choices act as a proxy is UNKNOWN | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Habeas petition for release | one_case | a different judge of the trial court or the appeals court | partly_independent (same court) / independent (appeals court) | [EX] |
| 2 | Appeal of the contempt order | one_case | the appeals court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Paying the purge amount ends one jailing, but paying or complying is not a stop path.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes, in part. The support itself is owed to the child's parent and falls due on schedule; 2.B.2 says that is not escalation. But the state adds interest on unpaid arrears at 8% a year [EX], and support keeps falling due while the parent is jailed and earning nothing. A motion to lower support applies only from the date it is filed | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — the notice of hearing is a legal form; there is no appointed lawyer in civil contempt; a simple ability-to-pay form exists but is not given out by default | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | UNKNOWN — force at arrest and in jail is the Sheriff's and is not recorded here | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest before a judicial officer within 48 hours [S1]; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | no for civil contempt; conditionally yes for criminal contempt. Civil contempt jail aims to compel payment; it is not (a) a threat, (b) custody for trial, (c) a sanction for past conduct, or (d) a brief stop. Where the parent cannot pay, it is confinement because of poverty. Criminal contempt can fit (c) if willful non-payment is proved with due process and the sentence is proportionate | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical treatment | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | no — a parent facing jail for civil contempt has no right to an appointed lawyer [EX]; one is appointed only for criminal contempt [EX]. Hearings are public. A national high court decision requires the judge to find the parent able to pay before civil contempt; in about 40% of jailings [EX] the file shows no written ability-to-pay finding | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — not reviewed; in the clerk's sample about 90% of jailed parents are fathers [EX] | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | not_applicable | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — jailing is recorded under Confinement; wage withholding belongs to the state enforcement agency and is not recorded here |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — jailing is recorded under Confinement; denial of a passport for arrears is a national agency's power, not recorded here |  |

**B7. Data.** Contempt orders, payment histories, booking records. Jail records of the confinement are accountability records and should be held for 10 years [S1] by a custodian chosen by an independent body (2.D.14). The contempt order is a sanction against the parent and follows 2.D.12 and 2.D.6 instead. Here the court clerk keeps both under the court's own schedule.

**B8. Dependencies and evasion.** The state enforcement agency decides whom to bring to court, using an automated list of cases with arrears over 3 months [EX]. The court does not see how the list is built.

**B9. Harms seen.**
- economic — admitted: the clerk's sample shows median arrears at jailing of 7,500 currency units [EX], about half of it interest [EX].
- agency, economic — allegation: parents lost jobs because of jail, which lowered later payments to the child.
- generational — allegation: children lost contact with the jailed parent.

**B10. Decision inputs and oversight.** Payment records from the enforcement agency; the judge's ability-to-pay finding. No outside body reviews contempt jailings as a group.

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.D.3(b) (48 hours), 2.D.12 (20 years), 2.D.14 (10 years) | | yes |

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

- Child support itself is not escalation. 2.B.2 says amounts owed to another person on their ordinary schedule are not barred; added interest and penalties caused by inability to pay are.
- Civil contempt jail fits none of the four grounds in 2.D.3: it coerces payment rather than sanctioning past conduct. Criminal contempt can fit 2.D.3(c) with due process (2.D.5) and proportion.
- Jailing a parent who cannot pay also fails 2.B.1: liberty is made conditional on paying money the parent does not have. It is not economic extraction as defined, because the support is owed to the other parent, not to the court.
- Records of the jailing (what the court and Sheriff did) are accountability records and belong in independent custody for 10 years [S1] (2.D.14), not on the court's own schedule. The contempt order, as a sanction against the parent, is not; it follows 2.D.12 and 2.D.6, and the parent may ask for its earlier deletion unless a hold applies.
- Custody orders are hard to reverse in effect even when the order is reversed on appeal: lost time with a child cannot be returned (3.D.1, 3.D.2). Stop paths here reach one case.
- Under 3.D.2 a temporary protective custody order can be containment if it is reversible by default, limited in time, confined to the danger, and reviewed by an independent decision-maker within a short fixed period. P1's orders are ordinary custody orders lasting until the child is an adult, so they are not containment; a permanent change of legal status never is. Under 2.D.12 the custody judgment may be kept as a status register while the status lasts, for confirming it only; evaluators' reports and the rest of the file stay under the 20-year [S1] ceiling.
- Stopping a particular court's custody power is not the same as ending society's ability to resolve custody disputes. The legislature's general power to remove or transfer jurisdiction is not a whole-power stop path; it would count only through an existing, usable procedure that must end the power within a defined time. None is shown, so P1 is NONE EXISTS and not conforming, even though appeals and emergency stays are real one-case protections. Any stop or transfer would need to keep a minimum essential function (3.C.5).
- Evasion is conforming for P1: delegation to evaluators is visible and the judge decides on stated reasons. Not every row is a gap.
- The Due process row asks about a lawyer whenever liberty is at stake. A parent facing civil contempt jail has no appointed lawyer, so P2 fails 2.D.5 on that ground as well as on missing ability-to-pay findings. P1's relocation orders raise a 2.D.16 question that the record logs for interpretation (7.3) rather than deciding.
