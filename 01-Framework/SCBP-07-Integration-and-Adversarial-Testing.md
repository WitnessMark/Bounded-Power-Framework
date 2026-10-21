# SCBP-07 — Integration and Adversarial Testing

*v1 · 2026-10-21 · Published for independent review · Not adopted by anyone*

**Status:** Guidance. It may never narrow, waive, or reinterpret the Core Requirements (6.1). Where it and the Core Requirements differ, the Core Requirements govern. Where it and the Operations Manual (SCBP-03) overlap, the manual's procedure is the one to follow.

---

## Part I — How the pieces fit

The Core Requirements apply to an existing institution without replacing it. They attach to its **powers**, one at a time. How that happens depends on who is doing the work.

| Situation | What happens | Where it is set out |
|---|---|---|
| Someone records an existing institution from the outside | Institution first, then each power (P1, P2…). Observed vs required. Findings only. | Operations Manual, Stage 0; registration form |
| An institution adopts the Core Requirements | Every existing power is authorized within 12 months, or on an approved schedule of up to 3 years | Core 7.1; Operations Manual, Step 1.11 |
| A new power is created by an adopting institution | Authorized separately, by an independent body, before it operates | Core 3.A.1, 3.A.2; Operations Manual, Stage 1 |
| An authorized power operates | Monitoring, stop signals, pauses and stops | Operations Manual, Stages 2–4 |
| People report harm, signal a stop, or petition for review | Witness Report form; pause-then-check for adopting institutions | Core 3.C.3, 3.E.5; SCBP-08 |
| Its term ends | Renewal as a new decision, or expiry | Operations Manual, Stages 5–6 |
| Findings are expressed and published | Fixed vocabulary; no silent replacement | SCBP-05; SCBP-06 |

Three points matter at every step:
- **Nothing is attached by force.** The framework claims its Floors for everyone (Force and Status). But a non-adopting institution receives only findings, never obligations. An adopting institution may withdraw after 12 months' public notice (7.1). Pending pauses, stops, findings, and obligations survive withdrawal.
- **Outside help is part of the power.** Vendors, contractors, partners, and foreign or affiliated systems are treated as part of the authority when their outputs are used to achieve effects the Core Requirements restrict (4.5). The same goes for anything that gets its outputs (4.6).
- **Separate systems may be one authority.** Systems that coordinate as one authority function are evaluated as one (4.2). That finding needs Causation Ladder tier 5 or stronger. Sharing data, or producing similar outcomes, is not enough by itself.

---

## Part II — Adversarial testing

### Purpose

Adversarial testing looks for the ways a power could grow, persist, or escape its limits without breaking any rule on its face. It assumes **hostile compliance**: someone following the letter of every rule while defeating its purpose (4.8).

These tests serve two uses:
- **Required review.** For an adopting authority, every renewal needs a drift review by testers independent of the authority (3.E.2). Stop paths must be shown by test to work before a power operates (3.A.7).
- **Better records.** For an outside record, the tests point to where to look. Their results go into the record only as findings under SCBP-05 and SCBP-06.

### Who tests

Testers for the renewal drift review must be **independent** of the authority (3.E.2; Definitions, "Independent"). This means not funded, appointed, or controlled by it, and not relying on it for data. For other testing, independence is good **practice**. Publish the results **(practice)**.

### Section I — Test modes

Each mode names the rule it tests against.

**Evasion**

| Test mode | What it probes | Core rule |
|---|---|---|
| Relabeling | Renaming or reclassifying a function to escape its limits | 1.3, 4.1 |
| Fragmentation | Splitting one function across entities, systems, or time periods | 4.2 |
| Intermediaries | Getting a contractor, vendor, partner, or affiliate to do what the authority could not | 4.5 |
| Laundered data | Using bought data, or data from a non-authority source, or derived outputs, to escape purpose or expiry limits | 4.4 |
| Proxy variables | A variable that stands in for a characteristic listed in 2.D.10 | 4.7 |
| Indirect authority | Scores, rankings, defaults, or filtering that bind people without any formal order | 4.3 |
| Interpretation abuse | Formal compliance that defeats the purpose | 4.8 |

**Drift.** Every renewal needs an independent drift review (3.E.2). The Operations Manual (Step 5.1) lists what it covers; these are those modes.

| Test mode | What it probes | Core rule |
|---|---|---|
| Reinterpretation | Scope widened by reading the grant more broadly | 1.5, 7.3 |
| Accumulation | Growth by small steps, in any of the six dimensions | 3.B.1, 3.A.6 |
| Stop friction | Stop paths that are slower, costlier, or harder to use than at the start | 3.A.7, 3.C.1 |
| Capture | Dependence on concentrated private interests or infrastructure | 3.B.6 |
| Lock-in | Dependencies, contracts, or data formats that make replacement harder | 3.A.8, 3.B.7 |
| Accumulating advantage | Exclusive data, skills, or contracts that build up over those who could stop, challenge, or replace the power | 3.A.6, 3.B.7 |

**Evidence and metrics**

| Test mode | What it probes | Core rule |
|---|---|---|
| Metric manipulation | Declared inputs that are incomplete or misleading | 5.3, 3.B.8 |
| Outcome drift | Practical effects beyond the authorized scope | 5.4 |
| Evidence withholding | Restricting what reviewers need | 5.1, 5.2 |
| Signal suppression | Stop signals falling while activity grows | 3.B.8, 7.7 |

### Section II — Scenario tests

Each test asks one question. A "yes" is a finding against the rule named. It is not a verdict on the whole institution. For a non-adopting authority it is a published finding only (SCBP-06).

| Test | Question | Core rule |
|---|---|---|
| Global effect | Does each part comply locally while the parts together exceed the limits, or become harder to stop? | 3.B.3, 4.1, 4.2 |
| Time | Can delay, speed, or procedural time be used to make an effect irreversible before review, pause, or renewal? | 3.D.2, 5.6 |
| Essential function | During a stop, is the "minimum essential function" widened to keep the power running? Is it run by the authority whose power was stopped? | 3.C.5 |
| Reversibility | Is rollback possible on paper but impossible in practice? | 3.D.1 |
| Dependency | Would removing the power disrupt things beyond its authorized scope, or make replacement impractical? | 3.B.7; Definitions, "Dependency" |
| Stop path | Does each stop path actually work when tried, without the authority's cooperation? | 3.A.7, 3.C.1 |
| Interruption **(practice)** | If a key vendor withdrew or infrastructure failed, could the power be halted and the function transferred safely? | 3.A.7, 3.B.2 |
| Emergency | Does a claimed emergency widen the power or disable a stop or Floor? | 1.6 |

### Section III — Test output

Each test produces:
- the method used;
- what was observed, with sources (three-answer rule);
- the finding, in the SCBP-05 vocabulary, with the rule and the Causation Ladder tier where needed;
- what correction the Core Requirements call for (SCBP-06, Part C).

### Section IV — When to test

| When | What | Basis |
|---|---|---|
| Before a power operates | Every stop path tested. Halting, replacing, and dismantling rehearsed; minor powers skip the rehearsal but not the test (3.A.4) | 3.A.7 |
| Every year | Stop paths re-tested; holders still independent | Operations Manual, Stage 3 **(practice)** |
| At each renewal | Independent drift review covering every drift mode above | 3.E.2 |
| After a material change | The modes the change could affect | **(practice)** |

For an adopting authority, missing tests have consequences under the Core Requirements:
- A power without tested stop paths has an invalid authorization (3.A.7).
- Renewal evidence without the drift review is incomplete, and incomplete evidence means no renewal (3.E.2).
