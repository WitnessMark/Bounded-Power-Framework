---
record_type: authorization
example: true
record_id: SCBP-REG-EXAMPLE-TOWN-LIBRARY
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
  name: "[TOWN] Public Library"
  legal_entity: "[TOWN] (municipal corporation), acting through the Library Board of Trustees"
  related_entities: "[FILTER VENDOR]; [LIBRARY SYSTEM VENDOR] (catalog and circulation); [E-BOOK PLATFORM]"
  type: government
  country: "[COUNTRY]"
  region: "[STATE]"
  locality: "[TOWN]"
  official_url: NONE
adoption_status: adopted
powers:
  - power_id: P1
    short_name: "Meeting-room booking"
    category: licensing_permits_or_access
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "yes"
    findings:
      authorization: conforming
      maximum_term: conforming
      harm_thresholds: conforming
      stop_paths: conforming
      ending_plan: conforming
      remedy: conforming
      data_limits: conforming
      visibility: conforming
      floors: conforming
      evasion: conforming
  - power_id: P2
    short_name: "Borrowing suspension"
    category: licensing_permits_or_access
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "yes"
    findings:
      authorization: conforming
      maximum_term: conforming
      harm_thresholds: conforming
      stop_paths: conforming
      ending_plan: conforming
      remedy: conforming
      data_limits: conforming
      visibility: conforming
      floors: conforming
      evasion: conforming
  - power_id: P3
    short_name: "Internet filtering"
    category: information_control_or_visibility
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: conforming
      maximum_term: conforming
      harm_thresholds: conforming
      stop_paths: conforming
      ending_plan: conforming
      remedy: conforming
      data_limits: conforming
      visibility: conforming
      floors: conforming
      evasion: conforming
  - power_id: P4
    short_name: "Borrowing and patron records"
    category: data_collection_or_records
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: conforming
      maximum_term: conforming
      harm_thresholds: conforming
      stop_paths: conforming
      ending_plan: conforming
      remedy: conforming
      data_limits: conforming
      visibility: conforming
      floors: conforming
      evasion: not_demonstrated
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

> **Structural record.** Based on public sources and/or the preparer's own observation. People are referred to by role or title. This record describes structure, not guilt. Adjudicated or admitted facts are kept separate from allegations.

# [TOWN] Public Library — Registration (authorization record)

## PART A — The institution

A1. **What it is, in one paragraph.** A small-town public library serving about 14,000 residents [EX], with about 8,000 active cardholders [EX]. It lends books and other items, offers public internet terminals and Wi-Fi, and lends two meeting rooms to community groups for free. The town has adopted the Core Requirements for the library, and this record authorizes its four powers under them: two as minor powers under one light authorization, and two through the full process.

A2. **Legal basis.** The [STATE] public library statute, the town charter, and policies adopted by the Library Board of Trustees. A [STATE] statute makes library records confidential [EX]. National constitutional law requires a public meeting room, once offered to groups, to be offered without regard to viewpoint. A national law ties a library internet subsidy to filtering of certain images on public terminals; the library receives about 12,000 currency units a year under it [EX].

A3. **Who controls it.** A Board of 7 [EX] trustees appointed by the town council sets policy and hires the Director. Under the town's adoption ordinance, no trustee, staff member or town officer may authorize the library's powers; authorization belongs to the bodies named for each power.

A4. **Related entities.** [FILTER VENDOR] supplies filtering software and category lists. [LIBRARY SYSTEM VENDOR] hosts the catalog and circulation records. [E-BOOK PLATFORM] lends e-books and audiobooks to cardholders through its own app. Figures belong to the library.

A5. **Adoption.** adopted, by town ordinance, which brought every existing library power under the Core Requirements within 12 months, as 7.1 requires [S1].

A6. **Powers found.**
- P1 — Meeting-room booking (minor power claimed).
- P2 — Suspension of borrowing for overdue items (minor power claimed).
- P3 — Internet filtering on public terminals and Wi-Fi (not minor: it restricts access to lawful material).
- P4 — Borrowing and patron records (not minor: exposure cannot be undone).

