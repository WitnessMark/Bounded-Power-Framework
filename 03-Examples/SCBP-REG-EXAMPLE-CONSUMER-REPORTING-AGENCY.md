---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-CONSUMER-REPORTING-AGENCY
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
  name: "[NATIONAL CONSUMER REPORTING AGENCY]"
  legal_entity: "[CRA PARENT CORPORATION]"
  related_entities: "[SCORE-MODEL VENDOR]; [COURT-RECORDS AGGREGATOR]; the agency's [RENTAL SCREENING DIVISION]"
  type: private_company
  country: "[COUNTRY]"
  region: NONE
  locality: NONE
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Credit file and score used in lending"
    category: scoring_ranking_or_classification
    authority_basis: indirect_a_operationalized
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_demonstrated
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: not_conforming
      remedy: not_demonstrated
      data_limits: not_applicable
      visibility: not_conforming
      floors: not_conforming
      evasion: not_demonstrated
  - power_id: P2
    short_name: "Tenant-screening report and recommendation"
    category: scoring_ranking_or_classification
    authority_basis: indirect_a_operationalized
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_demonstrated
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: not_conforming
      remedy: not_demonstrated
      data_limits: not_conforming
      visibility: not_conforming
      floors: not_conforming
      evasion: not_conforming
  - power_id: P3
    short_name: "Compiling and keeping consumer files"
    category: data_collection_or_records
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_demonstrated
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: not_conforming
      remedy: not_demonstrated
      data_limits: not_conforming
      visibility: not_conforming
      floors: not_conforming
      evasion: not_demonstrated
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [NATIONAL CONSUMER REPORTING AGENCY] — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** A private company that gathers payment, debt, court and address information about almost every adult in [COUNTRY], keeps it in a file per person, and sells reports and scores built from those files. Lenders, landlords, insurers and some employers buy the reports and build them into their decisions. The company does not lend, rent or hire. It decides what goes into the file, how long it stays, and what score or recommendation comes out.

A2. **Legal basis.** Incorporated under [STATE] corporate law. It operates as a consumer reporting agency under the federal fair credit reporting law, which sets permitted purposes, dispute duties, and reporting periods for most negative items. The federal consumer financial regulator and the federal consumer protection agency enforce that law; state attorneys general share enforcement. No body grants it a licence to operate or sets an end date.

A3. **Who controls it.** A board elected by shareholders. Day-to-day decisions on file contents, scoring and products are made by management.

A4. **Related entities.** [SCORE-MODEL VENDOR] licenses the main score model the agency runs on its files; figures about score use describe the agency's sale of that score. [COURT-RECORDS AGGREGATOR] supplies eviction filings and criminal records to the [RENTAL SCREENING DIVISION]; figures about eviction records belong to the division's product. About 10,000 [EX] furnishers (banks, card issuers, collectors, some landlords and utilities) send monthly account data.

A5. **Adoption.** not_adopted. Like nearly every institution of this kind, it has not adopted the Core Requirements.

A6. **Powers found.**
- P1 — Credit file and score used in lending (scoring, indirect_a).
- P2 — Tenant-screening report and accept/decline recommendation (scoring, indirect_a), run by a product division.
- P3 — Compiling and keeping consumer files (data collection, direct).
- Not recorded: pre-screened marketing lists sold to lenders; employment background reports; identity-verification scores.

---

## PART B — One section per power

## Power P1 — Credit file and score used in lending

**B1. What it can do to people.** It produces a credit report and a three-digit score for a named person on request from a lender. Lenders set score cut-offs: below the cut-off the application is declined automatically or priced higher. The agency cannot itself deny a loan, but its score decides whether a person is offered credit, at what price, and whether a person can rent a car, open some utility accounts, or get some insurance at standard rates.

**B2. Who and where.** Adults in [COUNTRY] with a file: about 180 million [EX]. Nobody chooses to be included; a file opens when any furnisher first reports an account. Non-participants include people with no file at all ("credit invisible"), who are scored as unscorable and face the same declines.

