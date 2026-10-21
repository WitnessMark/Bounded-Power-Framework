# How to Run a Citizen Inquiry

This guide shows you how to record an institution's powers with an AI assistant and the [AI Registration Bundle](AI-Registration-Bundle.md). For a shorter overview, see the [AI Registration Guide](06-AI-Registration-Guide.md).

The result is an **observed record**. It lists what the institution can do to people, one power at a time. For each power it compares what exists with what the [Core Requirements](../01-Framework/SCBP-04-Core-Requirements.md) require, and reports the gap.

Reading this guide takes about five minutes. The inquiry takes twenty minutes to an hour.

---

## Before you start

**You need:**
- an AI assistant (Claude, ChatGPT, or Gemini);
- an institution in mind.

**You do not need:**
- legal training;
- to know the framework well;
- the institution's internal documents;
- anyone's permission.

Public sources can provide a useful starting point: laws, court records, government reports, institutional publications, and reputable news. Some information may remain unavailable. Record those gaps as UNKNOWN rather than guessing.

---

## Step 1 — Pick an institution

Any institution that can affect people:
- a government body: police, a court, a jail, a benefits office, a licensing board;
- a private one you depend on: an insurer, a credit bureau, a platform, a landlord's screening company;
- a membership body: a homeowners' association, a cooperative, a congregation.

If it is huge, such as a whole city, a state, or a big company, pick the part that affects you. The AI will help you narrow it.

## Step 2 — Give the bundle to the AI

1. Download the bundle file: [`00-Reading/AI-Registration-Bundle.md`](AI-Registration-Bundle.md).
2. Open a new conversation and attach the file.
3. Type the institution and where it is, then send. For example: *"the county jail in my county"*.

You don't need to read the bundle. Only the short "FOR THE PERSON" part at the top is for you.

## Step 3 — Choose the powers

An institution usually holds several powers. A police department, for example, may use force, make arrests, run cameras, and tow cars. Each is recorded separately, because each has its own limits and its own way of being stopped.

The AI will list the powers it finds and ask which to record. Pick the ones that matter to you. Fewer powers recorded well beats many recorded badly.

## Step 4 — Let the AI research and write

The AI searches public sources and fills in the record. For each power it covers:
- what the power can do to people, and to whom;
- what it is based on (a law, a contract, a rule);
- whether it was authorized by an independent body, and whether it expires;
- whether harm limits are published;
- **what can stop it**, and whether anything can stop it as a whole;
- the four Floors: ecological, economic, agency, and human rights;
- what data it collects, and what it depends on.

## Step 5 — Read what you got

Look for three kinds of answer. The AI is not allowed to give any other kind.

| You see | It means |
|---|---|
| A value with a tag like `[S3]` | A fact, with its source listed in Part C |
| **UNKNOWN** | The available evidence does not establish the answer, including information the AI could not find, access, or verify |
| **NONE EXISTS** | Evidence establishes that the thing is missing: no expiry date, no published harm limit, no independent stop |

**NONE EXISTS is an important finding when supported by evidence.** It means the available evidence establishes that a required safeguard is absent, not merely that the AI could not find it. Do not use NONE EXISTS when the answer is UNKNOWN.

Then check:
- **Every number has a source tag.** If one doesn't, ask the AI to source it or change it to UNKNOWN.
- **Spot-check a few sources.** Open the link and see whether it says what the record claims. No tool can do this for you.
- **People are named by role,** such as "the sheriff" or "the director", never by name.
- **Facts are kept apart from allegations.** A court judgment or settlement is a fact; a lawsuit's claims are allegations.

If you can run Python, run the checker in `02-Forms/`: `python3 validate_record.py FILE`. It needs Python 3 and `pip install pyyaml`, with `validate_record.py` and `VOCAB.yml` in the same folder. Ask the AI to fix every ERROR. If you can't run it, skip it.

## Step 6 — Keep it

**The record is yours.** It is saved wherever you save it. Nobody files it. In v1 the framework publishes no records of real institutions.

You can:
- **keep it** for your own use;
- **share it** with others, such as a neighbourhood group, a journalist, or an oversight body;
- **publish it.** That is your choice and your responsibility: you are the one making those statements in public. Re-check the sources first.

If you learn something new later, make a **new version**. Add a section headed "What changed from version 1" that quotes the old text, gives the new text, and says why. Don't quietly overwrite the old one.

If the institution answers you, its answer belongs beside your record as an **authority response**, not inside it. You decide whether to accept each point in a new version. See the [water utility example](../03-Examples/SCBP-RSP-EXAMPLE-CITY-WATER-UTILITY-2026-10-21.md).

---

## If something goes wrong

**The AI can't read the bundle.** Attach it again, or try another of the three assistants. Attaching the file works better than pasting it.

**The AI made up a number, or guessed.** Say: *"Use only public sources. Where the evidence doesn't establish an answer, write UNKNOWN. Write NONE EXISTS only where evidence shows it doesn't exist. Never estimate."*

**The AI listed a stop path that isn't real.** Paying, complying, leaving, or switching a setting off is not a stop path. The general ability to pass a new law or abolish the institution doesn't count either, and nor does a vote by the institution's own board. A sunset vote that must take place, or a standing review body with power to end the power, can count if it is independent of the institution. Say: *"Count only stop paths that exist under current law and are held by someone independent of the institution."*

**The wording is loaded or angry.** Say: *"Describe structure, not motives. No loaded words and no bold for emphasis."* "No expiry date exists" is stronger than any adjective.

**The output stopped halfway.** Say: *"Continue from where you stopped,"* then ask for the whole record as one downloadable file.

**The institution is enormous.** Say: *"List its departments and their main powers, and let me choose."*

---

## Variations

- **Compare two institutions.** Record the same kind of power at each (for example, jail fees at two counties) and compare the findings row by row.
- **Go deeper on one power.** Record one power fully, then ask follow-up questions about its stop paths or data.
- **Learn from the examples first.** The fictional [worked examples](../03-Examples/README.md) show finished records for 32 fictional institutions.

---

## Records and witness reports

A record and a witness report are two halves of one picture:

- A **record** (this guide) shows how an institution's powers are built: their limits, stop paths, and gaps.
- A **witness report** documents something that **happened**: what an institution did, failed to do, or threatened to do. See the [Witness Report Filing Guide](09-Citizen-Witness-Report-Filing-Guide.md) or the [AI Witness Interview Bundle](10-AI-Witness-Interview-Bundle.md).

You can make either one without the other.

---

## Closing principle

The purpose is not to accuse. The purpose is to make visible how a power is built: who holds it, what limits it, and what can stop it. Anyone willing to ask the questions can do that.
