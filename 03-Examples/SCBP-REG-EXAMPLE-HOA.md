---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-HOA
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
  name: "[SUBDIVISION] Homeowners Association"
  legal_entity: "[SUBDIVISION] Homeowners Association, Inc. ([STATE] nonprofit corporation)"
  related_entities: "[MANAGEMENT COMPANY] (community manager); [COLLECTION LAW FIRM] (delinquency collection)"
  type: nonprofit
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: "[CITY]"
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Fines for rule violations"
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
  - power_id: P2
    short_name: "Liens and foreclosure"
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
  - power_id: P3
    short_name: "Architectural and use rules"
    category: rules_standards_or_prices
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
      floors: not_demonstrated
      evasion: conforming
  - power_id: P4
    short_name: "Regular and special assessments"
    category: fines_fees_or_charges
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
      floors: not_demonstrated
      evasion: conforming
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

> **Structural record.** Based on public sources and/or the preparer's own observation. People are referred to by role or title. This record describes structure, not guilt. Adjudicated or admitted facts are kept separate from allegations.

# [SUBDIVISION] Homeowners Association — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** A homeowners association for a single subdivision of about 290 single-family homes [EX], home to roughly 950 people [EX]. It maintains a pool, a clubhouse and common landscaping, and pays for them through mandatory assessments. It also writes and enforces rules about what owners may build, paint, park, post and rent; fines owners who break those rules; and records liens against homes for unpaid amounts, which it can enforce by foreclosure. Every owner becomes a member automatically on buying a home.

A2. **Legal basis.** A declaration of covenants, conditions and restrictions recorded against every lot by the original developer, the association's bylaws, and the [STATE] common-interest community statute. The declaration "runs with the land": it binds each later buyer without any separate agreement. The declaration renews itself automatically for successive periods of 10 years [EX] unless owners of a majority of lots record an amendment ending it.

A3. **Who controls it.** A board of 5 [EX] volunteer directors elected by the owners, one vote per lot. Owners can amend the declaration by a two-thirds vote of all lots [EX] and can remove directors by majority vote at a special meeting. The board hires a management company and a collection law firm.

A4. **Related entities.** [MANAGEMENT COMPANY] sends violation letters, tracks fines and collects assessments for a monthly fee. [COLLECTION LAW FIRM] handles accounts referred for collection, records liens and files foreclosure actions; its fees are charged to the owner's account. All figures here are the association's own unless stated.

A5. **Adoption.** not_adopted. The findings below are diagnostic: they record gaps against the Core Requirements and impose nothing [S1].

A6. **Powers found.**
- P1 — Fines for violations of the rules.
- P2 — Liens on homes for unpaid amounts, enforced by foreclosure.
- P3 — Architectural and use rules (approval of changes to homes, and rules on signs, parking, rentals and decorations).
- P4 — Regular and special assessments. Collection of unpaid assessments is part of P2.
- Not recorded: suspension of pool and clubhouse access (licensing_permits_or_access).

---

## Power P1 — Fines for rule violations

**B1. What it can do to people.** The board can fine an owner for any breach of the declaration or rules. A first fine is 25 currency units [EX]. A breach that continues after a cure date can be fined 10 currency units per day [EX], with no cap in the rules. Unpaid fines go on the owner's account, where they draw late fees of 15 currency units per month [EX] and interest at 18% a year [EX]. Once an account is referred to collection, the collection firm's fees are added as well.

**B2. Who and where.** All owners of the roughly 290 lots [EX]. Tenants, children and other household members live under the rules but are not members and cannot vote or contest fines; about 40% of residents are in this group [EX]. The fine is charged to the owner, who usually passes it on to a tenant under the lease.

