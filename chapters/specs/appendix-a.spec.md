# Writer Spec — Appendix A. The Complete 2023–2027 General Pool

**Output file:** `appendices/pool.md`
**Target length:** excluded from the book's ~48–52k prose target — it is the verbatim pool, 423 question blocks.
**Pool coverage:** **all 423 questions, exactly once each, in canonical pool order** — the audit's check #8 (`check_appendix_pool_coverage`) mechanically requires: every pool id present exactly once, every id a real pool question, and the sequence in pool order.

## 1. Purpose

Appendix A carries the full 2023–2027 General (Element 3) pool the same way the chapters' Exam Focus sections carry samples: every question verbatim, choices A–D verbatim, correct answer marked, plus a **one-line plain-language "why"** that names the chapter teaching it. Print-only — this appendix is **not narrated** in the audiobook (decision locked, design §2/§4).

## 2. Structure

- First line: `## Appendix A: The Complete 2023–2027 General Question Pool` (appendices are exempt from the chapter format laws — the audit's `check_format_laws` only applies to `chNN` stems — but keep the `## Appendix …` heading shape for the TOC; the colon form mirrors Book 2's shipped appendix).
- One short intro paragraph: what this is (the verbatim NCVEC 2023–2027 General pool, released into the public domain by the NCVEC QPC, valid for exams 2023-07-01 → 2027-06-30, incorporating all six errata through 2026-02-04 — 423 active questions; the nine withdrawn questions — G1A04, G1C08, G1C09, G1C10, G1E09, G6B09, G8C01, G9C06, G9D13 — simply do not appear, exactly as the canonical files omit them), how to use it (read the mapped chapter, then drill its group here), and the key to the entry format.
- Then **one `###` section per subelement, in pool order G1 → G9 → G0**, using the normalized published title + counts (straight apostrophe, em dash — mirror Book 2's normalization):

  | Heading line | 
  |---|
  | `### G1 — Commission's Rules (52 questions, 5 on the exam)` |
  | `### G2 — Operating Procedures (60 questions, 5 on the exam)` |
  | `### G3 — Radio Wave Propagation (37 questions, 3 on the exam)` |
  | `### G4 — Amateur Radio Practices (60 questions, 5 on the exam)` |
  | `### G5 — Electrical Principles (40 questions, 3 on the exam)` |
  | `### G6 — Circuit Components (23 questions, 2 on the exam)` |
  | `### G7 — Practical Circuits (38 questions, 3 on the exam)` |
  | `### G8 — Signals and Emissions (42 questions, 3 on the exam)` |
  | `### G9 — Antennas and Feed Lines (46 questions, 4 on the exam)` |
  | `### G0 — Electrical and RF Safety (25 questions, 2 on the exam)` |

- Within each subelement section, optionally one `####` line per group with the **published group heading verbatim** from `canon/pool-general.txt` (e.g. `#### G1A – General class control operator frequency privileges; primary and secondary allocations`) — the published en dash and curly punctuation are preserved byte-exactly; `####` group lines render as anchored h4s, never in the TOC. Then that group's questions in ascending number order, **skipping the deleted numbers** (G1A has no 04; G1C no 08/09/10; G1E no 09; G6B no 09; G8C starts at 02; G9C no 06; G9D ends at 12).
- The pool's single graphic belongs to G7A: embed the redrawn SVG on the line before **G7A09**'s quote block — `{{fig:ch07-pool-fig-g71}}` — and reference it by name ("the redrawn Figure G7-1, above") in the why lines of G7A10–G7A13. Embed once, at the first referencing question.

## 3. Entry format (audit check #8 parses this exactly)

Every one of the 423 entries is one blockquote in exactly this shape, followed by one plain line carrying the published ID line:

```
> **G1A01** <question text, verbatim from the pool>
> A. <choice text, verbatim>
> B. <choice text, verbatim>
> C. <choice text, verbatim>
> D. <choice text, verbatim>
> **Answer: C** — <one-line why, ending with the teaching chapter: "… — taught in chapter 1.">

Published ID line: `G1A01 (C) [97.301(d)]`
```

Rules (all mechanically enforced or canon law):

- **Question and choice text byte-exact** from `canon/pool-general.json` (the audit compares whitespace-normalized). Published Unicode punctuation (curly apostrophes/quotes, en dashes) is preserved, never converted to ASCII.
- **All four choice lines A–D always present**, in order. The `**Answer: X**` letter must match the pool key exactly.
- **Order:** canonical pool order = subelements G1…G9 then G0; group A–E within each subelement; ascending number within each group, skipping the nine deletions. (This is the published order and the audit's `pool_sort_key`; iterating `sorted(pool, key=pool_sort_key)` over `canon/pool-general.json` yields it.)
- **The published ID line** (answer letter + Part 97 reference as printed in `canon/pool-general.txt`) rides on a **separate plain-text line after the blockquote, in backticks** — never inside the `> **GnXnn** …` line itself (the audit would read it as part of the question text and fail the quote). Published quirks stay verbatim, never repaired:
  - `G9C01 (A) ` — the ID line carries a **published trailing space**; reproduce it (canon §7.7).
  - `G1D12 (B) [97.507]` — the printed citation is a misprint (canon §7.4); the why line cites the §97.301 preamble, never "repairs" the ID line.
  - `G1B05 (B) [97.111((5)(b)]` — malformed citation (double open-paren); the why line cites §97.111(b).
  - **G2E02's choice-D label quirk:** the published text prints `D.A DX spotting system…` (no space — the choice text itself begins with the word "A"). In the quote block print the normalized label with a space: `> D. A DX spotting system using a network of software defined radios` (this matches `canon/pool-general.json`'s choice text and keeps the audit's choice-line regex parsing; the no-space form is preserved in `canon/pool-general.txt` and noted here so the repair is never silent — canon §7.7).
- **The one-line "why"** is original prose: a plain sentence (or two short ones max) giving the reason the keyed answer is correct in colleague language, and naming the teaching chapter ("taught in chapter 3"). Never paraphrase the question back; never contradict the canon; where the canon carries the fact, the why should echo it (e.g., G1C03's why cites §97.303(h)(3), the current section — not the superseded [97.303(h)(1)] the pool prints; G1C04's cites §97.313(i)).
- The five figure questions (G7A09–G7A13) appear in their published forms — G7A09–G7A11 print "figure G7-1" lowercase, G7A12–G7A13 print "Figure G7-1" capitalized; preserve each as published (canon §1.4).
- Deleted questions are never quoted, and no placeholder marks their absence (canon §1.3: they appear only as numbering gaps).

## 4. Chapter-mapping table (for the "why" lines — binding, from canon §5)

| Pool groups | Teaching chapter |
|---|---|
| G1A–G1E | chapter 1 |
| G2A–G2E | chapter 2 |
| G3A–G3C | chapter 3 |
| G4A–G4E | chapter 4 |
| G5A–G5C | chapter 5 |
| G6A–G6B | chapter 6 |
| G7A–G7C | chapter 7 |
| G8A–G8C | chapter 8 |
| G9A–G9D | chapter 9 |
| G0A–G0B | chapter 10 |

## 5. Production method (fragment-per-subelement, then assemble)

The 423-block assembly is mechanical — script it, never hand-type pool text:

1. **Ten fragment agents (G1–G0), one per subelement.** Each emits one fragment file containing its subelement's `###` heading line, optional `####` group lines, and every active question block + Published ID line, in canonical order. The "why" lines are authored per subelement (colleague language, one line each, ending "— taught in chapter N." per §4) — everything else is verbatim pool or the published ID lines.
2. **Generation:** load `canon/pool-general.json`; iterate `sorted(pool, key=pool_sort_key)` (import `pool_sort_key` from `tools/audit_book.py`); for each id emit the six blockquote lines from the JSON fields (`question`, `choices` A–D, `answer`), then the published ID line parsed from `canon/pool-general.txt` (match `^GnXnn (L)( \[…\])?$` — some IDs carry no citation, e.g. G2E02). Merge the authored whys by id; regenerate mechanically — never hand-edit the generated question text.
3. **Assemble** the fragments in canonical order (G1…G9 then G0), normalize each `###` heading to the §2 table, and splice the `{{fig:ch07-pool-fig-g71}}` embed on the line before G7A09's blockquote.
4. **Byte-exact gate (per-fragment at handoff and book-wide at the end):** re-extract every question from the assembled `appendices/pool.md` and diff mechanically against `canon/pool-general.json` — run `python3 tools/audit_book.py`; check #8 must report 0 errors for `appendices/pool.md` (all 423 quoted once, in order, letters matching the key).

## 6. Integrity notes

- Public domain: the NCVEC QPC released this pool into the public domain (release page captured in `canon/source/release-page.html`); the intro paragraph says so in one sentence with the validity window **2023-07-01 → 2027-06-30** and the six-errata record (no 7th errata as of 2026-07-24).
- No `**FACT:**` lines required in appendices (exempt from the format laws); no Key Takeaways; no banned phrases anywhere ("little did they know", "in that moment", "a testament to").
- The "why" lines are the only original prose in the appendix — everything else is verbatim pool or the published ID lines.
- The 60 m entries (G1C03, G1C04) drill the keyed answers exactly as published; their whys explain with the current rule sections (§97.303(h)(3), §97.313(i)) per canon §7.1 — never teach the withdrawn wording as current.
