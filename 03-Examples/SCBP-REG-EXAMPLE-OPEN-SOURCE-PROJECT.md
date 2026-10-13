---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-OPEN-SOURCE-PROJECT
record_version: 1
supersedes: NONE
form: {name: registration, version: 1.0.0, date: 2026-10-13}
core_requirements: {version: v1, date: 2026-10-13}
bundle: NONE
vocab_version: 1.0.0
prepared_by: person
ai_tool: NONE
prepared_date: 2026-10-13
sources_checked_date: 2026-10-13
institution:
  name: "[PROJECT] Open-Source Project"
  legal_entity: "[PROJECT] Foundation ([COUNTRY] nonprofit corporation)"
  related_entities: "[CODE HOSTING SERVICE]; [PACKAGE REGISTRY]; corporate sponsors (unnamed)"
  type: nonprofit
  country: "[COUNTRY] (place of incorporation only; the project has no territory)"
  region: NONE
  locality: NONE
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Merge, release and licence decisions"
    category: rules_standards_or_prices
    authority_basis: indirect_a_operationalized
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: conforming
      remedy: not_conforming
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_applicable
      evasion: not_demonstrated
  - power_id: P2
    short_name: "Code of Conduct bans"
    category: licensing_permits_or_access
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: not_conforming
      harm_thresholds: not_conforming
      stop_paths: not_conforming
      ending_plan: not_conforming
      remedy: not_conforming
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_conforming
      evasion: not_demonstrated
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

> **Structural record.** Based on public sources and/or the preparer's own observation. People are referred to by role or title. This record describes structure, not guilt. Adjudicated or admitted facts are kept separate from allegations.

# [PROJECT] Open-Source Project — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** A widely used open-source software library, maintained by volunteers and a few sponsored developers and held by a small nonprofit foundation. Anyone may read, use, change and redistribute the code under its open-source licence. A technical steering committee and about 80 maintainers [EX] decide what code is accepted, what each release contains, which features are removed, and under what licence future versions are published. A conduct committee enforces the project's Code of Conduct in its own spaces: the code repository, issue tracker, mailing lists and chat. The project has no territory; its contributors and users are spread across many countries.

A2. **Legal basis.** The foundation's articles and bylaws; the project charter; the Code of Conduct; and the open-source licence, which grants every recipient the right to copy, change and redistribute each released version, permanently. Contributors sign a contributor licence agreement that lets the foundation publish their contributions under a different licence in future [EX].

A3. **Who controls it.** A technical steering committee of 7 [EX], elected by the maintainers for two-year terms [EX]. A foundation board of 5 [EX]: three elected by maintainers and two appointed by the largest sponsors [EX]. A conduct committee of 4 [EX] appointed by the steering committee.

A4. **Related entities.** Code is hosted on [CODE HOSTING SERVICE] and published through [PACKAGE REGISTRY]; both apply their own terms of service. The largest sponsor provides about 40% of foundation funding [EX] and employs about a fifth of active maintainers [EX]. Figures belong to the project unless stated.

A5. **Adoption.** not_adopted. Findings are diagnostic only [S1].

A6. **Powers found.**
- P1 — Decisions on what code is merged and released, what is deprecated, and the licence of future versions.
- P2 — Code of Conduct bans from project spaces.
- Not recorded: grant and removal of maintainer rights (licensing_permits_or_access); trademark control over the project name (rules_standards_or_prices); security-disclosure timing (information_control_or_visibility).

---

## Power P1 — Merge, release and licence decisions

**B1. What it can do to people.** The project decides what goes into each release, including breaking changes and removals, and can publish future versions under a different licence. It cannot order anyone to upgrade, and it cannot withdraw the licence on versions already released. Security fixes are published only for the two most recent major versions [EX], so an organization that stays on an older version stops receiving them.

