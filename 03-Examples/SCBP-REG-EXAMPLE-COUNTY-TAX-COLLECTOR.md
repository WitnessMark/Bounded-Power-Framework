---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-COUNTY-TAX-COLLECTOR
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
  name: "[COUNTY] Tax Collector"
  legal_entity: "[COUNTY] (county government), acting through the elected Tax Collector"
  related_entities: "[COUNTY] governing board (sets local fees, receives unclaimed surplus); [COUNTY] Land Bank (receives no-bid parcels); [AUCTION VENDOR] (runs online sales)"
  type: government
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: "[COUNTY]"
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Penalties, interest, and fees on delinquent property tax"
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
      remedy: not_demonstrated
      data_limits: not_conforming
      visibility: conforming
      floors: not_conforming
      evasion: conforming
  - power_id: P2
    short_name: "Tax-deed sale and retention of surplus equity"
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
      evasion: not_demonstrated
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [COUNTY] Tax Collector — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** The county office that bills and collects property tax for the county, cities, schools, and special districts. When tax goes unpaid it adds penalties, interest, and fees; after several years it sells the property at auction to recover the debt. A sale transfers the whole property, not just the amount owed, so an owner who owes a small debt can lose a home worth many times more.

A2. **Legal basis.** [STATE] property tax law sets due dates, penalty and interest rates, and the tax-deed sale process [EX]. The state later added a surplus-claim procedure after courts held that keeping more than the debt can be a taking of property [EX].

A3. **Who controls it.** An elected Tax Collector with a 4-year term [EX]. The county governing board sets local administrative fees and receives unclaimed surplus into the general fund [EX].

A4. **Related entities.** An auction vendor runs online sales for a fee paid by buyers [EX]. No-bid parcels pass to the county and are transferred to the county land bank [EX]. Figures are the Tax Collector's unless marked.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — Penalties, interest, and fees on delinquent property tax.
- P2 — Tax-deed sale and retention of surplus equity (assigned teaching point: an irreversible effect, 3.D.2).
- Not recorded: assessment (held by the county Assessor); collection of unsecured tax on business property.

---

## Power P1 — Penalties, interest, and fees on delinquent property tax

**B1. What it can do to people.** When an installment is late, the office adds a 5% penalty [EX] and a cost fee of 25 [EX]. From the end of the tax year, unpaid amounts carry a redemption penalty of 1% a month [EX] and a yearly redemption fee of 40 [EX]. After 3 years [EX] of delinquency the parcel becomes eligible for sale under P2.

**B2. Who and where.** About 140,000 parcels [EX] in a county of about 350,000 residents [EX]. About 4,200 parcels are delinquent [EX], and about 600 are in their third year [EX].

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | Rates set by state statute [EX]; no authorizing decision with findings on each requirement: NONE EXISTS | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | NONE EXISTS [EX] | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS [EX] | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Penalty cancellation for reasonable cause by the office itself; court [EX]; single cases only | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS [EX] | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Refund claims for erroneous charges within 4 years [EX], then court; whether these reach penalties caused by inability to pay is UNKNOWN | compliance not demonstrated |
| Data limits | Stated retention periods; deletion records (2.D.12–2.D.14, 7.6) | Tax roll and payment history kept permanently [EX], beyond the 20-year ceiling [S1] of 2.D.12. Title records may be kept as status registers while the title lasts (2.D.12), but the tax roll and payment history serve collection, not the owner's own status, and are public for any use [EX]. An owner's need for proof of payment is met by giving the owner a copy before destruction (2.D.14), not by permanent retention | not conforming |
| Visibility | Knowable to an ordinary person (3.B.9). Decision inputs declared (5.3) | Bills show due dates, penalty rates, and the date a parcel becomes eligible for sale [EX]; the statute plainly has no end date [EX], so the absence is knowable (failure recorded under Maximum term) | conforming |
| Floors | See B6 (Part II) | Penalties and interest grow because owners cannot pay [EX] (2.B.2) | not conforming |
| Evasion | Part IV | Charges are applied by the office itself [EX] | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Cancellation of a penalty for reasonable cause (illness, office error) [EX] | one_case | Tax Collector | not_independent | [EX] |
| 2 | Court action for refund | one_case | Trial court | independent | [EX] |
| 3 | Deferral for owners aged 65 or over [EX] with household income under 30,000 [EX]; a state agency pays the tax and holds a lien | one_case | State revenue agency | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Every path reaches one case; only a new statute could end the power, and a new law does not count.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | — | not_applicable — a charge on money owed | — |
| Economic (2.B) | Essentials conditional? Do obligations grow because people can't pay? Path to pay off? | yes, escalation — the redemption penalty adds 12% a year [EX] because the owner has not paid (2.B.2); a 3-year payment plan [EX] exists but is available only once and ends after two missed installments [EX] | [EX] |
| Agency (2.C) | Told plainly without asking? | yes — annual delinquency notice in plain language [EX] | [EX] |
| Force (2.D.1) | — | not_applicable | — |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no detention | — |
| Emergency medical care (2.D.2) | Treatment without consent only on incapacity plus imminent harm? | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — court [EX] | [EX] |
| Expression (2.D.9) | — | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? Reviewed? | UNKNOWN — no review | [EX] |
| Identification (2.D.11) | — | not_applicable | — |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — no search or seizure under this power; the sale is P2 |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Owner names, mailing addresses, parcel numbers, and payment history, all on the public tax roll [EX]. No deletion schedule [EX].

