# How to Write a Worked Example

*2026-10-13 · Guide for contributors · Registration Form 1.0.0 · Core Requirements v1*

Worked examples show how the framework applies to a *kind* of institution. They are **not** records of any real institution. Version 1 of the framework publishes worked examples instead of records of real institutions.

## Hard rules
1. **Nothing real and identifiable.**
   - No real institution, place, person, product, vendor, court case, news outlet, or nonprofit.
   - Use bracketed placeholders: `[CITY]`, `[COUNTY]`, `[STATE]`, `[COUNTRY]`, `[CITY] Police Department`, `[BODY-CAMERA VENDOR]`, `[STATE] Mental Health Code`.
   - Don't combine details so that the example obviously points to one real organization (for example, "one of two dominant card networks with about 4 billion cards").
2. **Allowed real things:** national laws and national agencies that form common infrastructure, named generally ("the federal fair credit reporting law", "the federal consumer financial regulator", "a federal civil-rights lawsuit"). Avoid statute section numbers; if you use one, give it a real source row in Part C.
3. **Every figure is tagged `[EX]`,** meaning an illustrative number for the example. Tag it in the same sentence or the same table row. Use realistic orders of magnitude, but never copy one real institution's figures.
4. **Front matter:**
   - `record_type: observed` (or `authorization` for the two authorization examples; see below);
   - `example: true`;
   - `record_id: SCBP-REG-EXAMPLE-{SUFFIX}`;
   - `prepared_by: person`;
   - `institution.name` in brackets;
   - `official_url: NONE`;
   - `adoption_status: not_adopted` (or `adopted` for authorization examples);
   - `bundle: NONE`.

   Save the file as `SCBP-REG-EXAMPLE-{SUFFIX}.md`.
5. **Banner** directly under the front matter:
   `> **WORKED EXAMPLE — not a record of any real institution.** Names, places, and figures are illustrative.`
6. **Findings must be realistic, not automatic.** Show what typically exists for this kind of institution today.
   - Many existing institutions really do have NONE EXISTS for independent authorization, expiry, thresholds and ending plans. Say so where it's typical.
   - Where something real usually exists, show it: a statutory appeal, an inspector general, a court injunction, a sunset clause, a consent decree.
   - Mix findings honestly. Some rows should be `conforming` where that's typical.
7. **Stop paths:** show what each can really stop (`whole_power` / `one_practice` / `one_case`). State plainly whether anything can stop the whole power under current law.
8. **Tone:** describe structure, not motives. No loaded words. No bold text for emphasis inside answers.
9. **Run the checker** and fix every ERROR:
   `python3 ../02-Forms/validate_record.py FILE`

## Conventions
- **No signature facts.** Don't reproduce a real body's distinctive combination of details: an exact settlement amount, a unique committee size or founding year, a named program, or a famous incident. Change numbers and details enough that no single real body or event is pointed to.
- **Currency:** examples set in `[COUNTRY]` use "currency units". `[STATE]` examples may use dollars.
- **Rule-derived numbers** (48 hours, 90 days, 20 years) are tagged `[S1]`, with S1 = `BPF: Core Requirements v1` (data_point).
- **Causation Ladder:** tiers 1–5 support a finding; tiers 6–7 support only a recorded concern. Tier 1 is the strongest.
- **Whole-power stop paths:** follow the definition under B5 in the form. A new law, the institution's own governing body, or a fork or replacement does not count.
- **Self-help is not a stop path** (declining, paying, turning a setting off).
- **Visibility:** judged on whether the facts are knowable. A publicly stated "no expiry" can be conforming; record the failure under Maximum term.
- **A 3.D.5 pattern finding needs established Floor violations.** A settlement without admission, or unproven allegations, supports only a recorded concern.
- **Each example stands on its own.** Don't refer to other editions of the framework.

## Structure
- Use the template in the Registration Form (`../02-Forms/01-Registration.md`) exactly:
  - `## PART A`;
  - `## Power P1 — …` with **B1 to B10** in order;
  - `## PART C — Sources`, which can be an empty table if there are no real sources;
  - `## PART D`.
- **Authorization examples** (Town Library, Mutual-Aid Network) use `record_type: authorization` with `example: true`. They include `## PART E` with the institution's authorization record and commitments, following SCBP-03 Stage 1. That means thresholds with five parts, tested stop paths, term, ending plan, and so on. The checker requires PART E for authorization records.
- **End with a non-binding teaching section:**
  ```
  ## Teaching notes (non-binding)
  ```
  Write 5–10 short bullets on what this example teaches, each with the Core Requirements rule numbers (such as 2.D.3(b) or 3.C.5).

## Length
About 150–300 lines. Record 1–4 powers. Depth on the example's main teaching point matters more than completeness everywhere else.

## References
- Core Requirements: `../01-Framework/SCBP-04-Core-Requirements.md`
- Operations manual: `../01-Framework/SCBP-03-Operations-Manual.md` (Stage 0 for observed records, Stage 1 for authorization records)
- Vocabulary: `../02-Forms/VOCAB.yml`
- What each example teaches: `README.md` in this folder
