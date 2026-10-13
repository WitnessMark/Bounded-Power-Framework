---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-CITY-PD
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
  name: "[CITY] Police Department"
  legal_entity: "[CITY] (municipal corporation)"
  related_entities: "[BODY-CAMERA VENDOR]; [PLATE-READER VENDOR]; [TOWING CONTRACTOR]"
  type: government
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: "[CITY]"
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Use of force by officers"
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
  - power_id: P2
    short_name: "Stops, arrests and short holding"
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
      remedy: not_demonstrated
      data_limits: not_conforming
      visibility: conforming
      floors: not_conforming
      evasion: not_demonstrated
  - power_id: P3
    short_name: "Plate readers and camera network"
    category: inspection_search_or_surveillance
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: not_demonstrated
      remedy: not_conforming
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_conforming
      evasion: not_conforming
  - power_id: P4
    short_name: "Tow, impound and forfeiture"
    category: property_land_or_seizure
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
      visibility: not_demonstrated
      floors: not_conforming
      evasion: not_conforming
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

> **Structural record.** Based on public sources and/or the preparer's own observation. People are referred to by role or title. This record describes structure, not guilt. Adjudicated or admitted facts are kept separate from allegations.

# [CITY] Police Department — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** A municipal police department in a mid-size city. Officers stop, question, search and arrest people; use force, up to and including deadly force; hold arrested people briefly before transfer to the county jail; operate fixed and car-mounted plate readers and a network of public cameras; and tow, impound and seek forfeiture of vehicles and cash. The city has about 160,000 residents [EX], and about 300 sworn officers [EX].

A2. **Legal basis.** The [CITY] charter, the [STATE] municipal police statute, the [STATE] criminal procedure code, and national constitutional limits on searches, seizures and force as applied by the courts. A city surveillance-technology ordinance governs P3. None of these sets an end date for the department or any of its powers, except the ordinance for P3.

A3. **Who controls it.** A Chief appointed by the Mayor with council confirmation. The City Council sets the budget and can amend the ordinances. A Civilian Police Review Board, appointed by the Mayor and Council, reviews complaints and issues recommendations. A federal court supervises some force practices under a consent decree (see P1 B5).

A4. **Related entities.** [BODY-CAMERA VENDOR] stores body-camera footage. [PLATE-READER VENDOR] runs the plate-reader cameras and a data-sharing network across many agencies. [TOWING CONTRACTOR] tows and stores vehicles under a city contract. All figures in this record are the department's own unless stated.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — Use of force by officers.
- P2 — Brief stops, arrests, and holding in the precinct cells until transfer.
- P3 — Plate readers and the public camera network.
- P4 — Tow, impound, and civil forfeiture of vehicles and cash.
- Not recorded: traffic and municipal citations (fines_fees_or_charges); the gang-affiliation list (data_collection_or_records); school resource officers.

---

## Power P1 — Use of force by officers

**B1. What it can do to people.** Officers may grab, take down, handcuff, strike, use a conducted electrical weapon, spray chemical irritant, release a police dog, and shoot. Force is used to make arrests, to overcome resistance to orders, and to stop threats to officers or others.

**B2. Who and where.** Anyone in city limits, resident or not. Officers reported about 900 uses of force in the most recent year [EX]. Everyone affected is a non-participant: nobody opts into a police encounter.

