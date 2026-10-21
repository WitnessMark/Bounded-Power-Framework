---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-COUNTY-HEALTH-DEPT
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
  name: "[COUNTY] Health Department"
  legal_entity: "[COUNTY] (county government), acting through the County Health Officer"
  related_entities: "[STATE] Department of Health (state lab, disease surveillance system); [COUNTY] Sheriff's Office (enforces confinement orders); [COUNTY] governing board (ratifies emergency declarations)"
  type: government
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: "[COUNTY]"
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Isolation and quarantine orders"
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
      visibility: conforming
      floors: not_conforming
      evasion: conforming
  - power_id: P2
    short_name: "Food embargo, recall, and destruction"
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
      remedy: not_demonstrated
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_conforming
      evasion: conforming
  - power_id: P3
    short_name: "Local public-health emergency declaration"
    category: other
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_demonstrated
      ending_plan: not_demonstrated
      remedy: not_conforming
      data_limits: not_applicable
      visibility: conforming
      floors: not_demonstrated
      evasion: not_conforming
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [COUNTY] Health Department — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** The county's public-health agency. It tracks communicable disease, inspects food businesses, and can order people to stay home or be held in a facility when they carry or have been exposed to a dangerous disease. It can stop the sale of contaminated food and order it destroyed. In an outbreak its Health Officer can declare a local emergency that unlocks closure orders and limits on gatherings.

A2. **Legal basis.** The [STATE] Public Health Code, which gives each county Health Officer isolation, quarantine, embargo, and emergency powers [EX], and the [STATE] Food Code for food-safety standards [EX].

A3. **Who controls it.** The County Health Officer, a physician appointed by and removable by the county governing board [EX]. The board funds about 60% of the department's budget; the state funds the rest [EX].

A4. **Related entities.** The state lab confirms pathogens; the state disease surveillance system holds case records; the Sheriff's Office enforces court confinement orders. Figures in this record are the department's unless marked as the state's.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — Isolation and quarantine orders (assigned teaching point: confinement under 2.D.3(a)).
- P2 — Food embargo, recall, and destruction (assigned teaching point: protective containment under 3.D.2).
- P3 — Local public-health emergency declaration (the 1.6 clock).
- P4 — Food-business permits and inspections: not recorded.

---

## Power P1 — Isolation and quarantine orders

**B1. What it can do to people.** The Health Officer can order a person who has a listed communicable disease to stay isolated, and a person exposed to one to stay in quarantine, usually at home. A person who breaks an order can be brought before a court and confined in a designated facility, with deputies enforcing the court order. An order lasts up to 21 days [EX] and can be renewed by a new order. For tuberculosis the code allows facility confinement "until treatment is complete" [EX].

**B2. Who and where.** Anyone present in the county, about 900,000 residents [EX] plus visitors. In the [EX] 2025 reporting year the department issued 1,240 orders [EX], almost all home isolation, and sought 3 court confinement orders [EX]. Household members of a person under order are affected without being named in it.

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | A general grant in the state code [EX]; no authorizing decision with findings on each requirement: NONE EXISTS | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | Each order has a limit of 21 days [EX]; the power itself has no expiry: NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | Criteria for issuing orders exist [EX]; thresholds for the power's own harms, such as orders later found unneeded: NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Court and state review of single orders only [EX]. NONE EXISTS for the whole power: the legislature's general power to amend or repeal the statute does not count, and no independent body has an existing procedure to end the power within a defined time | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS [EX] | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Court release exists; compensation for an unneeded order is barred by discretionary-act immunity [EX]: NONE EXISTS | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | County files kept 10 years [EX]; state surveillance records kept with no end date [EX], past the 20-year ceiling [S1] | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Code and order criteria public; weekly counts of orders published [EX]; each order explains itself in plain language in 5 languages [EX] | conforming |
| Floors | See B6 (Part II) | Confinement can outlast the threat; no wage support [EX]; no free lawyer for home orders (2.D.5) | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Orders issued and enforced by public bodies only [EX] | conforming |