**B2. Who and where.** An estimated 200,000 organizations [EX] build the library into their own software, and far more end users rely on that software without knowing the library is there (non-participants). Download counts suggest tens of millions of installs a month [EX], but the true number of users is UNKNOWN.

**B3. Authority basis.** `indirect_a_operationalized`. The project gives no orders. But dependent software is built so it cannot run without the library, and many build systems pull new releases automatically within a version range [EX]. Refusing a change means freezing on an old version without security fixes or maintaining one's own copy — more than a minimal burden, so a material cost. Evidence strength on the Causation Ladder: tier 3 (data dependency: the dependent systems cannot function without the library's code), which meets the tier 5-or-stronger requirement. The record does not find `indirect_b`: the project's defaults steer technical choices, but people can and do switch libraries.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The charter grants the power; the steering committee is elected by maintainers, not by an independent body or by dependents [EX] | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | Committee seats expire every two years [EX], but the power itself has no end date: NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS — a deprecation policy promises 12 months' notice before removals [EX], but no threshold triggers a stop | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Only the maintainers' vote, which is not independent (B5) [EX]. The licence lets anyone fork the code without permission, and two community forks have replaced the project in parts of the ecosystem before [EX], but a fork is a replacement path, not a stop path | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | Published archival procedure: final release, read-only repository, foundation keeps the name [EX]; the licence keeps every version usable after the end | conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS — the licence disclaims all warranty and liability | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; deletion records (2.D.12–2.D.14, 7.6) | Contributor names and email addresses stay in the public code history permanently [EX]; no retention period | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9) | Decisions, votes, charter and licence are all public in the repository and mailing-list archives [EX] | conforming |
| Floors | See B6 (Part II) | No Floor engaged by this power (B6) | not applicable |
| Evasion | Not split, outsourced, laundered, or using proxies (Part IV) | UNKNOWN whether sponsor employment shapes technical decisions; the contributor licence agreement concentrates relicensing control in the foundation [EX] | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Maintainers vote out the steering committee | one_practice | Maintainers | not_independent — maintainers are part of the project | [EX] |

A dependent can also pin an older version. That is declining a change, not stopping it, so it is not listed.

Replacement path: anyone may fork the code under the licence and continue it under new governance, with no permission needed; the public repository shows about 9,000 forks [EX]. A fork does not halt the original project's next release. It ends the project's control over the code for everyone who moves, because the licence hands the whole function — not just a copy — to anyone, permanently. Under the form's definition that is replacement, not a stop, so it is not counted in the table. The project keeps its name and its place in the package registry, which is where its residual power sits.

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**. Path 1 reaches one practice and is held by the maintainers; the fork is a replacement path.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Irreversible ecological threshold? | not_applicable — software releases | [EX] |
| Economic (2.B) | Essentials conditional? Escalation? Path out? | no — no charges; path out is the fork or another library [EX] | [EX] |
| Agency (2.C) | Told plainly? Report harm without forms? Leave? | yes — release notes and deprecation notices are public; anyone can file an issue in plain words with a free account [EX] | [EX] |
| Force (2.D.1) | Force? | not_applicable | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Challenge before someone independent? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | not_applicable — no person is deprived of property or standing; each released version stays licensed | [EX] |
| Expression (2.D.9) | Restricts lawful expression? News reporting or petitioning? Approval before publication? | no | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? | not_applicable — decisions apply to code, not people | [EX] |
| Identification (2.D.11) | Compelled identification? | no — contributors may use a pseudonym [EX] | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — release decisions search and seize nothing |  |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** Public code history records each contributor's chosen name and email address, permanently [EX]. Download statistics come from [PACKAGE REGISTRY]. Whether public history counts as a historical archive exempt from propagation duties (4.6) is a separate question from the project's own retention under 2.D.12.

