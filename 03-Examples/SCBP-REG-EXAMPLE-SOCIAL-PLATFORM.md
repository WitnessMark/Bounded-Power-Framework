---
record_type: observed
example: true
record_id: SCBP-REG-EXAMPLE-SOCIAL-PLATFORM
record_version: 1
supersedes: NONE
form: {name: registration, version: 1.0.0, date: 2026-10-21}
core_requirements: {version: v1, date: 2026-10-21}
bundle: NONE
vocab_version: 1.0.0
prepared_by: person
ai_tool: NONE
prepared_date: 2026-10-21
sources_checked_date: 2026-10-21
institution:
  name: "[SOCIAL PLATFORM]"
  legal_entity: "[SOCIAL PLATFORM INC.]"
  related_entities: "[CONTENT-REVIEW CONTRACTOR] (human moderators); [AGE-CHECK VENDOR] (ID and face age checks); [SOCIAL PLATFORM REGIONAL SUBSIDIARY] (operator in [REGION])"
  type: private_company
  country: "[COUNTRY]"
  region: NONE
  locality: NONE
  official_url: NONE
adoption_status: not_adopted
powers:
  - power_id: P1
    short_name: "Account suspensions and bans"
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
      visibility: not_conforming
      floors: not_conforming
      evasion: conforming
  - power_id: P2
    short_name: "Feed ranking and reach limits"
    category: information_control_or_visibility
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
      visibility: not_conforming
      floors: not_demonstrated
      evasion: conforming
  - power_id: P3
    short_name: "Age and ID verification for [STATE] users"
    category: inspection_search_or_surveillance
    authority_basis: direct
    uses_force_or_confinement: "no"
    minor_power_claimed: "no"
    findings:
      authorization: not_conforming
      maximum_term: conforming
      harm_thresholds: not_conforming
      stop_paths: not_demonstrated
      ending_plan: not_conforming
      remedy: not_demonstrated
      data_limits: not_demonstrated
      visibility: conforming
      floors: not_conforming
      evasion: not_demonstrated
---

> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.

# [SOCIAL PLATFORM] — Registration

## PART A — The institution

A1. **What it is, in one paragraph.** A private company that runs a social network where people post, follow, message and earn money from their posts. It decides who may have an account, what is removed, and how widely each post is shown. For many people it is where family news, local information, job leads and political talk happen; for creators and small businesses it is a source of income.

A2. **Legal basis.** Incorporated under [STATE] corporate law. Its powers over users come from its terms of service, a contract users accept to sign up, which the company can change on notice. A federal law shields it from most liability for users' posts and protects its moderation choices. In [REGION] a regional digital services law requires statements of reasons, an internal complaint system, access to certified out-of-court dispute bodies, yearly risk assessments and independent audits. A [STATE] age-verification law requires age checks for [STATE] users.

A3. **Who controls it.** A board elected by shareholders. Policy is set by a trust-and-safety team reporting to management.

A4. **Related entities.**
- [CONTENT-REVIEW CONTRACTOR] employs most human reviewers, about 10,000 [EX], applying the platform's policies under the platform's direction.
- [AGE-CHECK VENDOR] runs P3 checks.
- [SOCIAL PLATFORM REGIONAL SUBSIDIARY] is the legal operator in [REGION]; figures for [REGION] are its figures.

A5. **Adoption.** not_adopted.

A6. **Powers found.**
- P1 — Account suspensions and bans (licensing_permits_or_access, direct).
- P2 — Feed ranking and reach limits (information_control_or_visibility, direct).
- P3 — Age and ID verification for [STATE] users (inspection_search_or_surveillance, direct).
- Not recorded: demonetization; advertising rules; responses to government takedown requests.

---

## PART B — One section per power

## Power P1 — Account suspensions and bans

**B1. What it can do to people.** It can lock an account for hours or days, or remove it permanently, along with the person's posts, followers, messages and any income from the account. Bans can extend to new accounts the system links to the same person. Most actions are taken by automated classifiers; a minority are reviewed by a person.

