#!/usr/bin/env python3
"""
BPF record checker, version 1.0.0 (2026-10-13).

Checks registration records (form 1.0.0), witness reports (form 1.0.0), and
authority responses (form 1.0.0). Reads VOCAB.yml from its own folder.

Usage (from the repository root):
    python3 02-Forms/validate_record.py FILE [FILE ...]
    python3 02-Forms/validate_record.py 03-Examples/SCBP-*.md 04-Registry/SCBP-*.md
    python3 02-Forms/validate_record.py --vocab path/to/VOCAB.yml FILE

What it checks:
  - front matter parses, required fields present, versions and dates stated
  - every vocabulary value comes from VOCAB.yml
  - registration: every listed power has a body section; finding values valid;
    observed records contain no Part E commitments
  - every source tag [S#] used in the text exists in the Sources table, and
    every source row has a link (or 'first_hand') and a location
  - NUMBERS WITHOUT SOURCES: any line stating a figure (count, %, money,
    duration, year) with no [S#] tag is flagged. This is how invented values
    are caught.
  - placeholder text left unfilled

What it cannot check:
  - whether a source actually says what the record claims (a person must)
  - whether a value marked UNKNOWN could have been found
  - whether people are named (it warns about titles followed by a
    capitalized word, and flags capitalized name-like pairs near accusation
    words, for human review only)

Exit code 0 = no errors (warnings may remain); 1 = errors found.
"""
import re
import sys
import os
import datetime

try:
    import yaml
except ImportError:
    print("This checker needs PyYAML:  pip install pyyaml")
    sys.exit(2)

CHECKER_VERSION = "1.0.0"
HERE = os.path.dirname(os.path.abspath(__file__))

