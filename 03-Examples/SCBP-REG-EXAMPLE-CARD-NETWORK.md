---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-CARD-NETWORK
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
  name: "[CARD NETWORK]"
  legal_entity: "[CARD NETWORK CORPORATION]"
  related_entities: "[ACQUIRING BANKS] (sign up merchants under network rules); [ISSUING BANKS] (issue cards under network rules); [TERMINATED-MERCHANT LIST] (shared list run by the network)"
  type: private_company
  country: "[COUNTRY]"
  region: NONE
  locality: NONE
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Prohibited and restricted merchant categories"
    category: licensing_permits_or_access
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
  - power_id: P2
    short_name: "Interchange schedule and acceptance rules"
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
      floors: not_demonstrated
      evasion: not_demonstrated
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [CARD NETWORK] — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** A private company that runs a card payment network. It does not lend or hold deposits. It writes the operating rules that banks must follow to issue its cards or to let merchants accept them, sets default fees that pass between banks on every purchase, and runs the systems that approve and settle payments. Through those rules it decides which kinds of lawful business may take card payments and on what terms. It is one of several card networks in [COUNTRY]; most merchants accept the cards of all of them.

A2. **Legal basis.** Incorporated under [STATE] corporate law. Its power over banks and merchants rests on contract: banks agree to the operating rules to join the network, and acquiring banks pass the rules on to merchants. National banking, anti-money-laundering and sanctions laws apply. Antitrust law applies to its rules. A federal regulator caps the default fee on debit cards issued by large banks.

A3. **Who controls it.** A board elected by shareholders. Rule changes are made by management and announced to member banks; there is no vote by merchants or cardholders.

A4. **Related entities.**
- [ACQUIRING BANKS] sign up merchants, apply the network's category rules, and terminate merchants when the rules require it.
- [ISSUING BANKS] receive the interchange fee set under P2.
- [TERMINATED-MERCHANT LIST] is a shared list the network runs; acquirers must add terminated merchants and must check it before signing new ones.
- This example deliberately gives no cardholder count or market share. Those figures would point to one real network.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — Prohibited and restricted merchant categories (licensing_permits_or_access, indirect_a).
- P2 — Interchange schedule and acceptance rules (rules_standards_or_prices, indirect_b).
- Not recorded: fines on member banks for rule breaches. That power is `direct` over the banks, and would be its own record.
- Not recorded: real-time fraud declines; the dispute and chargeback system.

---

## PART B — One section per power

## Power P1 — Prohibited and restricted merchant categories

**B1. What it can do to people.** The operating rules list business categories that may not accept the network's cards at all, and higher-risk categories that need extra monitoring, higher reserves and higher fees. When a merchant falls into a prohibited category, or a high-risk merchant passes a chargeback or complaint limit, the acquirer must terminate it and add its owners to [TERMINATED-MERCHANT LIST]. A listed owner usually cannot open a card account at any acquirer, including for an unrelated new business. Some lawful businesses — certain adult content, some sellers of lawful regulated goods, some fundraising and crowdfunding services — have been cut off this way.

**B2. Who and where.** Merchants that accept cards in [COUNTRY]: over a million [EX] businesses. About 20,000 [EX] merchant principals added to the list per year. Non-participants: customers and workers of terminated businesses; creators paid through platforms that lose card access.

