# Findability

*Background, not rules. How the project aims to stay discoverable and usable without constant promotion or the maintainer's presence.*

---

## What findable means

The project is findable if a person can:

- find it by searching for the problem it addresses;
- read all of it without asking permission;
- check that a copy is the official version;
- understand it without contacting the maintainer.

## What it should not depend on

- continuous promotion or audience-building;
- trust in a particular person;
- a single host or distributor.

Whatever keeps it findable should be low-maintenance, repeatable by others, and able to survive the maintainer's absence.

## How

- **Search.** The repository's name, description, and topics use the words people actually search for. The core documents describe the problem in plain language.
- **Entry points.** The root README and [Start Here](../../00-Reading/00-Start-Here.md) orient a new reader. Other short documents in [00-Reading](../../00-Reading/) give separate ways in.
- **Plain formats.** Documents are Markdown and plain text, so they are easy to read, copy, and reuse.
- **Integrity.** Each published file outside `05-Reference/` has a SHA-256 fingerprint in the hash registry (Core Requirements 6.5). Anyone can check a copy with `sha256sum`. See [05-Maintainer-Resources](../05-Maintainer-Resources/). The registry file is created by the repository workflow on first publication; until then, no fingerprints are recorded.
- **Copies.** The open licences let anyone copy, mirror, or fork the work without permission. No single host is required. The project itself maintains no mirror today ([BPF's own record](../../04-Registry/SCBP-REG-0001-BPF.md), P1 B8).

## Permitted, limited actions

These may be done once or rarely. None of them depends on engagement or growth:

- accurate repository topics and description;
- several short entry-point documents;
- a small number of explanatory summaries;
- an occasional post in a relevant public forum;
- mirrors on other platforms.

## Not used

Marketing, a content schedule, engagement optimization, or audience management. Discovery is started by the reader, not driven by the project.

## Failure modes

| Failure | What limits it |
|---|---|
| The host removes the repository | Copies made by others under the open licences |
| Few people find it | Does not affect whether the framework is sound |
| Altered copies circulate | The hash registry shows which version is official |
| It is misread | Several plain-language entry points |

## Enough

The project is findable enough if a person can find it with relevant search terms, read all of it, check its integrity, and understand its purpose and structure on their own.

*Note: the public location of v1 has not been decided yet.*
