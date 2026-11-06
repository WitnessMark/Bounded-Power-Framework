# Website

This folder is the project's website, served by GitHub Pages.

| Page | What it is |
|---|---|
| [`index.html`](index.html) | The front page of witnessmark.org: what the framework is, and the three ways in. |
| [`witness-report/`](witness-report/index.html) | A web form for making a witness report. It asks the questions of the [Witness Report form](../02-Forms/02-Witness-Report.md) one step at a time and produces the same report file. |

## How the witness report page keeps its promise

- **Nothing is sent.** The page is one self-contained file. Its security policy blocks every network connection, so it cannot send what is typed, even by mistake. It also works offline: the file can be saved and opened without an internet connection.
- **Nothing is saved.** What is typed lives only in the open page, and is gone when the page is closed. The report is kept only by saving or sending it through the phone's own share menu, or by downloading, copying or printing it.
- **Codes are calculated in the page.** The verification phrase and file fingerprints (SHA-256) are worked out inside the browser. The phrase never appears in the report; a fingerprinted file is read but never attached.
- **The output is checked.** A report made with the page passes the [record checker](../02-Forms/validate_record.py).

## Keeping it in step with the form

The page declares the form, Core Requirements and vocabulary versions near the top of its script. When the Witness Report form changes, the page's questions and those values are changed with it, and a report made with the page is run through the checker.
