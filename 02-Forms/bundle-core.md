# BPF AI Registration Bundle

*Bundle version 1.0.0 · 2026-10-13 · Published for independent review · Not adopted · Contains: Registration Form {{FORM_VERSION}}, Vocabulary {{VOCAB_VERSION}}, Core Requirements v1*

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
- `bundle: {version: {{BUNDLE_VERSION}}, date: {{BUNDLE_DATE}}}`
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

# APPENDIX A — Registration Form {{FORM_VERSION}}
{{FORM}}

---

# APPENDIX B — Vocabulary {{VOCAB_VERSION}}
```yaml
{{VOCAB}}
```

---

# APPENDIX C — Core Requirements v1
*Reference. Use it to fill the "Required" column and the Floor questions. Rule numbers like 3.A.5 refer to this text.*

{{CORE}}
