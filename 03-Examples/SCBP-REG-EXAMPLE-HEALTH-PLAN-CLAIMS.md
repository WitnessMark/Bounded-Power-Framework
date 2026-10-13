---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-HEALTH-PLAN-CLAIMS
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
  name: "[COMPANY] Health Plan"
  legal_entity: "[COMPANY] Health Plan, Inc., a licensed health insurer"
  related_entities: "[CRITERIA VENDOR] (licensed medical-necessity criteria); [UTILIZATION-MANAGEMENT VENDOR] (imaging prior authorization); [ANALYTICS VENDOR] (claim-scoring model); employer plan sponsors"
  type: private_company
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: NONE
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Prior authorization"
    category: benefits_eligibility_or_allocation
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: not_conforming
      remedy: not_conforming
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_conforming
      evasion: not_conforming
  - power_id: P2
    short_name: "Automated claim-denial model"
    category: scoring_ranking_or_classification
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

# [COMPANY] Health Plan — Registration (worked example)

## PART A — The institution

A1. **What it is.** A regional health insurer with about 1.2 million [EX] members in [STATE]. It decides whether it will pay for care, before the care (prior authorization) and after it (claim review). A "no" usually means the care does not happen, or the member owes the full price.

A2. **Legal basis.** A state insurance licence and a state utilization-review licence; policy contracts filed with the state insurance regulator; for employer self-funded plans, administrative contracts governed by the federal employee-benefits law, named generally. [EX]

A3. **Who controls it.** A board elected by shareholders of a holding company [EX].

A4. **Related entities.** [CRITERIA VENDOR] licenses the medical-necessity criteria. [UTILIZATION-MANAGEMENT VENDOR] decides imaging requests. [ANALYTICS VENDOR] built and maintains the claim model. For self-funded plans the employer is the plan sponsor and the insurer decides claims for it; about 40% [EX] of members are in such plans. Figures belong to the insurer.

A5. **Adoption.** not_adopted. [EX]

A6. **Powers found.**
- P1 Prior authorization of care.
- P2 Model-driven denial of submitted claims.
- Not recorded: drug formulary, provider network admission, premium setting.

---

## Power P1 — Prior authorization

**B1. What it can do to people.** Before about 400 [EX] listed services and drugs are given, the treating clinician must get the insurer's approval. A denial means the insurer will not pay. Most members then go without the care, take a substitute, or pay themselves.

**B2. Who and where.** All members. About 900,000 [EX] requests a year; 9% [EX] denied. Clinicians and their staff bear the paperwork.

**B3. Authority basis.** `direct`. The insurer decides whether it will pay under its own contract, and that decision binds the member's coverage. This is not indirect authority: no other party relies on an output of the insurer's to make a decision of its own [S3]. The same holds when the insurer decides for a self-funded employer plan: the insurer makes the denial.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The state regulator licenses the utilization-review program on paper standards. It is independent but hears no affected people and makes no findings on each requirement. | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | The utilization-review licence expires every 2 years [EX] and lapses unless the regulator renews it. | conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. Decision deadlines exist (B10) but no harm threshold. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | External review per case; regulator orders reach only fully insured plans. No whole-power path. | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS. | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | External review can reverse a denial; no compensation for harm from delay. Employer plans can recover only the benefit owed. | not conforming |
| Data limits | Retention; 20-year ceiling; deletion records (2.D.12–2.D.14, 7.6) | Records kept 10 years [EX]. Deletion records: UNKNOWN. | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9) | The list of services needing approval, yearly approval and denial rates, and changes to the list are published [EX]; notices give the reason and appeal rights; the licence and its expiry are on the regulator's public register. | conforming |
| Floors | See B6 (Part II) | Protection depends on self-advocacy (B6). | not conforming |
| Evasion | Not split, outsourced, laundered, or using proxies (Part IV) | Imaging denials by the vendor are left out of the published denial rate (B8). | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | External review of a medical-necessity denial, binding on the insurer (fully insured plans: reviewer assigned by the state regulator) | one_case | independent review organization | independent | [EX] |
| 2 | External review for self-funded plans: reviewer chosen by the insurer from 3 [EX] organizations it contracts with | one_case | independent review organization | partly_independent | [EX] |
| 3 | Market-conduct examination and corrective order | one_practice | state insurance regulator | independent | [EX] |
| 4 | Non-renewal of the utilization-review licence | one_practice — fully insured plans only; federal law places self-funded plans outside state reach | state insurance regulator | independent | [EX] |
| 5 | Class action under the federal employee-benefits law | one_practice | federal court | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Prior authorization is permitted by contract; only a new law could end it.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Ecological threshold? | not_applicable — no ecological effect | |
| Economic (2.B) | Essentials conditional on compliance? Growing obligations? | no — coverage turns on clinical criteria, not the member's compliance; but care received after a denial becomes the member's full-price debt to the provider | [EX] |
| Agency (2.C) | Told plainly; usable without self-advocacy? | no — notices state reasons, but only 12% [EX] of denials are appealed, and an appeal needs records the member must gather (2.C.2) | [EX] |
| Force (2.D.1) | Force? | not_applicable — no force | |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no detention | |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — the insurer decides payment, not treatment | |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — external review; partly independent for self-funded plans | [EX] |
| Expression (2.D.9) | Restricts expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens; reviewed? | UNKNOWN — denial rates are not reported by group; notices are in English with a translation tagline | [EX] |
| Identification (2.D.11) | Identification without cause? | not_applicable — acts on a named request | |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — prior authorization acts on a clinician's request; nothing is searched or seized |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Diagnoses, clinical notes, test results, and the decision. Purpose: the coverage decision. Records sent to the imaging vendor are covered by the insurer's limits. [EX]

