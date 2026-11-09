# Witness Report Form

*Form v1 · 2026-11-05 · Published for independent review · Not adopted · For use with Core Requirements v1 · Vocabulary: VOCAB.yml v1*

## What this is

If an institution did something, failed to do something, or threatened to do something that seems wrong to you, you can write it down here, as a **Witness Report**.

A witness report is a dated, written record of what an institution did, failed to do, or threatened to do. Use it for any of these:

> **v1 has no place to file this.** Saving the form creates a dated file on your device, nothing more. Nobody receives it, publishes it, or answers it unless you choose to send it to someone. Most people should start with the plain [Witness Report Guide](../00-Reading/1-Something-Happened/Witness-Report-Guide.md) or the [AI witness interview](../00-Reading/1-Something-Happened/AI-Witness-Interview-Bundle.md); this page is the technical form.

| Report type | Use it when… | Core rule |
|---|---|---|
| `incident` | Something happened that you want on the record | 2.C.2 (reporting must be easy) |
| `stop_signal` | A defined limit was crossed, or there is a credible pathway to serious harm, and you want it to pause. Has an effect only on an institution that has adopted the Core Requirements; none has yet | 3.C.3 |
| `challenge` | The institution is acting outside its limits: beyond its scope, after expiry, retaliating, or blocking a stop path. With an institution that has adopted the Core Requirements it goes to independent review; with any other, it is a record | Parts III–V |
| `change_request` | You want a limit, safeguard, or procedure changed, even before anyone is harmed | 2.C.2 |
| `review_petition` | You are joining or starting a request by affected people to review, narrow, or end a power early. Has an effect only on an institution that has adopted the Core Requirements; none has yet | 3.E.5 |

A report is a dated record that **you keep**. v1 has no place to file reports; you decide whether to share it, and with whom. If the institution has adopted the Core Requirements, a stop signal sent through its own stop-signal route starts the pause-then-check process (3.C.3). For any other institution, the report is a record and nothing more.

**You don't need to be a lawyer, an expert, or a formal party.** You don't need proof, a special format, or anyone's permission (2.C.2). Write what you know. Leave the rest as **UNKNOWN**.

**Under the Core Requirements, no penalty may attach to giving a stop signal or reporting** (3.C.6), and retaliation is itself a violation that you can report with this same form. That protection binds only institutions that have adopted the Core Requirements, and as of v1 none has. Against any other institution, a report brings visibility, not shelter. Your legal protections come from the law where you live, not from this framework.

## Choosing how identified you are

- **Identified** (name plus contact): carries the most weight, and keeps legal options open. It can expose you to retaliation.
- **Pseudonymous** (a stable handle, no legal name): recommended for most people. You can be followed up with, and your reports can be linked over time.
- **Anonymous**: the most protection. It carries less weight and can't be followed up.

**Optional verification phrase** (stored as `verification_hash`). Make up a long secret phrase. Use at least five random words. Don't use your name, birthday, address, or anything about you. Calculate its SHA-256 hash and put only the hash in `verification_hash`. Keep the phrase private. If you choose to reveal it later, someone can check that it matches the recorded hash. This can help link you to the report, but does not independently prove who originally wrote it.

Any free "SHA-256 generator" can calculate the hash. Type the phrase exactly, with no space or Enter at the end, and note which tool you used.

## Three rules that protect you and everyone else

1. **Public sources and your own observation only.** Nothing private, leaked, or speculative.
2. **Roles, not names, in any copy you share.** "The arresting officer", "the caseworker", not a person's name. An office that only one person holds (the Sheriff, the Mayor, the County Executive) identifies that person, so conduct is attributed to the office or the institution ("the Sheriff's Office", "the county"), not to the officeholder. Your own copy can keep names (see "Two copies" below).
3. **Keep what's proven apart from what you saw or believe.** Adjudicated facts (a conviction, a settlement, a final order) are stated with their source. Everything else is your observation or an allegation.

## Two copies

A report is first a record for its author, so nothing remembered is lost. It can be kept in two copies.

- **A full copy, for the author.** Names, the exact place, unit numbers, phone numbers and web addresses, as remembered. Each person is named by role first, with the name after it in square brackets: "the manager at the front desk [name]". The first line of the report is the full-copy line below. The file name ends in `-PRIVATE.md`.

  `> **Full copy. Private.** Names, places and contact details are kept as the witness gave them. This copy is not shared. A separate copy exists for sharing.`