**Confinement ground.** Of the four grounds, only 2.D.3(a) could support this power: confinement to stop an imminent threat of bodily harm to identifiable people, for no longer than the threat lasts. It is not an arrest, so the 48-hour judicial rule of 2.D.3(b) does not apply [S1], but due process does (2.D.5).
- 2.D.3(a) covers isolating a person, on an individualized finding, who is infectious and exposing a defined group to a serious transmissible disease, for no longer than the infectious period. Isolation orders here are individualized and rest on lab results [EX], so they can fit (a) while the person is infectious.
- Quarantine of a person who is only exposed fits (a) only on an individualized finding that the person may be infectious, and only for the period in which infection is still possible. Orders run their full 21 days [EX] even after a negative test, because the code ties duration to the order, not to the infectious period. That part does not fit (a).
- Confinement "until treatment is complete" [EX] can continue after a person stops being infectious. In the [EX] 2025 cases one person was held 5 months [EX], about 3 of them after testing non-infectious [EX]. That period rests on a prediction of future non-adherence, which 2.D.3 does not allow.
- Breaking an order is also a misdemeanor [EX]. Any jail sentence must stand on its own ground under 2.D.3(c); the quarantine authority cannot be used to punish.

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Court hearing on the person's request, held within 72 hours [EX] | one_case | Trial court judge | independent | [EX] |
| 2 | State Health Director may rescind a county order [EX] | one_case | State Health Director | independent — the county neither funds, appoints, nor can remove the Director [EX] | [EX] |
| 3 | Mandatory court review every 30 days [EX] for facility confinement | one_case | Trial court judge | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. The state legislature can amend or repeal the statutory authority for this power, but that is the general ability to pass a new law, which does not count. The scenario shows no sunset vote and no standing review body with power to end it. Existing judicial and administrative review protects individual cases and practices.

A stop signal against this power is acted on at once. The protective-operations deferral in 3.C.5 does not apply, because confinement is enforced with force.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Irreversible ecological threshold? | not_applicable — no physical activity on the environment | — |
| Economic (2.B) | Essentials conditional on compliance? Escalating obligations? Path out? | no — food and medicine are delivered during orders [EX]; but no wage replacement exists, so low-wage workers lose income for complying [EX] (2.B.1 risk) | [EX] |
| Agency (2.C) | Told plainly without asking? Report harm without forms? Leave? | partly — plain-language orders [EX]; but a hearing happens only if the person asks, a burden of self-advocacy (2.C.2) | [EX] |
| Force (2.D.1) | Force separately authorized, minimal, stoppable, reviewed? | no — deputies enforce confinement under general sheriff authority; no separate force authorization or review for these transports [EX] | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds — (a) imminent bodily threat; (b) arrest before a judicial officer within 48 hours, pretrial custody on individualized findings; (c) sanction after due process; (d) brief stop on suspicion? | no — isolation of an infectious person fits (a), but orders run their full 21 days [EX] after a negative test, and facility confinement continued about 3 months [EX] after the person tested non-infectious, past the infectious period; see "Confinement ground" above | [EX] [S1] |
| Emergency medical care (2.D.2) | Treatment without consent only on incapacity plus imminent serious harm, incapacity found by an independent clinician, valid refusals honored? | UNKNOWN — whether people confined for tuberculosis are treated over their refusal is not reported [EX] | [EX] |
| Due process (2.D.5) | Challenge before someone independent? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | partly — a court hearing within 72 hours [EX] on the person's request; counsel is appointed only for facility confinement [EX], so a person under a home order, which also confines, has no free lawyer. Hearings are closed to protect medical privacy unless the person asks for an open one [EX] | [EX] |
| Expression (2.D.9) | Restricts lawful expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? Reviewed? | UNKNOWN — orders are concentrated in two zip codes with large immigrant populations [EX]; no review | [EX] |
| Identification (2.D.11) | Compelled identification without cause? | no — naming contacts is voluntary [EX]; orders are individualized | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — adherence is checked by phone and text [EX]; staff do not enter homes or search belongings | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — an order that keeps a person at home keeps them within an area, which 2.D.16 treats as confinement; recorded under Confinement |  |

**B7. Data.** Name, address, test results, contacts, and adherence notes. Purpose: disease control. County files are kept 10 years [EX]; the state system keeps case records with no end date [EX]. Deletion records: NONE EXISTS. Court confinement records are court records.

**B8. Dependencies and evasion.** The state lab (independent) confirms disease; the Sheriff enforces court orders; a contracted motel houses people who cannot isolate at home [EX]. No sign of splitting or proxies.

**B9. Harms seen.**
- bodily and psychological — one complaint of injury during transport to a facility [EX] (allegation).
- economic — job loss reported by 12 people under orders [EX] (allegation); state law bars dismissal but enforcement is by private lawsuit [EX].
- agency — the 3 months of confinement after non-infectiousness noted above [EX] (admitted fact, recorded in the court file).

**B10. Decision inputs and oversight.** Inputs: lab results, symptom reports, exposure history, and a published adherence checklist [EX] (5.3). No outside audit of orders exists; the state reviews county programs every 3 years [EX] without reviewing individual orders.

