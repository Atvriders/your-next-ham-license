# Your Next Ham License

*The General Course (2023–2027) · from Technician to worldwide HF · 91,920 words*

> You already hold the Technician license — the General exam is 35 questions drawn
> one per group from a public 423-question pool, and 26 correct answers opens
> worldwide HF: phone and data segments on every HF band, up to 1.5 kW PEP. This
> book teaches the deeper radio behind the questions — then hands you the questions.

A complete upgrade course for the US General class amateur radio license (Element 3,
2023–2027 NCVEC question pool), written for the licensed Technician: it assumes the
Technician course's knowledge — no more, no less — and goes deeper: HF operating,
real AC theory (reactance, impedance, resonance), practical circuits, and antennas
and feedlines at a working level. Eleven chapters walk from what the upgrade opens
through your HF privileges and the rules that come with them, operating on HF,
propagation in depth, station setup and good practice, AC theory, components,
practical circuits, signals and emissions, antennas and feedlines at General depth,
and safety and RF exposure — and every teaching chapter ends with an **Exam Focus**
section quoting the exact pool questions that chapter unlocks, verbatim, with the
keyed answer and a one-line plain-language why. It is **the middle book of the
three-book program** — after *[Your First Ham
License](https://github.com/Atvriders/your-first-ham-license)* (the Technician
course); the Extra course follows the same template.

## What's inside

- **11 chapters** (~49,600 words) — a real upgrade course, not a cram sheet: each
  concept is taught plainly first, then tied to the pool questions it answers. Math
  is expected at this level and taught step by step with worked examples.
- **The exam-focus method** — every one of the **423 active pool questions** is
  answerable after its mapped chapter; the chapter map (canon §5) is the contract,
  and a mechanical audit verifies every quoted question and answer letter against
  the official pool.
- **Appendix A: the complete 2023–2027 pool** — all 423 active questions verbatim
  (the nine withdrawn questions simply do not appear, exactly as the official
  document omits them), choices A–D, correct answer marked, one-line why naming the
  chapter that teaches it.
- **Appendix B: glossary & formulas** — 402 terms in plain language plus the book's
  complete formula set (26 formulas, each with a worked example from the pool's own
  numbers).
- **35 original figures**, including the pool's one official graphic, Figure G7-1,
  redrawn as a clean, themeable SVG.
- **A practice-exam generator** and an **8-voice audiobook** — see below.

## Formats

| File | What it is |
|---|---|
| [`build/index.html`](build/index.html) | The book, typeset as a single self-contained page — linked table of contents, light/dark themes, 35 figures and all math embedded inline. Open it in any browser; it works fully offline. The nicest way to read it. |
| [`build/your-next-ham-license.pdf`](build/your-next-ham-license.pdf) | PDF edition — open in any PDF reader. |
| [`build/your-next-ham-license.txt`](build/your-next-ham-license.txt) | Plain-text edition — open in any editor; math spoken as words, figures as placeholders. |
| [`chapters/`](chapters/) | The 11 source chapters as Markdown (`ch00.md` … `ch10.md`). |
| [`appendices/`](appendices/) | Appendix A ([the complete annotated pool](appendices/pool.md)) and Appendix B ([glossary & formulas](appendices/glossary-and-formulas.md)). |
| Audiobook (release v1.0) | Eight voices, each reading all 11 chapters, plus a spoken introduction — see below. |
| [`Dockerfile`](Dockerfile) / [`docker-compose.yml`](docker-compose.yml) | Serve the book yourself — see below. |

## Read online via Docker

The image packages the book and the audiobook behind nginx, built and pushed to
`ghcr.io/atvriders/your-next-ham-license` by CI on every push to `master`. On any
Docker host:

```sh
docker compose pull && docker compose up -d
```

