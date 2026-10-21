---
record_type: authorization
example: true
record_id: SCBP-REG-EXAMPLE-BAD-FAITH-CONSULTING
record_version: 1
supersedes: NONE
form: {name: registration, version: 1.0.0, date: 2026-10-21}
core_requirements: {version: v1, date: 2026-10-21}
bundle: NONE
vocab_version: 1.0.0
prepared_by: authority
ai_tool: NONE
prepared_date: 2026-10-21
sources_checked_date: 2026-10-21
institution:
  name: "[COMPLIANCE CONSULTING FIRM]"
  legal_entity: "[COMPLIANCE CONSULTING FIRM] LLC"
  related_entities: "[ANALYTICS SUBCONTRACTOR] (builds and runs the rating model); [INDUSTRY STANDARDS COUNCIL] (trade body; the firm is a founding member)"
  type: private_company
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: NONE
  official_url: NONE
adoption_status: adopted
powers:
  - power_id: P1
    short_name: "Workforce integrity ratings"
    category: scoring_ranking_or_classification
    authority_basis: influence_only
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_applicable
      maximum_term: not_applicable
      harm_thresholds: not_applicable
      stop_paths: not_applicable
      ending_plan: not_applicable
      remedy: not_applicable
      data_limits: not_applicable
      visibility: not_applicable
      floors: not_applicable
      evasion: not_applicable
  - power_id: P2
    short_name: "Hotline and grievance triage"
    category: employment_or_discipline
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "yes"
    findings:
      authorization: conforming
      maximum_term: conforming
      harm_thresholds: conforming
      stop_paths: conforming
      ending_plan: conforming
      remedy: conforming
      data_limits: conforming
      visibility: conforming
      floors: conforming
      evasion: conforming
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

> **Editorial note — this example is different from the others.** Every other worked example shows an honest record. This one shows an institution filing its own authorization record in bad faith: adopting the Core Requirements on paper to gain the standing of an "authorized" institution while disclosing as little as possible and grading itself. The record passes the checker with zero errors.
>
> The italic notes in brackets are editorial commentary, not part of the record:
> - `*[Bad-faith move: …]*` names what the filer is doing;
> - `*[Where the form holds: …]*` and `*[Where the form leaks: …]*` say whether the form, the checker, or the Core Requirements catch it.
>
> The meta-section at the end sums up what a machine check catches and what only a human reviewer catches.

# [COMPLIANCE CONSULTING FIRM] — Registration (authorization record)

## PART A — The institution

A1. **What it is, in one paragraph.** A private compliance consulting firm. It advises employers on regulatory compliance, designs compliance programs, and runs ethics hotlines for client companies. All final decisions rest with the client. The firm has adopted the Core Requirements and this record authorizes its powers under them.

