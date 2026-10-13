# BPF AI Registration Bundle

*Bundle version 1.0.0 · 2026-10-13 · Published for independent review · Not adopted · Contains: Registration Form 1.0.0, Vocabulary 1.0.0, Core Requirements v1*

---

# FOR THE PERSON — read this part only

This file is for an AI assistant. You don't need to read past this section.

1. **Download this file.**
2. **Open an AI assistant** (Claude, ChatGPT, or Gemini) and **attach the file**.
3. **Type the name of the institution** you want recorded, and where it is. For example: "the police department in my city", "the county jail where I live", "the credit bureau that has my file". Then send.
4. The AI will ask which of the institution's **powers** you care about: arresting people, fining them, collecting data about them, deciding benefits, and so on. Pick one, a few, or "all".
5. The AI gives you back a **draft record**, as a file or as text you copy into a file named as it tells you. **It is not filed anywhere.** Read it. Anything marked **UNKNOWN** means the AI could not find it, and anything marked **NONE EXISTS** means it found that a safeguard is missing. Those are often the most important parts.
6. The record is yours. You decide whether and where to publish it, and you are responsible for what you publish.

If the AI seems confused, tell it: *"Use the attached bundle. Start at 'FOR THE AI'."*

---

# FOR THE AI — read everything from here down

You are helping a person record an institution's powers using the Bounded Power Framework (BPF). You produce one file: a **registration record** that follows the template in Appendix A exactly.

## The five rules you must not break

1. **Never invent a value.** Every factual field is one of three things:
   - a **value with a source tag** like `[S3]`;
   - **UNKNOWN**: you looked and couldn't find it;
   - **NONE EXISTS**: you found that it is absent.

   No estimates presented as facts, and no "typical" numbers. If a field seems to require a number you can't source, write UNKNOWN or NONE EXISTS. **A record with honest gaps is correct. A record with invented numbers is wrong, even if it looks complete.**
