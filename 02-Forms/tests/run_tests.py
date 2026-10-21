#!/usr/bin/env python3
"""Test the BPF record checker against the fictional files in this folder.

Run from anywhere:
    python3 02-Forms/tests/run_tests.py

Rules:
  - every TEST-GOOD-*.md file, and every other .md file here, must pass (no ERROR);
  - every TEST-BAD-*.md file must fail;
  - a file with a line "> Expected error: TEXT" must fail with an ERROR that
    contains TEXT, so each bad file proves the check it was written for.

Exits 0 if every file behaves as expected, 1 otherwise.
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKER = os.path.join(os.path.dirname(HERE), "validate_record.py")


def main():
    files = sorted(glob.glob(os.path.join(HERE, "*.md")))
    if not files:
        print("run_tests: no test files found")
        return 1
    failures = 0
    for path in files:
        name = os.path.basename(path)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        expect_fail = name.startswith("TEST-BAD-")
        expected = re.findall(r"^> Expected error: (.+)$", text, re.M)
        res = subprocess.run([sys.executable, CHECKER, path], capture_output=True, text=True)
        errors = [l.strip() for l in res.stdout.splitlines() if l.strip().startswith("ERROR")]
        problems = []
        if res.returncode not in (0, 1):
            problems.append(f"checker did not run (exit {res.returncode}): {res.stdout.strip()[:200]}")
        elif expect_fail and not errors:
            problems.append("should fail but passed")
        elif not expect_fail and errors:
            problems.append("should pass but failed: " + errors[0])
        for e in expected:
            if not any(e in line for line in errors):
                problems.append(f"expected an ERROR containing {e!r}")
        if problems:
            failures += 1
            print(f"FAIL  {name}")
            for p in problems:
                print(f"      {p}")
        else:
            print(f"ok    {name} ({'fails as expected' if expect_fail else 'passes'})")
    print(f"\n{len(files) - failures} of {len(files)} test files behaved as expected.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
