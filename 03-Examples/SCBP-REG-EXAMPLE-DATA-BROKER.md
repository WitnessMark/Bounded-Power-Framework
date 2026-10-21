---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-DATA-BROKER
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
  name: "[PEOPLE-DATA BROKER]"
  legal_entity: "[PEOPLE-DATA BROKER HOLDINGS]"
  related_entities: "[PEOPLE-SEARCH WEBSITE] (consumer brand); [LOCATION-DATA SUPPLIER] (app location feed); [LAW-ENFORCEMENT RESELLER] (sells P2 access to police)"
  type: private_company
  country: "[COUNTRY]"
  region: NONE
  locality: NONE
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "People-search dossiers"
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
      visibility: not_demonstrated
      floors: not_conforming
      evasion: not_conforming
  - power_id: P2
    short_name: "Location-history lookups sold to police"
    category: data_collection_or_records
    authority_basis: indirect_a_operationalized
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

# [PEOPLE-DATA BROKER] — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** A private company that buys, copies and infers information about people it has no relationship with, joins it into one profile per person, and sells access. Its records come from public records (property, court, voter, licensing), data bought from apps and other companies, and its own inferences. It sells two things that matter here: a people-search dossier anyone can buy for a small fee, and a location-history lookup sold by subscription to police agencies. People in its files never signed up and usually do not know it exists.

A2. **Legal basis.** Incorporated under [STATE] corporate law. No licence is needed to operate. A [STATE] data broker registration law requires it to register each year [EX], and a state deletion law requires it to honor deletion requests from [STATE] residents. The federal consumer protection agency can act against unfair or deceptive practices. It states that it is not a consumer reporting agency, so the federal fair credit reporting law's accuracy and dispute duties do not apply to its dossiers.

A3. **Who controls it.** Privately held; a board appointed by its investors.

A4. **Related entities.**
- [PEOPLE-SEARCH WEBSITE] sells P1 dossiers to the public.
- [LOCATION-DATA SUPPLIER] gathers device location from software kits inside about 1,000 [EX] phone apps and sells the feed to the broker. Location figures in this record are the supplier's.
- [LAW-ENFORCEMENT RESELLER] licenses P2 to police agencies under its own brand.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — People-search dossiers (data collection, direct).
- P2 — Location-history lookups sold to police (data collection, indirect_a).
- Recorded for watching only, not as a power: "audience segments" sold to advertisers. People can and do ignore an advertisement without material cost, so this is `influence_only` (Authority definition; 4.3).

---

## PART B — One section per power

## Power P1 — People-search dossiers

**B1. What it can do to people.** It builds a profile of a named person: current and past addresses, phone numbers, emails, relatives, neighbors, estimated income, court records, and photos of the home from public listings. Anyone who pays about 1 currency unit [EX] per search or a monthly fee can read it. The person cannot stop the profile from being built and must find and opt out of each brand separately. A profile that gives a home address to someone the person has fled can lead to bodily harm.

**B2. Who and where.** Profiles on about 250 million [EX] people in [COUNTRY], which is nearly every adult. All are non-participants: none chose to be included.

**B3. Authority basis.** `direct`. Collecting information about a person — including by buying, copying or inferring it — is an act the broker takes on that person itself (Definitions: Collect) [S1]. No buyer's later decision is needed for the power to exist. The power also has an indirect side: landlords, employers and others use dossiers to screen people, which the broker says is against its terms. That reliance is shown only by scattered examples (tier 7) and is not used for a finding here.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. State registration is a listing, not an authorization; nobody can refuse it. | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | NONE EXISTS. Registration renews on payment of a fee [EX]. | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Per-person deletion and one-practice orders; see B5 | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS for most people. No private right of action under the [STATE] law; the federal law's dispute rights do not apply because the broker says it is not a consumer reporting agency. | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | No retention period stated; records go back more than 20 years [EX]. Deletion requests honored within 45 days [EX], but the person can reappear when new data arrives. | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | The state registry names the broker and states what kind of data it sells; the deletion route and the annual registration are public, and the lack of any expiry is knowable from them. But sources, inferences and buyers are not disclosed (5.3), and growth cannot be tracked. | compliance not demonstrated |
| Floors | See B6 (Part II) | See B6 | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Many brand names for one database, so opting out of one leaves the others (4.2). Court and licence records whose purpose has ended are carried on (4.4). | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Deletion request under the [STATE] deletion law, enforced against every registered broker | one_case (one person, in one state) | [STATE] privacy agency | independent | [EX] |
| 2 | Order from a consumer protection regulator on a deceptive or unfair practice | one_practice | consumer protection regulator | independent | [EX] |
| 3 | State address-confidentiality program for survivors, which bars publishing enrolled addresses | one_case | [STATE] secretary of state | independent | [EX] |
| 4 | Opt-out form on each brand's website | one_case (one brand) | the broker | not_independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Path 1 is the strongest existing path, and it works only one person at a time and only for residents of [STATE].

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | no — no essential is conditioned. Paid "privacy removal" services sold by partners, at about 100 currency units [EX] a year, put a price on the person's own protection; recorded under Agency | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — nobody is told; opt-out requires finding each brand and sometimes uploading identification | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 hours; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical care | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | no — no independent forum for an inaccurate dossier, outside the [STATE] deletion law | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — dossiers have been used to locate people who spoke publicly; allegations only | |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — inferred categories may include ethnicity and religion; not reviewed | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | yes — it identifies and locates anyone, without cause, for any buyer | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — the broker searches no person, home or device itself; its compiling is recorded under Identification (2.D.11) and 2.D.12 |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | no — it bars no one from any place, though a dossier can reveal where a person who moved to escape someone now lives (B1) | [EX] |

