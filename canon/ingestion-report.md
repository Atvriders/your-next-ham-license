# Ingestion report — 2023–2027 NCVEC General (Element 3) question pool

Date: 2026-07-24 (UTC). Operator: automated ingestion (Kimi Code CLI).
Status: **all verification checks passed; audit exit 0; pytest exit 0.**

## 1. Source files

Landing page: <https://ncvec.org/index.php/2023-2027-general-question-pool-release>
(verified working 2026-07-24; the spec's draft URL
`…/2023-2027-general-question-pool` 404s). Downloaded 2026-07-24 into
`canon/source/` (curl with a browser User-Agent; no 403s):

| file | bytes | sha256 |
|---|---:|---|
| `source/ncvec-2023-2027-general-pool-6th-errata-feb4-2026.docx` | 277,568 | `a07b15d6b9b7aef9e51dae3dd7d37b23de1d7bb410733b7ac6323eaac2f4b396` |
| `source/ncvec-2023-2027-general-pool-6th-errata-feb4-2026.pdf` | 487,877 | `0627221fe69014b3015e97b44d3552a119ef7370144da8de9d02719c91cfa433` |
| `source/ncvec-2023-2027-general-pool-5th-errata-nov8-2024.docx` | 276,895 | `eb1addf7dbcaf2e147594daee6f04bb8d4750d2af4922e617fad874c44e68b8f` |
| `source/ncvec-2023-2027-general-pool-5th-errata-nov8-2024.pdf` | 489,304 | `e527d28172f2e47260fe5cce37d395ec4086e4b0fab14ac5720acc5e62e47085` |
| `source/G7-1.pdf` | 11,312 | `13b8ed81fc963ec1c24a414c78a288d658e52ff5d89e58c775aff85f17e57c3f` |
| `source/release-page.html` | 20,771 | `2bc4ece3d97131c819a514685f6cd285486a504aa6c630d59a3484cb4aa0501b` |

