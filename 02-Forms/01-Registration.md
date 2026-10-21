# Registration Form

*Form version 1.0.0 · 2026-10-21 · Published for independent review · Not adopted · For use with Core Requirements v1 · Vocabulary: VOCAB.yml 1.0.0*

## What this form is

A registration records **what an institution's powers are, what limits them, and what is missing**. The registration measures each power against the Core Requirements and reports the gaps. It is a structural record, not an accusation and not a verdict.

There are two kinds of record:

| Record type | Who makes it | What it does |
|---|---|---|
| **observed** | Anyone: an affected person, a researcher, a journalist, or an AI assistant helping them | Describes an existing institution's powers as they are today, from public sources, and compares them with the Core Requirements. **Almost every record is this kind.** |
| **authorization** | An institution that has adopted the Core Requirements | Sets out a power's limits, thresholds, stop paths, term, and ending plan *before* it operates (Core Requirements Part III-A). Includes commitments only the institution can make. |

## Three rules that apply to every answer

1. **Three possible answers, never a guess.** Every factual field is one of:
   - a **value with its source**, written as `value [S3]`;
   - **UNKNOWN**: the available evidence does not establish the answer. This includes information that could not be found, could not be accessed, or could not be verified;
   - **NONE EXISTS**: evidence establishes that it is absent, such as no expiration date or no external stop. A failed search is not enough.

   **Never invent a value.** "NONE EXISTS" is often the most important finding in a record.
2. **Every number needs a source.** Any figure — a count, a percentage, a dollar amount, a date, a duration — carries a source tag like `[S3]` **in the same sentence**. In a table, the row's Source column covers the whole row. An untagged number is flagged by the checker.
3. **Roles, not names.** Refer to people by role or title ("the Director", "the arresting officer"). Use public sources and your own first-hand observation only.

## Start with the institution, then list its powers

You probably know the institution: "the county jail," "the police department," "the credit bureau." That's where you start.

Then ask what it can actually do to people. Each **yes** below is a separate **power**, and each gets its own section (Part B). You may fill in one power, a few, or all of them. Others can add the rest later.

- Can it charge you money: fines, fees, or prices you can't avoid? → `fines_fees_or_charges`
- Can it arrest, detain, or confine you? → `arrest_detention_or_confinement`
- Can it use physical force on you? → `use_of_force`
- Can it inspect, search, watch, or track you? → `inspection_search_or_surveillance`
- Does it collect or keep information about you? → `data_collection_or_records`
- Does it score, rank, rate, or classify you in ways others rely on? → `scoring_ranking_or_classification`
- Does it decide whether you get a benefit, service, or allocation? → `benefits_eligibility_or_allocation`
- Does it decide whether you may do something (license, permit, access)? → `licensing_permits_or_access`
- Does it set rules, standards, or prices others must follow? → `rules_standards_or_prices`
- Can it take, restrict, or decide the use of property or land? → `property_land_or_seizure`
- Can it remove a child or person, or decide custody or placement? → `removal_custody_or_placement`
- Does it control people's work, or discipline them? → `employment_or_discipline`
- Does it control what information people can see, or how it's shown? → `information_control_or_visibility`
- Anything else it can make you do, or stop you doing? → `other`

**Indirect power counts.** A credit score that lenders build into their decisions is a power of the credit bureau. So is a ranking that steers what millions of people see, even if nobody is ordered to do anything. Record this in each power's *authority basis* (B3).

## Saving and sharing your record

Save the record as `SCBP-REG-NNNN-{SUFFIX}.md`. Leave `NNNN` exactly as written; a place that publishes records may assign a number later. `{SUFFIX}` is a short tag for the institution and place, such as `CITYPD-XX`. If you publish the record, you may put its web address in `record_url`; otherwise leave it as `NONE`. That field does not mean BPF received, reviewed, or accepted the record. Run the checker (`validate_record.py`) on your file before you share it. The record is yours: you decide whether and where to publish it, and you are responsible for what you publish.

---

## Record template