Informational sovereignty (2.D.12): the dossier is a permanent index with no purpose limit and no ceiling; deletion does not stop re-collection. Many entries are copied from status registers, such as land titles, court judgments and licence lists. 2.D.12 lets those registers be kept while the status lasts only because access is limited to confirming the status and the record is never used for any other purpose. A copy joined into a dossier and sold for any purpose is that other use, so the status-register rule gives the broker no basis for keeping it.

**B7. Data.** Names, addresses back to the 1990s [EX], phones, emails, relatives, property, court and licence records, inferred income and interests. Bought or copied, never asked for. Retention: none stated. Deletion record: a suppression list exists, but no record of what was deleted from backups or partner copies (7.6).

**B8. Dependencies and evasion.**
- Sources: county recorders, court dockets, state licensing and voter files where sale is allowed, marketing lists, and other brokers.
- Under 4.4, information from a source that is not itself an authority counts as collected when received. Public records copied from courts and agencies are derived outputs of those authorities and carry their purpose limits.
- The broker runs many sites from one database. Under 4.2 they are one authority system; the evidence is tier 1 (common ownership).

**B9. Harms seen.**
- bodily, psychological: people located by a former partner through a purchased dossier; adjudicated in a civil suit against a broker of this kind [EX].
- informational: inaccurate dossiers mixing two people; allegation in consumer complaints [EX].
- agency: removal requests ignored or reversed after new data arrived; a state agency enforcement notice, settled without admission [EX].

**B10. Decision inputs and oversight.** Record-matching rules and inference models decide what appears under a person's name. None are published (5.3). The [STATE] privacy agency can audit compliance with deletion; no one audits accuracy or sources (5.1).

---

## Power P2 — Location-history lookups sold to police

**B1. What it can do to people.** A police analyst enters a place and a time window; the tool returns the devices seen there and where each device went before and after, including its likely home. A device can be tied to a name through P1. Police use it to find suspects, witnesses and people at protests or clinics, without a warrant, because the data is bought rather than demanded.

**B2. Who and where.** Device histories for about 100 million [EX] devices in [COUNTRY]. Subscribers: about 300 [EX] police agencies. Everyone whose phone runs a supplying app is included, almost all of them people never suspected of anything.

