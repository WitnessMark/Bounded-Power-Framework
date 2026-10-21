# AI Registration Guide

The AI Registration Bundle is one file you give to an AI assistant. The AI then helps you record the powers of a real institution: what it can do to people, what limits it has, and what is missing.

**The bundle is here: [`00-Reading/AI-Registration-Bundle.md`](AI-Registration-Bundle.md).**

It contains the instructions for the AI, the Registration Form, the shared vocabulary, and the full Core Requirements. You only need to read the short part at the top headed "FOR THE PERSON".

---

## How to use it

1. **Download the bundle file** from the link above.
2. **Open an AI assistant** (Claude, ChatGPT, or Gemini) and **attach the file.** It may show as a small file icon. That is normal.
3. **Say which institution, and where.** For example: "the county jail where I live" or "the credit bureau that has my file".
4. **Choose its powers.** The AI lists what the institution can do (arrest, fine, collect data, deny benefits…) and asks which to record. Pick one, a few, or all.
5. **Read the draft it gives you.**
   - **UNKNOWN** means the available evidence does not establish the answer, including information the AI could not find, access, or verify.
   - **NONE EXISTS** means evidence establishes that a safeguard is missing, such as no expiry date or no independent way to stop the power. These are often the most important parts.
   - Every number should have a source tag like `[S3]`. Spot-check a few sources yourself: the checker can confirm a number has a source, but only a person can confirm the source says it.
6. **Check it, if you can.** The checker needs Python 3 and `pip install pyyaml`; download `validate_record.py` and `VOCAB.yml` from `02-Forms/` into the same folder, then run `python3 validate_record.py FILE`. Ask the AI to fix every ERROR. If you can't run it, skip it and ask the AI to go through its self-check list again.

**Your own experience.** If you saw or experienced something yourself (what a notice said, a fee you were charged), the AI can record it as a `first_hand` source, with no link. What happened to you personally belongs in a separate witness report: see the [Witness Report Filing Guide](09-Citizen-Witness-Report-Filing-Guide.md).

The step-by-step guide, with what to do when something goes wrong, is the [Citizen Inquiry Guide](05-Citizen-Inquiry-Guide.md).

---

## The result is your record

- **The record belongs to you.** Nobody files it, stores it, or publishes it for you. In v1 the framework publishes no records of real institutions.
- **Publishing it is your choice and your responsibility.** If you share it, you are the one making those statements in public. Check the sources first, keep people as roles not names, and keep facts separate from allegations.
- **It is an observed record.** It describes what exists and compares it with the Core Requirements. It is not a verdict, and it does not say the institution broke any law.
- **If you later learn something new,** issue a new version yourself. Quote what changed; don't quietly replace the old one.

To see what finished records look like, read the fictional [worked examples](../03-Examples/README.md).