---

## Power P2 — Food embargo, recall, and destruction

**B1. What it can do to people.** The Health Officer can tag food as embargoed so it cannot be sold or moved, order a recall when a firm refuses to recall voluntarily, issue public alerts naming the firm, and order destruction once the state lab confirms contamination. Perishable food may be destroyed before any hearing [EX].

**B2. Who and where.** Food businesses in the county, about 6,500 permit holders [EX], and the public who would eat the food. In the [EX] 2025 year: 46 embargoes [EX], 9 destruction orders [EX], 2 mandatory recalls [EX].

**B3. Authority basis.** `direct`.

**Containment test (3.D.2).** Physically containing a hazard is stopping harm, not an irreversible exercise of power, if it is the least harmful means that works, confined to the hazard, documented, and independently reviewed afterward. Observed:
- Least harmful means: embargo comes first and is released if the lab result is negative [EX]. Met.
- Confined to the hazard: embargoes normally cover named lot codes [EX]. In one [EX] 2025 case the whole facility's stock was embargoed, including product lines never tested [EX]. Not met in that case.
- Documented: an embargo log with lot, reason, and lab result [EX]. Met.
- Independent review afterward: only when the owner appeals [EX]. No routine review: NONE EXISTS.
- Destruction falls on the property of the firm whose product is contaminated, so its challenge after the fact before a state administrative law judge [EX] satisfies 2.D.5.
- A permit suspension or fine that follows is a change of legal status or a financial penalty. It is never containment and belongs to P4 (not recorded).

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | State code grant [EX]; NONE EXISTS as a 3.A.2 decision | not conforming |
| Maximum term | Expires on a set date (3.E.1, 7.2) | NONE EXISTS; an embargo lasts up to 15 days [EX] | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | Action triggers rest on independent state lab results [EX]; thresholds for the power's own harms (wrongful destruction, over-broad embargo): NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one independent (3.A.7, 3.C.1) | Single-case appeals only [EX]. NONE EXISTS for the whole power: the legislature's general power to amend or repeal the statute does not count, and no independent body has an existing procedure to end the power within a defined time | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS [EX] | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Administrative judge can order release; whether tort claims for wrongful destruction survive immunity is UNKNOWN [EX] | compliance not demonstrated |
| Data limits | Stated retention periods; deletion records (2.D.12–2.D.14, 7.6) | Traceback uses retailer loyalty-card purchase records to notify buyers [EX]; retention period UNKNOWN | compliance not demonstrated |
| Visibility | Knowable to an ordinary person (3.B.9) | Alerts, embargo notices, and annual counts published [EX] | conforming |
| Floors | See B6 (Part II) | Embargoes made without a judicial officer's approval are reviewed only if the owner appeals, and one embargo seized untested product lines (2.D.15); destruction can be challenged after the fact [EX] | not conforming |
| Evasion | Not split, outsourced, laundered (Part IV) | Performed by the department itself [EX] | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Hearing before a state administrative law judge, requested within 10 days [EX] | one_case | State office of administrative hearings | independent | [EX] |
| 2 | Court review of the judge's decision | one_case | Trial court | independent | [EX] |
| 3 | Negative state lab result releases the embargo automatically [EX] | one_case | State lab | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. The state legislature can amend or repeal the statutory authority for this power, but that is the general ability to pass a new law, which does not count. The scenario shows no sunset vote and no standing review body with power to end it. Existing judicial and administrative review protects individual cases and practices.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Irreversible ecological threshold? | no — destroyed food goes to licensed disposal [EX] | [EX] |
| Economic (2.B) | Essentials conditional? Escalating obligations? | no — no fees or penalties attach to an embargo itself [EX] | [EX] |
| Agency (2.C) | Plain explanation? | yes — the tag and notice explain the reason and appeal route [EX] | [EX] |
| Force (2.D.1) | — | not_applicable — no force against persons | — |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no detention | — |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Challenge before someone independent? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — state administrative judge [EX] | [EX] |
| Expression (2.D.9) | Restricts lawful expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? Reviewed? | no, reviewed — a recent state audit [EX] found no disparity by owner language [EX]; most holders are organizations, which claim only due process | [EX] |
| Identification (2.D.11) | Compelled identification? | not_applicable | — |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | no — inspections are a published condition of the food permit, limited to food and premises [EX], which 2.D.15 permits. An embargo seizes named lots on an inspector's specific finding, without a judicial officer's prior approval; waiting could allow imminent bodily harm, which 2.D.15 accepts. But a seizure without approval must then be reviewed promptly, and here review happens only if the owner appeals within 10 days [EX]; one embargo also seized untested product lines (B3). Embargoed food is released when the lab result is negative [EX]. Most permit holders are organizations, which may claim only due process; the rule protects the sole proprietors and street vendors among them, about a fifth of permit holders [EX] | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — an embargo holds goods, not people |  |

