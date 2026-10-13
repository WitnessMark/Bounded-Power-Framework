# Validator Coverage Matrix

*For checker `02-Forms/validate_record.py` 1.0.0 · Registration form 1.0.0 · Witness Report form 1.0.0 · Vocabulary 1.0.0 · 2026-10-13 · Draft*

**Purpose:** show which checks the automated checker makes on a record, and which only a person can make.

The checker prints three kinds of line:
- **ERROR** — the record is broken; the checker exits with an error. A record should have none.
- **WARN** — something looks incomplete. A person decides.
- **REVIEW** — a person should read this part before relying on the record.

## Registration records

| Responsibility | Checker | Person |
|---|---|---|
| Front matter present and valid YAML | ERROR | |
| Required fields present (record type, ID, version, supersedes, preparer, dates, institution, adoption status, powers) | ERROR | |
| Versions stated: form, Core Requirements, bundle, vocabulary | ERROR | |
| Vocabulary values come from `VOCAB.yml` | ERROR | |
| Record ID format; example IDs and the WORKED EXAMPLE banner | ERROR | |
| Dates in YYYY-MM-DD form | ERROR | |
| Institution name, legal entity, type, country, and website filled in (a value, UNKNOWN, or NONE EXISTS) | ERROR | |
| Each listed power has its own section, and all ten finding rows | ERROR | |
| Front-matter findings match the finding column of the B4 table | ERROR | |
| A minor power is claimed only in an authorization record, and never for force or confinement (3.A.4) | ERROR | |
| A version above 1 states what it supersedes and has a "What changed" section | ERROR | |
| An observed record has no Part E; an authorization record has one | ERROR | |
| Part C (Sources) present | ERROR | |
| Every `[S#]` tag has a row in the Sources table | ERROR | |
| Every source row has a valid kind, a link (or `first_hand`, or `BPF: <document>`), and a quote where the kind is quote | ERROR | |
| **Every number has a source tag** in the same sentence or table row | ERROR | |
| `[EX]` illustrative tags used only in worked examples | ERROR | |
| B1–B10 present in each power section; B5 stop-path statement present | WARN | |
| Empty Observed cells or empty findings in B4 | WARN | |
| Source rows with no location, or never cited | WARN | |
| File name matches the record ID and version | WARN | |
| Placeholder text left unfilled | WARN | |
| Quotes seen only in a summary, not the original | REVIEW | Check against the original |
| Possible personal names near accusation words | REVIEW | Replace names with roles |
| A title or rank followed by a capitalized word that is not a role word ("Officer D…", "Dr. …") | WARN | Replace names with roles |
| **Whether each source actually says what the record claims** | | ✓ |
| Whether an UNKNOWN could have been found | | ✓ |
| Whether NONE EXISTS was checked where the thing would be | | ✓ |
| Whether each Observed answer leads to the right finding (for example NONE EXISTS → not conforming) | | ✓ |
| Authority basis and limb (direct, operationalized, directive control, influence only) | | ✓ |
| Causation Ladder tier stated, and strong enough for the finding | | ✓ |
| Stop paths: what each can really stop, and whether its holder is independent | | ✓ |
| Floor answers and their reasons | | ✓ |
| Facts kept separate from allegations, and labelled correctly | | ✓ |
| No real person named anywhere, including where the name check cannot see | | ✓ |
| Powers missed by the record | | ✓ |
| A worked example does not resemble a real institution closely enough to be read as describing it | | ✓ |

## Witness reports and authority responses

| Responsibility | Checker | Person |
|---|---|---|
| Required fields, ID format, versions, vocabulary values, dates | ERROR | |
| Witness report: coordinates in range; withheld location has no coordinates; a stop signal states its basis | ERROR | |
| Witness report: numbers without a source tag outside the witness's own first-hand sections (dates, section 2, block quotes, "my own observation" rows and the list of what exists are not flagged) | WARN | |
| Witness report: a title or rank followed by a name, anywhere except the witness's own name line | WARN | Replace names with roles |
| A value meaning "unknown" (UNKNOWN or unknown) accepted in any case | — | |
| Authority response: carries the banner saying it does not replace the record | ERROR | |
| Authority response: a correction or disagreement quotes the record point by point | WARN | |
| Whether the account is accurate and fairly labelled | | ✓ |

## Principle

The checker checks structure, completeness, and that every number has a source. It does not decide whether anything is true.

A person checks evidence, reasoning, and judgment.

Both are needed. A record with no ERRORs is well-formed, not correct.