**B3. Authority basis.** `direct`. Officers apply force themselves.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. Force is permitted by state statute and a department policy the Chief adopts; no independent body authorizes force as a separate power | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. Policy requires supervisor review of each use; no measurable threshold stops anything | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Paths exist for one practice or one case (B5); none for the whole power; none tested | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | A federal civil-rights lawsuit for damages, which the injured person must bring and fund; officer immunity doctrines limit it. No funded remedy process | not conforming |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Force reports are kept by the department's own internal affairs unit, for 5 years [EX] | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Force policy and annual totals are published, so growth can be seen; state law and the charter show plainly that the power has no expiry or renewal (that failure is recorded under Maximum term) | conforming |
| Floors | See B6 (Part II) | Force not separately authorized and not independently reviewed (2.D.1); disparity not independently reviewed (2.D.10) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Force is used only by sworn officers; no outsourcing found | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Consent decree after a national civil-rights investigation; the court can enforce limits on specific techniques | one_practice | the federal judge and court-appointed monitor | independent | [EX] |
| 2 | Federal civil-rights lawsuit seeking an injunction | one_practice | a federal court, on a resident's petition | independent | [EX] |
| 3 | Officer decertification by the [STATE] officer standards board | one_case | the state board | partly_independent (half its seats are held by serving police officials [EX]) | [EX] |
| 4 | Civilian Police Review Board finding | one_case (recommendation only; the Chief may decline) | the Board | not_independent (appointed by the Mayor and Council, staffed from the city budget) | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Only a change in state law could end police authority to use force in the city.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway identified | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | not_applicable — the power imposes no charges | |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — complaints may be made by phone or online, but the complaint form must be signed under penalty of perjury | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | no — policy bans force as punishment, but force is not separately authorized, not externally stoppable while used, and reviewed inside the chain of command except under the decree | [EX] |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — confinement is recorded under P2 | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | yes — in court, after the fact | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — complaints allege irritant spray at a protest; no finding yet | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | yes, not independently reviewed — published data show force per stop about 1.8 times higher for one group [EX] | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | not_applicable — see P2 and P3 | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — searches are recorded under P2 |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — stops and arrests are recorded under P2 |  |

**B7. Data.** Force reports, body-camera footage of each use, injury photos. Force reports are accountability records (Definitions). They are held by the internal affairs unit, which reports to the Chief, and are destroyed after 5 years [EX]. The rule requires 10 years in custody chosen by an independent body [S1]. Deletions are not logged.

**B8. Dependencies and evasion.** [BODY-CAMERA VENDOR] holds footage under a city contract; the department controls access and deletion. Weapons and training come from vendors. No sign of outsourcing force.

**B9. Harms seen.** Bodily — settled without admission: the city agreed to a consent decree on use-of-force practices after a national civil-rights investigation reported a pattern of excessive force. The decree is still in its monitoring phase. Bodily — adjudicated: two civil judgments for excessive force in the last 5 years [EX]. Psychological, non_participant — allegation: bystanders and family members report lasting harm after a fatal shooting.

**B10. Decision inputs and oversight.** The written force policy and officer judgment drive decisions. The policy is public; training scenarios are not. The decree monitor audits a sample of force reports twice a year [EX]. Outside researchers can obtain aggregate data only.

---

## Power P2 — Stops, arrests and short holding

**B1. What it can do to people.** Stop a person on the street or in a car, question them, frisk them, require them to give their name during a lawful stop, arrest them, and hold them in precinct cells until transfer to the county jail or release on a citation.

