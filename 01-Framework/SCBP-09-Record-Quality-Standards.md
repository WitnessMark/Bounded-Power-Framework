# SCBP-09 — Record Quality Standards

*v1 · 2026-10-21 · Published for independent review · Not adopted by anyone*

*Guidance document. Subordinate to the Core Requirements v1. Guidance may explain how to meet the Core Requirements; it may never narrow, waive, or reinterpret them (6.1).*

---

## Purpose

This document says **what makes a record good enough to rely on**. It covers:

- observed records;
- authorization records;
- worked examples;
- new versions of a record (version 2 and later);
- authority responses.

Witness reports are covered by SCBP-08 (Witness Reports and Stop Signals). The checker rules for them are in Section VIII here.

### Who this is for

**Version 1 of the framework publishes no records of real institutions.** It publishes only worked examples, which are fictional, and the framework's own record.

Anyone can still make a record of a real institution, for example with the AI Registration Bundle. That record belongs to the person who made it. Whether to publish it is their choice and their responsibility. These standards are what they, and their readers, can use to judge whether the record is sound.

These standards are a quality bar, not a gate. Meeting them does not mean a record is true, and nobody is endorsing it. They mean the record is honest about what it knows, shows where every claim comes from, and can be checked.

---

## Section I — The kinds of record

| Kind | Who makes it | Key marks |
|---|---|---|
| **Observed** | Anyone outside the institution: an affected person, a researcher, a journalist, an AI assistant helping them | `record_type: observed`. Describes what exists today from public sources and first-hand observation, and compares it with the Core Requirements. Contains no commitments (no Part E) |
| **Authorization** | An institution that has adopted the Core Requirements | `record_type: authorization`. Sets each power's limits *before* it operates (Part III-A). Must include Part E |
| **Worked example** | The framework | `example: true`. Fictional. Shows how the framework applies to a *kind* of institution (Section VI) |
| **New version** | Only the original preparer | `record_version: 2` or higher, with `supersedes` and a "What changed" section (Section IV) |
| **Authority response** | The institution described in a record | Filed beside the record it answers. Never replaces it (Section V) |

**Power first.** Every record starts with the institution and then lists each of its powers separately (P1, P2…). The power, not the institution, is what is authorized, bounded, renewed, paused, stopped, and ended (Definitions: Power; 3.A.1).

---

## Section II — Rules for every answer

### 1. The three-answer rule

Every factual field holds one of three answers:

- **a value with its source**, written `value [S3]`;
- **UNKNOWN**: the available evidence does not establish the answer, including information that could not be found, accessed, or verified;
- **NONE EXISTS**: evidence establishes that it is absent, such as no expiry date or no external stop. A failed search is not enough.

**Never invent a value.** "NONE EXISTS" is often the most important finding in a record.

### 2. Every number has a source

Every figure — a count, a percentage, an amount of money, a date, a duration — carries a source tag **in the same sentence**. In a table, the row's Source column covers the whole row.
- Numbers that come from the Core Requirements themselves (48 hours, 20 years) cite a source row `BPF: Core Requirements v1`.
- In worked examples only, illustrative figures are tagged `[EX]`.

### 3. Roles, not names

Refer to people by role or title: "the Director", "the arresting officer". A person's name may appear in a source title or link only where it is needed to find the source, never in the text of the record.

### 4. Public sources and first-hand observation only

Nothing private, leaked, or speculative.

### 5. Keep facts and allegations apart

