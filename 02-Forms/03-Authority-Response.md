# Authority Response Form

*Form version 1.0.0 · 2026-10-13 · Published for independent review · Not adopted · For use with Core Requirements v1 · Vocabulary: VOCAB.yml 1.0.0*

## What this is

Use this form if your institution is described in a registration record and you want to **correct it, add to it, disagree with it, or announce a change**.

**A response never replaces the record it answers.** It is filed beside the record. Readers always see the original record and every response together, so no one has to dig through history to find what was first said. This rule, *no silent replacement*, protects everyone: the people who made the record, the institution responding, and the public.

| Response type | Use it when… |
|---|---|
| `correction` | A fact in the record is wrong. Show the evidence. |
| `added_information` | The record says UNKNOWN or NONE EXISTS, and you can show what exists. |
| `disagreement` | You disagree with a finding or a classification, such as whether something counts as authority. |
| `adoption_notice` | Your institution has adopted the Core Requirements, or has changed something the record describes, such as adding a stop path or an expiry date. |

**What happens next:**
- The person who made the record may accept a correction by issuing a **new version** of their record. Every new version must quote, word for word, everything it changed or removed (see "Versions" below).
- If they don't accept it, the response stays beside the record, and readers can judge for themselves.
- A response doesn't change any finding by itself.

## Template

```
---
response_id: SCBP-RSP-{RECORD-SUFFIX}-{YYYY-MM-DD}     # add -A, -B for more than one on the same day
response_to: {record_id: SCBP-REG-NNNN-SUFFIX, record_version: 1}   # the exact record and version you are answering
response_type: correction            # correction | added_information | disagreement | adoption_notice
form: {name: authority-response, version: 1.0.0, date: 2026-10-13}
core_requirements: {version: v1, date: 2026-10-13}
vocab_version: 1.0.0
institution_name: ""                 # the institution described in the record
responder_role: ""                   # a job title is enough, for example "General Counsel"; no personal name needed
authorized_by_institution: yes       # yes | no | UNKNOWN: is this an official response of the institution?
filed_date: YYYY-MM-DD
---

> **Authority response.** Filed beside record [record_id] version [n]. It does not replace or change that record.

# Response — [Institution] — to [record_id] v[n]

## 1. Summary
In plain words, what are you correcting, adding, disputing, or announcing?

## 2. Point by point

| # | The record says (quote it exactly, with its section, such as P1 B4) | Your response | Evidence [S#] |
|---|---|---|---|
| 1 | | | |

## 3. Changes you have made, if any
For example, you published thresholds, added an independent stop path, set an expiry date, or adopted the Core Requirements. Give dates and evidence. [S#]

## 4. Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it | Quote | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | | | | | | |

## 5. Assertions
- [ ] This response is accurate to the best of our knowledge.
- [ ] Every number has a source.
- [ ] People are referred to by role or title.
```

---

## Versions: how a record changes without anything disappearing

- **Nothing is overwritten.** Version 1 stays at its own file name. A new version is a new file: `SCBP-REG-NNNN-SUFFIX-v2.md`, with `record_version: 2` and `supersedes: {record_id, record_version: 1}`.
- **Every new version must include a section headed `## What changed from version N`.** It lists each change with:
  - the old text, quoted exactly;
  - the new text;
  - the reason, such as a response it accepts, a new source, or an error found.

  Removed text is quoted too, so a reader of the new version sees what used to be there.
- **Only the original preparer issues new versions.** An institution answers with a response instead. If an institution files its own record, for example as an adopting authority, that is a separate record. It sits beside the outside record and never supersedes it.
- **Displays show all versions and responses together.** The newest version is shown first, with links to every earlier version and every response, and a one-line note of what changed.
