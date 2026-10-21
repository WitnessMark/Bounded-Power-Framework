---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-PRETRIAL-RISK-TOOL
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
  name: "[RISK-TOOL VENDOR]"
  legal_entity: "[RISK-TOOL VENDOR], a private corporation registered in [STATE]"
  related_entities: "county pretrial services offices and courts that license the tool; [VALIDATION FIRM]"
  type: private_company
  country: "[COUNTRY]"
  region: NONE
  locality: NONE
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Pretrial risk score and release matrix"
    category: scoring_ranking_or_classification
    authority_basis: indirect_a_operationalized
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_demonstrated
      ending_plan: conforming
      remedy: not_conforming
      data_limits: not_demonstrated
      visibility: not_conforming
      floors: not_conforming
      evasion: not_demonstrated
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

> **Structural record.** Based on public sources and/or the preparer's own observation. People are referred to by role or title. This record describes structure, not guilt. Adjudicated or admitted facts are kept separate from allegations.

# [RISK-TOOL VENDOR] — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** A private software company that licenses a pretrial risk tool to county courts and pretrial services offices. For each arrested person, the tool produces a score predicting whether the person will miss a court date or be arrested again before trial, places the score in a band, and looks up a recommended release condition in a "release matrix" the vendor supplies. A pretrial officer gives the result to the judicial officer at the first appearance. The vendor makes no custody decision itself.

A2. **Legal basis.** Contract law and procurement. Each county signs a license. In some states a court rule or statute requires a validated risk tool at first appearance; it does not name a vendor. No national law regulates pretrial risk tools.

A3. **Who controls it.** The company's board and owners. Customers control their own use of the output.

A4. **Related entities.** About 40 county customers [EX] in several states. [VALIDATION FIRM] performs validation studies under contract with the vendor. All figures in this record are the vendor's unless stated.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — Pretrial risk score and release matrix, as operationalized by courts.
- Not recorded: a separate supervision-level product sold to probation offices.

---

## Power P1 — Pretrial risk score and release matrix

**B1. What it can do to people.** The vendor's output tells a judicial officer how risky a person is before that officer has heard from them. The tool computes a score from 0 to 100 [EX] for two outcomes, missing court and new arrest, and puts the person in one of five bands, A to E [EX]. The release matrix maps band and charge type to a recommendation: release on own recognizance, release with conditions, electronic monitoring, or "detention hearing recommended." The vendor cannot confine anyone. Its output can lead a judicial officer to set conditions or hold the person.

**B2. Who and where.** About 180,000 people a year [EX] in customer counties. Every person scored is a non-participant: they cannot decline to be scored, and most have not been convicted of anything.

**B3. Authority basis.** `indirect_a_operationalized`. Courts and pretrial offices build the output into a decision that binds the person.
- Who relies on it: county pretrial services prepare the report; judicial officers decide release.
- Evidence tier: in 12 counties [EX], a local court rule requires the matrix recommendation to be presented and requires the officer to state reasons on the record for departing from it. This is tier 2, contractual dependency, plus tier 5, shared decision criteria. Tiers 1–5 support a finding.
- Recorded result: in the vendor's own customer report, judicial officers followed the matrix recommendation in about 85% of cases [EX].
- In counties where the score is only one paper among many and no rule requires it, the only evidence is that officers often reach the same result as the score: residual correlation (tier 7). That supports only a recorded concern there.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | Each county approves a purchase contract. No body that heard affected people authorized the scoring power. The state court rule mandates "a validated tool", not this one | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | County licenses run 3 years [EX] and renew automatically unless cancelled. The scoring model has no end date | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | The vendor sets its own accuracy target in its validation plan. No authorizing body sets a threshold, and the only measure is the vendor's own study | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Each county can cancel; a defense lawyer can contest one score; state court rules and federal litigation can restrict particular deployments. None is shown to stop the scoring power across all customer jurisdictions; whether any other whole-product mechanism exists is not assessed | compliance not demonstrated |
| Ending plan | A documented way to end the power safely (3.A.9) | The contract requires the vendor to deliver all case data and the scoring formula to the county within 60 days [EX] of termination, then delete its copies. Courts can return to unaided decisions the next day | conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS. A person held after a wrong score has no claim against the vendor; the contract makes the county responsible for use | not conforming |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | The vendor keeps de-identified case data "for model improvement" with no stated period; whether the data can be re-linked is UNKNOWN | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | The list of 14 inputs [EX] is published. Weights, band cut-points and the matrix are trade secrets shared only with counties under a non-disclosure agreement. The person scored sees only the band | not conforming |
| Floors | See B6 (Part II) | Disparity not independently reviewed (2.D.10); used as a ground for custody in matrix counties (2.D.3); electronic monitoring recommended by band (2.D.16); scored interview answers taken without a warning that the person may decline (2.D.5) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Several inputs may act as proxies (B8); a proxy finding needs tier 5 or stronger evidence, which no independent study has yet produced | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | County cancels its license at renewal | one_practice (use in one county) | the county court administrator or board | independent of the vendor | [EX] |
| 2 | Defense counsel contests the score or the inputs at the detention hearing | one_case | the judicial officer | independent | [EX] |
| 3 | State high court amends its rule to bar a tool or a matrix | one_practice (all counties in one state) | the state high court | independent | [EX] |
| 4 | Federal civil-rights lawsuit against a county's use of the matrix | one_practice | a federal court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **UNKNOWN**. County cancellation, judicial challenges, state court rules, and federal litigation can restrict or terminate particular deployments of the pretrial risk tool. None is demonstrated here to stop the vendor's scoring power across all customer jurisdictions. The vendor could withdraw the product, but its own decision does not qualify as an independent stop path. The scenario does not assess whether any independent body, such as a regulator, has an existing procedure that can end the product across all jurisdictions within a defined time. The general ability of a legislature to pass a new law banning such tools would not count.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | UNKNOWN — the matrix can recommend electronic monitoring, which some counties charge at 12 currency units a day [EX]; the vendor does not set that fee | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — the person is interviewed for some inputs without being told the answers will be scored; the report shows a band letter with no explanation | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — the vendor uses no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | no, in matrix counties. Ground (b) allows continued custody only on the officer's own finding from specific facts about the person. A prediction, including a risk score, never alone justifies confinement. Where a court rule makes a "detention hearing recommended" result the default that the officer must argue against, the score is functioning as a ground for custody | [EX] |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — the tool gives no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | partly — the person can contest at the hearing, with appointed counsel in most customer counties [EX], but cannot see the weights or cut-points; "undisclosed enforcement criteria are prohibited" (2.D.5). Interview answers that feed the score are taken before counsel is appointed, without telling the person they may decline [EX] (see Agency) | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | yes, not independently reviewed — the vendor's study shows the false "high band" rate is about 1.6 times higher for one racial group [EX]. The study was done by a firm the vendor pays | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | not_applicable — scoring happens after an arrest | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — the tool scores records it receives from counties (B7); it searches no person, home or device |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | no, in matrix counties — the matrix recommends electronic monitoring by band [EX], so a restriction on where an unconvicted person may go rests on a prediction rather than the officer's findings from specific facts. 2.D.16 permits such a restriction only under 2.D.3, and under 2.D.3 a prediction never alone suffices | [EX] |

