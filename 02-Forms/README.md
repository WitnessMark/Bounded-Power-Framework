# Forms

*v1 · 2026-10-13 · Published for independent review · Not adopted · For use with the Core Requirements ([SCBP-04](../01-Framework/SCBP-04-Core-Requirements.md))*

**Something happened to you?** Start with the plain [Witness Report Filing Guide](../00-Reading/09-Citizen-Witness-Report-Filing-Guide.md) or the [AI Witness Interview Bundle](../00-Reading/10-AI-Witness-Interview-Bundle.md). **Recording an institution?** Start with the [Citizen Inquiry Guide](../00-Reading/05-Citizen-Inquiry-Guide.md). You don't need anything else on this page.

These are the tools for describing an institution and its powers, and comparing each power with the Core Requirements.

## Files

| File | What it is | Version |
|---|---|---|
| [`01-Registration.md`](01-Registration.md) | Registration form. Records the institution, then each of its powers, and compares each power with the Core Requirements | 1.0.0 |
| [`02-Witness-Report.md`](02-Witness-Report.md) | Witness report form: incidents, stop signals, challenges, change requests, review petitions | 1.0.0 |
| [`03-Authority-Response.md`](03-Authority-Response.md) | Authority response form. An institution's answer, filed beside a record, never replacing it | 1.0.0 |
| [`VOCAB.yml`](VOCAB.yml) | Shared word lists used by the forms, the bundle, and the checker | 1.0.0 |
| [`validate_record.py`](validate_record.py) | Checker for records, reports, and responses | 1.0.0 |
| [`AI-Registration-Bundle.md`](AI-Registration-Bundle.md) | AI bundle: one file to give an AI assistant. Built from `bundle-core.md`, the registration form, the vocabulary, and the Core Requirements | 1.0.0 |
| [`10-AI-Witness-Interview-Bundle.md`](../00-Reading/10-AI-Witness-Interview-Bundle.md) (in `00-Reading/`) | AI witness interview bundle: one file that turns an AI chat into an interviewer and produces a witness report | 1.0.0 |
| [`bundle-core.md`](bundle-core.md), [`build_bundle.py`](build_bundle.py) | The bundle's own text, and the script that assembles the bundle | — |
| [`tests/`](tests/) | Fictional test files for the checker. One should pass and one should fail | — |

Every form, the bundle, and every record state their versions and dates, so it is always clear which rules applied when a record was made.

## The rules every record follows

- **Three answers, never a guess.** Every factual field is a value with its source, UNKNOWN, or NONE EXISTS.
- **Every number has a source tag** in the same sentence, or in its table row.
- **Roles, not names.** Public sources and your own observation only.
- **Power first.** Record the institution, then each power separately.
- **No silent replacement.** A record changes only by a new version from its original preparer, quoting what changed. An institution answers with an authority response filed beside the record.

## Using them

v1 has no place to submit records or reports. If you make a record, it is yours, and publishing it is your choice and your responsibility (see [TERMS](../TERMS.md)). The [worked examples](../03-Examples/) show complete records.

To check a file, from the repository root (needs Python 3 and PyYAML: `pip install pyyaml`):

```
python3 02-Forms/validate_record.py path/to/your-record.md
```

The checker confirms that each number has a source tag. It cannot confirm that the source says what the record claims. A person must check the sources.

To rebuild the AI bundle after changing the form, the vocabulary, the bundle text, or the Core Requirements:

```
python3 02-Forms/build_bundle.py
```
