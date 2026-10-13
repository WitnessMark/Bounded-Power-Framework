---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-INTL-REFUGEE-OPERATION
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
  name: "[REGIONAL HUMANITARIAN BODY] — [HOST COUNTRY] Operation"
  legal_entity: "[REGIONAL HUMANITARIAN BODY], an organization created by treaty among its member states"
  related_entities: "[FOOD-SUPPLY PARTNER] (a separate humanitarian organization that supplies rations); [IMPLEMENTING PARTNER] (a nonprofit that runs distributions); [BIOMETRIC SYSTEM VENDOR]; the [HOST COUNTRY] refugee office; resettlement states that receive registration data"
  type: international
  country: "[HOST COUNTRY]"
  region: "[BORDER REGION]"
  locality: "[SETTLEMENT] refugee settlement"
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Refugee status determination"
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
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_conforming
      evasion: not_applicable
  - power_id: P2
    short_name: "Biometric registration"
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
      visibility: conforming
      floors: not_conforming
      evasion: not_conforming
  - power_id: P3
    short_name: "Food ration allocation"
    category: benefits_eligibility_or_allocation
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
      evasion: not_demonstrated
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

> **Structural record.** People are referred to by role or title. This record describes structure, not guilt. Adjudicated or admitted facts are kept separate from allegations.

# [REGIONAL HUMANITARIAN BODY] — [HOST COUNTRY] Operation — Registration

## PART A — The institution

A1. **What it is.** The country operation of a treaty-based humanitarian body. In [HOST COUNTRY], which has no national asylum procedure, it decides who is recognized as a refugee, registers every arrival with fingerprints, iris scans, and a photograph, and — with a food-supply partner — decides who receives food rations and how much. Its work protects people from being returned to danger and keeps them fed; its decisions are also very hard to challenge.

A2. **Legal basis.** A mandate set by its founding treaty and reviewed periodically by the member states; a treaty on privileges and immunities that shields the organization and its staff from the jurisdiction of national courts; and a host agreement with [HOST COUNTRY] that confirms those immunities and lets the operation work in the country.

A3. **Who controls it.** A head of organization chosen by the member states; a governing council of member states; a country representative who directs the operation. Most funding comes from voluntary contributions by a small number of donor states.

A4. **Related entities.** A separate humanitarian organization supplies the food; a nonprofit implementing partner runs distributions; a vendor supplies the biometric system; the host government's refugee office co-signs identity documents; resettlement states receive registration records for cases referred to them. Figures belong to the operation unless stated.

A5. **Adoption.** not_adopted. Findings are diagnostic (Force and Status).

A6. **Powers found.**
- P1 Refugee status determination.
- P2 Biometric registration.
- P3 Food ration allocation.
- Not recorded: shelter allocation; resettlement referral; camp security arrangements with host police.

---

## Power P1 — Refugee status determination

**B1. What it can do to people.** It decides whether a person is a refugee. Recognition brings a protection letter, which host police generally respect, and access to assistance and resettlement. Rejection closes the file: the person loses that protection and may be detained or returned by the host state.

**B2. Who and where.** About 14,000 [EX] individual cases pending in [HOST COUNTRY]; median wait of 26 [EX] months from registration to first decision. Arrivals of one nationality are recognized as a group without individual interviews; arrivals of other nationalities go through individual determination.

**B3. Authority basis.** `direct`. The operation decides; the host state relies on the decision.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | Mandate in the founding treaty and a host agreement; no authorization of status determination in this country, and refugees were not heard | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for broad-reach powers (3.E.1, 7.2) | NONE EXISTS. The treaty mandate has no end date; member states review it periodically, on no fixed schedule, and the review covers the whole organization, not this power | not conforming |
| Harm thresholds | 3.A.5 | NONE EXISTS. Published procedural standards set target times but no harm threshold | not conforming |
| Stop paths | 3.A.7, 3.C.1 | No independent path; immunity bars every court (B5) | not conforming |
| Ending plan | 3.A.9 | A multi-year operation strategy describes handover of determination to a future national asylum office; whether it covers open cases and records: UNKNOWN | compliance not demonstrated |
| Remedy | Independent, funded correction (3.A.10) | Appeal to another officer of the same office; no compensation route; immunity bars courts | not conforming |
| Data limits | 2.D.12–2.D.14 | Interview records kept indefinitely; whether a retention period exists: UNKNOWN | compliance not demonstrated |
| Visibility | 3.B.9 | Procedural standards, eligibility criteria, and the open-ended treaty mandate are public; that the power has no expiry is knowable (the failure is recorded under Maximum term) | conforming |
| Floors | Part II | No independent challenge (B6) | not conforming |
| Evasion | Part IV | Immunity comes from treaty, not from splitting or outsourcing the power | not applicable |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Appeal of a rejection | one_case | A second eligibility officer of the same operation | not_independent | [EX] |
| 2 | Request to reopen on new facts | one_case | The operation | not_independent | [EX] |
| 3 | Withdrawal of host consent under the existing host agreement | whole_power (in this country) | [HOST COUNTRY] government | partly_independent — party to the host agreement; its refugee office receives project funding from the operation | [EX] |

