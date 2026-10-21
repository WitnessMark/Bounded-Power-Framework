---
response_id: SCBP-RSP-EXAMPLE-DATA-BROKER-2026-10-21
response_to: {record_id: SCBP-REG-EXAMPLE-DATA-BROKER, record_version: 1}
response_type: disagreement
example: true
form: {name: authority-response, version: 1.0.0, date: 2026-10-21}
core_requirements: {version: v1, date: 2026-10-21}
vocab_version: 1.0.0
institution_name: "[PEOPLE-DATA BROKER]"
responder_role: "General Counsel, [PEOPLE-DATA BROKER HOLDINGS]"
authorized_by_institution: yes
filed_date: 2026-10-21
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

> **Authority response.** Filed beside record SCBP-REG-EXAMPLE-DATA-BROKER version 1. It does not replace or change that record.

# Response — [PEOPLE-DATA BROKER] — to SCBP-REG-EXAMPLE-DATA-BROKER v1

## 1. Summary

The company disagrees with how the record classifies both of its products. In its view, neither people-search dossiers (P1) nor location-history lookups (P2) are authority. Both should be recorded as `influence_only`, the same classification the record already gives to the company's advertising segments. The company's position is:

- it compels no one, restricts no one, and makes no decision about any person;
- its products are information, much of it already public, that buyers may use or ignore;
- every consequential decision, whether a landlord's, an employer's, or a police agency's, is made by the buyer under the buyer's own legal duties.

The company does not dispute the record's figures in this response, and it announces no change.

## 2. Point by point

| # | The record says (quote it exactly, with its section, such as P1 B4) | Your response | Evidence |
|---|---|---|---|
| 1 | P1 B3: "`direct`. Collecting information about a person — including by buying, copying or inferring it — is an act the broker takes on that person itself (Definitions: Collect) [S1]. No buyer's later decision is needed for the power to exist." | Disagree. Compiling lawfully available records does nothing to the person. Nobody is ordered, charged, or excluded by the existence of a profile. Anything that happens to a person happens because a buyer chose to act, so P1 should be `influence_only`. | The company's terms of use [EX] |
| 2 | P1 B3: "That reliance is shown only by scattered examples (tier 7) and is not used for a finding here." | Agree with this sentence, and rely on it. The record itself finds no tier 5 evidence that anyone builds dossiers into binding decisions. In the company's view, that confirms the product is influence only. | The terms of use bar screening for housing, employment, credit, or insurance [EX] |
| 3 | P2 B3: "`indirect_a_operationalized`. The broker does not arrest or charge anyone; police agencies rely on its output to open investigations, identify people and seek warrants." | Disagree. The company agrees with the first half of this sentence. Police agencies do not "rely on" the output in the sense of the Authority definition: an investigative lead is one input among many, weighed by trained officers, and binds no one. P2 should be `influence_only`. | Subscription terms state the output is "an investigative lead only, not a sole basis for any enforcement action" [EX] |
| 4 | P2 B3: "Causation Ladder: tier 4, operational reliance [S1]." | Disagree. The record rests reliance on how police use the data, but the contracts say nothing that supports it. The contracts bind the company to supply data and limit the purposes for which agencies may use it. They do not oblige any agency to use the data, or to act on it, in any case. | Model subscription agreement, purpose clause [EX] |
| 5 | P2 B3: "Material cost: a person cannot avoid it without giving up ordinary phone apps, and the person does not know which apps supply it." | Disagree. Every supplying app asks for location permission, and any person can decline it [EX]. Declining costs nothing that matters. | App-store permission prompts [EX] |
| 6 | Front matter, both powers: "findings" rows set to not_conforming (for example, "authorization: not_conforming") | Disagree as a consequence of points 1 to 5. If both products are influence only, they are recorded for watching, and the B4 requirements do not apply to them. | As above [EX] |

## 3. Changes you have made, if any