---

## Power P1 — Meeting-room booking

**B1. What it can do to people.** Decides which groups get the two meeting rooms and when. Bookings are free and first-come, up to 4 a month per group [EX]. Staff may refuse a booking only for a clash, capacity or safety limit stated in the room policy, and may withdraw a group's booking right for at most 30 days [EX] after damage to a room, with a written reason. The policy never looks at a group's views or subject.

**B2. Who and where.** About 120 groups a year [EX], and the people who attend their meetings.

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | One minor-power authorization for P1 and P2 by a cardholder panel of 9 chosen by lot [EX], excluding staff, trustees and anyone paid by the library; heard groups and borrowers at an open session; appeal to [COUNTY] Independent Authorization Board | conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | 4 years [EX], within the 5-year limit for minor powers [S1] | conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | Short form; two thresholds (PART E) [EX] | conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | Stop signal to [COUNTY] checking body; people's path; tested (B5) [EX] | conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | Honor bookings already made for 60 days [EX], then close bookings | conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Named external complaint route ([COUNTY] checking body) and the town's liability insurance | conforming |
| Data limits | Stated retention periods; 20-year ceiling; deletion records (2.D.12–2.D.14, 7.6) | Contact name and phone for each booking, deleted 30 days after the meeting [EX]; deletion recorded by schedule | conforming |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9) | Room policy, term, stop route and renewal body on one page at the desk and online [EX] | conforming |
| Floors | See B6 (Part II) | Viewpoint-neutral by rule; no Floor engaged (B6) | conforming |
| Evasion | Not split, outsourced, laundered, or using proxies (Part IV) | Counted with P2 for the minor spending limit (4.2) [EX] | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Stop signal by anyone, in any form, to [COUNTY] Stop-Signal Checking Body | whole_power | [COUNTY] checking body | independent | [EX] |
| 2 | Automatic stop when a threshold is crossed | whole_power | Rule of the authorization | independent | [EX] |
| 3 | People's path: 30 cardholders [EX] require early review (3.E.5) | whole_power | [COUNTY] Independent Authorization Board | independent | [EX] |

Test before start: a test signal paused new bookings within 1 hour [EX].

Statement: *Can anything stop this power as a whole?* — `yes, [paths 1–3]`.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Threshold? | not_applicable — room bookings | [EX] |
| Economic (2.B) | Essentials conditional? Escalation? | no — free, no fees or deposits [EX] | [EX] |
| Agency (2.C) | Told plainly? Leave? | yes — refusals are written, with the reason and the stop route [EX] | [EX] |
| Force (2.D.1) | Force? | not_applicable | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — checking body and lot panel [EX] | [EX] |
| Expression (2.D.9) | Restricts lawful expression or assembly? News reporting or petitioning? Approval before publication? | no — content and viewpoint are never criteria; a refusal based on them would be a Floor finding and end minor status | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? | no — first-come; the panel reviews refusals yearly [EX] | [EX] |
| Identification (2.D.11) | Compelled identification? | no — one contact name per booking, no ID [EX] | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — no search; one contact name per booking [EX] | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | no — withdrawing a group's booking right bars no one from the building [EX] | [EX] |

**B7. Data.** One contact name and phone per booking; deleted 30 days after the meeting [EX].

**B8. Dependencies and evasion.** None.

**B9. Harms seen.** None recorded.

**B10. Decision inputs and oversight.** Calendar availability and the published policy. The lot panel reviews refusals.

---

## Power P2 — Borrowing suspension

**B1. What it can do to people.** When an item is 30 days overdue [EX], the cardholder cannot borrow more physical items until it is returned. The suspension ends on return, or automatically after 30 days [EX], whichever comes first, and the same items cannot trigger a second suspension [EX]. The library charges no overdue fines. A lost item carries a replacement charge that never grows, is cancelled if the item comes back, and is never sent to collections or reported to anyone [EX]. A suspension never blocks in-library reading, internet terminals, e-books, meeting rooms or programs.