Not counted: an instruction from the governing council of member states (the organization's own governing body); a future national asylum law (a new law); national courts (barred by immunity).

Statement: *Can anything stop this power as a whole?* — **yes, path 3 — holder not independent** (partly independent, never tested, and no refugee can start it).

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | — | not_applicable — no ecological effect | — |
| Economic (2.B) | Essentials conditional? | Rejection ends assistance after 3 [EX] months | [EX] |
| Agency (2.C) | Told plainly? | Rejection letters give short standard reasons in English only; interpreters at interviews | [EX] |
| Force (2.D.1) | — | not_applicable — no force | — |
| Confinement (2.D.3) | Only on the four permitted grounds? | not_applicable — the operation confines no one; host detention after rejection is the host's power | — |
| Emergency medical care (2.D.2) | — | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Challenge before someone independent? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | no — appeal stays within the operation; immunity bars courts | [EX] |
| Expression (2.D.9) | — | No evidence | — |
| Equal treatment (2.D.10) | Burdens by national origin? Reviewed? | UNKNOWN — group recognition for one nationality and individual procedure for others is a difference by national origin; it may be justified by country conditions, but no independent review exists | — |
| Identification (2.D.11) | — | See P2 | — |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | UNKNOWN — original identity documents handed in for the interview are kept in the file until a decision [EX], a median wait of 26 [EX] months; whether they are returned on request, once holding them no longer serves the determination, is not shown | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — the operation restricts no one's movement; detention or return after rejection is the host state's power (B1) |  |

**B7. Data.** Interview transcripts, testimony about persecution, country-of-origin research. Highly sensitive; a breach could endanger family members in the country of origin.

**B8. Dependencies and evasion.** Most funding comes from a few donor states, which shapes priorities such as resettlement quotas (3.B.6). Host recognition of protection letters depends on the host agreement.

**B9. Harms seen.** Psychological and agency: waits of over two [EX] years in uncertainty (observed in the operation's statistics). Bodily: rejected applicants detained and returned by host authorities (allegation, reported by refugee-led groups; host action, not the operation's).

**B10. Decision inputs and oversight.** Interview, credibility assessment, and country-of-origin information, under published guidance. Oversight: an internal inspector general (misconduct, not decisions) and member-state auditors (finances). No outside body evaluates decisions.

---

## Power P2 — Biometric registration

**B1. What it can do to people.** Every arrival aged 5 [EX] and over must give ten fingerprints, both irises, and a photograph to be registered. Without registration a person receives no ration card, no shelter, and no protection letter. Records are shared with the host government and, for referred cases, with resettlement states.

**B2. Who and where.** About 210,000 [EX] registered people in [HOST COUNTRY], including children. Host communities are not registered.

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | 3.A.1, 3.A.2 | Adopted by the organization's own data and registration policy; no independent authorization | not conforming |
| Maximum term | 3.E.1, 7.2 | NONE EXISTS | not conforming |
| Harm thresholds | 3.A.5 | NONE EXISTS. No exposure size set as a stop condition (3.C.2) | not conforming |
| Stop paths | 3.A.7, 3.C.1 | Internal complaint only (B5) | not conforming |
| Ending plan | 3.A.9 | NONE EXISTS for the biometric database | not conforming |
| Remedy | 3.A.10 | Complaints to an internal data protection officer; no independent route | not conforming |
| Data limits | Biometrics destroyed within 10 [S1] years (2.D.13) | Kept indefinitely, including after return or resettlement; copies held by the host government and resettlement states under data-sharing agreements | not conforming |
| Visibility | 3.B.9 | A data protection policy, the sharing agreements' existence, and registration rules are public | conforming |
| Floors | Part II | Biometric identification as a condition of food, with no non-biometric option (B6) | not conforming |
| Evasion | Part IV | Copies held by host and resettlement states are outside the operation's deletion; the receivers have propagation duties (4.4, 4.6), but the sharing agreements impose none | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Complaint to the data protection officer | one_case | Internal officer | not_independent | [EX] |

Not counted: a change of registration policy by the head of organization (the institution itself).

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | — | not_applicable | — |
| Economic (2.B) | Essentials used as leverage? | yes — food is given only after biometric registration (2.B.3) | [EX] |
| Agency (2.C) | Told plainly? Can people refuse? | A consent form is read at registration, but refusing means no food; consent is not real | [EX] |
| Force (2.D.1) | — | not_applicable | — |
| Confinement (2.D.3) | Only on the four permitted grounds? | not_applicable — no detention | — |
| Emergency medical care (2.D.2) | — | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | no | [EX] |
| Expression (2.D.9) | — | No evidence | — |
| Equal treatment (2.D.10) | Reviewed? | UNKNOWN — failed fingerprint matches are higher among older manual workers; no review | — |
| Identification (2.D.11) | Compelled identification without cause? | yes — 2.D.11 permits verifying the identity of a person claiming an individual entitlement such as a ration, by the least intrusive means that works, but a non-biometric way must always be offered and the information may not be used for any other purpose. Here fingerprints, irises and a photograph are required of every person aged 5 [EX] and over, with no non-biometric route, and the records are shared with the host government and resettlement states | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — registration takes biometrics, recorded under Identification and Data limits; no search of belongings |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — use of shared records at host checkpoints is the host state's power |  |

**B7. Data.** Fingerprints, irises, face images, family links, and places of origin. Biometric data is covered by 2.D.13: a documented purpose and destruction within 10 [S1] years at most, including every copy held by contractors and partners. Deletion records: NONE EXISTS.

**B8. Dependencies and evasion.** The vendor's system and matching algorithm; host-government copies under the host agreement; resettlement-state copies under referral agreements. Once shared, data is outside the operation's control.

**B9. Harms seen.** Informational exposure: the host government has made a data-sharing request covering registration records (recorded; outcome not public). Agency: people unable to enroll fingerprints were delayed in receiving food (observed in the partner's distribution reports).

**B10. Decision inputs and oversight.** Biometric match scores from the vendor's algorithm; match thresholds are not published (5.3). No independent audit of the database.

---

## Power P3 — Food ration allocation

**B1. What it can do to people.** With the food-supply partner, it decides who is on the ration list and the size of each household's ration. When funding fell, it cut rations and used a household vulnerability score to decide who kept a full ration.

**B2. Who and where.** About 190,000 [EX] people receiving rations. Rations were cut to 72% [EX] of the minimum standard for most households; about 30% [EX] of households, scored most vulnerable, kept full rations.

**B3. Authority basis.** `direct`, held jointly with the food-supply partner (4.2).

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | 3.A.1, 3.A.2 | Joint plan of the two bodies, approved by their own staff | not conforming |
| Maximum term | 3.E.1, 7.2 | Annual joint plan of 12 [EX] months; the allocation power itself does not expire | not conforming |
| Harm thresholds | 3.A.5 | A published minimum standard of 2,100 [EX] kilocalories a day exists, but it is a planning figure set by the bodies themselves, and falling below it triggers nothing | not conforming |
| Stop paths | 3.A.7, 3.C.1 | Feedback line only (B5) | not conforming |
| Ending plan | 3.A.9 | A transition-to-self-reliance plan exists; whether it protects people below the minimum: UNKNOWN | compliance not demonstrated |
| Remedy | 3.A.10 | Complaints hotline run by the implementing partner; no independent route | not conforming |
| Data limits | 2.D.12–2.D.14 | Vulnerability survey data: retention UNKNOWN | compliance not demonstrated |
| Visibility | 3.B.9 | Ration levels and targeting criteria announced at community meetings in 4 [EX] languages | conforming |
| Floors | Part II | Rations below minimum; no review of triage; rations tied to staying in the camp, 2.D.16 (B6) | not conforming |
| Evasion | Part IV | Distribution run by the implementing partner on the operation's lists; whether the partner adds criteria: UNKNOWN | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Appeal of a vulnerability score through the feedback line | one_case | Implementing partner | not_independent | [EX] |

Not counted: a joint decision of the two bodies' country heads (the institutions themselves).

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. (Stopping food allocation would itself cross the Economic Floor; 3.C.5 keeps the minimum essential function.)

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | — | not_applicable | — |
| Economic (2.B) | Essentials conditional on compliance? | yes — rations depend on attending biometric headcounts (2.B.1). Below-minimum rations are caused by funding shortfall, not used as leverage | [EX] |
| Agency (2.C) | Report harm without forms? | yes — by phone or at help desks | [EX] |
| Force (2.D.1) | — | not_applicable | — |
| Confinement (2.D.3) | Only on the four permitted grounds? | not_applicable — no detention | — |
| Emergency medical care (2.D.2) | — | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | no | [EX] |
| Expression (2.D.9) | — | No evidence | — |
| Equal treatment (2.D.10) | Reviewed? | UNKNOWN — the vulnerability score uses household size and head-of-household sex; no review of effects | — |
| Identification (2.D.11) | — | See P2 | — |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — rations are allocated, not seized |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | no — rations are handed out only at camp distribution points to households registered there [EX], and a household absent for two distribution cycles [EX] is taken off the list, so moving to a town costs a family its food. That restricts where people may live on none of the grounds in 2.D.16, with an essential as the lever (2.B.3) | [EX] |

Triage (3.A.12): allocating scarce food by published criteria is not a trade of harms only if the criteria are applied without regard to 2.D.10 characteristics and are independently reviewed afterward. The criteria are published; no independent review has taken place.

**B7. Data.** Ration list, household vulnerability survey answers, attendance at headcounts.

**B8. Dependencies and evasion.** Food supply depends on donor contributions to the food-supply partner. Two bodies hold the power jointly; under 4.2 they are assessed as one function.

**B9. Harms seen.** Bodily: rising child malnutrition after the cut, reported in the bodies' own nutrition survey (admitted). Economic: households selling assets to buy food (observed in surveys).

**B10. Decision inputs and oversight.** Vulnerability score from survey answers; the weighting is published in summary only. Oversight: donor reviews, which are not independent of the funding relationship.

---

## PART C — Sources

This is a worked example. Figures are tagged [EX] and are illustrative; no real source is cited for them.

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it | Quote | Verified? |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.D.11; 2.D.13; 3.A.12; 3.C.5; 7.2 | | yes |

---

## PART D — Honesty assertions

- [x] Every number has a source tag ([EX] for illustrative figures).
- [x] Nothing presented as real was invented; figures are marked illustrative.
- [x] No real organization or country is described.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] Made in good faith, as a structural description, not an accusation.

Preparer: Bounded Power Framework examples set.

---

## Teaching notes (non-binding)

- Immunity removes the usual independent stop paths at once. The only whole-power path (host withdrawal of consent) is held by a partly independent holder, is untested, and cannot be started by the people affected, so 3.A.7 is not met (3.C.1). The organization's own governing council does not count.
- An international body is held to the same rules as any other authority; its form, purpose, and good work do not enlarge its limits (1.3, 1.4).
- Biometrics required for food fail three rules at once: leverage over essentials (2.B.3), biometric-only identification with no non-biometric option (2.D.11), and indefinite retention past 10 [S1] years (2.D.13).
- 2.D.11 allows checking who is claiming a ration, as a claimed individual entitlement, but only by the least intrusive means that works, with a non-biometric way always offered and no other use. Mandatory biometrics with no alternative, shared onward with states, still fail; a ration card or document check offered alongside biometrics, with no onward sharing, could conform.
- Data passed to host and resettlement states escapes deletion. Shared copies are derived outputs and keep the source's limits (4.4); propagation duties apply to the receivers (4.6).
- Ration cuts show the triage exception: scarce essentials may be allocated by published criteria, but only with independent review afterward (3.A.12).
- Stopping a power that provides food would itself cross a Floor; only the harmful operation stops and the minimum essential function continues (3.C.5).
- Group recognition for one nationality may be well founded, but a difference by national origin needs independent review (2.D.10). The record leaves it as UNKNOWN rather than a finding.
- A periodic review of the whole mandate by member states is not a term: it has no set date, is not specific to the power, and is held by the body that governs the organization (3.A.2, 3.E.1, 7.2).
- Tying rations to living in a camp restricts where people may live on none of the grounds 2.D.16 allows, and uses an essential as the lever (2.B.3). The operation needs no guard or gate for the rule to apply.