SPECIAL = {"UNKNOWN", "NONE EXISTS", "NONE"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SRC_TAG = re.compile(r"\[S(\d+)\]|\[EX\]")
S_ONLY = re.compile(r"\[S(\d+)\]")
RULE_REF = re.compile(r"\b\d\.[A-E]\.\d+\b|\b\d\.\d+\b|\bPart [IVX]+\b|\b2\.[A-D]\b|\bR\d{2}\b")
NUMBER_RE = re.compile(
    r"(\$\s?\d[\d,.]*|\d[\d,.]*\s?%|\b\d{1,3}(,\d{3})+\b|\b\d+(\.\d+)?\s?(million|billion|thousand|percent|years?|months?|days?|hours?|people|persons|consumers|residents|employees|staff|cases|files|records)\b|\b(19|20)\d{2}\b|\b\d{2,}\b)",
    re.I)
PLACEHOLDER_RE = re.compile(r"\[(Institution name|Institution|short name|S#|Incident date)\]|\{SUFFIX\}|YYYY-MM-DD")


def load_vocab(path):
    with open(path) as f:
        return yaml.safe_load(f)


def split_front_matter(text):
    if not text.startswith("---"):
        return None, text
    parts = text.split("\n---", 2)
    if len(parts) < 2:
        return None, text
    fm = parts[0][3:]
    body = parts[1] if len(parts) == 2 else parts[1] + "\n---" + parts[2]
    # body begins after the closing '---' line
    body = body.split("\n", 1)[1] if "\n" in body else ""
    return fm, body


class Report:
    def __init__(self, path):
        self.path = path
        self.errors = []
        self.warnings = []
        self.reviews = []

    def err(self, m): self.errors.append(m)
    def warn(self, m): self.warnings.append(m)
    def review(self, m): self.reviews.append(m)

    def show(self):
        print(f"\n== {os.path.basename(self.path)} ==")
        for m in self.errors: print("  ERROR   ", m)
        for m in self.warnings: print("  WARN    ", m)
        for m in self.reviews: print("  REVIEW  ", m)
        if not (self.errors or self.warnings or self.reviews):
            print("  OK")


def check_versions(fm, r, form_name):
    form = fm.get("form")
    if not isinstance(form, dict) or form.get("name") != form_name or not form.get("version") or not form.get("date"):
        r.err(f"'form' must be {{name: {form_name}, version, date}}")
    cr = fm.get("core_requirements")
    if not isinstance(cr, dict) or not cr.get("version") or not cr.get("date"):
        r.err("'core_requirements' must state {version, date}")
    b = fm.get("bundle")
    if b not in ("NONE", None) and not (isinstance(b, dict) and b.get("version") and b.get("date")):
        r.err("'bundle' must be NONE or {version, date}")
    if not fm.get("vocab_version"):
        r.err("'vocab_version' missing")


def check_date(val, name, r, allow=("UNKNOWN", "NONE", "ongoing")):
    if isinstance(val, (datetime.date, datetime.datetime)):
        return
    if val in allow:
        return
    if not (isinstance(val, str) and DATE_RE.match(val)):
        r.err(f"'{name}' must be YYYY-MM-DD or one of {list(allow)} (got {val!r})")


def in_vocab(val, key, vocab, r, field=None, extra=()):
    allowed = list(vocab.get(key, [])) + list(extra)
    # "unknown" is accepted in any case where the vocabulary has an unknown value
    if isinstance(val, str) and val.lower() == "unknown" and any(
            isinstance(a, str) and a.lower() == "unknown" for a in allowed):
        return
    if val not in allowed:
        r.err(f"'{field or key}' value {val!r} not in VOCAB.yml {key}: {allowed}")


def sources_table(body):
    """Return dict S# -> row cells from Part C table."""
    rows = {}
    for line in body.splitlines():
        m = re.match(r"\|\s*S(\d+)\s*\|(.*)\|\s*$", line)
        if m:
            cells = [c.strip() for c in m.group(2).split("|")]
            rows[m.group(1)] = cells
    return rows


def segments(line, skip_cols):
    """Split a line into table cells (minus skipped columns) or sentences."""
    s = line.strip()
    if s.startswith("|"):
        if SRC_TAG.search(s):      # a table row's Source column covers the whole row
            return []
        cells = [c for c in s.strip("|").split("|")]
        return [c for k, c in enumerate(cells) if k not in skip_cols]
    return re.split(r"(?<=[.!?])\s+", s)


ISO_DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
FIRST_HAND_ROW = re.compile(r"my own observation|my_observation", re.I)
# witness-report sections written from the witness's own experience
WITNESS_FIRST_HAND = re.compile(r"^#{1,3}\s*(2\.|7\.)|What happened|About you", re.I)


def unsourced_numbers(body, r, as_error=True, offset=0, witness=False):
    in_code = False
    skip_section = False
    first_hand = False
    in_inventory = False
    skip_cols = set()
    count = 0
    for i, line in enumerate(body.splitlines(), 1 + offset):
        s = line.strip()
        if s.startswith("|") and (("Required" in s and "Observed" in s) or ("Question" in s and "Answer" in s)):
            # template text columns (rule summaries, floor questions) are not claims
            skip_cols = {k for k, c in enumerate(s.strip("|").split("|"))
                         if c.strip().startswith(("Required", "Question", "Floor", "Requirement"))}
            continue
        if not s.startswith("|"):
            skip_cols = set()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if re.match(r"^#{1,3} ", s):
            # don't scan the sources section or honesty section
            skip_section = bool(re.search(r"PART C|Sources|PART D|Honesty|PART E|Resolution", s, re.I))
            first_hand = witness and bool(WITNESS_FIRST_HAND.search(s))
            in_inventory = False
            continue
        if in_code or skip_section or not s:
            continue
        if re.match(r"^\|\s*S\d+\s*\|", s):
            continue
        if witness:
            # the witness's own account: first-hand sections, quotes, own-observation
            # evidence rows, and the inventory of what exists are their own source
            if re.match(r"^\*\*What exists but isn", s):
                in_inventory = True
                continue
            if first_hand or in_inventory or s.startswith(">") or (s.startswith("|") and FIRST_HAND_ROW.search(s)):
                continue
            s = ISO_DATE.sub(" ", s)
        for seg in segments(s, skip_cols):
            if SRC_TAG.search(seg) or not seg.strip():
                continue
            hit = _number_in(seg)
            if hit:
                count += 1
                if count <= 40:
                    (r.err if as_error else r.warn)(f"line {i}: number without a source tag -> \"{hit}\" in: {seg.strip()[:110]}")
    if count > 40:
        (r.err if as_error else r.warn)(f"... {count - 40} more unsourced numbers")


def _number_in(s):
        cleaned = RULE_REF.sub(" ", s)
        cleaned = re.sub(r"\b(P|S)\d+\b", " ", cleaned)             # power / source ids
        cleaned = re.sub(r"SCBP-[A-Z]+-[\w-]+", " ", cleaned)       # record ids
        cleaned = re.sub(r"\btier[:\s]*\d\b|\b\d\s*[–-]\s*\d\b", " ", cleaned, flags=re.I)
        cleaned = re.sub(r"^\s*[-*]?\s*\d+[.)]\s", " ", cleaned)    # list numbering
        cleaned = re.sub(r"^\|\s*\d+\s*\|", "|", cleaned)          # table row numbering
        cleaned = re.sub(r"\b[A-Z]\d\.?\b", " ", cleaned)           # field labels A1, B4
        m = NUMBER_RE.search(cleaned)
        return m.group(0).strip() if m else None


def check_sources(body, r):
    rows = sources_table(body)
    unver = []
    used = set(S_ONLY.findall(body))
    for sid in sorted(used - set(rows), key=int):
        r.err(f"source tag [S{sid}] used but S{sid} is not in the Sources table")
    for sid, cells in rows.items():
        kind = cells[0] if cells else ""
        link = cells[2] if len(cells) > 2 else ""
        loc = cells[3] if len(cells) > 3 else ""
        quote = cells[4] if len(cells) > 4 else ""
        ver = cells[5] if len(cells) > 5 else ""
        if kind not in ("quote", "data_point", "first_hand"):
            r.err(f"S{sid}: kind must be quote | data_point | first_hand (got {kind!r})")
        if kind != "first_hand" and not re.search(r"https?://|^BPF:", link):
            r.err(f"S{sid}: needs a link (or 'BPF: <document>' for framework documents)")
        if kind != "first_hand" and not loc:
            r.warn(f"S{sid}: say where in the source (page, section, table)")
        if kind == "quote" and len(quote.split()) < 3:
            r.err(f"S{sid}: kind is quote but no quote given")
        if ver not in ("yes", "tool_text", "unverified", ""):
            r.err(f"S{sid}: verified must be yes | tool_text | unverified")
        if ver == "unverified" and kind == "quote":
            unver.append(f"S{sid}")
    for sid in sorted(set(rows) - used, key=int):
        r.warn(f"S{sid} listed but never cited")
    if unver:
        r.review(f"{len(unver)} quote(s) seen only in summary, not checked against the original: {', '.join(unver)}")


INSTITUTION_WORDS = r"(Authority|Department|Agency|Bureau|Office|Court|Board|Commission|Council|County|City|Center|Centre|Services?|Company|Inc|LLC|Corporation|Act|Code|Street|Avenue|Park|Hall|Police|Sheriff|University|School|District|Fund|Trust|Bank|Group|Association)"


TITLES = (r"(?:Officer|Sgt\.?|Sergeant|Lt\.?|Lieutenant|Det\.?|Detective|Deputy|Judge|Mayor|Dr\.|"
          r"Mr\.?|Ms\.?|Mrs\.?|Councilmember|Councilman|Councilwoman|Commissioner|Chief|Sheriff|"
          r"Captain|Capt\.)")
TITLE_NAME = re.compile(r"\b" + TITLES + r"\s+([A-Z][a-zA-Z'’-]+)")
# capitalized words that follow a title but are roles or places, not names
ROLE_WORDS = {
    "Executive", "Officer", "Officers", "Justice", "Judge", "Judges", "Medical", "Financial",
    "Operating", "Information", "Technology", "Technical", "Administrative", "Administrator",
    "Inspector", "Clerk", "Director", "Deputy", "Assistant", "Associate", "General", "Health",
    "Public", "Fire", "Police", "Building", "Code", "Elections", "Election", "Council",
    "Board", "Governor", "Minister", "Secretary", "Counsel", "Attorney", "Constable",
    "Marshal", "Warden", "Commissioner", "Commissioners", "Mayor", "Sheriff", "Chief",
    "Captain", "Sergeant", "Lieutenant", "Detective", "Magistrate", "Registrar", "Steward",
    "Examiner", "Engineer", "Planner", "Auditor", "Treasurer", "Compliance", "Privacy",
    "Risk", "Data", "Security", "Probation", "Parole", "Patrol", "Corrections", "Custody",
    "Intake", "Housing", "Welfare", "Social", "Child", "Children", "Family", "School",
    "Academic", "Learning", "Program", "Programs", "Operations", "Investment", "Economist",
    "Executives", "Medicine", "Nursing", "Science", "Scientific", "Product", "Content",
    "Trust", "People", "Human", "Legal", "Ethics", "Diversity", "Equity", "Fiscal",
    "Of", "The", "A", "An", "And", "Or", "In", "On", "For", "At", "To", "Who",
    "May", "Must", "Can", "Is", "Are", "Has", "Was", "With", "By", "From", "As", "If",
    "Pro", "Tem", "Emeritus", "Designate", "Elect", "Gate", "Desk", "Unit", "Office",
    "Department", "Division", "Court", "Courts", "County", "City", "State", "District",
    "Town", "Village", "Township", "Region", "Regional", "National", "Federal",
    "Name", "Names", "Role", "Roles", "Title", "Example", "Fictional",
}


def title_names(body, r, offset=0, witness=False):
    """WARN for a title or rank followed by a capitalized word that is not a role word."""
    skip = False
    in_code = False
    found = []
    for i, line in enumerate(body.splitlines(), 1 + offset):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if re.match(r"^#{1,3} ", s):
            # sources may need a name to find a document
            skip = bool(re.search(r"PART C|Sources", s, re.I))
            continue
        if skip or in_code or re.match(r"^\|\s*S\d+\s*\|", s):
            continue
        if witness and re.match(r"^[-*]?\s*Name or stable handle", s):
            continue        # an identified witness gives their own name here
        for m in TITLE_NAME.finditer(line):
            word = m.group(1)
            if word in ROLE_WORDS or re.fullmatch(INSTITUTION_WORDS + r"s?", word):
                continue
            found.append((i, m.group(0)))
    for i, text in found[:10]:
        r.warn(f"line {i}: possible personal name after a title: \"{text}\" — use the role, not the name")
    if len(found) > 10:
        r.warn(f"... {len(found) - 10} more possible names after a title")


def name_heuristic(body, r, offset=0):
    words = r"(arrested|convicted|charged|accused|fired|sued|indicted|misconduct|abuse|fraud)"
    in_sources = False
    for i, line in enumerate(body.splitlines(), 1 + offset):
        if re.match(r"^#{1,3} ", line.strip()):
            in_sources = bool(re.search(r"PART C|Sources", line, re.I))
        if in_sources:
            continue
        if re.search(words, line, re.I) and re.search(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", line):
            cand = re.findall(r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b", line)
            cand = [c for c in cand if not re.match(r"(The|This|Part|Power|Core|United|Supreme|Consumer|Federal|District|County|City|State|New|North|South|East|West)\b", c)
                    and not re.search(INSTITUTION_WORDS + r"$", c)]
            if cand:
                r.review(f"line {i}: possible personal name near accusation words: {cand[:3]} — roles, not names")


ROW_KEYS = {"authorization": "authorization", "maximum term": "maximum_term", "harm thresholds": "harm_thresholds",
            "stop paths": "stop_paths", "ending plan": "ending_plan", "remedy": "remedy", "data limits": "data_limits",
            "visibility": "visibility", "floors": "floors", "evasion": "evasion"}


def norm_finding(t):
    t = t.strip().lower().replace("_", " ").replace("*", "")
    if t.startswith("not conforming"): return "not_conforming"
    if "not demonstrated" in t: return "not_demonstrated"
    if t.startswith("not applicable"): return "not_applicable"
    if t.startswith("conforming"): return "conforming"
    return None


def check_b4_consistency(pid, sec, fd, r):
    for line in sec.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        key = ROW_KEYS.get(cells[0].lower().replace("*", "").strip())
        if not key:
            continue
        f = norm_finding(cells[-1])
        if f is None:
            if cells[-1]:
                r.err(f"{pid} B4 '{cells[0]}': finding '{cells[-1]}' is not conforming / not conforming / compliance not demonstrated / not applicable")
            else:
                r.warn(f"{pid} B4 '{cells[0]}': finding is empty")
        elif fd.get(key) and fd.get(key) != f:
            r.err(f"{pid}: front-matter finding {key}={fd.get(key)} contradicts B4 table ({f})")
        obs = cells[2] if len(cells) >= 4 else ""
        if obs == "":
            r.warn(f"{pid} B4 '{cells[0]}': Observed is empty (use value [S#], UNKNOWN, or NONE EXISTS)")


def check_registration(fm, body, vocab, r):
    check_versions(fm, r, "registration")
    for k in ("record_type", "record_id", "record_version", "supersedes", "prepared_by",
              "prepared_date", "sources_checked_date", "institution", "adoption_status", "powers"):
        if k not in fm:
            r.err(f"missing field '{k}'")
    rt = fm.get("record_type")
    in_vocab(rt, "record_type", vocab, r)
    in_vocab(fm.get("prepared_by"), "prepared_by", vocab, r)
    in_vocab(fm.get("adoption_status"), "adoption_status", vocab, r)
    rid = str(fm.get("record_id", ""))
    is_example = fm.get("example") is True or rt == "example"
    if is_example:
        if not re.match(r"^SCBP-REG-EXAMPLE-[A-Z0-9-]+$", rid):
            r.err(f"an example record_id must look like SCBP-REG-EXAMPLE-DOMAIN (got {rid!r})")
        if "WORKED EXAMPLE" not in body:
            r.err("an example must carry the WORKED EXAMPLE banner")
    elif "[EX]" in body:
        r.err("[EX] illustrative tags are allowed only in example records (example: true)")
    if not is_example and not re.match(r"^SCBP-REG-(NNNN|\d{4})-[A-Z0-9-]+$", rid):
        r.err(f"record_id must look like SCBP-REG-NNNN-SUFFIX (got {rid!r})")
    base = os.path.splitext(os.path.basename(r.path))[0]
    ver = fm.get("record_version")
    expected = rid if (not isinstance(ver, int) or ver <= 1) else f"{rid}-v{ver}"
    if base != expected and not base.startswith("TEST"):
        r.warn(f"file name '{base}' differs from expected '{expected}'")
    check_date(fm.get("prepared_date"), "prepared_date", r, allow=())
    check_date(fm.get("sources_checked_date"), "sources_checked_date", r, allow=())
    inst = fm.get("institution") or {}
    for k in ("name", "legal_entity", "type", "country", "official_url"):
        if not inst.get(k):
            r.err(f"institution.{k} is empty (use UNKNOWN if not found)")
    if inst.get("type"):
        in_vocab(inst.get("type"), "institution_type", vocab, r, "institution.type")
    if fm.get("prepared_by") == "ai_assisted" and fm.get("ai_tool") in (None, "NONE"):
        r.warn("prepared_by is ai_assisted but ai_tool is NONE")
    powers = fm.get("powers") or []
    if not powers:
        r.err("at least one power must be listed")
    ids = []
    for p in powers:
        pid = p.get("power_id")
        ids.append(pid)
        if not re.match(r"^P\d+$", str(pid)):
            r.err(f"power_id {pid!r} must be P1, P2, ...")
        in_vocab(p.get("category"), "power_category", vocab, r, f"{pid}.category")
        in_vocab(p.get("authority_basis"), "authority_basis", vocab, r, f"{pid}.authority_basis")
        if p.get("uses_force_or_confinement") not in ("yes", "no", "UNKNOWN", True, False):
            r.err(f"{pid}.uses_force_or_confinement must be yes | no | UNKNOWN")
        mp = p.get("minor_power_claimed")
        if mp in ("yes", True) and rt != "authorization":
            r.err(f"{pid}: minor_power_claimed may be yes only in an authorization record")
        if mp in ("yes", True) and p.get("uses_force_or_confinement") in ("yes", True):
            r.err(f"{pid}: a power that uses force or confinement cannot be minor (Core 3.A.4)")
        fd = p.get("findings") or {}
        for row in vocab["requirement_rows"]:
            if row not in fd:
                r.err(f"{pid}.findings.{row} missing")
            else:
                in_vocab(fd[row], "finding", vocab, r, f"{pid}.findings.{row}")
        if not re.search(rf"^## Power {pid}\b", body, re.M):
            r.err(f"no body section '## Power {pid} — ...' for listed power {pid}")
        else:
            sec = re.split(rf"^## Power {pid}\b", body, flags=re.M)[1]
            sec = re.split(r"^## (Power P\d+|PART [C-E])\b", sec, flags=re.M)[0]
            for lab in ("B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"):
                if not re.search(rf"\*\*{lab}\.", sec):
                    r.warn(f"{pid}: section {lab} missing")
            if not re.search(r"Can anything stop this power as a whole\?", sec):
                r.warn(f"{pid}: B5 statement 'Can anything stop this power as a whole?' missing")
            check_b4_consistency(pid, sec, fd, r)
    if len(ids) != len(set(ids)):
        r.err("duplicate power_id")
    try:
        ver = int(fm.get("record_version", 1))
    except (TypeError, ValueError):
        ver = 1
        r.err("record_version must be a whole number")
    if ver > 1:
        sup = fm.get("supersedes")
        if not (isinstance(sup, dict) and sup.get("record_id") and sup.get("record_version")):
            r.err("a version above 1 must state supersedes: {record_id, record_version}")
        if not re.search(r"^## What changed from version \d+", body, re.M):
            r.err("a version above 1 must include '## What changed from version N', quoting every changed or removed passage")
    if rt == "observed" and re.search(r"^## PART E\b", body, re.M):
        r.err("observed record must not contain PART E (commitments only the institution can make)")
    if rt == "authorization" and not re.search(r"^## PART E\b", body, re.M):
        r.err("authorization record requires PART E")
    if not re.search(r"^## PART C\b", body, re.M):
        r.err("PART C — Sources is missing")


def check_response(fm, body, vocab, r):
    check_versions(fm, r, "authority-response")
    for k in ("response_id", "response_to", "response_type", "institution_name", "responder_role", "filed_date"):
        if k not in fm:
            r.err(f"missing field '{k}'")
    in_vocab(fm.get("response_type"), "response_type", vocab, r)
    rt = fm.get("response_to") or {}
    if not (isinstance(rt, dict) and rt.get("record_id") and rt.get("record_version")):
        r.err("response_to must be {record_id, record_version}")
    if not re.match(r"^SCBP-RSP-[A-Z0-9-]+-\d{4}-\d{2}-\d{2}(-[A-Z])?$", str(fm.get("response_id", ""))):
        r.err("response_id must look like SCBP-RSP-SUFFIX-YYYY-MM-DD")
    check_date(fm.get("filed_date"), "filed_date", r, allow=())
    if "does not replace" not in body:
        r.err("a response must carry the banner saying it does not replace the record")
    if fm.get("response_type") in ("correction", "disagreement") and not re.search(r"^\|\s*1\s*\|", body, re.M):
        r.warn("a correction or disagreement should quote the record point by point (section 2 table)")


def check_witness(fm, body, vocab, r):
    check_versions(fm, r, "witness-report")
    for k in ("report_id", "report_type", "record_id", "power_id", "institution_name",
              "incident_date", "filed_date", "location", "identity_disclosure", "status"):
        if k not in fm:
            r.err(f"missing field '{k}'")
    in_vocab(fm.get("report_type"), "report_type", vocab, r)
    in_vocab(fm.get("identity_disclosure"), "identity_disclosure", vocab, r)
    in_vocab(fm.get("status"), "report_status", vocab, r, "status")
    if not re.match(r"^SCBP-WR-[A-Z0-9-]+-\d{4}-\d{2}-\d{2}(-[A-Z])?$", str(fm.get("report_id", ""))):
        r.err("report_id must look like SCBP-WR-SUFFIX-YYYY-MM-DD")
    check_date(fm.get("incident_date"), "incident_date", r, allow=("UNKNOWN",))
    check_date(fm.get("incident_end_date", "NONE"), "incident_end_date", r)
    check_date(fm.get("filed_date"), "filed_date", r, allow=())
    loc = fm.get("location") or {}
    in_vocab(loc.get("precision"), "location_precision", vocab, r, "location.precision")
    for k in ("latitude", "longitude"):
        v = loc.get(k)
        if v in ("UNKNOWN", "WITHHELD"):
            continue
        try:
            fv = float(v)
            if (k == "latitude" and not -90 <= fv <= 90) or (k == "longitude" and not -180 <= fv <= 180):
                r.err(f"location.{k} out of range")
        except (TypeError, ValueError):
            r.err(f"location.{k} must be decimal degrees, UNKNOWN, or WITHHELD")
    if loc.get("precision") == "withheld" and (loc.get("latitude") not in ("WITHHELD", "UNKNOWN")):
        r.err("precision is withheld but coordinates are given")
    sb = fm.get("stop_signal_basis", "NONE")
    in_vocab(sb, "stop_signal_basis", vocab, r)
    if fm.get("report_type") == "stop_signal" and sb == "NONE":
        r.err("a stop_signal report must state stop_signal_basis")
    if fm.get("report_type") != "stop_signal" and sb != "NONE":
        r.warn("stop_signal_basis is set but report_type is not stop_signal")


def main(argv):
    vocab_path = os.path.join(HERE, "VOCAB.yml")
    files = []
    it = iter(argv)
    for a in it:
        if a in ("-h", "--help"):
            print(__doc__)
            return 0
        if a == "--vocab":
            vocab_path = next(it)
        else:
            files.append(a)
    if not files:
        print(__doc__)
        return 2
    vocab = load_vocab(vocab_path)
    print(f"BPF record checker {CHECKER_VERSION} · vocabulary {vocab.get('vocab_version')}")
    any_err = False
    for path in files:
        r = Report(path)
        text = open(path, encoding="utf-8").read()
        # allow a test banner (lines starting with '>') before the front matter
        stripped = re.sub(r"^(>.*\n|\s*\n)+", "", text)
        fm_text, body = split_front_matter(stripped)
        if fm_text is None:
            r.err("no front matter (--- block at top)")
            r.show(); any_err = True; continue
        try:
            fm = yaml.safe_load(fm_text) or {}
        except yaml.YAMLError as e:
            r.err(f"front matter is not valid YAML: {e}")
            r.err("hint: a value that contains a colon (:), a # or brackets must be in double quotes, "
                  "for example  institution_name: \"Example: North Branch\"")
            r.show(); any_err = True; continue
        if fm.get("vocab_version") and str(fm.get("vocab_version")) != str(vocab.get("vocab_version")):
            r.warn(f"record uses vocab {fm.get('vocab_version')}, checker has {vocab.get('vocab_version')}")
        offset = stripped[: stripped.find(body)].count("\n") + (len(text) - len(stripped) and text[: len(text) - len(stripped)].count("\n"))
        if "response_id" in fm:
            check_response(fm, body, vocab, r)
            check_sources(body, r)
        elif "report_id" in fm:
            check_witness(fm, body, vocab, r)
        else:
            check_registration(fm, body, vocab, r)
            check_sources(body, r)
        # Registrations: an unsourced number is an error. Witness reports are
        # often first-hand, so there it is only a warning.
        is_witness = "report_id" in fm
        unsourced_numbers(body, r, as_error=not is_witness, offset=offset, witness=is_witness)
        name_heuristic(body, r, offset=offset)
        title_names(body, r, offset=offset, witness=is_witness)
        for i, line in enumerate(body.splitlines(), 1 + offset):
            if PLACEHOLDER_RE.search(line) and "```" not in line:
                r.warn(f"line {i}: unfilled placeholder: {line.strip()[:80]}")
                break
        r.show()
        any_err = any_err or bool(r.errors)
    return 1 if any_err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