The canonical document is the **6th-errata release** ("General Class Pool and
Syllabus 2023-2027 Public Release with 6th Errata Feb 4 2026"), the file at the
top of the release page. Its front matter carries all six errata sheets in
full, and the pool body already incorporates every change (verified in §5).
The pool is public domain; effective for exams 2023-07-01 … 2027-06-30.

The 5th-errata release (docx+pdf) is kept as the pre-6th baseline for the
errata cross-check in §5.4. `release-page.html` is the fetched release page
itself (the errata ledger source). `source/sha256sums.txt` records the same
hashes.

**Post-sixth-errata check:** the release page (fetched 2026-07-24) lists the
6th errata (2026-02-04) as the newest entry; there is **no 7th errata**. The
page's own errata history and the document's front matter agree exactly.

**Pool figure:** the single required graphic is **Figure G7-1**, published as
`G7-1.pdf` (a schematic with 11 numbered symbols; content verified visually
after `pdftoppm` render). The page also links a JPEG ("General Question Pool
Graphics.jpg" → `…/downloads/G7-1 diagram 2023 Figure G7-1.jpg`) which returns
**nginx 404** from the NCVEC server (tried the linked URL, https, and
`+`-encoding variants — all 404; the server-side link is simply broken). The
PDF carries the same graphic, so the figure source is fully obtained; the 404
is recorded here for the ledger.

### ARRL cross-check mirror — not available as a separate file

<https://www.arrl.org/question-pools> does **not** host its own copy of the
2023–2027 General pool: its "GENERAL POOL" link points back to the NCVEC
release page above (confirmed by fetching the ARRL page HTML). Therefore no
NCVEC-vs-ARRL content diff is possible. As a substitute cross-check with equal
evidentiary value, the two independent NCVEC renderings (.docx vs .pdf) were
parsed separately and diffed — see §4.

## 2. Outputs

| file | bytes | sha256 |
|---|---:|---|
| `canon/pool-general.txt` | 119,372 | `4226fcc6502146e714cd516bc2ea3862a524068eb97bbebc76d21e6f4488cbe2` |
| `canon/pool-general.json` | 184,398 | `b6804225ab455f31405298625a741d6f030b479602233c691ba41ba52a9cd373` |

`pool-general.json` matches `tests/fixtures/pool_sample.json` schema exactly:
top-level object keyed by question id; each entry has, in fixture key order,
`group` ("G1A"), `subelement` ("G1"), `question` (single string), `choices`
(object with exactly "A".."D"), `answer` (one of "A".."D"), `figure` (null, or
"G7-1"). No extra keys (the Part 97 references are kept only in the .txt,
which preserves the published ID-line format).

`pool-general.txt` follows `tests/fixtures/pool_sample.txt` layout and the
Technician convention: `G1A01 (C) [97.301(d)]` ID line (answer in parentheses,
Part 97 ref in brackets where published), question text, `A.`–`D.` choice
lines, `~~` block separator. Subelement (`SUBELEMENT G1 – …`) and group
(`G1A – …`) headings are preserved as published (the General pool prints them
with en dashes, unlike the Tech pool's hyphens — preserved, not normalized).
A `#`-comment header documents provenance and the normalization rules; the
file ends with the published tail marker `~~~end of question pool text~~~`
and the published `NOTE: One graphic is required …` line, both verbatim.

## 3. Converter and normalization rules

Tooling probe: `pandoc` absent, `python-docx` absent, `pdftotext` present.
Chosen converter: **the .docx, parsed directly** with python3 `zipfile` +
`xml.etree.ElementTree` over `word/document.xml` (no third-party packages —
paragraph text assembled from `w:t` runs; same approach as the Tech build).
The docx carries logical paragraphs, so wording is byte-exact with no
line-wrap artifacts.

Normalization rules (also in the .txt header):

1. Each question/choice printed as one line, exactly as the docx paragraph;
   no re-wrap or reflow. Every one of the 423 questions was exactly one
   paragraph of question text plus 4 single-paragraph choices (0 anomalies
   from the strict parser; any deviation raised an error).
2. Paragraph-edge whitespace is stripped. One instance occurred: **G4E11
   choice B** carries a leading tab in the .docx (`\tB. Ensure the battery …`)
   — indentation, not content; stripped. This is the only whitespace
   normalization applied to any carried field.
3. No U+00A0 no-break spaces, soft hyphens, or fi/fl ligatures occur anywhere;
   none were altered. No double spaces occur in any question, choice, or
   heading (the only double spaces in the source are inside the nine
   "Question Deleted" placeholder lines, which are not carried — see §5.3).
4. Published Unicode punctuation preserved byte-exactly: en dash U+2013
   (×55, mostly headings), curly apostrophe U+2019 (×49), curly quotes
   U+201C/U+201D (×51 each). These are the only non-ASCII characters in the
   pool text.
5. ID lines preserve the published form, including two quirks:
   - 60 questions carry a Part 97 ref (all 52 G1 questions, 3 in G2, 5 in
     G0); the other 363 are published as bare `G2A01 (A)` — both forms kept.
   - **G9C01**'s ID line is published with a trailing space (`G9C01 (A) `);
     preserved verbatim, not "fixed".
6. Published choice-label quirk preserved: **G2E02 choice D** is printed in
   the source as `D.A DX spotting system using a network of software defined
   radios` (no space after the `D.` label). Kept byte-exact in the .txt; the
   JSON carries the choice text after the label
   (`A DX spotting system using a network of software defined radios`).
   Never repaired.
7. The PDF (pdftotext -layout) was parsed fully independently for the diff in
   §4; its single wrap artifact is not in this data.

## 4. Cross-extraction diff (docx vs pdf)

Both parsers produced **423 questions / 35 groups / 10 subelements / 9 deleted
placeholders** with identical id order, and all 45 heading lines equal after
whitespace normalization (the PDF wraps two long group headings across lines;
the docx does not). Field-by-field diff over question text, all 4 choices per
question, answer letters, Part 97 refs, and ID lines (whitespace-normalized):
**exactly one difference**, and it is a PDF-side extraction artifact, not a
content difference:

- G1A06 choice D: pdf `…permitted 24- hour use of the band` vs docx
  `…permitted 24-hour use of the band` — pdftotext split the line at the
  hyphen and the join left a space. Docx is authoritative; canonical files
  carry `24-hour`.

No substantive differences. No whitespace-only differences beyond this one.

## 5. Verification evidence

### 5.1 Counts and structure (parse-authoritative)

- Total published ID lines: **432** = **423 active questions** + **9 deleted
  placeholders**. The active count **423** is the parse-authoritative number
  and matches the plan's expectation (432 at the December 1, 2022 release
  − 9 withdrawn). No duplicate ids; document order == canonical pool order
  (G1…G9, G0 / group A–E / number), verified in the JSON and by re-parsing
  the .txt.
- Subelements: **exactly 10** (G1–G9, G0). Groups: **35** (the exam draws one
  question per group).
- Numbering is contiguous within every group from 01 up, **except exactly the
  eight gaps** G1A04, G1C08, G1C09, G1C10, G1E09, G6B09, G8C01, G9C06 — all
  known deletions. The ninth deletion, **G9D13, leaves no numbering gap** (it
  was the last question of G9D; the group now ends at G9D12); it is known
  from the deleted placeholder in the document and the errata sheets. Zero
  unexplained gaps.
- Every question: exactly 4 non-empty choices keyed A–D; answer ∈ {A,B,C,D};
  question text non-empty. (Answer-letter sanity: A×105, B×108, C×105, D×105.)

Per-subelement / per-group counts (authoritative, from the parse):

| subelement | questions | groups | per-group counts |
|---|---:|---|---|
| G1 | 52 | 5 | G1A:10 G1B:11 G1C:8 G1D:12 G1E:11 |
| G2 | 60 | 5 | G2A:12 G2B:11 G2C:11 G2D:11 G2E:15 |
| G3 | 37 | 3 | G3A:14 G3B:12 G3C:11 |
| G4 | 60 | 5 | G4A:13 G4B:13 G4C:12 G4D:11 G4E:11 |
| G5 | 40 | 3 | G5A:12 G5B:14 G5C:14 |
| G6 | 23 | 2 | G6A:12 G6B:11 |
| G7 | 38 | 3 | G7A:13 G7B:11 G7C:14 |
| G8 | 42 | 3 | G8A:14 G8B:13 G8C:15 |
| G9 | 46 | 4 | G9A:11 G9B:12 G9C:11 G9D:12 |
| G0 | 25 | 2 | G0A:12 G0B:13 |
| **total** | **423** | **35** | |

Syllabus reconciliation: the syllabus printed in the final document claims
G1:54, G2:60, G3:37, G4:60, G5:40, G6:23, G7:38, G8:42, G9:46, G0:25 (sum
425). Every subelement except **G1** matches the parse exactly. The printed
G1 count is **stale**: it reflects the post-4th-errata state (57 at release →
55 after the 3rd errata → 54 after the 4th) and was not updated for the 6th
errata's two G1 withdrawals (G1A04, G1C09) — the actual G1 body has 52 active
questions. The per-group active counts also match each errata sheet's own
"leaving N questions" statements exactly (G1A:10, G1C:8, G1E:11, G6B:11,
G8C:15, G9C:11, G9D:12). The parse, not the syllabus, is authoritative.

### 5.2 Errata ledger (all six; from the document's front-matter errata sheets, cross-checked against the release page)

| errata | issued | changes |
|---|---|---|
| Errata 1 | 2023-02-01 | Syllabus: SUBELEMENT G9 count 48→46. 9 questions modified (G1B01 "not" added; G1C01/G1C02 "transmitting"→"transmitter"; G5C02 "output"→"input signal"; G7C10 period after the "D" answer label; G9B05 elevation-angle clause added; G9C09 "In free space," prefix; G9D09 "MF and" added to answer A; G9D10 "1/3"→"1/10"). **2 withdrawn: G9C06, G9D13.** |
| Errata 2 | 2023-04-10 | 3 modified (G1A05 answer D → "All these choices are correct"; G1E10 question "24. 930"→"24.930"; G9D01 answer C gains leading "A"). **1 withdrawn: G6B09.** |
| 3rd errata | 2023-12-01 | FCC rule change. Syllabus: SUBELEMENT G1 count 57→55; G2E12 answer D → "All these choices are correct". **2 withdrawn: G1C08, G1C10.** |
| 4th errata | 2024-03-06 | **1 withdrawn: G1E09.** |
| 5th errata | 2024-11-08 | **1 withdrawn: G8C01.** |
| 6th errata | 2026-02-04 | **2 withdrawn: G1A04, G1C09** (the sheet states no reason; the plan attributes the withdrawal to the FCC 60 m rule change — context only, not document text). |

All twelve published text modifications (errata 1–3) were verified **present
in the final pool text** (spot-checked byte-exactly: G1B01, G1C01, G1C02,
G5C02, G9B05, G9C09, G9D09, G9D10, G1A05, G1E10, G9D01, G2E12 — all OK).

### 5.3 Deleted questions — verified

The nine withdrawn IDs from the plan were confirmed against the errata sheets
in the document front matter **and** against the release page text **and**
against the pool body, where each appears as a placeholder line
`GnX##  Question Deleted (section not renumbered)` (published with a double
space; **G1E09's placeholder is published with a single space** — quirk noted;
placeholders are not carried into the canonical files):

- G1A04 (6th), G1C08 (3rd), G1C09 (6th), G1C10 (3rd), G1E09 (4th),
  G6B09 (2nd), G8C01 (5th), G9C06 (1st), G9D13 (1st).

The deleted set from the parse == the plan's list exactly. The canonical
files carry the **active pool only**; the deletions are visible as numbering
gaps (G9D13 as the truncated end of G9D). IDs were never renumbered.

**5th-vs-6th document cross-check:** the 5th-errata .docx was parsed with the
same parser: 425 active + 7 deleted. Diff against the 6th-errata parse: the
only differences are the removal of G1A04 and G1C09 (both present as full
questions in the 5th, placeholders in the 6th); **zero content differences
among the 423 common questions** — the 6th errata changed nothing else.

### 5.4 Figure-referencing questions (1 pool graphic, 5 questions)

The pool ships a single graphic, **Figure G7-1** (`source/G7-1.pdf`). Five
questions reference it, all in group G7A; each carries `"figure": "G7-1"` in
the JSON (the other 418 carry `"figure": null`):

- **G7A09, G7A10, G7A11** — published as "figure G7-1" (lowercase)
- **G7A12, G7A13** — published as "Figure G7-1" (capitalized)

The case difference is published and preserved. (Detected by the literal
string "G7-1" in question text; no figure mentions occur in any choice text.
The document's closing NOTE confirms: "One graphic is required for certain
questions in section G7".)

### 5.5 Round-trips

- `json.load()` on `pool-general.json`: OK; schema/key-order/types checked
  against the fixture shape for all 423 entries; `figure` is null or "G7-1".
- `pool-general.txt` re-parsed with an **independent** script (shares no code
  with the generator): 423 question blocks, 10 subelement headings, 35 group
  headings, 45 header-comment lines, 2 published tail lines; ids, order,
  answer letters, question texts, and all 1,692 choice texts identical to the
  JSON (whitespace-normalized comparison). 0 mismatches.
- `python3 tools/audit_book.py`: **exit 0** — "Audit PASSED: 0 errors,
  0 warning(s)." Check [8/8] loaded the pool JSON, found no chapter quotes to
  check, and printed "appendix coverage skipped (no appendices/pool.md)".
- `python3 -m pytest -q`: **exit 0** — 62 passed.

## 6. Notes on schema adaptation

- The audit's check #8 reads only `canon/pool-general.json`; the fixture
  schema has no field for the Part 97 rule references. Those references are
  data the NCVEC publishes on the ID line, so they are preserved in the .txt
  ID lines (e.g. `G1A01 (C) [97.301(d)]`) and omitted from the JSON rather
  than adding a non-fixture key.
- `figure` values use the pool's own label "G7-1" (the questions literally
  say "figure G7-1" / "Figure G7-1").
- The nine deleted questions are absent from both canonical files by design
  (active pool only); the deletion record lives in this report and in the
  numbering gaps. The audit's coverage check tolerates non-contiguous
  numbering (its own fixture carries a deleted-ID gap), so no tool changes
  were needed.
- No content wording was altered for schema reasons; the only adaptations are
  the normalization rules in §3 (one stripped leading tab, G4E11 choice B).
