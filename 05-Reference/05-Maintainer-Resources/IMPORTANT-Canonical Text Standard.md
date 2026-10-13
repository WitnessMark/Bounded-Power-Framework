# Canonical Text Standard

*Maintainer resource. Supports Core Requirements rule 6.5 (Canonical Integrity).*

Rule 6.5 requires every canonical file to have a publicly recorded SHA-256 fingerprint in the hash registry. The fingerprint is taken over the file's bytes **exactly as stored**. No clean-up is applied before hashing. So a file must already be in canonical form when it is committed. Otherwise an invisible change, such as a line ending or a trailing space, gives a different fingerprint for the same words.

## The standard

Applies to every published text file: Markdown, plain text, YAML, and code.

| Item | Rule |
|---|---|
| Encoding | UTF-8, no byte-order mark |
| Line endings | Unix LF (`\n`) only |
| Indentation | Spaces only, no tabs |
| Trailing spaces | None |
| Quotes | Straight quotes (`"` and `'`) |
| Dashes | Hyphen-minus (`-`) unless a longer dash is intended |
| End of file | Exactly one newline |
| Blank lines | In documents, no more than one blank line in a row. Code follows its language's usual style. |
| Non-printing characters | None, other than the line ending |

## Quick check before committing

1. Save as UTF-8 without a byte-order mark.
2. Use LF line endings.
3. Replace tabs with spaces; remove trailing spaces.
4. Replace curly quotes with straight quotes.
5. Make sure the file ends with one newline.

From the repository root, these commands list files that break the most common rules (each should print nothing):

```
grep -rlI $'\r' --include='*.md' .          # Windows line endings
grep -rlI '[[:blank:]]$' --include='*.md' . # trailing spaces or tabs
grep -rlI $'\t' --include='*.md' .          # tabs
```

## How the fingerprints are made

The hash registry, `00-SCBP-Hash-Registry.txt` in this folder, is regenerated automatically by the repository's "Refresh hash registry" workflow whenever a published file changes. The registry file is created by the repository workflow on first publication; until then, no fingerprints are recorded. Anyone can check a file with:

```
sha256sum FILE
```

A file whose fingerprint differs from the registry is not an official version (6.5). Superseded versions stay public in the repository history.
