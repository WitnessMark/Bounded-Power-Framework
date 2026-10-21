> **FICTIONAL TEST FIXTURE** for the checker. Not a real institution.
> Tests: a version 2 that claims to supersede a different record.
> Expected error: supersedes.record_id

---
record_type: observed
record_id: SCBP-REG-NNNN-EXLIB-XX
record_version: 2
supersedes: {record_id: SCBP-REG-NNNN-OTHER-XX, record_version: 1}
form: {name: registration, version: 1.0.0, date: 2026-10-21}
core_requirements: {version: v1, date: 2026-10-21}
bundle: NONE
vocab_version: 1.0.0
prepared_by: person
ai_tool: NONE
prepared_date: 2026-10-21
sources_checked_date: 2026-10-21
institution:
  name: "Example County Library (fictional)"
  legal_entity: UNKNOWN
  related_entities: NONE
  type: government
  country: "Exampleland"
  region: NONE
  locality: "Example County"
  official_url: UNKNOWN
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Library card suspension"
    category: licensing_permits_or_access
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: not_conforming
      harm_thresholds: not_demonstrated
      stop_paths: not_demonstrated
      ending_plan: not_demonstrated
      remedy: not_demonstrated
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_demonstrated
      evasion: not_applicable
---

# Example County Library — Registration

## PART A — The institution
A1. A fictional public library used to test the checker.

## Power P1 — Library card suspension
**B1. What it can do to people.** Suspends borrowing privileges when fines exceed a limit of 25 dollars [S1].
**B2. Who and where.** Card holders in the county. Number: UNKNOWN.
**B3. Authority basis.** direct.
**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | 3.A.1, 3.A.2 | NONE EXISTS | not conforming |
| Maximum term | 3.E.1, 7.2 | NONE EXISTS | not conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by | Independent? | Source |
|---|---|---|---|---|---|
| 1 | Appeal to the library board | one_case | the board | not_independent | [S1] |

Statement: *Can anything stop this power as a whole?* — UNKNOWN
**B6. Floor checklist.** UNKNOWN.
**B7. Data.** UNKNOWN.
**B8. Dependencies and evasion.** UNKNOWN.
**B9. Harms seen.** UNKNOWN.
**B10. Decision inputs and oversight.** UNKNOWN.

## What changed from version 1

- Old text, quoted exactly: "record_version: 1"
- New text: "record_version: 2"
- Reason: a fictional revision used to test the version chain.

## PART C — Sources

| ID | Kind | Title | Link | Where | Quote | Verified |
|---|---|---|---|---|---|---|
| S1 | data_point | Fictional fee schedule | https://example.org/fees | table 1 | | yes |

## PART D — Honesty assertions
- [x] Every number has a source tag.