- **A copy to share.** The same report without the bracketed names, and without anything else that points to a private person: the author's own name and contact (unless the author chooses to be identified), private addresses and phone numbers, a child's school, a made-up name that gives away a place. In the witness's own words (section 1), each one is replaced with its role in square brackets, such as `[the manager]`, and a line under the quote says so. The place is given only as precisely as is safe (see below). The full-copy line is left out. The file name has no `-PRIVATE`.

A lawyer, a legal aid service or an oversight body may need the full details; that is the author's call. The full copy is never pasted into a new AI chat to strip it: that gives another company everything in it.

## Location, and keeping yourself safe

In a copy to share, the location is given only as precisely as is **safe for the author**. Coordinates help reports about the same place be grouped. If an exact location could identify the author, the copy gives only the town or region, or the location is `withheld`.

## How to save it

Save the copy to share as `SCBP-WR-{SUFFIX}-{YYYY-MM-DD}.md`, and the full copy as `SCBP-WR-{SUFFIX}-{YYYY-MM-DD}-PRIVATE.md`. SUFFIX is a short uppercase tag for the institution, with an optional place tag, such as `CITYPD-XX`. The date is the incident date, or the date of writing if the incident date is UNKNOWN. Add `-A`, `-B` for more than one report on the same day. Run the checker (`validate_record.py`) if you can. If not, skip it, or ask the AI to go through its "before you hand it over" checks. The report is yours: you decide whether to share it, and with whom.

---

## Report template

**How it is laid out.** The report comes first, for people. The technical fields come last, under "Technical details", in a fixed format a computer reads. Keep each field name there as it is; the comment line under each field explains it and lists the allowed answers.

**How it is written.** Short, plain sentences. One fact to a sentence. People by role. No "you" and no "I", except inside the witness's own words. Each section starts with a prompt line in italics; replace it with the answer, or with UNKNOWN.

**The optional sections** (6 to 9) can be skipped. Each is UNKNOWN if skipped.
- **6, what seems wrong,** is the concern in the witness's own words.
- **7, protective duty,** asks what the witness saw or knows. It does not ask anyone to decide whether a duty was broken.
- **8, what this shows about the power,** asks whether what happened says something about how the power works for everyone. With a registration record for the institution, it can also name the part the report bears on. No record is needed.
- **9, potential harm warning,** is a warning, not a severity score or a finding. It does not change the stop-signal rules. An independent checking body still looks at the evidence.

Section 15, including the effect on the power, is filled in later by whoever reviews the report. It stays blank.

````
> **Public sources and first-hand observation only.** People are referred to by role. This is a good-faith report, not a verdict.

# Witness Report - [Institution] - [Incident date]

## 1. In the witness's own words

*What the institution did, failed to do, or threatened to do, told the witness's own way. Kept exactly as given.*

> "…"

## 2. Evidence