**B3. Authority basis.** `indirect_a_operationalized`. The network does not terminate merchants itself; acquirers do. But acquirers terminate because the network's rules require it.
- Who relies on it: [ACQUIRING BANKS], whose decisions to refuse or terminate a merchant bind that merchant.
- Causation Ladder: tier 1, formal control by binding directive [S1]. The operating rules oblige acquirers to refuse prohibited categories and to terminate and list merchants over set limits, with fines for failure.
- Material cost: a business that cannot accept cards loses most of its sales; the cost is material.
- Both are in scope: the network for its rule, each acquirer for its own decision (Authority definition).

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. The network adds or changes categories on its own, sometimes after public pressure. | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS for harm to merchants. The chargeback ratio that triggers termination, 1% [EX], is a limit on merchants, set by the network. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | See B5 | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS. Merchant contracts bar most claims; the network has no contract with the merchant. | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Owners stay on the list for several years [EX], then drop off. Deletion record UNKNOWN. An entry on the list is a sanction listing against a person, not an accountability record, so it follows 2.D.12 and 2.D.6 (2.D.14): a retention period stated and justified for each reason code, deletion when the purpose ends, and the owner's right to ask for earlier deletion unless a hold applies. The period is not stated per reason code [EX], and an owner can ask only the acquirer that listed them, and only on the ground of a wrong listing. | not conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Core rules are published; the guidance that assigns higher-risk categories is not. Merchants are often told only "network rules". | not conforming |
| Floors | See B6 (Part II) | See B6 | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Acquirers say the network requires the termination; the network says the acquirer decided. Neither answers for the result (4.1). | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Antitrust suit against a category rule that excludes competitors | one_practice | a federal court | independent | [EX] |
| 2 | Bank supervisor guidance against terminating whole categories without individual review | one_practice (at supervised acquirers) | national bank supervisor | independent | [EX] |
| 3 | Removal from the list for an owner wrongly added | one_case | the acquirer that added the owner | not_independent | [EX] |
| 4 | State law barring payment discrimination against one lawful category of business in [STATE] | one_practice (in [STATE] only) | [STATE] attorney general | independent | [EX] |

Path 2 is guidance and not binding on the network itself. Path 4 protects one category in one state; it does not reach other lawful businesses.

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Under current law no body can review or stop the network's category rules as such.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes — card acceptance is an indispensable means of ordinary commerce; listing bars an owner from it for years, and reserves held back from terminated merchants can exceed their remaining sales | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — terminations often give no reason; owners learn of listing only when refused elsewhere | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 hours; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical care | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | no — no independent forum; an organization may claim this floor for its own property and standing | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | yes — lawful publishers and fundraising services have lost card access because of lawful content | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — no review | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | no — owner identification is a condition of a regulated activity the owner chooses | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | UNKNOWN — the rules let an acquirer hold back a terminated merchant's settlement funds as a reserve for up to 180 days [EX], with no judicial officer's approval. Most merchants are organizations, which may claim only due process (Definitions: Person); for owners trading as sole proprietors the hold is a seizure of a person's property, and whether the whole reserve is returned when the chargeback period ends is not shown | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

Leverage over essentials (2.B.3): whether the network has used card access to obtain changes unrelated to payment risk is an allegation only, recorded for watching.

**B7. Data.** [TERMINATED-MERCHANT LIST] holds owners' names, addresses, tax and ID numbers, and the reason code. Kept several years [EX]. Visible to every acquirer. The owner cannot see the entry except through the acquirer. Because the list is a sanction listing that bars a person from ordinary commerce for years, 2.D.6 also applies: the listing must not keep a person from moving beyond a past termination once its purpose has ended.

**B8. Dependencies and evasion.** Acquirers depend on network membership and so follow its rules; the network depends on acquirers to carry out terminations. Other networks have similar category rules; a finding that the networks act as one authority system (4.2) would need tier 5 evidence, such as shared written criteria. This example has only tier 7 (similar outcomes), which supports a recorded concern only.

**B9. Harms seen.**
- economic, communicative: lawful publishers cut off after a category change; allegation in publisher complaints [EX].
- economic: owners listed for reasons later found wrong; allegation in merchant complaints [EX].
- non_participant: creators who lost income when a platform lost card access; allegation.

**B10. Decision inputs and oversight.** Category codes, chargeback and fraud ratios, complaint counts and higher-risk category reviews. Ratios are published; the category criteria are not (5.3). No outside body audits category decisions (5.1).

---

## Power P2 — Interchange schedule and acceptance rules

**B1. What it can do to people.** It sets the default fee that a merchant's bank pays the cardholder's bank on each purchase, plus the network's own fees. It also sets acceptance rules, such as requiring merchants that take one kind of its cards to take all kinds, and limits on adding a surcharge. Merchants pass these costs into prices, so every buyer pays them, including people who pay in cash.

**B2. Who and where.** Every merchant that accepts the cards and every buyer from them in [COUNTRY]. Interchange on credit cards runs about 2% [EX] of the sale. Non-participants: cash buyers and people without cards, who pay the higher prices but receive no card rewards.