**B2. Who and where.** About 300 suspensions a year [EX] among about 8,000 cardholders [EX].

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body (3.A.1, 3.A.2) | Covered by the single minor-power authorization with P1 [EX] | conforming |
| Maximum term | Set expiry (3.E.1, 7.2) | 4 years [EX] | conforming |
| Harm thresholds | Published, measurable (3.A.5) | Short form; one threshold (PART E) [EX] | conforming |
| Stop paths | Tested; one held outside (3.A.7, 3.C.1) | Same as P1; tested [EX] | conforming |
| Ending plan | Documented (3.A.9) | Lift all suspensions on the day the power ends [EX] | conforming |
| Remedy | Independent, funded (3.A.10) | Named external complaint route; town insurance | conforming |
| Data limits | Retention stated (2.D.12–2.D.14) | Suspension flag deleted when it ends [EX] | conforming |
| Visibility | Five facts knowable (3.B.9) | Printed on every overdue notice [EX] | conforming |
| Floors | See B6 | No escalation; no essential access blocked (B6) | conforming |
| Evasion | Part IV | No collection agency or credit reporting [EX]; counted with P1 (4.2) | conforming |

**B5. Stop paths that actually exist.** P1's paths 1–3 (stop signal, automatic stop, people's path) cover P2 under the same authorization, held by the same independent bodies, and were tested together [EX].

Statement: *Can anything stop this power as a whole?* — `yes, [P1 paths 1–3]`.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Threshold? | not_applicable | [EX] |
| Economic (2.B) | Escalation? Path out? | no escalation — no fines; replacement charge fixed and cancelled on return [EX] (2.B.2) | [EX] |
| Agency (2.C) | Told plainly? | yes — every notice says what is blocked, what is not, and when it ends [EX] | [EX] |
| Force (2.D.1) | Force? | not_applicable | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — checking body [EX] | [EX] |
| Expression (2.D.9) | Restricts lawful expression? News reporting or petitioning? Approval before publication? | no — reading, internet and e-books stay open during a suspension [EX] | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? | UNKNOWN until the first yearly review by neighborhood [EX]; no disparity flagged | [EX] |
| Identification (2.D.11) | Compelled identification? | not_applicable | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — nothing is seized; a replacement charge is cancelled if the item comes back [EX] | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | no — a suspension never blocks entry, reading or programs [EX] | [EX] |

**B7. Data.** A suspension flag on the card record, deleted when it ends [EX]. The overdue link itself is part of P4.

**B8. Dependencies and evasion.** None.

**B9. Harms seen.** None recorded.

**B10. Decision inputs and oversight.** Days overdue only. The lot panel reviews counts yearly [EX].

---

## Power P3 — Internet filtering

**B1. What it can do to people.** Software from [FILTER VENDOR] blocks some web pages on the 20 public terminals [EX] and the library Wi-Fi. As authorized, it blocks only the categories of images the national subsidy law requires, using a list the library reviews; the vendor's other categories are switched off [EX]. Adults can turn the filter off for their own session at any time, with no reason asked and no record of who did [EX]. On sessions marked for patrons under 17 [EX], a blocked page shows a button that sends an unblock request to staff, who must decide within 15 minutes [EX] and may refuse only if the page falls in a required category. No category filter is exact, so some lawful pages are still blocked by mistake. That residual blocking of lawful material is what this power does to people.

**B2. Who and where.** About 45,000 terminal and Wi-Fi sessions a year [EX]. About 18% of cardholders have no home internet [EX] and depend on library access. Young people are the group most affected, since adults can switch the filter off.