**B7. Data.** Business records, lot codes, and customer purchase records received from retailers for recall notice [EX]. Under 4.4 the customer records are collected by the department when received. Retention and deletion: UNKNOWN.

**B8. Dependencies and evasion.** State lab (independent). Retailers' loyalty-card systems supply customer data [EX]. No splitting or proxies found.

**B9. Harms seen.**
- economic — the over-broad facility embargo noted in B3 cost the firm stock valued at 180,000 currency units [EX], released after 9 days [EX] (admitted fact in the department's log).
- informational — a public alert named a firm whose product later tested negative [EX] (admitted fact; a correction was issued).

**B10. Decision inputs and oversight.** Inputs are state lab results and traceback records under the published Food Code [EX] (5.3). The state reviews the food program every 3 years [EX].

---

## Power P3 — Local public-health emergency declaration

**B1. What it can do to people.** The Health Officer may declare a local public-health emergency. While it lasts, the Health Officer may close businesses, limit gatherings, and require masks, enforced by misdemeanor citations [EX]. The declaration lapses after 7 days [EX] unless the county governing board ratifies it; the board may extend it in 30-day [EX] steps with no limit on the number of steps.

**B2. Who and where.** Everyone in the county, about 900,000 residents [EX]. In the [EX] respiratory epidemic, closure orders reached about 14,000 businesses [EX].

**B3. Authority basis.** `direct`.

**B4. Observed vs required.** Under 1.6, a power activated because of an emergency expires within 90 days; it may continue only through re-entry, no more than twice, with each continuation shorter than the one before [S1]. A standing power that needs no declared emergency would be an ordinary power instead.

Observed [EX]: declared, ratified, then extended 13 times in 30-day steps, for 14 months in all. When the board declined a fourteenth extension, the Health Officer issued a new declaration the next day citing a new variant, and the board ratified it.

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | Ratified by the county governing board, which appoints the Health Officer and funds the department [EX]: not independent | not conforming |
| Maximum term | Emergency power: 90 days, at most two shrinking continuations by re-entry (1.6, 7.2) | 14 months through equal 30-day extensions [EX], against a 90-day limit [S1] | not conforming |
| Harm thresholds | Published, measurable thresholds (3.A.5) | Case-rate triggers for reopening were published [EX] but were set and changed by the Health Officer; harm thresholds for the closures themselves: NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one independent (3.A.7, 3.C.1) | The Governor may end any local declaration [EX]; test record UNKNOWN | compliance not demonstrated |
| Ending plan | A documented way to end the power safely (3.A.9) | The code says all orders lapse when the declaration ends [EX]; no plan for unwinding contracts or records: UNKNOWN | compliance not demonstrated |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS [EX] | not conforming |
| Data limits | Retention periods (2.D.12–2.D.14) | The declaration itself collects no personal information [EX] | not applicable |
| Visibility | Knowable to an ordinary person (3.B.9) | Each declaration and extension published with its end date [EX] | conforming |
| Floors | See B6 (Part II) | Gathering limits and closures raise expression and economic questions [EX]; whether closures lasted no longer than the danger is not shown (2.D.16) | compliance not demonstrated |
| Evasion | Not split or renamed to avoid limits (Part IV) | A new declaration for the same epidemic reset the clock [EX] | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Governor terminates the local declaration [EX] | whole_power | Governor | independent | [EX] |
| 2 | County governing board declines to ratify or extend | whole_power | County governing board | not_independent | [EX] |
| 3 | Court injunction against a specific order | one_practice | Trial court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — yes, path 1: the Governor, independent, under existing law; never tested. Path 2 does not count, because the county governing board is not independent of the department; it was also defeated once by re-declaration [EX].

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Irreversible ecological threshold? | not_applicable | — |
| Economic (2.B) | Essentials conditional? Escalating obligations? | UNKNOWN — closures cut income for about 40,000 workers [EX]; grocery stores and pharmacies stayed open [EX] | [EX] |
| Agency (2.C) | Plain explanation? | yes — orders published in plain language [EX] | [EX] |
| Force (2.D.1) | — | not_applicable — enforced by citation | — |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — isolation orders are P1 | — |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Challenge before someone independent? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — court [EX] | [EX] |
| Expression (2.D.9) | Restricts lawful assembly? News reporting or petitioning? Approval before publication? | UNKNOWN — a court enjoined one gathering limit as broader than needed [EX] | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? Reviewed? | UNKNOWN — no review | [EX] |
| Identification (2.D.11) | Compelled identification? | no | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — the declaration searches nothing; closures are enforced by citation [EX] | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | UNKNOWN — closing named kinds of business to entry is the 2.D.16 case of a narrow, published rule closing specific places, but only for as long as an imminent danger there lasts. Closures ran 14 months [EX] through extensions and a re-declaration, and nothing tied each closure to the danger at the places closed. Gathering limits are recorded under Expression | [EX] |

**B7. Data.** None collected by the declaration itself. Orders issued under it fall under P1 or are not recorded.

**B8. Dependencies and evasion.** The re-declaration in B4 is functional continuity: under 4.2 the second declaration is the same power, and its clock runs from the first.

**B9. Harms seen.**
- economic — 1,100 business closures that did not reopen [EX]; the share caused by the orders is an estimate (allegation or estimate).
- communicative — the enjoined gathering limit (adjudicated fact).

**B10. Decision inputs and oversight.** Case rates and hospital capacity were published daily [EX]. No outside audit of the declaration exists.

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 1.6 (90 days), 2.D.3(b) (48 hours), 2.D.12 (20 years) | | yes |

All other facts and figures are illustrative and tagged [EX].

---

## PART D — Honesty assertions

- [x] Every figure carries a source tag or the [EX] illustrative tag.
- [x] Nothing presented as real was invented; illustrative content is marked as such.
- [x] No real institution, person, or place is described.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] Prepared in good faith as a structural description, not an accusation.