**B2. Who and where.** About 100 million [EX] monthly users in [COUNTRY] and [REGION]. About 2 million [EX] accounts suspended or banned per year. Non-participants: people who lose contact with a banned person, and customers of banned small businesses.

**B3. Authority basis.** `direct`. The platform itself removes the account; no other party's decision is involved [S1].

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS. The terms of service are written and changed by the platform. | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | NONE EXISTS | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. Reported error rates come from the platform's own appeal outcomes. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | One-case paths only, mostly in [REGION]; see B5 | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | [REGION]: certified dispute bodies can order reinstatement but not compensation, and are paid per case by the platform. [COUNTRY]: terms require private arbitration. | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Banned accounts' data kept for 1 year [EX] "for safety"; deletion record UNKNOWN. A ban entry against a user is a sanction listing that follows 2.D.12 and 2.D.6, not an accountability record; how long ban entries used to link new accounts are kept is UNKNOWN, and users cannot ask for earlier deletion [EX]. Records of the platform's own decisions are kept by the platform only. | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Rules are public; [REGION] statements of reasons are published to a regulator database; that the power has no expiry and is renewed by no one is plain from the terms (failure recorded under Maximum term). But classifier features and score cut-offs are not declared (5.3). | not conforming |
| Floors | See B6 (Part II) | See B6 | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Contract reviewers act under the platform's policies and the platform answers for their decisions; no splitting or routing to avoid limits found. | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Out-of-court dispute body decision (in [REGION]) | one_case | a certified dispute body | partly_independent | [EX] |
| 2 | Regulator order under the regional digital services law | one_practice | [REGION] digital services regulator | independent | [EX] |
| 3 | Internal appeal | one_case | the platform's review team | not_independent | [EX] |
| 4 | Arbitration under the terms of service (in [COUNTRY]) | one_case | an arbitrator chosen under the platform's terms | partly_independent | [EX] |

Path 1 is partly independent: a regulator certifies the body, but the platform pays a fee per case [EX]. Path 4 is partly independent: the arbitrator is not the platform's employee, but the platform drafts the rules and pays most costs.