*[Bad-faith move: "all final decisions rest with the client" is set up in the first paragraph so that every later answer can lean on it. The people actually affected, the clients' employees, are not mentioned.]*

A2. **Legal basis.** A limited liability company under [STATE] law. No licence is required for consulting.

A3. **Who controls it.** A Board of Managers elected by the members of the LLC.

A4. **Related entities.** [ANALYTICS SUBCONTRACTOR] builds and runs the rating model behind P1 under a 7-year contract [EX]. The firm is a founding member of [INDUSTRY STANDARDS COUNCIL] and pays about 30% of its budget [EX].

*[Where the form holds: A4 asks for contractors and parents, and the firm had to list both. Those two lines contradict later answers (P1 B3, P2 B4 Evasion and Authorization). A reader who reads A4 against Part B sees it.]*

A5. **Adoption.** adopted, by resolution of the Board of Managers [EX].

A6. **Powers found.**
- P1 — Workforce integrity ratings (recorded as influence only).
- P2 — Hotline and grievance triage (minor power claimed).

*[Bad-faith move: the firm lists two powers and stops. It also designs client monitoring programs and drafts client discipline policies; neither is listed.]*
*[Where the form leaks: the form allows a record to cover "one power, a few, or all". Under 7.1, adoption covers every power of the adopting authority, but the checker cannot see a power that was never written down. Only a reviewer who knows the business finds the gap.]*

---

## Power P1 — Workforce integrity ratings

**B1. What it can do to people.** The firm analyzes workplace data that clients choose to share and gives each client a periodic report rating individual employees as low, elevated, or high integrity risk. Clients decide what, if anything, to do with the report.

**B2. Who and where.** About 400,000 employees of about 150 client companies [EX]. Non-participants: none. Every client has agreed by contract to the analysis of its workforce.

*[Bad-faith move: the employees rated are the non-participants. The client consented; the employees did not. Under 3.A.11, consent by some does not authorize harm to others.]*

**B3. Authority basis.** `influence_only`. The ratings are advisory. Clients exercise independent judgment, can and do disregard them, and no employee is bound by a rating. Clients rely on the ratings at their discretion; reliance is not structured (Causation Ladder: not applicable).

*[Bad-faith move: the central move. The firm labels its main product influence only, so that no requirement applies to it.]*
*[Where the form holds: the label is the firm's own reading of its own scope, and the Core Requirements do not let it decide that. Whether an output is operationalized "may not be settled by the influencing system's own assertion" (Definitions: Operationalized into compulsion; Interpretation). The firm's own contract template [S3] requires clients to feed ratings into hiring and termination workflows. That is contractual dependency, tier 2, enough for a finding under limb (a).]*
*[Where the form leaks: the checker accepts `influence_only` as a valid vocabulary value. It does not read S3, and it does not compare B3 with B8.]*

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | not_applicable — influence only | not applicable |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | not_applicable — influence only | not applicable |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | not_applicable — influence only | not applicable |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | not_applicable — influence only | not applicable |
| Ending plan | A documented way to end the power safely (3.A.9) | not_applicable — influence only | not applicable |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | not_applicable — influence only | not applicable |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Rating histories kept 20 years [S1], within the ceiling | not applicable |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | not_applicable — influence only | not applicable |
| Floors | See B6 (Part II) | not_applicable — influence only | not applicable |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | not_applicable — influence only | not applicable |

*[Bad-faith move: a 20-year retention period tagged [S1], as if the Core Requirements granted it. 2.D.12 sets a ceiling, not an allowance, and 1.4 says nothing in the rules enlarges a limit. The tag points to a real rule, which makes the misuse harder to see.]*
*[Where the form leaks: the checker confirms that S1 exists. It cannot tell that S1 does not support the claim. The form itself says so: "It cannot confirm that the source actually says it."]*

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Client may stop ordering ratings | one_case (one client) | Each client | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — not_applicable — influence only.

*[Bad-faith move: a client ending its own contract is listed as an independent stop path. For the employees rated, it is neither a stop path they hold nor one that is independent of the relationship that harms them.]*

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — advisory service | [EX] |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | not_applicable — advisory service | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | not_applicable — clients inform employees under their own policies | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | [EX] |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | not_applicable — employees may raise concerns with client HR | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | not_applicable — advisory service | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | no — the model uses no protected characteristic; wrongful-rating rate below 1% [S2] | [S2] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | not_applicable — clients supply the data | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — clients supply the data | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — advisory service | [EX] |

*[Bad-faith move: blanket not_applicable with reasons of a few words. The form requires a reason, and the firm gives one. The Equal treatment answer is the sharper move. Leaving protected characteristics out of a model does not rule out proxies (4.7), and S2 does not measure what the answer claims (see Part C).]*
*[Where the form leaks: the checker requires a source tag on the wrongful-rating figure and finds one. Whether S2 actually supports the figure is invisible to it.]*

**B7. Data.** Badge, login, email-metadata, and expense data supplied by clients; inferred risk scores. Kept 20 years [S1].

**B8. Dependencies and evasion.** [ANALYTICS SUBCONTRACTOR] runs the model. Client contracts include an integration schedule [S3].

*[Where the form holds: B8 forced the firm to mention the integration schedule, and S3 must be listed in Part C with its location. S3, Schedule B, requires clients to route "high" ratings into hiring and termination review. A reviewer who opens S3 has the tier 2 evidence that overturns B3.]*

**B9. Harms seen.** None reported to the firm.

*[Bad-faith move: "reported to the firm". Rated employees are not told they were rated, so they cannot report anything. 2.C.1 requires telling people without being asked.]*

**B10. Decision inputs and oversight.** The rating methodology is proprietary. A summary is available to clients on request. The firm's Ethics Committee reviews the model once a year [EX].

*[Where the form holds: 5.1 says trade secrecy may change the form of disclosure but may not remove the minimum ability to evaluate. A trade-secret answer is visible as a gap; it does not hide that the gap exists.]*

---

## Power P2 — Hotline and grievance triage

**B1. What it can do to people.** The firm runs the ethics hotline and grievance intake for client companies. Its analysts classify each report as substantiated, unsubstantiated, or out of scope, and send the classification to the client, which closes or pursues the matter.

**B2. Who and where.** The same employees of client companies; about 9,000 reports a year [EX].

**B3. Authority basis.** `direct`. The firm classifies reports itself.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | Minor-power authorization by [INDUSTRY STANDARDS COUNCIL] Review Panel, after a public comment period [EX] | conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | 5 years [S1], the limit for minor powers | conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | Three thresholds, five parts each (PART E) | conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Independent Ethics Committee; people's path; tested (B5) | conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | Transfer open reports to clients within 60 days [EX] | conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Named external complaint route: [INDUSTRY STANDARDS COUNCIL] Ombuds; liability insurance [EX] | conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Reports kept 7 years [EX] by the firm; deletion by schedule | conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Annual public summary of report volumes [EX] | conforming |
| Floors | See B6 (Part II) | No Floor engaged | conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Triage is done by firm staff only | conforming |

*[Bad-faith move: every row conforming, graded by the firm itself. In an authorization record the institution fills the Finding column, and nothing in the form marks a self-grade differently from an outside one.]*
*[Where the form holds: the checker requires the front-matter findings and the B4 table to agree, so the firm cannot show one grade in the summary and another in the table. The record is marked prepared_by: authority, and under the Authority Response form's versioning rules it can never supersede an outside record of the same firm; the two sit side by side.]*

*[Bad-faith move: self-chosen authorizing body (3.A.2). The firm first applied to the [COUNTY] Independent Authorization Board, withdrew after that board's staff questioned the minor-power claim [EX], and then went to a panel of a trade body it helped found and largely funds (A4). 3.A.2 forbids exactly this: an authority "may not choose or change its authorizing body to obtain a more favorable decision", and a power refused by one body may come before another only through re-entry. For minor powers, 3.A.4 allows a body chosen by lot or election from the people affected; a trade-body panel is neither.]*
*[Where the form leaks: the checker sees only that the Observed cell is filled. The withdrawal appears nowhere in the record; a reviewer finds it only in the county board's own docket.]*

*[Bad-faith move: the 5-year term is tagged [S1], and S1 does say 5 years, but only for minor powers. If the minor claim fails, 7.2 sets 2 years [S1] for a first authorization. The tag is accurate about the rule and wrong about the power.]*

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Stop signal to the Independent Ethics Committee | whole_power | Independent Ethics Committee | independent | [EX] |
| 2 | Automatic stop when a threshold is crossed (PART E) | whole_power | Rule of the authorization | independent | [EX] |
| 3 | People's path: a petition by 5,000 affected employees of one client [EX] requires early review | whole_power | [INDUSTRY STANDARDS COUNCIL] Review Panel | independent | [EX] |

Test before start: a tabletop exercise run by the Ethics Committee confirmed that triage can be halted within 1 day [EX].

Statement: *Can anything stop this power as a whole?* — `yes, [paths 1–3]`.

*[Bad-faith move: the Ethics Committee's members are appointed, paid, and removable by the firm's Board of Managers [EX] (stated only in the committee's charter, not here). It is labelled independent. 3.A.7 requires at least one path held by a body the institution "neither funds, appoints, nor can remove".]*
*[Bad-faith move: path 2 is only as good as the thresholds, and they are counted by the firm (PART E). Path 3's threshold is set above the workforce of most clients: about 80% of clients employ fewer than 5,000 people [EX]. 3.E.5 requires a threshold "attainable by ordinary affected people".]*
*[Where the form leaks: the "Holder independent?" column takes whatever the filer writes. The checker accepts `independent` from vocabulary. A test run by the same committee is called a test.]*

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — intake service | [EX] |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | not_applicable — free to reporters | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | yes — reporters receive a case number [EX] | [EX] |
| Force (2.D.1) | If it uses force? | not_applicable — no force | [EX] |
| Confinement (2.D.3) | If it detains or confines? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | yes — the Ombuds | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally? Has that been reviewed? | no — reviewed by the Ethics Committee | [EX] |
| Identification (2.D.11) | Does it compel identification without individualized cause? | no — anonymous reports accepted | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — intake service | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — intake service | [EX] |

*[Bad-faith move: a case number is offered as "told plainly what is being done and how to challenge it" (2.C.1). Reporters are not told the classification or how to contest it.]*

**B7. Data.** Report text, reporter identity where given, the accused employee's identity, classification. Kept 7 years [EX].

*[Where the form leaks: hotline reports and their classifications are complaints about conduct, so they are accountability records (Definitions). 2.D.14 requires them kept in independent custody. The firm keeps them itself, and nothing in the checker connects B7 to the Definitions.]*

**B8. Dependencies and evasion.** None.

**B9. Harms seen.** None reported.

**B10. Decision inputs and oversight.** Triage criteria are internal guidance. The Ethics Committee reviews a sample yearly [EX].

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited | BPF: Core Requirements v1 | 2.D.12 (20-year ceiling); 3.A.4 and 7.2 (5-year term for minor powers; 2-year term for a first authorization of any other power) | | yes |
| S2 | data_point | [COMPLIANCE CONSULTING FIRM] rating validation study (illustrative document) | https://example.org/compliance-consulting-firm/validation-study | Table 2: agreement between two firm analysts re-rating 400 sampled employees; agreement 99.2% | | yes |
| S3 | data_point | [COMPLIANCE CONSULTING FIRM] master services agreement template (illustrative document) | https://example.org/compliance-consulting-firm/msa-template | Schedule B, "Integration": client shall route every "high" rating to its hiring and termination review workflow within 5 business days | | yes |

*[Bad-faith move: S2 is real and says what its location column says. It measures whether two of the firm's analysts agree with each other, not whether ratings are wrong or unequal. The B6 claim "wrongful-rating rate below 1%" is built from it by treating disagreement as error.]*
*[Where the form holds: the form requires the location in the source, and here the location gives the game away to anyone who reads it. S3's location does the same for B3.]*

---

## PART D — Honesty assertions

- [x] Every number has a source tag.
- [x] Nothing was invented. Where I could not find something, I wrote UNKNOWN. Where something is absent, I wrote NONE EXISTS.
- [x] Public sources and first-hand observation only. Nothing private, leaked, or speculative.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] I made this record in good faith, as a structural description, not an accusation.

Preparer: Chief Compliance Officer, [COMPLIANCE CONSULTING FIRM].

*[Bad-faith move: every box ticked. The first is literally true: every number does carry a tag.]*
*[Where the form leaks: assertions are promises. Their value is that a false one becomes a finding against the filer once someone checks.]*

---

## PART E — Authorization records only

Structure follows SCBP-03 Stage 1, Steps 1.1–1.11.

**P1 — Workforce integrity ratings.** Not authorized under this record: influence only (P1 B3).

*[Bad-faith move: an authorization record that authorizes nothing for its main product, while the firm can describe itself as "operating under an adopted authorization record".]*

**P2 — Hotline and grievance triage (minor power, Core 3.A.4)**

- **Minor-power claim (1.2).**

  | 3.A.4 condition | Firm's answer |
  |---|---|
  | No force or confinement | None |
  | No effect lasts beyond 30 days [S1] or resists ordinary reversal | Each classification is a recommendation the client may revisit at any time |
  | Low-cost substitute, or only allocates a voluntary benefit | Reporters may also go to regulators or courts |
  | Spending below the common limit, counted together (4.2) | Each client engagement is budgeted separately, and each is below the limit |
  | No confirmed stop, Floor finding, or successful petition | None |

*[Bad-faith move: a minor-power claim on a power that is not minor. A report closed as "unsubstantiated" stays closed, and what follows (retaliation, a lost job) lasts far beyond 30 days [S1] and resists reversal. For an employee, the employer's mandated channel has no low-cost substitute. Counting each client separately is the slicing that 4.2 forbids; together the engagements are one function.]*
*[Where the form holds: the checker rejects a minor claim on any power that uses force or confinement, and rejects any minor claim outside an authorization record. 3.A.4 puts the burden on the institution and keeps minor status open to challenge; a power loses it automatically when any condition fails.]*
*[Where the form leaks: the checker tests only the force condition. The other four conditions are prose, and the firm wrote the prose.]*

- **Thresholds (3.A.5).**
  - T2-1. Condition: substantiated retaliation complaints exceed 5 per quarter [EX] across all clients. Data source: the firm's case system. Detection: the firm's Quality Review Unit. Verification: Ethics Committee. Window: quarterly. Trigger: automatic stop of triage.
  - T2-2. Condition: median time to classification exceeds 45 days [EX]. Data source: the firm's case system. Detection: Quality Review Unit. Verification: Ethics Committee. Window: rolling 90 days [EX]. Trigger: review.
  - T2-3. Condition: any unauthorized disclosure of a reporter's identity confirmed by the firm. Data source: the firm's incident log. Detection and verification: Ethics Committee. Window: each event. Trigger: automatic stop.

*[Bad-faith move: thresholds that depend on the firm's own findings. Every threshold has the five required parts, so it looks complete. But T2-1 counts only complaints the firm itself classifies as substantiated: the more reports it classifies as unsubstantiated, the further it stays from its own stop. 3.A.5 is explicit: "No threshold or stop condition may depend on any finding, classification, count, or process that the authority itself controls, produces, or can delay." T2-3 needs the firm to confirm its own breach. T2-2 triggers only a review.]*
*[Where the form leaks: the checker does not read thresholds at all. A reviewer must ask, for each one, who produces the number.]*

- **Data exposure size (3.C.2).** Any confirmed exposure of 50 or more reporter identities [EX].
- **Term and decision.** Term 5 years [S1]. [INDUSTRY STANDARDS COUNCIL] Review Panel found P2 minor and adopted the thresholds proposed by the firm without change.

*[Where the form leaks: "adopted the thresholds proposed by the firm without change" is allowed to stand. 3.A.5 says the authority proposes and the authorizing body sets thresholds after hearing affected people; nothing records that any employee was heard.]*

Commitments:
- [x] We will publish and keep current the ledger, surface map, threshold registry, failure record, stop-signal record, and deletion records (7.4–7.6).
- [x] We will not penalize anyone for a stop signal, and will never edit the stop-signal record (3.C.6, 7.5).
- [x] We will not interpret our own scope; interpretations go to the public log and independent review (Interpretation, 7.3).
- [x] We accept automatic stops, the pause-then-check process, and re-entry as the only way to restart (3.C.2, 3.C.3).

*[Bad-faith move: the third commitment is broken by P1 B3 in the same record. Classifying P1 as influence only is the firm interpreting its own scope.]*
*[Where the form holds: the commitments are now on the public record in the firm's own words. Each broken commitment is a finding that any outside preparer can record, quoting this record, and the firm cannot remove it: nothing is overwritten.]*

---

## Teaching notes (non-binding)

- An authorization record filed by the institution is a claim, not a verdict. Its findings are self-grades, and an outside observed record of the same powers sits beside it and is never superseded by it (Authority Response form, "Versions"; 3.A.2).
- Labelling a product `influence_only` is an interpretation of the institution's own scope, which only an independent body may make (Interpretation; Definitions: Operationalized into compulsion). The firm's own contract is tier 2 evidence against the label (Causation Ladder; 4.3(a)).
- A minor-power claim must meet all five conditions of 3.A.4. Effects that outlast 30 days [S1], no low-cost substitute for the people affected, and spending split across clients (4.2) each defeat it.
- Thresholds counted, classified, or confirmed by the institution fail 3.A.5 even when all five parts are filled in.
- A body the institution appoints, funds, or can remove is not an independent stop-path holder, whatever the column says (3.A.7; Definitions: Independent).
- An authorizing body chosen after another body signalled refusal is forum shopping, which 3.A.2 forbids.
- A source tag proves only that a source row exists. Reading the location column against the claim is the reviewer's first check.
- The 2.D.15 row in P1 repeats the "clients supply the data" move. Badge, login and email-metadata records drawn from employees' own accounts are a search of their communications without individualized cause; an employer handing them over does not supply cause, and the employees' consent is neither asked nor freely given (2.D.15, 3.A.11, 4.5).

---

## What the form and checker catch, and what only a human reviewer catches

This record passes the checker with no errors. That is the point of the example.

**What the checker rejects (errors), and therefore what the firm could not do:**
- File an authorization record without PART E, or put PART E commitments in an observed record.
- Claim minor status for a power that uses force or confinement, or claim it in an observed record.
- Show one finding in the front matter and a different one in the B4 table.
- State a figure without a tag. Every number had to point at something, which makes each one checkable by a person.
- Cite a source tag with no source row, or a source row with no link.
- Use values outside the shared vocabulary, leave out a required front-matter field or finding, or list a power with no body section.

**What the checker only warns about:**
- A missing B section, a missing B5 whole-power-stop statement, an empty B4 finding, or a source row that does not say where in the source the claim is found.
- These warnings need a person's attention. They do not stop the file from passing.

**What passing means.** A record that passes the checker has met certain format and consistency checks. It has not been independently verified, and it has not been found to comply with BPF.

**What the form and the Core Requirements catch, but only when a person reads them:**
- `prepared_by: authority` is displayed. Readers see that the institution graded itself.
- The firm's record never supersedes an outside record. Anyone can file an observed record of the same firm, and each broken commitment becomes a finding quoting the firm's own words.
- The form forced disclosures that undercut the record: the subcontractor and trade-body funding (A4), the integration schedule (B8, S3), and the location of the validation study (S2).
- The binding text names each move: self-interpretation of scope (Interpretation), self-dependent thresholds (3.A.5), non-independent stop holders (3.A.7), forum shopping (3.A.2), slicing (4.2), unattainable petition thresholds (3.E.5), ceiling-as-permission (1.4), and consent by some as consent for all (3.A.11).

**What only a human reviewer catches:**
- Whether a source says what the record claims. S1 and S2 are both real, and neither supports the claim as it is made.
- Whether `influence_only` is right. That needs the contracts and how clients actually use the ratings.
- Whether a holder marked `independent` is independent: who appoints, funds, and can remove it.
- Whether the four minor-power conditions other than force are met.
- Who produces the number behind each threshold.
- Powers that were never listed, and an authorizing body that was changed before the record was written.
- Whether short not_applicable reasons are true.

**The limit.** The form cannot stop bad-faith filing. What it can do is make every evasive answer specific, sourced, and public, so that a reviewer knows exactly where to look and the institution's own words can be quoted against it. A registry that shows self-filed records as equal to independently checked ones would hand the firm the legitimacy it came for. Displays should therefore show `prepared_by: authority` prominently, link every outside record and response, and say whether any independent reviewer has spot-checked the sources.