Preparer: BPF examples working group (worked example).

---

## Teaching notes (non-binding)

- Of the four confinement grounds, only 2.D.3(a) can support isolation and quarantine. An order that runs its full length after a negative test, or confinement after a person stops being infectious, goes past that ground.
- 2.D.3(a) expressly covers isolating a person who is infectious and exposing a defined group to a serious transmissible disease, on an individualized finding and for no longer than the infectious period. The rule fits P1's individualized isolation orders; it does not reach the fixed 21-day [EX] term or confinement "until treatment is complete" [EX], so the Floors finding stays not conforming.
- The 48-hour judicial rule belongs to arrest under 2.D.3(b) [S1]; quarantine needs due process under 2.D.5 instead, and a hearing that happens only on request puts a self-advocacy burden on the person (2.C.2).
- Quarantine and food embargo are protective containment: stopping harm, not irreversible power, if least harmful, confined to the hazard, documented, and independently reviewed afterward (3.D.2). The over-broad facility embargo and the missing routine review are where this example falls short.
- Destroying a contaminated product falls on the property of the party whose conduct is addressed, so a challenge after the fact satisfies due process (3.D.2, 2.D.5). A permit suspension or fine that follows is never containment.
- For P1 and P2, the legislature's general power to amend or repeal the state code is not a whole-power stop path. It would count only through an existing, usable procedure that must end the power within a defined time, such as a sunset vote. None is shown, so B5 is NONE EXISTS and stop paths are not conforming. P3 differs: the Governor's existing power to end a declaration is a whole-power path in law, though never tested. Urgent isolation, quarantine, and food containment can still happen when justified, subject to independent review, limited duration, and safe ending (3.A.7, 3.C.1, 3.D.2).
- The protective-operations deferral in 3.C.5 does not reach quarantine, because its enforcement uses force.
- An emergency declaration is the 1.6 case: 90 days [S1], then at most two shorter continuations through re-entry. Ratification by the body that appoints and funds the Health Officer is not re-entry (3.A.2).
- Re-declaring the same emergency to reset the clock is evasion by functional continuity (4.2).
- Data received from retailers for a recall is collected when received (4.4), and state case records with no end date breach the 20-year ceiling [S1] (2.D.12).
- 2.D.16 says a restriction that keeps people within an area is confinement, so P1's home orders are judged under 2.D.3, and the 2.D.5 right to a free lawyer applies to them as much as to facility confinement.
- P2's embargo is a seizure under 2.D.15 for the sole proprietors it reaches. Seizing contaminated food before any approval is allowed when waiting would allow imminent bodily harm, but the seizure must then be reviewed promptly by a judicial officer in every case, not only when the owner appeals. With no routine review, P2's Floors finding is not conforming. P3's closures are judged as closures of specific places, which 2.D.16 allows only while the danger there lasts.