**B8. Dependencies and evasion.** Penalty and interest revenue goes to the county general fund, about 6 million a year [EX]. No outsourcing for this power.

**B9. Harms seen.**
- economic — on a typical third-year delinquency of 7,000 in tax [EX], penalties, interest, and fees add about 2,300 [EX] (admitted; calculated from the office's published schedule).

**B10. Decision inputs and oversight.** The rates are statutory and published [EX] (5.3). The county auditor audits collections [EX]; no outside body reviews the effect of penalties on owners.

---

## Power P2 — Tax-deed sale and retention of surplus equity

**B1. What it can do to people.** After 3 years [EX] of delinquency, the Tax Collector may sell the whole property at public auction without a court order [EX]. The minimum bid is the debt: tax, penalties, interest, and costs. Two outcomes follow.
- The property sells for more than the debt. The surplus is held for 1 year [EX]. The former owner must file a claim with a notarized form and proof of ownership [EX]. Unclaimed surplus goes to the county general fund [EX].
- Nobody bids the minimum. Title passes to the county with no surplus calculation [EX], and the county transfers the parcel to its land bank. The former owner receives nothing.

**B2. Who and where.** Last year [EX]: 131 parcels offered, 112 sold, 19 passed to the county [EX]. Surplus from the 112 sales was 6.3 million [EX]; 2.1 million was claimed [EX] and 4.2 million went to the general fund [EX]. Non-participants: family members living in the home, and heirs who inherited a home without probate and never received notice.

**B3. Authority basis.** `direct`.

**Irreversibility test (3.D.2).** No power may create an effect that is irreversible or materially hard to reverse; any action that risks one must be blocked before it is executed. Observed:
- A sale changes legal title permanently. Only a temporary, protective change of legal status can be containment, and a permanent change never is, so the sale is an ordinary exercise of power and must meet 3.D.2 in full.
- Recovering the debt is reversible: money can be refunded. Taking the equity above the debt becomes irreversible once the 1-year claim window closes [EX], or at once when a no-bid parcel passes to the county.
- In one [EX] case, a home with an estimated value of 260,000 [EX] and a debt of 11,800 [EX] passed to the county with no bid. The owner, who was in hospital during the notice period [EX], lost about 248,000 [EX] of equity.
- Less binding means existed: an automatic refund of surplus with no claim needed, a sale of only part of the value through a lien, or a court foreclosure that sets value [EX]. Under 2.B.4 the least binding means that accomplishes the purpose is required.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | State statute [EX]; each sale is decided by the Tax Collector without a court [EX] | not conforming |
| Maximum term | Expires on a set date (3.E.1, 7.2) | NONE EXISTS [EX] | not conforming |
| Harm thresholds | Published, measurable thresholds (3.A.5) | NONE EXISTS for equity lost, sales of occupied homes, or claim rates [EX] | not conforming |
| Stop paths | Tested paths, at least one independent (3.A.7, 3.C.1) | Single-case paths only [EX]; whole-power path NONE EXISTS | not conforming |
| Ending plan | Documented ending (3.A.9) | NONE EXISTS [EX] | not conforming |
| Remedy | Independent, funded remedy (3.A.10) | The surplus claim lasts 1 year [EX] and is run by the office; no remedy for no-bid parcels: NONE EXISTS | not conforming |
| Data limits | Retention periods (2.D.12–2.D.14) | Sale files kept permanently [EX]; retention UNKNOWN beyond that | compliance not demonstrated |
| Visibility | Knowable to an ordinary person, including whether it has grown (3.B.9) | Counts of properties taken and surplus kept are not published [EX]: NONE EXISTS | not conforming |
| Floors | See B6 (Part II) | Irreversible economic deprivation (2.B.4); notice omits the surplus right [EX]; property seized without a judicial officer's approval, and equity above the debt not returned (2.D.15) | not conforming |
| Evasion | Part IV | No-bid parcels pass to the county land bank [EX]; whether the land bank keeps resale proceeds above the debt is UNKNOWN | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Bankruptcy filing; the automatic stay halts the sale | one_case | Bankruptcy court | independent | [EX] |
| 2 | Lawsuit to set aside a deed for defective notice, within 2 years [EX] | one_case | Trial court | independent | [EX] |
| 3 | Tax Collector withdraws a parcel from sale [EX] | one_case | Tax Collector | not_independent | [EX] |
| 4 | Senior deferral (see P1, path 3) prevents sale [EX] | one_case | State revenue agency | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Each path halts one sale; only a new statute could end tax-deed sales, and a new law does not count. Redeeming by paying the debt is not a stop path.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | — | not_applicable | — |
| Economic (2.B) | Escalating obligations? Path out? Reversible? | yes — the debt that triggers sale grew through P1 penalties (2.B.2); loss of equity is practically irreversible (2.B.4); occupied homes are sold [EX], removing shelter (2.B.1) | [EX] |
| Agency (2.C) | Told plainly without asking? Usable protections? | no — notice by certified mail, posting, and newspaper [EX] does not mention the surplus right; the claim needs a notarized form and proof of ownership [EX] (2.C.1, 2.C.2) | [EX] |
| Force (2.D.1) | — | not_applicable at sale; eviction after sale is by a court order [EX] | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no detention | — |
| Emergency medical care (2.D.2) | Treatment without consent only on incapacity plus imminent harm? | not_applicable — no medical treatment | — |
| Due process (2.D.5) | Challenge before someone independent before the deprivation? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | partly — no court before the sale [EX]; challenge only afterwards | [EX] |
| Expression (2.D.9) | — | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? Reviewed? | UNKNOWN — owners over 70 and inherited homes without probate make up 45% of sales [EX]; no review | [EX] |
| Identification (2.D.11) | — | not_applicable | — |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | no — the sale takes the whole property without a judicial officer's approval [EX], and no emergency applies. Delinquency is individualized cause, but 2.D.15 also requires that approval for a seizure. Seized property must be returned when its purpose ends: once the debt is paid from the sale, the equity above it is returned only if claimed within 1 year [EX], and never for no-bid parcels | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — removal of occupants after a sale needs a court order [EX]; recorded under Force | [EX] |

**B7. Data.** Owner, occupant, and heir search results bought from a title-search vendor [EX]; under 4.4 those are collected when received. Retention: UNKNOWN.

**B8. Dependencies and evasion.** The auction vendor runs sales [EX]; the land bank receives no-bid parcels [EX]; a title-search vendor finds owners and heirs [EX]. Under 4.2 the chain from tax bill through land-bank resale is one function for scrutiny.

**B9. Harms seen.**
- economic — 4.2 million in unclaimed surplus kept last year [EX] (admitted in the county budget).
- economic and generational — 19 no-bid parcels taken with no surplus calculation [EX] (admitted in sale records); heirs lose a home that would have passed to them (2.D.7).
- psychological and agency — the hospitalized owner case in B3 [EX] (alleged in a pending lawsuit).

**B10. Decision inputs and oversight.** The sale rule is a statutory count of years delinquent [EX] (5.3). No outside body reviews individual sales before they happen; the county auditor reviews only the accounts [EX].

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.D.12 (20 years) | | yes |
| S2 | quote | Core Requirements v1 | BPF: Core Requirements v1 | Rule 3.D.2 | "A permanent change of legal status is never containment." | yes |

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

- Collecting a debt is reversible; keeping equity above the debt is not. A power that risks an irreversible effect must block it before execution (3.D.2), and 2.B.4 requires the least binding means.
- A tax-deed sale changes legal title permanently, so it can never be called protective containment [S2] (3.D.2). Only a temporary, protective, independently reviewed change of status can be.
- A surplus right that needs a notarized claim within a short window, and that the sale notice does not mention, is a protection that is not practically usable (2.C.1, 2.C.2).
- Penalties that grow because an owner cannot pay are escalation (2.B.2), and here they also enlarge the debt that later triggers the irreversible sale. The two powers are one chain (4.2).
- Paying, redeeming, or giving up is never a stop path; bankruptcy and a notice lawsuit are real paths, but each stops only one case (B5 rules; 3.C.1).
- Not publishing how many homes are taken and how much surplus is kept fails the "whether it has grown" part of the visibility test (3.B.9).
- Parcels and resale proceeds that move to a land bank stay inside the same function for scrutiny (4.2, 4.5).
- Heirs and household members who never owed the tax are non-participants (3.A.11), and the loss of family property binds a later generation (2.D.7).
- Under 2.D.12 title records are status registers and may be kept while the title lasts, for confirming it only. The tax roll and payment history are not; they serve collection and stay under the 20-year [S1] ceiling, with proof of payment given to the owner before destruction (2.D.14). Keeping them permanently makes P1's data limits not conforming.
- 2.D.15 makes the surplus a seizure question as well as an economic one: seized property is returned when its purpose ends. Once the debt is paid from the sale, the equity above it serves no purpose of the seizure, so keeping it unless claimed fails the rule. Selling without a judicial officer's prior approval fails it too, since no emergency applies.
