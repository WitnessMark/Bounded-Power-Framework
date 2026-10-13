---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-CITY-WATER-UTILITY
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
  name: "[CITY] Water Department"
  legal_entity: "[CITY] (municipal corporation), acting through its Water Department"
  related_entities: "[CITY] City Council (sets rates and policy); [BILLING VENDOR] (billing and shutoff-list software); [COLLECTION AGENCY]; [COUNTY] Tax Collector (enforces certified liens)"
  type: government
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: "[CITY]"
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Setting water and sewer rates"
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
      remedy: not_demonstrated
      data_limits: not_applicable
      visibility: conforming
      floors: not_demonstrated
      evasion: not_demonstrated
  - power_id: P2
    short_name: "Shutoff of water service for non-payment"
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
      remedy: not_conforming
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_conforming
      evasion: not_demonstrated
  - power_id: P3
    short_name: "Unpaid bills certified as property liens"
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
      visibility: not_conforming
      floors: not_conforming
      evasion: not_conforming
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [CITY] Water Department — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** The city-owned utility that treats and delivers drinking water and collects sewage for everyone in the city. It is the only provider: private wells are prohibited inside city limits [EX], so a household cannot switch suppliers or leave without moving. It sets prices, shuts off water when bills go unpaid, and turns unpaid balances into liens on the property.

A2. **Legal basis.** The [CITY] charter and municipal code [EX]; [STATE] law requiring published notice and a hearing before rate increases [EX]; [STATE] utility shutoff statute for notice and payment-plan rules [EX]; national safe-drinking-water law for water quality.

A3. **Who controls it.** The City Council sets rates and policy by ordinance; a Director appointed by the Mayor runs the department [EX]. The state utility regulator does not regulate rates of city-owned utilities [EX].

A4. **Related entities.** A billing vendor's software generates the monthly shutoff list [EX]; a collection agency pursues closed accounts; the county Tax Collector enforces liens the city certifies. Figures are the department's unless marked.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — Setting water and sewer rates.
- P2 — Shutoff of water service for non-payment (assigned teaching point).
- P3 — Unpaid bills certified as property liens.
- Not recorded: water-quality operations; meter-tampering penalties; drought-use restrictions.

**Minimum essential function (3.C.5).** Water delivery is not itself a power listed here; it is the function that the powers above attach conditions to. If P2 were paused or stopped, shutoffs end and water keeps flowing, with no Floor problem. If P1 or the department's billing powers expired with no successor, 3.C.5 requires that treatment and delivery continue as the minimum essential function. A controller with no stake must be named within 7 days, a successor authorized within 12 months, and the arrangement reviewed every 90 days [S1]; the department itself may never run it. No such arrangement exists in current law [EX]. The nearest thing is the state drinking-water regulator's power to seek a court-appointed receiver, and it applies only to water-safety failures [EX]. That is also the only plan under 3.B.2 for moving a single unavoidable provider to other control.

---

## Power P1 — Setting water and sewer rates

**B1. What it can do to people.** The Council sets the fixed monthly charge and the price per unit of water and sewage for every account. Nobody in the city can avoid paying it and still have running water. The average residential bill is 95 currency units a month [EX], up 60% over 10 years [EX].