**B3. Authority basis.** `direct`. The library controls what can be seen on its own terminals and network.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body, affected people heard, public record (3.A.1, 3.A.2) | The lot panel refused minor status (PART E). [COUNTY] Independent Authorization Board then authorized a narrowed version after a public hearing with young patrons, parents and teachers [EX] | conforming |
| Maximum term | Set expiry within 7.2 (3.E.1, 7.2) | 2 years, as a first authorization of a non-minor power [S1] | conforming |
| Harm thresholds | Published, measurable, independent (3.A.5) | Four thresholds, counted by an independent reviewer from samples (PART E) [EX] | conforming |
| Stop paths | Tested; one held outside (3.A.7, 3.C.1) | Signal, automatic stop, people's path; switch-off rehearsed (B5) [EX] | conforming |
| Ending plan | Documented (3.A.9) | Switch off on the day the power ends; accept loss of the subsidy; vendor contract ends without penalty [EX] | conforming |
| Remedy | Independent, funded (3.A.10) | Complaints to [COUNTY] independent reviewer, funded under a town agreement of 3,000 currency units a year [EX]; town insurance | conforming |
| Data limits | Retention stated; deletion recorded (2.D.12–2.D.14, 7.6) | Block logs hold no user identity and are kept 30 days for sampling [EX]; vendor contractually barred from keeping or selling logs, with independent audit right [EX] | conforming |
| Visibility | Five facts knowable (3.B.9) | Block page states why, how to override or request, term, and stop route [EX] | conforming |
| Floors | See B6 | Filtering limited to the required categories is a narrow, published, viewpoint-neutral rule tied to the purpose of a public terminal, and every block can be challenged (2.D.9). Mistaken blocks fall outside that permission; they are measured (T3-1, T3-4) and reviewed weekly for young patrons (B6) | conforming |
| Evasion | Part IV | Vendor treated as part of the power (4.5); filtering counted as one power across terminals and Wi-Fi (4.2) [EX] | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Stop signal by anyone, including a young patron, at the desk, by phone or through the block page | whole_power | [COUNTY] Stop-Signal Checking Body | independent | [EX] |
| 2 | Automatic stop when a threshold in PART E is crossed | whole_power | Rule of the authorization, counted by the independent reviewer | independent | [EX] |
| 3 | People's path: 30 people subject to the power [EX] require early review (3.E.5) | whole_power | [COUNTY] Independent Authorization Board | independent | [EX] |

An adult switching the filter off for their own session is self-help, not a stop path, so it is not listed. Test and rehearsal before start: a test signal switched filtering off across all terminals and Wi-Fi within 30 minutes [EX]; the reviewer's first sample ran on the test system.

Statement: *Can anything stop this power as a whole?* — `yes, [paths 1–3]`.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Threshold? | not_applicable | [EX] |
| Economic (2.B) | Essentials conditional? | no — but for patrons without home internet the library is the only access [EX] | [EX] |
| Agency (2.C) | Told plainly? Report without forms? | yes — every block page explains and offers the override or request [EX] | [EX] |
| Force (2.D.1) | Force? | not_applicable | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — the independent reviewer hears complaints about wrong blocks [EX] | [EX] |
| Expression (2.D.9) | Restricts lawful expression beyond a narrow, published, viewpoint-neutral rule tied to the space's purpose that can be challenged? News reporting or petitioning? Approval before publication? | no, within the measured limits — the rule blocks only the categories of images the subsidy law requires, is published on every block page, applies by category without regard to viewpoint, and every block can be challenged through the unblock request and the independent reviewer [EX]. No category filter is exact: blocks of lawful pages outside the required categories are not covered by the rule, so they are counted by T3-1 and T3-4 and corrected. Adults can remove the filter at once; young patrons must ask, a 2.C.2 burden reduced by the weekly staff review below [EX] | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? Reviewed? | Filters often block health and sexuality pages more than others; threshold T3-4 measures this [EX] | [EX] |
| Identification (2.D.11) | Compelled identification? | no — no record links a person to a block, override or request [EX] | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | not_applicable — the filter keeps no record linking a person to a page [EX] | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

The authorizing body logged the 2.D.9 question for independent interpretation; rule 2.D.9 itself answers it (see the teaching notes). The measure the body adopted meanwhile stays as a condition, because it lifts the burden of asking from young patrons (2.C.2): staff review every block on young patrons' sessions each week and unblock wrong ones without waiting for a request [EX]. If the weekly review lapses, or T3-1 or T3-4 is crossed, the operation stops or goes to review under PART E.