Serves the book at [http://localhost:8080](http://localhost:8080) and the audiobook
player at `/audiobook/`.

To build locally instead: regenerate the typeset editions, fetch the audiobook from
the release (it is not stored in git), then build the image:

```sh
python3 tools/build_book.py --html --txt --pdf --out build/
# fetch audiobook/ from release v1.0 (see .github/workflows/build.yml for the exact loop), then:
docker build -t ghcr.io/atvriders/your-next-ham-license:latest .
```

## The series site

This book is the second of three to ship (Technician, General, Extra). The repo
carries the machinery for the whole series behind one nginx proxy, runnable today
with the first two books:

```sh
docker compose -f series-docker-compose.yml up -d
```

Serves everything at [http://localhost:8080](http://localhost:8080): a landing page
at `/` with a card per book, the Technician book (text + audiobook) at `/tech/`,
this book at `/general/`, and `/extra/` reserved for the last book — marked "coming
soon" on the landing page and in the book-switcher bar at the top of every page
until it ships. Config lives in [`series/`](series/) (proxy + landing page) and
[`series-docker-compose.yml`](series-docker-compose.yml).

## Audiobook

The audiobook comes in **eight voices** — men and women in **American, British,
Australian, and Irish** accents — each reading all eleven chapters, synthesized with
[edge-tts](https://pypi.org/project/edge-tts/) via
[`tools/make_audiobook.py`](tools/make_audiobook.py) (`--voice <key>` for one voice,
`--all` for every voice) plus a spoken introduction via
[`tools/make_intro.py`](tools/make_intro.py). Formulas and figures are narrated in
words, not read as raw markup. The verbatim pool appendix is print-only and is not
narrated.

All audio is hosted on **release v1.0** rather than committed to git. The player
lives at **`/audiobook/`** in the container: a themed page with continuous
chapter-to-chapter playback, a **voice switcher** grouped by accent, a live
visualizer, **resume** (it remembers your voice, chapter, and position between
visits), and an **Auto-play next chapter toggle** — on by default; switch it off and
playback stops at the end of each chapter.

## Practice-exam generator

Draw a valid practice exam from the pool — exactly one question per NCVEC group, 35
questions, just like the real thing:

```sh
python3 tools/make_exam.py            # random draw
python3 tools/make_exam.py --seed 7   # reproducible draw
```

Writes `build/practice-exam.md` (questions and choices A–D, never the answers —
print it and circle) and `build/practice-exam-key.md` (the answer key with a
subelement tally). Pass `--out` to write elsewhere.

## Practice tests & flashcards

Two interactive study pages, generated from the same canonical pool data and served in
the container at **`/practice.html`** and **`/flashcards.html`** (themed like the
audiobook player, light/dark, fully self-contained — they work offline):

- **`/practice.html`** draws a valid exam — one question per group, 35 questions, 26
  to pass — reseeding with every **New exam** click. Answer by clicking; grading shows
  your score, pass/fail, and a full review list (your answer, the correct answer, and
  the one-line why). A per-subelement **drill mode** gives immediate feedback with the
  why after each question.
- **`/flashcards.html`** flips through all **423 questions**: front is the question and
  choices, back is the correct answer, the why, and a hint naming the published pool
  group and the chapter that teaches it. Filter by subelement, shuffle, and mark cards
  **review later** (persisted in `localStorage`). Keyboard-friendly: space/enter flips,
  arrows move, M marks.

The redrawn pool figure G7-1 appears inline on the five cards and exam questions that
reference it (G7A09–G7A13). Regenerate after any pool update:

```sh
python3 tools/make_study.py --out build/
```

## Pool currency — this pool expires 2027-06-30

**This book tracks the NCVEC 2023–2027 General question pool, valid for exams
2023-07-01 through 2027-06-30 — after that date, exams use the successor pool.** The
book incorporates all six errata issued for this pool (through the 6th, 2026-02-04;
nine questions withdrawn across the six). The next General pool takes effect
2027-07-01; check [ncvec.org](https://ncvec.org/) from December 2026 for the
successor pool. The pool is public domain and is carried verbatim in
[`canon/pool-general.txt`](canon/pool-general.txt) (byte-exact) and
[`canon/pool-general.json`](canon/pool-general.json) (structured), with sha256
hashes and full provenance in [`accuracy-canon.md`](accuracy-canon.md) §1.

When an errata issues — or when the 2027–2031 pool arrives — the swap is contained
by design, because only the pool-facing artifacts change with the pool:

1. Ingest the new pool into `canon/` (new canonical files, sha256s, errata ledger,
   deleted-ID list, ingestion report) and update the canon's revision record.
2. Re-run `python3 tools/audit_book.py` — check #8 mechanically flags every
   chapter/appendix quote and answer letter that drifted, and any coverage gap.
3. Refresh the affected quotes (script-assisted, never retyped), the chapters' Exam
   Focus picks, and Appendix A against the new files; update any FACT lines the
   canon change invalidates.
4. Rebuild. Nothing else changes — notation, glossary, chapter map, teaching prose,
   and figures stand.

Any printing of this book after mid-2027 must state which pool exams actually use.
Fees and other time-sensitive values carry verification dates and re-verify triggers
in the canon (§7.13).

## Development

```sh
python3 -m pytest -q                              # 117 tooling tests
python3 tools/audit_book.py                       # the 8-check accuracy/format/pool gate (exit 0 = green)
python3 tools/build_book.py --html --txt --pdf --out build/   # rebuild the editions
```

The audit is the gate: figure integrity, copyright tags, TOC/anchors, math
rendering, canon cross-check of every `**FACT:**` line, no unresolved uncertainty
markers, format laws, and pool fidelity (every quoted question byte-exact, every
answer letter matching the key, all 423 active questions in Appendix A exactly
once).

## For AI models

[`AI-CONTEXT.md`](AI-CONTEXT.md) is a complete machine-oriented context dump — the
accuracy-canon discipline, pool record (six-errata ledger, nine deleted IDs, the
G7-1 redraw spec), chapter/subelement map, format laws, pool-fidelity rules, figure
pipeline, tooling, series machinery, copyright ledger, resolved uncertainties
(including the 60 m rule change), time-sensitive register, and production history —
sufficient to understand, extend, or adapt the book without contradicting it.

## How it was made

Built by a **multi-agent workflow** over `accuracy-canon.md` — a bible-as-law
accuracy canon carrying the entire 423-question pool verbatim (double-parsed from
the official .docx and .pdf and cross-checked to zero disagreement, with the
six-errata ledger and the nine withdrawn questions cataloged), pinned Part 97 facts,
notation, glossary, the chapter map, and the copyright ledger — reusing the
production machinery of its sibling project, *[Your First Ham
License](https://github.com/Atvriders/your-first-ham-license)*.

| | |
|---|---|
| **Sections** | 13 (11 chapters + 2 appendices) |
| **Words** | 91,920 (49,639 chapters · 33,081 annotated pool · 9,200 glossary & formulas) |
| **Figures** | 35 (all original — hand-authored themeable SVG + matplotlib-plotted curves; the NCVEC pool figure G7-1 redrawn, never copied) |
| **Pool questions annotated** | 423/423 — every active question verbatim, answer keyed, one-line why (six errata incorporated, nine withdrawals omitted) |
| **Agents** | ~45 subagent launches across tooling, canon, figures, chapters, appendix, and audit phases (estimate), plus retries after transient engine errors |
| **Tooling tests** | 117 pytest tests |
| **Audit checks** | 8, including mechanical verbatim-pool verification: 423/423 questions in Appendix A, every quote byte-exact, every answer key matching the pool |
| **Calendar build span** | 2026-07-23 → 2026-07-24, with parallel agents throughout |
| **Subagent tokens** | **~4.1M subagent tokens** (estimate — modeled from agent reads + written volume at ~4 chars/token; this runtime does not meter subagent tokens) |