**B2. Who and where.** Anyone in city limits. About 30,000 traffic and street stops [EX] and 6,000 arrests [EX] a year.

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. State criminal procedure law; no separate authorization of the power | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Case-level paths only (B5) | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Suppression of evidence and civil lawsuits exist; whether any funded route exists for people never charged is UNKNOWN | compliance not demonstrated |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | The department keeps arrest reports 75 years [EX] in its own custody. An arrest is a confinement, so the report is an accountability record: 10 [S1] years in custody chosen by an independent body, then removal of non-agents' personal information (2.D.14). Retention of fingerprints in state and national databases: UNKNOWN | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Stop data published under a state data law; state law shows plainly that the power has no expiry or renewal (that failure is recorded under Maximum term) | conforming |
| Floors | See B6 (Part II) | Reasons for stops are not given to the person (2.D.3(d)); disparity not reviewed (2.D.10); vehicle, arrest and consent searches with no judicial approval or later review, and consent not shown to be freely given (2.D.15) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Officers on a regional task force act under another agency's rules; UNKNOWN whether this avoids city limits | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Release at first appearance when the judge finds no probable cause | one_case | a county judge | independent | [EX] |
| 2 | Motion to suppress evidence from an unlawful stop | one_case | the trial court | independent | [EX] |
| 3 | Injunction in a class lawsuit over a stop practice | one_practice | a federal court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | not_applicable — charges are recorded outside this power | |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — arrested people receive rights warnings; stopped people receive no explanation of how to challenge the stop | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | see P1 | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | partly. Arrests (b): 97% of arrested people reach a judge within 48 [S1] hours [EX]; weekend arrests sometimes exceed it. Brief stops (d): reasons are recorded on a stop-data form but not given to the person | [EX] |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | yes, for people who are charged — a public defender is appointed at first appearance for anyone who cannot pay, rights warnings are given before questioning, and first appearances are held in open court [EX]; some weekend arrests wait longer than 48 [S1] hours (see Confinement). People stopped and released have only a complaint or lawsuit | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — protest arrests for "failure to disperse" not reviewed | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | yes, not reviewed — stop rates per resident differ by group by about 2.5 times [EX]; no independent review | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | no — a state law requires a name only during a stop based on individualized suspicion | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | no — home searches need a warrant and frisks need individualized suspicion [EX], but vehicles are searched without a warrant under the state's vehicle exception, and searches at arrest and by consent need no judicial approval; none of these is reviewed by a judicial officer afterwards unless the person is charged and moves to suppress. Officers ask for consent at traffic stops without saying it may be refused [EX], so consent is not shown to be freely given. Property taken at arrest is returned on release, except cash and vehicles held for forfeiture (P4) | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | UNKNOWN — dispersal orders at protests close streets to everyone present [EX]; whether each was narrow and lasted no longer than an imminent danger is not reviewed. Stops and arrests are recorded under Confinement | [EX] |

**B7. Data.** Stop forms, arrest reports, booking photos and fingerprints. Fingerprints and photos are biometric data; they are sent to the state and national identification databases, where retention is set by those agencies and is UNKNOWN for this record. The department keeps arrest reports for 75 years [EX] in its own custody, which fails 2.D.14 (see B4) and the 20-year [S1] ceiling in 2.D.12.

**B8. Dependencies and evasion.** The county jail receives arrested people. A regional drug task force operates under a multi-agency agreement; city officers on it follow the lead agency's rules.

**B9. Harms seen.** Agency, informational — allegation: people stopped report never learning why; arrest records remain on background checks after dismissal. Psychological — allegation: repeated stops of the same residents in two neighborhoods [EX].

**B10. Decision inputs and oversight.** Officer judgment, dispatch calls, and plate-reader alerts (P3). Stop data are published each year under state law. No outside body audits stop decisions.

---

## Power P3 — Plate readers and camera network

**B1. What it can do to people.** Photograph and log every passing license plate with time and place, alert officers when a plate is on a hot list, and search the stored reads. Fixed cameras record public streets and squares.

**B2. Who and where.** Every vehicle passing 60 fixed readers [EX] and 25 patrol cars with readers [EX]; about 1.5 million plate reads a month [EX]. Almost all are people suspected of nothing.

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The City Council approves the technology each year after a public hearing, under the surveillance-technology ordinance. The Council is part of the same city, so it is not independent of the power. No panel chosen by lot from the people affected, with appeal to an independent body, authorizes it (3.A.2) | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | Approval lapses after 12 months [EX] unless renewed | conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. The annual report counts hits and errors, but nothing stops at any number | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Only the Council can end the power, and it is the city's own governing body (B5) | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | The vendor contract has a termination clause; data return or destruction on exit is UNKNOWN | compliance not demonstrated |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS for a wrong stop caused by a misread plate, beyond a lawsuit | not conforming |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Reads not linked to a case are deleted after 30 days [EX]; no deletion record; copies on the vendor's sharing network UNKNOWN | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Use policy, annual report, renewal date and camera map are published under the ordinance | conforming |
| Floors | See B6 (Part II) | Every passing car's location is kept for 30 days [EX] and searchable without individualized cause (2.D.11; B6) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Officers can query reads from other cities through the vendor's network, which the ordinance does not cover | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Court order removing one camera location | one_practice | a court | independent | [EX] |