**B3. Authority basis.** `indirect_a_operationalized`. The broker does not arrest or charge anyone; police agencies rely on its output to open investigations, identify people and seek warrants.
- Who relies on it: police agencies that subscribe through [LAW-ENFORCEMENT RESELLER].
- Supply relationship: subscription contracts bind the broker to supply location-history data to police agencies. The agencies' published procurement records show this. A supply obligation alone does not prove that the output is operationalized into police decisions.
- Causation Ladder: tier 4, operational reliance [S1]. The fictional scenario separately states that police use location-history results to identify people, open investigations, and seek warrants (B1). In this worked example those stated uses are the evidence of reliance. A real record would need a source for each use, such as agency procedures, warrant applications, or case records, and would apply the Causation Ladder to that evidence. A contractual label such as "investigative lead only" neither proves nor disproves operationalization. Where actual reliance is not sufficiently established, the record states that uncertainty rather than treating the supply contract as conclusive.
- Material cost: a person cannot avoid it without giving up ordinary phone apps, and the person does not know which apps supply it.
- Both are in scope: the broker for its output, the police agency for its own decision (Authority definition).

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. Some city councils approve surveillance-technology purchases after a hearing; this authorizes the police purchase in that city, not the broker's power. | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | Contracts run 1 year [EX] and renew; the power itself has no end date. | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | A regulator order bars sale of visits to listed sensitive places; that list is one partial threshold. Others: NONE EXISTS. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | See B5 | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS. People are not told they were found this way; suppression of evidence in a criminal case is the only route, and only for a person charged. | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | History kept for 3 years [EX] under the contract; no deletion record; police copies kept under each agency's own rules. | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Known mainly through public-records requests by journalists and researchers; not knowable to an ordinary person. | not conforming |
| Floors | See B6 (Part II) | See B6 | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Police buy what they could get otherwise only with a warrant (4.5). Location is "pseudonymous" but re-identified through P1 (Definitions: Personal information). | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Regulator order on sensitive locations | one_practice | consumer protection regulator | independent | [EX] |
| 2 | City council refusal or repeal under a surveillance-technology ordinance | one_practice (that city's purchase) | [CITY] council | partly_independent | [EX] |
| 3 | Court suppression of evidence obtained from the tool | one_case | a criminal court | independent | [EX] |

Path 2 is partly independent: the council funds the police agency that wants the tool and is not independent of the buyer, though it is independent of the broker. Turning off location in each app is self-help, not a stop path, so it is not listed; most people also cannot tell which apps supply the feed.

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Only a new law barring government purchase of location data could.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | no evidence found | |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — never told | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — the broker uses no force; police force is the police agency's power | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 hours; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — the broker confines no one | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical care | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | no for people never charged; only a person charged can challenge in court | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — place-and-time searches around protests are documented in records requests [EX]; whether any person was punished is not shown | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — searches around places of worship appear in records requests [EX]; no review | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | yes — place-and-time searches identify everyone present, with no individualized cause: suspicionless mass identification. Keeping, combining and searching people's movement history also requires individualized cause under 2.D.11, and the broker keeps it for every device | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | no — a place-and-time query returns location histories drawn from people's own phones, with no individualized cause and no judicial approval [EX]. Police would need a warrant to demand the same history from a phone company; buying it skips that step (4.5). The broker answers for supplying the search, the police agency for running it | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | no — the tool bars no one from any place; tracking who went to a protest or clinic is recorded under Expression and Identification | [EX] |

**B7. Data.** Device identifiers, timestamped coordinates, inferred home and work places. Collected from app software kits; consent screens in the apps do not mention police. Retention 3 years [EX] at the broker; police copies kept under each agency's rules. No deletion record.

**B8. Dependencies and evasion.**
- [LOCATION-DATA SUPPLIER] depends on app makers who are paid per device [EX]; the broker depends on the supplier; police depend on the broker through [LAW-ENFORCEMENT RESELLER]. Under 4.1 every link shares responsibility.
- For police, buying the data produces a result they could not obtain directly without cause; under 4.5 the broker's system is treated as part of the police power for that use. This record covers the broker's side only.

**B9. Harms seen.**
- informational, agency: tracking of people at sensitive places; regulator order, settled without admission [EX].
- communicative: place-and-time searches near a protest; allegation, from public-records documents [EX].
- non_participant: every person whose device is in the dataset.

**B10. Decision inputs and oversight.** Search inputs are chosen by police analysts. The broker logs searches but does not publish them, and police agencies' audit logs are not public (5.3, 5.1). Nobody audits for accuracy of re-identification.

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures and definitions cited | BPF: Core Requirements v1 | Definitions (Authority, Collect, Personal information, Causation Ladder); 4.4; 4.5 | | yes |

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

- Buying, copying and inferring are all collecting. A broker that never asks anyone for anything still exercises a direct data-collection power (Definitions: Collect; 2.D.12).
- Data from a source that is not an authority counts as collected on receipt; data copied from courts and agencies carries the purpose limits of its source (4.4). For status registers such as titles and judgments, that limit is confirming the status only, so their long retention does not carry over to a dossier (2.D.12).
- One database behind many brand names is one authority system. Common ownership is tier 1 evidence, so the finding needs nothing more (4.2; Definitions: Causation Ladder).
- The same company can hold a direct power (P1) and an indirect one (P2). For P2 the reliant party is a police agency. The subscription contract shows a supply relationship, not reliance; the indirect classification rests on the stated police uses, placed on the Causation Ladder (4.3(a)).
- Both sides of a purchase are in scope. Police buying what they could not lawfully demand is evasion on the police side (4.5); the broker answers for its output (Authority definition; 4.1).
- Place-and-time searches that identify everyone present are suspicionless mass identification, whoever runs them (2.D.11).
- "Pseudonymous" location data is still personal information when it can be re-identified (Definitions: Personal information).
- A state deletion law is a real, independent stop path, but it reaches one person at a time. That is why the stop-path row is still not conforming (3.A.7, 3.C.1).
- Nearly every requirement row here is not conforming. That is typical for this kind of firm, and it is a finding, not a default: each row names what is absent. A state registration law is a listing, not an authorization, because no one can refuse it (3.A.2).
- Visibility is judged on what can be known (3.B.9). The registry makes some facts knowable for P1, so that row is compliance not demonstrated rather than not conforming; P2 is known only through records requests, so it fails.
- Self-help is not a stop path. Turning off app location is something the person does to themselves, not a check on the broker (Form B5).
- Ad segments are recorded as influence only. People can ignore them at no material cost, so they are watched rather than registered as a power (4.3).
- Location history drawn from people's own phones is a search of their devices under 2.D.15. Buying the data does not change that: individualized cause and a judicial officer's approval are needed either way (2.D.15, 4.5).