**B3. Authority basis.** `direct`. The association imposes the fine itself, and state law lets it collect fines like assessments.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The developer wrote the fining power into the declaration; the elected board sets fine amounts by resolution [EX]. No independent body authorized it. 3.A.2 now offers a member-governed body a route: a panel chosen by lot from affected residents, excluding board members, the management company and anyone paid by the association, with appeal to an independent body. No such panel has been used [EX] | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | Declaration renews itself automatically every 10 years [EX]; the fining power has no end date of its own | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Court action reaches single fines; owners' amendment vote is not independent; see B5 [EX] | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Only a lawsuit at the owner's cost; the declaration shifts the association's legal fees to an owner who loses [EX] | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; deletion records (2.D.12–2.D.14, 7.6) | UNKNOWN | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9) | Declaration, rules and fine schedule are public in the land records and on the member portal [EX]; the declaration states plainly that it renews automatically and that only an owners' amendment ends it, so the absence of expiry is knowable (failure recorded under Maximum term) | conforming |
| Floors | See B6 (Part II) | Escalating charges; no independent hearing (B6) | not conforming |
| Evasion | Not split, outsourced, laundered, or using proxies (Part IV) | UNKNOWN whether collection-firm fees are set by the firm or the board | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Owner's lawsuit that the fine breaches the declaration or state statute | one_case | [STATE] trial court | independent | [EX] |
| 2 | Owner vote to amend the declaration and remove the fining power, two-thirds of all lots | whole_power | The owners as a body | not_independent — the owners are the association's members and its governing body | [EX] |
| 3 | Board resolution waiving or reducing a fine | one_case | The board | not_independent | [EX] |

Statement: *Can anything stop this power as a whole?* — `yes, [path 2] — holder not independent`. Path 2 can end the power, but it is held by the association's own members, so it does not meet the independence condition of 3.A.7.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Irreversible ecological threshold? | not_applicable — the power regulates conduct on house lots, not resource use | [EX] |
| Economic (2.B) | Essentials conditional? Obligations grow because people can't pay? Path out? | yes — a 25-unit fine grows through daily fines, late fees, 18% interest and collection fees when unpaid; no hardship route exists [EX] | [EX] |
| Agency (2.C) | Told plainly? Report harm without forms? Leave? | Notice letters are sent, but they do not explain how to challenge the fine outside the board [EX]; leaving means selling the home | [EX] |
| Force (2.D.1) | Force? | not_applicable — no force | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Challenge before someone independent? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | no — state law requires a hearing before the board itself, the body that imposed the fine [EX] | [EX] |
| Expression (2.D.9) | Punish or restrict lawful expression? News reporting or petitioning? Approval before publication? | Fines can attach to signs and decorations; see P3 [EX] | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? Reviewed? | UNKNOWN — enforcement depends on complaints from neighbors and has not been reviewed [EX] | [EX] |
| Identification (2.D.11) | Compelled identification? | not_applicable | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | UNKNOWN — the management company finds violations by driving the streets and photographing homes from the road [EX]. Looking at what anyone can see from a public street is not a search of the home; whether inspectors enter yards is not shown | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — fines restrict no one's movement; suspension of pool and clubhouse access is not recorded here (A6) |  |

**B7. Data.** Violation files hold owner names, addresses, photographs of homes and complaint records from neighbors. Retention period: UNKNOWN. Deletion records: NONE EXISTS. Complaints about the board are kept by the management company the board hires, not by an independent custodian.

**B8. Dependencies and evasion.** The management company drafts violation letters and the collection firm sets its own charges, which the declaration lets the association add to the owner's account. Whether the board reviews those charges is UNKNOWN.

**B9. Harms seen.** Economic: a typical case in this kind of association is an owner who misses a 25-unit fine [EX] during a hospital stay and owes several hundred currency units within six months [EX] — illustrative, not an adjudicated fact. Agency: tenants are fined through their landlord and cannot contest. Communicative: some owners describe fines as a response to criticism of the board — allegation only.

**B10. Decision inputs and oversight.** Fines start from neighbor complaints or a drive-through inspection by the management company. Which homes are inspected, and how often, is not published. A certified accountant audits the association's finances yearly [EX], but no one audits enforcement.

---

## Power P2 — Liens and foreclosure

**B1. What it can do to people.** When an account is past due by more than 90 days [EX], the association can record a lien against the home for unpaid assessments, fines, late fees, interest and collection costs. It can then sue to foreclose the lien and have the home sold. State law requires court foreclosure, but does not bar foreclosure where most of the balance is fines and fees [EX]. After a sale, any surplus over the debt and liens goes to the owner.

