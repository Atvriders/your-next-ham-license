# AI-CONTEXT — Your Next Ham License: The General Course (2023–2027)

This document is a complete, machine-oriented context dump for AI models (and humans)
working with this repository. It contains everything needed to understand, extend,
adapt, or continue *Your Next Ham License: The General Course (2023–2027)* without
contradicting the finished book: what the book is and who it is for, the accuracy-canon
discipline, the pool record, the chapter/subelement map, the format laws, the
pool-fidelity rules, the figure pipeline, the tooling, the series-site machinery, the
copyright ledger, the resolved uncertainties, the time-sensitive register, how to
extend the series, and the production history. Treat **`accuracy-canon.md`** (plus its
companion canonical pool files under `canon/`) as law — the published chapters already
conform to it exactly, and this file only summarizes it.

Credentials, API tokens, and personal contact details from the production session are
deliberately omitted.

---

## 1. What this is

*Your Next Ham License: The General Course (2023–2027)* is a **91,920-word** upgrade
course + exam-prep book for the **US General class amateur radio license (Element 3,
2023–2027 NCVEC question pool)**: **49,639 words across 11 chapters** (ch00–ch10:
2,800 / 5,174 / 4,931 / 4,427 / 4,830 / 5,312 / 4,526 / 4,310 / 4,405 / 4,898 /
4,026) plus **2 appendices** (Appendix A, the complete annotated pool, 33,081 words;
Appendix B, glossary & formulas, 9,200 words), with **35 original figures** (one of
them redrawn from the NCVEC pool's single graphic, Figure G7-1).

The audience is the **licensed Technician** upgrading to General — a reader who
already knows Ohm's law, repeater basics, and Part 97 fundamentals. The book assumes
Book 2's knowledge, **no more, no less**: concepts beyond Technician scope are taught
before use; Technician-scope material gets at most a one-line refresher. The book does
two jobs at once: teaches the deeper radio craft the General ticket opens (HF bands,
more power, more modes, real AC theory), and prepares for the exam — after reading a
chapter, the reader can answer every question in its mapped pool subelement. Spine:
*going farther* — the upgrade from local VHF life to worldwide HF: what changes when
your signal can cross oceans, and the deeper theory that makes it work. Math is
expected at this level (reactance, impedance, resonance, dB, power calculations),
taught step by step with worked examples.

This is **the middle book of the three-book "Your First Ham License" program**,
following *Your First Ham License: The Technician Course (2026–2030)*; the Extra
course inherits this book's template. Production machinery (build, audit, figures,
audiobook, Docker, series site) is inherited from the Technician book and
retargeted; new here are the
builder's markdown-table support, the `mathsvg` extension for the real formula set,
ch10 as a full teaching chapter (only ch00 is exempt from Exam Focus), and a messier
pool (six errata, nine deletions, non-contiguous IDs).

## 2. The accuracy canon is LAW

**`accuracy-canon.md`** is the single, binding source of truth for every pool wording,
number, date, notation choice, glossary definition, chapter mapping, and copyright
determination in the book. Where a draft ever disagreed with the canon, the canon won.
**Prose is always original** — facts, 47 CFR Part 97, and the NCVEC pool are public
domain and free to quote; everything else is written fresh.

What the canon pins down (read the file before adding or changing any fact):