**B7. Data.** Block logs: page address, time, terminal number; no card number or name [EX]. Kept 30 days [EX] for sampling, then deleted with a deletion record. Wi-Fi uses no login [EX].

**B8. Dependencies and evasion.** [FILTER VENDOR] is part of the power (4.5); its contract runs one year, ends without penalty, and passes to any successor (3.A.8) [EX]. The library proposed splitting filtering into children's terminals, adult terminals and Wi-Fi, each small enough to be minor; the lot panel treated them as one function (4.2).

**B9. Harms seen.** None recorded under the new authorization. Before adoption, staff logged complaints about blocked health pages [EX] — the reason for T3-4.

**B10. Decision inputs and oversight.** The vendor's classifier, limited to the required categories, plus the library's reviewed list. The vendor's classification method is a trade secret, so the independent reviewer evaluates it by sampling outcomes, which 5.1 allows when it still permits meaningful evaluation [EX].

---

## Power P4 — Borrowing and patron records

**B1. What it can do to people.** Keeps a record for each cardholder (name, address, date of birth, card number) and a link between the cardholder and each item they currently have out. The link is deleted when the item is returned [EX], unless a replacement charge is open. A cardholder may choose to keep a reading history [EX]. Staff disclose records only under a court order, as [STATE] law requires [EX].

**B2. Who and where.** About 8,000 active cardholders [EX] and about 3,000 inactive records [EX].

**B3. Authority basis.** `direct`.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Independent body (3.A.1, 3.A.2) | [COUNTY] Independent Authorization Board, after a public hearing [EX] | conforming |
| Maximum term | Set expiry (3.E.1, 7.2) | 2 years [S1] | conforming |
| Harm thresholds | Published, measurable (3.A.5) | Three thresholds including the data-exposure size (PART E) [EX] | conforming |
| Stop paths | Tested; one held outside (3.A.7, 3.C.1) | Signal, automatic stop, people's path; rehearsed (B5) [EX] | conforming |
| Ending plan | Documented (3.A.9) | Offer each cardholder a copy, then delete, with a deletion record [EX] | conforming |
| Remedy | Independent, funded (3.A.10) | Independent reviewer complaint route and data-exposure insurance of 50,000 currency units [EX] | conforming |
| Data limits | Retention stated; deletion recorded (2.D.12–2.D.14, 7.6) | Item link deleted on return [EX]; registration deleted 3 years after last use [EX]; vendor backups purged within 14 days, confirmed by audit [EX] | conforming |
| Visibility | Five facts knowable (3.B.9) | Privacy notice at sign-up and online; any cardholder can see their own record [EX] | conforming |
| Floors | See B6 | No Floor crossed (B6) | conforming |
| Evasion | Part IV | [E-BOOK PLATFORM] collects its own reading data under its own terms; not yet shown to meet P4's limits (B8) | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop | Held by (role) | Holder independent? | Source |
|---|---|---|---|---|---|
| 1 | Stop signal to [COUNTY] checking body | whole_power | [COUNTY] checking body | independent | [EX] |
| 2 | Automatic stop on an exposure at or above the size in PART E (3.C.2) | whole_power | Rule of the authorization | independent | [EX] |
| 3 | People's path (3.E.5) | whole_power | [COUNTY] Independent Authorization Board | independent | [EX] |

Rehearsal: a full export-and-delete of the test database, observed by the checking body, took 4 hours [EX].