Not counted: the Council declining the annual renewal. That would end the power, but the Council is the city's own governing body, not independent of the department (form B5).

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | not_applicable — no charges | |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — signs are posted at city entrances, but people are not told how to challenge a read | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — the power uses no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | no — no route to challenge a stored read | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — reads near protest sites are stored like any others | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — fixed readers are concentrated in some districts; not reviewed | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | yes — showing a plate is a published condition of driving, and 2.D.11 permits identification at the point of driving for its regulatory purpose. But the system keeps every car's time-and-place reads for 30 days [EX] and lets officers search them without a case or other individualized cause, and through the vendor network for up to a year [EX]. Keeping or searching location history needs individualized cause | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — the cameras search no person, home, device or belongings; searching stored reads without a case is recorded under Identification (2.D.11) |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | no — the system records where cars go but bars no one from any place | [EX] |

**B7. Data.** Plate, time, place, and a photo of the vehicle. Purpose: hot-list alerts and investigations. Reads not linked to a case are deleted after 30 days [EX]; reads linked to a case follow the case file. Deletion is automatic; no deletion record is kept (7.6).

**B8. Dependencies and evasion.** [PLATE-READER VENDOR] hosts all reads and runs a network through which agencies share them. Officers can search other agencies' reads, which are kept for up to a year [EX] under those agencies' rules. This gets around the city's 30-day [EX] limit (4.5).

**B9. Harms seen.** Informational — admitted: the annual report lists 14 misreads leading to a stop [EX], including one stop at gunpoint [EX]. Agency — allegation: a resident reports that her car's location history was searched without a case.

**B10. Decision inputs and oversight.** Hot lists from the state and national crime databases and officer entries. The ordinance requires an annual use report to the Council. No outside auditor reviews searches.

---

## Power P4 — Tow, impound and forfeiture

**B1. What it can do to people.** Tow and impound a vehicle after an arrest, for unpaid tickets, for unregistered driving, or as evidence; charge towing and daily storage fees; sell unclaimed vehicles; and seek civil forfeiture of vehicles and cash alleged to be linked to a crime, without a criminal conviction.

**B2. Who and where.** About 4,000 tows a year [EX]; about 150 forfeiture cases a year [EX]. Owners who were not driving are often affected.

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. State traffic code, the towing contract, and the state forfeiture law | not conforming |
| Maximum term | Expires on a set date; 2 [S1] years for force, confinement, broad-reach, or first-time powers; never over 10 [S1] (3.E.1, 7.2) | NONE EXISTS. The towing contract runs 5 years [EX], but the power does not end with it | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Case-level hearings only | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | A wrongly towed owner can get the tow fee back after a hearing; storage fees, lost work and a sold vehicle are not compensated | not conforming |
| Data limits | Stated retention periods; 20-year [S1] ceiling; 10 [S1] years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | UNKNOWN | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Fee schedule published; forfeiture totals published only in a state report | compliance not demonstrated |
| Floors | See B6 (Part II) | Storage fees grow while the owner cannot pay (2.B.2); property seized without judicial approval, and permanently forfeited without a finding that the owner was responsible (2.D.15) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | The department keeps 80% of forfeiture proceeds [EX] and the contractor keeps storage fees, so both profit from the power (economic extraction; 4.1) | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Post-tow hearing | one_case | a city hearing officer | not_independent (a city employee) | [EX] |
| 2 | Forfeiture trial | one_case | a state court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes — storage accrues at a daily fee of 35 [EX] currency units; after 30 days [EX] the vehicle is sold. A worker who needs the car to earn the fee cannot get it back. No fee waiver for inability to pay | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — the forfeiture notice is a legal form; the owner must file a written claim within 30 days [EX] or lose the property | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 [S1] hours, with pretrial custody only on individualized findings; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical treatment |  |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | partly — forfeiture goes to court; tow hearings are before a city employee | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — not reviewed | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | not_applicable | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | no — officers tow vehicles and seize cash without a judicial officer's approval, and no judicial officer reviews the seizure afterwards unless the owner asks for a hearing [EX]. Civil forfeiture permanently takes vehicles and cash without any finding that the owner was responsible, including from owners who were not driving [EX]; unclaimed vehicles are sold after 30 days [EX] | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Vehicle and owner records, tow and sale records. Retention UNKNOWN.