**B2. Who and where.** About 180,000 accounts [EX] serving about 600,000 residents [EX]. Tenants pay through rent or sub-metering without being account holders.

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The Council, which owns the utility and receives transfers from it, sets rates after a public hearing [EX]; not independent. No panel chosen by lot from the people affected, with appeal to an independent body, authorizes the power (3.A.2) | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | Rate ordinances run until replaced [EX]: NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | The rate study sets an affordability goal of 4% of median household income [EX], with no stop consequence; low-income households pay about 9% [EX] | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | A voter referendum can block one increase [EX]; never used; whole-power path NONE EXISTS | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS [EX] | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Courts have ordered refunds where rates exceeded the cost of service [EX]; no route for affordability harm | compliance not demonstrated |
| Data limits | Retention periods (2.D.12–2.D.14, 7.6) | Rate-setting uses aggregate usage data [EX] | not applicable |
| Visibility | Knowable to an ordinary person (3.B.9). Decision inputs declared (5.3) | Rate schedules and the cost-of-service study published [EX]; the municipal code plainly shows rate ordinances have no end date and no renewal [EX], so the absence is knowable (failure recorded under Maximum term) | conforming |
| Floors | See B6 (Part II) | No income-based rate; affordability effects unreviewed [EX] | compliance not demonstrated |
| Evasion | Part IV | 8% of water revenue is transferred to the general fund [EX]; whether this routes a general tax through an essential-service charge is UNKNOWN | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Lawsuit that a rate exceeds the cost of service [EX] | one_practice | Trial court | independent | [EX] |
| 2 | Voter referendum on a rate ordinance [EX] | one_practice | Voters | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. A new ordinance by the Council does not count: it is a new law, and the Council is the utility's own governing body. A referendum (path 2) reaches one ordinance, not the power to set rates; it has never been used [EX].

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Irreversible ecological threshold? | not_applicable — pricing only; withdrawals are under state permit [EX] | [EX] |
| Economic (2.B) | Essentials conditional? Escalating? Path out? | UNKNOWN — a 20% discount for low-income households [EX] is funded from a small voluntary-donation program [EX]; 4% of eligible households are enrolled [EX] | [EX] |
| Agency (2.C) | Plain explanation? | yes — bills itemize charges [EX] | [EX] |
| Force (2.D.1) | — | not_applicable | — |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no detention | — |
| Emergency medical care (2.D.2) | Treatment without consent only on incapacity plus imminent harm? | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — court [EX] | [EX] |
| Expression (2.D.9) | — | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? Reviewed? | UNKNOWN — no review | [EX] |
| Identification (2.D.11) | — | not_applicable — see P2 | — |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — rate setting searches and seizes nothing |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Aggregate consumption and cost data only for this power [EX].

**B8. Dependencies and evasion.** Bond covenants require rates high enough to cover debt payments 1.25 times [EX]; that obligation outlasts any term and constrains future rate decisions (3.A.8). The general-fund transfer is recorded under Evasion.