**B3. Authority basis.** `indirect_a_operationalized`. The agency issues no binding decision. Lenders rely on its score as a structured determinant of a binding decision (Authority definition, limb (a); 4.3(a)) [S1].
- Who relies on it: card issuers, auto lenders, mortgage lenders, and the secondary-market buyers whose purchase guidelines require a minimum score from a consumer reporting agency.
- Causation Ladder: tier 2, contractual dependency. Lenders' subscriber agreements and loan-program guidelines oblige them to pull and apply a score at a stated cut-off [S1]. Tier 2 is stronger than the tier 5 needed for a finding. It is not tier 1, because the agency neither owns the lenders nor directs them; the binding guideline belongs to the loan buyer.
- Material cost: a person cannot refuse to be scored and still obtain mainstream credit.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | Existing safeguards: the federal fair credit reporting law, enforcement by federal and state regulators, and court remedies. They regulate conduct. As described here they are not an independent, affected-person-informed authorization of the scoring power for a fixed term. A qualifying authorization: UNKNOWN | compliance not demonstrated |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS. Open-ended. Broad reach means a 2-year limit would apply [S1]. | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. Error and dispute counts exist only in the agency's own reports. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Independent holders exist (regulator, courts) but each reaches one practice or one case; none is tested; see B5. | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS publicly. | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Federal private right of action with damages and fee-shifting; regulator complaint portal; state attorneys general. Financial assurance: UNKNOWN. | compliance not demonstrated |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | The score is computed at request and not kept as a separate record [EX]; the underlying file is assessed under P3. | not applicable |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Score factors are published only as broad categories with approximate weights [EX], so decision inputs are not declared (5.3). That the power has no expiry, renewal, or whole-power stop is knowable from the federal law; that failure is recorded under Maximum term and Stop paths. | not conforming |
| Floors | See B6 (Part II) | See B6: equal-treatment review and entrapment gaps. | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Proxy concern recorded (B9); evidence is tier 7 only. | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Enforcement order or consent order under the federal fair credit reporting law | one_practice | federal consumer financial regulator | independent | [EX] |
| 2 | Class action or state attorney general suit seeking an injunction | one_practice | a federal or state court | independent | [EX] |
| 3 | Individual suit for an inaccurate item | one_case | a court | independent | [EX] |
| 4 | Consumer dispute, which the agency must investigate within about 30 days [EX] | one_case | the agency's dispute unit | not_independent | [EX] |

A security freeze blocks new reports on one person's file, but it works only by giving up new credit. It is not counted as a stop path.

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Under current law no body can stop the scoring of a population; only a new law could.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — data processing with no ecological pathway of note | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes — a low score raises the price of credit, so people who cannot pay pay more. A paid collection stays on the file for up to 7 years [EX]. | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — notice arrives only when a lender sends an adverse-action notice; disputes require identifying the item; no exit | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | yes, through courts, slowly; the first-line dispute is decided by the agency itself | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | no evidence found | |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN for the agency's own model; published studies show score gaps by race of about 50 points [EX]. No independent review within 90 days [S1] is required or done. | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | no — identity matching is used to build files, not to compel identification | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — the agency compiles records furnished by lenders; it searches no person, home or device |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

Structural entrapment (2.D.6): a file follows a person for life with no periodic justification of its existence.

**B7. Data.** Inputs come from the file kept under P3. The score request itself is logged as an inquiry and shown on the file for 2 years [EX].

**B8. Dependencies and evasion.** The score model is licensed from [SCORE-MODEL VENDOR]; the agency cannot publish its internals. Under 4.1 both share responsibility. A handful of agencies of this kind exchange data formats through an industry standards body; a finding that they form one authority system (4.2) would need tier 5 evidence, which this example does not have.