**B8. Dependencies and evasion.** [TOWING CONTRACTOR] tows, stores and sells vehicles and keeps fees. Forfeiture proceeds return to the department's budget. A state program also lets the department hand seized property to a national agency and receive a share back, which can bypass stricter state limits (4.2, 4.5).

**B9. Harms seen.** Economic — admitted: city reports show about 900 vehicles sold each year [EX] because owners did not pay fees. Economic — allegation: owners with no criminal charge lost cash in forfeiture cases they could not afford to contest.

**B10. Decision inputs and oversight.** Officer discretion on whether to tow; the fee schedule; prosecutors' decisions to file forfeiture. The city auditor reviewed towing once, 4 years ago [EX]. No ongoing outside oversight.

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.D.3, 2.D.12, 2.D.14 | | yes |

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

- One institution, four powers. Each is bounded, stopped and ended on its own (Definitions: Power; 3.A.1). A single "police department" finding would hide that P3 is far closer to conforming than P1.
- Whole-power stop paths are usually NONE EXISTS for force and arrest (3.A.7, 3.C.1). A consent decree is real and independent, but it reaches one practice, not the power.
- P3 shows why an annual council vote is a term (3.E.1, 7.2) and visibility (3.B.9) but neither an independent authorization (3.A.2) nor a counted stop path: the council belongs to the same city. Under 3.A.2 a self-governing city may have its powers authorized by a panel chosen by lot from the people affected, excluding operators and anyone paid by the city, with appeal to an independent body. The council's own vote is not such a panel, so authorization stays not conforming.
- A pattern reported by an investigation is the kind of fact 3.D.5 treats as structural, but settled without admission it supports a recorded concern and a 3.D.5 review, not a pattern finding. Individual damages would not discharge a finding.
- Force reports and arrest reports (records of confinement) are accountability records. Keeping them in the department's own unit fails 2.D.14 even if nothing is deleted early; for arrest reports 2.D.14 applies, not only the 2.D.12 ceiling.
- P2 separates the arrest ground 2.D.3(b) (judge within 48 hours [S1]) from the brief-stop ground 2.D.3(d), which also requires that the reason be given to the person.
- Plate readers under 2.D.11: reading a plate at the point of driving, for driving's regulatory purpose, is a permitted licensed-activity identification. Keeping, combining, or searching every car's location history is not; it needs individualized cause. P3 keeps 30 days [EX] of reads of everyone and allows searches without a case, so its Floors finding is not conforming.
- Daily storage fees are the 2.B.2 escalation case; forfeiture proceeds and contractor fees are economic extraction (Definitions) and a 4.1 incentive issue.
- 2.D.15 separates a seizure from a permanent taking. Holding a car as evidence can be justified case by case, with a judicial officer's approval or prompt review; forfeiting it without a finding that its owner was responsible never can (P4). In P2, vehicle and consent searches fail on the missing judicial review, and consent asked for without saying it may be refused is not shown to be freely given.
