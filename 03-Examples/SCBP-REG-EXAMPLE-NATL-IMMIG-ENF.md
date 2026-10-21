---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-NATL-IMMIG-ENF
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
  name: "[COUNTRY] Immigration Enforcement Agency"
  legal_entity: "[COUNTRY] national government, [INTERIOR MINISTRY]"
  related_entities: "[DETENTION CONTRACTOR]; county jails under detention agreements; [DATA BROKER]"
  type: government
  country: "[COUNTRY]"
  region: NONE
  locality: NONE
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Civil immigration detention"
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
      evasion: not_conforming
  - power_id: P2
    short_name: "Removal from the country"
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
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_conforming
      evasion: not_demonstrated
  - power_id: P3
    short_name: "Bought data and biometrics"
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
      visibility: not_conforming
      floors: not_conforming
      evasion: not_conforming
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

> **Structural record.** Based on public sources and/or the preparer's own observation. People are referred to by role or title. This record describes structure, not guilt. Adjudicated or admitted facts are kept separate from allegations.

# [COUNTRY] Immigration Enforcement Agency — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** The national agency that finds, arrests, detains and removes non-citizens whom the immigration law treats as removable. It works inside the country, away from the border. Detention and removal are civil, not criminal, under the law. The agency also builds files on people from its own records, from other agencies, and from data it buys.

A2. **Legal basis.** The [COUNTRY] Immigration Act, regulations of the [INTERIOR MINISTRY], and the national constitution as applied by the courts. The Act has no end date. Funding is set by the national legislature each year.

A3. **Who controls it.** A Director appointed by the Minister. Removal cases and bond reviews are decided by members of [IMMIGRATION TRIBUNAL], a tribunal attached to a ministry rather than to the courts. An internal oversight office of the [INTERIOR MINISTRY] audits the agency.

A4. **Related entities.** [DETENTION CONTRACTOR] runs most detention centers under contract; county jails hold people under paid detention agreements. [DATA BROKER] sells location, utility and address data. Figures here belong to the agency unless stated.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — Civil detention of non-citizens during and after removal proceedings.
- P2 — Removal (deportation) from the country.
- P3 — Collection of bought data and biometrics.
- Not recorded: arrests and use of force by officers (use_of_force); worksite inspections (inspection_search_or_surveillance); detainer requests to local jails.

---

## Power P1 — Civil immigration detention

**B1. What it can do to people.** Lock a person in a detention center or contracted jail cell while their removal case runs, and after a removal order until they are removed. For some groups the law makes detention mandatory; for others an officer sets a money bond, which a tribunal member may review.

**B2. Who and where.** About 16,000 people on an average day [EX], in about 70 facilities [EX]. Average stay about 50 days [EX]; some stays exceed 1 year [EX]. Families and children of detained people are non-participants.

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. The Immigration Act grants detention; no independent body authorizes it as a separate power | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. Detention standards exist, but they are the agency's own and nothing stops when they are breached | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Individual court petitions and one facility injunction (B5). NONE EXISTS for the whole power: the legislature's general power to amend or repeal the Act does not count, and no independent body has an existing procedure to end the power within a defined time | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS for wrongful detention beyond a damages claim against the state, which has narrow exceptions for discretionary acts | not conforming |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Detention files kept by the agency; retention UNKNOWN | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Daily population is published and the Act shows plainly that detention has no expiry; bond criteria and the custody worksheet are not published, so what the power may do in a given case cannot be learned | compliance not demonstrated |
| Floors | See B6 (Part II) | Detention does not fit any ground in 2.D.3; no free lawyer (2.D.5); home entries on administrative warrants, blanket strip searches and phone searches without judicial approval (2.D.15) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Most beds are contracted; contractor standards are set and inspected by the agency itself (4.2, 4.5) | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Petition to a national court for release from unlawful detention | one_case | a national trial court | independent | [EX] |
| 2 | Bond hearing before a tribunal member | one_case | a member of [IMMIGRATION TRIBUNAL] | partly_independent (the tribunal is attached to a ministry, not to the courts or the agency) | [EX] |
| 3 | Injunction on conditions at one facility | one_practice | a national court | independent | [EX] |
| 4 | Oversight office report | one_practice (recommendation only) | the internal oversight office | partly_independent (inside the same ministry) | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. The national legislature can amend or repeal the statutory authority for civil immigration detention, but that is the general ability to pass a new law, which does not count. The Act has no end date, so no sunset vote must take place. The yearly funding vote sets money, not whether the power exists, so it is not a procedure to end the power. Individual court petitions, bond hearings, and facility injunctions provide protections of differing independence and scope; none is shown here to suspend the detention power as a whole.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes — release depends on paying a bond, set at a minimum of 1,500 currency units [EX]; people who cannot pay stay detained | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — notices are legal forms, often in a language the person does not read; there is no appointed lawyer; about 70% of detained people have none [EX] | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | UNKNOWN — force inside facilities is reviewed by the contractor and the agency | [EX] |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | no. Not (a): no imminent threat is required. Not (c) or (d): it is neither a sanction nor a brief stop. Not (b): the charge is a civil violation the law itself calls non-punitive; even if it were read as an offense, nobody is brought before an independent judicial officer within 48 hours [S1], mandatory categories bar individual findings, and there is no review every 30 days [S1] | [EX] |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | UNKNOWN — medical care in facilities is given by contractor staff; whether treatment without consent ever occurs, and under what rule, is not published | [EX] |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | partly — a court petition is possible; the bond tribunal is attached to a ministry; there is no appointed lawyer, and about 70% of detained people have none [EX] | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — allegation that detained people who spoke to reporters were moved to remote facilities | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — national origin is the basis of the whole system; disparity by race or language within it has not been reviewed | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | see P3 | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | no — homes are entered to make arrests on administrative warrants signed by agency officers, not judicial officers [EX]; everyone admitted to a facility is strip-searched without an individualized finding [EX]; and phones taken at arrest are searched without a judicial officer's approval [EX] | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — detention is recorded under Confinement; release conditions such as ankle monitors are not recorded here |  |