Each documented harm or claim is labelled as one of:
- an **adjudicated or admitted fact**;
- **settled without admission** (a regulator's findings in an order the institution agreed to without admitting them);
- an **allegation**, or, in witness reports, the reporter's own observation.

### 6. Describe structure, not motives

No loaded words, no bold text for emphasis inside answers. A record is a structural description, not an accusation and not a verdict.

---

## Section III — Findings

Each power has a table comparing what is **observed** with what the Core Requirements **require**, in ten fixed rows: authorization, maximum term, harm thresholds, stop paths, ending plan, remedy, data limits, visibility, floors, evasion.

Each row ends in one finding:

| Finding | When |
|---|---|
| `conforming` | The observed value meets the requirement |
| `not_conforming` | It does not. **NONE EXISTS** for a required item is not conforming |
| `not_demonstrated` | Compliance cannot be shown. **UNKNOWN** leads here. This is not proof of a violation (5.2) |
| `not_applicable` | The requirement does not apply, with a reason (for example, "the power uses no force") |

Rules for sound findings:
- **Front matter and table must agree.** A finding stated in the front matter must match the table.
- **Visibility** is judged on whether people can learn the facts. A publicly stated "no expiry" can be conforming for visibility; the failure belongs in the Maximum term row.
- **Causation Ladder.** A finding that systems are one authority, that a variable is a prohibited proxy, or that an output is operationalized by another party needs evidence at tier 5 or stronger. Tiers 6 and 7 support only a recorded concern (Definitions: Causation Ladder).
- **Patterns.** A finding of a pattern of Floor violations (3.D.5) needs established Floor violations. A settlement without admission, or unproven allegations, supports only a recorded concern.
- **For a non-adopting institution,** every finding is a public finding, not an imposed obligation (Force and status).

### Stop paths in observed records

- **There is no minimum number.** Record every real stop path, and what each can actually stop: the `whole_power`, `one_practice`, or `one_case`.
- **State plainly whether anything can stop the power as a whole.** A whole-power path means a holder independent of the institution can, under current law, halt the power entirely.
- **These do not count as whole-power stop paths:** the general ability to pass a new law or to abolish the institution; a vote by the institution's own governing body; forking or replacing the institution. If only a new law or abolition could stop the power, the answer is NONE EXISTS.
- **When a legislature or other body counts.** A legislature or other body counts as a whole-power stop path only if it is independent of the institution and has an existing, usable procedure that can stop the power within a defined time, for example a sunset vote that must take place, or a standing review body with power to end it. The general ability to pass a new law, or to abolish the institution, does not count.
- **Self-help is not a stop path:** paying, complying, declining, or turning a setting off.
- **Holder independence** is recorded as independent, partly independent, not independent, or UNKNOWN, with the reason.

### Authorization records

An authorization record also sets out, for each power, everything required by SCBP-03 Stage 1 (Part E). Points that are often missed:
- each harm threshold states its observable condition, data source, detection method, independent verification path, and time window, and depends on nothing the institution controls (3.A.5);
- stop paths are tested, and at least one is held by a body the institution neither funds, appoints, nor can remove (3.A.7);
- the term is within the limits of 7.2;
- a minor-power claim meets every condition of 3.A.4, and never for a power that uses force or confinement;
- the authorizing body meets 3.A.2.

An authorization record's findings are the institution's own grades. It is displayed with `prepared_by: authority`. It never supersedes an outside observed record of the same powers; both stand side by side.

---

## Section IV — Sources

Every record ends its body with a numbered Sources table (Part C):

| Column | What goes in it |
|---|---|
| ID | S1, S2… Every tag used in the text must have a row |
| Kind | `quote` (proves a statement; copy the passage word for word, at least a few words) · `data_point` (supports a number or table cell; give the location) · `first_hand` (the preparer's own observation) |
| Title or description | What the source is |
| Link | A web link, or `BPF: <document name>` for a framework document. Not needed for `first_hand` |
| Where in it | Page, section, or table |
| Quote | For kind = quote |
| Verified? | `yes` (read the original) · `tool_text` (a tool returned the exact page text) · `unverified` (only a summary was seen) |

Good practice:
- record `sources_checked_date`, the date the sources were last read;
- say which related entity each figure belongs to (parent, subsidiary, contractor);
- cite no source that is not used, and use no tag that has no source.

**A source tag proves only that a source row exists.** Reading the source against the claim is the reviewer's first job (Section IX).

---

## Section V — Versions and responses: no silent replacement

**Nothing is overwritten, and nothing disappears.**

### New versions (version 2 and later)

- **Only the original preparer** issues a new version.
- A new version is a **new file**: `…-v2.md`, with `record_version: 2` and `supersedes: {record_id, record_version: 1}`. Version 1 stays public at its own file name.
- It must include a section headed **`## What changed from version N`**. For each change it gives:
  - the old text, **quoted exactly**;
  - the new text;
  - the reason: a response it accepts, a new source, or an error found.
- **Removed text is quoted too,** so a reader of the new version sees what used to be there.
- If a version accepts some points of a response and not others, it says which.

### Authority responses

An institution described in a record answers with the **Authority Response form (version 1.0.0)**.

| Response type | Use it when… |
|---|---|
| `correction` | A fact in the record is wrong. Show the evidence |
| `added_information` | The record says UNKNOWN or NONE EXISTS, and the institution can show what exists |
| `disagreement` | The institution disagrees with a finding or a classification |
| `adoption_notice` | The institution has formally adopted the Core Requirements |
| `change_notice` | The institution reports a change to its powers, safeguards, procedures, or limits, without necessarily adopting the Core Requirements |

A sound response:
- names the **exact record and version** it answers (`response_to`);
- carries the banner saying it **does not replace** that record;
- for a correction or disagreement, **quotes the record point by point**, with its section (such as P1 B4);
- follows the same source rules as a record (Section IV), with every number sourced;
- names the responder by **role**, not personal name, and says whether it is an official response of the institution.

What a response does and does not do:
- it is **filed beside** the record and never replaces it;
- it does **not change any finding by itself**;
- the preparer may accept it by issuing a new version; if not, it stays beside the record and readers judge;
- if an institution files its own record, that is a separate record. It never supersedes the outside record.

### Displays

Anyone who displays records should show **all versions and responses together**: the newest version first, with links to every earlier version and every response, and a one-line note of what changed. A display should also show prominently:
- who prepared the record (`person`, `ai_assisted`, or `authority`);
- whether an independent reviewer has spot-checked its sources.

A display that shows self-filed records as equal to independently checked ones hands the institution a legitimacy it has not earned.

---

## Section VI — Worked examples

Worked examples show how the framework applies to a **kind** of institution. They are not records of any real institution. The full guide is in the examples folder (`00-EXAMPLES-GUIDE.md`); its hard rules are:

1. **Nothing real and identifiable.** No real institution, place, person, product, vendor, court case, news outlet, or nonprofit. Use bracketed placeholders: `[CITY]`, `[COUNTY] Jail`, `[BODY-CAMERA VENDOR]`. National laws and agencies may be named generally ("the federal fair credit reporting law").
2. **No signature facts.** Don't reproduce a real body's distinctive combination of details: an exact settlement amount, a unique committee size or founding year, a named program, or a famous incident.
3. **Every illustrative figure is tagged `[EX]`,** in the same sentence or table row. Rule-derived numbers cite the Core Requirements instead.
4. **Front matter:** `example: true`; `record_id: SCBP-REG-EXAMPLE-{SUFFIX}`; `prepared_by: person` (or `authority` for an example of an authorization record, which the institution prepares itself); `official_url: NONE`; `bundle: NONE`.
5. **Banner** directly under the front matter: *"WORKED EXAMPLE — not a record of any real institution. Names, places, and figures are illustrative."*
6. **Findings must be realistic and evidence-aware, not automatic.** Show safeguards that plausibly exist for the kind of institution being illustrated, including statutory appeals, independent review, court injunctions, sunset clauses, or consent decrees.
   - Use `NONE EXISTS` only when the example explicitly establishes the safeguard's absence within its fictional scenario. Otherwise use `UNKNOWN`.
7. **End with non-binding teaching notes** citing Core Requirements rule numbers.
8. **Pass the checker** with no errors.

---

## Section VII — If you publish a record of a real institution

The framework does not publish these in v1. If you choose to publish your own, these conditions keep it fair. They follow from the framework's own commitments on informational sovereignty and communicative integrity (2.D.12, 2.D.8):

1. **Public interest.** The institution exercises authority, or materially affects an identifiable population, and the visibility you give it is proportionate to that.
2. **Public, cited sources only,** under the three-answer rule.
3. **Uncertainty is marked,** never filled in by assumption.
4. **No natural person is named.**
5. **Correction is easy.** You tell the institution how to respond, and you keep its responses beside your record, under the no-silent-replacement rule.

You are responsible for what you publish, including under ordinary law.

---

## Section VIII — What the checker checks

The record checker is `validate_record.py` (version 1.0.0, vocabulary 1.0.0). Run it on any draft:

```
python3 validate_record.py FILE [FILE ...]
```

It reports three levels:
- **ERROR**: must be fixed. The checker exits with code 1;
- **WARN**: should be looked at;
- **REVIEW**: needs a person to decide.

### Every file
- The front matter is present and valid.
- It states its form name, version, and date; the Core Requirements version and date; the bundle (or NONE); and the vocabulary version. A vocabulary mismatch is warned.
- Every controlled value comes from the shared vocabulary (`VOCAB.yml`).
- **Numbers without sources.** Any sentence or table row stating a figure with no `[S#]` (or, in examples, `[EX]`) tag is flagged. Rule numbers, power IDs, source IDs, and record IDs are not counted. This is how invented values get caught. In records it is an error; in witness reports, which are often first-hand, it is a warning.
- Possible personal names near accusation words are flagged for review.
- Unfilled template placeholders are warned.

### Registration records (observed, authorization, example)
- All required fields are present: record type, ID, version, `supersedes`, preparer, dates, institution, adoption status, powers.
- The record ID has the right shape. An example's ID is `SCBP-REG-EXAMPLE-…`, and it carries the WORKED EXAMPLE banner. `[EX]` tags appear only in examples.
- The file name matches the record ID (with `-v2` and so on for later versions).
- The institution's name, legal entity, type, country, and official URL are filled in (UNKNOWN is allowed).
- `ai_assisted` without a named AI tool is warned.
- Each power has an ID (P1, P2…), a valid category and authority basis, and a yes/no/UNKNOWN for force or confinement. Power IDs are not duplicated.
- A minor-power claim appears only in an authorization record, and never for a power that uses force or confinement (3.A.4).
- All ten findings are present and valid for each power, and match the table.
- Each listed power has its own body section, with sections B1 to B10 and the statement "Can anything stop this power as a whole?"
- **Version 2 and later** state `supersedes` and include `## What changed from version N`.
- An observed record contains no Part E. An authorization record must have one.
- The Sources section is present.

### Sources (records and responses)
- Every `[S#]` tag in the text has a row in the Sources table.
- Each row's kind is valid; it has a link or `BPF:` reference (unless first-hand) and says where in the source; a quote row has an actual quote; the verified value is valid.
- Sources listed but never cited are warned.
- Quotes seen only in summary (`unverified`) are listed for review.

### Authority responses
- Required fields are present, the response type is valid, and the response ID has the right shape.
- `response_to` names an exact record and version.
- The banner saying the response does not replace the record is present.
- A correction or disagreement without a point-by-point table is warned.

### Witness reports
- Required fields are present, and the report type, identity level, and status are valid.
- The report ID has the right shape, and the dates are valid.
- Location coordinates are in range, and no coordinates are given when the location is withheld.
- A stop signal states its basis (defined condition or credible pathway).

---

## Section IX — What only a human reviewer can check

The checker confirms form, not truth. A record that passes with no errors can still be wrong, or written in bad faith. The worked example of a bad-faith consulting firm (`SCBP-REG-EXAMPLE-BAD-FAITH-CONSULTING`) passes the checker cleanly to show exactly this.

**Before anyone relies on a record, a person should check:**

1. **Does each source say what the record claims?** Read the location against the claim. Spot-check at least the sources behind every not-conforming finding and every number that matters.
2. **Could an UNKNOWN have been found?** Is a NONE EXISTS based on looking where the thing would be?
3. **Is the authority basis right?** For example, whether a power is really `influence_only`. That needs evidence of how others actually use its outputs, and the right tier on the Causation Ladder.
4. **Is each "independent" holder really independent?** Who appoints, funds, and can remove it? (Definitions: Independent.)
5. **Who produces the number behind each threshold?** A threshold the institution counts, classifies, or confirms fails 3.A.5, even with all five parts filled in.
6. **Are minor-power claims sound?** The checker tests only the force condition; the other conditions of 3.A.4 need a person.
7. **Is anything missing?** Powers never listed; an authorizing body changed just before the record was written; work split across entities to stay under a limit (4.2).
8. **Are short `not_applicable` reasons true?**
9. **Are people named** anywhere the name heuristic missed, or identifiable from details?
10. **For a new version:** does the "What changed" section quote everything that changed, including removed text? Compare the two versions line by line.
11. **For a response:** does it quote the record accurately, and do its sources support it?
12. **For an example:** could it point to one real institution or event?

**The limit.** No form can stop bad-faith filing. What these standards can do is make every evasive answer specific, sourced, and public, so a reviewer knows exactly where to look, and an institution's own words can be quoted against it.

---

## Section X — Changing these standards

These standards change only by a new published version, with a version number, a date, and a list of what changed. Earlier versions stay public (6.5). A record states the form, vocabulary, and Core Requirements versions it was made under, so it is always judged by the standards that applied when it was made.

---

## Relationship to other documents

- **Core Requirements v1:** the binding rules. If this document conflicts with them, the Core Requirements govern.
- **SCBP-03 — Operations Manual:** Stage 0 (observed records) and Stage 1 (authorization records).
- **SCBP-08 — Witness Reports and Stop Signals:** witness reports, stop signals, challenges, and review petitions.
- **Forms:** Registration form 1.0.0, Witness Report form 1.0.0, Authority Response form 1.0.0, vocabulary 1.0.0.
- **Record checker:** `validate_record.py`.
- **Worked examples** and their guide, `00-EXAMPLES-GUIDE.md`.

---

*SCBP-09 — Record Quality Standards — guidance under the Core Requirements*
