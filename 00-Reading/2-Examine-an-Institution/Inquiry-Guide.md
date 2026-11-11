# Inquiry Guide

An inquiry produces an **observed record** of an institution: what it can do to people, one power at a time, and how each power compares with the [Core Requirements](../../01-Framework/SCBP-04-Core-Requirements.md). The record reports what exists and what is missing. It is a structural description, not an accusation and not a verdict.

An inquiry needs no legal training, no detailed knowledge of the framework, no internal documents, and no one's permission. It draws on public sources: laws, regulations, court records, government reports, the institution's own publications, and reputable news. Some answers will not be found. Those are recorded as UNKNOWN, never guessed.

With an AI assistant, an inquiry takes between twenty minutes and an hour. By hand, it takes longer.

## 1. Choose the institution

Any institution that can affect people qualifies:

- a government body: police, a court, a jail, a benefits office, a licensing board;
- a private body people depend on: an insurer, a credit bureau, a platform, a tenant-screening company;
- a membership body: a homeowners' association, a cooperative, a congregation.

A very large institution, such as a whole city, a state or a large company, holds powers in many departments. The inquiry is narrowed to the part that matters.

## 2. Choose the powers

An institution usually holds several powers. A police department may use force, make arrests, run cameras and tow cars. Each is recorded separately, because each has its own limits and its own ways of being stopped. A few powers recorded well are worth more than many recorded badly.

For each power, the record establishes:

- what the power can do to people, and to whom;
- what it rests on: a law, a contract, a rule;
- whether an independent body authorized it, and whether it expires;
- whether harm limits are published;
- **what can stop it**, and whether anything can stop it as a whole;
- whether it reaches the four Floors: ecological, economic, agency, and human rights;
- what data it collects, and what it depends on.

## 3. Make the record

### With an AI assistant

1. **Download the bundle:** [AI-Registration-Bundle.md](AI-Registration-Bundle.md). It holds the instructions for the AI, the registration form, the vocabulary and the full Core Requirements. Only the short part at the top, headed "FOR THE PERSON", is meant for people.
2. **Open a new conversation** in an AI assistant (Claude, ChatGPT or Gemini) and **attach the file**.
3. **Name the institution and where it is**, for example "the county jail in [county], [state]", and send.
4. **Choose the powers** from the list the AI returns.
5. **Read the draft and work through its checking list** (step 4).

### By hand

Copy the template from the [registration form](../../02-Forms/01-Registration.md) into a new text file and complete it from top to bottom, one power section at a time. The form explains each question.

A personal observation of a structural fact, such as what a notice said or what fee was charged, can be recorded as a `first_hand` source, with no link. A personal incident belongs in a separate [witness report](../1-Something-Happened/Witness-Report-Guide.md).

## 4. Check what came back

Every answer in a record is one of three kinds. No other kind is allowed.

| Answer | Meaning |
|---|---|
| A value with a tag such as `[S3]` | A fact, with its source listed in Part C |
| **UNKNOWN** | The available evidence does not establish the answer, including what could not be found, opened or verified |
| **NONE EXISTS** | Evidence shows the thing is absent: no expiry date, no published harm limit, no independent stop |

NONE EXISTS is often the most important finding, but only when evidence supports it. Failing to find something is UNKNOWN, not NONE EXISTS.

The AI ends with a **checking list**: each source it could not read in full, with its link, what to look for, and which parts of the record depend on it. Each source is opened and read. Where it says what the record says, `unverified` becomes `yes`. Where it does not, the record is corrected or the claim becomes UNKNOWN. A record with unchecked sources is a draft.

Then:

- **Every number has a source tag.** A number without one is sourced or changed to UNKNOWN.
- **People appear by role,** such as "the director" or "the arresting officer", never by name. An office that only one person holds, such as the Sheriff or the Mayor, identifies that person, so conduct is attributed to the office or the institution.
- **Every court case has a link** to the decision or to a reputable report of it. A case an AI cites without one may not exist, or may not say what is claimed; the checker flags it.
- **Facts stay apart from allegations.** A court judgment or a settlement is a fact; the claims in a lawsuit are allegations.

The checker in `02-Forms/` can test the file, for those who can run Python: `python3 validate_record.py FILE`, with Python 3, `pip install pyyaml`, and `validate_record.py` and `VOCAB.yml` in the same folder. Every ERROR is fixed. The checker is optional.

## 5. Keep it

*The record belongs to its author.* It is saved wherever its author saves it, and no one files it. This project publishes no records of real institutions.

A record can be kept for private use, shared with others such as a neighbourhood group, a journalist or an oversight body, or published. Publishing is the author's choice and responsibility: the author is the one making those statements in public, and checks the sources again first.

New information calls for a **new version**, with a section headed "What changed from version 1" that quotes the old text, gives the new, and says why. The old version is never quietly overwritten.

An answer from the institution belongs beside the record, as an **authority response**, not inside it. The author decides point by point whether to accept it in a new version. The [water utility example](../../03-Examples/SCBP-RSP-EXAMPLE-CITY-WATER-UTILITY-2026-11-05.md) shows the whole exchange.

## When something goes wrong

**The AI cannot read the bundle.** Attach it again, or try another assistant. Attaching works better than pasting.

**The AI invented a number or guessed.** Tell it: *"Use only public sources. Where the evidence does not establish an answer, write UNKNOWN. Write NONE EXISTS only where evidence shows it does not exist. Never estimate."*

**The AI cited an encyclopedia or a summary instead of the source.** Tell it: *"Cite the primary source: the law, the regulation, the court record or the institution's own publication. If you cannot open it, mark the claim unverified and put the link on the checking list."*

**The AI listed a stop path that is not real.** Paying, complying, leaving or switching a setting off is not a stop path. Neither is the general ability to pass a new law or abolish the institution, nor a vote by the institution's own board. A sunset vote that must take place, or a standing review body with power to end the power, counts if it is independent of the institution. Tell it: *"Count only stop paths that exist under current law and are held by someone independent of the institution."*

**The wording is loaded.** Tell it: *"Describe structure, not motives. No loaded words and no bold for emphasis."* "No expiry date exists" carries more weight than any adjective.

**The output stopped partway.** Tell it: *"Continue from where you stopped,"* then ask for the whole record as one file.

**The institution is very large.** Tell it: *"List its departments and their main powers, and let me choose."*

## Variations

- **Two institutions compared.** The same kind of power is recorded at each, such as jail fees in two counties, and the findings compared row by row.
- **One power in depth.** One power is recorded fully, then followed by questions about its stop paths or its data.
- **The examples first.** The [worked examples](../../03-Examples/README.md) are finished records of 32 fictional institutions.

## Records and witness reports

A record and a witness report are two halves of one picture. A **record** shows how an institution's powers are built: their limits, their stop paths, and their gaps. A **witness report** puts on record what one of those powers did. See the [Witness Report Guide](../1-Something-Happened/Witness-Report-Guide.md).

Either can be made without the other. When both exist, a witness report can name the record, the power, and the part of the record the incident bears on, such as a stop path that did not work (the optional question "Does this happen to others?" in the [witness report form](../../02-Forms/02-Witness-Report.md)). A shared record lets people who make reports use it this way.

## Purpose

The purpose is not to accuse. It is to make visible how a power is built: who holds it, what limits it, and what can stop it.
