---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-STATE-BENEFITS-AGENCY
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
  name: "[STATE] Department of Workforce Benefits"
  legal_entity: "[STATE] Department of Workforce Benefits, an executive agency of [STATE]"
  related_entities: "[CLAIMS-SYSTEM VENDOR] (built and maintains the claims and fraud-flag system); [IDENTITY-VERIFICATION VENDOR] (face-match identity checks); [STATE] Department of Revenue (tax-refund intercept); the federal labor agency (funds administration and checks conformity with federal law)"
  type: government
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: NONE
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Unemployment-benefit eligibility"
    category: benefits_eligibility_or_allocation
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
      visibility: conforming
      floors: not_demonstrated
      evasion: not_applicable
  - power_id: P2
    short_name: "Automated fraud flags"
    category: scoring_ranking_or_classification
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
      evasion: not_conforming
  - power_id: P3
    short_name: "Overpayment recovery with penalties and refund intercept"
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
      evasion: not_demonstrated
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

> **Structural record.** People are referred to by role or title. This record describes structure, not guilt. Adjudicated or admitted facts are kept separate from allegations.

# [STATE] Department of Workforce Benefits — Registration

## PART A — The institution

A1. **What it is.** The state agency that decides who receives unemployment benefits, flags claims it suspects are fraudulent, and recovers money it says was overpaid. For people who have lost a job, its decisions decide whether rent and food are paid this month.

A2. **Legal basis.** The [STATE] Employment Security Act and agency rules, within the federal unemployment-insurance law that funds administration and requires states to pay benefits "when due".

A3. **Who controls it.** A director appointed by the Governor. The legislature sets benefit levels and penalties.

A4. **Related entities.** A vendor built and maintains the claims system, including the fraud-flag module (P2). A second vendor runs face-match identity checks. The Department of Revenue intercepts state tax refunds on the agency's request (P3). The federal labor agency funds administration and reviews conformity. Figures belong to the agency unless stated.

A5. **Adoption.** not_adopted. Findings are diagnostic (Force and Status).

A6. **Powers found.**
- P1 Unemployment-benefit eligibility, including weekly re-certification.
- P2 Automated fraud flags.
- P3 Overpayment recovery with penalties, interest, wage garnishment, and tax-refund intercept.
- Not recorded: employer tax rates; work-search audits.

---

## Power P1 — Unemployment-benefit eligibility

**B1. What it can do to people.** It decides whether a person who lost work receives weekly payments, and how much, and it stops payment when a weekly re-certification is missed or answered in a way the system reads as disqualifying.