Statement: *Can anything stop this power as a whole?* — **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway of note | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | yes for creators and small businesses: a ban removes their income, with no path to restore it | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | partly — notices name a policy but not the post or evidence in about half [EX] of cases outside [REGION] | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 hours; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical care | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | partly — in [REGION], yes (path 1); in [COUNTRY], only arbitration | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, or assembly, beyond narrow, published, viewpoint-neutral rules tied to the space's purpose that can be challenged? News reporting or petitioning? Approval before publication? | UNKNOWN — the rules are published, but they cover a general-purpose service rather than a space with a narrow purpose; whether classifiers apply them without regard to viewpoint has not been independently reviewed; and in [COUNTRY] a ban can be challenged only through arbitration under the platform's terms [EX]. The permission in 2.D.9 is not shown to be met | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — classifiers are weaker in less common languages [EX]; a [REGION] audit noted this but no disparity review was done | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | partly — some banned users must upload ID to appeal [EX]. Verifying the identity of a person claiming back an account is a claimed entitlement under 2.D.11, permitted with the least intrusive means that works, a non-biometric way offered, and no other use. ID upload is non-biometric, but whether a less intrusive check (such as confirming the account's email) would work, and whether ID images are used for anything else, is not shown | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | no — to enforce bans, the system reads device and network identifiers from people's phones and computers to link new accounts to a banned person [EX], with no individualized cause beyond the earlier ban and no independent approval. On a permanent ban, earnings not yet paid out are withheld [EX] with no finding by anyone independent; whether they are ever returned is not shown | [EX] |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — a ban closes an online service, not a place; its effect on expression is recorded under Expression |  |

**B7. Data.** Account details, posts, device and network identifiers used to link accounts. A suspension or ban entry against a user is a sanction listing, not an accountability record: it follows 2.D.12 and 2.D.6, needs a stated retention period, and the user may ask for its earlier deletion unless a hold applies (2.D.14). The platform's records of its own decisions (policy applied, classifier or reviewer, outcome of appeal) are accountability records; they are kept only by the platform, not in independent custody.

**B8. Dependencies and evasion.** Classifiers are built in-house. [CONTENT-REVIEW CONTRACTOR] reviewers work under quotas set by the platform. Shared hash lists for certain illegal content come from a national clearinghouse [EX]; that is a legal duty, not evasion.

**B9. Harms seen.**
- communicative, economic: wrongful bans of accounts reinstated on appeal, about 30% [EX] of appealed bans in a [REGION] transparency report; admitted by the platform in that report.
- agency: account bans without a stated reason; allegation in user complaints.

**B10. Decision inputs and oversight.** Policy text is public; classifier features and score cut-offs are not (5.3). The [REGION] law requires a yearly independent audit, paid for by the platform [EX], so it is partly independent (5.1).

---

## Power P2 — Feed ranking and reach limits

**B1. What it can do to people.** It decides which posts each person sees and in what order. It can quietly reduce a post's or account's reach — removing it from recommendations and search — without removing it or telling the author. For news sources, local groups and candidates, reach on the platform decides who hears them.

**B2. Who and where.** Every user's feed: about 100 million [EX] people. Authors whose reach is cut, and readers who never see what was cut, are both affected. Non-participants include people discussed in amplified posts.

**B3. Authority basis.** `direct`. The platform directly controls the ranking, recommendation, and visibility functions of its own service. A deliberate reach restriction imposed on a particular post or account is a direct exercise of control over distribution within that service [S1].
- Wider effect on behavior: feed ranking also influences what users encounter and may affect their behavior. The platform's own experiments show that changing ranking changed what users read and posted. These are reported in its [REGION] risk assessment [EX].
- Not shown to be indirect_b: scale or measured behavioral effects alone do not establish `indirect_b_directive_control`. That classification would need a separate explanation of how the mechanism's practical effect operates as directive control rather than ordinary influence. The scenario does not supply one, so the wider behavioral effect is recorded as influence, with its classification uncertain. This does not weaken scrutiny of the platform's direct decisions.
- Not indirect_a: no outside party builds the ranking into a binding decision.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | NONE EXISTS | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | NONE EXISTS. Ranking changes weekly [EX] with no outside approval. | not conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. [REGION] risk assessments are written by the platform. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | See B5 | not conforming |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | NONE EXISTS. Authors are not told of reach limits, so they cannot challenge them. | not conforming |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Engagement history used for ranking: retention UNKNOWN | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Main ranking signals described in plain words in [REGION]; reach limits not disclosed to authors. | not conforming |
| Floors | See B6 (Part II) | See B6 | compliance not demonstrated |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Ranking is run in-house by the same entity; no splitting or vendor routing found. | conforming |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Regulator order to change a ranking practice found to create systemic risk | one_practice | [REGION] digital services regulator | independent | [EX] |
| 2 | Court-ordered temporary restriction of the whole service in [REGION], as a last resort after repeated failures | whole_power (in [REGION] only) | a [REGION] court, on the regulator's request | independent | [EX] |

A user can switch to the non-personalized chronological feed (required in [REGION]); that is self-help, not a stop path, so it is not listed. Path 2 has never been used [EX] and is not tested. It would stop every power of the platform in [REGION], not just ranking, so it is not a narrow stop (3.C.5).

Statement: *Can anything stop this power as a whole?* — `yes, [path 2]`, in [REGION] only and untested. In [COUNTRY]: **NONE EXISTS**.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway of note | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | no — but reach can be bought through paid promotion, so reach limits fall harder on those who cannot pay | [EX] |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | no for reach limits — authors are not told. Readers can choose the chronological feed in [REGION] | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 hours; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical care | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | no for reach limits | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | UNKNOWN — reach limits apply to "borderline" lawful posts, including posts by news sources [EX]; whether they fall on criticism of authority or on news reporting is not shown | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — no independent disparity review | |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | no | |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — ranking searches and seizes nothing |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

Communicative integrity (2.D.8): reach limits applied to posts reporting harm would suppress a harm signal. Not shown here; recorded for watching.

**B7. Data.** Viewing time, clicks, follows, inferred interests. Retention UNKNOWN. Deletion record UNKNOWN.

**B8. Dependencies and evasion.** Built and run in-house. Advertisers depend on the ranking; the platform depends on ad revenue, which rewards time spent. That is a structural incentive to grow reach (3.B.6), not evasion.

**B9. Harms seen.**
- communicative: reach of some kinds of posts fell after ranking changes [EX]; shown in the platform's own [REGION] risk assessment.
- psychological: harm to young users from recommended content; allegation in pending suits by state attorneys general.
- non_participant: people targeted by amplified harassment posts; allegation.

**B10. Decision inputs and oversight.** Main signals are described in general terms in [REGION]; weights and reach-limit rules are not published (5.3). Vetted researchers in [REGION] can request data under the regional law; in [COUNTRY], no outside access (5.1).

---

## Power P3 — Age and ID verification for [STATE] users

**B1. What it can do to people.** Before a [STATE] user may keep using the platform, the user must prove being an adult: by uploading a government ID, or by a face scan that estimates age. A user who fails or refuses is moved to a restricted teen account or locked out.

**B2. Who and where.** About 3 million [EX] users in [STATE]. Adults who refuse to show ID or their face lose full access. Minors are restricted.

**B3. Authority basis.** `direct`. The platform, through [AGE-CHECK VENDOR], inspects the person's ID or face itself [S1]. The [STATE] legislature requires the check; that mandate is the legislature's own power, which would need its own record.

**B4. Observed vs required.**

| Requirement | Required (Core rule) | Observed | Finding |
|---|---|---|---|
| Authorization | Authorized separately by an independent body that heard affected people, on a public record (3.A.1, 3.A.2) | The [STATE] legislature mandated the check after public hearings. The statute states no findings on harms, thresholds or stop paths. | not conforming |
| Maximum term | Expires on a set date; 2 years for force, confinement, broad-reach, or first-time powers; never over 10 (3.E.1, 7.2) | The statute's age-check section sunsets after 2 years [EX] unless re-enacted. | conforming |
| Harm thresholds | Published, measurable, set by the authorizing body, not dependent on the institution's own findings (3.A.5) | NONE EXISTS. No limit on wrongful lock-outs or data exposure. | not conforming |
| Stop paths | Tested paths, at least one held by a body the institution neither funds, appoints, nor can remove (3.A.7, 3.C.1) | A court can enjoin the statute; the [STATE] attorney general enforces it. Neither tested. | compliance not demonstrated |
| Ending plan | A documented way to end the power safely (3.A.9) | NONE EXISTS beyond the sunset date | not conforming |
| Remedy | An independent, funded way to get harm corrected and compensated (3.A.10) | Complaint to the [STATE] attorney general; private suit for a data breach under the statute. Funding UNKNOWN. | compliance not demonstrated |
| Data limits | Stated retention periods; 20-year ceiling; 10 years for biometrics; deletion records; accountability records kept independently (2.D.12–2.D.14, 7.6) | Statute requires deletion of ID images and face scans within 7 days [EX]; vendor states compliance. Deletion record and custody of complaint records UNKNOWN. | compliance not demonstrated |
| Visibility | An ordinary person can learn what it may do, when it expires, what stops it, who renews it, and whether it has grown (3.B.9). Decision inputs are declared (5.3) | Statute, sunset date, enforcing office and renewing body are public; the attorney general reports yearly counts of checks [EX]. | conforming |
| Floors | See B6 (Part II) | See B6 | not conforming |
| Evasion | Not split, outsourced, laundered through vendors or bought data, or using proxies (Part IV) | Vendor contract terms on reuse of face data: UNKNOWN | compliance not demonstrated |

**B5. Stop paths that actually exist.**

| # | Stop path | What it can stop (whole_power / one_practice / one_case) | Held by (role) | Holder independent? (independent / partly_independent / not_independent / UNKNOWN) | Source |
|---|---|---|---|---|---|
| 1 | Court injunction against the statute on free-expression grounds | whole_power | a federal court | independent | [EX] |
| 2 | Sunset of the statute | whole_power | the [STATE] legislature, by not re-enacting | independent | [EX] |
| 3 | Attorney general enforcement order on how checks are done | one_practice | [STATE] attorney general | independent | [EX] |

Statement: *Can anything stop this power as a whole?* — `yes, [paths 1–2]`. Neither has been tested. The platform could keep checking after the sunset on its own choice; that would be a new power, outside the statute.

**B6. Floor checklist.**

| Floor | Question | Answer | Source |
|---|---|---|---|
| Ecological (2.A.1) | Does it cause or accumulate toward an irreversible ecological threshold? | not_applicable — no ecological pathway | |
| Economic (2.B) | Does it make essentials conditional on compliance? Do obligations grow because people can't pay? Is there a path to pay off and get out? | no | |
| Agency (2.C) | Are people told plainly, without asking, what is being done and how to challenge it? Can they report harm without forms or proof? Can they leave? | yes — a plain notice explains the check and the appeal | [EX] |
| Force (2.D.1) | If it uses force: is force separately authorized, never aimed at pain or injury, externally stoppable while used, and independently reviewed? | not_applicable — no force | |
| Confinement (2.D.3) | If it detains or confines: only on the four permitted grounds — (a) imminent bodily threat; (b) arrest brought before a judicial officer within 48 hours; (c) a sanction after due process; (d) a brief stop on individualized suspicion? | not_applicable — no confinement | |
| Emergency medical care (2.D.2) | If it treats people without consent: only for incapacity plus imminent serious harm, with incapacity found by an independent clinician, and valid refusals honored? | not_applicable — no medical care | |
| Due process (2.D.5) | Can people challenge its actions before someone independent of it? If liberty is at stake: is a lawyer available (free if needed), is silence protected, and is the hearing public and prompt? | no — a failed check is appealed to the vendor | [EX] |
| Expression (2.D.9) | Does it punish or restrict lawful expression, belief, assembly, news reporting, or petitioning? Does it require approval before publication? | yes — adults who will not show ID lose full access to a place of lawful expression | [EX] |
| Equal treatment (2.D.10) | Do its burdens fall unequally by race, sex, religion, disability, language, or similar? Has that been reviewed? | UNKNOWN — face age estimates are less accurate for some groups [EX]; not reviewed | [EX] |
| Identification (2.D.11) | Does it compel identification, or identify people by surveillance, without individualized cause? | yes for the ID-upload route: expression is never an activity that may be conditioned on identification. The claimed-entitlement case in 2.D.11 does not cover it: the check does not confirm who is claiming an account, it conditions every [STATE] user's continued access to a place of expression on proving age, without individualized cause. The face-estimate route estimates age without naming the person; whether that is identification is UNKNOWN. | [EX] |
| Search and seizure (2.D.15) | If it searches people, homes, devices, or belongings, or seizes property: only on individualized cause, with prior approval by an independent judicial officer except in an emergency? Is property returned, and never kept permanently without a finding of responsibility? | not_applicable — the check takes a document image or face scan the user supplies; its problems are recorded under Identification and Expression |  |
| Movement (2.D.16) | Does it restrict where people may go, live, leave, or return, beyond the permitted grounds? | not_applicable — no restriction on movement |  |

**B7. Data.** ID images, names, birth dates, face scans (biometric data under 2.D.13). Deletion within 7 days [EX] under the statute; well inside the 10-year biometric limit [S1]. The yes/no result is kept for the life of the account.

**B8. Dependencies and evasion.** [AGE-CHECK VENDOR] holds the data during checks. Whether it trains models on the face scans is UNKNOWN; if it does, the trained model would be a derived output (4.4).

**B9. Harms seen.**
- agency, communicative: adults wrongly classed as minors and restricted; allegation in user complaints [EX].
- informational: none documented yet; the risk of an ID-image breach is recorded for watching.

**B10. Decision inputs and oversight.** Document checks and a face age model; the model's error rates by age band are published by the vendor [EX], but not by group (5.3). The [STATE] attorney general receives yearly reports (5.1).

---

## PART C — Sources

| ID | Kind (quote / data_point / first_hand) | Title or description | Link | Where in it (page, section, table) | Quote (for kind = quote) | Verified? (yes / tool_text / unverified) |
|---|---|---|---|---|---|---|
| S1 | data_point | Core Requirements v1: rule figures and definitions cited | BPF: Core Requirements v1 | Definitions (Authority, Causation Ladder); 2.D.11; 2.D.13 | | yes |

All other figures are illustrative and tagged [EX]. No real institution was used as a source.

---

## PART D — Honesty assertions

- [x] Every number has a source tag.
- [x] Nothing was invented. Where I could not find something, I wrote UNKNOWN. Where something is absent, I wrote NONE EXISTS.
- [x] Public sources and first-hand observation only. Nothing private, leaked, or speculative.
- [x] People are referred to by role or title.
- [x] Adjudicated or admitted facts are kept separate from allegations.
- [x] I made this record in good faith, as a structural description, not an accusation.

Preparer: BPF examples working group. Worked example; all figures illustrative.

---

## Teaching notes (non-binding)

- Identify what the platform directly controls before attributing directive authority over users' behavior. Ranking, recommendation, and reach limits on its own service are direct. Scale and measured effects on behavior do not by themselves make ranking `indirect_b`; that needs its own explanation of how the effect works as directive control, and indirect_a would need a reliant party and a tier (Authority definition; Definitions: Causation Ladder; 4.3).
- Classifying ranking as direct does not mean it is harmless or beyond scrutiny. Opaque reach limits, undisclosed inputs, and the lack of an independent challenge are still findings against P2. A platform can exercise both direct and indirect power, but each classification needs its own evidence. Each power gets its own row of findings (3.A.1).
- A stop path that shuts the whole service is real but not narrow. It would stop unrelated powers along with ranking (3.C.5).
- "Partly independent" fits dispute bodies certified by a regulator but paid per case by the platform, and arbitrators chosen under the platform's own terms (Definitions: Independent; 3.A.7).
- A statute can make some rows conforming. The sunset meets the 2-year term limit, and the public statute meets visibility. A mandate without findings on harms and stops is still not an authorization (7.2, 3.B.9, 3.A.2).
- Identification as a condition of expression is never permitted, even when a law requires it. The legislature's mandate would itself be recorded as a power (2.D.11, 2.D.9).
- Reach limits that authors are never told about fail the plain-explanation floor, and they leave nothing to challenge (2.C.1, 2.D.5).
- Using contractors is not evasion when the platform directs them and answers for their work. That is why the evasion row conforms for P1 (4.1, 4.5).
- Choosing a chronological feed is self-help, not a stop path (Form B5).
- Rule 2.D.9 permits narrow, published rules tied to a space's purpose, applied without regard to viewpoint and open to challenge. Publishing rules is not enough. For P1, narrowness, viewpoint-neutral application and challenge in [COUNTRY] are not shown, so the expression answer is UNKNOWN. Identity checks to win back an account fall under the claimed-entitlement case of 2.D.11, while the [STATE] age check does not. A ban entry is a sanction listing under 2.D.12 and 2.D.6, not an accountability record (2.D.14).
- A ban that follows a person to new accounts works by reading identifiers from their devices, and a ban that keeps unpaid earnings takes property. Both are 2.D.15 questions as well as 2.D.9 ones: the first needs individualized cause and independent approval, the second a finding of responsibility with due process.
