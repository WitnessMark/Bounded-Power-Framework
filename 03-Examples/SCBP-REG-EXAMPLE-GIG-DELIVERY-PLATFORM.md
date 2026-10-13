---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-GIG-DELIVERY-PLATFORM
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
  name: "[DELIVERY APP]"
  legal_entity: "[DELIVERY APP INC.]"
  related_entities: "[BACKGROUND-CHECK VENDOR] (courier screening); [IDENTITY-CHECK VENDOR] (selfie checks at login)"
  type: private_company
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: "[CITY]"
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Algorithmic deactivation of couriers"
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
      remedy: not_demonstrated
      data_limits: not_demonstrated
      visibility: not_conforming
      floors: not_conforming
      evasion: not_demonstrated
  - power_id: P2
    short_name: "Setting courier pay per offer"
    category: rules_standards_or_prices
    authority_basis: indirect_b_directive_control
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: not_conforming
      remedy: not_demonstrated
      data_limits: not_applicable
      visibility: not_conforming
      floors: not_conforming
      evasion: not_demonstrated
  - power_id: P3
    short_name: "GPS tracking, identity checks and ratings"
    category: inspection_search_or_surveillance
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
      visibility: not_conforming
      floors: not_conforming
      evasion: conforming
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [DELIVERY APP] — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** A private company that runs an app connecting restaurants and shops, customers, and couriers who deliver orders by car, bike or scooter. The company treats couriers as independent contractors, not employees. Its software offers each delivery to a courier at a price it sets, tracks the courier during the job, collects customer ratings, and can remove a courier from the app. For many couriers the app is their main or only income.

A2. **Legal basis.** Incorporated under [STATE] corporate law. Its power over couriers comes from a contractor agreement couriers accept in the app, which the company can change on notice. In [CITY], a local ordinance on app-based work sets a minimum pay standard and gives couriers notice and an outside challenge to deactivation. Elsewhere in [STATE], no such law applies.

A3. **Who controls it.** A board elected by shareholders. Pay and deactivation rules are set by management and run by software.

A4. **Related entities.**
- [BACKGROUND-CHECK VENDOR] screens couriers at sign-up and every year [EX].
- [IDENTITY-CHECK VENDOR] runs the selfie check under P3.
- Figures in this record are for [CITY] unless stated.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — Algorithmic deactivation of couriers (employment_or_discipline, direct).
- P2 — Setting courier pay per offer (rules_standards_or_prices, indirect_b).
- P3 — GPS tracking, identity checks and ratings (inspection_search_or_surveillance, direct).
- Not recorded: fees and menu-price rules for restaurants; customer account bans.

---

## PART B — One section per power

## Power P1 — Algorithmic deactivation of couriers

**B1. What it can do to people.** It can remove a courier from the app, temporarily or permanently, which ends that courier's income from it at once. Triggers include a customer rating average below a cut-off, too many late or cancelled deliveries, a failed selfie check, a background-check result, or a fraud flag. Most deactivations are made by software; a person reviews some of them afterwards.

**B2. Who and where.** About 40,000 [EX] active couriers in [CITY]; about 4,000 [EX] deactivated per year. Many are immigrants or have few other job options. Non-participants: the courier's household, which loses the income.