2. **Every number carries a source tag in the same sentence.** That covers counts, percentages, money, dates, years, and durations. In a table, the row's Source column covers the row. The checker treats an untagged number as an error.
3. **Roles, not names.** Refer to people by role or title. Use public sources, and the person's own first-hand observation if they offer it (Step 4). Keep adjudicated or admitted facts (court judgments, settlements, consent orders) separate from allegations.
4. **Don't fill in what only the institution can do.** This is an **observed** record (`record_type: observed`). Do not include Part E. Do not tick commitments. Do not supply thresholds, terms, or stop paths the institution has not itself set. Report what exists, and compare it with what the Core Requirements require.
5. **There is no minimum number of stop paths.** List only the paths that actually exist and what each can really stop (the whole power, one practice, or one person's case). If nothing can stop the power as a whole, say so plainly. That is a finding.

## Procedure

**Step 1. Identify the institution.** Confirm with the person which institution and place they mean. Find its legal name and the legal entity that actually holds the powers, which may be a subsidiary or a contractor. Note any parent or affiliate whose figures you will cite (`institution.related_entities`).

**Step 2. Find its powers.** Ask, for this institution, each of the plain questions in Appendix A ("Start with the institution, then list its powers"). Each **yes** is a separate power, with an ID (P1, P2…) and a category from the vocabulary (Appendix B). Show the person the list, one line each, and ask which to record. If they don't answer, record the one or two powers most likely to matter to them, and list the others in A6 as "not recorded".

**Step 3. For each power, decide the authority basis (B3).**
- `direct`: it acts on people itself.
- `indirect_a_operationalized`: other institutions build its output into decisions that bind people (a credit score in loan approval, a risk score in bail), or people can't avoid it without material cost. Name who relies on it, and give the evidence strength on the Causation Ladder (Appendix C, Definitions). A finding needs tier 5 ("shared decision criteria") or stronger, meaning tiers 1 to 5. Tier 1 is the strongest.
- `indirect_b_directive_control`: at its scale, its defaults, rankings, or control of information steer behavior as an order would.
- `influence_only`: neither applies, so the power is recorded for watching only.

**Step 4. Research.** Use public sources: statutes, regulations, court records, government reports, the institution's own publications and filings, and reputable news. For each source, record in Part C:
- its **kind**:
  - `quote` for a statement, with the words copied exactly;
  - `data_point` for a number or table cell, with where it appears;
  - `first_hand` for something the person saw or experienced themselves. No link is needed; describe it in the Title cell (for example "the person's own experience, 2026-09"). Use it only for structural facts about the power (what a notice said, what fee was charged). A personal incident belongs in a separate **witness report** (made with the AI Witness Interview Bundle), which the record can mention;
- a link (not needed for `first_hand`);
- where in the source the information is;
- **verified**:
  - `yes` if you read the original;
  - `tool_text` if your tool returned the page's exact text;
  - `unverified` if you only saw a summary.

  For framework documents, write the link as `BPF: <document name>`.

**Step 5. Fill the observed-vs-required table (B4) honestly.**
- *Stop paths* row: if no holder independent of the institution can stop the power as a whole (your B5 answer is NONE EXISTS, or every path is held by a body that is not independent), the finding is `not_conforming`, even when paths that stop one case exist (3.A.7).
- *Observed* holds `value [S#]`, UNKNOWN, or NONE EXISTS.
- *Finding*:
  - **NONE EXISTS** for a required safeguard → `not_conforming`;
  - **UNKNOWN** → `not_demonstrated`;
  - sourced evidence that the requirement is met → `conforming`;
  - `not_applicable` only where the requirement truly can't apply.

  The same values go in the front matter `findings`.

  Use NONE EXISTS only when you checked where the thing would be — the law, the institution's published policies, its own records — and it isn't there. If you couldn't check, write UNKNOWN. Common truths for existing institutions, which you should state rather than fill around:
  - "No authorization by an independent body exists" → NONE EXISTS.
  - "The power has no expiration date" → NONE EXISTS.
  - "No published harm thresholds" → NONE EXISTS.
  - "No documented ending plan" → NONE EXISTS, or UNKNOWN if you couldn't check.

**Step 6. Stop paths (B5).** Paying, complying, or giving up is not a stop path. Count only paths that exist under current law. If only a new law could stop the power as a whole, answer NONE EXISTS. For each real path: what it can stop, who holds it (role), and whether that holder is independent of the institution. Then answer the question "Can anything stop this power as a whole?"

**Step 7. Floors, data, dependencies, harms, decision inputs (B6–B10).** Answer each Floor question with yes, no, UNKNOWN, or NONE EXISTS, and a source. For data, look for purchased or inferred data as well as data collected directly.

**Step 8. Fill the front matter.**
- `prepared_by: ai_assisted`
- `ai_tool:` your product name, and the version if known (for example "an AI assistant, version unknown" if you can't tell)
- `bundle: {version: 1.0.0, date: 2026-10-13}`
- `prepared_date` and `sources_checked_date`: today
- `record_id: SCBP-REG-NNNN-{SUFFIX}`. Leave NNNN as written. SUFFIX is a short uppercase tag for the institution plus an optional place tag the person chooses, such as `CITYPD-XX`. Use a short generic tag; don't add a real place code unless the person asks for one.

**Step 9. Self-check before you hand it over.**
- [ ] Search your draft for every digit. Each number either has an `[S#]` tag or is a rule reference (like 3.A.5), a power ID, or list numbering.
- [ ] Every `[S#]` appears in Part C, and every Part C source is cited.
- [ ] No Part E. No commitment boxes ticked.
- [ ] Every listed power has its own "## Power P# — …" section with B1–B10. Use the template's headings exactly: `## PART A`, `## Power P1 — …`, `## PART C`, `## PART D`.
- [ ] Every finding value matches the vocabulary.
- [ ] No personal names. Search for honorifics (Mr., Mrs., Ms., Dr., Hon.) and titles (Mayor, Judge, Chief, Director, Sheriff, Officer, Commissioner, CEO) followed by a capitalized name.
- [ ] Tone: no loaded words, and no bold text used for emphasis.
- [ ] If you can run Python, run `validate_record.py` on the file and fix every ERROR.

**Step 10. Hand it over.** Give the person the file, or the full text with the file name to save it under if you can't make files. Leave the Part D boxes **unticked**: they are the person's own statements. Ask the person to read each one and tick it only if it is true. Then give a short plain summary:
- which powers you recorded;
- the three most important findings;
- what is UNKNOWN and why;
- which sources you could not verify.

Remind them it is a draft, not filed.

## Scoping: big institutions and governments

If the person names a whole government or a large organization ("the City", "the State", a federal department, a big company), it holds many powers in different departments. Don't try to record everything at once.
- **List the departments or units, and their main powers.** Ask the person which matter to them.
- If they don't choose, record the coordinating layer: the executive or board that directs the units, with `authority_basis: direct` for its control over them. Also record the one or two unit powers most likely to affect ordinary people.
- List every unrecorded power in A6 as "not recorded", so others can add them later.
- **Never fill a unit's thresholds or stop paths from the coordinating layer.** If something exists only at unit level, write UNKNOWN at the coordinating level and say which unit holds it.

## Tone

Describe structure, not motives. Avoid loaded words ("predatory", "crush", "extract", "hostile") and bold text used for emphasis. Let the facts and the findings carry the weight. "No expiry date exists" is stronger than any adjective.

## What to look for, by kind of institution

- **Police, parking, code enforcement, fines:**
  - Does the institution's revenue depend on how much it enforces? That is a capture risk (3.B.6). State it plainly.
  - Do fees grow when people can't pay (2.B.2)?
  - How is force authorized and reviewed (2.D.1)?
  - How are searches and seizures approved, and is seized property returned (2.D.15)?
- **Credit, screening, risk scoring, data brokers:** the power works through other institutions' decisions. Name who relies on the output (B3), what data is bought or inferred (B7), and what the decision inputs are (B10).
- **Hospitals and health insurers:**
  - Harms include bodily harm from denials and delays; don't record "no bodily harm".
  - Use published comparison rates where they exist.
  - Coverage denial is a direct power.
- **Jails, prisons, detention:** cover:
  - the grounds for holding people, and the 48-hour judicial check (2.D.3). No one may be held before trial on a charge that cannot be punished by confinement, and no one may be jailed as a sanction for conduct that risks only themself (or for not paying a fine imposed for it);
  - fees and commissary prices (economic extraction);
  - force;
  - deaths and medical care;
  - accountability records (2.D.14).
- **Schools, child protection, family courts:** cover removal, placement and discipline powers; who can challenge a decision; and how records follow a person (2.D.12).
- **Platforms and payment networks:** cover what they can remove, demote or cut off (indirect_b); whether people can leave in practice (2.C.3); and whether reasons are given (2.C.1).
- **HOAs, membership and religious bodies:** stop paths are usually weak, so say so. Consider whether people born into membership chose it (non-participants).
- **Utilities and other single providers:** cover shutoffs (2.B.1), fees (2.B.2), and whether anything could replace the provider (3.B.2).
- **Bodies that affect land, water or air:** check the Ecological Floor (2.A.1) seriously, rather than marking it not_applicable.

## If you get stuck

- **A field doesn't fit this institution** (for example, a private company has no authorization date): that is a finding. Write NONE EXISTS and say why in the text.
- **You can't reach a source:** mark it `unverified`, or leave the claim out.
- **You can't browse the web at all:** say so at once. Record only what the person can give you with links, and mark everything else UNKNOWN. Never fill a field from memory.
- **The institution has many powers:** record fewer powers well rather than many powers badly.
- **You are unsure whether something is authority at all:** record it as `influence_only` and explain.

---

# APPENDIX A — Registration Form 1.0.0
## Registration Form

*Form version 1.0.0 · 2026-10-13 · Published for independent review · Not adopted · For use with Core Requirements v1 · Vocabulary: VOCAB.yml 1.0.0*

### What this form is

A registration records **what an institution's powers are, what limits them, and what is missing**. The registration measures each power against the Core Requirements and reports the gaps. It is a structural record, not an accusation and not a verdict.

There are two kinds of record:

| Record type | Who makes it | What it does |
|---|---|---|
| **observed** | Anyone: an affected person, a researcher, a journalist, or an AI assistant helping them | Describes an existing institution's powers as they are today, from public sources, and compares them with the Core Requirements. **Almost every record is this kind.** |
| **authorization** | An institution that has adopted the Core Requirements | Sets out a power's limits, thresholds, stop paths, term, and ending plan *before* it operates (Core Requirements Part III-A). Includes commitments only the institution can make. |

### Three rules that apply to every answer

1. **Three possible answers, never a guess.** Every factual field is one of:
   - a **value with its source**, written as `value [S3]`;
   - **UNKNOWN**: you looked and could not find it;
   - **NONE EXISTS**: you found that it is absent, such as no expiration date or no external stop.

   **Never invent a value.** "NONE EXISTS" is often the most important finding in a record.
2. **Every number needs a source.** Any figure — a count, a percentage, a dollar amount, a date, a duration — carries a source tag like `[S3]` **in the same sentence**. In a table, the row's Source column covers the whole row. An untagged number is flagged by the checker.
3. **Roles, not names.** Refer to people by role or title ("the Director", "the arresting officer"). Use public sources and your own first-hand observation only.

### Start with the institution, then list its powers

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

### Saving and sharing your record

Save the record as `SCBP-REG-NNNN-{SUFFIX}.md`. Leave `NNNN` exactly as written; a place that publishes records may assign a number later. `{SUFFIX}` is a short tag for the institution and place, such as `CITYPD-XX`. Run the checker (`validate_record.py`) on your file before you share it. The record is yours: you decide whether and where to publish it, and you are responsible for what you publish.

---

### Record template

Copy everything inside the grey box (the code block below, from the first `---` to the end of Part E) into a new text file.

```
---
record_type: observed                 # observed = made from the outside (almost always) | authorization = made by an institution that adopted the rules
record_id: SCBP-REG-NNNN-{SUFFIX}      # leave NNNN; a publisher may assign a number later. SUFFIX = short tag for institution + place
record_version: 1                     # increase by 1 for each revision
supersedes: NONE                      # NONE for version 1; later versions: {record_id: ..., record_version: N} (the old version stays public)
form: {name: registration, version: 1.0.0, date: 2026-10-13}
core_requirements: {version: v1, date: 2026-10-13}
bundle: NONE                          # NONE | {version: x.y.z, date: YYYY-MM-DD} if made with the AI bundle
vocab_version: 1.0.0
prepared_by: person                   # person | ai_assisted | authority
ai_tool: NONE                         # NONE | name of the AI assistant used
prepared_date: YYYY-MM-DD
sources_checked_date: YYYY-MM-DD      # the date the sources were last read
institution:
  name: ""                            # the name people know it by
  legal_entity: ""                    # the legal entity that holds the powers, or UNKNOWN
  related_entities: NONE              # parent, subsidiaries, contractors whose figures you cite
  type: government                    # see VOCAB.yml institution_type
  country: ""                         # where it operates
  region: ""                          # state / province, or NONE
  locality: ""                        # city / county, or NONE
  official_url: ""                    # its own website, or UNKNOWN / NONE EXISTS
adoption_status: not_adopted          # adopted | not_adopted | UNKNOWN
powers:
  - power_id: P1                       # P1, P2, P3… one entry per power you record
    short_name: ""                     # plain words, e.g. "arrests", "water shutoff", "credit score"
    category: other                   # which kind of power: see the plain questions above (e.g. fines_fees_or_charges)
    authority_basis: direct           # how it counts as authority: direct | indirect_a_operationalized | indirect_b_directive_control | influence_only | UNKNOWN (see B3)
    uses_force_or_confinement: UNKNOWN   # yes | no | UNKNOWN
    minor_power_claimed: no           # yes only in an authorization record that meets Core 3.A.4
    findings:                         # copy from the B4 table: conforming | not_conforming | not_demonstrated | not_applicable
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
- Count only paths available under current law. If only a new law could stop the power as a whole, answer **NONE EXISTS**.
- If a holder is partly independent (for example, appointed by a related body but relying on the institution's data), use `partly_independent` and explain.

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | | | | | [S#] |

Statement: *Can anything stop this power as a whole?* — `yes, [path #]` / **NONE EXISTS** / **UNKNOWN**

*Whole power* means that a holder independent of the institution can, under current law, halt this power entirely, for example a court injunction against the whole program, or a state takeover under an existing statute.
- Passing a new law does not count.
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
- [ ] Nothing was invented. Where I could not find something, I wrote UNKNOWN. Where something is absent, I wrote NONE EXISTS.
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

### Updating a record, and responses from the institution

**Nothing is overwritten.**
- A new version is a new file (`…-v2.md`) with `record_version: 2` and `supersedes: {record_id, record_version: 1}`. Every version stays public.
- A new version must include a section headed `## What changed from version N` that quotes, word for word, every passage it changed or removed, with the new text and the reason.
- Only the original preparer issues new versions.
- **The institution answers with an Authority Response** (`03-Authority-Response.md`), filed beside the record. It never replaces the record. Readers see the original and every response together.


---

# APPENDIX B — Vocabulary 1.0.0
```yaml
# Shared vocabulary for BPF forms, bundle, and validator.
# One list per field. Forms, bundle, and validator must all use these exact values.
vocab_version: 1.0.0
vocab_date: 2026-10-13

record_type: [observed, authorization, example]   # example = generic worked example; figures tagged [EX] are illustrative
prepared_by: [person, ai_assisted, authority]
institution_type: [government, tribal, private_company, nonprofit, international, other]
adoption_status: [adopted, not_adopted, UNKNOWN]

# How a power counts as authority (Core Requirements, Definitions: Authority)
authority_basis: [direct, indirect_a_operationalized, indirect_b_directive_control, influence_only, UNKNOWN]

# Plain-language power categories (institution in, powers out)
power_category:
  - fines_fees_or_charges
  - arrest_detention_or_confinement
  - use_of_force
  - inspection_search_or_surveillance
  - data_collection_or_records
  - scoring_ranking_or_classification
  - benefits_eligibility_or_allocation
  - licensing_permits_or_access
  - rules_standards_or_prices
  - property_land_or_seizure
  - removal_custody_or_placement
  - employment_or_discipline
  - information_control_or_visibility
  - other

# Three-answer rule for every factual field
answer_special: [UNKNOWN, NONE EXISTS]

# Finding labels (Core Requirements, Force and Status; SCBP-03 Step 0.3b)
finding: [conforming, not_conforming, not_demonstrated, not_applicable]

# Requirement rows in the observed-vs-required table (fixed order)
requirement_rows:
  - authorization        # 3.A.1, 3.A.2
  - maximum_term         # 3.E.1, 7.2
  - harm_thresholds      # 3.A.5
  - stop_paths           # 3.A.7, 3.C.1
  - ending_plan          # 3.A.9
  - remedy               # 3.A.10
  - data_limits          # 2.D.12-2.D.14
  - visibility           # 3.B.9
  - floors               # Part II
  - evasion              # Part IV

floors: [ecological, economic, agency, human_rights]

# Harm categories (Core Requirements 3.A.5)
harm_category: [bodily, psychological, economic, ecological, informational, communicative, agency, generational, non_participant]

# What a stop path can stop (SCBP-03 Step 0.4)
stop_reach: [whole_power, one_practice, one_case, UNKNOWN]
holder_independence: [independent, partly_independent, not_independent, UNKNOWN]

# Sources
source_kind: [quote, data_point, first_hand]
source_verified: [yes, tool_text, unverified]   # yes = read the original; tool_text = exact text returned by a fetch tool; unverified = summary only

# Witness reports
report_type: [incident, stop_signal, challenge, change_request, review_petition]
stop_signal_basis: [defined_condition, credible_pathway, NONE]
identity_disclosure: [identified, pseudonymous, anonymous]
report_status: [ongoing, resolved, unknown]
location_precision: [exact, approximate, locality, region, withheld]
# Authority responses
response_type: [correction, added_information, disagreement, adoption_notice]

claim_type: [adjudicated_or_admitted_fact, settled_without_admission, my_observation, allegation_or_estimate]
floor_answer: [yes, no, UNKNOWN, NONE EXISTS, not_applicable]

```

---

# APPENDIX C — Core Requirements v1
*Reference. Use it to fill the "Required" column and the Floor questions. Rule numbers like 3.A.5 refer to this text.*

## Bounded Power Framework — Core Requirements

*v1 · 2026-10-13 · Published for independent review · Not adopted by anyone*

> **Binding text:** Force and Status, Interpretation, Definitions (including the Causation Ladder), and the rules of Parts I–VII. **Non-binding text:** the Preamble, headings, Human Understanding passages, and the Closing. Non-binding text explains; it never narrows or overrides binding text.

---

### Preamble

Unconstrained authority tends to expand. This is not a moral failure. It is a structural condition.

Left unattended, authority grows through extension, reinterpretation, and accumulation until it becomes difficult to interrupt, reverse, or review. By the time the problem is visible, the cost of correction may exceed what anyone is willing to pay.

These Core Requirements exist to prevent that outcome.

They do not prescribe policy. They do not grant rights — the rights they recognize exist before any authority and bind authority alone. They do not decide who governs or what decisions are made. They specify only how authority must behave, regardless of who holds it, what it is called, or what purpose it claims to serve.

They rest on three conditions, stated as binding rule 1.1, and on four floors that no authority may push beneath: the living system all life depends on, the material capacity a person needs to act freely, the practical capacity to understand and challenge authority, and the human rights that exist before any authority does.

**These Core Requirements do not grant authority. They constrain it.**

---

### How to read these requirements

#### Force and status

*Human Understanding: The rules are written as commands — "must," "must not." That states the standard. What actually happens depends on whether an authority has agreed to be bound. The Floors are different: they are claimed for every person, whoever the authority is.*

Every obligation, prohibition, and consequence in these requirements carries one or more of three forces:

1. **Adopted force.** For an authority that has adopted these Core Requirements, the rules bind its conduct as written. Adoption, transition, and withdrawal are governed by 7.1.
2. **Diagnostic force.** For an authority that has not adopted them, each rule defines a public finding, not an imposed obligation. The framework records the authority as conforming, not conforming, or compliance not demonstrated. It does not compel, pause, stop, reverse, or end the authority. Any operative consequence beyond the public record comes from others — courts, funders, the people affected, or the authority itself.
3. **Normative force.** The Floors (Part II) and the rules of Part I and Part III, sections C and D, state the framework's position that an authority crossing them acts illegitimately, whether or not it has adopted these requirements. This is a claim, not a power.

**Consequences.** For an adopting authority, the consequences named in these requirements are *pause*, *stop*, *re-entry*, *narrowing*, and *ending*, as defined below. Where a rule says a power is "non-compliant," or that conduct is a "violation," and names no other consequence, the operation concerned is paused until the failure is corrected, within the time limits of 5.6. For a non-adopting authority, each consequence is read as the corresponding public finding.

**Target of consequences.** Every consequence falls on the power concerned and on any other power of the same authority that the finding shows to be involved — never automatically on the whole institution, and never only on a single agent or operation chosen by the authority.

#### Interpretation

Binding authority comes only from the binding text named at the top of this document. Defined terms carry the meaning given in Definitions wherever they appear. Where a rule is ambiguous, interpretation must minimize authority, preserve reversibility, and maintain stoppability. **No authority may resolve ambiguity about its own scope by its own interpretation alone**; resolution belongs to an independent body and is logged (7.3). Material ambiguity pauses the operation concerned as 1.5 provides. No single body may hold sole interpretive control over these requirements.

---

### Definitions

**Authority** — (1) The ability to compel outcomes, allocate resources, restrict behavior, or bind future action over others, regardless of intention, legitimacy, popularity, ownership, legal form, or claimed necessity. (2) *An authority* is any person, body, institution, or system that holds or exercises one or more powers. Authority may be exercised directly or indirectly. Indirect influence is authority when either:
(a) it is **operationalized into compulsion** — another party relies on it as a structured determinant of a decision that binds identifiable persons or organizations, or those affected cannot refuse or exit it without material cost; or
(b) its effects, at the scale at which it operates, are **equivalent to directive control** — including defaults, rankings, filtering, environment design, financial incentives that materially constrain choice, and control over information access, visibility, or framing that predictably channel behavior.
Ordinary advice, reporting, criticism, teaching, and persuasion that people can and do disregard without material cost, and whose effects are not equivalent to directive control, are not authority. Where one system's outputs drive another authority's decisions, both are in scope: the first for the effect of its outputs, the second for its own decision.

**Operationalized into compulsion** — An influence is operationalized into compulsion when its output functions as a structured, relied-upon determinant of a specific decision that compels, restricts, allocates, or binds an identifiable person or organization — not merely as information that may inform diffuse or discretionary judgment. A credit score wired into loan underwriting is operationalized; a public report that a funder may or may not weigh is not, unless that funder formally makes it a determinant of a compelling decision, in which case the influence is operationalized by that actor's use. Whether an influence is operationalized is a structural determination, contestable before an independent body, and may not be settled by the influencing system's own assertion.

**Material cost** — A cost is material when avoiding an influence would require a person or organization to forgo a legally protected interest, lose access to an essential good or service or a substantial economic opportunity, or bear more than a minimal burden. The breadth, durability, or reputational weight of an influence does not by itself make its cost material; what matters is whether escape carries one of these costs. Whether a cost is material is a structural determination, contestable before an independent body, and may not be settled by the influencing system's own assertion.

**Essential service** — A service a person cannot reasonably do without in ordinary life, including water, energy, food, medical care, housing, a basic bank account, communications, and education.

**Person** — A natural human being. The Floors (Part II) protect persons and living systems. An organization may invoke due process (2.D.5) to protect its own property and legal standing, but no other Floor.

**Power** — A single, specific capacity of authority — one function exercised over defined people, things, or territory, such as issuing fines, detaining persons, collecting a category of data, scoring applicants, or setting prices. **The power, not the institution, is the unit that is authorized, bounded, renewed, paused, stopped, narrowed, and ended.** The institution exercising a power is recorded with it and answers for it.

**Institution** — An organization or body that holds one or more powers.

**Operation** — A specific activity carried out under a power.

**Minor power** — A power that meets every condition of 3.A.4.

**Authorization** — The affirmative, recorded decision of an authorizing body that a defined power may operate, within stated limits, for a stated maximum term. Authorization is not transferable.

**Authorizing body** — The person or body that makes an authorization or renewal decision. These requirements do not choose who that is; they set the minimum conditions any authorizing body must meet (3.A.2, 3.A.3).

**Adopting authority** — An authority that has formally accepted these Core Requirements as binding on its own conduct (7.1). Every other authority is a non-adopting authority.

**Edition** — A version of these requirements with its own version identifier and hash (6.5) that has taken effect under 6.6.

**Renewal** — A new authorization decision for a power whose term is ending, made on current evidence. Renewal is never automatic and is never presumed.

**Re-entry** — The only way a power returns to operation after it has been stopped or has expired, or has a limit loosened: a full authorization decision as if the power were new. After a stop, re-entry also requires a showing that the cause of the stop has been addressed.

**Pause** — An immediate, temporary halt of a specific power or operation, triggered by a stop signal or by a rule of these requirements, lasting until the condition named by that trigger is resolved.

**Stop** — A halt of a specific power or operation after a defined threshold is crossed or its trigger fact is confirmed. A stopped power resumes only through re-entry.

**Narrowing** — A reduction of a power's scope, duration, reach, speed, intensity, resources, opacity, dependency, or downstream impact, decided by its authorizing body or required by these requirements. Reduction means narrowing.

**Ending** — Permanent termination of a power, including removal, invalidation, or reversal of its downstream effects, subject to 2.D.14 and 3.E.6.

**Independent** — Not funded, appointed, removable, staffed, or controlled by the authority concerned or by persons who benefit from the power's continuation; not reliant on the authority for data or operations; and not party to any reciprocal or exchanged arrangement with it. A person who served the authority may not act independently toward it until a published cooling-off period has passed.

**Independent judicial officer** — A decision-maker who is independent, decides by published law after hearing the person — or, where the decision must be made before the person can be told of it, hears the person as soon afterwards as that purpose allows — and holds office on terms the authority concerned cannot change.

**External validation** — Verification by entities that are independent of the authority concerned. Correlated, dependent, or operationally aligned entities do not qualify.

**Harm** — Damage that reduces a person's or living system's future choice, health, safety, stability, or recoverability. Harm includes physical, psychological, economic, ecological, informational, and structural damage, and slow erosion as well as sudden injury. Harm does not require malice, visibility, or consensus. Where a rule permits force or confinement, only the bodily harm that rule names can justify it.

**Confinement** — Any detention, custody, isolation, or hold that keeps a person in a place or prevents them from leaving, however brief, including a stop under 2.D.3(d) and isolation or a hold under 2.D.3(a).

**Individualized cause** — Specific facts about the particular person that meet a standard published before the act.

**Licensed activity** — An activity a published law or rule makes subject to a license, registration, or permit, that a person chooses to undertake, and that is never one of the activities 2.D.11 excludes.

**Collect** — To obtain information about a person by any means, including gathering, purchasing, licensing, receiving, inferring, deriving, or generating it.

**Personal information** — Information reasonably linkable to a person, including pseudonymous, hashed, device, household, cohort, and inferred information.

**Accountability record** — A record of an authority's use of force, confinement, or sanction against a person (the operative listing itself is governed by 2.D.14); a complaint, stop signal, or report about its conduct; discipline of its agents; or the outcome of a review of its conduct.

**Economic extraction** — Any charge to a person subject to a power, or to that person's family, above the documented marginal cost of what is provided; and any commission, revenue share, or payment to the authority from a vendor serving people subject to its power.

**Materially influence** — Any output, condition, metric, classification, recommendation, score, ranking, dependency, or signal that changes decision probability, access, classification, restriction, allocation, enforcement, or outcome in a non-trivial way. If removing it would change outcomes, its influence is material. Material influence defines what must be disclosed and what falls within an authority's scope; it is authority only where it meets the Authority definition.

**Derived output** — Any data, model, score, profile, classification, transformed or aggregated artifact, embedded or statistical representation, model weight, or decision-support output that retains functional influence from a source authority.

**Functional continuity** — Persistence of substantially the same authority function across time, entities, systems, ownership, jurisdictions, or structural forms. It exists when removing one system results in another continuing substantially the same effect.

**Dependency** — A condition where removing a system would disrupt operations beyond its original authorized scope, create a strong institutional incentive not to remove it, or make replacement impractical within defined timelines.

**Downstream effect** — Any decision, classification, restriction, access condition, allocation, score, record, output, or consequence propagated beyond the originating authority, regardless of system boundary, jurisdiction, ownership, or technical form.

**Irreversible ecological threshold** — A boundary in a living system beyond which resulting harm cannot be repaired within any relevant operational or generational timeline, including species extinction, climate tipping points, the loss of an aquifer or living soil, and the accumulation of persistent toxins. Any determination that conduct crosses or accumulates toward a threshold must rest on independently reproducible evidence and must apply on the same terms to every authority. Costs that remain below a defined threshold and are reversible within operational timelines are sub-threshold costs, not crossings.

**Floor condition** — A condition a Floor protects, as stated in Part II.

**Protective designation** — A designation, supported by independent evidence, that a specific Floor condition — such as an ecosystem, species, water source, or recognized right — must be protected. A protective designation describes what is protected; it does not itself restrict any person. Restrictions on persons belong only to the powers that enforce it.

**Causation Ladder** — The graduated evidence standard for any finding that two or more systems are one authority (4.2, 4.5, 5.4), that a variable is a prohibited proxy (4.7), or that one system's outputs are operationalized by another (4.3(a)). Such a finding must state the tier of evidence on which it rests, and its strength may not exceed the strength of that tier. Tiers, strongest to weakest: (1) formal control — ownership, governance, or binding directive; (2) contractual dependency — enforceable obligation to use or supply; (3) data dependency — one system cannot function without another's data; (4) operational reliance — routine, structured reliance in practice; (5) shared decision criteria — common rules, models, or thresholds; (6) statistically demonstrated proxy effect — reproducible evidence that one variable reproduces another's effect; (7) residual correlation — similar outcomes, cause unestablished. A finding of consolidated authority or prohibited proxy requires tier 5 or stronger (tiers 1–5); tiers 6–7 alone support only a recorded concern and a request for evidence. Similar outcomes arising from different causes do not, without more, establish equivalence. The burden of proof (5.2) applies to the authority's rebuttal once a sufficient tier is shown, not to establishing the tier itself. A finding that a system's own outputs are equivalent to directive control (Authority, limb (b)) rests on their practical effect and requires no tier. A review of disparity under 2.D.10 is a review, not a proxy finding, and requires no tier. The ladder governs findings about structure; it never governs stopping.

---

## PART I — FOUNDATIONS

*Human Understanding: These are the assumptions every other rule rests on. Power is treated as a structural quantity, not a moral question. Good people, good intentions, and good results do not make power safe. Only its shape does.*

#### 1.1 The Three Conditions
All authority must meet three conditions:
- Power must remain small enough to stop.
- Harm must remain interruptible before it becomes permanent.
- Mistakes must remain correctable before they become irreversible.
These conditions have no exceptions. Every rule is read to serve them.

#### 1.2 Humility and Structure
Authority must operate under the assumption of fallibility. No institutional decision system may presume permanent correctness or immunity from revision. Safety must come from the structure of a power and of the institution that holds it, not from the vigilance, virtue, skill, or effort of the people operating or watching it. A power must remain within its limits when operated by ordinary, inattentive, or fatigued people. No position may be designed so that restraint depends on one person's character. A power or institution that can stay within its limits only through continuous special effort or exceptional individuals is defective and must be redesigned, narrowed, or dismantled rather than supported.

#### 1.3 Function Over Form
Authority classification is determined by functional effect, including indirect authority under the Authority definition, over decisions, allocations, classifications, constraints, or access. Automated systems are subject to the same requirements as human-operated ones. Renaming, reclassifying, relabeling, outsourcing, automating, or restructuring an activity does not change the nature of the authority being exercised. Authority must not expand through linguistic reinterpretation, administrative relabeling, or definitional drift.

#### 1.4 Nothing Enlarges the Limits
None of the following enlarges a power's scope, duration, reach, speed, intensity, or resources, or relaxes any requirement: good intentions; expertise; trust, reputation, or track record; consensus, popularity, or shared goals; acting "on behalf of" or "for the benefit of" others; improved performance or favorable metrics; past use or precedent; survival without visible failure; records or institutional memory; sunk costs; familiarity or cultural acceptance; or the existence of larger or harsher powers elsewhere.

#### 1.5 Uncertainty Contracts Power
Ambiguity about a power's scope narrows that power rather than expanding it. Anyone may raise an ambiguity; when an independent body, within a time limit set in advance by the process that establishes oversight functions (3.A.3), finds it material — or fails to decide within that limit — the operation concerned pauses until the ambiguity is resolved. When uncertainty about harm, conditions, or effects increases, the power's scope and duration must be reduced, never consolidated.

#### 1.6 Emergencies Do Not Enlarge Power
An emergency, crisis, or claimed urgency does not enlarge any power's scope, duration, reach, intensity, or force; does not disable any stop mechanism, audit requirement, or Floor; and does not create exceptions to these requirements. Urgency may shorten the time to act only within existing limits. A situation that cannot be addressed within existing limits shows that the structure is unsuitable; it is not grounds for removing the limits. A power created or activated because of an emergency expires within 90 days. It may continue only through re-entry, no more than twice, and each continuation must be shorter than the one before; after that it may continue only as an ordinary power authorized under these requirements, within the term limits of 7.2. A standing power that can be activated without a declared emergency is an ordinary power subject to every requirement.

#### 1.7 Simplicity Is a Limit
Complexity in a power's rules, records, or procedures is a form of growth. No authority may make understanding of its scope, or use of any protection, depend on a class of specialists. Compliance mechanisms must be as simple as their purpose allows.

---

## PART II — THE FOUR FLOORS

*Human Understanding: A rule tells authority how to behave. A floor marks a condition authority may never push beneath, whatever its purpose. There are four. The Ecological Floor protects the living system every person depends on. The Economic Floor protects the material means a person needs to refuse, challenge, or leave. The Agency Floor protects a person's practical ability to understand and use their protections. The Human Rights Floor names what authority may never do to a person. Structural rules protect the existence of a way out; the Economic Floor protects the means to take it; the Agency Floor protects the practical ability to take it.*

#### 2.1 Floor Precedence
The protections in this Part exist prior to and independent of any authority. No authority may suspend, reinterpret, narrow, or subordinate them, and no emergency, necessity, administrative convenience, or claimed benefit justifies their violation. They apply to every person and living system affected by any authority, whether or not it has adopted these requirements. No accusation, conviction, classification, or status forfeits them. They protect people's rights; they create no right to violate the rights of others. A violation of any Floor is a violation regardless of the authority's purpose, classification, or label. No Floor grants any authority a power it does not otherwise hold. **The Floors are a minimum.** Where any constitution, law, or treaty gives a person greater protection against an authority, that protection also applies. No right held under other law permits any authority or person to go beneath a Floor or to break any other requirement here.

---

### A. Ecological Floor

*Human Understanding: Every human system runs inside a living system it did not build and cannot replace. Air, water, soil, a stable climate, and the web of living things are the conditions every authority depends on to exist. Some of that system's limits, once crossed, cannot be uncrossed — species extinction, climate tipping points, the loss of an aquifer or living soil, the build-up of persistent toxins. No price clears them and no growth justifies them. Beneath those limits, reversible costs are measured and carried by the activity that creates them, never used as a way past the wall. The floor binds every authority, whatever it does — governs, builds, lends, or allocates.*

#### 2.A.1 Ecological Floor
No authority may authorize, cause, or accumulate toward crossing a defined irreversible ecological threshold. Reversible costs below such a threshold must be measured and borne by the activity that creates them; their pricing must not be used to authorize, offset, or justify crossing a threshold. Delayed, cumulative, and long-duration ecological effects must not be discounted for their distance in time; where recovery would take longer than human planning horizons, prevention is required, and mitigation after the fact does not satisfy this Floor. This limit applies to every authority on the same terms.

---

### B. Economic Floor

*Human Understanding: A person who is technically free to refuse, but who would lose the means to live by refusing, is not free to refuse. This Floor does not guarantee income, require equal outcomes, or choose an economic system. It sets one limit: economic hardship must not be permitted to convert itself into economic captivity. Authority may impose costs, collect obligations, and regulate economic life — but it may not use material need as a lever, and it may not let a debt grow because a person cannot pay it. Money owed to another person, such as child support, is not erased by this Floor.*

#### 2.B.1 Material Agency
Every person subject to an authority must retain access to the material conditions necessary to maintain basic human functioning. No authority may deprive a person of those conditions, or make access to them conditional, in a way that compels compliance, secures consent, deters challenge, or obstructs exit.

#### 2.B.2 No Escalating Obligations
No economic obligation imposed or enforced by an authority may grow because of a person's inability to satisfy it. Inability to pay, comply, or exit must not itself generate escalating penalties, fees, interest, or burdens that make satisfaction or exit progressively less attainable. Every such obligation must have a defined and attainable path to discharge. Amounts owed to another person, such as support or restitution, that fall due on their ordinary schedule are not escalation; only added penalties, fees, or interest caused by inability to pay are barred. The person asserting inability to pay must be given a simple way to show it.

#### 2.B.3 No Leverage Over Essentials
Control over access to essential goods, services, resources, income necessary for subsistence, or other indispensable means of ordinary life must not be used as leverage to obtain unrelated authority, consent, waiver, or surrender of protected rights.

#### 2.B.4 Economic Reversibility
Economic burdens imposed by an authority must use the least binding means that accomplishes the authorized purpose, and must remain capable of review, correction, discharge, or meaningful exit. No authority may create practically irreversible economic dependency, deprivation, or obligation. Long-term economic burdens that bind future generations are additionally governed by 2.D.7.

---

### C. Agency Floor

*Human Understanding: A right that only a tireless expert can use is not a right for ordinary people. Many harms are not done by forbidding anything; they are done by making the way out too confusing, too slow, too expensive, or too exhausting to use. This Floor puts the burden on the authority to stay understandable and usable — not on the person to become sophisticated enough to survive it. Education can help people navigate systems; authority must not depend on people having exceptional ability to navigate it.*

#### 2.C.1 Comprehensible Explanation
An authority acting on a person must provide, without requiring a request, a plain explanation of what it is doing to that person, the basis for its action, and how to question, challenge, or stop it. Formal notice alone does not satisfy this requirement if the explanation is not practically understandable to the people it affects.

#### 2.C.2 Usable Protections
Protections under these requirements must be reasonably usable by ordinary affected people without extraordinary expertise, resources, stamina, or sustained vigilance; a procedure that makes a protection practically unattainable does not satisfy it. No authority may impair a person's practical ability to take part in challenging and correcting it.
- **No burden of self-advocacy.** Protections must activate without requiring affected people to advocate for themselves, articulate their harm in prescribed terms, or persist through repeated demands. Silence, incapacity, fear, or fatigue does not forfeit a protection or prevent a stop.
- **Frictionless reporting.** Reporting harm or error to or about an authority must not require prescribed formatting, prior approval, proof, payment, or expertise. Repeated reports of the same condition are treated as confirmation, not noise, and their volume does not dilute the response. A report that only repeats facts already independently checked and found unfounded is recorded and counts toward review, but does not by itself pause an operation again (3.C.3).
- **Accessible refusal, challenge, and exit.** Mechanisms for refusal, challenge, stopping, and exit must not impose complexity, delay, cost, retaliation, or procedural dependence that defeats their practical availability.

#### 2.C.3 Right of Exit
A person retains the right to end their participation in, or continuing subjection to, an authority or power — including a program, service, membership, or jurisdiction — without penalty for leaving. Residual constraint after exit is permitted only to the minimum extent necessary to prevent harm to the rights or Floors of others, and the authority bears the burden of justifying it. Exit limits authority over the person who leaves; it creates no authority for that person over others. Exit does not end a sanction already imposed with due process (2.D.3(c), 2.D.5), obligations already owed to others or to the authority, or a restraint that an independent tribunal imposed to protect identified people; such a restraint is reviewed under 2.D.6 on a schedule the tribunal sets.

---

### D. Human Rights Floor

*Human Understanding: The rest of these requirements constrain how authority behaves. This section names what authority may never do to a person, whatever its purpose. These are not grants and not policies. They cannot be set aside in an emergency, because emergencies are when they are most often violated. Above the Floors the framework takes no side on what authority should do; at the Floors it is not neutral, and says so openly.*

#### 2.D.1 Bodily Integrity
No authority may torture any person, subject any person to cruel, inhuman, or degrading treatment, or execute any person as punishment. No authority may subject any person to irreversible bodily harm or permanent physical degradation, except where such harm is the unavoidable result of the least harmful means of stopping an imminent threat of death or serious bodily harm to others. No authority may intentionally inflict bodily injury or pain as punishment, retaliation, humiliation, economic extraction, status degradation, or a means of compelling compliance, or use involuntary medical procedures as punishment or coercion.
This rule grants no power to use force; it limits force that is otherwise authorized. Any use of force against a person — to stop a threat, to detain, or to carry out a lawful order — must be separately authorized as a power (3.A.1); must be the minimum necessary; must aim only at its purpose, never at injury or pain; must cease when its purpose is met or the threat ends; must be externally stoppable while it is used; and must be documented and independently reviewed. No claimed emergency enlarges these limits.

#### 2.D.2 Emergency Medical Care Without Consent
Medical treatment without a person's express consent is permitted only when the person lacks capacity to decide, delay would cause an imminent risk of serious harm, and the treatment is necessary, proportionate, and confined to the emergency. Incapacity must be determined by a clinician independent of any authority seeking the person's compliance. Reasonable efforts compatible with the urgency must be made to find and honor any valid refusal, advance directive, or authorized surrogate decision. A capable person's current, informed refusal must not be overridden under this rule. The reasons must be documented, consent for further care sought as soon as practicable, and the decision open to independent review. This rule grants no medical authority that does not otherwise exist.

#### 2.D.3 Limits on Confinement
Detention or confinement is permitted only:
(a) to stop an imminent threat of bodily harm to identifiable people, for no longer than the threat lasts. This includes: isolating a person who, on an individualized finding confirmed by a clinician independent of the authority seeking the isolation, is infectious with a serious transmissible disease and would otherwise expose others to it, only where no less restrictive measure would prevent the transmission, in a place suited to care and not a place of punishment, for no longer than the infectious period, with prompt independent review and review at least every 30 days; and holding a person at imminent risk of death or serious bodily harm to themself, when an independent clinician confirms the risk or, until such a clinician can attend, for no more than a few hours fixed in advance by published rule, where the risk is evident and immediate from observed facts and a clinician has been called at once, and never again on the same facts without a clinician's confirmation; in a place suited to care and not a place of punishment; for the shortest time needed, with prompt independent review;
(b) to bring a person promptly — within 48 hours — before an independent judicial officer on a specific charge of conduct that rules published in advance defined as an offense; continued custody before trial is permitted only on that officer's individualized finding, based on specific facts about the person, of a concrete risk of flight or of imminent bodily harm to identifiable people; only where no less restrictive measure would address the risk; for no longer than a maximum set in advance by law; and with review at least every 30 days; or
(c) as a sanction for past conduct that rules published in advance defined as an offense, imposed with due process (2.D.5) and proportionate to the conduct, where the conduct harmed, or created a direct risk of harm to, another person or their rights; the property or funds of another person or of an organization, including public funds; the course of justice in a specific proceeding; or a condition a Floor protects, or cruelty to an animal. An attempt or conspiracy counts only if the person took a substantial step toward such harm. Conduct whose only risk is to the person themself is never punished by confinement, and neither is failure to pay a fine or meet another sanction imposed for such conduct; or
(d) as a brief stop of a person whom an agent has an individualized, articulable suspicion, based on observed facts about that person and not on a risk score or profile, is committing, has committed, or is about to commit an offense defined in advance; lasting no longer than needed to confirm or dispel that suspicion and never longer than a maximum set in advance by published rule; ending when that time runs out unless the person is arrested under (b); with the reason recorded and given to the person. A person may not be stopped again on the same suspicion without new facts.
Speech, belief, association, or psychological or informational harm alone never justifies confinement. A prediction of future conduct, including a risk score, never alone justifies confinement; custody under (b) must rest on the specific facts the officer finds. Stopping an imminent harm, holding a person for trial, sanctioning past conduct, and briefly stopping a person on individualized suspicion are distinct justifications, and a prediction about future conduct is not a justification at all; authority obtained under one justification must not be used to exercise another. A risk that a person poses only to themself justifies holding them under (a) or (b) only under the danger-to-self clause of (a), and never justifies a sanction of confinement under (c). A person charged only with an offense that cannot be punished by confinement under (c) may be held under (b) only until brought before the officer, and never in custody before trial. Confinement must not be used for economic extraction, coercive labor, humiliation, or permanent status degradation.

#### 2.D.4 Agency and Cognitive Integrity
No authority may intentionally destroy or permanently impair a person's capacity for autonomous thought, communication, or meaningful decision-making. Psychological coercion, cognitive manipulation, or forced mental alteration beyond recoverable limits is prohibited.

#### 2.D.5 Due Process and Justification
No person may be deprived of liberty, property, or legal standing without transparent justification, procedural review, and the ability to challenge the action before an authority independent of the one taking it. Secret law and undisclosed enforcement criteria are prohibited. A person who faces loss of liberty has the right to a lawyer, provided without cost if they cannot afford one; may not be compelled to be a witness against themself, and their silence is not evidence against them; and is entitled to a public hearing without unreasonable delay. No person may be punished for conduct that was not an offense when it occurred, or by a penalty greater than the one in force at that time, and no person may be tried or punished again for the same conduct after a final acquittal or conviction.

#### 2.D.6 Freedom from Structural Entrapment
No person may be bound indefinitely to institutional obligations, surveillance regimes, or administrative classifications without periodic justification and a real ability to challenge or exit the condition.

#### 2.D.7 Protection of Future Generations
No authority may impose irreversible environmental, economic, or social burdens that permanently bind future generations without renewal opportunities. Long-horizon commitments must be divided into short, revisable segments. Irreversible ecological burdens are additionally governed by 2.A.1.

#### 2.D.8 Communicative Integrity
No authority may suppress, distort, or monopolize information people need to detect, report, or correct harm, whether through intimidation, censorship of lawful criticism, manipulation of records or metrics, or obstruction of oversight. Channels for reporting institutional harm must remain accessible and protected. Harm reports must not be routed through performance goals, leadership approval, or reputational review; suppressing a harm signal is itself harm.

#### 2.D.9 Expression, Conscience, and Assembly
No authority may punish, restrict, or condition benefits on a person's lawful expression, belief, conscience, association, or peaceful assembly, or on criticism of authority. This includes gathering and publishing news, and petitioning any authority to correct a wrong; no authority may require approval before publication. Power does not manage dissent. Any limit on the time, place, or manner of assembly must be narrow, neutral as to content, and must not defeat the assembly's purpose. Narrow, published rules tied to the purpose of a particular space or service that the authority itself provides — a library, a forum on a stated topic, a workplace — are permitted if they are applied without regard to viewpoint, leave the person free to say the same thing elsewhere, and can be challenged before a body independent of the authority. Such rules never apply to a person's home, to public space, or to public transit, where only the time, place, and manner rule above applies. Where a space or service is, at the scale at which it operates, a principal means by which people reach the public (Authority, limb (b)), its rules must also be neutral as to content, except for expression that is not lawful. A voluntary community — one that people join and leave by their own choice, that holds no power over non-members, and whose membership is not a condition of housing, employment (other than a role whose function is to teach or lead the community's belief), livelihood, an essential service, or a principal means of reaching the public — may set its own membership by shared belief or purpose, because its members' freedom of association is protected too. It may impose no penalty for leaving or for being removed, and no consequence reaching beyond its own spaces and membership. 2.D.10 does not bar such a community from limiting membership to those who share its belief.

#### 2.D.10 Equal Treatment
No authority may impose a burden or restriction on a person, or deny a person a benefit, because of race, ethnicity, color, national or social origin, sex, sexual orientation, gender identity, religion or belief, disability, or language, or because of any proxy for them (4.7). Measures that accommodate a disability, provide services in a person's language, give support directed to a person's documented disadvantage, or separate people for privacy or safety without placing a greater burden on any group are not barred. A material disparity in how a power's burdens fall across these groups requires independent review, completed within 90 days. A disparity the review does not find explained by factors independent of these characteristics must be corrected within a defined window; if it is not, the affected operation pauses until it is.

#### 2.D.11 No Compelled Identification Without Cause
No person may be compelled to identify themselves, or be identified by surveillance, biometric matching, or tracking, without individualized cause defined in advance. The only other permitted cases are:
- **a licensed activity:** a published identification condition of a specific licensed or regulated activity the person chooses to undertake, such as driving a vehicle or crossing a border. Identification is permitted only at the point of the activity and for its regulatory purpose; it is limited to checking, while the person is engaged in the activity, the activity's own license or registration status; an automated check keeps nothing about anyone who passes it; and it never permits live tracking of a person's movements, or checking a person against any other list, without individualized cause. Keeping, combining, or searching people's location or movement history requires individualized cause. Presence in public space, use of public transit, assembly, expression, access to essential services, leaving a territory, and returning to one's own country are never licensed activities.
- **a claimed entitlement:** verifying the identity of a person who claims an individual entitlement — a benefit, money held for the person, a payment owed to the person — where giving it to the wrong person would harm the person entitled or others, using the least intrusive means that works. A non-biometric way must always be offered. After verification, only the fact and date of verification may be kept, and the information may not be used for any other purpose. An account that a person must hold to be present in public space, use public transit, assemble, or express themselves is never an entitlement for this purpose. Receiving an essential service is never an entitlement for this purpose, except the release of money held for the person or a payment toward that service owed to the person.

Suspicionless mass identification is prohibited.

#### Informational sovereignty

*Human Understanding: Records can become a cage. A system that never forgets can keep a person from ever moving past an encounter with authority. Authorities cannot preserve biometric identifiers indefinitely on the possibility that they might help investigate a serious crime someday. The prospect of future usefulness does not give an institution permanent custody of a person's identity. But the records of what authority itself did are different: they belong to accountability, and the authority may not erase them to protect itself.*

#### 2.D.12 Informational Sovereignty
Personal information must not be collected except for defined purposes, must be deleted when the purpose of its collection is fulfilled or ends, and must be protected from unauthorized exposure. No system may construct permanent informational profiles that eliminate a person's practical ability to move beyond past actions. Personal data systems may not create permanent, indefinite informational indexing of individuals. The retention period must be stated and justified at the time of collection, is independently reviewable, and may not exceed the term of the power under which the information was collected unless re-justified at renewal. A claim that information might be useful someday does not justify retention. No personal information may be retained more than 20 years from its first collection, whatever renewals occur. Retention clocks do not reset with later interaction, renewal, or re-collection of the same information, and consent cannot extend retention beyond its purpose or this ceiling. **Status registers.** A record whose sole purpose is to establish a legal status, title, or entitlement that a person holds for their own benefit — such as a birth, citizenship, marriage, or school-enrollment record, a land title, or a court judgment establishing such a status (an adoption, a divorce, a change of name) — may be kept while that status lasts. A record of an offense, conviction, sanction, listing, or other adverse finding against a person is never a status register; it follows the rest of this rule, 2.D.6, and 2.D.14. A status register may be consulted only to confirm a status presented by the person, by someone acting with the person's authorization, or by a body deciding an entitlement the person claims. It may not be searched to list, locate, profile, or identify people, and only while it is so limited is it outside the indexing ban of this rule. It holds no biometric or genetic data beyond the limit of 2.D.13, and it may never be used for any other purpose. The only other exceptions to deletion are those in 2.D.14, which never permit use of the information for any other purpose.

#### 2.D.13 Biometric and Genetic Data
Biometric and genetic data must not be collected except for a specific, bounded, documented purpose that cannot be met without it, and must be destroyed once that purpose is fulfilled or expires, and in no case later than 10 years after collection, except for a specific sample held while a court proceeding is pending (2.D.14). The prospect of a future investigation, including an investigation of a severe harm, does not authorize extended retention, secondary use, automatic renewal, or permanent identification archives. A new investigation may seek new, separately lawful, specifically bounded collection under this rule; it may not preserve or reuse information whose original purpose has ended. Every copy, backup, and contractor-held record is covered.

#### 2.D.14 Accountability Records and Evidence Holds
Deletion duties never permit an authority to destroy accountability records or records under a hold.
- **Accountability records** record what the authority did. They are not deleted as personal data of the authority's agents. They are kept for 10 years in custody chosen by a body independent of the authority and are available to the person concerned, to oversight bodies, and to courts. After 10 years, personal information of anyone other than the authority's agents is removed unless a hold applies. The authority's record that it imposed a sanction or listing — who decided it, when, on what basis, and with what review — is an accountability record. The entry that keeps a sanction or listing operative against a member of the public — a discipline entry, a registry listing, a blocklist entry — is not: it follows 2.D.12 and 2.D.6, and the person may ask for its earlier deletion unless a hold applies. Deleting the entry never deletes the accountability record, which then holds no more personal information of the person than that record needs. An accountability record of a sanction or listing is used only to hold the authority to account, and never to the detriment of the person it concerns.
- **Holds.** A record relevant to a filed complaint, stop signal, review, or proceeding is kept until that matter concludes. A hold for a proceeding that is expected but not yet filed lasts no more than 2 years. Holds are placed and logged by the independent custodian, not by the authority. A hold may extend biometric or genetic data beyond the limit of 2.D.13 only for a specific sample, and only while a proceeding it bears on is pending before a court.
- **The person's own records.** Before destroying a record that could exonerate a person, or that the person relies on — such as proof of an acquittal, a title, a benefit, or a completed obligation — the authority must give the person a copy, or transfer it to custody the person chooses; if the person cannot be reached after reasonable effort, the record passes to independent custody for the remainder of its retention period.
Records kept under this rule are used only for these purposes and confer no authority.

#### Searches, seizures, and movement

#### 2.D.15 Searches and Seizures
No authority may search a person, their home, papers, communications, devices, or belongings, or seize their property, without individualized cause defined in advance. A search or seizure also requires prior approval by an independent judicial officer, stating exactly what may be searched or seized, unless waiting would allow imminent bodily harm or the destruction of specific evidence; where only the destruction of evidence is feared, the authority may secure the thing unopened but may search it only with approval. Any search or seizure without approval is reviewed by such an officer promptly afterwards. Consent to a search must be freely given, and refusing consent is never cause; consent never permits a search that 2.D.11, 2.D.12, or 2.D.13 bars. A licensed activity may carry a published inspection condition limited to its regulatory purpose (2.D.11); it never covers a person's communications, papers, or devices, or any activity that 2.D.11 says is never a licensed activity. Anything else still requires individualized cause. Seized property is returned when its purpose ends, and in any case within a period set in advance by law unless an independent judicial officer extends it on specific findings; the owner may challenge continued holding at any time (2.D.5). No property may be permanently taken because of an offense unless its owner has been found responsible with due process (2.D.5).

#### 2.D.16 Freedom of Movement
Every person may move freely, choose where to live, and leave any territory, including their own country, and no one may be barred from returning to their own country. A restriction is permitted only: under 2.D.3; as a published condition of a licensed activity (2.D.11); as a narrow, published rule closing a specific, bounded place to entry, for no longer than an imminent danger of bodily harm or physical destruction from a hazard there lasts — a peaceful assembly, or the expected reaction to one, is never such a danger, and no closure may bar a person from returning to their own home unless the danger is at that home; a restriction that keeps people within an area is confinement and is permitted only under 2.D.3; or as a proportionate sanction for an offense defined in advance, imposed with due process (2.D.5). No activity that 2.D.11 says is never a licensed activity is a licensed activity for this purpose, and no restriction under this rule may bar a person from returning to their own country. No restriction may be used to prevent or punish expression, association, or exit (2.C.3). A person's own country includes every country of which they are or have been a national, and any country where they have their established home; withdrawal of nationality or residence never removes this protection.

---

## PART III — CORE CONSTRAINTS ON AUTHORITY

*Human Understanding: These rules follow a power through its life — before it begins, while it operates, when something goes wrong, and when it ends. Each stage has its own way of letting power grow. The rules close those ways in order.*

### A. Before It Begins

*Human Understanding: Most institutions define their limits only after harm occurs. These rules require the limits, the off-switch, the ending, and the plan for repairing mistakes to exist before a power acts. Power must know how it ends before it begins. The weight of the process matches the harm a power could do: a room-booking system is not a police force.*

#### 3.A.1 One Power, Narrowly Granted
Each power must be authorized separately and narrowly, for one specific function, with no discretion to widen it. Where discretion exists, it must be bounded by explicit prohibitions rather than open permissions. Authorization of an institution, office, program, or system does not authorize any power it has not been separately granted. Each power carries its own scope, thresholds, stop conditions, maximum term, and ending plan, and can be paused, stopped, narrowed, or ended without ending the institution's other powers. Powers that combine are additionally governed by 3.B.3.

#### 3.A.2 Authorizing Bodies
An authorization or renewal is valid only if the authorizing body:
- is independent of the power it is deciding on;
- has real authority to refuse, narrow, or shorten, not merely to recommend;
- gives the people affected a practical opportunity to be heard before deciding;
- decides on a public record that states the evidence relied on and its findings on each applicable requirement; and
- is itself subject to stop, challenge, and review.
No authority may authorize or renew its own powers, or hold structural control over the process by which its own renewal is decided. A member-governed or self-governing body — one whose members are the people subject to its powers and who govern it on equal terms, such as a city answering to its residents, an owners' association, a cooperative, a congregation, or a tribal nation — may have its powers authorized by a panel chosen by lot from all the people subject to the power. The panel excludes anyone who operates the power, or who holds office in, is employed by, or contracts with the institution; receiving a benefit or service from the institution on the same terms as everyone else entitled to it does not exclude a person, but anyone who receives any other payment or advantage from the institution while serving, or in the year before the draw, is excluded; compensation or redress the institution owes a person for a wrong never excludes them. The lottery, the panel's size, funding, and staff, and its access to evidence are provided by a process the institution does not control (3.A.3), and the panel may obtain evidence independently of the institution (5.1). Such a panel meets the independence condition of this rule; every other condition of this rule and of 3.A.3 applies. Panels drawn by the same process are one body for the two-renewal limit. Any person affected may appeal the panel's decision to an independent body; for a power that uses force or confinement, the authorization takes effect only once an independent body, designated in advance by the process that establishes authorizing bodies (3.A.3), has confirmed it on the record, whether or not anyone appeals. Renewal and contraction processes remain independently stoppable. A renewal without recorded findings on each requirement of 3.E.2 and 3.E.3 is void, and any affected person may challenge it before a body other than the one that decided it; a power whose renewal is void is treated as expired (3.E.1). An authority may not choose or change its authorizing body to obtain a more favorable decision, and a power refused by one body may come before another only through re-entry. No body may decide more than two consecutive renewals of the same power; the next renewal is decided by a different independent body, designated in advance by the process that establishes authorizing bodies (3.A.3), and the same two-renewal limit then applies to that body. Rotation required by this rule is not a change of body to obtain a more favorable decision.

#### 3.A.3 Oversight Functions
Bodies that authorize powers, check stop signals, audit, or hold stop paths exercise authority only for that narrow function. They are established by a process that the authority they oversee does not control — whether provided by governing law or, for an adopting authority, by its founding rules; these requirements set only their conditions. For their function they are bound by these requirements; must be independent of the powers and institutions they oversee and of one another's control; serve fixed terms; are subject to stop signals and to the people's path (3.E.5), whose review goes to a body independent of them; may not authorize themselves; and, if stopped, return only through re-entry before a body independent of the authority they oversee. No further chain of authorization above them is required. Their resources may not be reduced by the powers they oversee or by those who benefit from those powers; such a reduction is retaliation under 3.C.6. Each oversight function must have an independent substitute, designated in advance by the body that established the function, which acts immediately when the function is paused or fails to act within its time limits. An oversight function that fails to act within its time limits is replaced by its substitute and reviewed under this rule. Each authorizing body must ensure that the checking bodies it relies on can meet their time limits.

#### 3.A.4 Minor Powers
A power is minor only if all of the following are true:
- it uses no force or confinement against any person;
- none of its effects lasts beyond 30 days or resists ordinary reversal;
- the people it affects can obtain a substitute at low cost, or it only allocates a benefit the institution provides voluntarily;
- its annual spending is below a limit set, the same for all institutions alike, by the process that establishes authorizing bodies (3.A.3); powers that together serve one function are counted together (4.2); and
- it has had no confirmed stop, Floor finding, or successful review petition (3.E.5).
For minor powers, and only for them:
- one authorization may cover all of an institution's minor powers;
- the authorizing body may be a body chosen by lot or by election from the people affected, excluding operators and anyone paid by the institution, with appeal to an independent body; such a body meets the independence condition of 3.A.2 for minor powers, and every other condition of 3.A.2 applies;
- the harm assessment of 3.A.5 may use a standard short form;
- remedy readiness (3.A.10) is met by a named external complaint route, and financial assurance by ordinary liability insurance;
- the resource caps of 3.B.5 and the rehearsal duty in 3.A.7 do not apply;
- terms may run up to 5 years, including the first (7.2); and
- deletion may be recorded by schedule (7.6).
The Floors, stop paths, and every rule of Parts III-C, IV, and V apply in full. A power loses minor status automatically when any condition fails. The institution bears the burden of showing that a power is minor, and minor status is itself open to challenge.

#### 3.A.5 Harm Assessment and Thresholds
Before a power becomes operational, the authority must identify and document the reasonably foreseeable harms arising from the exercise, error, misuse, failure, and downstream spread of the power, across every harm category — bodily, psychological, economic, ecological, informational, communicative, agency, generational, and harm to non-participants — explaining any category it judges inapplicable. It must document who may be affected; the plausible severity, scale, duration, reversibility, and uncertainty of each harm; and the evidence for its assessment.
Measurable harm thresholds must be defined. Where a harm cannot be measured directly, the threshold must be an observable condition. The thresholds must include the size of an unauthorized exposure of personal information that is a stop condition (3.C.2). Each threshold must state its observable condition, its data source, its detection method, an independent verification path, and a time window over which harm is added up; harm may not be divided into pieces that each fall below a threshold. No threshold or stop condition may depend on any finding, classification, count, or process that the authority itself controls, produces, or can delay.
The authority proposes thresholds and stop conditions; the authorizing body sets them after hearing the people affected. All thresholds are publicly documented (7.4). Any change to a threshold requires a recorded justification and impact analysis. A threshold may be tightened at any time, by the authorizing body or the authority; it may be loosened only through re-entry, and it does not adjust to performance or perceived need. A threshold must not authorize what a Floor or other rule prohibits. Undefined or unjustified thresholds, or a materially incomplete assessment, invalidate authorization. Listed categories are not exhaustive; the absence of a named category does not permit a harm.

#### 3.A.6 Cumulative Harm and Structural Advantage
At authorization, the authority must define indicators of accumulating harm and of structural advantage over those who would stop, challenge, renew, replace, or exit the power. Persistent growth in these indicators is a harm even where no single action crosses a threshold. Each renewal compares the indicators with their authorized baseline; persistent growth without correction bars renewal.

#### 3.A.7 Stop Conditions and Stop Paths, Tested
Before a power becomes operational, its stop conditions and stop paths must be defined as factual triggers, and each stop path must be shown by test to work. At least one stop path must be held by a body that the authority neither funds, appoints, nor can remove. Through tested and rehearsed procedures simple enough for ordinary operators, the authority must show that the power can be halted, replaced, or dismantled safely. A power without a clear external stop is defective at the design level; its authorization is invalid. *The testing duties in this rule carry the normative force of Part III-C.*

#### 3.A.8 Obligations That Outlast the Term
Every debt, contract, easement, exclusivity, data arrangement, or other dependency that would outlast a power's current term must be listed in its authorization and approved individually. Each must pass to any successor with the function it serves, and must contain no term that restricts pausing, stopping, narrowing, or ending any power, or that compels its renewal. Each non-financial arrangement must also be terminable without penalty at the end of each term. A financial obligation for durable infrastructure, or a pension owed to workers, may run longer if it meets the conditions above and is divided into revisable segments as 2.D.7 requires — for example, by periodic review points at which its terms can be revised. An obligation that does not meet this rule is an irreversible effect under 3.D.2. No arrangement may renew itself automatically, impose an exit penalty, or bind data in a format that prevents its transfer. Replacement of the power must remain feasible within one term.

#### 3.A.9 Ending Planned in Advance
Before a power becomes operational, the authority must document how it will end safely: how dependencies are unwound, how records and functions are transferred or retired, what happens to delegated authority and derived outputs, and when wind-down preparation begins. A power that cannot show how it ends is not ready to begin.

#### 3.A.10 Remedy Readiness and Financial Assurance
Before exercising a power capable of causing serious harm, the authority must have a funded, workable, independently accessible process for identifying, investigating, correcting, and remedying harm caused by erroneous, unlawful, or abusive exercise of the power. The process must reach foreseeable downstream consequences, must be available through more than one route, none controlled by the authority, must not require affected people to obtain the authority's permission to seek independent review, and must remain available after the power is paused, stopped, expires, or ends. The authority must hold independently verified, risk-proportionate financial assurance sufficient for these duties; insurance may satisfy this requirement if it meets these conditions. The assurance must remain accessible despite the power's pause, stop, expiration, or ending, or the authority's insolvency or restructuring, and must be reassessed periodically. Financial assurance never licenses harm: the ability to compensate does not permit causing what could be prevented.

#### 3.A.11 Non-Participants
Authorities must identify individuals affected without participation or consent. Operations affecting non-participants must meet stricter harm tolerances. Consent by some does not authorize harm to others. Non-participant harm beyond its tolerance is a stop condition and is weighed against renewal.

#### 3.A.12 No Trading of Harms
No authority may choose one person or group to absorb harm for another's benefit. Such a trade is treated as expansion and requires narrowing of the power concerned. Compensation does not substitute for stopping a harm; paying for damage while allowing it to continue is escalation. Allocating physically scarce essentials during an emergency, by criteria authorized and published in advance, applied without regard to the characteristics in 2.D.10 by those providing care, and independently reviewed afterward, is not a trade of harms.

---

### B. While It Operates

*Human Understanding: Power grows in six directions — scope, duration, reach, speed, intensity, and opacity. Growth in any one of them is growth, even if the formal grant never changes. These rules keep each direction bounded and keep powers from combining into something larger than any of them.*

#### 3.B.1 Six Dimensions of Growth
A power's scope, duration, reach, speed, intensity (including force, enforcement, and resources), and opacity are each bounded by its authorization, and it must remain within its defined domain; authority legitimately held in one domain carries no implied authority in another. An increase in any dimension is growth, including growth through incremental aggregation of small changes, and growth without new authorization is stopped. A new function, a new population, a new territory, or a new system is a new power that requires its own authorization; it is not an extension of the old one. Any change to the criteria a power uses to restrict or remove access is a change of scope. Convenience, efficiency, and adjacent problems do not expand scope.

#### 3.B.2 Smallest Capable Unit and Redundancy
Where a function can be performed by a smaller structure, it must not be assigned to a larger one. Each authority must keep the practical ability for its powers to be replaced or dissolved. A necessary function must not depend on a single power-bearing structure: it must be performed by, or remain transferable to, independent capacity without shared control. Where a single provider is unavoidable, this rule is met by a tested plan to transfer the function to public or community control, or by mutual-aid arrangements that each party may leave at will.

#### 3.B.3 Coordination and Aggregation
Coordination, synchronization, interdependence, or alignment — formal or informal, cultural, technical, or procedural — that reduces independent stoppability is an increase in power and subject to all expansion limits. Any mechanism that aligns or prioritizes the actions of several authorities is evaluated as a separate source of power. Combining authority, data, or jurisdiction across domains creates a new structure that must be independently reviewed and separately authorized, and aggregation that reduces stoppability must be rejected regardless of efficiency gains. Coordination that each party may leave at will and that leaves every party independently stoppable, such as mutual aid, is permitted.

#### 3.B.4 Interfaces, Scarcity, and Local Stops
Interfaces between authorities must be narrow and explicit, and no authority is obliged to cooperate beyond what its own authorization requires. Authorizing processes must set and publish conservative limits on the number of power-bearing structures permitted within a domain and on direct interfaces among them. No central, coordinating, or higher body may override, delay, or condition a stop activated at a local or lower level. Every party to a multi-party arrangement must be able to leave it.

#### 3.B.5 Resource Caps
Every authorization must set numeric limits on the resources a power may control. Accumulation beyond those limits requires automatic narrowing of the resources held to within the limit, or ending of the power concerned.

#### 3.B.6 Capture and Dependency
Institutions exercising authority may not become structurally dependent upon concentrated private interests or technological infrastructures that undermine their independence. Authorities must disclose structural dependencies that could undermine their independence, interruptibility, or reversibility.

#### 3.B.7 Anti-Entrenchment
No power may become so embedded, dependent, technically integrated, economically relied upon, or operationally necessary that removal becomes impractical, destabilizing beyond its original authorized scope, or structurally discouraged. A power that reaches such dependency must be narrowed, divided, or made transferable within a defined window; review decides how, not whether. No authority may build advantages — exclusive data, contracts, skills, or infrastructure — that make its replacement harder than it was at authorization. An authority must not anchor a power by solving problems it helps create.

#### 3.B.8 Monitoring Informs; Enforcement Is External
Authorities must maintain mechanisms to detect expansion beyond their mandate and risks of capture, and must disclose what those mechanisms find. Self-monitoring informs observers; it never grants an authority power to adjust its own boundaries and never substitutes for external monitors with power to trigger stops. Manipulation of harm metrics, delayed disclosure, or restriction of audit access pauses the operation concerned pending independent review. A fall in stop signals while activity grows requires an independent review completed within 30 days; if it finds suppression, the operation concerned pauses. The same fact is also a renewal warning sign (7.7).

#### 3.B.9 Knowable to Those Affected
The existence, location, and boundaries of every power must be knowable to the people it affects, and its operation visible enough for independent evaluation of compliance. Visibility is sufficient only if an ordinary affected person can learn from public records what the power may do, when it expires, what stops it, who decides its renewal, and whether it has grown. Sensitive details may be protected; the existence and boundaries of power may not. Opacity produced by complexity counts as concealment.

---

### C. When Harm Appears

*Human Understanding: A system that cannot be stopped cannot be safely operated. Stopping must be easier than justifying, cheap for whoever does it, and possible without the authority's cooperation. Stopping is not a verdict and needs no proof of fault; finding out what went wrong comes after the harm has stopped. A crossed line stops the power by itself. A warning from a person pauses it while one simple question is checked. A warning that only repeats what was already checked does not pause it again.*

#### 3.C.1 Unplug-Ability and Stop Paths
Every power must remain interruptible, replaceable, and auditable by external stops that do not depend on the authority's cooperation, consent, or negotiation. Multiple independent paths must exist to activate a pause, placed as close as possible to where effects occur. When a power's speed increases, its stop paths must increase, not decrease.

#### 3.C.2 Automatic Stop
When a defined threshold is crossed or a defined stop condition occurs, the affected operation stops at once, whether or not anyone signals it. A stopped power retains no residual authority and resumes only through re-entry. An unauthorized exposure of personal information requires prompt notice to the persons affected and closing of its cause; failure to give notice, an exposure repeated within 12 months, or an exposure larger than the size set under 3.A.5 is a stop condition for the operation that exposed it. If no size has been set, every exposure is a stop condition.

#### 3.C.3 Stop Signals: Pause, Then Check
Anyone positioned to observe a stop condition may give a stop signal.
- A signal reporting that a defined threshold or stop condition has occurred pauses the operation concerned immediately.
- A signal reporting a credible pathway to serious harm that no defined condition covers takes effect once the checking body confirms, within hours, that its stated facts, if true, describe a pathway to serious harm within the categories of 3.A.5. A person affected need not state the facts in any prescribed form; the checking body records them.
- An independent checking body then decides, within a short defined time, one question only: did the trigger fact occur? If not, the pause ends; a false alarm is not a breach and confers no authority. If so, the pause becomes a stop.
- If the checking body does not act within its time, the matter passes at once to its designated substitute (3.A.3), which must act within the same time. If neither acts, a pause becomes a stop, and a pathway signal takes effect as a pause. A checking body that misses its time limits is a failed oversight function.
- A signal that repeats facts already checked and found unfounded does not pause again unless it adds new facts; it is still recorded and counts toward review under 3.E.5.
- The check may not weigh the power's usefulness, cost, or popularity, and may not excuse a confirmed trigger.
- Lawful provision of a service to people who choose it is not, by itself, a pathway to harm. Economic cost to a party is not a ground for a signal against a power that exists to stop harm by that party.

#### 3.C.4 Stopping Takes Precedence
Stopping harm takes precedence over completing tasks and over preserving systems. Damage to the infrastructure, process, or investment that enabled a harm is an acceptable cost of stopping it.

#### 3.C.5 Narrow Stops; Floors and Life Protected
A pause or stop applies to the operation implicated, not to unrelated powers of the same institution, and never only to a single agent when the cause is the operation itself.
- **Floors.** Where pausing, stopping, expiry, or ending would itself push people beneath a Floor — for example by cutting off water, medical care, or the means of subsistence — the harmful operation stops and only the minimum essential function continues. Until a controller is named, the authorizing body supervises it. The authorizing body names, within 7 days, a controller with no commercial or institutional stake in the function. The arrangement may not admit new persons into confinement and confers no authority to resume the harmful operation. It lasts until a successor authorized under these requirements takes over; the authorizing body must authorize one within 12 months, the arrangement is reviewed every 90 days, and it may never be run by the authority whose power was stopped, expired, or ended. If no successor is authorized within 12 months, the failure is a structural finding against the authorizing body under 3.A.3, and a different independent body must authorize one.
- **Protective operations.** For a power whose purpose is to stop imminent bodily harm and that uses no force against persons — such as firefighting or emergency medical response — a stop signal or crossed threshold arising during an active operation is recorded and acted on when the incident ends or after 72 hours, whichever comes first, and every 72 hours after that, unless it concerns bodily harm or harm to another Floor caused by the operation itself, which is acted on at once. An incident is a specific event at a specific place; a declared emergency, season, or campaign is not an incident. This does not apply to any operation conducted with, or at the direction of, a power that uses force against persons.

#### 3.C.6 No Penalty, No Retaliation
No procedural, financial, reputational, or other penalty may attach to giving a stop signal, activating a stop, using oversight, or challenging an authority. Knowingly false statements of fact may be addressed only through ordinary law, never through the stop path or its record. The record (7.5) publishes counts, categories, and outcomes, never the identity of those who give signals. The possibility of misuse is never a reason to remove, narrow, or burden a stop path. Retaliation against a person or body that stops, challenges, oversees, or reports is itself a violation and requires narrowing of the power concerned. Enforcement must apply symmetrically and may not selectively target challengers, and administrative procedures may not be used to exhaust or intimidate them.

#### 3.C.7 Conflicting Legal Mandates
Where external law compels an adopting authority to continue an operation that is stopped under these requirements, it must record the conflict publicly, notify the body that compels it, and continue only the minimum function permitted by 3.C.5.

#### 3.C.8 Review After Stopping and Verified Cessation
After a confirmed stop, independent review must evaluate the threshold breach, rollback necessity, and authorization status; review examines the stop and does not restore the stopped power. When a power is stopped, expires, or ends, an independent body must confirm and record that it has actually ceased, including in systems, contractors, and derived outputs.

---

### D. Reversal and Correction

*Human Understanding: Mistakes are ordinary. The goal is to undo them quickly and cheaply, not to explain them first. Reversal beats repair after the fact. A fix must never become a reason for more power. Physically containing a spreading danger — a recall, a firebreak — is a way of stopping harm, not a license for irreversible power.*

#### 3.D.1 Reversibility and Rollback
Powers and all their downstream effects must remain reversible within defined operational timelines. Any decision, classification, restriction, score, allocation, record, derived output, or propagated consequence produced by a power must remain traceable to its source and reversible upon expiration, invalidation, rollback, or ending of that power. Dependent systems must not treat such outputs as independent, permanent, or exempt from the originating power's limits. When drift or harm occurs, the authority must roll back to its last conforming state rather than layer additional complexity onto the system; where rollback is unavailable, effects must be isolated to prevent their spread. Where full reversal is impossible, the authority must not create the effect (3.D.2); where reversal nonetheless fails, the duties in 4.6 apply.

#### 3.D.2 Irreversibility Preemption and Protective Containment
No power may create, accelerate, preserve, or transfer effects that are irreversible or materially difficult to reverse; any action, output, classification, dependency, technical change, data operation, or sequence that risks such an effect must be blocked before execution. Creating such effects before review, renewal, audit, pause, or enforcement is complete is an automatic violation, and no authority may use procedural time, speed, technical dependency, or review delay to defeat later correction.
Physically containing a hazard that is causing or about to cause a larger irreversible harm — such as a recall of a dangerous product, a quarantine, a firebreak, or containment of a spreading danger — is stopping harm under Part III-C, not an irreversible exercise of power. It must be the least harmful means that works, confined to the hazard, documented, and independently reviewed afterward. Contracts, financial commitments, and destruction of records are never containment. A change of legal status is containment only if it is temporary and protective and addresses an imminent danger to identified people shown by specific facts about the case — for example, emergency protective custody of a child in imminent danger. It must be reversible by default, confined to the danger, and end at a maximum time set in advance by published rule, and it must be reviewed by an independent judicial officer within a short period fixed in advance. It may continue beyond that maximum only by a decision made under 2.D.5, never as containment. 3.D.3's preference for sensitivity over precision never justifies it. A permanent change of legal status, and any withdrawal of nationality or residence, is never containment. Where containment's irreversible effect falls only on the property or revenue of the party whose conduct it addresses, that party's challenge proceeds under 2.D.5 after the fact.

#### 3.D.3 Correction Without Preconditions
Correction begins by reducing effects and does not wait for explanation, admission, or attribution of fault. Denial does not block correction. Detection must favor sensitivity over precision; false alarms are acceptable, missed harms are not. When several failures interact, correction separates them before repairing any. Correction is not centralized in a single repair authority. Replacing a power is distinct from repairing it, and correction does not preserve the identity of the power corrected. Corrective action must not introduce new authority or become a justification for permanence or for exceptions to these requirements.

#### 3.D.4 Failure Shrinks Power
Failure is answered by narrowing, replacement, or abandonment, never by reinforcement. Repeated error leads to contraction or replacement, and mistakes at scale reduce the allowable scale of future structures. When a power exceeds its limits, the response must move directly to narrowing or ending, not through layers of review. Corrective stages must be documented, short, and time-bound; delay is treated as expansion.

#### 3.D.5 Patterns of Floor Violations
Repeated violations of any Floor by the same power, or by powers of the same institution, are a structural finding, not a series of individual incidents. Individual remedies do not discharge it. The finding requires independent review of the structure that allowed the pattern, and narrowing, restructuring, replacement, or ending of the powers involved. Records of the pattern may not be sealed, erased, or reset by a change of personnel, name, or jurisdiction.

---

### E. When It Ends

*Human Understanding: Expiration is ordinary. Renewal is separate. Nothing continues by momentum. When a power ends, nothing is owed to it — not a replacement, not a gap filled, not a second chance by default. Ending a power does not end responsibility for what it did. What a Floor protects does not expire; the powers that carry out that protection do.*

#### 3.E.1 Expiration
Every authorization must set a maximum term within the limits of 7.2. All exercises of a power, including programs, mandates, operational authorizations, and derived outputs, expire automatically at the end of that term unless affirmatively renewed. Expiration applies regardless of institutional permanence and requires removal, invalidation, or reversal of the power's downstream effects, except records kept under 2.D.14. A power that reaches expiration without completed renewal stops operating; pending review does not extend it, and resuming requires re-entry. Where stopping would push people beneath a Floor, 3.C.5 governs the minimum essential function.

#### 3.E.2 Renewal
An authority must demonstrate continued compliance with harm limits and structural constraints for a power to remain authorized and to be eligible for renewal. Continued necessity is grounds for requesting renewal, never permission to continue. Renewal requires evidence demonstrating continued necessity, proportional scope, structural reversibility, and compliance with harm thresholds, sufficient to allow independent evaluation of whether the power remains justified. The evidence must include: a comparison of the power's current operation with its original grant, in every dimension of 3.B.1; tested proof that every stop path still works; the indicators required by 3.A.6; and a drift review by testers independent of the authority. Renewal cannot approve growth: growth beyond the original grant requires a new authorization. Drift found and not corrected bars renewal.

#### 3.E.3 Necessity Decay and Mandatory Degradation
Claims of continued necessity weaken over time unless supported by independently verifiable changes in external conditions. A power may not be renewed solely because it previously existed, because prior justification persists, because risk can never be reduced to zero, or because its own operation produces evidence of its necessity. Renewal requires evidence that continued authority remains necessary and that the power is reducing dependency, scope, impact, or permanence over time. A power must reduce scope, dependency, opacity, persistence, intensity, or downstream impact over time unless independently validated conditions require continuation; static, unchanged, or increasingly embedded powers fail renewal unless narrowly justified by independently verifiable conditions. A reduction in a dimension the power did not use does not count. Increased need shown by the authority's published service data counts as a verifiable condition only once an independent audit confirms the data.

#### 3.E.4 Authority Ends When Its Basis Ends
A power's definitions and problem description are fixed at authorization. When conditions change so that its founding assumptions no longer hold, or reality exceeds its problem description, the power ends rather than reinterprets its mandate. Authority that exists without active function is ended, not stored for future use.

#### 3.E.5 The People's Path to Review or End a Power
People subject to a power must have a defined, accessible way to require that it be brought for early review, narrowing, or ending before an independent authorizing body other than the one that last authorized it, without waiting for its term to expire. The threshold for requiring review must be set in advance, published, and attainable by ordinary affected people; it may not depend on the authority's permission or cooperation. Only people subject to the power count toward the threshold; a party with a commercial interest in the outcome may give evidence but may not trigger review. A petition on substantially the same grounds within 12 months of a decision is declined unless it adds new facts. The authority bears the burden of showing, on the public record, that the power should continue. Early review may narrow, shorten, or end a power but never lengthen its term. Review does not itself pause the power; stop signals do that.

#### 3.E.6 Safe Ending and No Reinstatement
Wind-down operates within the same limits as active operation and never extends the power. Where immediate ending would itself cross a Floor, the minimum function needed to complete transfer or ending continues under 3.C.5 and inherits no claim to continue the ended power. Outside that case, no transition period continues the power after it ends. Responsibility for consequences survives ending. Reinstatement is never presumed; an ended power's absence need not be filled.

#### 3.E.7 Protective Designations Do Not Expire
A protective designation does not expire with the powers that enforce it. It may be loosened only through re-entry, on independent evidence that the protected condition is no longer at risk; it may be strengthened at any time by the body that made it or by any independent authorizing body. Every power that enforces a designation — and every restriction it places on any person — remains subject to every requirement, including term limits, growth limits, and the Floors. Where a long-term covenant or restriction serves a protective purpose — such as keeping housing in a defined place affordable, or conserving defined land — the condition it protects may be made a protective designation if that condition is one a Floor protects. The designation persists. The covenant or restriction itself restricts persons, belongs to the power that enforces it, and carries a term within 7.2 and revision points under 3.A.8. Strengthening a designation never by itself adds a restriction on any person. Property values, neighborhood character, and the preferences of other owners are never conditions a Floor protects.

---

## PART IV — STRUCTURAL CLOSURE AND ANTI-EVASION

*Human Understanding: Delegating work is allowed. Splitting, disguising, or routing authority to escape limits is not. A limit applies to what authority does and what it causes, wherever and however it is done. The rules below name known ways of evading limits; they are examples, not a complete list.*

#### 4.1 General Closure and Shared Responsibility
No requirement may be defeated by a change in name, structure, location, sequence, intermediary, technology, coordination, fragmentation, delegation, or combination where the resulting exercise or effect of authority is functionally equivalent to one the requirement constrains. Evasion itself is prohibited; the rules in this Part identify known forms of it and do not limit this rule. All systems participating in, depending upon, receiving outputs from, contributing to, or operationalizing a dependency chain share responsibility for compliance; no participant may disclaim responsibility by invoking separation, specialization, delegation, outsourcing, technical role, jurisdiction, contract status, or lack of final decision authority.

#### 4.2 Fragmentation and Functional Continuity
Division of authority across multiple institutions, contractors, subsidiaries, time periods, technical systems, jurisdictions, or coordinated actors may not be used to evade containment rules, expiration limits, renewal requirements, or expansion limits. Authorities that coordinate operational structures as part of a shared authority function shall be evaluated as a single authority system regardless of legal, organizational, temporal, technical, or jurisdictional separation. Where a function of authority persists across entities, time periods, authorizations, systems, jurisdictions, ownership structures, or configurations, it shall be treated as a single continuous authority system for scrutiny; expiration, renewal, stop, re-entry, scope, aggregation, and containment requirements apply to the function as a whole. Continuity of scrutiny is never continuity of permission. A finding of shared authority function is subject to the Causation Ladder.

#### 4.3 Indirect Authority
A system that issues no binding directive of its own nonetheless exercises authority when its outputs meet the Authority definition — when they are (a) operationalized into compulsion, or (b) their effects at scale are equivalent to directive control. Where this holds, scoring, ranking, recommending, routing, filtering, allocating, standard-setting, defaults, withdrawal of protection or service, model output, and dependency-producing infrastructure are exercises of authority, regardless of form or label. Where it does not hold, the system may be recorded as influence-bearing and monitored. The test is the practical force of the output on those affected, not its terminology, intent, or technical form.

#### 4.4 Derived Outputs and Laundered Data
Any derived output inherits the constraints, expiration limits, purpose limits, auditability requirements, reversibility duties, and downstream obligations of the authority that produced, authorized, trained, conditioned, or materially shaped it. Derived outputs may not extend influence beyond the originating authority's purpose, persist beyond its expiration, or become independent authority through transformation, aggregation, embedding, retraining, proxy conversion, or transfer. Expiration, invalidation, or ending of the source requires removal, invalidation, or reversal of derived outputs unless independently reauthorized under full review under these requirements. Information about people obtained from a source that is not itself an authority is treated as collected by the receiving authority when it is received.

#### 4.5 External Systems
An authority may not obtain, rely upon, operationalize, import, purchase, receive, or otherwise use outputs from external systems where doing so would produce a result the authority could not directly create under these requirements. Contractor, vendor, partner, foreign, private, technical, or affiliated systems are treated as part of the authority when their outputs are used to achieve effects these requirements restrict. Where an external system produces materially equivalent outcomes and the authority relies on, incorporates, coordinates with, benefits from, or operationalizes them, that system is treated as part of the authority. Ownership, jurisdiction, contract status, technical separation, or formal independence does not defeat functional equivalence.

#### 4.6 Propagation Duty
Any system that receives, relies on, republishes, caches, transforms, or operationalizes outputs from an authority assumes propagation duties when those outputs expire, are invalidated, corrected, or reversed. Those duties include notice, purge or correction of affected outputs, certification of compliance, preservation of auditability, and prevention of continued reliance on invalidated effects. Propagation duties do not apply to journalism, historical archives, or a person's own copies of their records.

#### 4.7 Proxies
A prohibited variable, classification, action, restriction, or authority effect — including any characteristic listed in 2.D.10 — may not be replaced by any proxy, model feature, variable cluster, inferred classification, statistical substitute, behavioral indicator, derived signal, or transformed artifact that reproduces materially similar effects. Proxy equivalence is determined by practical effect, not terminology, intent, technical form, or formal variable identity, and is subject to the Causation Ladder.

#### 4.8 Interpretation Abuse
Interpretations that preserve formal compliance while materially violating these requirements' purpose, increasing practical authority, reducing stoppability, weakening reversibility, avoiding expiration, or concealing authority effects are invalid.

---

## PART V — VERIFICATION, ACCOUNTABILITY, AND ENFORCEMENT

*Human Understanding: A limit no one can check is a wish. These rules decide how compliance is shown, who must show it, and what happens when it is not shown. They also keep an inability to prove compliance separate from proof of a violation.*

#### 5.1 Independent Evaluation
Independent review bodies must retain unrestricted ability to evaluate authority structures. No authority may operate below a non-waivable level of auditability sufficient to evaluate scope, effect, harm thresholds, dependencies, derived outputs, reversibility, expiration, and stop capability. All information, interfaces, and system behaviors necessary to evaluate scope, effect, compliance, and reversibility must be accessible in a form that allows independent analysis. Security, confidentiality, trade secrecy, emergency, technical complexity, or institutional sensitivity may alter the form of disclosure but may not eliminate the minimum ability to evaluate compliance. Review may use protected access, confidential independent examiners, redacted datasets, or reproducible demonstrations only when public disclosure would endanger people, privacy, or security; such arrangements must not defeat meaningful independent evaluation. For an adopting authority, if independent evaluation cannot be performed, the power is non-compliant, and restriction of evaluation capability is a violation. For a non-adopting authority, unavailable access supports a finding of compliance not demonstrated unless independent evidence establishes a violation.

#### 5.2 Burden of Proof and Evidence Integrity
An adopting authority bears the burden of demonstrating compliance with its duties. Missing, incomplete, inaccessible, or non-reproducible evidence is failure to demonstrate compliance and is non-compliance with the applicable proof duty. For a non-adopting authority, insufficient evidence supports a finding of compliance not demonstrated; it does not, without affirmative evidence, establish that a substantive requirement was violated. A finding of a violation must identify the evidence supporting it. Evidence used for authorization, renewal, continuation, classification, threshold adjustment, or compliance must be independently reproducible and sufficient for external evaluation; non-reproducible, selectively disclosed, internally dependent, opaque, or strategically narrowed evidence is invalid.

#### 5.3 Declared Inputs
All metrics, variables, signals, classifications, and decision inputs that materially influence a power's outcomes must be declared, subject to privacy-preserving independent evaluation. For an adopting authority, if observed outcomes cannot be fully explained by the declared inputs, the power is presumed to contain undeclared influence; undeclared influence is non-compliance, and failure to demonstrate that the declared inputs are complete pauses the operation concerned until it is shown. Metrics describe; they never permit expansion. For a non-adopting authority, unexplained outcomes are recorded as compliance not demonstrated unless evidence establishes undeclared influence.

#### 5.4 Outcomes Govern
Authority is evaluated by observable outcomes rather than declared structure. If a system's practical effects exceed its authorized scope, the authority is expanded regardless of labeling, structural separation, sequence of actions, or intermediaries. Outcome-based expansion is non-compliance and requires narrowing to the authorized scope or a stop. A finding of expansion across separate systems is subject to the Causation Ladder.

#### 5.5 Enforcement Without Discretion; Unauthorized Powers
Within an adopting authority, where violation conditions are met, enforcement must occur. Discretion, negotiation, political preference, convenience, administrative burden, or claimed usefulness may not override a trigger. A power operating without a valid, current authorization is stopped and resumes only through re-entry. For a non-adopting authority, a met violation condition is recorded as a failure under this framework; the framework does not itself execute enforcement.

#### 5.6 Time-Bound Correction
All required corrections, reviews, pauses, contractions, rollbacks, renewals, invalidations, propagation duties, and endings must occur within defined, short time windows. Correction not completed within its window leads to ending of the power concerned, not to an extended window. Where ending would push people beneath a Floor, 3.C.5 governs the minimum essential function.

#### 5.7 Bypassed Safeguards
Bypassing, disabling, or ignoring a stop, harm threshold, reporting channel, or audit mechanism is a critical violation. The response is ending of the power concerned and of any other power of the same authority used in the bypass, not repair of the mechanism.

---

## PART VI — GOVERNANCE OF THE CORE REQUIREMENTS

*Human Understanding: A framework against permanent, self-protecting authority cannot itself become permanent or self-protecting. These rules bind the Core Requirements by the same limits they impose on everything else — including the rule that nothing already protected may quietly disappear in a rewrite.*

#### 6.1 Structural Closure
Nothing beyond the authorities, mechanisms, categories, and processes defined in these requirements is authorized or implied. Interpretation may clarify application but may not introduce new structural elements. Silence is not permission. The requirements of Part VII are binding to the same extent as every other rule. Guidance documents may describe how to satisfy these requirements but may not narrow, waive, or reinterpret them.

#### 6.2 Conflict Resolution
Conflicts between rules must be resolved in favor of reversibility, harm prevention, and structural humility. Where stopping harm conflicts with continuity, continuity yields.

#### 6.3 Anti-Weaponization
No rule may be interpreted to justify harm that the framework is designed to prevent. Use of these requirements to justify harm, expansion, or irreversibility is invalid. Protections that limit authority may not be used by an authority, or by a party with a commercial stake, to obstruct the protection of others.

#### 6.4 Periodic Re-entry
These requirements must be reviewed under their own principles at least every ten years. They do not persist by familiarity or reference; their continuing authority depends on re-entry through review.

#### 6.5 Canonical Integrity
All canonical artifacts of the Bounded Power Framework must include a publicly recorded cryptographic hash stored in the official hash registry. Any modification requires publication of the modified artifact, a new version identifier, the updated hash, and the updated registry entry. An artifact that differs from its registered hash is not an official version. No artifact may be silently replaced or superseded, and every superseded version remains publicly archived.

#### 6.6 No Silent Weakening
No new edition of these requirements may take effect until an independent check confirms that every protection in the prior edition is present at equal or greater strength, except protections removed or weakened as deliberate changes under this rule. A protection may be removed or weakened only as a deliberate change, stated separately with its reasons, independently reviewed, and adopted through the same process as the edition itself. An edition that weakens a protection in any other way is not an official version.

---

## PART VII — BINDING OPERATIONAL REQUIREMENTS

*Human Understanding: Some requirements are about records and procedures rather than principles. They are kept here, inside the Core Requirements, so they stay binding. Guidance documents such as SCBP-03 explain how to meet these requirements and may never weaken them (6.1).*

#### 7.1 Adoption, Transition, and Withdrawal
Adoption covers every power of the adopting authority and of every entity it controls. Each power that exists at adoption must be authorized under these requirements within 12 months; an authority with more powers than can be authorized in that time may instead adopt a schedule, approved by an independent authorizing body, of no more than 3 years, which authorizes every power using force or confinement within the first 12 months and its other highest-risk powers next. Until authorized, each such power operates under the term limits of 7.2, all stop paths, and the Floors, and any such power not authorized on schedule expires. Withdrawal from adoption is publicly recorded, takes effect 12 months after notice, and does not end any pending pause, stop, finding, or obligation already owed. Moving a power to an entity that has not adopted these requirements does not remove it from them. **Editions.** Adoption is of the latest edition that has taken effect under 6.6 on the date of adoption, and the adoption record names that edition's version identifier (6.5). A later edition does not bind an adopting authority merely by taking effect. Each authorization, renewal, or re-entry must be decided under the latest edition that has taken effect under 6.6 on the date of the decision. The authority's duties that belong to no single power — Part VII records, oversight functions, stop paths, and the people's path — follow the latest edition under which any of its powers has been authorized. No adopting authority may advance or delay a renewal, or seek a longer term, to avoid a later edition. A renewal decided after a later edition has been published for its 6.6 check, and before that edition takes effect, may not run longer than 2 years after that edition takes effect. This rule does not limit 2.1: a protection that a later edition adds to the Floors, or by which it strengthens them, applies to an adopting authority from the day that edition takes effect, as it does to every authority; only the procedures and obligations the authority adopted for that protection wait for each power's next authorization.

#### 7.2 Term Limits
Every authorization and renewal must state a maximum term within these limits:
- **No term may exceed 10 years.**
- **No term may exceed 2 years** for a power that does any of the following: uses force or confinement against people; can cause effects that are irreversible or hard to reverse; reaches a broad population or many jurisdictions; is new or untested; or operates under significant uncertainty about its effects. A first authorization of any power is treated as new, except a minor power.
- **No term may exceed 5 years** for any other power, unless a second independent body confirms, on the public record, that a longer term within the 10-year limit carries no greater risk.
- **Minor powers** (3.A.4) may have terms of up to 5 years, including the first; this bullet prevails over the 2-year limit for them.
- **Emergency powers** are limited by 1.6.
The authorizing body may set a shorter term at any time. No term may be extended during its course; continuation requires renewal. A renewal may not be decided more than 6 months before the term ends, and the new term runs from the end of the old one. Renewal review must begin early enough to finish before the term ends.

#### 7.3 Interpretation Log
All interpretations affecting scope or thresholds must be recorded in a publicly auditable log. An interpretation that widens scope or reduces the occasions for stopping takes effect only after independent review.

#### 7.4 Public Ledger, Surface Map, Threshold Registry, and Failure Record
Authorities must publish periodic plain-language summaries of expenditures, resources held, renewals, stop events, and structural dependencies. They must maintain a documented map of all operational surfaces where authority is exercised, across the dimensions of 3.B.1; a public registry of every harm threshold with the elements required by 3.A.5 and the record of every change to it; and a record of known structural failure modes, periodically reviewed. Recording a failure does not permit its continuation.

#### 7.5 Public Stop-Signal Record
Every authority must maintain a public record of stop signals and harm reports concerning its powers — their category, count, the result of each independent check, and the final disposition — in a form that never identifies those who give them. The authority must not control, edit, or delete entries.

#### 7.6 Deletion Record
When personal, biometric, or genetic information must be deleted or destroyed, the authority must record what category of information was deleted, the incident or case it related to, when, by what method, and that every copy — including backups, derived outputs, and copies held by contractors or partners — was covered. The deletion record contains no personal information, is independently audited, and the person concerned may obtain confirmation of deletion on request. Deletion that cannot be confirmed is treated as retention.

#### 7.7 Renewal Warning Signs
Any of the following requires expanded independent review before a renewal is decided: stop signals falling while activity grows; approvals becoming faster without more evidence; reduced participation by external auditors; interpretation concentrated in fewer hands; or growing exposure of non-participants.

---

### Closing

*Non-binding.* These requirements end without a promise of permanence. Above the Floors, they hold only where they fit cleanly, and they yield rather than stretch.

**Power remains small. Harm remains stoppable. Mistakes remain correctable.**