Statement: *Can anything stop this power as a whole?* — `yes, [paths 1–3]`.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Threshold? | not_applicable | [EX] |
| Economic (2.B) | Escalation? | not_applicable — records only | [EX] |
| Agency (2.C) | Told plainly? Leave? | yes — notice at sign-up; a cardholder can close the card and have the record deleted within 7 days [EX] | [EX] |
| Force (2.D.1) | Force? | not_applicable | [EX] |
| Confinement (2.D.3) | Only on the four permitted grounds (a)–(d)? | not_applicable — no confinement | [EX] |
| Emergency medical care (2.D.2) | Treatment without consent? | not_applicable — no medical care | [EX] |
| Due process (2.D.5) | Independent challenge? If liberty is at stake: free lawyer, silence protected, public and prompt hearing? | yes — court order needed for any disclosure [EX] | [EX] |
| Expression (2.D.9) | Restricts expression? News reporting or petitioning? Approval before publication? | no — keeping no reading history protects it [EX] | [EX] |
| Equal treatment (2.D.10) | Unequal burdens? | no — the same record for everyone [EX] | [EX] |
| Identification (2.D.11) | Compelled identification? | no — proof of address is needed for a card [EX], but in-library reading and internet need no card | [EX] |
| Search and seizure (2.D.15) | Search or seizure only on individualized cause, with prior judicial approval except in an emergency? Property returned? | yes — staff disclose a patron's records only under a court order, as [STATE] law requires [EX], and borrowing links deleted on return cannot be searched at all [EX] | [EX] |
| Movement (2.D.16) | Restricts where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** As in B1 and B4. No biometrics. Accountability records (complaints and stop signals about the library) go to the [COUNTY] independent custodian for 10 years [S1].

**B8. Dependencies and evasion.** [LIBRARY SYSTEM VENDOR] hosts records under a contract with an independent audit right [EX]. [E-BOOK PLATFORM] records what cardholders read in its app, on its own terms. Data it collects through the library's service counts as part of this power (4.4, 4.5). The vendor has not agreed to P4's limits [EX]; the authorizing body set a condition that, within 6 months [EX], either the contract conforms or e-book lending pauses.

**B9. Harms seen.** None recorded.

**B10. Decision inputs and oversight.** No decisions are made from P4 except due dates and P2's overdue trigger. The independent reviewer audits access logs twice a year [EX].

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures cited (institutional figures in this example are illustrative [EX]) | BPF: Core Requirements v1 | 2.D.10, 2.D.14, 3.A.4, 4.2, 7.1, 7.2 | | yes |
| S2 | data_point | SCBP-03 Operations Manual, Stage 1 (structure of PART E) | BPF: 01-Framework/SCBP-03-Operations-Manual.md | Steps 1.1–1.11 | | yes |

---

## PART D — Honesty assertions

- [x] Every number has a source tag (illustrative figures are tagged [EX]).
- [x] Nothing was invented as fact. Open items are written as UNKNOWN or compliance not demonstrated.
- [x] Public sources and first-hand observation only. Nothing private, leaked, or speculative.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] This is a worked example made in good faith, as a structural description, not an accusation.

Preparer: BPF examples working group (worked example).

---

## PART E — Authorization records only

The structure follows SCBP-03 Stage 1, Steps 1.1–1.11 [S2]. Description, limits, stop paths and tests, ending plan, remedy and data retention for each power are as recorded in its B1, B4, B5 and B7; this part adds what Part B does not hold. All figures are illustrative [EX] unless tagged [S1].

**P1 and P2 — one minor-power authorization (Core 3.A.4)**

- **Minor-power claims (1.2).** The library bears the burden of showing each condition; both claims are open to challenge.

  | 3.A.4 condition | P1 Meeting rooms | P2 Borrowing suspension |
  |---|---|---|
  | No force or confinement | None [EX] | None [EX] |
  | No effect lasts beyond 30 days or resists ordinary reversal | One booking; a booking ban of at most 30 days [EX] | Ends on return or after 30 days [EX]; no repeat for the same items; no fines |
  | Low-cost substitute, or only allocates a voluntary benefit | Rooms are a benefit the library chooses to offer [EX] | Borrowing is a benefit the library chooses to offer; reading, internet and e-books stay open [EX] |
  | Spending below the common limit, counted together (4.2) | P1 and P2 together about 21,000 currency units a year in staff time [EX], below the limit of 150,000 currency units [EX] set for all institutions by the [COUNTY] process | same |
  | No confirmed stop, Floor finding, or successful petition | None [EX] | None [EX] |

