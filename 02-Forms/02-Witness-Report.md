# Witness Report Form

*Form version 1.0.0 · 2026-10-21 · Published for independent review · Not adopted · For use with Core Requirements v1 · Vocabulary: VOCAB.yml 1.0.0*

## What this is

If an institution did something, failed to do something, or threatened to do something that seems wrong to you, you can write it down here, as a **Witness Report**.

A witness report is a dated, written record of what an institution did, failed to do, or threatened to do. Use it for any of these:

> **v1 has no place to file this.** Saving the form creates a dated file on your device, nothing more. Nobody receives it, publishes it, or answers it unless you choose to send it to someone. Most people should start with the plain [filing guide](../00-Reading/09-Citizen-Witness-Report-Filing-Guide.md) or the [AI witness interview](../00-Reading/10-AI-Witness-Interview-Bundle.md); this page is the technical form.

| Report type | Use it when… | Core rule |
|---|---|---|
| `incident` | Something happened that you want on the record | 2.C.2 (reporting must be easy) |
| `stop_signal` | A defined limit was crossed, or there is a credible pathway to serious harm, and you want it to pause. Has an effect only on an institution that has adopted the Core Requirements; none has yet | 3.C.3 |
| `challenge` | The institution is acting outside its limits: beyond its scope, after expiry, retaliating, or blocking a stop path | Parts III–V |
| `change_request` | You want a limit, safeguard, or procedure changed, even before anyone is harmed | 2.C.2 |
| `review_petition` | You are joining or starting a request by affected people to review, narrow, or end a power early | 3.E.5 |

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
2. **Roles, not names.** Write "the arresting officer" or "the caseworker", not a person's name.
3. **Keep what's proven apart from what you saw or believe.** Adjudicated facts (a conviction, a settlement, a final order) are stated with their source; everything else is your observation or an allegation.

## Location, and keeping yourself safe

Give the location as precisely as is **safe for you**. Coordinates help reports about the same place be grouped together. If an exact location could identify you, give only the city or region, or choose `withheld`.

## How to save it

Save the report as `SCBP-WR-{SUFFIX}-{YYYY-MM-DD}.md`. SUFFIX is a short uppercase tag you choose for the institution, with an optional place tag, such as `CITYPD-XX`. Use the incident date (if the incident date is UNKNOWN, use the date you wrote the report). Add `-A`, `-B` for more than one report on the same day. Run the checker (`validate_record.py`) if you can. If you can't, skip it, or ask the AI to go through its "before you hand it over" checks. The report is yours: you decide whether to share it, and with whom.

---

## Report template

**How it is laid out.** The part between the two `---` lines holds the technical fields, in a fixed format a computer can read. Keep each field name as it is. The line under each field asks the same thing as a plain question, and lists the allowed answers. The numbered sections below it are the questions you answer in your own words.

**The optional questions** (2f, 2g, 2h) can be skipped. Answer them only if they fit what you know.
- **2f, potential harm warning**, is a warning, not a severity score or a finding. It does not change the stop-signal rules. An independent checking body still looks at the evidence.
- **2g, protective duty**, asks what you saw or know. It does not ask you to decide whether a duty was broken.
- **2h, what seems wrong to you**, is your concern in your own words.

Section 8, including the effect on the power, is filled in later by whoever reviews the report. Leave it blank.

```
---
report_id: SCBP-WR-{SUFFIX}-{YYYY-MM-DD}
# Name of this report: SCBP-WR-, a short tag for the institution in CAPITALS, then the date it happened.
report_type: incident
# What kind of report is this? incident | stop_signal | challenge | change_request | review_petition
form: {name: witness-report, version: 1.0.0, date: 2026-10-21}
# The form version used. Leave as written.
core_requirements: {version: v1, date: 2026-10-21}
# The Core Requirements version this report refers to. Leave as written.
bundle: NONE
# Made with the AI interview? NONE if not. If so, the interview file's version and date: {version: x.y.z, date: YYYY-MM-DD}
vocab_version: 1.0.0
# The VOCAB.yml version whose values this report uses. Leave as written.
record_id: NONE
# Is there a registration record for this institution? Its ID (SCBP-REG-...), or NONE.
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
---

> **Public sources and first-hand observation only.** People are referred to by role or title. This is a good-faith report, not a verdict.

# Witness Report — [Institution] — [Incident date]

## 1. The institution, and which power
- Which institution, and where:
- What power did it use over people? Say it in plain words (for example "arrest", "fines", "credit score", "benefit denial"):
- Registration record, if one exists: [record_id and power_id, or NONE]

## 2. What happened
2a. **In your own words.** What did the institution do, fail to do, or threaten to do? Use roles, not names.

> "…"

2b. **Timeline.** What happened, in order? Give dates and times if you know them.
2c. **Impact.** What did it do to people?
2d. **Who is affected.** Which people or groups? Roughly how many? Did any of them never choose to deal with this institution?
2e. **Earlier warnings and attempts to fix it.** Did anyone warn about this, or raise it with the institution, before or after it happened? What happened then? Is there anything that shows the risk was known, such as a letter, a complaint, an inspection, or a report? Say where it can be found.
2f. **Potential harm warning (optional):** Is there a credible risk of widespread, cumulative, long-lasting, or irreversible harm, including ecological harm? Describe what may be affected, the possible extent and duration, and any observations or evidence supporting the concern. Use UNKNOWN where necessary.
2g. **Protective duty (optional).** Was there something the institution was supposed to do to protect people that it did not do, did late, or did only for some people? You can skip this if you don't know.
2h. **What seems wrong to you? (optional)** Say it in your own words. You don't need to name a rule or a law.

## 3. For a stop signal only
3a. **Basis:**
  - [ ] a **defined condition**: a published limit or stop condition was crossed. Which one?
  - [ ] a **credible pathway to serious harm**: a real risk of serious harm that no published limit covers. What facts show it? Describe them in your own words; the checking body records them.
3b. Is the harm happening **now**, or about to? Is anyone in immediate danger?

## 4. For a challenge, change request, or review petition only
4a. **What limit is being exceeded, or what should change?** Mark any that apply:
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
4b. **What would fix it?** (optional)
4c. **For a review petition:** is this joining an existing petition? Give its ID, or NONE.

## 5. Evidence
For each key claim: what are you saying, where does it come from, and what kind of claim is it? Claim types: `adjudicated_or_admitted_fact` (a court judgment, a final order, or an admission), `settled_without_admission` (a settlement where the institution admitted nothing), `my_observation` (you saw or heard it yourself), `allegation_or_estimate` (everything else).

| Claim | Source (link, record number, or "my own observation") | Claim type |
|---|---|---|
| | | |

**What exists but isn't attached.** For example, "letter dated…", "photos", "case number…". Say where each can be found.

## 6. Honesty
- [ ] Made in good faith.
- [ ] Public sources and my own observation only.
- [ ] Roles, not names.
- [ ] Facts kept separate from allegations.

## 7. About you (optional)
- Name or stable handle:
- Contact, for follow-up:
- Relationship to the institution:
- Verification phrase used? yes / no

## 8. Resolution (filled in later by whoever reviews the report)
- Response from the institution, and its date:
- For a stop signal, the result of the independent check: did the trigger fact occur? yes / no / not checked. Date:
- Effect on the power: did the power itself change (for example paused, stopped, narrowed, changed in another way, or not changed)? Date and source:
- Outcome:
- Linked reports:
```

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