None. The company does not adopt the Core Requirements and announces no change to its products. It notes that it honors deletion requests from residents of [STATE] within 45 days [EX], as the record already states in P1 B4.

## 4. Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it | Quote | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | quote | The record answered: SCBP-REG-EXAMPLE-DATA-BROKER, version 1 | BPF: SCBP-REG-EXAMPLE-DATA-BROKER v1 | P1 B3; P2 B3; front matter | "`indirect_a_operationalized`. The broker does not arrest or charge anyone; police agencies rely on its output to open investigations, identify people and seek warrants." | yes |

In a real response, each [EX] item would be a source row linking to the company's published terms and contracts.

## 5. Assertions

- [x] This response is accurate to the best of our knowledge.
- [x] Every number has a source (illustrative figures are tagged [EX]).
- [x] People are referred to by role or title.

---

## Teaching notes (non-binding)

*These notes are written by the examples working group, not by the company. They explain how the framework treats a disagreement like this one.*

- **A response never changes a finding by itself.** The record keeps its findings until the original preparer issues a new version, and the preparer changes a finding only if the response shows the record is wrong (Authority Response form, "What happens next"). Whether an influence is operationalized, and whether a cost is material, "may not be settled by the influencing system's own assertion" (Definitions: Operationalized into compulsion; Material cost). The company's view is therefore an argument for the preparer and for any independent body that hears a contest. It is not a reclassification.
- **P1 does not depend on limb (a) at all.** The record classifies P1 as `direct` because buying, copying and inferring information about a person is collecting it (Definitions: Collect), and collecting is something the broker does to that person. Point 2 of the response is correct that the buyers' reliance is only tier 7, but the record already says that tier 7 evidence "is not used for a finding here". The tier 7 evidence was never what P1 rested on, so agreeing with it does not move P1 toward influence only (Definitions: Causation Ladder; 2.D.12).
- **P2 requires evidence of operationalized reliance, not merely a supply contract.** The subscription agreement establishes a contractual relationship under which the broker supplies location-history data to police agencies. That agreement does not, by itself, establish that an agency uses the data as a structured determinant of decisions affecting identifiable people.
- The fictional registration separately describes police using the output to identify people, open investigations, and seek warrants. Those asserted uses must be evaluated through the Causation Ladder, with evidence appropriate to the claimed classification. The company's "investigative lead only" label neither establishes nor defeats operationalized reliance. Police remain responsible for their own decisions, while the broker's indirect authority depends on what the evidence shows about how its output is used.
- If the evidence does not establish the required causal threshold, the preparer must record that uncertainty and reassess the classification rather than relying on the supply obligation as conclusive proof.
- **"Lead only" does not defeat limb (a).** If the evidence shows that a lead decides whom police look at, it is a structured determinant of that decision even if officers weigh other facts afterwards. The definition's own test example is a credit score wired into underwriting: other inputs exist there too. The Authority definition also puts both sides in scope: the police agency for its decision and the broker for the effect of its output, so "the buyer decides" moves no responsibility (4.1).
- **Material cost is a separate and independent route.** Limb (a) is also met when people "cannot refuse or exit it without material cost". Point 5 says anyone can decline location permission. That is self-help, which is not a stop path (Form B5), and declining location in apps whose identity is unknown is not a practical exit. Whether the remaining cost is material is for an independent body to decide, not the company.
- **The advertising segments show where the line is.** The record already recorded them as `influence_only` because people ignore ads at no material cost (4.3). The record applies the definition product by product, so the company's request for equal treatment is already met: each product gets the classification its own evidence supports.
- **How readers see both.** A display shows the newest version of the record first, with a link to this response and a one-line note of what it disputes (Authority Response form, "Versions"). A reader of the dossier and lookup findings sees the company's disagreement beside them without searching history, and can judge the argument directly. If the preparer issues a new version, that version must quote every passage it changes. If not, this response stays beside version 1.