**B3. Authority basis.** `direct`. The company itself removes the courier; no other party's decision is involved [S1]. Calling couriers contractors does not change what the power does (1.3).

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. The [CITY] ordinance limits how deactivation is done; it does not authorize the power. | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. Wrongful-deactivation rates come only from the company's own reviews. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | One-case paths; see B5 | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | [CITY]: arbitration with reinstatement and back pay, arbitrator paid by the company. Elsewhere: individual arbitration under the contractor agreement. Financial assurance UNKNOWN. | compliance not demonstrated |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Deactivation records kept for 3 years [EX]; custody by the company only. Deletion record UNKNOWN. A deactivation entry is a sanction listing against the courier, not an accountability record; it follows 2.D.12 and 2.D.6, and the courier may ask for its earlier deletion unless a hold applies (2.D.14). The 3-year period [EX] is stated but not justified, and whether couriers can ask for deletion is UNKNOWN. | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | [CITY] ordinance requires a published deactivation policy. The rating cut-off and fraud rules are not published. | not conforming |
| Floors | See B6 (Part II) | See B6 | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Contractor classification may relabel employer discipline (1.3, 4.1); a [STATE] labor agency finding that couriers are employees is under appeal [EX]. Customer ratings may act as a proxy (B9). | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Challenge to a deactivation before an arbitrator under the [CITY] ordinance | one_case | an arbitrator approved by the [CITY] labor agency | partly_independent | [EX] |
| 2 | [CITY] labor agency enforcement order against a deactivation practice | one_practice (in [CITY]) | [CITY] labor agency | independent | [EX] |
| 3 | Internal appeal | one_case | the company's courier support team | not_independent | [EX] |
| 4 | Employment-law suit or agency action if couriers are found to be employees | one_practice | a [STATE] court; [STATE] labor agency | independent | [EX] |

Path 1 is partly independent: the city approves the arbitrators, but the company pays the arbitrator's fee [EX]. Path 4 depends on a classification ruling that is still under appeal.

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. In [CITY] the power is limited case by case; nowhere can it be stopped as a whole.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway of note | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes — income needed for subsistence ends at once; couriers who rented vehicles for the work keep owing the rent | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | partly — in [CITY], a notice with a reason category is required within 1 day [EX]; elsewhere a generic message | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | partly — in [CITY] (path 1); elsewhere no | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — couriers who organized a strike report deactivations afterwards; allegation only | |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — see B9; no independent disparity review | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | recorded under P3 | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — deactivation searches nothing itself; the tracking it relies on is recorded under P3 |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Ratings, delivery times, cancellations, selfie-check results, background reports, fraud flags. A deactivation entry is a sanction listing against a courier, not an accountability record: it follows 2.D.12 and 2.D.6, needs a justified retention period, and the courier may ask for its earlier deletion unless a hold applies (2.D.14). The company's records of its own decisions (rule applied, inputs, reviewer if any) are accountability records; they are held only by the company, not in independent custody.

**B8. Dependencies and evasion.** [BACKGROUND-CHECK VENDOR] results can trigger deactivation automatically. The vendor is a consumer reporting agency, so the federal fair credit reporting law's adverse-action notice applies to that path only.

**B9. Harms seen.**
- economic: couriers deactivated and later reinstated by arbitrators, about 40% [EX] of challenged cases in [CITY]'s first year; adjudicated in those arbitrations.
- economic, agency: deactivation after failed selfie checks in poor light; allegation in courier complaints [EX].
- economic (equal treatment): customer ratings lower for some couriers by race or accent; academic studies show a statistical pattern (Causation Ladder tier 6) [S1]. That supports a recorded concern and a request for evidence, not a proxy finding (4.7). A disparity review under 2.D.10 needs no tier and has not been done.

**B10. Decision inputs and oversight.** Rating average with a cut-off of 4.5 out of 5 [EX], completion rate, lateness, selfie result, fraud score. The deactivation policy is published in [CITY]; the fraud score is not (5.3). The [CITY] labor agency can audit records; nobody audits the software (5.1).

---

## Power P2 — Setting courier pay per offer

**B1. What it can do to people.** For each delivery, software decides the pay offered to a courier, shows it for a few seconds, and offers it to someone else if refused. Pay varies by courier, time and place by rules the courier cannot see. Couriers who decline many offers are shown fewer or worse ones. The result is that the company decides, offer by offer, what an hour of a courier's work is worth.

**B2. Who and where.** About 40,000 [EX] couriers in [CITY] and more across [STATE]. Couriers who work for several apps at once are affected too, because the apps' rates set the going rate.