**B3. Authority basis.** `indirect_b_directive_control`. Banks may in principle negotiate other rates, but almost none do; the network's schedule is the default that applies. At its scale, a default price paid on every card purchase channels what merchants charge and how people pay, as an order would (Authority definition, limb (b)) [S1].
- No Causation Ladder tier is needed: the finding rests on the practical effect of the network's own schedule [S1].
- Not indirect_a: no single party builds the schedule into one binding decision about an identified person; the effect is market-wide.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS for credit cards. For debit cards from large banks, the regulator's cap limits the price but does not authorize the power. | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | The debit cap is a published, measurable ceiling set by an independent regulator, about 0.2% [EX] plus a fixed amount. Nothing comparable for credit cards or for other harms. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | See B5 | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Merchant antitrust class actions have produced damages settlements [EX]; routes are courts. Financial assurance: UNKNOWN. | compliance not demonstrated |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Setting a fee schedule collects no personal information; transaction data belongs to unrecorded powers. | not applicable |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Rate tables are published; how rates are set is not. Buyers are not shown the fee in the price. | not conforming |
| Floors | See B6 (Part II) | See B6 | compliance not demonstrated |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Allegations that incentives steer debit routing away from competing networks to avoid the cap's competition rules; not adjudicated. | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Regulator's debit interchange cap | one_practice (debit cards of large banks) | federal banking regulator | independent | [EX] |
| 2 | Antitrust judgment or consent decree on an acceptance rule | one_practice | a federal court; the national antitrust agency | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Paths 1 and 2 limit parts of the price or the rules; none can stop the network from setting the schedule.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | UNKNOWN — the fee raises prices of essentials for everyone; whether it shifts cost from rewards-card holders to lower-income cash buyers at a level that harms basic functioning is studied but disputed [EX] | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no — buyers are not told the fee exists; merchants can leave only by refusing cards | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 hours; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical care | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | yes, through antitrust courts, slowly and at high cost | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | no evidence found | |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — no review | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | not_applicable — fee setting identifies no one | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — fee setting searches and seizes nothing |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** None collected by this power itself. Transaction data used to price categories belongs to the network's processing, not recorded here.

**B8. Dependencies and evasion.** Issuing banks depend on interchange revenue to fund rewards; that dependency makes the schedule hard to lower (3.B.7). Routing incentives are an allegation under review, recorded under B4.

**B9. Harms seen.**
- economic: merchants' acceptance costs; antitrust class actions settled without admission [EX].
- non_participant: cash buyers paying higher prices; estimate in economic research, not adjudicated.

**B10. Decision inputs and oversight.** Rate tables are published by category and card type. The method and the data used to set them are not (5.3). Antitrust agencies can demand data in an investigation; nobody audits routinely (5.1).

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures and definitions cited | BPF: Core Requirements v1 | Definitions (Authority, Causation Ladder, Person); 2.B.3; 2.D.9 | | yes |

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

- A rule that obliges another party to decide is indirect_a at tier 1. The acquirer terminates the merchant, but the network's binding rule is the determinant, and both are in scope (Authority definition (a); Definitions: Causation Ladder; 4.3(a)).
- A default price paid on every purchase is indirect_b. The finding rests on the practical effect at scale and needs no tier (Authority definition (b); 4.3).
- One institution can hold all three bases. Fines on member banks are direct and would be their own record (3.A.1).
- When the network and the acquirer each say the other decided, nobody answers for the result. That is an evasion finding, because responsibility is shared along the chain (4.1).
- Cutting lawful businesses off from card payments is recorded under the expression floor and the essentials floor. An organization may itself claim only due process; its owners and customers are persons (2.D.9, 2.B.3, Definitions: Person).
- A regulator's price cap is a real, independent, one-practice stop path and a partial threshold. It is not an authorization of the power (3.A.2, 3.A.5).
- Similar category rules across networks are tier 7 evidence only. A finding that the networks form one authority system would need shared written criteria, which is tier 5 (4.2).
- Leave out any figure that would identify a real firm, and say so in the record, as A4 does here.
- Rule 2.D.14: a shared list of sanctioned merchants is a listing against members of the public, not an accountability record. It follows 2.D.12 and 2.D.6, with a stated and justified retention period, deletion when the purpose ends, and a right to ask for earlier deletion unless a hold applies. It does not get 10 years [S1] of independent custody. P1's data row stays not conforming, now because retention is not justified per reason code and owners have no route to ask for deletion.
- Reserves held back from a terminated merchant are a 2.D.15 seizure question only for owners who are persons; an organization may claim due process alone (Definitions: Person). The answer stays UNKNOWN until it is shown that reserves are returned in full when their purpose ends.
