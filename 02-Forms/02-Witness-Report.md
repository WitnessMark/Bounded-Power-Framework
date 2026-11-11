# Witness Report Form

*Form v1 · 2026-11-11 · Published for independent review · Not adopted · For use with Core Requirements v1 · Vocabulary: VOCAB.yml v1*

## What this is

If an institution did something, failed to do something, or threatened to do something that seems wrong to you, you can write it down here, as a **Witness Report**.

A witness report is a dated, written record of what an institution did, failed to do, or threatened to do. It is first a record for you: it keeps what you remember, and the details that identify what happened and who was involved, before they fade.

> **v1 has no place to file this.** Saving the form creates a dated file on your device, nothing more. Nobody receives it, publishes it, or answers it unless you choose to send it to someone. Most people should start with the plain [Witness Report Guide](../00-Reading/1-Something-Happened/Witness-Report-Guide.md), the [web form](https://witnessmark.org/witness-report/) or the [AI witness interview](../00-Reading/1-Something-Happened/AI-Witness-Interview-Bundle.md); this page is the technical form.

Use it for any of these:

| Report type | Use it when… | Core rule |
|---|---|---|
| `incident` | Something happened that you want on the record | 2.C.2 (reporting must be easy) |
| `stop_signal` | A defined limit was crossed, or there is a credible pathway to serious harm, and you want it to pause. Has an effect only on an institution that has adopted the Core Requirements; none has yet | 3.C.3 |
| `challenge` | The institution is acting outside its limits: beyond its scope, after expiry, retaliating, or blocking a stop path. With an institution that has adopted the Core Requirements it goes to independent review; with any other, it is a record | Parts III–V |
| `change_request` | You want a limit, safeguard, or procedure changed, even before anyone is harmed | 2.C.2 |
| `review_petition` | You are joining or starting a request by affected people to review, narrow, or end a power early. Has an effect only on an institution that has adopted the Core Requirements; none has yet | 3.E.5 |

A report is a dated record that **you keep**. If the institution has adopted the Core Requirements, a stop signal sent through its own stop-signal route starts the pause-then-check process (3.C.3). For any other institution, the report is a record and nothing more.

**You don't need to be a lawyer, an expert, or a formal party.** You don't need proof, a special format, or anyone's permission (2.C.2). Write what you know. Leave the rest as **UNKNOWN**.

**Under the Core Requirements, no penalty may attach to giving a stop signal or reporting** (3.C.6), and retaliation is itself a violation that you can report with this same form. That protection binds only institutions that have adopted the Core Requirements, and as of v1 none has. Against any other institution, a report brings visibility, not shelter. Your legal protections come from the law where you live, not from this framework.

## Four rules

1. **Made in good faith.**
2. **First-hand observation and public sources only.** What you saw, heard or went through yourself, and what public records show.
3. **Keep what's proven apart from what you saw or believe.** Adjudicated facts (a conviction, a settlement, a final order) are stated with their source. Everything else is your observation or an allegation.
4. **Nothing leaked or private.** No material you had no right to hold.

**Names and details are kept.** The report is a record to help you remember and to identify what happened: names, badge and ID numbers, unit and car numbers, licence plates, descriptions of people, places, phone numbers, and case and reference numbers. Write them down as you know them, and say how sure you are.

**This report names people. Sharing or publishing it can expose you to retaliation or a legal claim.** Think about who receives it. If you want a version to pass around that identifies no private person, make a [copy for sharing](#a-copy-for-sharing-optional).

## Choosing how identified you are

- **Identified** (name plus contact): carries the most weight, and keeps legal options open. It can expose you to retaliation.
- **Pseudonymous** (a stable handle, no legal name): you can be followed up with, and your reports can be linked over time.
- **Anonymous**: the most protection. It carries less weight and can't be followed up.

**Optional verification phrase** (stored as `verification_hash`). Make up a long secret phrase. Use at least five random words. Don't use your name, birthday, address, or anything about you. Calculate its SHA-256 hash and put only the hash in `verification_hash`. Keep the phrase private. If you choose to reveal it later, someone can check that it matches the recorded hash. This can help link you to the report, but does not independently prove who originally wrote it.

Any free "SHA-256 generator" can calculate the hash. Type the phrase exactly, with no space or Enter at the end, and note which tool you used.

## What the statement covers

The statement is written from your account. **Tell it first, your own way**; the questions come after, and only for what your account did not cover.

**Every report**

- **When:** the day, roughly what time, and whether it is still going on.
- **Where:** as exactly as you can.
- **Which organization or office.**
- **How you know:** it happened to you, you saw or heard it, you learned of it first-hand afterwards (a letter, the aftermath), someone told you, or you are reporting for someone else.
- **What happened, in order.**
- **Who did it:** a name, a badge or ID number, a job title, a unit or car number, what they looked like.
- **Who it was done to:** what they looked like, or what you know about them.
- **Who else saw or heard it,** and whether you know how to reach them.
- **What happened after:** how it ended; whether anyone was hurt, taken away, or left without something.
- **What it did to people:** money, health, housing, work, safety, fear.
- **Evidence:** video, photos, papers, messages, and where each is kept.
- **Whether it was reported anywhere,** and any case or reference number.
- **How sure you are** about each name, number and description.
- **Anything that could have changed your memory:** whether you talked with other witnesses, or saw video or news about it, before writing.

**Then, depending on the kind of situation** (`situation_kind`; a report can be more than one):

- **A scene** (something you saw happen: a stop, a raid, a confrontation): where you were and how far away; whether you could see clearly and hear what was said; the light; anything in the way; how long you watched and when you left; how many of them and how many others; vehicles (kind, colour, plate, car number); words said, as close to exact as you can; and what you did (recorded, spoke up, stepped in, left).
- **A process** (something done to you through decisions, letters or calls: an eviction, a benefit denied, a fine, a firing): each contact in order (the date, how, with whom, what was said or decided); case, account or reference numbers; the papers and messages you have; the decision and any reason given; whether you were told how to challenge it and by when; deadlines, and whether they were met.
- **A condition** (something ongoing you have noticed: contaminated water, mould, a camera network, a policy being applied): when you first noticed it; each time you noticed it since, and what you saw, smelled, measured or went through; any tests, by whom, and the result; who else is affected and roughly how many; whether anyone was warned; and whether it is getting better, worse, or staying the same.

**How the statement is written.** First person, past tense, in time order, one fact to a sentence: "I was riding my bike down John R when I saw…". Only what you said, in your words for things: no legal terms you did not use. What you were unsure of stays unsure: "about 1:30", "what looked like a flashlight". What is not known is left out of the statement; the technical fields record it as UNKNOWN. If someone else wrote it from your account (a helper, the AI interview, the web form), you read it and correct it before you sign it.

## How to save it

Save the report as `SCBP-WR-{SUFFIX}-{YYYY-MM-DD}.md`. SUFFIX is a short uppercase tag for the institution, with an optional place tag, such as `CITYPD-XX`. The date is the incident date, or the date of writing if the incident date is UNKNOWN. Add `-A`, `-B` for more than one report on the same day. Run the checker (`validate_record.py`) if you can. If not, skip it, or ask the AI to go through its "before you hand it over" checks. The report is yours: you decide whether to share it, and with whom.

## A copy for sharing (optional)

If you want a version to pass around, a second copy can be made that identifies no private person. It is never made automatically.

- **About me** (section 4) is left out.
- In the statement and in your own words, the names and details of **private people** are replaced with a description in square brackets: you, bystanders, the person it was done to, private addresses, licence plates of private vehicles, private phone numbers, account numbers. For example `[a bystander]`, `[the man in handcuffs]`.
- **People acting in an official role keep their names, badge numbers and unit or car numbers.** What an officer or official does on duty is public conduct.
- The place is given only as precisely as you choose: exact, the general area, the town, or withheld.
- The line `> **Copy for sharing.** Details that identify private people are replaced in [brackets]. The full report is kept by its author.` goes first, and a line under the quote in section 3 says what was replaced.
- The file name ends in `-SHARE`. `report_id` stays the same.

You see the list of replacements before the copy is made. Read it once more as a stranger would before sending it: no tool catches everything. The full report is never pasted into a new AI chat to make the copy: that gives another company everything in it.

---

## Report template

**How it is laid out.** The report comes first, for people: the statement, the evidence, your own words, and who you are. Below a line come the parts for record-keeping: the optional questions, what you are asking for, what happened next, and the technical fields, in a fixed format a computer reads. Keep each field name there as it is; the comment line under each field explains it and lists the allowed answers.

Each section starts with a prompt in italics; replace it with your answer. In the statement, leave out what is not known. In the record-keeping part, an optional question you skip is left out entirely.

````
# Witness Report - [Institution] - [Incident date]

**When:** [Incident date], about [time] · **Where:** [place] · **Statement of:** [name or handle] · **Written:** [date written]

## 1. Statement

*In the first person, in time order, from your account. Start with when, where, who you are and what you saw: "On November 11, 2026, at about 1:30 p.m., at the intersection of… I, [name], saw…". Then what happened, in order; who did it and who it was done to, with any names, numbers and descriptions, and how sure you are; where you were and what you could see and hear; who else was there; what happened after, and when you left; what it did to people; whether it was reported anywhere; and whether anything could have changed your memory.*

*For a process or a condition, add a dated list after the prose:*

**Contacts, in order.** *(a process)* / **Observations, in order.** *(a condition)*

- **YYYY-MM-DD.** *How (in person, letter, phone, email, online, a notice), with whom, what was said or decided, any reference number.*

*This statement was written from my account by [the AI interview / the web form / a helper]. I read it and confirm it.* (or) *I wrote this statement myself.*

- [ ] Made in good faith.
- [ ] First-hand observation and public sources only.
- [ ] What is proven is kept apart from what I saw or believe.
- [ ] Nothing leaked or private.

This statement is true to the best of my knowledge and belief.

**Signed:** [name or handle] · [date]

## 2. Evidence

*Each thing you are saying that comes from somewhere other than your own eyes and ears, where it comes from, and what kind of claim it is. Types: `adjudicated_or_admitted_fact` (a court judgment, a final order, an admission); `settled_without_admission` (a settlement where they admitted nothing); `institution_statement` (their own published rule, policy, notice or announcement: what they say they do, not proof that they did it); `my_observation` (I saw or heard it myself); `allegation_or_estimate` (everything else).*

| Claim | Source | Type |
|---|---|---|
| | | |

**What I have (not attached).** *Each item, and where you keep it: "video on my phone", "letter dated…", "case number…". The files stay with you.*

## 3. In my own words

*Exactly as you told it or wrote it. Not corrected or edited.*

> "…"

## 4. About me

*Left out of a copy for sharing.*

- **Name or handle:**
- **Contact:**
- **How I am connected to them:**
- **Verification phrase:** yes / no

---

# Record-keeping — not part of the statement

*Everything below this line is for record-keeping. A reader can stop here. Nothing below changes the statement.*

## 5. Optional questions

*Answer any that fit. Leave out any you skip.*

### What feels wrong about it

*Your concern, in your own words. No rule or law needs to be named.*

### What they should have done

*Something they were supposed to do to protect people and did not do, did late, or did only for some.*

### Does this happen to others?

*Whether this shows how it works for everyone: a protection or deadline that did not work, no way to challenge it or no one explaining how, a limit that was crossed, something they do that is written down nowhere. With a registration record: the part it bears on, a stop path (B5, by number), a requirement row (B4), or a Floor (B6).*

### Could it get worse, or last?

*A real risk of harm that spreads, builds up, lasts, or cannot be undone, including harm to land, water, air or living things. What could be affected, for how long, and what you saw that makes you think so. A warning, not a finding or a score.*

## 6. Asking for something to stop or change

*Only for a stop signal, a challenge, a change request or a review petition. For an incident, write "Not applicable."*

**Stop signal.**
- **Basis:**
  - [ ] a **defined condition**: a published limit or stop condition was crossed. Which one?
  - [ ] a **credible pathway to serious harm**: a real risk of serious harm that no published limit covers. The facts that show it, in your own words.
- **Now:** whether the harm is happening now or about to, and whether anyone is in immediate danger.

**Challenge, change request, or review petition.**
- **What limit is exceeded, or what should change:**
  - [ ] acting outside its scope or limits
  - [ ] operating after its term ended, or without authorization
  - [ ] a stop path is blocked or harder to use
  - [ ] someone was penalized for raising a concern or giving a stop signal
  - [ ] acted on wrong, outdated, or unverified information about me
  - [ ] a threshold depends on the institution's own findings
  - [ ] information was suppressed, distorted, or hidden
  - [ ] unequal treatment
  - [ ] a Floor is at stake (which one?)
  - [ ] other
- **What would fix it (optional):**
- **Joining an existing petition:** its ID, or NONE.

## 7. What happened next

*Filled in later by whoever reviews the report. Leave it blank.*

- Response from them, and its date:
- For a stop signal, the result of the independent check (did the trigger fact occur? yes / no / not checked), and its date:
- Effect on the power (paused, stopped, narrowed, changed in another way, or not changed), its date and source:
- Outcome:
- Linked reports:

---

## Technical details

*For computers. Left as written.*

```yaml
report_id: SCBP-WR-{SUFFIX}-{YYYY-MM-DD}
# Name of this report: SCBP-WR-, a short tag for the institution in CAPITALS, then the date it happened.
report_type: incident
# What kind of report is this? incident | stop_signal | challenge | change_request | review_petition
form: {name: witness-report, version: v1, date: 2026-11-11}
# The form version used. Leave as written.
core_requirements: {version: v1, date: 2026-11-05}
# The Core Requirements version this report refers to. Leave as written.
bundle: NONE
# Made with the AI interview? NONE if not. If so, the interview file's version and date: {version: x.y.z, date: YYYY-MM-DD}
vocab_version: v1
# The VOCAB.yml version whose values this report uses. Leave as written.
filed_date: YYYY-MM-DD
# The date you wrote this report.
composed_by: witness
# Who wrote the statement from your account? witness | ai_interview | web_form | helper
statement_confirmed: true
# Did you read the statement and confirm it? true | false
truth_statement: plain
# The line above your signature. plain ("true to the best of my knowledge and belief") | none
situation_kind: [scene]
# What kind of situation? One or more of: scene | process | condition
institution_name: ""
# Which institution? The name people know it by.
incident_date: YYYY-MM-DD
# When did it happen, or start? A date, or UNKNOWN.
incident_time: UNKNOWN
# Roughly what time? "HH:MM" in 24-hour time, in quotes, such as "13:30". Or UNKNOWN.
incident_end_date: NONE
# Has it ended? NONE (no end date) | YYYY-MM-DD (the date it ended) | ongoing
jurisdiction: {locality: UNKNOWN, region: UNKNOWN, country: UNKNOWN}
# Town or city, state or province, and two-letter country code (US, CA, GB...). Kept even when the place is withheld.
location:
  description: ""
  # Where did it happen? For example "the intersection of John R and Kirby streets, Detroit, MI".
  latitude: UNKNOWN
  # Map coordinates only if taken from a map app: decimal degrees | UNKNOWN | WITHHELD
  longitude: UNKNOWN
  precision: exact
  # How exact is the place? exact | approximate | locality (town or city) | region | withheld
action_category: [other]
# What did they do? One or more of: use_of_force | arrest_or_detention | stop_or_search | threat_or_intimidation |
# surveillance_or_data_collection | eviction_or_removal | utility_shutoff | fine_fee_or_seizure | benefit_or_service_denied |
# decision_without_explanation | retaliation | discrimination | failure_to_act | records_error | environmental_harm | other
harm_type: [none_known]
# What did it do to people? One or more of: physical_injury | death | loss_of_liberty | financial | housing | health |
# employment | privacy | emotional_distress | property | environmental | none_known
affected_count: unknown
# Roughly how many people were affected? one | 2_10 | 11_100 | over_100 | unknown
reporter_role: eyewitness
# How do you know? affected_person | eyewitness | learned_after | told_by_others | on_behalf_of
evidence_held: [none]
# What exists? One or more of: video | photo | audio | document | message | medical_record | physical | none
memory_influences: [none]
# Before writing, did anything else shape your memory? One or more of: none | talked_with_witnesses | saw_video | saw_news | unknown
identity_disclosure: pseudonymous
# How identified do you want to be? identified | pseudonymous | anonymous
verification_hash: NONE
# Optional. The SHA-256 code of your secret phrase, never the phrase itself. Or NONE.
stop_signal_basis: NONE
# Stop signals only. Was a published limit crossed (defined_condition), or is there a real risk of serious harm that no limit covers (credible_pathway)? NONE for every other report.
record_id: NONE
# A registration record for this institution, if you know of one (SCBP-REG-...). Otherwise NONE; you don't need one.
power_id: UNKNOWN
# Which power in that record? P1, P2..., or UNKNOWN.
```
````

---

## What happens to the report

**In v1:**

- **Kept by you.** Nothing is filed or published for you. If you share it, corrections are made by a new version; the original is never replaced.
- **No one is expected to respond.** No institution has adopted the Core Requirements, so none owes a response to a report.
- **No registration yet?** You can still write a report. Use `record_id: NONE`. The fact that no registration exists is itself worth knowing.

**If a place to send reports exists in future** (one is being considered; no host has been chosen and nothing is live), it would work like this:

- A registration record and power would be linked to the report on receipt, if the author did not give them, with a note of who made the link and when.
- Reports about the same event, the same power or the same place could be grouped and counted toward review (3.E.5, 7.7). Published counts would round the time to the hour and the place to the town, so that a pseudonymous author cannot be picked out.
- An institution that has adopted the Core Requirements would be expected to answer publicly within its published response window, and a missing answer would itself be recorded.

**Stop signals to an adopting institution**, sent through its own stop-signal route, follow 3.C.3: a pause, then an independent check of one question, "did the trigger fact occur?" A signal that only repeats facts already checked and found unfounded is recorded and counted, but does not pause the power again.