**B8. Dependencies and evasion.** Distribution depends on [PACKAGE REGISTRY] and [CODE HOSTING SERVICE], whose terms the project does not control. The contributor licence agreement lets the foundation relicense all contributions [EX]; with two of five board seats appointed by sponsors [EX], a licence change could be decided by a body partly controlled by commercial users. No proxy use found.

**B9. Harms seen.** Economic: a past breaking release forced dependents to spend migration effort — an illustrative pattern, not an adjudicated fact. Non-participant: end users of dependent software exposed to an unpatched flaw in an old version.

**B10. Decision inputs and oversight.** Code review by maintainers, automated tests, and steering-committee votes on contested changes. All inputs are public. Anyone can audit the history.

---

## Power P2 — Code of Conduct bans

**B1. What it can do to people.** The conduct committee can warn, suspend for a set period, or permanently ban a person from all project spaces [EX]. A ban removes the ability to file issues, comment, submit code, join meetings and keep maintainer rights. It does not remove the licence: a banned person can still use and fork the code. The Code covers conduct in project spaces and conduct elsewhere that "targets project participants" [EX].

**B2. Who and where.** About 600 people active in the last year [EX], plus anyone who posts in project spaces. The committee issued about 10 suspensions and 2 permanent bans last year [EX]. For a maintainer paid by an employer to work on the project, a ban can end that job.

**B3. Authority basis.** `direct`. The committee acts on the person itself.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body (3.A.1, 3.A.2) | The steering committee adopted the Code and appoints the conduct committee [EX] | not conforming |
| Maximum term | Set expiry (3.E.1, 7.2) | NONE EXISTS for the power; permanent bans have no review date [EX] | not conforming |
| Harm thresholds | Published, measurable (3.A.5) | NONE EXISTS | not conforming |
| Stop paths | Tested; one held outside (3.A.7, 3.C.1) | Appeal to the steering committee, which appoints the conduct committee (B5) [EX] | not conforming |
| Ending plan | Documented (3.A.9) | NONE EXISTS | not conforming |
| Remedy | Independent, funded (3.A.10) | NONE EXISTS | not conforming |
| Data limits | Retention stated (2.D.12–2.D.14) | Reports and decisions kept by the committee; retention UNKNOWN | compliance not demonstrated |
| Visibility | Five facts knowable (3.B.9) | The Code, the enforcement guide and the range of outcomes are published [EX]; a yearly summary gives counts by outcome [EX] | conforming |
| Floors | See B6 | No independent challenge; the clause on conduct elsewhere reaches beyond the project's spaces, outside what 2.D.9 permits (B6) | not conforming |
| Evasion | Part IV | UNKNOWN whether the hosting service's own moderation is used to enforce bans beyond project spaces | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Appeal to the steering committee within 14 days [EX] | one_case | Steering committee | not_independent — it appoints the conduct committee | [EX] |
| 2 | Maintainers amend the charter to change the Code or the committee | whole_power | Maintainers | not_independent | [EX] |

A fork does not stop P2: it creates a new set of spaces but does not lift a ban in this project's spaces.

Statement: *Can anything stop this power as a whole?* — `yes, [path 2] — holder not independent`. No path held outside the project reaches the whole power.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Threshold? | not_applicable | [EX] |
| Economic (2.B) | Essentials conditional? | no — but a ban can end a sponsored maintainer's paid role [EX] | [EX] |
| Agency (2.C) | Told plainly? Leave? | yes — written notice of the finding and the reasons [EX]; reporting harm needs no account or prescribed form [EX] | [EX] |
| Force (2.D.1) | Force? | not_applicable | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | no — appeal stays inside the project | [EX] |
| Expression (2.D.9) | Restricts lawful expression beyond a narrow, published, viewpoint-neutral rule tied to the space's purpose that can be challenged? News reporting or petitioning? Approval before publication? | Within project spaces: no — the Code is published, tied to the purpose of shared work spaces, addresses conduct rather than viewpoint [EX], and a decision can be appealed, though only inside the project (see Due process). Outside project spaces: yes — the clause on conduct elsewhere that "targets project participants" reaches speech outside the project [EX], with no definition of "targets", so it is neither narrow nor tied to a space | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? | UNKNOWN — the yearly summary does not break outcomes down by language or region [EX] | [EX] |
| Identification (2.D.11) | Compelled identification? | no — reporters and reported people may remain pseudonymous [EX] | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — the committee reviews reports and screenshots people submit [EX]; it searches no one's accounts or devices | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — a ban closes project spaces, not places; its reach is recorded under Expression |  |