**B3. Authority basis.** `indirect_b_directive_control`. The company orders no one to work at any rate. But at its scale, its pay offers, offer-acceptance metrics and hidden incentives channel when, where and for how much couriers work, as an order would (Authority definition, limb (b)) [S1].
- No Causation Ladder tier is needed: the finding rests on the practical effect of the company's own outputs [S1].
- An arguable alternative: for couriers who work only on this app, pay setting could be recorded as `direct`. The basis is a structural determination that can be contested before an independent body. This record uses indirect_b because the effect reaches the local delivery labor market, not only this app's couriers.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | [CITY] minimum pay standard: a per-hour floor [EX] for time spent on deliveries, set by the [CITY] labor agency after public hearings. It covers one harm only, and compliance is measured from the company's own reported data. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | See B5 | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | [CITY] labor agency can order back pay. Elsewhere: individual arbitration. Financial assurance UNKNOWN. | compliance not demonstrated |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Pay setting uses data collected under P3; assessed there. | not applicable |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | In [CITY], each offer must show pay, distance and tip before acceptance. How pay is calculated is not disclosed. | not conforming |
| Floors | See B6 (Part II) | See B6 | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | After the [CITY] standard began, offers outside [CITY] limits fell [EX]; whether this shifts cost to evade the standard is not shown. | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Enforcement of the [CITY] minimum pay standard | one_practice (pay below the floor, in [CITY]) | [CITY] labor agency | independent | [EX] |
| 2 | Wage claim, if couriers are found to be employees | one_case | [STATE] labor agency | independent | [EX] |

Not counted: declining an offer. That is self-help, not a stop path (form B5). Declining also tends to lower future offers, which bears on the Economic and Agency Floors (2.B.3, 2.C.2), not on stop paths.

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway of note | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes — income is conditioned on accepting offers; acceptance-rate penalties make refusal costly. Outside [CITY], pay after vehicle costs falls below the [STATE] minimum wage on about a third [EX] of hours. | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — pay rules are not explained; couriers can leave, but those who depend on the income cannot in practice | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | partly — in [CITY], through the labor agency | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | no evidence found for pay setting | |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — individualized pay could differ by group; no data published and no review | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | not_applicable — recorded under P3 | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — pay setting uses P3 data; collection is recorded under P3 |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | no — offers vary by zone, but a courier may log in and work anywhere in [CITY] [EX] | [EX] |

**B7. Data.** Uses P3 data (location, acceptance history, ratings). No separate collection.

**B8. Dependencies and evasion.** Restaurants and customers fund pay through fees; the company sets both sides. How customer tips interact with offered pay is not disclosed.

**B9. Harms seen.**
- economic: pay after costs below the minimum wage outside [CITY]; estimate in academic research, not adjudicated [EX].
- agency: couriers unable to predict earnings; allegation in courier surveys.

**B10. Decision inputs and oversight.** Distance, time, demand, courier acceptance history and unpublished incentives. Inputs are not declared (5.3). The [CITY] labor agency receives monthly data [EX] but cannot see the pricing model (5.1).

---

## Power P3 — GPS tracking, identity checks and ratings

**B1. What it can do to people.** While a courier is logged in, the app records location every few seconds, speed, phone movement and time at each stop. It asks for a selfie at random times to match the courier to the account photo. It collects a customer rating after each delivery. All of this feeds P1 and P2.

**B2. Who and where.** All active couriers: about 40,000 [EX] in [CITY]. Customers' addresses and delivery details are recorded too.

**B3. Authority basis.** `direct`. The company itself watches the courier through its app [S1].

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. No exposure size set as a stop condition (3.C.2). | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | See B5 | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS outside a data-breach suit | not conforming |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Location kept "as long as needed for business purposes"; face templates kept for the life of the account plus 3 years [EX]; no deletion record. | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Privacy notice lists data types; uses in pay and deactivation are not explained. | not conforming |
| Floors | See B6 (Part II) | See B6 | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Tracking is run in-house; the notice states courier location is not sold, and no sale or routing around limits was found. | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Suit under the [STATE] biometric privacy law over face templates | one_practice | a [STATE] court | independent | [EX] |