**B8. Dependencies and evasion.** [UTILIZATION-MANAGEMENT VENDOR] decides imaging requests and is paid a fee per member plus a bonus tied to cost savings [EX]. Its denials are not in the insurer's published rate. Under 4.5 the vendor's decisions are the insurer's power, and leaving them out of the published rate defeats visibility (4.1).

**B9. Harms seen.** bodily: deterioration during delay (allegation in complaints to the regulator). economic: members billed after denial. Of appealed denials, 60% [EX] are reversed internally and 45% [EX] of the rest are reversed on external review (admitted in the insurer's own published data). A regulator order found late decisions in 8% [EX] of sampled urgent requests (adjudicated, order).

**B10. Decision inputs and oversight.** [CRITERIA VENDOR] criteria plus in-house policies. Criteria are proprietary; a member can see the criterion used only on request (5.3). State deadlines: 72 hours [EX] for urgent and 7 days [EX] for standard requests. The regulator examines every 5 [EX] years.

---

## Power P2 — Automated claim-denial model

**B1. What it can do to people.** After care is given, a model scores every claim for "payment risk". Claims above a cut-off are denied for coding or necessity reasons, or held until the provider sends records. A medical director signs batches of flagged denials without opening the records [EX]. The member may then be billed by the provider.

**B2. Who and where.** About 14 million [EX] claims a year; 3% [EX] flagged; about 380,000 [EX] members affected a year.

**B3. Authority basis.** `direct`. The model's score becomes the insurer's own payment decision. A human signature on a batch does not change that: automated systems face the same requirements as human ones [S2].

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body, public record (3.A.1, 3.A.2) | Deployed by the insurer's payment-integrity unit. No outside approval. NONE EXISTS. | not conforming |
| Maximum term | Set expiry (3.E.1, 7.2) | NONE EXISTS. The vendor contract renews automatically each year [EX]. | not conforming |
| Harm thresholds | Not dependent on the institution's own findings (3.A.5) | An internal target that fewer than 25% [EX] of appealed model denials be reversed, set and measured by the insurer. | not conforming |
| Stop paths | Tested, one independent (3.A.7, 3.C.1) | Coding denials get internal appeal only; external review covers necessity denials only. | not conforming |
| Ending plan | Documented (3.A.9) | NONE EXISTS. | not conforming |
| Remedy | Independent, funded (3.A.10) | Internal appeal; provider payment disputes. No independent route for coding denials. | not conforming |
| Data limits | Retention; 20-year ceiling (2.D.12) | Training data kept in a data store with no deletion date [EX], which cannot meet the 20-year ceiling [S1]. | not conforming |
| Visibility | Knowable (3.B.9); inputs declared (5.3) | Members are not told a model was used; inputs and cut-off are not published. | not conforming |
| Floors | Part II | No independent challenge for coding denials (B6). | not conforming |
| Evasion | Part IV | Output called a "recommendation" but followed in 99% [EX] of flagged claims (B8). | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | External review, necessity denials only | one_case | independent review organization | independent | [EX] |
| 2 | Regulator order on automated denials (fully insured plans) | one_practice | state insurance regulator | independent | [EX] |
| 3 | Insurer switches the model off | whole_power | chief medical officer | not_independent | [EX] |

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Path 3 is the insurer's own decision, which does not count because it is not independent of the insurer.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Ecological threshold? | not_applicable — software only | |
| Economic (2.B) | Growing obligations? | yes — denied claims turn into member balances that providers send to collection | [EX] |
| Agency (2.C) | Told plainly without asking? | no — the notice gives a code, not the fact that a model flagged the claim (2.C.1) | [EX] |
| Force (2.D.1) | Force? | not_applicable — no force | |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no detention | |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — the insurer decides payment, not treatment | |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | no — coding denials have no independent review; the criteria are undisclosed | [EX] |
| Expression (2.D.9) | Restricts expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens; reviewed? | UNKNOWN, concern — flag rates are 1.7 times [EX] higher for members in some postal codes, evidence at tier 6 (B9); no independent review | [EX] |
| Identification (2.D.11) | Identification without cause? | not_applicable — acts on submitted claims | |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — records come from providers under the plan contract to decide claims; their handling is recorded under Data (B7) |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Claim lines, diagnosis and procedure codes, provider billing history, the member's past claims, and postal code. The model is retrained yearly on seven [EX] years of claims. The trained model is a derived output that keeps the limits of the data it came from (4.4). [EX]

**B8. Dependencies and evasion.** [ANALYTICS VENDOR] is paid 20% [EX] of the savings it finds, which ties its revenue to denials. The insurer calls the score a recommendation, yet the sign-off rate and the unopened records show the score decides. Relabeling does not change the power (1.3, 4.8). [EX]

**B9. Harms seen.** economic: balance bills (admitted in appeal files). A pending lawsuit alleges denials without individual review (allegation). Postal code may stand in for race or income (4.7). A university audit using public data shows a statistical proxy effect (tier 6), which supports only a recorded concern and a request for evidence [S4]. It does require independent disparity review under 2.D.10 within 90 days [S1].

**B10. Decision inputs and oversight.** Inputs, weights, and the cut-off are undeclared (5.3). The vendor audits its own accuracy. No outside body evaluates the model (5.1). [EX]

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it | Quote | Verified? |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.D.10 (90 days), 2.D.12 (20 years) | | yes |
| S2 | quote | Core Requirements v1 | BPF: Core Requirements v1 | 1.3 | Automated systems are subject to the same requirements as human-operated ones. | yes |
| S3 | quote | Core Requirements v1, Definitions: Authority | BPF: Core Requirements v1 | Definitions, Authority (a) | another party relies on it as a structured determinant of a decision that binds identifiable persons or organizations | yes |
| S4 | quote | Core Requirements v1, Causation Ladder | BPF: Core Requirements v1 | Definitions, Causation Ladder | tiers 6–7 alone support only a recorded concern and a request for evidence | yes |

Figures tagged [EX] are illustrative and have no source.

## PART D — Honesty assertions

- [x] Every number has a source tag or an [EX] tag.
- [x] Nothing was presented as a real institution's data.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] Made in good faith, as a structural description.

Preparer: BPF examples working group (worked example).

## Teaching notes (non-binding)

- The authority basis is `direct`. An insurer denying payment under its own contract is acting on the member itself. Indirect authority (4.3) is for outputs another party relies on [S3]; it is not needed here and would understate the power.
- The same is true when the insurer decides for an employer's self-funded plan, but the stop paths differ: federal law puts those plans outside state regulators, so a state order reaches only part of the power. Record reach honestly as `one_practice` (3.A.7, 3.C.1).
- A licence that expires every 2 years [EX] and lapses unless an independent regulator renews it can make the maximum term conforming (3.E.1, 7.2) while authorization still fails (3.A.2).
- External review is a real, independent, binding path, and due process (2.D.5) is met where it applies. It still reaches one case, gives no compensation (3.A.10), and depends on members appealing, which most do not (2.C.2).
- A model whose score is signed in batches is an automated decision [S2]. Calling it a recommendation is relabeling (1.3, 4.8); declared inputs are required (5.3).
- Vendors that decide or score are part of the insurer's power (4.5). Leaving their denials out of published figures is an evasion finding.
- A proxy finding under 4.7 needs Causation Ladder tier 5 or stronger; a tier 6 audit supports only a concern [S4]. Disparity review under 2.D.10 needs no tier.