**B7. Data.** Detention files, medical records, force and segregation reports, deaths-in-custody reviews. Force reports and death reviews are accountability records; they are held by the agency and its contractors, not by an independent custodian (2.D.14).

**B8. Dependencies and evasion.** [DETENTION CONTRACTOR] is paid per bed per day, with a guaranteed minimum payment whether or not the beds are filled [EX]. A guaranteed minimum makes reducing detention cost money (3.B.7). County jails earn a daily rate of 70 currency units per detained person [EX].

**B9. Harms seen.**
- bodily — admitted: the agency reports 6 deaths in custody last year [EX]; the oversight office found delayed medical care in 3 of them [EX].
- psychological, generational — allegation: children separated from detained parents.
- economic — admitted: families paid bonds averaging 6,000 currency units [EX].

**B10. Decision inputs and oversight.** Statutory categories, officer discretion, and an internal custody classification worksheet that is not published (5.3). The oversight office inspects about 8 facilities a year [EX]; a private inspection firm paid by the agency inspects the rest.

---

## Power P2 — Removal from the country

**B1. What it can do to people.** Physically remove a person from [COUNTRY] to another country after a removal order, and bar their lawful return for a set period or for life.

**B2. Who and where.** About 120,000 removals a year [EX]. Many removed people have spouses and children who are citizens. Those families are non-participants.

**B3. Authority basis.** `direct`. The agency carries out removal with its own officers and charter flights.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Stays of removal in single cases (B5) | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | A person wrongly removed may ask to return if a court later wins; no funded process; the agency facilitates return only "where appropriate" | not conforming |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Removal records kept to enforce re-entry bars; length UNKNOWN | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | The grounds for removal, relief categories, and annual removal numbers are published in the Act and agency reports; the Act shows plainly that the power has no expiry (that failure is recorded under Maximum term) | conforming |
| Floors | See B6 (Part II) | Irreversible effects created before review is complete (3.D.2); citizens removed in error are helped to return only "where appropriate" (2.D.16) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Removal flights are run by contracted charter airlines; whether contract terms add or shift any removal decision: UNKNOWN | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Appeal to the tribunal's appeal division, with automatic stay | one_case | the appeal division of [IMMIGRATION TRIBUNAL] | partly_independent (attached to a ministry) | [EX] |
| 2 | Petition to a national appeals court with a discretionary stay | one_case | a national appeals court | independent | [EX] |
| 3 | Injunction against removal to one destination country | one_practice | a national court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | not_applicable — no charges | |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — appeal deadlines are 30 days [EX] and notices are legal forms | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | UNKNOWN — restraints are used on removal flights; review is internal | [EX] |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | see P1 | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | partly — a tribunal hearing is available, but the tribunal is attached to a ministry, there is no appointed lawyer, and a removal can proceed while a court petition is pending without a stay | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN | |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — not reviewed | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | not_applicable — see P3 | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — searches at arrest and in detention are recorded under P1 |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | partly — conditions on entering and staying are a published condition of crossing a border, a licensed activity that 2.D.16 allows to be conditioned. But 2.D.16 never permits barring a person from returning to their own country. The agency's own audit counted 6 citizens removed in error over five years [EX], and it helps a wrongly removed person return only "where appropriate" (B4 Remedy). Whether life-long re-entry bars on long-term residents who grew up in [COUNTRY] bar them from their own country is for independent interpretation (7.3) | [EX] |

**B7. Data.** Removal orders, travel documents, fingerprints shared with destination governments. Retention UNKNOWN.

**B8. Dependencies and evasion.** Charter airlines under contract; agreements with destination governments.

**B9. Harms seen.**
- bodily, psychological — allegation: people removed to countries where they face danger.
- generational, non_participant — admitted: the agency's own statistics show about 20% of people removed [EX] reported a citizen child.
- agency — adjudicated: courts ordered the return of 2 wrongly removed people in 3 years [EX]; return took months in each.

**B10. Decision inputs and oversight.** Removal orders from the tribunal; agency priorities set by ministerial memos, which change with each government. The national legislature receives annual reports.