Not counted: logging off. It stops tracking only by giving up work, which is self-help, not a stop path (form B5).

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes — income is conditioned on continuous tracking and face checks | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — not told how tracking data is used against them | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | no for tracking itself | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — location data could show attendance at a courier meeting; no evidence of use | |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — face matching fails more often for some groups [EX]; not reviewed | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | yes, in part — confirming that the person working is the account holder falls under the claimed-entitlement case of 2.D.11 (an account and its payments). That case permits the least intrusive means that works, requires a non-biometric way always to be offered, and bars any other use. The check is a face match with no non-biometric way offered [EX]; random repeated checks go beyond the least intrusive means; and face-match results also feed pay setting (B10), another use | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | no — while a courier is logged in, the app reads the phone's location, motion sensors and camera [EX]: a search of the courier's own device, with no individualized cause and no independent approval. Accepting the app's terms is a condition of earning, so it is not consent freely given (2.D.15), and logging off is giving up work (B5) | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | no — the app records where couriers go but bars them from no place; delivery zones decide which offers a courier sees [EX] | [EX] |

**B7. Data.** Location trails, speed, phone sensors, face templates (biometric, 2.D.13), ratings, customer addresses. Face templates have no stated deletion date within the 10-year biometric limit [S1]. No deletion record (7.6).

**B8. Dependencies and evasion.** [IDENTITY-CHECK VENDOR] holds face templates on the company's behalf and is treated as part of the company (4.5). No sale of courier location found.

**B9. Harms seen.**
- informational: face templates collected without written consent; [STATE] biometric privacy suit, settled without admission [EX].
- psychological, agency: constant monitoring and speed alerts; allegation in courier surveys.

**B10. Decision inputs and oversight.** Location, timing and face-match results drive P1 and P2. Not declared in plain terms (5.3). No outside audit (5.1).

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | Definitions (Authority, Causation Ladder); 1.3; 2.D.3; 2.D.13; 2.D.14; 4.7 | | yes |

All other figures are illustrative and tagged [EX]. No real institution was used as a source.

---

## PART D — Honesty assertions

- [x] Every number has a source tag.
- [x] Nothing was invented. Where I could not find something, I wrote UNKNOWN. Where something is absent, I wrote NONE EXISTS.
- [x] Public sources and first-hand observation only. Nothing private, leaked, or speculative.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] I made this record in good faith, as a structural description, not an accusation.

Preparer: BPF examples working group. Worked example; all figures illustrative.

---

## Teaching notes (non-binding)

- Discipline by software is still discipline. Calling workers contractors does not change the power, so deactivation is recorded as direct employment_or_discipline (1.3, 3.A.1).
- Pay setting shows the boundary between direct and indirect_b. The record uses indirect_b for the market-wide effect, notes the direct reading, and says the basis can be contested (Authority definition (b); 4.3).
- A city pay floor set after public hearings is a real threshold, but an incomplete one. It covers one harm and is measured on the company's own data, which 3.A.5 does not allow.
- An arbitrator approved by the city but paid by the company is partly independent (Definitions: Independent; 3.A.7).
- Customer-rating bias at tier 6 supports only a recorded concern under 4.7. A disparity review under 2.D.10 needs no tier and is still owed (Definitions: Causation Ladder).
- Self-help is not a stop path. Declining an offer or logging off is giving up, not stopping the power; and because declining lowers future offers, it is recorded as leverage over income (2.B.3, 2.C.2), not as a penalty on a stop signal.
- Face templates are biometric data and must have a stated deletion date within the 10-year limit [S1]. A vendor holding them is part of the company (2.D.13, 4.5).
- Verifying that a courier is the account holder is a claimed-entitlement check under 2.D.11. It must use the least intrusive means, always offer a non-biometric way, and serve no other use. A face-only check at random times, whose results also feed pay, fails all three.
- Rule 2.D.14: a deactivation entry is a sanction listing, not an accountability record. It follows 2.D.12 and 2.D.6, with a justified retention period and the courier's right to ask for earlier deletion, so the 10-year [S1] custody rule does not lengthen how long a sanction follows a courier. The company's records of how it decided remain accountability records.
- Continuous reading of a courier's own phone is a search of a device under 2.D.15. Consent built into the terms of earning a living is not freely given, so it cannot stand in for individualized cause.