**B2. Who and where.** About 180,000 [EX] new claims a year in [STATE], rising to 900,000 [EX] in a recession year. Households and landlords of claimants are affected without choosing to be.

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | Enacted by the legislature; no record of findings on the Core requirements | not conforming |
| Maximum term | Expires on a set date (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body (3.A.5) | NONE EXISTS. Federal timeliness measures (first payment within 21 [EX] days for 87% [EX] of claims) exist but are performance targets, not harm thresholds | not conforming |
| Stop paths | Tested paths, one held outside the institution (3.A.7, 3.C.1) | One-case appeals; nothing stops the power as a whole (B5) | not conforming |
| Ending plan | 3.A.9 | NONE EXISTS | not conforming |
| Remedy | Independent, funded correction and compensation (3.A.10) | Appeal to an independent appeals board; back pay on reversal; whether that reaches late fees and evictions caused by the delay: UNKNOWN | compliance not demonstrated |
| Data limits | Stated retention periods (2.D.12–2.D.14) | Claim files are retained for five years [EX] after the last payment under a published schedule, and scheduled deletions are logged [EX]. These are documented safeguards. The scenario does not establish whether continued retention is periodically re-justified, whether eligible claimants can request earlier deletion, or whether records documenting the agency's own decisions and their review are identified and handled separately where the accountability-record requirements apply. Full data-limits compliance is therefore not demonstrated | compliance not demonstrated |
| Visibility | 3.B.9 | The Act, rules, benefit formula, and appeal rights are published in plain language and in 6 [EX] languages; the Act shows plainly that the power has no expiry and no renewal step (that failure is recorded under Maximum term) | conforming |
| Floors | Part II | Payment delays during surges (B6) | compliance not demonstrated |
| Evasion | Part IV | No outsourcing of the eligibility decision itself | not applicable |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Appeal to an administrative law judge, then the appeals board | one_case | State appeals board | independent — separate agency | [EX] |
| 2 | Judicial review | one_case | State court | independent | [EX] |
| 3 | Federal conformity finding that a practice violates federal law, with funding at stake | one_practice | Federal labor agency | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS** under current law. (Stopping it would also cut off income; see 3.C.5.)

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | — | not_applicable — no ecological effect | — |
| Economic (2.B) | Essentials conditional on compliance? | UNKNOWN — in a recession year the median wait for a first payment reached 9 [EX] weeks; whether that pushed claimants below basic functioning was not measured | [EX] |
| Agency (2.C) | Told plainly? Report without forms? | yes — decisions state the reason and appeal deadline; a phone line takes reports without forms | [EX] |
| Force (2.D.1) | — | not_applicable | — |
| Confinement (2.D.3) | Only on the four permitted grounds? | not_applicable — the power detains no one | — |
| Emergency medical care (2.D.2) | — | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Challenge before someone independent? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — appeals board and court | [EX] |
| Expression (2.D.9) | — | no | — |
| Equal treatment (2.D.10) | Reviewed? | Federal civil-rights review of language access found gaps, since corrected (finding in a resolution agreement) | [EX] |
| Identification (2.D.11) | Compelled identification? | See P2 | — |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — eligibility rests on wage records and the claimant's answers; nothing is searched or seized |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Identity, wage history from employers, separation reason, weekly answers. Kept on a published schedule; deletions are logged by schedule. Not shown: periodic re-justification of continued retention, a route for eligible claimants to ask for earlier deletion, and separate handling of records of the agency's own decisions and their review (2.D.12, 2.D.14).

**B8. Dependencies and evasion.** The claims vendor runs the system; the eligibility rules are the agency's. Federal funding pays for administration, which makes the agency dependent on federal performance measures.

**B9. Harms seen.** Economic: delayed payments in surge years (admitted in the agency's own reports). Agency: weekly re-certification questions that a wrong click turns into a denial (allegation, raised in appeals).

**B10. Decision inputs and oversight.** Wage records, separation reason, weekly answers, and the P2 flag. Inputs other than P2 are declared. The federal labor agency and the state auditor review the program.

---

## Power P2 — Automated fraud flags

**B1. What it can do to people.** A module of the claims system compares claims with employer wage records and other data, flags claims as suspected fraud, freezes payment, and — in the period described in B9 — issued most fraud determinations without a person reviewing the individual file. A fraud determination brings penalties under P3 and removes the waiver that ordinary overpayments get.

**B2. Who and where.** About 18,000 [EX] flags a year. Over the automated period, about 11,000 [EX] fraud determinations were issued without individual review. People sharing a name, address, or employer with a flagged claim are affected without choosing to be.

**B3. Authority basis.** `direct`. The agency's own system makes or drives the decision. Built by a vendor, but the agency is responsible for it (1.3, 4.5).

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | 3.A.1, 3.A.2 | Procured as an upgrade to the claims system by the agency itself; no separate authorization of automated fraud decisions | not conforming |
| Maximum term | 3.E.1, 7.2 | NONE EXISTS; the vendor contract renews yearly | not conforming |
| Harm thresholds | 3.A.5 | NONE EXISTS. No error-rate limit on flags or determinations | not conforming |
| Stop paths | 3.A.7, 3.C.1 | One-practice and one-case paths only (B5); no tested stop of the whole power | not conforming |
| Ending plan | 3.A.9 | NONE EXISTS | not conforming |
| Remedy | 3.A.10 | Individual refunds after a review-body decision and settlement; no standing route for people wrongly flagged since | not conforming |
| Data limits | 2.D.12–2.D.14 | Flag history kept indefinitely; face-match images kept by the identity vendor for 7 [EX] years; NONE EXISTS for a limit on flag history | not conforming |
| Visibility | 3.B.9 | The flag rules and their weights are treated as confidential to prevent gaming | not conforming |
| Floors | Part II | Repeated due-process and escalation violations; biometric-only identity check with no non-biometric option (B6) | not conforming |
| Evasion | Part IV | Renamed and replaced after the review-body decision with substantially the same function (B8) | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Appeal of a fraud determination | one_case | Appeals board | independent | [EX] |
| 2 | Precedent decision barring determinations without individual review | one_practice | State administrative review body | independent | [EX] |
| 3 | Judicial review of a fraud determination | one_case | State court | independent | [EX] |
| 4 | Federal conformity finding | one_practice | Federal labor agency | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS** under current law. The precedent decision stopped one practice (determinations without review); flagging continued.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | — | not_applicable | — |
| Economic (2.B) | Escalating obligations? | yes — a fraud label adds the P3 penalty and interest and removes the waiver (2.B.2) | [EX] |
| Agency (2.C) | Told plainly? Usable without expertise? | no — the fraud notice cited rule numbers rather than the facts relied on, and the only way to contest the flag was a long online form with a 10 [EX]-day deadline and no phone or paper route (2.C.1, 2.C.2: protections must not depend on self-advocacy) | [EX] |
| Force (2.D.1) | — | not_applicable | — |
| Confinement (2.D.3) | Only on the four permitted grounds? | not_applicable — the power detains no one | — |
| Emergency medical care (2.D.2) | — | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Challenge before someone independent? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | no, during the automated period — the state's independent administrative review body held, in a precedent decision, that determinations without individual review or real notice violated due process (adjudicated) | [EX] |
| Expression (2.D.9) | — | no | — |
| Equal treatment (2.D.10) | Reviewed? | UNKNOWN — the auditor found flag rates about 1.7 [EX] times as high for claimants with limited English; no review of the cause exists | [EX] |
| Identification (2.D.11) | Compelled identification without cause? | yes — 2.D.11 permits verifying the identity of a person claiming an individual entitlement, by the least intrusive means that works, but a non-biometric way must always be offered and the information may not be used for any other purpose. Here every claimant must pass a face match to be paid, with no non-biometric route, and the images are kept by the vendor for 7 [EX] years as part of this power's data (B7), so no limit to the verification purpose is shown | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — the module matches claims against records the agency already holds; freezing payment is recorded under Due process |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**Pattern finding (3.D.5).** The same power crossed the due-process Floor (2.D.5) and the economic Floor (2.B.2) repeatedly, for thousands of people, over about 3 [EX] years; the due-process violation is adjudicated, and the escalation follows from the penalty rules in the Act. The renamed module still freezes payments without individual review; that later period is a recorded concern, not an established violation. Under 3.D.5 this is one structural finding, not a series of individual incidents. Refunds paid under the settlement are individual remedies and do not discharge it. The rule calls for independent review of the structure that allowed the pattern, and narrowing, restructuring, replacement, or ending of the power. Because the agency has not adopted the Core Requirements, this is recorded as a public finding; the framework itself compels nothing (Force and Status).

**B7. Data.** Claims, wage records, address and bank-account matches across claims, device data, and face-match images held by the identity vendor. The vendor's retention of images is set by its contract, not by the agency's schedule. Deletion records: NONE EXISTS.

**B8. Dependencies and evasion.** The fraud module is the vendor's product, configured by the agency. After the precedent decision, the module was replaced by the vendor's next version under a new name with human review added for determinations, but not for payment freezes. A change of name or vendor does not reset the record of the pattern (3.D.5, 1.3).

**B9. Harms seen.**
- Adjudicated: the review body's due-process decision on determinations without individual review.
- Settled without admission: a group settlement providing refunds and penalty reversals for people covered by the decision.
- Audit finding (not adjudicated): the state auditor reviewed a sample and found that a large share — about 2 in 5 [EX] — of automated fraud determinations lacked support in the file.
- Allegations: evictions, utility shutoffs, and damaged credit reported by claimants (economic, psychological).

**B10. Decision inputs and oversight.** Cross-matches, timing patterns, and device data. The inputs are not declared (5.3); outcomes such as the language disparity cannot be explained from public information. The state auditor reviewed once, after the harm.

---

## Power P3 — Overpayment recovery with penalties and refund intercept

**B1. What it can do to people.** It bills people for benefits it says were overpaid, adds a penalty and monthly interest when fraud was found, and collects by wage garnishment, by keeping future benefits, and by intercepting state tax refunds, without a court order.

**B2. Who and where.** About 25,000 [EX] overpayment accounts open in [STATE]. Family members who share a joint tax return lose refunds without choosing to be involved.

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | 3.A.1, 3.A.2 | Enacted by the legislature; no separate authorization with findings | not conforming |
| Maximum term | 3.E.1, 7.2 | NONE EXISTS; fraud debts can be collected for 10 [EX] years and renewed | not conforming |
| Harm thresholds | 3.A.5 | NONE EXISTS | not conforming |
| Stop paths | 3.A.7, 3.C.1 | One-case paths only (B5) | not conforming |
| Ending plan | 3.A.9 | NONE EXISTS | not conforming |
| Remedy | 3.A.10 | Refund on reversal; no interest paid back to the person; no route for losses caused by garnishment | not conforming |
| Data limits | 2.D.12–2.D.14 | Retention of closed collection accounts: UNKNOWN | compliance not demonstrated |
| Visibility | 3.B.9 | Penalty rate, interest rate, waiver rules, and collection methods are in the Act and published; the absence of any expiry is stated there too | conforming |
| Floors | Part II | Escalation and leverage (B6); wages and refunds seized without a judicial officer's approval (2.D.15) | not conforming |
| Evasion | Part IV | Refund intercept runs through the Department of Revenue; whether it re-checks the debt: UNKNOWN | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Waiver request for a non-fraud overpayment | one_case | The agency | not_independent | [EX] |
| 2 | Appeal of the overpayment determination | one_case | Appeals board | independent | [EX] |
| 3 | Judicial review | one_case | State court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS** under current law.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | — | not_applicable | — |
| Economic (2.B) | Escalating obligations? Path out? | yes — a fraud penalty of 100% [EX] of the overpayment plus 1% [EX] a month in interest grows while the person cannot pay (2.B.2). Ordinary overpayments have a waiver when repayment would cause hardship; fraud overpayments do not | [EX] |
| Agency (2.C) | Told plainly? | Bills state the amount and how to appeal; they do not explain the waiver | [EX] |
| Force (2.D.1) | — | not_applicable | — |
| Confinement (2.D.3) | Only on the four permitted grounds? | not_applicable — the power detains no one | — |
| Emergency medical care (2.D.2) | — | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Challenge before someone independent? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes for the determination; no for each garnishment or intercept | [EX] |
| Expression (2.D.9) | — | no | — |
| Equal treatment (2.D.10) | Reviewed? | UNKNOWN | — |
| Identification (2.D.11) | — | not_applicable | — |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | no — wages are garnished and state tax refunds intercepted by the agency's own order, without a court [EX]; a person can contest the underlying determination, but no judicial officer approves or reviews each seizure (see Due process) | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Debt balances, employer and bank details, tax-refund matches. Shared with the Department of Revenue for each intercept.

**B8. Dependencies and evasion.** The Department of Revenue intercepts refunds on the agency's certification, without its own review. As in any chain, both share responsibility (4.1).

**B9. Harms seen.** Economic: garnishment of wages and intercepted refunds on fraud debts later reversed (reversals ordered under the review-body decision for the automated period). Generational: joint-return refunds of spouses intercepted (allegation).

**B10. Decision inputs and oversight.** The overpayment amount and the fraud label from P2. A wrong P2 label passes straight into P3 penalties. No one audits P3 separately.

---

## PART C — Sources

This is a worked example. Figures are tagged [EX] and are illustrative; no real source is cited for them.

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it | Quote | Verified? |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.B.2; 2.C.2; 2.D.11; 3.D.5 | | yes |

---

## PART D — Honesty assertions

- [x] Every number has a source tag ([EX] for illustrative figures).
- [x] Nothing presented as real was invented; figures are marked illustrative.
- [x] No real institution is described.
- [x] People are referred to by role or title.
- [x] Adjudicated facts, settled matters, audit findings, and allegations are labelled separately.
- [x] Made in good faith, as a structural description, not an accusation.

Preparer: Bounded Power Framework examples set.

---

## Teaching notes (non-binding)

- 3.D.5 is not only about force. Repeated due-process and escalation failures by one automated power are a structural finding; refunds to individuals do not discharge it [S1].
- For a non-adopting agency, the 3.D.5 consequence (review, narrowing, restructuring, ending) is read as a public finding. Courts, the legislature, and the federal funder supply any operative consequence (Force and Status, 5.5).
- Renaming or replacing a module does not reset the pattern (3.D.5, 1.3). Automation is held to the same rules as people (1.3); the vendor's system is the agency's power (4.5).
- Powers chain: a wrong P2 label becomes a P3 penalty and removes the waiver. Each power is recorded separately, but the harm runs through both (3.A.1, 4.1).
- A contest route that only works for people who can read rule citations and finish a long online form in days fails the Agency Floor: protections must not depend on self-advocacy (2.C.2).
- Real partial answers exist and are shown: an independent appeals board, a published retention schedule, a federal conformity check. They stop cases or practices, not the power (3.A.7).
- Positive findings need the same evidence as negative ones. A published five-year [EX] schedule with logged deletions is a real safeguard, but it does not show re-justified retention, earlier deletion on request, or separate handling of accountability records, so P1's data limits are not demonstrated rather than conforming (2.D.12, 2.D.14, 7.6).
- Federal timeliness and improper-payment measures are performance targets, not harm thresholds set by an authorizing body (3.A.5).
- 2.D.11 allows an identity check on a person claiming an individual entitlement, but only by the least intrusive means that works, with a non-biometric way always offered, and with no other use of the information. A face match that every claimant must pass, with no alternative, still fails; offering a document check or in-person route, and keeping images out of the fraud system, would be needed to conform.
- Garnishing wages or intercepting a refund by an agency's own order is a seizure under 2.D.15. A right to contest the debt is not the judicial approval the rule requires for each seizure.
