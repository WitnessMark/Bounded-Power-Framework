> **FICTIONAL TEST FIXTURE** for the checker. Not a real institution.
> Tests: a registration whose P1 lists, in B11, a report that names P2. Checked together with that report.
> Expected error: P1 B11 lists SCBP-WR-EXWATER-XX-2026-10-02
> Check together with: TEST-GOOD-WITNESS-LINKED.md

---
record_type: example
record_id: SCBP-REG-EXAMPLE-RIVER-WATER
example: true
record_version: 1
supersedes: NONE
form: {name: registration, version: v1, date: 2026-11-05}
core_requirements: {version: v1, date: 2026-11-05}
bundle: NONE
vocab_version: v1
prepared_by: person
ai_tool: NONE
prepared_date: 2026-11-05
sources_checked_date: 2026-11-05
institution:
  name: "Example River Water Authority (fictional test)"
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
  - power_id: P2
    short_name: "Discharge permit monitoring"
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

> **WORKED EXAMPLE — not a record of any real institution.**

# Example River Water Authority — Registration

## PART A — The institution
A1. A fictional water authority used to test links between records and reports.

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
**B11. Reports about this power (optional).** SCBP-WR-EXWATER-XX-2026-10-02 (incident).

## Power P2 — Discharge permit monitoring
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

## PART C — Sources

| ID | Kind | Title | Link | Where | Quote | Verified |
|---|---|---|---|---|---|---|
| S1 | data_point | Fictional fee schedule | https://example.org/fees | table 1 | | yes |

## PART D — Honesty assertions
- [x] Every number has a source tag.
