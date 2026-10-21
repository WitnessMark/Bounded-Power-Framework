# Challenge Workflow — Worked Example

*Core Requirements v1 · Example made with Witness Report form 1.0.0 and Authority Response form 1.0.0*

> **WORKED EXAMPLE — not about any real institution.** Names, places, dates and outcomes are illustrative.

## What a challenge is

A challenge says that something on the record is wrong, or that an institution is acting outside its limits. In v1 there are two ways to make one, depending on who is challenging what.

| Who | Challenges what | Uses | Example in this folder set |
|---|---|---|---|
| **Anyone** (an affected person, a worker, a neighbour) | An institution acting outside its limits: beyond its scope, after its term ended, blocking a stop path, retaliating | A **witness report** with `report_type: challenge` | [SCBP-WR-EXAMPLE-TOWN-LIBRARY-2026-10-06.md](SCBP-WR-EXAMPLE-TOWN-LIBRARY-2026-10-06.md) |
| **The institution** | A registration record about it that it thinks is wrong or incomplete | An **authority response**, filed beside the record | [Water utility correction](../SCBP-RSP-EXAMPLE-CITY-WATER-UTILITY-2026-10-21.md), [data broker disagreement](../SCBP-RSP-EXAMPLE-DATA-BROKER-2026-10-21.md) |

Neither one changes a record by itself. **No silent replacement:** a record changes only when the person who made it issues a new version that quotes everything it changed. See [the water utility's version 2](../SCBP-REG-EXAMPLE-CITY-WATER-UTILITY-v2.md).

No penalty may attach to challenging an authority. Retaliation is itself a violation, and can be reported with the same form (3.C.6).

---

## Route 1 — A person challenges an institution (witness report)

### The case

The `[TOWN] Public Library` has adopted the Core Requirements. Its authorization record ([SCBP-REG-EXAMPLE-TOWN-LIBRARY](../SCBP-REG-EXAMPLE-TOWN-LIBRARY.md)) limits internet filtering (power P3) to the categories of images a national subsidy law requires. It also says: no new categories without re-entry.

A regular user of the public computers notices that pages about local news and community groups are now blocked under a category called "Social and Forums".

### Step by step

1. **The person files a witness report of type `challenge`.** They give the place first, then what happened in their own words. They tick "acting outside its scope or limits" and name the record and power (SCBP-REG-EXAMPLE-TOWN-LIBRARY, P3). They file under a handle, not their name. No proof, special wording, or permission is needed (2.C.2).
2. **The report enters the library's adopted review process.** In this fictional scenario, the library has adopted the Core Requirements and established a reporting and review arrangement. The report is received through that arrangement, linked to the library's P3 authorization record, and considered with other relevant reports under the applicable review rules (3.E.5, 7.7). Filing a report does not mean that BPF itself operates a central registry, accepts submissions, or conducts the independent review. Those functions must be provided by the institution's actual adopted arrangements and the independent bodies authorized to perform them.
3. **The library must not decide its own scope.** Whether "Social and Forums" falls inside the authorization is a question about the library's own limits. The library may not settle it by its own reading; it goes to an independent body and into the public interpretation log (Interpretation; 7.3). Meanwhile the narrower reading applies (1.5).
4. **The independent check (illustrative).** The library's independent reviewer compares the filter settings with the authorization. It confirms that a vendor software update switched on two categories that were not authorized. The vendor is part of the power, so the update is the library's responsibility (4.5).
5. **Growth is stopped.** A new restriction category is a change of scope, and growth without new authorization is stopped (3.B.1). Only the two added categories are switched off; the authorized filtering continues, because a stop reaches only the operation implicated (3.C.5).
6. **The library responds on the record.** It answers publicly within its published response window, and its answer is entered in section 8 of the report. It logs the failure in its failure record (7.4) and adds a check of vendor updates to its routine.
7. **Later: renewal.** The event is evidence at P3's renewal. Drift that was found and corrected is part of the drift review; drift found and not corrected would bar renewal (3.E.2). See the [Renewal Workflow](../Renewal-Workflow/Renewal-Review-EXAMPLE.md).

### What section 8 of the report would say afterwards (illustrative)

- *Response from the institution, and its date:* the library confirmed a vendor update had switched on two unauthorized categories, and switched them off.
- *Outcome:* growth stopped under 3.B.1; failure recorded (7.4); vendor-update check added.

### Two variations

- **If the person had wanted an immediate pause,** they could have filed a `stop_signal` instead. Its basis would be `defined_condition` if they read the category limit as a defined stop condition, or `credible_pathway` if not; the checking body records the facts either way. A signal that a defined stop condition has occurred pauses the operation at once, and an independent body then checks one question: did the trigger fact occur (3.C.3)? A challenge asks for the limit to be enforced; a stop signal asks for a pause now. Either way, the same facts get checked.
- **If the library had not adopted the Core Requirements,** nothing would be paused or stopped by the framework. A nonadopter is not subject to BPF stop or pause requirements, and there would be no adopted review arrangement to receive the report. The person could still keep the report, publish it, or send it to the library and to others. If published, the finding ("acting outside its stated limits") becomes part of the public record about the library. Any operative consequence comes from others: courts, funders, the people affected, or the library itself (Core Requirements, "Force and status").

---

## Route 2 — An institution challenges a record (authority response)

1. An outside record says something the institution thinks is wrong or incomplete.
2. The institution files an **authority response** beside the record. It quotes each point exactly and gives its evidence. Types: `correction`, `added_information`, `disagreement`, `change_notice` (the institution announces changes it has made, without adopting the Core Requirements), and `adoption_notice` (the institution has formally adopted them).
3. The response never replaces the record. Readers see both.
4. The record's preparer decides, point by point. Accepted points go into a **new version** with a section headed "What changed from version N" that quotes the old text, the new text, and the reason. Points not accepted are explained.
5. Every version and every response stay public.

Read the three worked responses, then the water utility's version 2, to see this end to end.

---

## Checking a report

The checker (`../../02-Forms/validate_record.py`) reads witness reports as well as records. On a first-hand report it warns about numbers and dates without a source tag. That is expected: a witness's own observation is its own source, recorded in the Evidence table as `my_observation`. The warnings are a prompt to check, not errors to "fix" by editing the witness's words.