- **§1 Pool record** — the canonical pool files and their provenance (§3 below).
- **§2 Pinned facts with sources** — the fact reservoir. Each line is
  `- **FACT:** <one self-contained sentence> — Source: <§ or URL>`. Chapter writers
  copy the sentence **verbatim** (minus the trailing source tag) into their chapters;
  the build audit greps every chapter `**FACT:**` line for an exact match in this file
  (check #5). Rule quotations are verbatim from the **eCFR text of 47 CFR Part 97,
  issue date 2026-07-20** (§97.509 quoted from the 2026-07-22 issue), pulled
  2026-07-24. Where current rule text differs from the pool-era text the 2022 pool
  was written against, the FACT pins the **current** text and §7.1/§7.5 carry the
  difference — the only such hazard areas are 60 m and the HF symbol-rate rules.
- **§3 Notation & Units** — one symbol set (V, I, R, P, f, λ, c, C, L, X, Z, N).
  Prose uses **V** for voltage and **×** for multiplication, exactly as Book 2 does.
  The 2023–2027 General pool states electrical quantities **in words** ("200 volts
  peak-to-peak across a 50-ohm dummy load") — no formula typography occurs anywhere in
  the pool text, so verbatim pool quotes never conflict with the prose convention.
  Unit case is load-bearing (kHz, MHz, mA, µV, pF). The pool's own shortcut
  **λ(m) = 300 / f(MHz)** is taught as an approximation of c = f·λ, never an exact
  identity. Deliberate difference from Book 2, stated openly: **dB = 10·log₁₀(P₂/P₁)
  is first-class exam math here** (pool G5B10, G4D05), not sidebar material.
- **§4 Glossary** — canonical one-line definitions (**402 terms** feed Appendix B).
  Series law: where a term also appears in Book 2's canon, the definition is Book 2's
  **verbatim**; terms new to the General course carry new definitions in the same
  style. A chapter may expand a term but must not contradict it.
- **§5 Subelement → chapter map** — the ownership contract (§4 below).
- **§6 Copyright ledger** — (§9 below).
- **§7 Resolved uncertainties** — every research flag closed to a sourced value or a
  deliberately careful wording (13 subsections; highlights in §10 of this file). **No
  open uncertainty markers remain**; the audit greps for `UNVERIFIED` (check #6).

## 3. The pool record (canon §1)

The 2023–2027 General pool is carried as **canonical files — the only quoting
sources**:

| File | Bytes | sha256 |
|---|---:|---|
| `canon/pool-general.txt` | 119,372 | `4226fcc6502146e714cd516bc2ea3862a524068eb97bbebc76d21e6f4488cbe2` |
| `canon/pool-general.json` | 184,398 | `b6804225ab455f31405298625a741d6f030b479602233c691ba41ba52a9cd373` |

The `.txt` is the byte-exact human-readable rendering (ID lines `G1A01 (C)
[97.301(d)]`, `~~` separators, published headings with their en dashes, the published
tail lines); the `.json` is the structured form (`{id: {group, subelement, question,
choices{A–D}, answer, figure}}`). Question text, choices, and answer letters are
quoted from these two files **only** — never from memory, web mirrors, or study
guides.

Key facts:

- **423 active questions** (432 published IDs minus 9 withdrawn), 10 subelements
  (G1–G9, G0), **35 groups**; every question has exactly 4 choices A–D and one keyed
  answer. **The exam: 35 questions, one drawn from each group; 26 correct to pass**
  (47 CFR §97.503(b)).
- **Valid for exams 2023-07-01 through 2027-06-30. THIS POOL EXPIRES MID-2027.** The
  successor General pool takes effect 2027-07-01 (four-year rotation: Technician
  2026–2030, General 2023–2027, Extra 2024–2028). Every printing, chapter, exam
  product, and web page derived from this book states the 2023–2027 validity window;
  the contained-swap procedure is pinned in canon §7.13 (§11 below).
- **Public domain:** released as such by the NCVEC Question Pool Committee (statement
  on the release page, captured in `canon/source/release-page.html`, fetched
  2026-07-24). Initial release **2022-12-01** (432 questions); the current document
  is the **6th-errata release of 2026-02-04**, whose pool body already incorporates
  every change.
- **Six-errata ledger** (from the document's front-matter errata sheets,
  cross-checked against the release page): Errata 1 (2023-02-01) — 9 questions
  modified, **G9C06, G9D13 withdrawn**; Errata 2 (2023-04-10) — 3 modified, **G6B09
  withdrawn**; 3rd errata (2023-12-01) — FCC rule change, syllabus G1 count 57→55,
  G2E12 answer D modified, **G1C08, G1C10 withdrawn**; 4th errata (2024-03-06) —
  **G1E09 withdrawn**; 5th errata (2024-11-08) — **G8C01 withdrawn**; 6th errata
  (2026-02-04) — **G1A04, G1C09 withdrawn** (the sheet states no reason; the
  rule-change context is the FCC's 60 m amendment — §10.1 below). All twelve
  published text modifications (errata 1–3) were verified present in the final pool
  text byte-exactly during ingestion. **No 7th errata exists as of 2026-07-24.**
- **The nine deleted IDs: G1A04, G1C08, G1C09, G1C10, G1E09, G6B09, G8C01, G9C06,
  G9D13.** Withdrawn **without renumbering** (each printed in the source as `GnX##
  Question Deleted (section not renumbered)`); eight leave a numbering gap, **G9D13
  leaves none** (it was the last question of G9D, which now ends at G9D12). The
  canonical files carry the active pool only; **deleted questions are never quoted,
  taught, or referenced as exam content anywhere in the book** — they appear only as
  numbering gaps and in this ledger.
- **Syllabus reconciliation:** the printed syllabus claims G1:54 (sum 425); the
  parse-authoritative G1 count is **52** — the printed number is stale (not updated
  for the 6th errata's two G1 withdrawals). The parse, not the syllabus, is
  authoritative.
- **Provenance:** downloaded 2026-07-24 from ncvec.org into `canon/source/` (sha256s
  in canon §1.2, including the 5th-errata release kept as the pre-6th baseline — it
  differs from the 6th only by the removal of G1A04 and G1C09, zero content
  differences among the 423 common questions). Parsed from the `.docx`
  (authoritative; python3 `zipfile` + `ElementTree`, no third-party packages) and
  independently re-parsed from the `.pdf` with `pdftotext -layout`; the two agreed on
  all 423 questions, all 1,692 choices, all answer letters, all Part 97 refs, and all
  45 headings except one PDF-side line-wrap artifact (G1A06 "24- hour" — the
  canonical files carry `24-hour`). ARRL hosts no separate copy of this pool (its
  question-pools page links back to NCVEC), so the docx-vs-pdf double parse is the
  cross-check of record. Full evidence in `canon/ingestion-report.md`.
- **Published quirks are preserved, never repaired:** the `G9C01 (A) ` ID-line
  **trailing space**; G2E02's choice D printed as `D.A DX spotting system …` with
  **no space after the label**; the citation misprints **G1D12 `[97.507]`** and
  **G1B05 `[97.111((5)(b)]`** (operative citations in §10.6 below); published Unicode
  punctuation preserved byte-exactly (en dash U+2013 ×55, curly apostrophe U+2019
  ×49, curly quotes U+201C/U+201D ×51 each — the only non-ASCII characters in the
  pool text). The only whitespace normalization applied anywhere is one stripped
  leading tab (G4E11 choice B — indentation, not content).
- **Pool figure G7-1 (5 questions):** the pool ships a single graphic, referenced by
  G7A09–G7A13 (three print "figure G7-1" lowercase, two "Figure G7-1" capitalized —
  the case difference is published and preserved). The book **redraws it as an
  original SVG conveying exactly the official content — same components, same labels,
  same numbered callouts — never copies the published graphic** (§6 below); canon
  §1.4 carries the binding redraw specification: a two-stage circuit (a
  varactor-tuned FET oscillator feeding an NPN amplifier/buffer) with 11 numbered
  symbols — 1 FET (asked by G7A09), 2 NPN (G7A11), 3 plain diode, 4 varactor, 5
  Zener (G7A10), 6 solid-core transformer (G7A12), 7 tapped inductor (G7A13), 8/10
  electrolytics, 9 fixed resistor, 11 variable resistor — and **every ground symbol
  drawn as three slanted strokes of decreasing length** (the same style as Book 2's
  T-1/T-2/T-3 redraws).

## 4. Chapter / subelement map (canon §5)

One subelement per chapter, G1→ch01 … G0→ch10, with ch00 the upgrade welcome. Every
one of the 423 pool questions is answerable after its mapped chapter; a chapter
teaches its subelement, and only that chapter quotes those questions in its Exam
Focus.

| Chapter | Title | Pool subelement | Groups owned | Pool questions | Exam questions |
|---|---|---|---|---:|---:|
| ch00 | The Upgrade: Why General, and How This Book Works | — (upgrade logistics, canon §2.4) | — | — | — |
| ch01 | Your HF Privileges & the Rules That Come with Them | G1 | G1A–G1E | 52 | 5 |
| ch02 | Operating on HF | G2 | G2A–G2E | 60 | 5 |
| ch03 | Propagation in Depth | G3 | G3A–G3C | 37 | 3 |
| ch04 | Station Setup & Good Practice | G4 | G4A–G4E | 60 | 5 |
| ch05 | AC Theory: Reactance, Impedance, Resonance | G5 | G5A–G5C | 40 | 3 |
| ch06 | Components & Devices | G6 | G6A–G6B | 23 | 2 |
| ch07 | Practical Circuits | G7 | G7A–G7C | 38 | 3 |
| ch08 | Signals & Emissions | G8 | G8A–G8C | 42 | 3 |
| ch09 | Antennas & Feedlines at General Depth | G9 | G9A–G9D | 46 | 4 |
| ch10 | Safety & RF Exposure at General Depth | G0 | G0A–G0B | 25 | 2 |
| Appendix A | The Complete 2023–2027 General Question Pool | all 423 verbatim + one-line why | all 35 | 423 | 35 |
| Appendix B | Glossary & Formulas | — (canon §3, §4) | — | — | — |

Binding notes:

- **ch00 teaches no pool questions** — it covers the upgrade logistics of canon §2.4
  (Element 3, CSCE, §97.9(b) immediacy with the /AG indicator, fees and the upgrade
  exemption, what General opens, what's next) and carries the "checklist" adaptation
  of the format laws (no Exam Focus; the audit enforces this).
- **Figure G7-1 belongs to ch07** (group G7A); its five figure questions
  (G7A09–G7A13) appear in ch07's Exam Focus.
- **ch10 treats G0A and G0B as separate sections** — RF-exposure/MPE material and
  shop/tower safety share no concepts.
- **ch09 carries the single Smith-chart sidebar** (§10.5 below): brief, "what a
  Smith chart shows," no exam weight, no dedicated figure.

## 5. Format laws

### 5.1 Chapter skeleton (audit check #7)

Every teaching chapter (ch01–ch10) follows one fixed skeleton so parallel writers
produce one coherent book:

1. First line exactly `## <N>. <Title>`.
2. **Opener** — one short plain-language paragraph (a concrete upgrade scenario plus
   "in this chapter you'll learn …").
3. **Teaching sections** (`### …`) — plain language, figures as `{{fig:id}}` on their
   own line, inline math `$…$` only where needed; optional
   `> **The math, if you want it:**` sidebars for anything beyond the main line.
4. **≥1 `> **Worked example:**` blockquote** — **a real calculation worked end to end
   with pool-relevant numbers** (reactance, resonance, dB, SWR, impedance);
   arithmetic-only is a defect at this level.
5. **`### Exam Focus`** — opens with the coverage line (subelement, groups, question
   counts, exam weight), then 5–10 verbatim pool questions with correct answer and a
   one-line plain-language why (quote format in §5.4).
6. **`### Key Takeaways`** — 4–8 bullets.
7. **3–5 `**FACT:** <sentence>` lines** as standalone plain paragraphs (never inside
   blockquotes — the audit's FACT regex won't see them there), copied **byte-exact**
   from `accuracy-canon.md`.

**Only ch00 is exempt** from the Exam Focus / worked-example rules — a deliberate
change from Book 2, which exempted ch00+ch10: here **ch10 owns subelement G0 and is a
full teaching chapter**. ch00 gets the "Your upgrade checklist" adaptation. Banned
phrases everywhere: *"little did they know"*, *"in that moment"*, *"a testament
to"*. Nonfiction integrity: no fabricated quotations; anecdotes are plainly framed as
illustrative scenarios, never attributed to real people. Depth law (span-auditor
enforced): assumes Book 2 knowledge — no more, no less; G5/G6/G7 are the risk
chapters.

### 5.2 Appendix A format (audit check #8 parses this exactly)

All 423 active questions, exactly once each, in canonical pool order (subelements
G1…G9 then G0; group A–F; ascending number, **skipping the nine deletions** — the
audit's `pool_sort_key`). One `###` section per subelement with the published title
and counts; optional `####` group lines. Every entry is one blockquote in exactly
this shape, followed by one plain line carrying the published ID line:

```
> **G1A01** <question text, verbatim from the pool>
> A. <choice text, verbatim>
> B. <choice text, verbatim>
> C. <choice text, verbatim>
> D. <choice text, verbatim>
> **Answer: C** — <one-line why, naming the teaching chapter: "… — taught in chapter 1.">

Published ID line: `G1A01 (C) [97.301(d)]`
```

The published ID line rides on a **separate plain-text line after the blockquote, in
backticks** — never inside the quote itself (the audit would read it as part of the
question text). The ID lines preserve the published citation quirks verbatim:
G1D12's `[97.507]`, G1B05's `[97.111((5)(b)]`, G9C01's trailing space. The redrawn
Figure G7-1 is embedded on the line before its first referencing quote and named
thereafter. The appendix was assembled from **per-subelement fragments**
(`appendices/pool-fragments/G1.md` … `G0.md`) concatenated in canonical order; every
quote was **script-extracted** from the canonical files, never hand-typed. Appendix A
is **print-only — never narrated** in the audiobook (decision carried from Book 2).

### 5.3 Appendix B format

Glossary as a **two-column pipe table** (402 terms, the canon's §4 definitions
verbatim) — which **renders as a real HTML table** in this book (see the builder's
new table support, §7 below) — then the formula set: **26 formulas** (the General
set — reactance, resonance, impedance magnitude/phase, power forms, RMS/peak/
peak-to-peak, PEP, decibels, SWR, dipole/monopole lengths, dBi/dBd, Carson's rule,
deviation through a multiplier chain, transformer ratios, series/parallel
combinations, and the Book 2 carry-overs such as Ohm's law, the wavelength shortcut,
and the prefix ladder), each with a plain statement and one worked example using the
pool's own numbers, plus a notation-and-units subsection (V/× prose convention, unit
case, c, f = 1/T, the hobby's customary units).

### 5.4 Build-dialect constraints (what `tools/build_book.py` actually parses)

The builder parses a small fixed markdown dialect; writers must stay inside it:

- **Consecutive non-blank lines join into one paragraph.** Therefore bullets (Key
  Takeaways, checklists) are **blank-line-separated** — each `-` item stands alone
  between blank lines, or the parser would merge them into a single paragraph.
- **A blockquote is consecutive `>` lines joined with spaces.** The six-line Exam
  Focus / Appendix A quote block works because of this; any `>` line directly
  adjacent to it would be absorbed into the same block. Blockquote classes: a quote
  starting `**The math, if you want it:**` renders as a sidebar; `**Worked
  example:**` as a worked example; anything else as a plain quote.
- **Inline math is `$…$`, rendered to SVG at build time** (`tools/mathsvg.py`). Keep
  it to **at most one `$…$` span per paragraph** and never use a literal `$` (e.g.
  "$35") inside a math paragraph — write "35 dollars" in prose. For this book the
  renderer's subset was **extended** to cover the General formula set: subscripts
  ($X_L$), $\pi$, $\sqrt{}$, and fractions.
- **Pipe tables are supported (new in this book):** consecutive `| … |` lines whose
  second line is a `|---|`-style separator parse as a table and render as a real
  `<table class="md-table">`; lines that fail the separator test fall back to the old
  join-into-paragraph behavior. This exists so Appendix B's 402-row glossary renders
  as a table — Book 2's builder lacked it and shipped its glossary as one joined
  paragraph.
- Figures are `{{fig:id}}` on their own line, resolved against `figures/figures.json`;
  `***` is a section rule; `####` headings render as anchored `<h4>`s (Appendix A
  group headings) and never enter the TOC; emphasis is `**bold**` / `*italic*`.
- The audit's Exam Focus quote regex (`> **G#X##** <text>` + `**Answer: L**`) is the
  exact contract for every pool quote in chapters and appendices.

## 6. Figures

**35 original figures** (`figures/figures.json` is the registry — a dict keyed by
figure id; `figures/*.svg` the assets — one SVG per registry entry). Distribution:
ch00:2, ch01:3, ch02:3, ch03:4, ch04:3, ch05:6, ch06:1, ch07:4, ch08:3, ch09:4,
ch10:2.

- **Hand-authored themeable SVG schematics/diagrams** using `currentColor` so they
  render correctly in both light and dark themes — e.g. `ch01-general-band-chart.svg`,
  `ch01-60m-structure.svg`, `ch04-grounding-bonding.svg`, `ch09-yagi-stack.svg`.
- **Matplotlib-plotted curves**, generated by paired `_gen_<id>.py` scripts, committed
  as static SVG and **post-processed black → `currentColor`** — e.g.
  `ch05-reactance-curves.svg`, `ch05-resonance-curves.svg`, `ch08-digital-waterfalls.svg`.
- **The NCVEC pool figure G7-1 redrawn as an original SVG** (`ch07-pool-fig-g71.svg`):
  same components, same labels, same numbered callouts as the official diagram —
  never a copy of the published graphic. Registered as `kind:"original"` with the
  source note "redrawn from NCVEC pool figure G7-1"; canon §1.4 is the binding
  component-by-component redraw specification (§3 above). The pool is public domain,
  so this is both safe and faithful; the redraw rule keeps the book's visual style
  consistent and themeable.

Every registry entry carries id, chapter, number (in **first-reference order within
each chapter** — never authoring order, so late insertions don't scramble the book),
caption, kind, source, file, and a one-line **spoken** description (used by the
narration transform so figures degrade gracefully in audio). Every figure is embedded
inline in the built HTML. `figreg`'s `validate()` enforces existence, copyright tags,
and the protected-years rule, and the audit checks figure integrity (#1) and
copyright tags (#2) at build time.

## 7. Tooling inventory

All Python 3, stdlib-first (`matplotlib` for plots, `edge-tts` + `ffmpeg` for audio,
headless Chromium/Chrome → weasyprint for best-effort PDF). Every runnable script
keeps the repo-root `sys.path` bootstrap so it works both as `python3 tools/<x>.py`
and as an imported module.

- **`tools/build_book.py`** — parses the fixed dialect and produces the self-contained
  single-file **HTML** edition (inline SVG figures, inline math SVG, linked TOC,
  light/dark themes, **series book-switcher bar**, no external references), the plain
  **TXT** edition (math spoken as words, figures as `[Figure: ID]`), and the
  best-effort **PDF** (probe order chromium/chromium-browser/google-chrome/
  google-chrome-stable → weasyprint → skip). Also holds `SERIES_BOOKS` /
  `SERIES_CURRENT` (§8). **New in this book: markdown pipe-table support** — the
  402-row glossary in Appendix B renders as a real table, unlike Book 2's shipped
  join-into-paragraph rendering.
- **`tools/audit_book.py`** — the verification gate; exits non-zero on any failure.
  **8 checks:** (1) figure integrity, (2) copyright tags, (3) TOC/anchor consistency,
  (4) math rendering (every `$…$` span renders), (5) canon cross-check of every
  `**FACT:**` line, (6) no `UNVERIFIED` markers left in the canon, (7) format laws
  (skeleton + banned phrases; **only ch00 exempt**), (8) **pool fidelity** — see
  §7.1.
- **`tools/mathsvg.py`** — inline `$…$` → embedded SVG; **extended for this book**
  with subscripts, `\pi`, `\sqrt{}`, and fractions so the whole General formula set
  renders (audit check #4 is the backstop).
- **`tools/figreg.py`** — loads/validates `figures/figures.json`; protected-years set
  (1968–1983), unchanged from the series' original ledger.
- **`tools/narration.py`** / **`tools/make_audiobook.py`** — the 8-voice edge-tts
  audiobook pipeline (US/British/Australian/Irish × male/female), **preface +
  chapters 00–10 only** (the verbatim pool appendix is never narrated); ID3
  `artist=Kimi K3`, `album=Your Next Ham License`. `docker/audiobook-index.html`
  is the player (§8).
- **`tools/make_exam.py`** — the practice-exam generator:
  `python3 tools/make_exam.py [--seed N] [--out build/] [--pool canon/pool-general.json]`
  draws exactly **one question per NCVEC group** (35 groups → a valid 35-question
  exam), uniform random within group, reproducible with `--seed`; writes
  `build/practice-exam.md` (questions + choices A–D, **never the answers**) and
  `build/practice-exam-key.md` (letters + subelement tally). The group model
  **tolerates the deleted-ID gaps** — one uniform-random draw per group from whatever
  ids exist.
- **`tests/`** — **128 pytest tests** covering all tooling (including the four
  check-#8 fixture tests: a correct quote passes; a one-word-off quote fails; a wrong
  answer letter fails; missing pool → skip — with a pool fixture that carries a
  **deleted-ID gap** so the coverage check is proven to tolerate non-contiguous
  numbering) plus a relative-links test on the built HTML.

### 7.1 Pool-fidelity rules (audit check #8)

- Question text, choice text, and answer letters are quoted **byte-exact** from
  `canon/pool-general.*` (the audit compares whitespace-normalized against the
  `.json`). Published Unicode punctuation is preserved; never paraphrase a question;
  never retype pool text by hand — quotes are pulled from the canonical files with
  script assistance.
- Every quoted id must exist in the pool; every stated choice line and answer letter
  must match the pool key; Appendix A must contain **all 423 active ids exactly once,
  in canonical pool order**, skipping the nine deletions exactly as the canonical
  files do. The audit mechanically verifies 423/423 coverage, every quote, and every
  letter — it is the backstop that makes silent pool drift impossible.
- The **fully-errata'd 6th-errata form** is the only form used — the canonical files
  already carry it; quote, don't retype.
- The published quirks are reproduced as published in every quotation, never
  silently repaired: **G9C01's ID-line trailing space**, **G2E02's `D.A` choice
  label** (no space after the label), and the **G1D12 `[97.507]` / G1B05
  `[97.111((5)(b)]` citation misprints** on the Published ID lines (chapters cite the
  operative rules when explaining — §10.6).
- The nine deleted questions are never quoted; Appendix A's coverage simply skips the
  deleted numbers.
- Check #8 **skips gracefully** (printed note, not failure) when the pool JSON is
  absent, so the audit still gates a bare scaffold.

## 8. Series-site machinery

The book is one of three in the *Your First Ham License* series (Technician / General
/ Extra) and carries the shared machinery. **This book ships with General live**:
Technician stays live, Extra remains "coming soon."

- **Book-switcher bar** — a slim series bar in both the generated book HTML
  (`tools/build_book.py`, driven by `SERIES_BOOKS = [("Technician","/tech/",True),
  ("General","/general/",True), ("Extra","/extra/",False)]` and `SERIES_CURRENT =
  "General"`) and the audiobook player. Shipped books are links, current book
  highlighted, unshipped books render as inert "coming soon" labels. General's flag
  flips to `True` in this repo (inert until push; the book is live the moment it
  ships); Extra flips when the Extra book ships.
- **Stable sub-paths** — the books mount at `/tech/`, `/general/`, `/extra/` behind a
  series nginx proxy. **Book HTML uses only relative/anchor links** (enforced by a
  build test; the only absolute links allowed are the three series paths), so
  sub-path proxying needs no response rewriting.
- **`series/`** — `series/nginx.conf` (proxy: `=` `/` → landing page; `/tech/` → the
  tech container, active; `/general/` → the general container, **active — this
  book**; the `/extra/` block commented out until that book ships),
  `series/index.html` (the landing page: three cover-style cards — Technician
  **live**, General **live + current highlight**, Extra "coming soon").
  **`series-docker-compose.yml`** wires the book images plus the proxy (the only
  published port, host :8080); tech and general services are live (General dropped
  the `future` profile), extra stays behind the `future` profile so `up` never pulls
  a placeholder. Each book's standalone image (`docker-compose.yml`, also :8080) runs
  fine alone.
- **Audiobook player** (`docker/audiobook-index.html`) — themed page with 12 tracks
  (preface + 11 chapters), a **voice switcher** grouped by accent (8 voices: Andrew,
  Ava, Ryan, Sonia, William, Natasha, Connor, Emily), continuous chapter-to-chapter
  playback, a live visualizer, and **resume** (voice/track/position persisted in
  `localStorage` under **`ynhl-audio`** — this book's key; Book 2's player uses
  `yfhl-audio`). The **"Auto-play next chapter" toggle** (default ON, persisted
  alongside; when OFF, playback stops at each chapter end) is kept from Book 2 — the
  `ended` handler auto-advances only when the toggle is on.
- **Hosting/CI** — `Dockerfile` (nginx serving `build/index.html`, the TXT/PDF,
  `chapters/`, and `audiobook/` with the player at `/audiobook/`); GitHub Actions
  (`.github/workflows/build.yml`, push to `master`/`main` or `workflow_dispatch`)
  fetches the audiobook from **release v1.0** (8 voices × 12 tracks — preface +
  11 chapters; the
  fetch loop stays `seq -f "%02g" 0 10`), rebuilds the book, and pushes
  `ghcr.io/atvriders/your-next-ham-license:latest`. GitHub-only CI; no Gitea path.
  **Audio ships on the release, not in git.**

## 9. Copyright ledger summary

- **Prose is always original.** Nothing is copied from any study guide, handbook, or
  web page.
- **47 CFR Part 97 is public domain** (US Government work, 17 U.S.C. §105) and is
  quoted verbatim with section pinpoints (eCFR issue date 2026-07-20; §97.509 from
  the 2026-07-22 issue).
- **The NCVEC 2023–2027 General pool is public domain** (released as such by the
  NCVEC Question Pool Committee; statement captured in
  `canon/source/release-page.html`, fetched 2026-07-24): questions, choices, answer
  keys, and figure *content* may be reproduced verbatim.
- **The pool figure G7-1 is redrawn, not copied** (§6).
- **Bare facts, frequencies, and formulas are not copyrightable**; all exam-prep
  explanations are written fresh.
- **ARRL Handbook ledger (carried over from the series' original canon, governs any optional archival
  figure):** of the 13 owned editions (1927–1983), **7 are public domain and
  reproducible** (1927, 1931, 1933, 1936, 1940, 1941, 1951 — each affirmatively
  evidenced) and **6 are protected and never reproduced in any form** (1968, 1974,
  1976, 1977, 1981, 1983). `figreg.validate()` mechanically rejects any figure tagged
  with a protected-year source. This book ships with **zero archival images** — every
  figure is original.

## 10. Resolved uncertainties — the headline rulings (canon §7)

Every research flag was closed to a sourced value or a deliberately careful wording
(13 subsections in the canon). The rulings a future editor must not undo:

### 10.1 The 60 m rule change (91 FR 1430) — the pool is older than the rule

The FCC's WRC-15 Report & Order (WT Docket 23-83, FCC 25-60, adopted 2025-09-23,
released 2025-12-09, published as 91 FR 1430 on 2026-01-14) replaced the channelized
60 m rules the 2022 pool was written against. **Current text** (verified 2026-07-24
against the eCFR, issue date 2026-07-20): amateurs may transmit (1) anywhere in the
contiguous **5351.5–5366.5 kHz** segment at **9.15 W ERP**, and (2) on **four** of
the five old channels — **5332, 5348, 5373, 5405 kHz** — at **100 W ERP**; the ≤ 2.8
kHz bandwidth cap now applies to all 60 m spectrum (§97.303(h)(3)); the non-dipole
antenna-gain record requirement survives verbatim (§97.313(i)). The NCVEC's 6th
errata already withdrew the two conflicted questions (**G1A04**, **G1C09**); G1C03
(2.8 kHz) and G1C04 (gain records) survive literally correct — only their provisions
moved (the pool prints the superseded cites `[97.303(h)(1)]` and `[97.303(i)]`).
**Binding:** chapters cite the CURRENT sections (§97.303(h)(3), §97.313(i)) when
explaining these answers, teach the two-part structure (segment plus four channels,
two power limits, USB phone, 2.8 kHz maximum bandwidth), and drill the pool's keyed
answers exactly as published. **No prose may describe 60 m as "five channels, USB
only, 100 W ERP" — that rule is dead.**

### 10.2 Upgrade immediacy — §97.9(b) plus the /AG indicator

A Technician who passes Element 3 and properly submits Form 605 to the administering
VEs may exercise General privileges **immediately** — "until final disposition of the
application or until 365 days following the passing of the examination, whichever
comes first" (§97.9(b)) — appending the indicator **AG** to the call sign
(§97.119(f)(2)), separated by the slant mark or any suitable word (§97.119(c)); in
one VEC's practice, say "temporary AG" on phone and sign call/AG on CW or digital,
dropping the suffix once ULS shows General (Laurel VEC FAQ; pool G1D06). Contrast
with Book 2's new-license readers: a first-time licensee has NO authority until the
grant appears in ULS. **Wording law (binding): never write "transmit as soon as you
pass" without both conditions (Form 605 properly submitted to the VEs + CSCE in
hand) and the /AG identification requirement in the same breath.**

### 10.3 The three sideband conventions

- **Voice:** LSB below 10 MHz (160, 75, 40 m), USB at 10 MHz and above — convention,
  not law or physics.
- **AFSK RTTY → LSB** (pool G2E01); stated as practice only, no origin story.
- **JT65/JT9/FT4/FT8 → USB on EVERY band**, including 80 and 40 m where voice is LSB
  (pool G2E05; WSJT-X manual).
- **60 m phone is USB** — the one band where sideband was written into the rule.
- **Anti-shorthand law:** never teach "LSB below 14 MHz." The boundary is 10 MHz;
  30/17/12 m are USB.

### 10.4 Symbol-rate rules changed after the pool was written

The FCC's December 2023 Order (88 FR 85127) replaced the HF symbol-rate limits with a
**2.8 kHz authorized-bandwidth standard**: §97.307(f)(3) now imposes the bandwidth
standard below 28 MHz, the 300-baud limit survives only for 2200 m/630 m, and (f)(4)
is Reserved. Verified by full-text search of the pool JSON: **no active question
tests maximum symbol rate**. Chapters teach the current 2.8 kHz standard and never
resurrect 300 baud as an exam fact.

### 10.5 Smith chart — one sidebar, no exam weight

Zero pool questions test the Smith chart (the 2023–2027 revision dropped the old
Smith-chart items). The book keeps **ONE brief "what a Smith chart shows" sidebar in
ch09, with no exam weight and no dedicated figure**; the glossary carries one
orientation entry so the sidebar and Appendix B stay consistent.

### 10.6 Pool citation defects — preserved, not propagated

- **G1D12 prints `[97.507]`** — an apparent misprint (§97.507 is "Preparing an
  examination"). The keyed answer rests on territorial jurisdiction (§97.301
  preamble); the ID line is preserved verbatim and chapters cite the §97.301
  preamble when explaining.
- **G1B05 prints `[97.111((5)(b)]`** — malformed (double open-paren). The operative
  Morse-practice permission is codified in the §97.111(b) list in current numbering;
  the ID line is preserved verbatim and chapters cite §97.111(b).

### 10.7 The remaining resolutions (canon §7.7–§7.12), in one line each

- **§7.7 Ingestion flags:** the stale syllabus count (§3 above); G1A06 carries
  `24-hour` (docx authoritative); no ARRL mirror exists — the docx-vs-pdf double
  parse is the cross-check of record; published quirks preserved verbatim; no 7th
  errata as of 2026-07-24; the 5th-vs-6th cross-check shows zero content differences
  among the 423 common questions.
- **§7.8 Other post-pool Part 97 amendments** (90 FR 57712; 88 FR 21451; 89 FR
  65223): zero General answer impact; the §2.4 VEC FACT cites §97.521 with the (b)
  reservation noted.
- **§7.9 Practice-not-rule answers:** G1E10's five beacon frequencies are the
  NCDXF/IARU network — good practice under §97.101(a), not a Part 97 set-aside (the
  only automatic-beacon segment Part 97 designates is 28.20–28.30 MHz, §97.203(d));
  G1B02's "National Beacon Organization" distractor is fictional and chapters say so;
  G1E06 (ITU Region 2) rests on the Note to §97.303; the auto-beacon segment and the
  beacon-network frequencies are kept apart (G1B09 vs G1E10); the G1D05/G1D12
  asymmetry is taught as a pair; G1E02 — privileges follow the repeater's control
  operator.
- **§7.10 Teaching watch items:** "All these choices are correct" is keyed 7 times
  and a distractor at least 7 more — chapters teach content, never pattern-guessing;
  G5B10 gets the full 10^(−0.1) = 0.794 derivation; G5C08's keyed answer prints
  "10.750 nF" with the trailing zero, reproduced exactly; G4D08's LSB example
  cross-references ch01↔ch04; the numbering gaps (§3) are errata deletions — never
  hunt for or quote them.
- **§7.11 Operating watch items:** FT8 clock tolerance is the pool's "about 1
  second," never ARRL's "within 2 seconds" as the exam number; net frequencies
  (14.300, 14.325/7.268) are centers of activity by long custom under §97.101(b),
  never "the emergency frequency"; contest "59(9)" is a fixed formality vs everyday
  honest reports — teach both; QRP ~5 W is club/award custom, not regulation; bureau
  fees are pinned "as of 2026-07-24" or omitted.
- **§7.12 Book 2 wording laws, adopted unchanged:** grant timing is "your ULS record
  typically updates within days," never a promised day count; remote exams are never
  promised — availability is the VE team's call; CORES/FRN registration "carries no
  fee and no exam requirement," never "free of charge"; Laurel VEC is larc-vec.org
  (laurelvec.com 307-redirects there).

## 11. Time-sensitive register (canon §7.13)

Each value is pinned in the canon with its verification date (**all verified
2026-07-24**, except the Laurel address 2026-07-23) and must be **re-verified at the
stated trigger before any reprint or new edition**:

| Item | Pinned value | Re-verify trigger |
|---|---|---|
| **Pool currency (the big one)** | 2023–2027 General pool valid for exams 2023-07-01 → **2027-06-30**; 6th errata (2026-02-04) incorporated; no 7th errata | Each reprint; **check ncvec.org from December 2026 for the 2027–2031 successor pool** (expected late 2026 by analogy with the Technician cycle, but never print a release date as fact) |
| FCC application fee | $35 (new license, renewal, rule waiver, vanity), effective 2022-04-19; **upgrades EXEMPT** | Before each reprint (fees change by FCC fiscal-year order) |
| ARRL VEC exam fee | $15.00 per session; $5.00 under 18 (calendar-2026 figure) | Each January |
| NCVEC Form 605 | 2022 edition | Before publication and each reprint |
| Part 97 rule text | eCFR issue date 2026-07-20 (§97.509 from the 2026-07-22 issue); includes the 60 m amendment 91 FR 1430 | Re-pull every cited section before any reprint |
| FT8 watering-hole frequencies | HF list per canon §2.5 (ARRL OTA table); 6 m/60 m per OnAllBands/DX Engineering table | Before print, against the current WSJT-X default frequency table and ARRL |
| ISS SSTV | 437.550 MHz, Robot36 mode | Close to print, against ariss.org / AMSAT news |
| Net schedules | MMSN 14.300 MHz daily 12:00–22:00 ET; HWN 14.325 MHz day / 7.268 MHz night | Close to print |
| QSL bureau rate | $3.00 for 1–10 cards (ARRL Outgoing QSL Service) | Before print — or describe the process without prices (§10.7) |
| Laurel VEC web address | https://larc-vec.org/ (laurelvec.com 307-redirects there) | Before each reprint |

**Contained-swap procedure for the 2027–2031 pool (binding, canon §7.13):** the
book's teaching content is durable by design — only the pool-facing artifacts change
with a new pool. On release of the successor pool: (1) ingest it into `canon/` with a
new ingestion report (new canonical files, sha256s, errata ledger, deleted-ID list);
(2) update the canon's §1 (files, counts, validity window) and any §2 FACT or §7
resolution whose rule or frequency changed; (3) refresh each chapter's Exam Focus
question picks and Appendix A's verbatim pool against the new canonical files; (4)
re-run the build audit and the full test suite to green; (5) nothing else changes —
notation, glossary, chapter map, teaching prose, and figures stay as pinned. **Any
printing of this book after mid-2027 must state which pool exams actually use.**

## 12. How to extend

**The Extra book** inherits this template end to end (the current Extra pool is
effective 2024-07-01, valid until 2028-06-30):

1. Copy the repo scaffold: `tools/`, `tests/`, Docker/CI, `series/` machinery,
   `docker/audiobook-index.html` — retarget constants (titles, `SERIES_CURRENT`,
   image names, chapter count in the CI audio-fetch loop, the player's `localStorage`
   key).
2. Ingest the current Extra pool into `canon/pool-*.txt/json` (same double-parse
   discipline; record sha256s and provenance in the new canon).
3. Rebuild `accuracy-canon.md` for that pool (pinned facts, notation, glossary,
   chapter map); write chapters against the same format laws; the same 8-check audit
   gates everything, including check #8 against the new pool.
4. Flip Extra's flag in `SERIES_BOOKS`, uncomment its block in `series/nginx.conf`,
   and drop its `future` profile in `series-docker-compose.yml` when it ships.

**A pool swap within this book** (an NCVEC errata, or the 2027–2031 pool): follow the
contained-swap procedure in §11 — replace the `canon/pool-general.*` pair, update the
canon, re-run `python3 tools/audit_book.py` (check #8 mechanically flags every
chapter and appendix quote whose text or answer letter drifted, and any coverage
gap), patch the affected quotes (script-assisted, never retyped), update any FACT
lines the canon change invalidates, rebuild.

## 13. Production history

Built 2026-07-23 → 2026-07-24 by a **multi-agent workflow** (~45 subagent launches
across the tooling, canon, figures, chapters, appendix, and audit phases — estimate —
plus retries after transient engine errors), reusing Book 2's production machinery
nearly unchanged: the same "bible-as-law" canon discipline, the same `chapters/*.md`
→ single-file HTML/PDF/TXT build shape, the same 8-voice audiobook pipeline,
retargeted from the Technician course to the General upgrade. New in this book:
markdown pipe-table support in the builder (the 402-row glossary renders as a real
table — Book 2 shipped its glossary as a joined paragraph), the `mathsvg` extension
for the General formula set (subscripts, π, √, fractions), ch10 as a full teaching
chapter (only ch00 is exempt from Exam Focus), a six-errata/nine-deletion pool with
non-contiguous IDs (audit and exam generator tolerate the gaps), and the series-site
General flip (Technician + General live, Extra coming soon). The gate the content was
written into: **79 pytest tests, 8 audit checks** (including mechanical verification
of all 423/423 pool quotes and answer keys), full HTML/PDF/TXT build. This runtime
does not meter subagent tokens; the ~4.1M figure in the README's stats block is an
estimate modeled from agent reads + written volume at ~4 chars/token.

## 14. Commands

**Regenerate the book:**
```
python3 tools/build_book.py --html --txt --pdf --out build/
```

**Verify (the accuracy/format/pool gate):**
```
python3 tools/audit_book.py
```

**Run the tooling test suite:**
```
python3 -m pytest -q
```

**Draw a practice exam:**
```
python3 tools/make_exam.py --seed 7 --out build/
```

## 15. Guidance for AI models extending this book

- **Obey `accuracy-canon.md` exactly.** It is the single source of truth for pool
  wording, dates, values, notation, glossary wording, the chapter map, and copyright
  status. Never re-date an event, restate a rule, or reword a question from memory —
  trace every fact back to the canon, and quote the pool only from
  `canon/pool-general.*`. If the canon needs a new entry, add it there first,
  sourced, before touching chapter prose.
- **Never paraphrase a pool question, repair a published quirk, or quote a deleted
  question.** Byte-exact quotes, the 6th-errata form always, G9C01's trailing space,
  G2E02's `D.A` label, and the G1D12/G1B05 citation misprints preserved; G1A04,
  G1C08, G1C09, G1C10, G1E09, G6B09, G8C01, G9C06, G9D13 exist only as numbering
  gaps. Extract quotes script-assisted — never retype pool text by hand.
- **Teach current rules where the rule moved after the pool was written.** 60 m is
  the segment-plus-four-channels structure under 91 FR 1430 (never "five channels,
  100 W ERP"); HF digital is the 2.8 kHz bandwidth standard (never 300 baud); the
  keyed answers are drilled exactly as published — the canon carries both halves of
  that split.
- **Keep the notation law.** Prose uses V and ×; unit case (kHz, MHz, mA, µV, pF) is
  load-bearing and tested; the pool's in-words quantities mean verbatim quotes never
  conflict.
- **Keep the careful wordings.** The /AG upgrade law, the sideband trio (boundary 10
  MHz, never 14), fees, timing promises, net frequencies, contest reports, QRP, and
  remote exams use exactly the hedged forms the canon resolved (§10) — do not
  strengthen them.
- **Never reproduce a protected Handbook image.** The 1968–1983 editions are under
  copyright — no scans, no traced reproductions, no quoted running text. This book
  needs none.
- **Run `python3 tools/audit_book.py` before considering any change done.** It is the
  mechanical enforcement of everything above (facts, format laws, figure tags, math,
  TOC, and 423/423 pool fidelity) — a change that doesn't pass it is not finished,
  regardless of how it reads.