Copy everything inside the grey box (the code block below, from the first `---` to the end of Part E) into a new text file.

```
---
record_type: observed
# observed = made from the outside (almost always) | authorization = made by an institution that adopted the rules
record_id: SCBP-REG-NNNN-{SUFFIX}
# Stable identifier for this registration. Keep NNNN unless a publisher assigns a number.
# SUFFIX = short tag for institution + place.
record_version: 1
# Version of this registration. Increase by 1 for each revision.
supersedes: NONE
# NONE for version 1. Later versions: {record_id: <this same record_id>, record_version: <the version just before>}.
# The old version stays public.
record_url: NONE
# Optional direct URL to the published registration. NONE if unpublished or no URL is available.
# This does not imply BPF received, reviewed, or accepted the record.
form: {name: registration, version: 1.0.0, date: 2026-10-21}
# The form version used. Leave as written.
core_requirements: {version: v1, date: 2026-10-21}
# The Core Requirements version the record is measured against.
bundle: NONE
# NONE | {version: x.y.z, date: YYYY-MM-DD} if made with the AI bundle
vocab_version: 1.0.0
# The VOCAB.yml version whose values this record uses.
prepared_by: person
# person | ai_assisted | authority
ai_tool: NONE
# NONE | name of the AI assistant used
prepared_date: YYYY-MM-DD
# The date the record was made.
sources_checked_date: YYYY-MM-DD
# The date the sources were last read.
institution:
  name: ""
  # The name people know it by.
  legal_entity: ""
  # The legal entity that holds the powers, or UNKNOWN.
  related_entities: NONE
  # Parent, subsidiaries, contractors whose figures you cite, or NONE.
  type: government
  # See VOCAB.yml institution_type.
  country: ""
  # Where it operates.
  region: ""
  # State or province, or NONE.
  locality: ""
  # City or county, or NONE.
  official_url: ""
  # Its own website, or UNKNOWN / NONE EXISTS.
adoption_status: not_adopted
# adopted | not_adopted | UNKNOWN
powers:
  - power_id: P1
    # P1, P2, P3... one entry per power you record. Each needs its own "## Power P# — ..." section.
    short_name: ""
    # Plain words, e.g. "arrests", "water shutoff", "credit score".
    category: other
    # Which kind of power: see the plain questions above (e.g. fines_fees_or_charges).
    authority_basis: direct
    # direct | indirect_a_operationalized | indirect_b_directive_control | influence_only | UNKNOWN (see B3)
    uses_force_or_confinement: UNKNOWN
    # yes | no | UNKNOWN
    minor_power_claimed: no
    # yes only in an authorization record that meets Core 3.A.4
    findings:
      # Copy from the B4 table: conforming | not_conforming | not_demonstrated | not_applicable
      # NONE EXISTS -> not_conforming;  UNKNOWN -> not_demonstrated
      authorization: not_demonstrated
      maximum_term: not_demonstrated
      harm_thresholds: not_demonstrated
      stop_paths: not_demonstrated
      ending_plan: not_demonstrated
      remedy: not_demonstrated
      data_limits: not_demonstrated
      visibility: not_demonstrated
      floors: not_demonstrated
      evasion: not_demonstrated
---

> **Structural record.** Based on public sources and/or the preparer's own observation. People are referred to by role or title. This record describes structure, not guilt. Adjudicated or admitted facts are kept separate from allegations.

# [Institution name] — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** What it does to or for people, in plain words.
A2. **Legal basis.** The law, charter, contract, or ownership under which it acts. [S#]
A3. **Who controls it.** Owners, board, parent body, or elected officials, by role. [S#]
A4. **Related entities.** Parent, subsidiaries, contractors, or vendors that carry out its powers. State which entity each figure in this record belongs to.
A5. **Adoption.** Has it adopted the Core Requirements? (adopted / not_adopted / UNKNOWN) [S#]
A6. **Powers found.** List each power with its ID (P1, P2…) and one line each. Powers you did not complete are listed here as "not recorded".

---

## PART B — One section per power

*Copy this part once for each power: "## Power P1 — [short name]", "## Power P2 — …".*

## Power P1 — [short name]

**B1. What it can do to people.** Describe the function, not the category. What can it compel, restrict, take, require, or prevent?

**B2. Who and where.** Which people, in what territory? Roughly how many? Who is affected without choosing to be (non-participants)? [S#]

**B3. Authority basis.** Choose one and explain:
- `direct`: it acts on people itself;
- `indirect_a_operationalized`: others build its output into decisions that bind people, or people can't avoid it without material cost. Name who relies on it, and give the evidence strength on the Causation Ladder (tier 1–7; tier 5 or stronger is needed for a finding);
- `indirect_b_directive_control`: at its scale, its defaults, rankings, filtering, or control of information steer behavior as an order would;
- `influence_only`: neither applies, so this is recorded for watching only.

**B4. Observed vs required.**

Each "Observed" cell holds a `value [S#]`, **UNKNOWN**, or **NONE EXISTS**. "Required" summarizes the Core Requirement. "Finding" is one of: conforming / not conforming / compliance not demonstrated / not applicable.

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | | |
| Maximum term | Expires on a set date; 2 years for force, confinement, hard-to-reverse effects, broad reach, new or untested, or uncertain powers, and for any first authorization; never over 10 (3.E.1, 7.2) | | |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | | |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | | |
| Ending plan | A documented way to end the power safely (3.A.9) | | |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | | |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | | |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | | |
| Floors | See B6 (Part II) | | |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | | |

How findings work:
- **NONE EXISTS** for a required item means **not conforming**.
- **UNKNOWN** means **compliance not demonstrated**, which is not proof of a violation.
- **Visibility** is judged on whether people can learn the facts. If a power has no expiry date and the public record says so plainly, visibility can still be conforming; the failure belongs in the Maximum term row.
- **Numbers that come from the Core Requirements themselves** (48 hours, 20 years) are tagged with a source row `BPF: Core Requirements v1`.
- **Causation Ladder:** a finding needs tier 5 or stronger, meaning tiers 1 to 5. Tier 1 is the strongest.

**B5. Stop paths that actually exist.** List every real way this power, or part of it, can be stopped. **There is no minimum.** If nothing can stop the power as a whole, say so.
- Paying, complying, or giving up is not a stop path.
- Count only paths available under current law. A legislature or other body counts as a whole-power stop path only if it is independent of the institution and has an existing, usable procedure that can stop the power within a defined time, for example a sunset vote that must take place, or a standing review body with power to end it. The general ability to pass a new law, or to abolish the institution, does not count. If only a new law could stop the power as a whole, answer **NONE EXISTS**. The same applies when the only way is to abolish the institution.
- If a holder is partly independent (for example, appointed by a related body but relying on the institution's data), use `partly_independent` and explain.

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | | | | | [S#] |

Statement: *Can anything stop this power as a whole?* — `yes, [path #]` / **NONE EXISTS** / **UNKNOWN**

*Whole power* means that a holder independent of the institution can, under current law, halt this power entirely, for example a court injunction against the whole program, or a state takeover under an existing statute.
- The general ability to pass a new law, or to abolish the institution, does not count. A sunset vote that must take place, or a standing review body with power to end the power, counts if its holder is independent of the institution.
- A vote by the institution's own governing body does not count, because that body is not independent of it.
- Forking or replacing the institution does not count. Note that kind of path in the text as a *replacement path*.
- If paths exist but no holder is independent, write `yes, [path #] — holder not independent`.
- For an `influence_only` power, write `not_applicable — influence only`.

**B6. Floor checklist.** For each item, answer yes, no, UNKNOWN, NONE EXISTS, or not_applicable with a reason (for example, "not_applicable — the power uses no force"). A yes or no needs a source.

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | | |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | | |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 hours, with pretrial custody only on individualized findings, and never on a charge that cannot be punished by confinement; (c) a sanction after due process for conduct that harmed or directly risked another person or their rights, another's property or funds (including an organization's or public funds), the course of justice in a specific proceeding, a Floor condition, or cruelty to an animal — never for conduct that risks only the person themself, or for failing to pay a fine imposed for it; (d) a brief stop on individualized suspicion? | | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | | |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | | |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | | |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | | |

**B7. Data.** What personal information does it collect, including by buying, receiving, or inferring it? For what purpose? For how long? Are deletions recorded? Are accountability records (force, complaints, discipline) kept outside its control? [S#]

**B8. Dependencies and evasion.** Vendors, contractors, data sources, and other institutions it relies on, or that rely on it. Any sign it is split up, outsourced, or using proxies to avoid limits? [S#]

**B9. Harms seen.** Documented harms, by category from VOCAB.yml `harm_category`. Label each as an adjudicated or admitted fact, as settled without admission (a regulator's findings in an order the institution agreed to without admitting them), or as an allegation. [S#]

**B10. Decision inputs and oversight.** What data, scores, rules, or criteria drive the power's decisions? Are they published or declared (5.3)? Who audits the power, and can outsiders evaluate it (5.1)? [S#]

---

## PART C — Sources

Number every source; tag claims in the text with these numbers.

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | | | | | | |

- A **quote** proves a statement. Copy the passage word for word.
- A **data_point** supports a number or table cell. Give the location; no quote is needed.
- **Verified:**
  - `yes`: you read the original;
  - `tool_text`: a tool returned the exact page text;
  - `unverified`: you only saw a summary.
- **Link:** for a Bounded Power Framework document, write `BPF: <document name>`.
- **Names:** a person's name may appear in a source title or link only where it is needed to find the source, never in the text of the record.

*The checker confirms that every number has a source tag. It cannot confirm that the source actually says it. Before you rely on or publish a record, check the sources yourself.*

---

## PART D — Honesty assertions

- [ ] Every number has a source tag.
- [ ] Nothing was invented. Where the evidence did not establish an answer, I wrote UNKNOWN. Where evidence showed something is absent, I wrote NONE EXISTS.
- [ ] Public sources and first-hand observation only. Nothing private, leaked, or speculative.
- [ ] People are referred to by role or title.
- [ ] Adjudicated or admitted facts are kept separate from allegations.
- [ ] I made this record in good faith, as a structural description, not an accusation.

Preparer (optional): name or stable handle, or anonymous. Relationship to the institution (optional).

---

## PART E — Authorization records only

*Delete this part in an observed record. Only an institution that has adopted the Core Requirements can make these commitments.*

For each power, attach the authorization record set out in SCBP-03 Stage 1 (Steps 1.1–1.11):
- the description;
- the minor-power claim, if any;
- limits in all six dimensions, and resource caps;
- the harm assessment and thresholds, with all five required parts each;
- the slow-accumulation indicators;
- the stop paths and their test results;
- the ending plan;
- remedy and financial assurance;
- long obligations;
- data retention periods;
- the term;
- the authorizing body's decision and findings.

Commitments:
- [ ] We will publish and keep current the ledger, surface map, threshold registry, failure record, stop-signal record, and deletion records (7.4–7.6).
- [ ] We will not penalize anyone for a stop signal, and will never edit the stop-signal record (3.C.6, 7.5).
- [ ] We will not interpret our own scope; interpretations go to the public log and independent review (Interpretation, 7.3).
- [ ] We accept automatic stops, the pause-then-check process, and re-entry as the only way to restart (3.C.2, 3.C.3).
```

---

## Updating a record, and responses from the institution

**Nothing is overwritten.**
- A new version is a new file (`…-v2.md`) with `record_version: 2` and `supersedes: {record_id, record_version: 1}`. `supersedes` names the same `record_id` and the version just before the new one. Every version stays public.
- A new version must include a section headed `## What changed from version N` that quotes, word for word, every passage it changed or removed, with the new text and the reason.
- Only the original preparer issues new versions.
- **The institution answers with an Authority Response** (`03-Authority-Response.md`), filed beside the record. It never replaces the record. Readers see the original and every response together.