**Why removal is the irreversibility case.** A wrongful removal can be followed by a court win, but the time apart, the lost job and home, and harm in the destination country cannot be undone. Under 3.D.2, an effect that is hard to reverse must be blocked until review is complete. Here removal can be carried out while a court petition is pending unless the person also wins a stay.

---

## Power P3 — Bought data and biometrics

**B1. What it can do to people.** Find and identify people by buying commercial location, address and utility data; by querying regional photo-ID databases with face matching; and by taking fingerprints, photos and, for some detained people, DNA. Keep all of it in a national identity database.

**B2. Who and where.** The biometric database holds records on about 40 million people [EX], many of them citizens and lawful residents who once applied for a visa or were fingerprinted at a border. The broker data cover nearly every adult in the country.

**B3. Authority basis.** `direct`. Bought data count as collected (Definitions: Collect; 4.4).

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. Purchases are made under general procurement rules; no body authorized buying location data | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Regional agencies can stop sharing photo-ID data (one practice); nothing else | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | A request to correct a record goes to the agency itself | not conforming |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Biometrics are kept 75 years [EX]; the limit is 10 years [S1] and the ceiling for all personal data is 20 years [S1] | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Broker contracts are not published; their existence became known through a records request | not conforming |
| Floors | See B6 (Part II) | Identification without individualized cause (2.D.11); biometric limit (2.D.13); bought location data and DNA swabs without judicial approval (2.D.15) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Buying location data the agency would need a court order to demand directly (4.4, 4.5) | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | A regional identity agency ends its data-sharing agreement | one_practice | a regional government | independent | [EX] |
| 2 | National privacy commissioner finding | one_practice (recommendation only) | the privacy commissioner | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | no — but utility-account data mean that getting water or power connected exposes a person's address | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — people are not told their data were bought | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | no | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — social-media monitoring contract exists; its use is not reported | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — face matching error rates by group not published | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | yes — bulk location data and face matching against regional photo-ID records identify people without individualized cause; holding a photo ID for one licensed activity is not a condition for immigration tracing | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | no — location histories drawn from people's phones are bought and searched with no individualized cause and no judicial approval, in place of the court order the agency would need to demand them [EX]; DNA is taken from some detained people by cheek swab without a judicial officer's approval [EX] | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | no — the data are used to locate people, not to bar them from places; families avoiding utilities and clinics is recorded under B9 | [EX] |

**B7. Data.** Location history, addresses, utility accounts, licence photos, fingerprints, face images, DNA for some detained people. Purpose: locating and identifying people for enforcement. Retention 75 years [EX] for biometrics; broker data retention UNKNOWN. No deletion record (7.6).

**B8. Dependencies and evasion.** [DATA BROKER] supplies data it bought from apps and utilities. Regional identity agencies give face-match access under agreements. This is the laundering case in 4.4: data obtained from a source that is not itself an authority are treated as collected when received.

**B9. Harms seen.**
- informational — admitted: a records request produced a multi-year contract worth 12 million currency units [EX] for location data.
- agency, non_participant — allegation: families stopped using utilities or clinics after address data were traced.

**B10. Decision inputs and oversight.** Search criteria and face-matching thresholds are not published. The privacy commissioner can investigate but cannot order a stop.

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.D.3, 2.D.12, 2.D.13, 3.D.2, 7.2 | | yes |

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

- Civil detention is tested against all four grounds of 2.D.3 and fits none. Calling detention "civil" or "non-punitive" does not change the analysis (1.3).
- Even read generously as a charge under 2.D.3(b), it fails that ground: no independent judicial officer within 48 hours [S1], no individualized finding where detention is mandatory, no 30-day review [S1].
- A bond a person cannot pay keeps them confined because of poverty. That is a 2.B.1 and 2.D.3 problem together.
- Removal is the 3.D.2 case: the effect is hard to reverse and can be carried out while review is pending.
- Under 3.D.2 only a temporary, protective change of legal status can be containment: reversible by default, limited in time, confined to the danger, and independently reviewed within a short fixed period. Removal is none of these. It is a lasting change of status with effects that cannot be undone, and a permanent change of legal status is never containment, so the P2 findings stand.
- Bought data are collected data (Definitions: Collect; 4.4). Buying what a court order would be needed to demand is evasion under 4.5.
- Biometrics kept for decades break both 2.D.13 (10 years [S1]) and the 20-year [S1] ceiling in 2.D.12.
- Bed guarantees in detention contracts create a dependency that makes narrowing costly (3.B.7, 3.A.8).
- A tribunal attached to a ministry is partly independent of the agency. Record it that way and explain why (form B5).
- 2.D.15 requires an independent judicial officer to approve entry into a home. An administrative warrant signed inside the agency is not approval by anyone independent, and buying location data in place of a court order fails the same rule (4.5).
- 2.D.16 never permits barring a person from returning to their own country. Citizens removed in error and helped back only "where appropriate" fail it; whether life-long re-entry bars reach long-term residents' own country is logged for interpretation (7.3).