**B7. Data.** The vendor receives arrest charge, criminal history, past court appearances, age, and interview answers about housing and work. It is personal information collected by receipt (Definitions: Collect). Case data are kept by counties under their records rules and by the vendor, de-identified, with no stated period. No deletion record (7.6).

**B8. Dependencies and evasion.** Inputs come from state criminal-history records and county court data. Possible proxies (4.7):
- Prior arrests, counted whether or not they led to a charge, carry past enforcement patterns into the score.
- Past failures to appear correlate with lack of transport, unstable housing and inflexible work.
- "Months at current address" and "employed" correlate with poverty.

Each is a candidate proxy. Under the Causation Ladder, a proxy finding needs tier 5 or stronger (tiers 1–5). No independent study has tested these inputs, so the evidence stays at tier 7 and supports only a recorded concern and a request for evidence. Responsibility is shared with every county that uses the output (4.1): the vendor cannot disclaim it because it does not make the final decision.

**B9. Harms seen.**
- agency, psychological — allegation: defendants held for days in "detention hearing recommended" cases before the hearing.
- economic — allegation: people lost jobs while held in band E [EX] cases later dismissed.
- informational — admitted: the vendor's customer notice reports a coding error that placed about 240 people [EX] one band too high over 7 weeks [EX]; scores were corrected, custody decisions were not reviewed.

**B10. Decision inputs and oversight.** Inputs are declared; weights and cut-points are not (5.3). Validation is performed by [VALIDATION FIRM], paid by the vendor; it is not independent (5.1). Counties may commission their own study but rarely do. No public body audits the tool across customers.

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.D.3(b), Causation Ladder | | yes |

---

## PART D — Honesty assertions

- [x] Every number has a source tag. In this worked example, institutional figures carry [EX] and are illustrative.
- [x] Nothing was invented as fact about a real institution. This is a composite example; it does not describe any one product.
- [x] Public sources and first-hand observation only. Nothing private, leaked, or speculative.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] I made this record in good faith, as a structural description, not an accusation.

Preparer: BPF examples working group (worked example).

---

## Teaching notes (non-binding)

- A vendor with no power to confine still holds authority when its output is a structured determinant of a binding decision (Definitions: Authority (a); 4.3). The evidence tier must be stated, and it differs by county.
- 2.D.3 says a prediction never alone justifies confinement. Custody under 2.D.3(b) rests on the officer's findings from specific facts about the person, within the 48-hour [S1] and 30-day [S1] limits. A matrix that makes "detention" the default shifts that finding onto the score.
- Candidate proxies (4.7) are recorded as concerns until evidence at tier 5 or stronger (tiers 1–5) exists (Causation Ladder). Tier 1 is the strongest. A disparity review under 2.D.10 needs no tier and is required now.
- A validation study paid for by the vendor is not independent evaluation (5.1, Definitions: Independent).
- Secret weights and cut-points are undeclared inputs (5.3) and undisclosed criteria under 2.D.5.
- Ending plans can be conforming even when nothing else is: a scoring tool is easy to stop using if the contract hands back data and formula (3.A.9).
- Cancellation by one customer is a real stop path, but it reaches only one practice. Shared responsibility (4.1) means each county is also answerable for its own use.
- Stopping one county's use is not stopping the vendor's power. The absence of a single nationwide regulator does not prove that nothing can stop the product as a whole; the vendor's voluntary withdrawal is not independent, and other mechanisms are not yet assessed, so the finding is not demonstrated rather than not conforming (3.A.7, 3.C.1). Courts remain responsible for their custody decisions while the vendor remains accountable for the scoring power its product exercises indirectly.
- Electronic monitoring restricts movement, and before trial 2.D.16 allows that only under 2.D.3, where a prediction never alone suffices. A matrix that recommends monitoring by band fails the same way a detention default does. Interviewing a person for scored inputs before counsel, without saying they may decline, engages the silence protection in 2.D.5.
