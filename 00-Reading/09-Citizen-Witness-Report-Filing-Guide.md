# How to Make a Witness Report

A **witness report** is a dated, written record of something an institution did, failed to do, or threatened to do. You write it in a set shape, so that it can be read, compared with other reports, and checked.

> **If anyone is in danger right now, contact emergency services first.** A witness report is a record, not a rescue.

---

## The easy way: let an AI interview you

About 20 minutes. You answer questions; the AI writes the report.

1. **Download the interviewer file:** [AI-Witness-Interview.md](https://raw.githubusercontent.com/WitnessMark/Bounded-Power-Framework/main/00-Reading/10-AI-Witness-Interview-Bundle.md)
   - **iPhone or iPad:** press and hold the link, then tap **Download Linked File**. It is saved in the **Files** app, under **Downloads**.
   - **Android:** press and hold the link, then tap **Download link**.
   - **Computer:** right-click the link, then choose **Save link as**.
2. **Open an AI app** (such as ChatGPT, Claude, or Gemini) and start a **new chat**.
3. **Attach the file.** Tap the **+** or 📎 button and choose the file you downloaded.
4. **Type "Interview me."** Answer in your own words. You can skip any question or stop at any time.
5. **Download your report at the end.** The AI offers it as a file. Save it on your phone or computer. If your AI app can't make files, it gives you the text and tells you how to save it.

**Don't upload photos or videos to the AI chat.** Just tell it what you have and where you keep it.

The rest of this page explains each part in more detail, and how to write the report yourself without an AI.

---

## What kind of report?

One form covers five kinds of report. Pick the one that fits best. If you're not sure, choose `incident`.

| Type | Use it when… |
|---|---|
| `incident` | Something happened that you want on the record |
| `stop_signal` | A defined limit was crossed, or there is a real risk of serious harm, and you want the power paused (Core Requirements 3.C.3). It has an effect only on an institution that has adopted the Core Requirements, and none has yet |
| `challenge` | The institution is acting outside its limits: beyond its scope, after its term ended, blocking a way to stop it, or punishing someone for speaking up |
| `change_request` | You want a limit or safeguard changed, even before anyone is harmed |
| `review_petition` | You are joining or starting a request by affected people to review, narrow, or end a power early (3.E.5) |

---

## Before you start

**You need:**
- an institution, and something specific it did, failed to do, or threatened to do;
- whatever you remember or can point to: dates, what you saw, any public records.

**You don't need:**
- a lawyer, or any legal training;
- proof, special wording, or anyone's permission (2.C.2);
- a registration record of the institution;
- to give your name.

---

## Three rules that protect you

1. **Public sources and your own observation only.** Write what you saw or heard yourself, or what public records show. Leave out anything private, leaked, or guessed.
2. **Roles, not names.** Write "the officer", "the caseworker", "the manager". Never a person's name. The report is about the institution. Naming a person can turn a record into a personal fight, and can put you at legal risk.
3. **Keep what's proven apart from what you saw or believe.** A conviction, a settlement, or a final order can be stated as fact, with its source. Everything else is "what I observed" or "an allegation". Never write an allegation as if it were proven.

---

## Step 1 — Start with where

Say where it happened, as exactly as is **safe for you**. Reports about the same place can then be grouped together.

- If an exact address could identify you (your home, a small workplace), give only the town or region.
- You can choose `withheld` and give no location at all.
- If you give map coordinates, take them from a map app. Never guess.

## Step 2 — Write down what happened

In plain words, with people by role only:
- **in your own words:** what happened, as you would tell a friend;
- **when:** dates and times, in order, as far as you know them;
- **the impact:** what it actually did to people;
- **who is affected:** roughly how many, and whether any of them never chose to deal with this institution;
- **what you already tried:** did anyone raise it with the institution? What happened?

Gaps are fine. Write **UNKNOWN** for anything you don't know. A report with honest gaps is far better than none.

## Step 3 — List your evidence; don't attach it

Make a list of what exists and where it can be found: "letter dated…", "case number…", "photos on my phone", "a receipt".

**Don't put photos, video, or recordings in the report.** Faces and voices identify people, and files carry hidden data such as location and time. Instead:
- keep your originals safe, with backups;
- give them only to someone who needs them, such as a lawyer or an oversight body;
- link only to media that is **already public**.

**Optional proof that a file existed today:** use a free "SHA-256 generator" on the file and write only the resulting code in the report. Later you can show the file matches the code, without publishing the file now.

## Step 4 — Choose how identified you are

- **Identified** (your name and contact): carries the most weight. It can expose you to retaliation.
- **Pseudonymous** (a made-up name you keep using): recommended for most people. You can be followed up, and your reports can be linked to each other.
- **Anonymous:** the most protection. It carries less weight and can't be followed up.

**Optional proof that the report is yours** (skip it if unsure): make up a long secret phrase, turn it into a code with a SHA-256 generator, and put only the code in `verification_hash`. Type the phrase exactly, with no space or Enter at the end, and note which tool you used, so the code matches later. Keep the phrase private. Revealing it later proves you wrote the report.

## Step 5 — Fill in the form

Two ways:
- **With an AI.** Follow [the easy way](#the-easy-way-let-an-ai-interview-you) at the top of this page. The [interviewer file](https://raw.githubusercontent.com/WitnessMark/Bounded-Power-Framework/main/00-Reading/10-AI-Witness-Interview-Bundle.md) asks one question at a time, keeps your words as you said them, builds the report, and gives it to you as a file to download. You can also [read the file here](10-AI-Witness-Interview-Bundle.md) first.
- **By hand.** Copy the template from the [Witness Report Form](../02-Forms/02-Witness-Report.md) into a new text file and work from top to bottom.

Name the file `SCBP-WR-{SHORT-NAME}-{date}.md`, for example `SCBP-WR-COUNTYJAIL-2026-10-01.md`, using the date it happened. If you don't know that date, use the date you write the report.

To see what a finished report looks like, read the fictional [example witness report](../03-Examples/Challenge-Workflow/SCBP-WR-EXAMPLE-TOWN-LIBRARY-2026-10-06.md).

If you can, run the checker in `02-Forms/`: `python3 validate_record.py FILE` (it needs Python 3 and `pip install pyyaml`). Fix every ERROR. Dates and figures in your own account are not flagged: your observation is its own source. **If you can't run it, skip it.** If you used the AI interview, ask the AI to go through its "Before you hand it over" checks.

## Step 6 — Keep it

**Your report is yours.** It is a file on your device. Nobody stores it for you. If you used an AI, download the file it gives you before you close the chat.

**There is no place to file witness reports in v1 yet.** A private way to send reports, and a public site to read them, are being considered, but no host has been chosen and no date is promised. Until then, don't send reports to the project's code repository or its issue pages.

Keep a dated copy: for example, email the file to yourself, or save it somewhere with automatic dates. That shows when it was written.

---

## Sharing your report safely

You decide whether to share it, with whom, and when. Before you share:

1. **Read it once as a stranger would.** Could a detail identify you, such as your street, your shift, or a rare job title? Change the place to a wider area, or leave the detail out.
2. **Check for names** of anyone, including yourself. Use roles.
3. **Share a text copy only.** Don't send the original photos with it.
4. **Use a separate email address** if you are reporting pseudonymously.
5. **Think about who receives it.**
   - A lawyer, legal aid service, or oversight body (an inspector general, an ombudsman, a licensing board) can act on it.
   - A journalist may publish it. Agree first how you will be described.
   - The institution itself. If it has adopted the Core Requirements, it must have a public way to receive stop signals and reports, and must never penalize you for using it (3.C.6, 7.5). If it hasn't adopted them, think about retaliation before sending it directly.
6. **If you publish it yourself,** you are the one making those statements in public. Stick to what you saw and what public records show.

For plain-language options on what you can do next, see [What You Can Do](07-What-You-Can-Do.md). It is information, not legal advice.

---

## If you're worried about retaliation

That worry is reasonable.
- Use a **pseudonym** or file **anonymously**.
- Use the **verification phrase** if you may want to step forward later.
- Under the Core Requirements, no penalty may attach to reporting or challenging an authority. Retaliation is itself a violation, and you can report it with this same form (3.C.6).

Be clear about the limits. That protection binds only institutions that have adopted the Core Requirements, and as of v1 none has. Against any other institution, a report brings **visibility, not shelter**. Choose how identified you are with that in mind. Your legal protections, such as whistleblower and anti-retaliation laws, come from the law where you live, not from this framework.

---

## A stop signal to an institution that has adopted the Core Requirements

If the institution has adopted the Core Requirements, a stop signal has a defined effect (3.C.3):
- A signal that a **defined limit** was crossed pauses the operation at once.
- A signal about a **credible risk of serious harm** that no limit covers takes effect once a checking body confirms, within hours, that your facts, if true, describe such a risk. You don't need any special wording; the checking body records the facts.
- An independent body then checks one question only: **did it happen?** If not, the pause ends, and you owe nothing for a false alarm. If so, the pause becomes a stop.

Send it through the institution's published stop-signal route. For any other institution, the report is a record and nothing more.

---

## Closing principle

The purpose is not to accuse. It is to put a specific, dated, honest account on paper, where it can be read and counted. If the institution stays silent, that silence can be recorded too.