- **Harm assessment (1.4).** Short form. P1: communicative and agency (a group denied a room). P2: agency and economic (loss of borrowing; replacement charge). Other categories judged not applicable, with reasons. Resource caps and rehearsal do not apply to minor powers; deletion is recorded by schedule.
- **Thresholds.**
  - T1-1. Condition: any confirmed refusal of a room for content or viewpoint. Data source: complaints to the checking body and its yearly review of all written refusals. Detection: review. Verification: checking body. Window: each case; any 12 months. Trigger: automatic stop of P1.
  - T1-2. Condition: refusals for any reason exceed 10% of requests [EX]. Data source: the booking calendar export sent monthly to the checking body. Detection and verification: checking body count. Window: rolling 90 days [EX]. Trigger: automatic stop and review.
  - T2-1. Condition: any suspension lasting over 30 days [S1], or any suspension that blocks anything other than physical borrowing. Data source: circulation export to the checking body. Detection and verification: checking body. Window: monthly. Trigger: automatic stop of P2, and loss of minor status.
- **Term and decision.** Term 4 years [EX]. The lot-chosen panel of 9 cardholders [EX] heard groups and borrowers, found P1 and P2 minor, and set the thresholds above. It refused minor status for P3 (below).

**P3 — Internet filtering**

- **Why P3 is not minor (1.2).** The library first proposed P3 as minor. The lot panel refused, with these findings:
  - It restricts access to lawful material. Every category filter blocks some lawful pages. That is a restriction touching 2.D.9, not an allocation of a benefit: it limits what people may read within a service the library chose to offer.
  - The substitute condition fails. For the patrons with no home internet [EX], there is no low-cost substitute.
  - Effects can resist ordinary reversal: health information or a job notice not found in time cannot be found later.
  - Anti-slicing (4.2): the proposal to split filtering into children's terminals, adult terminals and Wi-Fi, each under the limits, was refused; they serve one function and are one power.
- **Resource caps (3.B.5).** Software spending at most 4,000 currency units a year [EX]; no new categories without re-entry.
- **Harm assessment (1.4).** Full form, all nine categories. Communicative and agency: lawful pages blocked, mostly for young patrons. Informational: block logs. Psychological: embarrassment at asking staff to unblock — the reason no requester identity is kept. Non-participant: none found. Ecological and generational: not applicable, with reasons.
- **Thresholds.**
  - T3-1 (wrongful blocks). Condition: in a monthly random sample of 200 blocks [EX], more than 2% [EX] are lawful pages outside the required categories. Data source: block log. Detection: sample drawn and judged by the [COUNTY] independent reviewer, a librarian from another county [EX]. Verification: second reviewer on disputed items. Window: rolling 90 days [EX]. Trigger: automatic stop of filtering.
  - T3-2 (slow unblocking). Condition: more than 5% [EX] of young patrons' unblock requests not decided within 15 minutes [EX]. Data source: request timestamps sent to the reviewer. Window: rolling 30 days [EX]. Trigger: automatic stop.
  - T3-3 (identity). Condition: any record linking a person to a block, override or request. Data source: reviewer's quarterly audit of systems and vendor. Window: each case. Trigger: automatic stop.
  - T3-4 (unequal blocking, 2.D.10 and 4.7). Condition: the wrongful-block rate for health, sexuality or minority-community pages exceeds twice the overall rate [EX]. Data source and detection: reviewer's tagged sample. Window: rolling 90 days [EX]. Trigger: independent review within 90 days [S1], then correction or pause.
- **Slow-accumulation indicators (3.A.6).** Number of blocked pages per session; share of young patrons' sessions with any block; requests per block (a fall can mean people have stopped asking).
- **Ending plan and long obligations (3.A.9, 3.A.8).** Switch off; end the vendor contract; delete logs with a deletion record; notify the subsidy program. Losing the subsidy is an accepted cost of stopping (3.C.4). The subsidy agreement is yearly [EX] and contains no term that restricts stopping.
- **Term and decision.** Term 2 years [S1]. [COUNTY] Independent Authorization Board heard young patrons, parents and teachers; narrowed the proposal to the required categories; added the adult switch-off and the 15-minute rule [EX]; and logged the 2.D.9 and 2.C.2 question for independent interpretation, applying the narrower reading meanwhile. Rule 2.D.9 itself answers the expression question; the weekly review is kept as a condition for 2.C.2 (B6).