**B9. Harms seen.**
- economic, agency: a regulator consent order found that the agency's dispute process failed to correct errors; settled without admission [EX].
- informational: mixed files (two people's data merged) leading to wrongful declines; adjudicated in individual suits [EX].
- non_participant: people with no file are declined for lack of data; allegation in advocacy research [EX].
- economic (equal treatment): disparity in scores by race; allegation or estimate, not adjudicated against this agency.

**B10. Decision inputs and oversight.** Payment history, balances relative to limits, age of accounts, recent inquiries, collections and public records. Categories are published; exact features and weights are not (5.3). The federal regulator supervises; no outside party can audit the model on population data (5.1).

---

## Power P2 — Tenant-screening report and recommendation

**B1. What it can do to people.** For a landlord's fee, the [RENTAL SCREENING DIVISION] returns a report on a rental applicant with a result of "accept", "accept with conditions" or "decline". The report combines the credit file (P3), eviction filings and criminal records bought from [COURT-RECORDS AGGREGATOR], and a proprietary score. Property-management software applies the result directly to the application. A decline usually means the applicant loses that unit, and the same record can produce declines at every unit the person applies for.

**B2. Who and where.** About 15 million [EX] applicant reports per year in [COUNTRY]. Applicants do not choose the screener; the landlord does. Non-participants include co-applicants and household members whose names appear in eviction filings.

**B3. Authority basis.** `indirect_a_operationalized`. The landlord decides; the agency's recommendation is built into that decision.
- Who relies on it: landlords and property managers, through software settings that accept or decline on the result.
- Causation Ladder: tier 4, operational reliance [S1]. The evidence is routine, structured reliance in practice: the software applies the result without a person reviewing it, in about 80% [EX] of the managers' configured workflows. Tiers 1–5 support a finding, so tier 4 is enough.
- Not enough on its own: an aggregate statistic that landlords "usually follow" recommendations is tier 7 (residual correlation) and would support only a recorded concern. The software configuration is what lifts the evidence to tier 4.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The same federal law, regulators, and courts regulate tenant screening. They are not shown to authorize this power for a fixed term after hearing affected people. A qualifying authorization: UNKNOWN | compliance not demonstrated |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Same as P1, plus a [CITY] ordinance enforced by the [CITY] housing office that bars use of eviction filings older than 3 years [EX] | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Federal private right of action; fair-housing complaint to the federal housing agency. Financial assurance: UNKNOWN. | compliance not demonstrated |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Eviction filings reported for 7 years [EX] whatever the outcome; sealed records still appear (B9); no deletion record. | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Applicant learns the screener's name only from an adverse-action notice; score rules not published. | not conforming |
| Floors | See B6 (Part II) | See B6 | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Sealed and dismissed court records re-enter decisions through a bought dataset (4.4). | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Enforcement order under the federal fair credit reporting law | one_practice | federal consumer financial regulator or federal consumer protection agency | independent | [EX] |
| 2 | Local ordinance limiting use of eviction filings and old criminal records | one_practice, within [CITY] only | [CITY] housing office | independent | [EX] |
| 3 | Fair-housing suit on disparate impact | one_practice | a federal court | independent | [EX] |
| 4 | Applicant dispute of an item | one_case | the agency's dispute unit | not_independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes — housing, an essential, is conditioned on a record that cannot be paid off; a filed and dismissed eviction still counts | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — a dispute takes about 30 days [EX], by which time the unit is gone | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | yes, through courts; not before the housing is lost | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — tenants who organized and were then served eviction filings carry those filings into screening; not studied for this agency | |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | yes — eviction filings and criminal records fall unequally by race and sex; no independent review | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | no | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — the report is built from the credit file and bought court records; no person, home or device is searched |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | UNKNOWN — a decline applied automatically at every unit a person applies for can decide where the person is able to live (B1). The agency bars no one from any place, and whether a private screening result is a restriction under 2.D.16 is for independent interpretation (7.3); the harm is recorded under Economic and Due process | [EX] |

Structural entrapment (2.D.6): yes. A record that cannot be challenged in time and lasts for years binds a person to repeated exclusion.

**B7. Data.** Eviction filings, criminal records, addresses and the credit file. The division keeps each report for 5 years [EX]. Records are matched by name and birth date, without a unique identifier, which produces matches to the wrong person.

**B8. Dependencies and evasion.** [COURT-RECORDS AGGREGATOR] copies court dockets in bulk. When a court later seals a case, the copy already sold is not recalled. Under 4.4 the court record is a derived output of an authority and carries its purpose limits; under 4.6 the aggregator and the agency have a propagation duty when the record is sealed. Neither is met.

**B9. Harms seen.**
- economic, informational: reports that listed dismissed or sealed eviction cases; a regulator order addressed this, settled without admission by this agency.
- economic: applicants matched to another person's criminal record; adjudicated in individual suits [EX].
- generational, non_participant: children moved between schools after repeated declines of a household; allegation in advocacy research.

**B10. Decision inputs and oversight.** Eviction filings, criminal records, credit file, income ratio and the score. The weights and the decline rule are not published (5.3). No outside auditor has access (5.1).

---

## Power P3 — Compiling and keeping consumer files

**B1. What it can do to people.** It collects and keeps information about a person without asking: accounts, balances, late payments, collections, addresses, inquiries, and some public records. It decides whether a disputed item stays. What it keeps feeds P1 and P2 and every other report it sells.

**B2. Who and where.** About 200 million [EX] adults in [COUNTRY]. Inclusion is automatic and cannot be refused.

**B3. Authority basis.** `direct`. Collecting and keeping a person's information is an act the agency takes on that person itself; no other party's decision is needed for the power to exist. Under the Collect definition, receiving data from furnishers counts as collecting it [S1].

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The same federal law, regulators, and courts regulate file collection and retention. They are not shown to authorize this power for a fixed term after hearing affected people. A qualifying authorization: UNKNOWN | compliance not demonstrated |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. No exposure size is set as a stop condition (3.C.2). | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | One-practice orders only; see B5 | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Courts and regulators; a past breach settlement. Financial assurance: UNKNOWN. | compliance not demonstrated |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Most negative items 7 years [EX]; bankruptcies 10 years [EX]; accounts in good standing kept with no end date. No deletion record. | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | A person can get a free copy of the file once a year [EX], and the reporting periods are in the federal law. The matching rules that decide what enters a file are not published (5.3). | not conforming |
| Floors | See B6 (Part II) | See B6 | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Re-aging of old debts by furnishers can restart the reporting clock; the agency's controls are UNKNOWN. | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Regulator order on data security or accuracy | one_practice | federal consumer protection agency | independent | [EX] |
| 2 | Court order to delete an inaccurate item | one_case | a court | independent | [EX] |
| 3 | Statutory end of the reporting period for a negative item | one_case (that item only) | the federal law itself; applied by the agency | not_independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | no for P3 itself; its effects are recorded under P1 and P2 | |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — nobody is told when a file is opened; no exit | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | yes, through courts | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | no evidence found | |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — error rates by group not published | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | no | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — files are built from records furnished to the agency; it searches no person, home or device |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

Informational sovereignty (2.D.12): the file is a permanent index of each adult, with no stated purpose-based end. Records of accounts in good standing have no deletion date.

**B7. Data.** Identity data, account histories, inquiries, collections, some court records. Kept for the life of the file. No deletion record (7.6). A past data breach exposed a large share of files; there was no defined exposure size or automatic stop.

**B8. Dependencies and evasion.** About 10,000 [EX] furnishers report without payment. Contractors handle part of dispute processing offshore [EX]; they act under the agency's control and are counted as part of it (4.5).

**B9. Harms seen.**
- informational: a past data breach; regulator order, settled without admission.
- informational, agency: inaccurate items left after dispute; adjudicated in individual suits [EX].

**B10. Decision inputs and oversight.** What enters the file is decided by furnisher reports and the agency's matching rules. The matching rules are not published (5.3). Regulators examine; outsiders cannot (5.1).

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | Definitions (Authority, Collect, Causation Ladder); 2.D.3; 2.D.10; 2.D.12; 7.2 | | yes |

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

- Consumer-reporting law, regulatory enforcement, and judicial remedies are existing safeguards in this fictional scenario. They do not, as described here, amount to an independent, affected-person-informed authorization of the agency's powers for a fixed term. The record lists those safeguards and their limits. It uses `NONE EXISTS` only where the scenario establishes that no qualifying authorization exists; otherwise the qualifying authorization is `UNKNOWN` and the finding is `not_demonstrated` (3.A.1, 3.A.2). The same rule applies to P1, P2, and P3.
- Indirect authority needs a named reliant party and a Causation Ladder tier. P1 rests on contractual dependency (tier 2); P2 on operational reliance through software settings (tier 4). A bare "landlords usually follow it" statistic is tier 7 and supports only a concern (Definitions: Causation Ladder; 4.3(a)).
- The same company holds a direct power too. Collecting and keeping the file (P3) is direct, because receiving data is collecting it (Definitions: Collect; 2.D.12).
- A statutory reporting period is not a conforming retention limit when other data in the same file has no end date and nothing records deletion (2.D.12, 7.6).
- The status-register exception in 2.D.12 does not reach a credit file. It covers only a record whose sole purpose is to establish the person's own continuing status, title, or entitlement, used for nothing but confirming it; a consumer file exists to inform other parties' decisions. Accounts in good standing therefore stay under the 20-year [S1] ceiling, and consent cannot extend it. The person's interest in a long history is met by receiving a copy before destruction (2.D.14), not by keeping the file with no end date, so P3's data limits stay not conforming.
- Laundering through bought data: a sealed court record that re-enters screening through an aggregator's copy is an evasion finding, and both firms carry the propagation duty (4.4, 4.6, 4.1).
- Stop paths here are real but narrow. Regulators, courts and a city ordinance each stop one practice or one case; nothing stops the power as a whole, so the stop-paths row is not conforming (3.A.7, 3.C.1).
- A security freeze is not a stop path, because it works only by giving up credit. Paying, complying or giving up never counts (3.C.1; 2.B.3).
- An equal-treatment disparity calls for an independent review within the deadline in 2.D.10; that review needs no Causation Ladder tier, whereas a proxy finding under 4.7 does.
- Mark data limits "not applicable" for a power that keeps no data of its own (P1), and assess the data where it is actually kept (P3), rather than counting the same gap twice (3.A.1).
- A screening decline can decide where a person is able to live without barring anyone from a place. The record logs whether 2.D.16 reaches such a result for interpretation (7.3) and keeps the finding under 2.B and 2.D.5.
