# Validator Coverage Matrix

*For checker `02-Forms/validate_record.py` v1 · Registration form v1 · Witness Report form v1 · Authority Response form v1 · Vocabulary v1 · 2026-11-05 · Draft*

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
| A version above 1: `supersedes` names the same record ID and the version just before, and the heading reads "What changed from version N" for that version | ERROR | |
| Whether the earlier version exists, and whether every change was disclosed | | ✓ |
| `record_url` is NONE or a web address | ERROR | |
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
| Conduct words beside an office that one person holds (the Sheriff, the Mayor) | REVIEW | Attribute it to the office or the institution |
| A court case named ("A v. B") with no source tag | ERROR | |
| A title or rank followed by a capitalized word that is not a role word ("Officer D…", "Dr. …") | WARN | Replace names with roles |
| **Whether each source actually says what the record claims** | | ✓ |
| Whether an UNKNOWN could have been found | | ✓ |
| Whether the evidence establishes absence for each NONE EXISTS | | ✓ |
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
| Witness report: `verification_hash` is NONE or a 64-character SHA-256 code, never the phrase itself | ERROR | |
| Witness report: `record_id` is NONE or shaped like a registration ID; `power_id` is UNKNOWN or P1, P2…; a power is not named without a record | ERROR | |
| Witness report: `situation_kind`, `action_category`, `harm_type`, `evidence_held`, `memory_influences` are lists of vocabulary values; `none` stands alone | ERROR | |
| Witness report: `incident_time` is "HH:MM" in quotes or UNKNOWN; `jurisdiction` has locality, region and a two-letter country code | ERROR | |
| Witness report: `statement_confirmed` is true or false; `truth_statement` and `composed_by` are vocabulary values | ERROR | |
| Witness report: the retired `status` field | ERROR | Use `incident_end_date`; the outcome goes in What happened next |
| Witness report: a Statement section; and "In my own words" when someone other than the witness wrote the statement | ERROR | |
| Witness report: the statement holds only what the witness said | | ✓ |
| Witness report: the witness has not confirmed the statement (`statement_confirmed: false`) | WARN | Read it with the witness |
| Witness report: the named record and power actually exist | | ✓ (no place collects records in v1) |
| Witness report: numbers without a source tag outside the witness's own first-hand sections (dates, section 2, block quotes, "my own observation" rows, evidence rows that cite a link, and the list of what exists are not flagged; web addresses are never read as numbers) | WARN | |
| Witness report (copy for sharing): a town- or region-level location (`locality`, `region`) whose description names the institution | WARN | Check the place is no more exact than the witness chose |
| Witness report: an optional section answered "Not applicable" | WARN | Write UNKNOWN if it was skipped or not asked |
| Witness report: fields at the end, in a ```yaml block under "Technical details" (the current layout), or on top (the older one) | ERROR if neither | Both are read; only witness reports may keep fields at the end |
| Witness report: names, badge numbers and descriptions | — | Kept on purpose: the name and officeholder checks are not run on witness reports |
| Witness report: a "Private copy." line from the earlier layout | WARN | Remove it |
| Witness report (copy for sharing): About me is left out | ERROR | |
| Witness report (copy for sharing): a file name not ending in `-SHARE`, or a `-SHARE` file without the line | WARN | Rename the file, or add the line |
| Witness report (copy for sharing): no private person can still be identified | REVIEW | ✓ Read it as a stranger would |
| A value meaning "unknown" (UNKNOWN or unknown) accepted in any case | — | |
| Authority response: carries the banner saying it does not replace the record | ERROR | |
| Authority response: a correction or disagreement quotes the record point by point | WARN | |
| Authority response: `response_to` names a registration record ID and a whole-number version, and the response ID carries that record's suffix | ERROR | |
| Authority response: a `change_notice` or `adoption_notice` describes the changes in section 3 | WARN | |
| Whether the answered record and version exist | | ✓ |
| Whether the account is accurate and fairly labelled | | ✓ |

## Principle

The checker checks structure, completeness, and that every number has a source. It does not decide whether anything is true.

A person checks evidence, reasoning, and judgment.

Both are needed. A record with no ERRORs is well-formed, not correct.