**B7. Data.** Reports, evidence screenshots, committee notes and decisions. Retention: UNKNOWN. A suspension or ban is a sanction listing against the person, not an accountability record: it follows 2.D.12 and 2.D.6, needs a stated retention period, and the person may ask for its earlier deletion unless a hold applies (2.D.14). Reports about committee members' own conduct go to the steering committee, not to an independent custodian (2.D.14).

**B8. Dependencies and evasion.** Enforcement runs through tools on [CODE HOSTING SERVICE] (blocking accounts from the repository). Whether the project ever asks the hosting service to act beyond project spaces: UNKNOWN.

**B9. Harms seen.** Communicative and economic harms from bans are possible; harms from the conduct the Code addresses (harassment) are also real. No case is adjudicated in this example.

**B10. Decision inputs and oversight.** Reports, public records of conduct in project spaces, and the reported person's response. The enforcement guide is public; individual decisions are private except the outcome counts. No outside audit.

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures and definitions cited (institutional figures in this example are illustrative [EX]) | BPF: Core Requirements v1 | Definitions: Authority, Material cost, Causation Ladder; 3.B.2; 3.C.1 | | yes |

---

## PART D — Honesty assertions

- [x] Every number has a source tag (illustrative figures are tagged [EX]).
- [x] Nothing was invented as fact. Where something is unknown in this kind of project, it is written UNKNOWN; where it is typically absent, NONE EXISTS.
- [x] Public sources and first-hand observation only. Nothing private, leaked, or speculative.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] This is a worked example made in good faith, as a structural description, not an accusation.

Preparer: BPF examples working group (worked example).

---

## Teaching notes (non-binding)

- The fork is the set's model of a replacement path. The licence makes the function replaceable by anyone without permission, which serves 3.B.2. But a fork replaces rather than halts, so under the form's B5 definition it is not a whole-power stop, and the P1 stop-path row is not conforming (3.A.7, 3.C.1).
- A replacement path still matters. It limits how much a bad decision can bind dependents, and it keeps the ending plan real (3.A.9), even though it does not satisfy the stop-path rule.
- Stop paths are per power. The fork bounds P1 (the code) but does nothing for P2 (bans from project spaces), which has no external stop (3.A.1, 3.C.1).
- The basis for P1 is limb (a), not limb (b): dependents' systems cannot run without the library (Causation Ladder tier 3), and refusing a change carries a material cost (Definitions: Material cost; 4.3).
- A non-geographic institution still has an affected population; it is counted through dependents and non-participant end users (3.A.11), with UNKNOWN where the count cannot be known.
- Conforming rows are real here: everything is public (3.B.9) and the licence keeps every version usable after an ending (3.A.9).
- A licence that disclaims all liability means no remedy exists (3.A.10).
- Relicensing control concentrated by a contributor agreement, with sponsor-appointed board seats, is an evasion and capture concern to watch (3.B.6, Part IV), not yet a finding.
- Rule 2.D.9: a conduct code in a project's own spaces is permitted when it is narrow, published, tied to the space's purpose, applied without regard to viewpoint, and open to challenge. P2's in-space rules meet that test. Its clause on conduct elsewhere does not, and the appeal stays inside the project (2.D.5), so P2's Floors row stays not conforming. A ban record follows 2.D.12 and 2.D.6, not the accountability-record rule (2.D.14).