**P4 — Borrowing and patron records**

- **Why P4 is not minor.** Registration records are kept longer than 30 days [S1], and an exposure of what someone reads cannot be undone.
- **Resource caps and harm assessment.** No new data fields without re-entry; staff access by role only [EX]. Full form; main harms informational and communicative (exposure of reading); others judged not applicable, with reasons.
- **Thresholds.**
  - T4-1 (data-exposure size, 3.C.2). Condition: any unauthorized exposure of any item link, or of registration data of 10 or more people [EX]. Data source: vendor and library access logs; reports. Detection and verification: independent reviewer. Window: each event; a repeat within 12 months is a stop condition in any case. Trigger: automatic stop and notice to those affected.
  - T4-2. Condition: any disclosure without court order. Data source: disclosure log sent to the reviewer. Window: each event. Trigger: automatic stop.
  - T4-3. Condition: any item link found after return (other than open replacement charges). Data source: reviewer's quarterly database sample. Window: quarterly. Trigger: automatic stop.
- **Financial assurance and long obligations.** Data-exposure insurance of 50,000 currency units [EX], verified independently and payable after any stop or ending. [LIBRARY SYSTEM VENDOR] contract, three years [EX], individually approved, with full data export and annual termination without penalty [EX] (3.A.8).
- **Term and decision.** Term 2 years [S1]. [COUNTY] Independent Authorization Board authorized P4 and set the e-book vendor condition in B8.

Commitments:
- [x] We will publish and keep current the ledger, surface map, threshold registry, failure record, stop-signal record, and deletion records (7.4–7.6).
- [x] We will not penalize anyone for a stop signal, and will never edit the stop-signal record (3.C.6, 7.5).
- [x] We will not interpret our own scope; interpretations go to the public log and independent review (Interpretation, 7.3).
- [x] We accept automatic stops, the pause-then-check process, and re-entry as the only way to restart (3.C.2, 3.C.3).

---

## Teaching notes (non-binding)

- Light process for small powers: one lot-chosen panel authorizes both minor powers in one decision, with short-form harm assessments and 4-year terms [EX] (3.A.4, 7.2).
- Design keeps a power minor. P2 blocks only physical borrowing, ends within 30 days [S1] and charges no fines; if it blocked internet access or grew a debt, it would fail 3.A.4 and touch 2.B.2.
- P3 shows why restricting expression is not minor. Filtering limits what people may read within the service, has no low-cost substitute for patrons without home internet, and its effects can resist reversal (3.A.4, 2.D.9). Anti-slicing: three small filtering pieces are still one power, and P1 and P2 spending is counted together (4.2).
- The burden-of-self-advocacy rule (2.C.2) is where the residual concern sits: adults can switch the filter off, but young patrons must ask. The weekly staff review that unblocks wrong blocks without a request is what keeps that burden off them (2.C.2, 1.5). An adult's switch-off is self-help, not a stop path.
- Rule 2.D.9: a narrow, published rule tied to the purpose of a space is permitted if applied without regard to viewpoint and open to challenge. P3's filter meets each condition because it is limited to the required categories, explained on every block page, applied by category, and every block can be challenged. P3's Floors row is therefore conforming. The permission covers the rule, not the filter's mistakes; mistaken blocks of lawful pages still need thresholds (T3-1, T3-4). P3 is still not minor: a permitted restriction can still be hard to reverse and have no substitute (3.A.4).
- A vendor that collects data through the institution's service is part of the power (4.4, 4.5). The e-book platform leaves P4's evasion row at compliance not demonstrated, with a deadline.
- Accepting the loss of a subsidy is part of a real ending plan; stopping takes precedence over keeping funding (3.A.9, 3.C.4).
- A trade-secret classifier can still be evaluated by independent sampling of outcomes (5.1).
- P4 shows what 2.D.15 asks of a holder of records: patron records leave the library only on a court order stating what may be disclosed, and records that are not kept cannot be searched.
