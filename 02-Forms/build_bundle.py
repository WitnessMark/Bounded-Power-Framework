#!/usr/bin/env python3
"""Assemble the AI Registration Bundle from its parts. 2026-10-13.

Run from anywhere:
    python3 02-Forms/build_bundle.py

Inputs:
  02-Forms/bundle-core.md, 02-Forms/01-Registration.md, 02-Forms/VOCAB.yml,
  01-Framework/SCBP-04-Core-Requirements.md
Output:
  02-Forms/AI-Registration-Bundle.md

Version stamps ({{BUNDLE_VERSION}}, {{BUNDLE_DATE}}, {{FORM_VERSION}},
{{VOCAB_VERSION}}) are filled from the inputs' own headers, so the version the
AI is told to stamp always matches the bundle.

Options:
    --check   build in memory and exit 1 if the committed bundle differs
              (for CI on pull requests); writes nothing.

Exits with an error, and writes nothing, if an input is missing or a
placeholder is left unfilled.
"""
import os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(H)
CORE_REQUIREMENTS = os.path.join(ROOT, "01-Framework", "SCBP-04-Core-Requirements.md")


def read(path):
    if not os.path.exists(path):
        sys.exit(f"build_bundle: missing input {os.path.relpath(path, ROOT)}")
    with open(path, encoding="utf-8") as f:
        return f.read()


core = read(os.path.join(H, "bundle-core.md"))
form = read(os.path.join(H, "01-Registration.md"))
vocab = read(os.path.join(H, "VOCAB.yml"))
cr = read(CORE_REQUIREMENTS)


# demote headings of embedded documents so the bundle's own structure stays clear
def demote(t):
    out, fence = [], False
    for line in t.split("\n"):
        if line.strip().startswith("```"):
            fence = not fence
        if not fence and re.match(r"^#{1,5} ", line):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def version_of(text, pattern, what):
    m = re.search(pattern, text)
    if not m:
        sys.exit(f"build_bundle: cannot find the {what}")
    return m.group(1)


# Version stamps are read from the inputs, so the bundle cannot drift from them.
# The bundle's own version and date come from its header line.
bundle_version = version_of(core, r"\*Bundle version (\d+\.\d+\.\d+) ·", "bundle version in bundle-core.md")
bundle_date = version_of(core, r"\*Bundle version [\d.]+ · (\d{4}-\d{2}-\d{2})", "bundle date in bundle-core.md")
form_version = version_of(form, r"\*Form version (\d+\.\d+\.\d+) ·", "form version in 01-Registration.md")
vocab_version = version_of(vocab, r"(?m)^vocab_version:\s*([\d.]+)", "vocab_version in VOCAB.yml")
if f"form: {{name: registration, version: {form_version}," not in form:
    sys.exit("build_bundle: the form header and its template 'form:' line give different versions")

for ph in ("{{FORM}}", "{{VOCAB}}", "{{CORE}}", "{{BUNDLE_VERSION}}", "{{BUNDLE_DATE}}"):
    if ph not in core:
        sys.exit(f"build_bundle: placeholder {ph} not found in bundle-core.md")
out = (core.replace("{{BUNDLE_VERSION}}", bundle_version).replace("{{BUNDLE_DATE}}", bundle_date)
           .replace("{{FORM_VERSION}}", form_version).replace("{{VOCAB_VERSION}}", vocab_version)
           .replace("{{FORM}}", demote(form)).replace("{{VOCAB}}", vocab).replace("{{CORE}}", demote(cr)))
if re.search(r"\{\{[A-Z_]+\}\}", out):
    sys.exit("build_bundle: an unfilled {{PLACEHOLDER}} remains")
OUT = os.path.join(H, "AI-Registration-Bundle.md")
if "--check" in sys.argv[1:]:
    current = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
    if current != out:
        sys.exit("build_bundle: AI-Registration-Bundle.md is out of date; run python3 02-Forms/build_bundle.py")
    print("bundle is up to date")
    sys.exit(0)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(out)
print("wrote 02-Forms/AI-Registration-Bundle.md,", out.count("\n"), "lines")