**B2. Who and where.** Any owner in the subdivision. About 6 liens a year are recorded [EX], and about one foreclosure action is filed every two years [EX]. Household members and tenants lose their home if it is sold.

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body, affected people heard, public record (3.A.1, 3.A.2) | Granted by the declaration and the state statute; the board decides each referral [EX]. No lot panel under 3.A.2 has been used | not conforming |
| Maximum term | Set expiry within 7.2 limits (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, independent (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested; one held outside (3.A.7, 3.C.1) | Court can refuse foreclosure in one case; nothing reaches the power (B5) [EX] | not conforming |
| Ending plan | Documented (3.A.9) | NONE EXISTS | not conforming |
| Remedy | Independent, funded (3.A.10) | NONE EXISTS beyond defending the lawsuit at the owner's cost | not conforming |
| Data limits | Retention stated; deletion recorded (2.D.12–2.D.14, 7.6) | Liens are public land records with no removal date after release [EX]. A recorded lien is a status-register entry while it encumbers the title, so it may be kept while it lasts, used only to confirm that status (2.D.12). Once released, it no longer establishes any continuing status, so the status-register rule no longer covers keeping it. The land records are kept by the county recorder, not the association; the association's own retention of account and lien files is UNKNOWN | compliance not demonstrated |
| Visibility | Ordinary person can learn the five facts (3.B.9) | The lien power is in the declaration, but the collection policy and the board's referral criteria are not published [EX] | compliance not demonstrated |
| Floors | See B6 | Home loss for small debts; escalation (B6) | not conforming |
| Evasion | Part IV | The collection firm, paid from the owner's account, decides when to escalate within a standing referral [EX] | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Defense in the foreclosure lawsuit (procedural defects, disputed balance) | one_case | [STATE] trial court | independent | [EX] |
| 2 | Owner amendment of the declaration | whole_power | The owners as a body | not_independent | [EX] |

The statute also lets an owner cure by paying the full balance before sale. That is compliance, not a stop path, so it is not listed.

Statement: *Can anything stop this power as a whole?* — `yes, [path 2] — holder not independent`. No path held outside the association can halt the power; a change to the state statute would be a new law, which does not count.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Threshold? | not_applicable | [EX] |
| Economic (2.B) | Essentials conditional? Escalation? Path out? | yes — housing is put at risk for a debt that grew because it was unpaid; collection and legal fees are added at each step, so the balance rises faster as the owner falls behind [EX]; the only path out is paying in full | [EX] |
| Agency (2.C) | Told plainly? Leave? | Notices are formal legal papers; no plain explanation or hardship contact is required [EX] | [EX] |
| Force (2.D.1) | Force? | not_applicable — eviction after sale is done by the sheriff, a separate power | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — a court must order the sale [EX] | [EX] |
| Expression (2.D.9) | Restricts expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? Reviewed? | UNKNOWN — not reviewed | [EX] |
| Identification (2.D.11) | Compelled identification? | not_applicable | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | yes — a home is sold only on a court's order after a foreclosure action [EX], and any surplus over the debt goes to the owner (B1) | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — removal of occupants after a sale needs a court order; loss of the home is recorded under Economic |  |

2.B.4 (economic reversibility) is also engaged: a forced sale ends ownership permanently, and under 3.D.2 a change of legal status is never containment.

**B7. Data.** Account histories, lien filings and court papers. Liens are public and stay in the land records permanently after release [EX]. Retention of the collection firm's files: UNKNOWN.

**B8. Dependencies and evasion.** The collection firm is paid from charges added to the owner's balance, so its income grows as the balance grows. Under 4.5 its conduct is treated as part of the association's power. The record found no sign of splitting the power to avoid limits.

**B9. Harms seen.** Economic and generational: loss of home equity for an owner whose original debt was small — illustrative pattern in this kind of association, not an adjudicated fact here. Non-participant: tenants and children displaced by a sale.

**B10. Decision inputs and oversight.** The trigger is days past due, from the management company's ledger. The board's referral policy is not published. No outside body audits referrals.

---

## Power P3 — Architectural and use rules

**B1. What it can do to people.** Owners need written approval before changing the outside of the home: paint color, fences, sheds, solar panels, play equipment, landscaping. The board also adopts use rules on signs, flags, holiday decorations, parking, home businesses and rentals. Unapproved changes must be removed at the owner's cost, and breaches are enforced through P1.

**B2. Who and where.** All lots and everyone living in the subdivision, about 950 people [EX]. The architectural committee reviews about 60 applications a year [EX].

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body (3.A.1, 3.A.2) | The declaration lets the board adopt rules by its own vote [EX]. No lot panel under 3.A.2 has been used | not conforming |
| Maximum term | Set expiry (3.E.1, 7.2) | NONE EXISTS for board rules; the declaration renews itself [EX] | not conforming |
| Harm thresholds | Published, measurable (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested; one held outside (3.A.7, 3.C.1) | Courts can void a rule that conflicts with the declaration or statute (B5) [EX] | not conforming |
| Ending plan | Documented (3.A.9) | NONE EXISTS | not conforming |
| Remedy | Independent, funded (3.A.10) | NONE EXISTS | not conforming |
| Data limits | Retention stated (2.D.12–2.D.14) | UNKNOWN | compliance not demonstrated |
| Visibility | Five facts knowable (3.B.9) | Rules, design guidelines and application forms are published to all owners; decisions are given in writing with reasons [EX]; that board rules have no end date and are changed by board or owner vote is stated in the declaration | conforming |
| Floors | See B6 | Expression partly protected by law [EX]; the sign rule is viewpoint-neutral on its face, but whether it is narrow and tied to the purpose of a shared space is not shown; whether the rental cap fits 2.D.16 is not shown (B6) | compliance not demonstrated |
| Evasion | Part IV | No outsourcing found; the volunteer committee decides [EX] | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Lawsuit that a rule exceeds the declaration or violates state or national law | one_practice | [STATE] trial court | independent | [EX] |
| 2 | National and state laws that override specific rules (flag display, certain antennas, solar panels, accessibility changes) | one_practice | National and state legislatures, enforced by courts | independent | [EX] |
| 3 | Owners' vote to repeal a rule | one_practice | The owners as a body | not_independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS** outside the association.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Threshold? | not_applicable | [EX] |
| Economic (2.B) | Essentials conditional? | no — but removal orders can impose large costs, enforced through P1 [EX] | [EX] |
| Agency (2.C) | Told plainly? Leave? | yes — written decisions with reasons [EX]; leaving means selling | [EX] |
| Force (2.D.1) | Force? | not_applicable | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | no — appeal goes to the full board [EX] | [EX] |
| Expression (2.D.9) | Restricts lawful expression? News reporting or petitioning? Approval before publication? | UNKNOWN — political and other signs are limited to one sign of a set size for 30 days before an election [EX]; national law protects flag display. 2.D.9 permits narrow, published rules tied to a space's purpose, applied without regard to viewpoint and open to challenge. The rule is published and applies whatever a sign says, so it is viewpoint-neutral on its face. Challenge lies only to the full board, or to a court on legal grounds. Whether it is narrow and tied to a space's purpose is not shown: it reaches owners' own homes, not only common areas. How it has been applied has not been reviewed. Signs fall under the use rule, not the prior-approval process [EX] | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? | UNKNOWN — rules on home businesses and occupancy can fall unequally on larger or multigenerational households; not reviewed [EX] | [EX] |
| Identification (2.D.11) | Compelled identification? | not_applicable | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — reviews rely on drawings and photographs the owner submits [EX]; enforcement checks are recorded under P1 | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | UNKNOWN — the rental rule caps leased homes at 15% of lots, with a waiting list [EX], which decides whether a tenant can live in the subdivision. Whether a property-use rule of this kind restricts where people may live under 2.D.16 is for independent interpretation (7.3) | [EX] |

**B7. Data.** Applications with drawings and photographs of homes; owner contact data. Retention: UNKNOWN.

**B8. Dependencies and evasion.** None found.

**B9. Harms seen.** Communicative: sign limits around elections. Economic: removal orders for unapproved fences or sheds. Both are illustrative patterns, not adjudicated facts here.

**B10. Decision inputs and oversight.** Published design guidelines, plus the committee's judgment on "harmony with the community" [EX], which is not defined. No outside review.

---

## Power P4 — Regular and special assessments

**B1. What it can do to people.** The association charges every lot a share of the cost of shared property and services. It needs no rule breach to do this.
- Regular assessment: the board adopts a yearly budget and sets the assessment from it, about 1,200 currency units per lot a year [EX], paid quarterly.
- Special assessment: the board can levy a one-time charge for repairs or other costs outside the budget. Up to 5% of the yearly budget [EX] it may do so by its own vote. Above that, the declaration requires approval by a majority of all lots [EX]. Last year owners approved a special assessment of 2,500 currency units per lot [EX] for pool and clubhouse repairs.
- An unpaid assessment is a debt on the owner's account. Its collection, late charges, lien, and foreclosure are recorded under P2, not here.

**B2. Who and where.** All owners of the roughly 290 lots [EX]. Tenants usually bear assessments through rent but cannot vote on the budget or on special assessments; about 40% of residents are not members [EX]. Owners on fixed incomes face special assessments as large, unplanned costs.

**B3. Authority basis.** `direct`. The association imposes the charge itself, under the declaration and the state statute.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The developer wrote the assessment power into the declaration; the board adopts the budget at an open meeting after notice to owners [EX], and owners vote on large special assessments. Owners are the association's own members, so neither is independent. No lot panel under 3.A.2 has been used [EX] | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | The declaration renews itself automatically every 10 years [EX]; the assessment power has no end date of its own | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | The vote requirement above 5% of the budget [EX] limits board discretion, but it is a procedure, not a harm threshold. The declaration and board policies set no threshold on delinquency or hardship that triggers review [EX] | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | A court can void an assessment that exceeds the declaration or statute; owners can reject a budget or amend the declaration, but they are not independent (B5) [EX]. The only whole-power path is held by the owners; the legislature's general power to change the statute does not count | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | The declaration says common areas pass to the city on dissolution if it accepts them [EX]. Whether the city would accept, and how maintenance would be paid for, is not shown | compliance not demonstrated |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Only a lawsuit at the owner's cost; the declaration shifts the association's legal fees to an owner who loses [EX] | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; deletion records (2.D.12–2.D.14, 7.6) | Assessment ledgers are kept by the management company; retention UNKNOWN | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9) | The budget, the reserve study, and every assessment amount are sent to all owners each year, with past years' amounts [EX]; the declaration states plainly that the power renews automatically | conforming |
| Floors | See B6 (Part II) | Hardship relief is at the board's discretion, with no written policy; whether the burden falls unequally is not reviewed (B6) | compliance not demonstrated |
| Evasion | Not split, outsourced, laundered, or using proxies (Part IV) | Board minutes for the last 5 years [EX] show no special assessment split into smaller charges to stay under the vote requirement | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Owner's lawsuit that an assessment exceeds the declaration or state statute | one_practice | [STATE] trial court | independent | [EX] |
| 2 | Owners reject the yearly budget by a majority of all lots, under the state statute; the prior budget then continues [EX] | one_practice | The owners as a body | not_independent | [EX] |
| 3 | Owners vote down a special assessment above the 5% limit [EX] | one_practice | The owners as a body | not_independent | [EX] |
| 4 | Owner amendment of the declaration, two-thirds of all lots [EX] | whole_power | The owners as a body | not_independent | [EX] |

Statement: *Can anything stop this power as a whole?* — `yes, [path 4] — holder not independent`. Path 4 is held by the association's own members. No path held outside the association can halt the assessment power; a change to the state statute would be the general ability to pass a new law, which does not count. Any stop would need an ending plan that keeps shared property maintained and insured.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Threshold? | not_applicable | [EX] |
| Economic (2.B) | Essentials conditional? Obligations grow because people can't pay? Path out? | partly — an assessment is an ordinary scheduled charge for shared costs, not escalation (2.B.2); growth from late charges and collection is recorded under P2. A payment plan is available only at the board's discretion, with no written hardship policy [EX] | [EX] |
| Agency (2.C) | Told plainly? Leave? | yes — owners get the budget and a plain notice of each special assessment 30 days [EX] before it is due; leaving means selling the home | [EX] |
| Force (2.D.1) | Force? | not_applicable — no force | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | partly — owners can be heard at the budget meeting, which is not independent, and can sue in court at their own cost [EX] | [EX] |
| Expression (2.D.9) | Restricts expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? Reviewed? | UNKNOWN — every lot pays the same amount whatever its size or the household's income [EX]; the effect on low-income and fixed-income owners has not been reviewed | [EX] |
| Identification (2.D.11) | Compelled identification? | not_applicable | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — the charge itself takes nothing; any lien or sale is under P2 | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Owner names, lot numbers, payment history, and payment-plan requests, kept by the management company. Retention: UNKNOWN.

**B8. Dependencies and evasion.** Assessments are almost all of the association's income [EX]. The management company bills and collects them. Collection of unpaid assessments uses the same collection firm and lien process as P2; that machinery is recorded once, under P2.

**B9. Harms seen.** Economic: owners on fixed incomes describe the 2,500-unit special assessment [EX] as forcing them to borrow or to sell — allegation in public comment at the owners' meeting. No adjudicated harm.

**B10. Decision inputs and oversight.** The budget, and a reserve study by an outside engineer every 3 years [EX]. A certified accountant audits the association's finances yearly [EX]. No outside body reviews whether assessment levels or hardship decisions are fair.

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited (institutional figures in this example are illustrative [EX]) | BPF: Core Requirements v1 | 2.B.2, 2.B.4, 2.D.12, 3.D.2, 7.2 | | yes |

---

## PART D — Honesty assertions

- [x] Every number has a source tag (illustrative figures are tagged [EX]).
- [x] Nothing is presented as a verified fact about a real institution. This is a fictional worked example. `UNKNOWN` means the scenario does not establish the answer. `NONE EXISTS` is used only where the scenario explicitly establishes absence, not because a safeguard is assumed to be uncommon for this type of institution.
- [x] Public sources and first-hand observation only. Nothing private, leaked, or speculative.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] This is a worked example made in good faith, as a structural description, not an accusation.

Preparer: BPF examples working group (worked example).

---

## Teaching notes (non-binding)

- The clearest 2.B.2 case in the set: a 25-unit fine [EX] that is not paid becomes daily fines, late fees, interest and collection costs, and finally a lien and foreclosure. Each step is lawful on its own; the escalation is the finding (2.B.2, 2.B.4).
- One institution, four powers (3.A.1). Fines, liens, rules and assessments have different stop paths and different harms, so each gets its own section.
- The power to create a debt and the power to enforce that debt against someone's home are distinct powers, even when the same institution holds both. P4 records the assessment; P2 records the lien and foreclosure that can follow, so the enforcement machinery is counted once.
- For P2 and P4, the only whole-power path is the owners' own vote, and a change to the state statute would be a new law, which does not count. When every whole-power path is held by a body that is not independent, the Stop paths finding is not conforming (3.A.7).
- Assessments pay for real shared costs, and compulsory charges are not a violation in themselves. P4's findings follow the scenario: published budgets earn a conforming visibility row, and owner votes on large special assessments limit the board, though owners are not independent (3.A.2, 3.A.7). A hardship route that exists only at the board's discretion leaves the Floors finding not demonstrated.
- Automatic renewal is not renewal. A declaration that renews itself every 10 years [EX] still has no maximum term under 3.E.1 and 7.2, because renewal must be a new decision on evidence (3.E.2).
- Owners voting to amend the declaration can end a power, but they are the institution's own members, so that path is not independent (3.A.7, Definitions: Independent).
- A hearing before the board that imposed the fine is not due process under 2.D.5; court foreclosure is, for P2.
- Paying the balance to stop a foreclosure is compliance, not a stop path (Form B5; 3.C.1).
- A collection firm paid out of the charges it adds is part of the power under 4.5 and is listed as an evasion concern under Part IV.
- Some rows are conforming: P1 and P3 rules are public and P3 decisions come with written reasons (3.B.9). Visibility is judged on whether the facts are knowable; a plainly stated absence of expiry fails Maximum term, not Visibility.
- A member-governed body may be authorized by a panel chosen by lot from affected residents, excluding the board and anyone paid by the association, with appeal to an independent body (3.A.2). No panel has been used, so all four authorization rows stay not conforming; the route exists.
- A lien is a status-register entry while it encumbers the title (2.D.12). Once released, the exception ends; the county recorder's permanent land records are the recorder's power, not the association's. Under 2.D.9, a sign rule that is viewpoint-neutral on its face is not enough without narrowness, a purpose tied to the space, and a real challenge route, so P3's expression answer stays UNKNOWN.
- Most of this association's powers raise no 2.D.15 problem: violations are found from the street, and a foreclosure sale needs a court order with any surplus going to the owner. A rental cap shows where 2.D.16 may reach a property-use rule; the record logs it for interpretation (7.3) rather than deciding it.