**B9. Harms seen.**
- economic — low-income households pay about 9% of income for water and sewer [EX] (estimate in the city's own rate study).

**B10. Decision inputs and oversight.** The cost-of-service study and bond covenants are published [EX] (5.3). The city auditor audits the department [EX] but is appointed by the Council.

---

## Power P2 — Shutoff of water service for non-payment

**B1. What it can do to people.** When an account is 45 days [EX] past due with a balance over 150 [EX], the department shuts off water at the meter. Restoring service requires paying the balance or entering a plan, plus a reconnection fee of 75 [EX] and a deposit of 200 [EX]. Opening a new account requires government photo ID [EX].

**B2. Who and where.** 7,800 shutoffs last year [EX]. Non-participants: everyone in the household, and tenants in master-metered buildings whose landlord does not pay. They can open accounts of their own only with the landlord's consent [EX], and notice to them is by a posted notice only [EX].

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent authorizing body, public record (3.A.1, 3.A.2) | Council ordinance and state notice statute [EX]; NONE EXISTS as a 3.A.2 decision | not conforming |
| Maximum term | Expires on a set date (3.E.1, 7.2) | NONE EXISTS [EX] | not conforming |
| Harm thresholds | Published, measurable thresholds (3.A.5) | Annual shutoff counts reported [EX]; no threshold or stop condition: NONE EXISTS | not conforming |
| Stop paths | Tested paths, at least one independent (3.A.7, 3.C.1) | Medical delay, hearing, and court affect single cases [EX]; whole-power path NONE EXISTS | not conforming |
| Ending plan | Documented ending (3.A.9) | NONE EXISTS [EX] | not conforming |
| Remedy | Independent, funded remedy (3.A.10) | Wrongful shutoffs are refunded the reconnection fee only [EX]; no independent route: NONE EXISTS | not conforming |
| Data limits | Retention periods; deletion records (2.D.12–2.D.14, 7.6) | Payment history kept 7 years [EX] and sent to a collection agency that reports to credit bureaus [EX]; deletion records UNKNOWN | compliance not demonstrated |
| Visibility | Knowable to an ordinary person (3.B.9) | Shutoff policy, protections, and counts published [EX]; the code plainly states the policy has no end date [EX] | conforming |
| Floors | See B6 (Part II) | Water is withheld to compel payment (2.B.1, 2.B.3); whether the photo-ID rule is the least intrusive means is not shown (2.D.11) [EX] | not conforming |
| Evasion | Part IV | The vendor's software applies the shutoff criteria [EX]; whether its rules match the published policy is UNKNOWN (5.3) | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | A clinician's medical-need letter delays shutoff for 21 days [EX], renewable once | one_case | Treating clinician | independent | [EX] |
| 2 | Hearing before a department hearing officer | one_case | Department employee | not_independent | [EX] |
| 3 | State statute bars shutoffs on weekends and holidays [EX] and requires a 9-month payment plan for households enrolled in a means-tested benefit [EX] | one_practice (timing and plan only) | State law, applied by the department | not_independent | [EX] |
| 4 | Court action | one_case | Trial court | independent | [EX] |
| 5 | County health officer may order service restored where a household includes an infant or a person with a medical need [EX] | one_case | County health officer | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Every path reaches one case or one practice; only a new ordinance or statute could end shutoffs, and neither counts.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | — | not_applicable | — |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? | yes — water is withheld to compel payment (2.B.1, 2.B.3); late fees of 10% [EX], the reconnection fee, and the deposit grow because a household cannot pay (2.B.2) | [EX] |
| Agency (2.C) | Told plainly? Report harm? Leave? | partly — notice 10 days [EX] before and a door notice 48 hours [EX] before, in English and three other languages [EX]; no exit, because private wells are prohibited [EX] | [EX] |
| Force (2.D.1) | — | not_applicable — meter lock only | — |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no detention | — |
| Emergency medical care (2.D.2) | Treatment without consent only on incapacity plus imminent harm? | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | partly — hearing officer not independent; court available [EX] | [EX] |
| Expression (2.D.9) | — | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? Reviewed? | UNKNOWN — 70% of shutoffs fall in four of 15 council districts [EX]; no review | [EX] |
| Identification (2.D.11) | Compelled identification without cause? | UNKNOWN — 2.D.11 permits verifying the identity of a person opening an account in their own name, a claimed entitlement, by the least intrusive means that works, with a non-biometric way offered and no other use. A photo-ID document check is non-biometric. Photo ID is required to open an account [EX]; whether other proof is accepted from people without photo ID, and whether ID details are kept out of the payment history sent to the collection agency, is not shown | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — water is shut off at the meter in the public right of way [EX]; staff do not enter homes | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Name, address, ID number, payment history, and shutoff history [EX]. Payment data goes to a collection agency, which reports closed accounts to credit bureaus [EX]; under 4.5 those reports are part of the department's power.

**B8. Dependencies and evasion.** Billing vendor and collection agency [EX]. The shutoff list is generated automatically each month [EX]; crews act on it without individual review.

**B9. Harms seen.**
- bodily — 3 complaints to the county health department of households without water for more than 30 days [EX] (allegation).
- economic — 2.1 million currency units of late and reconnection fees last year [EX] (admitted in the department's annual report).
- non_participant — 41 master-metered buildings shut off for landlord non-payment [EX] (admitted).

**B10. Decision inputs and oversight.** Published criteria are days past due and balance [EX]; the vendor's actual rule set is not published [EX] (5.3). No outside audit of shutoffs [EX].

---

## Power P3 — Unpaid bills certified as property liens

**B1. What it can do to people.** Each year the Council certifies unpaid balances over 250 [EX] to the county tax roll. The balance becomes a lien on the property, collected with property tax, and bears the county's delinquency interest of 1% a month [EX]. If it stays unpaid, the county can sell the property for taxes. A tenant's unpaid bill becomes the owner's lien.

**B2. Who and where.** 2,900 parcels certified last year [EX], many owned by older homeowners with fixed incomes [EX].

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent authorizing body (3.A.1, 3.A.2) | Council resolution each year [EX] | not conforming |
| Maximum term | Expires on a set date (3.E.1, 7.2) | NONE EXISTS [EX] | not conforming |
| Harm thresholds | Published thresholds (3.A.5) | NONE EXISTS [EX] | not conforming |
| Stop paths | Tested paths, at least one independent (3.A.7, 3.C.1) | Council hearing on the certification list [EX]; court; single cases only | not conforming |
| Ending plan | Documented ending (3.A.9) | NONE EXISTS [EX] | not conforming |
| Remedy | Independent, funded remedy (3.A.10) | NONE EXISTS [EX] | not conforming |
| Data limits | Retention periods (2.D.12–2.D.14) | Lien and release are recorded in permanent land records [EX]. Land title records may be kept as status registers while the title lasts, with access limited to confirming it (2.D.12). The land records are public [EX]; whether use of lien entries is limited to confirming title, and whether a released lien stays only as part of the title or remains searchable as a debt record past the 20-year [S1] ceiling, is UNKNOWN | compliance not demonstrated |
| Visibility | Knowable (3.B.9) | Certification notice published in a newspaper only [EX]; counts not published | not conforming |
| Floors | See B6 (Part II) | Interest grows on inability to pay; can end in loss of the home [EX] | not conforming |
| Evasion | Part IV | The department cannot foreclose itself; certifying to the tax roll obtains a result it could not directly create [EX] | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Objection at the Council's annual certification hearing [EX] | one_case | City Council | not_independent | [EX] |
| 2 | Court challenge to the lien | one_case | Trial court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | — | not_applicable | — |
| Economic (2.B) | Escalating obligations? Path out? Reversible? | yes, escalation — 1% a month [EX] grows because the owner cannot pay (2.B.2); the path can end in tax sale, which is practically irreversible (2.B.4) | [EX] |
| Agency (2.C) | Told plainly without asking? | no — newspaper notice only [EX] | [EX] |
| Force (2.D.1) | — | not_applicable | — |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no detention | — |
| Emergency medical care (2.D.2) | Treatment without consent only on incapacity plus imminent harm? | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | partly — court only [EX] | [EX] |
| Expression (2.D.9) | — | no | [EX] |
| Equal treatment (2.D.10) | Reviewed? | UNKNOWN | [EX] |
| Identification (2.D.11) | — | not_applicable | — |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — a lien is recorded against the property; any later tax sale is the county's power, not recorded here |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Owner name, parcel, and amount, recorded in public land records [EX].

**B8. Dependencies and evasion.** The county Tax Collector enforces the lien through its own sale process (see the tax collector worked example). Under 4.2 the chain from water bill to tax sale is one function for scrutiny.

**B9. Harms seen.**
- economic — 37 parcels with water liens went to tax sale last year [EX] (public tax-sale records).

**B10. Decision inputs and oversight.** The certification list is a balance threshold applied by the billing vendor [EX]. No outside audit [EX].

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 3.C.5 (7 days, 12 months, 90 days); 2.D.12 (20 years) | | yes |

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

- Shutting off water to compel payment makes an essential conditional on compliance (2.B.1) and uses control of an essential as leverage (2.B.3). Late, reconnection, and deposit charges that grow because a household cannot pay are escalation (2.B.2).
- Stopping a power must never cut off water. The shutoff power can simply stop; if the billing or rate power stopped, delivery continues as the minimum essential function under a controller with no stake, with deadlines of 7 days, 12 months, and 90-day reviews [S1] (3.C.5, 3.E.6).
- A monopoly with no exit (no private wells) cannot rely on exit as a protection (2.C.3). The only transfer plan for a single provider is the state receivership, and it covers safety failures only (3.B.2).
- Opening an account in one's own name is a claimed entitlement, so 2.D.11 allows an identity check by the least intrusive means that works, with a non-biometric way offered and no other use. A photo-ID check is non-biometric; it conforms only if people without photo ID have another way in and the details are used for nothing else. This record cannot show either, so the B6 answer is UNKNOWN rather than yes or no.
- A shutoff list generated by vendor software with unpublished rules is an undeclared-input problem (5.3) and a vendor problem (4.5), even when staff carry out the shutoff.
- Certifying a water debt to the tax roll lets the utility obtain, through another authority, a result it could not create itself (4.5). The chain from bill to tax sale is one function (4.2).
- A referendum that can block a single increase is a real one-practice stop path, but only a new ordinance could end the power as a whole, and neither a new law nor a vote of the utility's own Council counts (3.C.1).
- Under 3.A.2 a city may have its utility's powers authorized by a panel chosen by lot from the people affected, excluding operators and anyone paid by the city, with appeal to an independent body. The Council's own votes are not such a panel, so authorization stays not conforming for P1–P3. Under 2.D.12 land title records may be kept while the title lasts, for confirming it only; P3's lien entries sit in public land records whose other uses are not shown, so P3's data limits stay not demonstrated.