*Each key claim, where it comes from, and what kind of claim it is. Types: `adjudicated_or_admitted_fact` (a court judgment, a final order, an admission); `settled_without_admission` (a settlement where the institution admitted nothing); `institution_statement` (the institution's own published rule, policy, notice or announcement: what it says it does, not proof that it did it); `my_observation` (seen or heard first-hand); `allegation_or_estimate` (everything else).*

| Claim | Source | Type |
|---|---|---|
| | | |

**Kept, not attached.** *Each item, and where it is kept: "letter dated…", "photos on my phone", "case number…".*

## 3. Effect on people

*What it did to people: money, health, housing, work, safety, fear.*

## 4. People affected, and other people present

*Who is affected, and roughly how many. Whether any of them never chose to deal with this institution. Who else saw or heard it, by role.*

## 5. Earlier warnings, and attempts to fix it

*Whether it was raised with the institution or anyone else, before or after. How, when, and what came of it. Where any letter, complaint, inspection or report can be found.*

## 6. What seems wrong (optional)

*The concern, in the witness's own words. No rule or law needs to be named.*

## 7. Protective duty (optional)

*Something the institution was supposed to do to protect people and did not do, did late, or did only for some.*

## 8. What this shows about the power (optional)

*Whether this shows how the power works for everyone: a protection, exemption or deadline that did not work; a way to challenge the decision that was missing or not explained; a limit that was crossed; a practice written down nowhere. With a registration record: the part it bears on, a stop path (B5, by number), a requirement row (B4), or a Floor (B6).*

## 9. Potential harm warning (optional)

*A credible risk of harm that spreads, builds up, lasts, or cannot be undone, including harm to land, water, air or living things. What may be affected, for how long, and what was seen that suggests it.*

## 10. Timeline

*What happened, in order, with dates and times where known. How each thing was done or said: in person, by letter, by phone, by email, online, by a notice. For a call: the number, the date and time, and any reference number. For a website: its address and the date it was seen.*

## 11. The institution and the power

- **Institution:** *the name people know it by, and where.*
- **Power used:** *in plain words: an arrest, a fine, a benefit denial, a shutoff, a credit score.*
- **Registration record:** [record_id and power_id, or NONE]

## 12. Stop signal, challenge, change request, or review petition

*Only for these report types. For an incident, write "Not applicable."*

**Stop signal.**
- **Basis:**
  - [ ] a **defined condition**: a published limit or stop condition was crossed. Which one?
  - [ ] a **credible pathway to serious harm**: a real risk of serious harm that no published limit covers. The facts that show it, in the witness's own words.
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

## 13. Honesty

- [ ] Made in good faith.
- [ ] Public sources and my own observation only.
- [ ] Roles, not names, in any copy I share.
- [ ] Facts kept separate from allegations.

## 14. The witness

- **Name or handle:**
- **Contact:**
- **Relationship to the institution:**
- **Verification phrase:** yes / no

## 15. Resolution

*Filled in later by whoever reviews the report.*

- Response from the institution, and its date:
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
form: {name: witness-report, version: v1, date: 2026-11-05}
# The form version used. Leave as written.
core_requirements: {version: v1, date: 2026-11-05}
# The Core Requirements version this report refers to. Leave as written.
bundle: NONE
# Made with the AI interview? NONE if not. If so, the interview file's version and date: {version: x.y.z, date: YYYY-MM-DD}
vocab_version: v1
# The VOCAB.yml version whose values this report uses. Leave as written.
record_id: NONE
# Do you know of a registration record for this institution? Its ID (SCBP-REG-...), or NONE. You don't need one.
power_id: UNKNOWN
# Which power in that record? P1, P2..., or UNKNOWN.
institution_name: ""
# Which institution? The name people know it by.
incident_date: YYYY-MM-DD
# When did it happen, or start? A date, or UNKNOWN.
incident_end_date: NONE
# Has it ended? NONE (no end date) | YYYY-MM-DD (the date it ended) | ongoing
filed_date: YYYY-MM-DD
# The date you wrote this report.
location:
  description: ""
  # Where did it happen? For example "intake area, [COUNTY] jail, [CITY], [STATE]".
  latitude: UNKNOWN
  # Map coordinates only if taken from a map app: decimal degrees | UNKNOWN | WITHHELD
  longitude: UNKNOWN
  precision: locality
  # How exact is the place? exact | approximate | locality (town or city) | region | withheld
stop_signal_basis: NONE
# Stop signals only. Was a published limit crossed (defined_condition), or is there a real risk of serious harm that no limit covers (credible_pathway)? NONE for every other report.
identity_disclosure: pseudonymous
# How identified do you want to be? identified | pseudonymous | anonymous
verification_hash: NONE
# Optional. The SHA-256 code of your secret phrase, never the phrase itself. Or NONE.
status: ongoing
# Is it still going on? ongoing | resolved | unknown (UNKNOWN is also accepted)
```
````

---

## What happens to the report

**In v1:**

- **Kept by you.** Nothing is filed or published for you. If you share it, corrections are made by a new version; the original is never replaced.
- **No one is expected to respond.** No institution has adopted the Core Requirements, so none owes a response to a report.
- **No registration yet?** You can still write a report. Use `record_id: NONE`. The fact that no registration exists is itself worth knowing.

**If a place to send reports exists in future** (one is being considered; no host has been chosen and nothing is live), it would work like this:

- Reports you choose to send could be grouped with others about the same power or place, and counted toward review (3.E.5, 7.7).
- An institution that has adopted the Core Requirements would be expected to answer publicly within its published response window, and a missing answer would itself be recorded.

**Stop signals to an adopting institution**, sent through its own stop-signal route, follow 3.C.3: a pause, then an independent check of one question, "did the trigger fact occur?" A signal that only repeats facts already checked and found unfounded is recorded and counted, but does not pause the power again.
