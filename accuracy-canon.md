# Accuracy Canon — Your Next Ham License: The General Course (2023–2027)

**This file is LAW.** It is the single, binding source of truth for *Your Next Ham License: The General Course (2023–2027)*. Every chapter writer, figure author, appendix writer, and auditor conforms to it exactly: pool wording, numbers, dates, notation, terminology, chapter mapping, and copyright reproducibility are governed here and nowhere else. Where a claim was ever contested during research, this file states the one resolved value the book will use and cites it; disagreements with any draft chapter are resolved in favour of this canon, not the chapter. Every uncertainty flagged during research has been closed to a sourced value or a deliberately careful wording in **§7 Resolved Uncertainties** — there are no open placeholders in this document, and the automated build audit greps this file to confirm it.

Companion canonical data (part of this canon by reference): `canon/pool-general.txt` and `canon/pool-general.json` — the verified 423-question NCVEC 2023–2027 General (Element 3) pool. Question text, choices, and answer letters are quoted from those two files only, never from memory, web mirrors, or third-party study guides.

Series note: this is Book 3 in the series, written for readers who hold the Technician license Book 2 (*Your First Ham License: The Technician Course (2026–2030)*) teaches to. Notation, units, and shared glossary terms are identical to Book 2's canon wherever they overlap (§3, §4); where the General material legitimately deepens a convention (e.g., the decibel formula is exam math here), the difference is stated explicitly rather than silently changed.

---

## 1. Pool Summary & Revision Record

### 1.1 Canonical pool files (the only quoting sources)

| File | Bytes | sha256 |
|---|---:|---|
| `canon/pool-general.txt` | 119,372 | `4226fcc6502146e714cd516bc2ea3862a524068eb97bbebc76d21e6f4488cbe2` |
| `canon/pool-general.json` | 184,398 | `b6804225ab455f31405298625a741d6f030b479602233c691ba41ba52a9cd373` |

The `.txt` is the human-readable, byte-exact rendering (ID lines `G1A01 (C) [97.301(d)]`, one line per question and per choice, `~~` separators, published subelement/group headings with their en dashes, a `#`-comment provenance header, and the published tail lines `~~~end of question pool text~~~` and `NOTE: One graphic is required for certain questions in section G7`). The `.json` is the structured form: top-level object keyed by question id; each entry has `group`, `subelement`, `question`, `choices` (exactly "A"–"D"), `answer` (one of "A"–"D"), `figure` (null, or "G7-1"). Part 97 references live only on the `.txt` ID lines.

### 1.2 Provenance (verified source downloads)

Landing page: <https://ncvec.org/index.php/2023-2027-general-question-pool-release> ("2023-2027 General Question Pool Release"; verified working 2026-07-24). Downloaded 2026-07-24 into `canon/source/`:

| File | Bytes | sha256 |
|---|---:|---|
| `canon/source/ncvec-2023-2027-general-pool-6th-errata-feb4-2026.docx` | 277,568 | `a07b15d6b9b7aef9e51dae3dd7d37b23de1d7bb410733b7ac6323eaac2f4b396` |
| `canon/source/ncvec-2023-2027-general-pool-6th-errata-feb4-2026.pdf` | 487,877 | `0627221fe69014b3015e97b44d3552a119ef7370144da8de9d02719c91cfa433` |
| `canon/source/ncvec-2023-2027-general-pool-5th-errata-nov8-2024.docx` | 276,895 | `eb1addf7dbcaf2e147594daee6f04bb8d4750d2af4922e617fad874c44e68b8f` |
| `canon/source/ncvec-2023-2027-general-pool-5th-errata-nov8-2024.pdf` | 489,304 | `e527d28172f2e47260fe5cce37d395ec4086e4b0fab14ac5720acc5e62e47085` |
| `canon/source/G7-1.pdf` | 11,312 | `13b8ed81fc963ec1c24a414c78a288d658e52ff5d89e58c775aff85f17e57c3f` |
| `canon/source/release-page.html` | 20,771 | `2bc4ece3d97131c819a514685f6cd285486a504aa6c630d59a3484cb4aa0501b` |

The canonical document is the **6th-errata release** ("General Class Pool and Syllabus 2023-2027 Public Release with 6th Errata Feb 4 2026"), the file at the top of the release page; its front matter carries all six errata sheets in full and the pool body already incorporates every change (verified during ingestion). The 5th-errata release is kept as the pre-6th baseline: re-parsed with the same parser, it differs from the 6th only by the removal of G1A04 and G1C09, with zero content differences among the 423 common questions. `release-page.html` is the fetched release page itself — the errata-ledger and public-domain-statement source. The release page's linked JPEG of the pool figure 404s on the NCVEC server (broken server-side link); the PDF `G7-1.pdf` carries the same graphic, so the figure source is fully obtained — the 404 is recorded here for the ledger.

Extraction and cross-check (full evidence in `canon/ingestion-report.md`): the canonical text was parsed from the `.docx` (logical paragraphs, byte-exact wording; python3 `zipfile` + `ElementTree`, no third-party packages) and independently re-parsed from the `.pdf` with `pdftotext -layout`; the two agreed on all 423 questions, all 1,692 choices, all answer letters, all Part 97 refs, and all 45 headings except one PDF-side line-wrap artifact (G1A06 "24- hour"). The `.docx` is authoritative; the canonical files carry `24-hour`. ARRL hosts no separate copy of this pool (its question-pools page links back to NCVEC), so the docx-vs-pdf double parse is the cross-check of record. Normalization preserved published Unicode punctuation byte-exactly (en dash U+2013 ×55, curly apostrophe U+2019 ×49, curly quotes U+201C/U+201D ×51 each — the only non-ASCII characters in the pool text) and the published ID-line and choice-label forms verbatim — including `G9C01 (A) ` with a trailing space and `G2E02`'s choice D printed as `D.A DX spotting system …` with no space after the label. The only whitespace normalization applied anywhere is one stripped leading tab (G4E11 choice B — indentation, not content). None of these quirks is ever "fixed" in quotation (§7.7).

### 1.3 Structure, counts, and revision record

- **Total: 423 active questions** (432 published IDs minus 9 withdrawn), 10 subelements (G1–G9, G0), **35 groups**. No duplicate ids; document order == canonical pool order; every question has exactly 4 choices A–D and one keyed answer (answer-letter sanity: A×105, B×108, C×105, D×105).
- **The exam: 35 questions, one drawn from each of the 35 groups; 26 correct answers required to pass** (47 CFR §97.503(b); pool structure per canonical counts).
- **Validity: exams from 2023-07-01 through 2027-06-30. THIS POOL EXPIRES MID-2027.** The successor General pool takes effect 2027-07-01 (four-year rotation: Technician 2026–2030, General 2023–2027, Extra 2024–2028). Every printing, chapter, exam product, and web page derived from this book must state the 2023–2027 validity window; any printing after mid-2027 must state which pool exams actually use. The contained-swap procedure for the successor pool is pinned in §7.13.
- **Public domain:** the NCVEC Question Pool Committee released the 2023–2027 General (Element 3) pool into the public domain (statement on the release page, captured in `canon/source/release-page.html`, fetched 2026-07-24). Initial release 2022-12-01 (432 questions); the current document is the 6th-errata release of 2026-02-04.
- **Errata ledger (all six; from the document's front-matter errata sheets, cross-checked against the release page):**

| Errata | Issued | Changes |
|---|---|---|
| Errata 1 | 2023-02-01 | Syllabus: SUBELEMENT G9 count 48→46. 9 questions modified (G1B01 "not" added; G1C01/G1C02 "transmitting"→"transmitter"; G5C02 "output"→"input signal"; G7C10 period after the "D" answer label; G9B05 elevation-angle clause added; G9C09 "In free space," prefix; G9D09 "MF and" added to answer A; G9D10 "1/3"→"1/10"). **2 withdrawn: G9C06, G9D13.** |
| Errata 2 | 2023-04-10 | 3 modified (G1A05 answer D → "All these choices are correct"; G1E10 question "24. 930"→"24.930"; G9D01 answer C gains leading "A"). **1 withdrawn: G6B09.** |
| 3rd errata | 2023-12-01 | FCC rule change. Syllabus: SUBELEMENT G1 count 57→55; G2E12 answer D → "All these choices are correct". **2 withdrawn: G1C08, G1C10.** |
| 4th errata | 2024-03-06 | **1 withdrawn: G1E09.** |
| 5th errata | 2024-11-08 | **1 withdrawn: G8C01.** |
| 6th errata | 2026-02-04 | **2 withdrawn: G1A04, G1C09** (the sheet states no reason; the rule-change context is the FCC's 60 m amendment — see §7.1). |

All twelve published text modifications (errata 1–3) were verified present in the final pool text byte-exactly during ingestion. There is **no 7th errata** as of 2026-07-24 (release page and document front matter agree); re-check the release page before each reprint.

- **The nine deleted IDs: G1A04, G1C08, G1C09, G1C10, G1E09, G6B09, G8C01, G9C06, G9D13.** Numbering rule (binding): IDs are contiguous within every group from 01 up **except exactly these deletions** — the questions were withdrawn without renumbering, each printed in the source as `GnX##  Question Deleted (section not renumbered)`. Eight of the nine leave a numbering gap; **G9D13 leaves no gap** because it was the last question of G9D (the group now ends at G9D12) and is known from the deleted placeholder and the errata sheets. The canonical files carry the active pool only; **deleted questions are never quoted, taught, or referenced as exam content anywhere in the book** — they appear only as numbering gaps and in this ledger.
- **Syllabus reconciliation:** the syllabus printed in the final document claims G1:54 (sum 425); the parse-authoritative G1 count is **52** — the printed number is stale (not updated for the 6th errata's two G1 withdrawals). Every other printed subelement count matches the parse exactly. The parse, not the syllabus, is authoritative (§7.7).

Per-subelement counts (exam weight = one question per group; titles as published, en dashes preserved):

| Subelement | Title (as published) | Questions | Groups | Per-group counts | Exam questions |
|---|---|---:|---:|---|---:|
| G1 | COMMISSION'S RULES | 52 | 5 | G1A:10 G1B:11 G1C:8 G1D:12 G1E:11 | 5 |
| G2 | OPERATING PROCEDURES | 60 | 5 | G2A:12 G2B:11 G2C:11 G2D:11 G2E:15 | 5 |
| G3 | RADIO WAVE PROPAGATION | 37 | 3 | G3A:14 G3B:12 G3C:11 | 3 |
| G4 | AMATEUR RADIO PRACTICES | 60 | 5 | G4A:13 G4B:13 G4C:12 G4D:11 G4E:11 | 5 |
| G5 | ELECTRICAL PRINCIPLES | 40 | 3 | G5A:12 G5B:14 G5C:14 | 3 |
| G6 | CIRCUIT COMPONENTS | 23 | 2 | G6A:12 G6B:11 | 2 |
| G7 | PRACTICAL CIRCUITS | 38 | 3 | G7A:13 G7B:11 G7C:14 | 3 |
| G8 | SIGNALS AND EMISSIONS | 42 | 3 | G8A:14 G8B:13 G8C:15 | 3 |
| G9 | ANTENNAS AND FEED LINES | 46 | 4 | G9A:11 G9B:12 G9C:11 G9D:12 | 4 |
| G0 | ELECTRICAL AND RF SAFETY | 25 | 2 | G0A:12 G0B:13 | 2 |
| **Total** | | **423** | **35** | | **35** |

### 1.4 Pool figure G7-1 (5 questions) and the redraw rule

Five questions reference the pool's single graphic, **Figure G7-1** (`canon/source/G7-1.pdf`); all other 418 carry `"figure": null`. Three questions print "figure G7-1" lowercase (G7A09, G7A10, G7A11) and two print "Figure G7-1" capitalized (G7A12, G7A13) — the case difference is published and preserved. The book **redraws the figure as an original SVG conveying exactly the official content — same components, same labels, same numbered callouts — never copies the published graphic**. The redrawn figure is registered in `figures/figures.json` as `kind:"original"` with the note "redrawn from NCVEC pool figure G7-1". The pool is public domain, so this is both safe and faithful; the redraw rule exists so the book's visual style stays consistent and themeable.

The binding specification below is r4's close read of `canon/source/G7-1.pdf` (rendered at 200 dpi; every numbered symbol verified by close-up crops and cross-checked against the pool answers).

**Overall:** a black-and-white line schematic of a **two-stage circuit — a variable-frequency oscillator (left, built around the FET) feeding an amplifier/buffer stage (right, built around the NPN transistor)** — with a single +DC supply rail across the top and an RF output terminal at the right. Open-circle terminals labeled "+DC" (top right) and "OUT" (right). Caption "Figure G7-1" centered beneath the drawing. **Every ground symbol is drawn as three slanted (diagonal) strokes of decreasing length, longest on top** — the same style as the Technician book's T-1/T-2/T-3 redraws, never the classic horizontal shrinking lines. Unnumbered support parts (bias resistors, bypass and coupling capacitors, a series resistor in the +DC rail) appear as in any discrete two-stage design; only the 11 numbered symbols are exam-relevant.

**Numbered symbols** (identity — position in drawing — asked by):
- **1 = field effect transistor (N-channel JFET)** — center; circle containing a vertical channel bar, gate lead entering from the left with a **filled arrowhead pointing inward (right) into the channel**; top of channel wired up toward the +DC rail, bottom of channel wired down toward the tapped inductor. Asked by **G7A09** (keyed answer C).
- **2 = NPN junction transistor** — right-center; circle with vertical base bar on its left half, base lead from the left, collector line exiting the top to the transformer primary, emitter line exiting downward with a **filled arrowhead pointing outward / down-right, away from the base** ("Not Pointing iN" = NPN); label "2" to the right. Asked by **G7A11** (keyed answer B).
- **3 = ordinary PN junction diode** — left of symbol 1, vertical branch to ground; **filled triangle pointing DOWN** onto a horizontal cathode bar (anode top). Not asked.
- **4 = varactor diode** — far left, vertical; filled triangle pointing UP into a straight cathode bar with a **curved (arc-shaped) second plate above it** — diode-plus-capacitor = voltage-variable capacitor, used for tuning. Not asked. (Distractor magnet: looks almost like a Zener — see G7A10's option A.)
- **5 = Zener diode** — top center-right, shunt from the +DC rail to ground; filled triangle pointing UP into a cathode bar whose **two ends are bent diagonally into the classic "Z" wings**. Asked by **G7A10** (keyed answer D).
- **6 = solid-core transformer** — right; primary coil (left, more humps) and secondary coil (right, fewer humps) separated by **two straight vertical core lines** (the solid/laminated core); secondary bottom grounded, secondary top to the OUT terminal. Asked by **G7A12** (keyed answer C).
- **7 = tapped inductor** — lower left; single vertical coil, bottom end grounded, with a **connection (tap) leaving the coil partway up** toward the right. Asked by **G7A13** (keyed answer A).
- **8 = polarized (electrolytic) capacitor** — top center, vertical shunt from the +DC rail to ground; **one straight plate, one curved plate**. Not asked.
- **9 = fixed resistor** — lower right, vertical zigzag from the transistor-2 emitter node to ground (an unnumbered bypass capacitor parallels it). Not asked.
- **10 = polarized (electrolytic) coupling capacitor** — left-center, horizontal in the long gate/signal wire; one straight plate, one curved plate. Not asked.
- **11 = variable resistor** — upper left, vertical zigzag between the +DC feed and the left-hand circuitry, with a **diagonal arrow drawn through the zigzag**. Not asked.

**Question→position map:** G7A09→1 (FET); G7A10→5 (Zener); G7A11→2 (NPN); G7A12→6 (solid-core transformer); G7A13→7 (tapped inductor). The five questions raid each other: options come from {1, 2, 4, 5, 6, 7, 11}, so partial knowledge still faces plausible distractors. Teaching strategy (binding for ch07): drill all 11 as one symbol-recognition table; the three diode variants (3 plain / 4 varactor / 5 Zener) are the discrimination students miss. Circuit story for the caption: the FET oscillator (symbol 1) with its tapped-inductor tank (symbol 7) generates the RF; the NPN stage (symbol 2) amplifies/buffers it; the solid-core transformer (symbol 6) couples the output to the OUT terminal; the Zener (symbol 5) regulates the +DC rail.

### 1.5 Quoting discipline (audit-enforced)

- Question text, choice text, and answer letters are quoted **only** from the two canonical pool files, byte-exact (the audit compares whitespace-normalized). Published Unicode punctuation (curly apostrophes/quotes, en dashes) is preserved, never converted to ASCII.
- Chapter and appendix pool quotes use this exact block markup (the audit parses it):

```
> **G1A01** <question text, verbatim from the pool>
> A. <choice text, verbatim>
> B. <choice text, verbatim>
> C. <choice text, verbatim>
> D. <choice text, verbatim>
> **Answer: C** — one-line why.
```

- Every quoted id must exist in the pool; every stated choice line and the stated answer letter must match the pool key. Appendix A quotes all 423 ids exactly once, in canonical pool order (G1…G9, G0; group A–E; number).
- The pool's own published quirks are reproduced as published, never silently repaired: the G9C01 ID-line trailing space, the G2E02 `D.A` choice label, and the two citation defects on G1D12 and G1B05 (§7.4).
- The nine deleted questions (§1.3) are never quoted; Appendix A's coverage simply skips the deleted numbers, exactly as the canonical files do.

---

## 2. Pinned Facts with Sources

The book's fact reservoir. Each line is `- **FACT:** <one self-contained sentence> — Source: <§ or URL>`. Chapter writers copy the sentence **verbatim** into their chapters (the build audit greps each chapter's `**FACT:**` lines for an exact match in this file); a chapter may add explanation around it but may never alter the sentence. Every sentence stands alone, needs no surrounding context to be true, and is safe for an upgrading Technician to memorize. Rule quotations inside FACT sentences are verbatim from the eCFR text of 47 CFR Part 97, issue date 2026-07-20 (with §97.509 quoted from the 2026-07-22 issue), pulled 2026-07-24 (research notes r1/r2); re-pull every cited section before any reprint — see §7.13. Where a rule quotation is embedded mid-sentence, the initial letter's case and the terminal punctuation may be adjusted to fit the host sentence (standard embedded-quote convention); the quoted words themselves are verbatim from the cited section. Where current rule text differs from the pool-era text the 2022 pool was written against, the FACT pins the current text and §7.1/§7.5 carry the difference — the only such hazard areas are 60 m and the HF symbol-rate rules, both resolved below.

### 2.1 General-class frequency privileges and emission standards (rules)

- **FACT:** The §97.301 frequency bands apply to "an amateur station located within 50 km of the Earth's surface, within the specified ITU Region, and outside any area where the amateur service is regulated by any authority other than the FCC." — Source: 47 CFR §97.301 preamble; pool G1D12 (see §7.4)
- **FACT:** A station with a Technician, General, Advanced, or Amateur Extra control operator may use all amateur bands at 50 MHz and above (Region 2 values: 6 m 50–54 MHz, 2 m 144–148 MHz, 1.25 m 222–225 MHz, 70 cm 420–450 MHz, and all higher allocations). — Source: 47 CFR §97.301(a) table
- **FACT:** General class MF/HF/LF privileges are exactly: 2200 m 135.7–137.8 kHz; 630 m 472–479 kHz; 160 m 1800–2000 kHz (1810–1850 kHz in Region 1); 80 m 3.525–3.600 MHz; 75 m 3.800–4.000 MHz in Region 2 and 3.800–3.900 MHz in Region 3 (no Region 1 allocation); 60 m 5.3515–5.3665 MHz (plus four discrete channels — see §7.1); 40 m 7.025–7.125 MHz and 7.175–7.300 MHz (7.175–7.200 MHz in Regions 1/3); 30 m 10.100–10.150 MHz; 20 m 14.025–14.150 MHz and 14.225–14.350 MHz; 17 m 18.068–18.168 MHz; 15 m 21.025–21.200 MHz and 21.275–21.450 MHz; 12 m 24.890–24.990 MHz; 10 m 28.000–29.700 MHz. — Source: 47 CFR §97.301(d) table (current text)
- **FACT:** Amateur Extra holds all General segments plus Extra-only HF segments — 3.500–3.525 MHz, 3.600–3.800 MHz, 7.000–7.025 MHz, 7.125–7.175 MHz, 14.000–14.025 MHz, 14.150–14.225 MHz, 21.000–21.025 MHz, and 21.200–21.275 MHz — so the Extra-exclusive spectrum sits on 80, 40, 20, and 15 meters only. — Source: 47 CFR §97.301(b) vs §97.301(d); pool G1A08
- **FACT:** The bands with portions where General class licensees cannot transmit are 80 meters, 40 meters, 20 meters, and 15 meters — on 160, 60, 30, 17, 12, and 10 meters General has the entire band. — Source: 47 CFR §97.301(d) vs §97.301(b); pool G1A01
- **FACT:** General licensees are excluded from 7.125–7.175 MHz on 40 meters, but they are not excluded from 28.000–28.025 MHz (CW is permitted on the entire 10 m band) or 21.275–21.300 MHz (inside the General 15 m phone segment). — Source: 47 CFR §97.301(d), §97.305(a); pool G1A05
- **FACT:** 21.300 MHz (21300 kHz) is inside the General class 15-meter segment 21.275–21.450 MHz. — Source: 47 CFR §97.301(d); pool G1A09
- **FACT:** Where General does not get a band's entire voice segment, the General share is the upper frequency portion — 20 m phone General 14.225–14.350 MHz, 40 m General 7.175–7.300 MHz, 75 m General 3.800–4.000 MHz, 15 m General 21.275–21.450 MHz. — Source: 47 CFR §97.301(d) vs §97.305(c) phone-segment edges; pool G1A11
- **FACT:** When the FCC designates the amateur service as secondary on a band, amateur stations "must not cause harmful interference to, and must accept interference from, stations in a primary service." — Source: 47 CFR §97.303 preamble; pool G1A06
- **FACT:** The United States, Puerto Rico, and the U.S. Virgin Islands are in ITU Region 2; other U.S. insular areas are in Region 2 or 3. — Source: Note to 47 CFR §97.303; pool G1E06
- **FACT:** "Except as specified elsewhere in this part, an amateur station may transmit a CW emission on any frequency authorized to the control operator" — which is why CW is allowed on the entire 10 m band, 28.0–29.7 MHz. — Source: 47 CFR §97.305(a); pool G1A07
- **FACT:** On 30 meters (10.100–10.150 MHz) only RTTY and data emissions are authorized — no phone and no image anywhere in the band. — Source: 47 CFR §97.305(c)(3)(viii); pool G1A02, G1A03
- **FACT:** On 10 meters, RTTY/data occupy 28.0–28.3 MHz and phone/image occupy 28.3–29.7 MHz. — Source: 47 CFR §97.305(c)(3)(xvii)–(xx)
- **FACT:** On 60 meters a station may transmit only phone, RTTY, data, and CW emissions, and emissions must not exceed a bandwidth of 2.8 kilohertz — the rule lives at §97.307(f)(14)(i) with the frequency list in §97.303(h)(3) (current text; the pool prints the superseded cite [97.303(h)(1)] — see §7.1). — Source: 47 CFR §97.307(f)(14)(i), §97.303(h)(3) (current); pool G1C03 (keyed answer 2.8 kHz remains correct)
- **FACT:** A station transmitting RTTY/data using a specified digital code "may use any technique whose technical characteristics have been documented publicly, such as CLOVER, G-TOR, or PacTOR, for the purpose of facilitating communications." — Source: 47 CFR §97.309(a)(4); pool G1C07
- **FACT:** RTTY/data emissions using an unspecified digital code "must not be transmitted for the purpose of obscuring the meaning of any communication." — Source: 47 CFR §97.309(b)
- **FACT:** The HF symbol-rate limits were replaced by a 2.8 kHz authorized-bandwidth standard below 28 MHz effective December 2023 (the 300-baud limit survives only on 2200 m and 630 m), and no active General pool question tests maximum symbol rate — see §7.5. — Source: 47 CFR §97.307(f)(3) current vs 2023-07-01 (88 FR 85127); full-text search of `canon/pool-general.json`
- **FACT:** On 10 meters, repeater operation is confined to the portion of the band above 29.5 MHz. — Source: 47 CFR §97.205(b); pool G1A10

### 2.2 Transmitter power standards (rules)

- **FACT:** "An amateur station must use the minimum transmitter power necessary to carry out the desired communications." — Source: 47 CFR §97.313(a)
- **FACT:** "No station may transmit with a transmitter power exceeding 1.5 kW PEP" — 1500 watts PEP output is the answer for a General on 12 meters, on 28 MHz, and on 1.8 MHz. — Source: 47 CFR §97.313(b); pool G1C02, G1C05, G1C06
- **FACT:** "No station may transmit with a transmitter power output exceeding 200 W PEP … (1) On the 10.10-10.15 MHz segment" — 30 meters is the 200 W PEP band for a General. — Source: 47 CFR §97.313(c)(1); pool G1C01 (asked as 10.140 MHz)
- **FACT:** The other 200 W PEP HF segments — 3.525–3.60 MHz, 7.025–7.125 MHz, 21.025–21.20 MHz, and 28.0–28.5 MHz — apply only "when the control operator is a Novice Class operator or a Technician Class operator"; a General control operator may use up to 1.5 kW PEP on those segments. — Source: 47 CFR §97.313(c)(2)
- **FACT:** On 60 meters (current text), no station may transmit on the four discrete channels 5332, 5348, 5373, and 5405 kHz with a radiated power exceeding 100 W ERP, and no station may transmit in the contiguous 5351.5–5366.5 kHz segment with a radiated power exceeding 9.15 W ERP — see §7.1. — Source: 47 CFR §97.313(i) (amended by 91 FR 1430)
- **FACT:** For 60 m ERP computation, "the transmitter PEP will be multiplied by the antenna gain relative to a half-wave dipole antenna. A half-wave dipole antenna will be presumed to have a gain of 1 (0 dBd). Licensees using other antennas must maintain in their station records either the antenna manufacturer's data on the antenna gain or calculations of the antenna gain." — Source: 47 CFR §97.313(i) (verbatim, unchanged by the 2026 amendment; pool G1C04 remains correct — see §7.1)
- **FACT:** "No station may transmit with a transmitter output exceeding 10 W PEP when the station is transmitting a SS emission type." — Source: 47 CFR §97.313(j); pool G1E08
- **FACT:** The 2200 m band limit is 1.5 kW PEP transmitter power or 1 W EIRP radiated, and the 630 m band limit is 500 W PEP or 5 W EIRP (1 W EIRP within 800 km of the Russian Federation in Alaska). — Source: 47 CFR §97.313(k), (l)
- **FACT:** Peak envelope power (PEP) means "the average power supplied to the antenna transmission line by a transmitter during one RF cycle at the crest of the modulation envelope taken under normal operating conditions" — the legal power measurement is PEP output from the transmitter. — Source: 47 CFR §97.3(b)(9); pool G1C11

### 2.3 Control operators, special stations, and operating rules (rules)

- **FACT:** "When transmitting, each amateur station must have a control operator," and the control operator must hold an FCC amateur operator/primary station grant on the ULS or be authorized for alien reciprocal operation — remotely controlling a US station from abroad still requires the US license. — Source: 47 CFR §97.7(a); pool G1D05
- **FACT:** "The control operator must ensure the immediate proper operation of the station, regardless of the type of control," and "a station may only be operated in the manner and to the extent permitted by the privileges authorized for the class of operator license held by the control operator." — Source: 47 CFR §97.105(a), (b)
- **FACT:** A Technician may legally talk through a 10-meter repeater only if the repeater's own control operator holds General class or higher, because the repeater is the transmitting station on 10 m and privileges follow its control operator. — Source: 47 CFR §97.205(b), §97.105(b), §97.301(e); pool G1E02
- **FACT:** A control operator is "an amateur operator designated by the licensee of a station to be responsible for the transmissions from that station to assure compliance with the FCC Rules," and a control point is "the location at which the control operator function is performed." — Source: 47 CFR §97.3(a)(13), (14)
- **FACT:** Local control uses a control operator "who directly manipulates the operating adjustments in the station"; remote control uses one "who indirectly manipulates the operating adjustments in the station through a control link"; automatic control uses "devices and procedures for control of a station when it is transmitting so that compliance with the FCC Rules is achieved without the control operator being present at a control point." — Source: 47 CFR §97.3(a)(31), (39), (6)
- **FACT:** A telecommand station on or within 50 km of the Earth's surface must have a radio or wireline control link (a radio control link must use an auxiliary station), must limit transmissions to no more than 3 minutes after a control-link malfunction, and must be protected against unauthorized transmissions. — Source: 47 CFR §97.213(a)–(c)
- **FACT:** An auxiliary station may transmit only on the 2 m and shorter wavelength bands, except 144.0–144.5 MHz, 145.8–146.0 MHz, 219–220 MHz, 222.00–222.15 MHz, 431–433 MHz, and 435–438 MHz; it may be automatically controlled and may transmit one-way communications. — Source: 47 CFR §97.201(b), (d), (e)
- **FACT:** A repeater may be automatically controlled, and "the control operator of a repeater that retransmits inadvertently communications that violate the rules in this part is not accountable for the violative communications." — Source: 47 CFR §97.205(d), (g)
- **FACT:** Where two repeaters interfere with each other, the licensees are equally responsible for resolving it unless one repeater is frequency-coordinated — then the licensee of the non-coordinated repeater bears primary responsibility. — Source: 47 CFR §97.205(c)
- **FACT:** "A beacon must not concurrently transmit on more than 1 channel in the same amateur service frequency band, from the same station location," and "the transmitter power of a beacon must not exceed 100 W." — Source: 47 CFR §97.203(b), (c); pool G1B02, G1B10
- **FACT:** A beacon is "an amateur station transmitting communications for the purposes of observation of propagation and reception or other related experimental activities," and a beacon may transmit one-way communications. — Source: 47 CFR §97.3(a)(9), §97.203(g); pool G1B03
- **FACT:** Automatically controlled beacons are permitted on 28.20–28.30 MHz, 50.06–50.08 MHz, 144.275–144.300 MHz, 222.05–222.06 MHz, 432.300–432.400 MHz, or the 33 cm and shorter bands — the HF automatic-beacon segment is 28.20–28.30 MHz. — Source: 47 CFR §97.203(d); pool G1B09
- **FACT:** "Any amateur station may be a space station," any license class may be its control operator within class privileges, and a space station "must be capable of effecting a cessation of transmissions by telecommand whenever such cessation is ordered by the FCC." — Source: 47 CFR §97.207(a), (b)
- **FACT:** An automatically controlled station may transmit RTTY or data "on the 6 m or shorter wavelength bands, and on the 28.120-28.189 MHz, 24.925-24.930 MHz, 21.090-21.100 MHz, 18.105-18.110 MHz, 14.0950-14.0995 MHz, 14.1005-14.112 MHz, 10.140-10.150 MHz, 7.100-7.105 MHz, or 3.585-3.600 MHz segments." — Source: 47 CFR §97.221(b); pool G1E11
- **FACT:** Outside those segments, automatic control of RTTY/data is allowed only if the station "is responding to interrogation by a station under local or remote control" and no transmission exceeds 500 Hz bandwidth — so contacting an automatically controlled digital station outside the auto-control segments requires the initiating station to be under local or remote control. — Source: 47 CFR §97.221(c)(1), (2); pool G1E03
- **FACT:** "In all respects not specifically covered by FCC Rules each amateur station must be operated in accordance with good engineering and good amateur practice" — and the FCC is the arbiter of that standard. — Source: 47 CFR §97.101(a); pool G1B11
- **FACT:** "Each station licensee and each control operator must cooperate in selecting transmitting channels and in making the most effective use of the amateur service frequencies. No frequency will be assigned for the exclusive use of any station." — Source: 47 CFR §97.101(b); pool G2B01
- **FACT:** "At all times and on all frequencies, each control operator must give priority to stations providing emergency communications, except to stations transmitting communications for training drills and tests in RACES." — Source: 47 CFR §97.101(c)
- **FACT:** The five frequencies G1E10 names — 14.100, 18.110, 21.150, 24.930, and 28.200 MHz — are not set aside by Part 97; avoiding them is good amateur practice because the NCDXF/IARU international beacon network operates there, and the only automatic-beacon segment Part 97 itself designates is 28.20–28.30 MHz. — Source: 47 CFR §97.101(a), §97.203(d); pool G1E10 (see §7.9)
- **FACT:** "Each amateur station, except a space station or telecommand station, must transmit its assigned call sign on its transmitting channel at the end of each communication, and at least every 10 minutes during a communication," and unidentified transmissions are prohibited. — Source: 47 CFR §97.119(a)
- **FACT:** Station identification may be sent by CW (by an automatic device at no more than 20 words per minute), by phone in English (phonetics encouraged), by a specified RTTY/data code when the communication uses RTTY/data, or by image conforming to the applicable standards. — Source: 47 CFR §97.119(b)(1)–(4)
- **FACT:** At the end of an exchange of international third-party communications, the station must also transmit the call sign of the station with which the third-party message was exchanged. — Source: 47 CFR §97.115(d)
- **FACT:** Permitted one-way transmissions include "brief transmissions necessary to make adjustments to the station," brief transmissions establishing two-way contact, telecommand, emergency communications, "transmissions necessary to assisting persons learning, or improving proficiency in, the international Morse code," information bulletins, and telemetry. — Source: 47 CFR §97.111(b)(1)–(7); pool G1B05 (citation defect — see §7.4)
- **FACT:** Two-way communication with amateur stations in other countries is permitted "except those in any country whose administration has notified the ITU that it objects to such communications." — Source: 47 CFR §97.111(a)(1); pool G1B08
- **FACT:** Amateur stations may exchange messages only with other amateur stations (plus the specific exceptions of §97.111(a)(2)–(5), such as emergencies, RACES, and Armed Forces Day tests) — there is no authorization to communicate with non-licensed Wi-Fi stations on 2.4 GHz or anywhere else. — Source: 47 CFR §97.111(a); pool G1E07
- **FACT:** "An amateur station shall not engage in any form of broadcasting" — broadcasting meaning "transmissions intended for reception by the general public, either direct or relayed" — nor transmit one-way communications except as specifically provided. — Source: 47 CFR §97.113(b), §97.3(a)(10)
- **FACT:** Prohibited communications include communications for hire or material compensation, communications in which the licensee or control operator has a pecuniary interest (with narrow exceptions), music via phone except as provided, communications intended to facilitate a criminal act, "messages encoded for the purpose of obscuring their meaning," obscene or indecent language, and false or deceptive signals or identification — Q-signals and abbreviations are fine as long as they do not obscure meaning. — Source: 47 CFR §97.113(a)(2)–(4); pool G1B07
- **FACT:** "No station shall retransmit programs or signals emanating from any type of radio station other than an amateur station, except propagation and weather forecast information intended for use by the general public and originated from United States Government stations, and communications, including incidental music, originating on United States Government frequencies between a manned spacecraft and its associated Earth stations" — and such retransmission "may not be conducted on a regular basis, but only occasionally." — Source: 47 CFR §97.113(c); pool G1B04
- **FACT:** "No amateur station, except an auxiliary, repeater, or space station, may automatically retransmit the radio signals of other amateur station." — Source: 47 CFR §97.113(d)
- **FACT:** Third-party traffic to any station within US jurisdiction is always permitted; to foreign jurisdictions only for emergency or disaster-relief communications or where that administration "has made arrangements with the United States to allow amateur stations to be used for transmitting international communications on behalf of third parties." — Source: 47 CFR §97.115(a)(1), (2)
- **FACT:** "Transmissions to a different country, where permitted, shall be limited to communications incidental to the purposes of the amateur service and to remarks of a personal character." — Source: 47 CFR §97.117; pool G1E05
- **FACT:** A third party may participate in stating the message only while the control operator is present at the control point continuously supervising, and the third party must not be a former licensee whose license was revoked and not reinstated, suspended and still in effect, surrendered for cancellation after an enforcement notice, or the subject of an active amateur-service cease-and-desist order. — Source: 47 CFR §97.115(b)(1), (2); pool G1E01
- **FACT:** "No station may transmit third party communications while being automatically controlled except a station transmitting a RTTY or data emission" — nothing in §97.115 restricts third-party traffic by local versus remote control, so third-party messages via remote control are permitted whenever third-party messages are permitted. — Source: 47 CFR §97.115(c); pool G1E12
- **FACT:** Third-party communications are "a message from the control operator (first party) of an amateur station to another amateur station control operator (second party) on behalf of another person (third party)." — Source: 47 CFR §97.3(a)(47)
- **FACT:** "Owners of certain antenna structures more than 60.96 meters (200 feet) above ground level at the site or located near or at a public use airport must notify the Federal Aviation Administration and register with the Commission as required by part 17 of this chapter." — Source: 47 CFR §97.15(a); pool G1B01
- **FACT:** "State and local regulation of a station antenna structure must not preclude amateur service communications. Rather, it must reasonably accommodate such communications and must constitute the minimum practicable regulation to accomplish the state or local authority's legitimate purpose." — Source: 47 CFR §97.15(b) (the PRB-1 doctrine); pool G1B06
- **FACT:** "Antennas used to transmit in the 2200 m and 630 m bands must not exceed 60 meters in height above ground level." — Source: 47 CFR §97.15(c)
- **FACT:** "A station within 1600 m (1 mile) of an FCC monitoring facility must protect that facility from harmful interference." — Source: 47 CFR §97.13(b); pool G1E04
- **FACT:** Before transmitting from anywhere the station could cause human exposure above the §1.1310 limits, the licensee must ensure compliance with the FCC's RF-exposure rules — evaluation guidance is OET Bulletin 65 (Supplement B for the amateur service); household members may be evaluated against occupational/controlled limits and others against general-population/uncontrolled limits. — Source: 47 CFR §97.13(c)(1); pool G0A03, G0A06
- **FACT:** "If the routine environmental evaluation indicates that the RF electromagnetic fields could exceed the limits contained in §1.1310 of this chapter in accessible areas, the licensee must take action to prevent human exposure to such RF electromagnetic fields." — Source: 47 CFR §97.13(c)(2); pool G0A05, G0A08
- **FACT:** Spread-spectrum stations "must not cause harmful interference to stations employing other authorized emissions, and must accept all interference" from them. — Source: 47 CFR §97.311(b); pool G1E04
- **FACT:** RACES is "a radio service using amateur stations for civil defense communications during periods of local, regional or national civil emergencies." — Source: 47 CFR §97.3(a)(38)
- **FACT:** "No person may be the control operator of an amateur station transmitting in RACES unless that person holds a FCC-issued amateur operator license and is certified by a civil defense organization as enrolled in that organization." — Source: 47 CFR §97.407(a); pool G2B09
- **FACT:** "Communications for RACES training drills and tests … may not exceed a total time of 1 hour per week," except up to 72 hours no more than twice per calendar year with the approval of the chief officer for emergency planning of the applicable state or territory. — Source: 47 CFR §97.407(d)(4); pool G2B11

### 2.4 The upgrade process: exam, CSCE, immediacy, fees

- **FACT:** To upgrade from Technician to General you pass examination Element 3 only — "General Class operator: Elements 2 and 3" — because your Technician license already credits Element 2. — Source: 47 CFR §97.501(b) with §97.505(a) (verified 2026-07-24)
- **FACT:** "Each applicant must pass an examination for a new amateur operator license grant and for each change in operator class." — Source: 47 CFR §97.501 (verified 2026-07-24)
- **FACT:** "Element 3: 35 questions concerning the privileges of a General Class operator license. The minimum passing score is 26 questions answered correctly." — Source: 47 CFR §97.503(b) (verified 2026-07-24)
- **FACT:** The 2023–2027 Element 3 exam is built as 35 questions drawn one per group from the pool's 35 groups, out of a 423-question pool across 10 subelements G1–G9 and G0. — Source: `canon/pool-general.json` (counts re-verified by parse 2026-07-24); `canon/ingestion-report.md` §5.1
- **FACT:** Every examination question set must use questions from the applicable published question pool, and each pool "must contain at least 10 times the number of questions required for a single examination" and be published before use. — Source: 47 CFR §97.507(b), §97.523
- **FACT:** "Each examination for an amateur operator license must be administered by a team of at least 3 VEs at an examination session coordinated by a VEC." — Source: 47 CFR §97.509(a) (verified 2026-07-24); pool G1D04
- **FACT:** To administer a General class exam, each VE must be accredited by the coordinating VEC, be at least 18 years old, hold an Amateur Extra or Advanced class license (a General-class VE may administer Technician exams only), and never have had an amateur license revoked or suspended — and no US-citizenship requirement exists. — Source: 47 CFR §97.509(b); pool G1D02, G1D07, G1D08, G1D10
- **FACT:** VEs must grade each examination element immediately upon completion (for remotely administered exams, at the earliest practical opportunity), and the VEs alone determine the correctness of the examinee's answers. — Source: 47 CFR §97.509(h)
- **FACT:** When an examinee passes, three VEs certify that the examinee is qualified for the license grant and must issue a Certificate of Successful Completion of Examination (CSCE); when an examinee fails, the VEs must return the application document and inform the examinee of the grade. — Source: 47 CFR §97.509(i), (l), (j)
- **FACT:** No compromised examination may be administered, and the same question set may never be re-administered to the same examinee. — Source: 47 CFR §97.509(f)
- **FACT:** Under ARRL VEC retest policy, a failed element may be retaken at the same session only if the team has a different version of that element the applicant has not taken, the team has the time, resources, and willingness, and the applicant pays an additional test fee — nothing in FCC rules entitles a failed candidate to an immediate retest. — Source: ARRL Volunteer Examiner Manual, "Retesting," http://www.arrl.org/files/file/VEs/VE%20Manual%20Web%20Final%202022.pdf; Laurel VEC FAQ, https://larc-vec.org/faq.php
- **FACT:** After a successful exam the VEs submit the application to the coordinating VEC, which screens the information, resolves discrepancies, and forwards all required data to the FCC electronically. — Source: FCC, Volunteer Examiner Coordinators, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/volunteer-examiner-coordinators
- **FACT:** VECs and VEs "may be reimbursed by examinees for out-of-pocket expenses incurred in preparing, processing, administering, or coordinating an examination" — the legal basis for exam session fees. — Source: 47 CFR §97.527
- **FACT:** Administering VEs must give Element 2 credit to an examinee holding an unexpired (or in-grace-period) Technician license granted on or after March 21, 1987; a Technician license expired beyond the grace period earns no credit. — Source: 47 CFR §97.505(a)(3) (verified 2026-07-24); pool G1D01, G1D11
- **FACT:** An unexpired (or in-grace-period) Advanced, General, or pre-March-21-1987 Technician license earns Elements 2 and 3 credit (Element 3 only if expired beyond grace), and an expired-beyond-grace Amateur Extra license earns Elements 3 and 4. — Source: 47 CFR §97.505(a)(1)–(2) (verified 2026-07-24)
- **FACT:** "The administering VEs must give credit to an examinee holding a CSCE for each element the CSCE indicates the examinee passed within the previous 365 days," and a CSCE is valid for 365 days from its issue date for the element credit it conveys — no subsequently issued CSCE renews another CSCE's validity period. — Source: 47 CFR §97.505(b); ARRL Volunteer Examiner Manual, CSCE section; pool G1D09
- **FACT:** "The person named in an operator license grant of Novice, Technician, General or Advanced Class, who has properly submitted to the administering VEs a FCC Form 605 document requesting examination for an operator license grant of a higher class, and who holds a CSCE indicating that the person has completed the necessary examinations within the previous 365 days, is authorized to exercise the rights and privileges of the higher operator class until final disposition of the application or until 365 days following the passing of the examination, whichever comes first." — Source: 47 CFR §97.9(b) (verbatim, verified 2026-07-24); pool G1D03, G1D09
- **FACT:** The §97.9(b) upgrade authority has exactly two conditions, both satisfied at the exam session — the Form 605 requesting the higher class has been properly submitted to the administering VEs, and the examinee holds the CSCE showing the required element passed — and from that moment the new privileges are legal to use, before the VEC files anything and before ULS changes. — Source: 47 CFR §97.9(b) (verified 2026-07-24)
- **FACT:** While operating under §97.9(b) upgrade authority the station must append an indicator to the call sign — "for a control operator who has requested a license modification from Novice or Technician to General Class: AG" — separated from the call sign by the slant mark (/) or any suitable word denoting it. — Source: 47 CFR §97.119(f)(2), §97.119(c) (verified 2026-07-24); pool G1D06
- **FACT:** In practice, on phone you say your call sign followed by "temporary AG" (for example, "This is KX9ABC temporary AG"), on CW or digital modes you sign KX9ABC/AG, and once the upgrade shows in the FCC ULS database you drop the suffix. — Source: Laurel VEC FAQ, https://larc-vec.org/faq.php (extracted 2026-07-24; one VEC's instructions — see §7.2)
- **FACT:** The §97.9(b) interim authority ends at "final disposition of the application" — normally the grant appearing in ULS — or 365 days after passing, whichever comes first; after the grant shows, the authority rests on the license itself under §97.9(a). — Source: 47 CFR §97.9(a)–(b) (verified 2026-07-24)
- **FACT:** A brand-new licensee has no operating authority until the license grant appears in the FCC's ULS database — the wait-for-the-grant rule applies to new licenses only, while an existing licensee upgrading operates immediately under §97.9(b). — Source: FCC, Amateur Radio Service, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service (re-verified 2026-07-24); 47 CFR §97.9(b)
- **FACT:** You keep your call sign when you upgrade: "The station is reassigned its same call sign upon renewal or modification of its license, unless the licensee applies for a change to a new sequentially assigned or vanity call sign on FCC Form 605." — Source: FCC, Amateur Call Sign Systems, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/amateur-call-sign-systems (re-verified 2026-07-24)
- **FACT:** An amateur service license "is normally granted for a 10-year term." — Source: 47 CFR §97.25
- **FACT:** "A person whose amateur station license grant has expired may apply to the FCC for renewal of the license grant for another term during a 2 year filing grace period … Unless and until the license grant is renewed, no privileges in this part are conferred." — Source: 47 CFR §97.21(b)
- **FACT:** If a candidate passes multiple exam elements at one session, the VEC transmits one application to the FCC reflecting the highest license class earned. — Source: ARRL, FCC Application Fee, http://www.arrl.org/fcc-application-fee (re-verified 2026-07-24)
- **FACT:** The 2026 ARRL VEC exam session fee is $15.00, and that one fee pays for one attempt at each of the three exam elements; candidates younger than 18 pay a reduced $5.00 fee. — Source: ARRL VEC Exam Fees, http://www.arrl.org/arrl-vec-exam-fees (calendar-2026 figures, re-verified 2026-07-24; re-verify each January — see §7.13)
- **FACT:** The FCC's $35 application fee (effective April 19, 2022) applies per application to new-license, renewal, rule-waiver, and vanity-call-sign applications — and upgrade applications are exempt, so an upgrader has no FCC payment step and no 10-day payment window. — Source: ARRL, FCC Application Fee, http://www.arrl.org/fcc-application-fee (re-verified 2026-07-24; re-verify before each reprint — see §7.13)
- **FACT:** VECs and VE teams must not collect the $35 FCC fee at exam sessions; when a fee is due it is paid online directly to the FCC through the CORES payment system, never to the VE team. — Source: ARRL, FCC Application Fee, http://www.arrl.org/fcc-application-fee (re-verified 2026-07-24)
- **FACT:** Laurel VEC has administered free amateur radio license exams since 1984 and charges no fees for any licensing-related services; its website is larc-vec.org (the legacy laurelvec.com domain redirects there). — Source: Laurel VEC FAQ, https://larc-vec.org/faq.php (redirect verified 2026-07-23)
- **FACT:** The NCVEC Quick-Form 605 is the standard exam-session application: the applicant completes Section 1 (email address and FRN are mandatory), the three administering VEs print, sign, and date Section 2, and the form goes to the coordinating VEC — never directly to the FCC. — Source: ARRL, NCVEC 605 Instructions, http://www.arrl.org/605-instructions
- **FACT:** The current NCVEC Form 605 is the 2022 edition. — Source: NCVEC, https://www.ncvec.org/downloads/NCVEC_Form_605_2022.pdf (re-verified 2026-07-24; check ncvec.org for a newer revision before publication — see §7.13)
- **FACT:** An FRN (FCC Registration Number) is a 10-digit number assigned by the FCC in CORES, it is required before exam day, the Social Security number is given to the FCC inside CORES registration rather than on the exam form, and a valid email address is mandatory on the application because the FCC sends all correspondence by email. — Source: FCC CORES FAQ, https://apps.fcc.gov/cores/html/know.html; ARRL, What to Bring to an Exam Session, http://www.arrl.org/what-to-bring-to-an-exam-session
- **FACT:** Registering in CORES to get your FRN carries no fee and no exam requirement. — Source: canonical safe wording per §7.12 (no payment step exists in the CORES registration flow; FCC CORES FAQ, https://apps.fcc.gov/cores/html/know.html)
- **FACT:** Exam candidates must present one legal photo ID (or two forms of non-photo ID if none), and every applicant must answer the Basic Qualification Question (felony conviction status) on the application form. — Source: ARRL, What to Bring to an Exam Session, http://www.arrl.org/what-to-bring-to-an-exam-session
- **FACT:** Amateur exams are offered both in person and as remote video-supervised online sessions, and availability of remote testing depends entirely on the individual VE team. — Source: ARRL, Find an Amateur Radio License Exam Session, http://www.arrl.org/find-an-amateur-radio-license-exam-session (re-verified 2026-07-24); Laurel VEC FAQ (Laurel runs in-person exams only), https://larc-vec.org/faq.php
- **FACT:** HamStudy.org's session page lists both in-person and remote exam sessions run by many VE teams. — Source: https://hamstudy.org/sessions (re-verified 2026-07-24)
- **FACT:** A typical ARRL VEC exam session tests about ten people and lasts about three and a half hours. — Source: ARRL Volunteer Examiner Manual, http://www.arrl.org/files/file/VEs/VE%20Manual%20Web%20Final%202022.pdf
- **FACT:** Written question sets must be prepared by a VE holding an Amateur Extra Class license — except Element 3 sets, which an Advanced VE may prepare, and Element 2 sets, which an Advanced or General VE may prepare. — Source: 47 CFR §97.507(a)
- **FACT:** A VEC must have a written agreement with the FCC, exist to further the amateur service, coordinate exams for all license classes, and register every qualified examinee without regard to race, sex, religion, national origin, or membership (or lack thereof) in any amateur service organization. — Source: 47 CFR §97.521 (paragraph (b), the VEC-region requirement, was Reserved by 90 FR 57712 — see §7.8)
- **FACT:** "The General class license grants some operating privileges on all Amateur Radio bands and all operating modes. This license opens the door to world-wide communications." — Source: ARRL, Getting Licensed, http://www.arrl.org/getting-licensed (re-verified 2026-07-24)
- **FACT:** General does not convey everything — the lowest slices of the 80/75, 40, 20, and 15 m bands remain Advanced/Amateur Extra territory, while all amateur bands above 30 MHz are shared with Technician, Advanced, and Amateur Extra. — Source: 47 CFR §97.301(b)–(d), §97.301(a) (verified 2026-07-24)
- **FACT:** Which emission types go in which segments (phone/image versus RTTY/data) is set by §97.305 — for example on 20 m, RTTY/data 14.00–14.15 MHz and phone/image 14.15–14.35 MHz. — Source: 47 CFR §97.305 (verified 2026-07-24)
- **FACT:** Amateur Extra requires passing Element 4 (with credit for Elements 2 and 3 already earned), and "Element 4: 50 questions concerning the privileges of an Amateur Extra Class operator license. The minimum passing score is 37 questions answered correctly." — Source: 47 CFR §97.501(a), §97.503(c) (verified 2026-07-24)
- **FACT:** The current Extra class (Element 4) pool is effective 2024-07-01 and valid until 2028-06-30, and a CSCE from passing Element 3 counts toward Extra for 365 days. — Source: ARRL, Question Pools, http://www.arrl.org/question-pools (re-verified 2026-07-24); 47 CFR §97.505(b)
- **FACT:** "The Amateur Extra class license conveys all available U.S. Amateur Radio operating privileges on all bands and all modes." — Source: ARRL, Getting Licensed, http://www.arrl.org/getting-licensed (re-verified 2026-07-24)
- **FACT:** ARRL publishes graphical frequency-allocation charts by license class — the canonical visual reference for the band-by-band detail. — Source: ARRL, Graphical Frequency Allocations, https://www.arrl.org/graphical-frequency-allocations (verified 2026-07-24)
- **FACT:** The 2023–2027 General Class (Element 3) pool is effective for exams from 2023-07-01 and is valid until 2027-06-30, when the successor pool takes effect (four-year rotation; no pools updated or released in 2025 or 2029). — Source: ARRL, Question Pools, http://www.arrl.org/question-pools (re-verified 2026-07-24); NCVEC release page
- **FACT:** The NCVEC Question Pool Committee released the 2023–2027 General (Element 3) pool into the public domain. — Source: NCVEC release page, https://ncvec.org/index.php/2023-2027-general-question-pool-release (captured in `canon/source/release-page.html`, fetched 2026-07-24)
- **FACT:** The 2023–2027 General pool carries a six-errata history — Errata 1 (2023-02-01), Errata 2 (2023-04-10), 3rd errata (2023-12-01), 4th errata (2024-03-06), 5th errata (2024-11-08), 6th errata (2026-02-04) — with nine withdrawals total, and the 6th-errata release is the current document with no 7th errata as of 2026-07-24. — Source: `canon/ingestion-report.md` §5.2 (errata sheets cross-checked against the NCVEC release page)

### 2.5 HF operating practice

**Phone conventions and technique:**

- **FACT:** The voice sideband convention is LSB below 10 MHz (160, 75, and 40 meters) and USB at 10 MHz and above (20, 17, 15, 12, and 10 meters, and VHF/UHF SSB) — it is commonly accepted practice, not regulation or physics. — Source: pool G2A01, G2A02, G2A03, G2A04, G2A09; "Ethics and Operating Procedures for the Radio Amateur" ed. 3, §II.8.1 (see §7.3)
- **FACT:** HF voice is single sideband, period: an SSB signal transmits one sideband with the carrier and the other sideband suppressed, which buys less bandwidth and better power efficiency than other analog voice modes and makes SSB the narrowest phone emission. — Source: pool G2A05, G2A07, G2A06, G8A07
- **FACT:** An SSB rig's dial reads the suppressed-carrier frequency and the speech energy spreads about 3 kHz to one side — above the dial on USB, below it on LSB — so with a 3 kHz LSB signal you stay at least 3 kHz above a lower band edge and with a 3 kHz USB signal at least 3 kHz below an upper band edge. — Source: pool G4D08, G4D09, G4D10, G4D11
- **FACT:** When choosing a transmitting frequency, the minimum separation from other stations is 150 Hz to 500 Hz for CW and 2 kHz to 3 kHz for SSB. — Source: pool G2B04, G2B05
- **FACT:** Except during emergencies, no amateur has priority on any frequency — not nets, not QSOs in progress, not contests — and stations that begin interfering with each other should work it out mutually. — Source: 47 CFR §97.101(b), (c); pool G2B01, G2B03
- **FACT:** Before calling on a frequency, listen, then ask "Is this frequency in use?" followed by your call sign on phone, or send "QRL?" followed by your call on CW — and follow the voluntary band plan. — Source: pool G2B06, G2C04, G2B07
- **FACT:** If you hear a station in distress, the first thing to do is acknowledge the station and determine what assistance is needed. — Source: pool G2B02
- **FACT:** 50.100–50.125 MHz is a voluntary 6-meter DX window where, by band-plan custom, US stations in the 48 contiguous states work only stations outside the 48 contiguous states — a band plan, not FCC law. — Source: pool G2B08; ARRL band plan, https://www.arrl.org/band-plan (verified 2026-07-24)
- **FACT:** To break into a phone contact, say your call sign once during a pause between the other stations' transmissions. — Source: pool G2A08
- **FACT:** "CQ DX" called from the contiguous 48 states invites answers from stations outside the lower 48. — Source: pool G2A11
- **FACT:** VOX is hands-free transmit/receive switching operated by your voice, and PTT is the safer default in a noisy shack. — Source: pool G2A10
- **FACT:** ALC is set with the microphone gain or transmit audio control — drive the transmitter until the ALC just begins to work on peaks, because past that point the envelope flat-tops, the signal distorts, and the bandwidth splatters. — Source: pool G2A12, G8A10, G8A08, G8C13
- **FACT:** The on-air CQ pattern is "CQ" a few times, "this is," your call sign a few times, pause to listen, and repeat. — Source: pool G2D05
- **FACT:** Use the standard NATO phonetic alphabet on HF (Alfa/Alpha through Zulu) — cute alternates confuse non-English speakers exactly when clarity matters. — Source: pool G2D07; "Ethics and Operating Procedures for the Radio Amateur" ed. 3
- **FACT:** Phone signal reports use RS (readability 1–5, strength 1–9), CW adds T (tone 1–9), a "C" suffix on the report means a chirpy, unstable signal, and reports go first in an exchange so both stations can adapt to conditions. — Source: pool G2C07, G2D11
- **FACT:** Volunteer Monitors are amateurs formally enlisted — via ARRL under an FCC agreement — to watch the bands for rules violations so the service self-regulates (the program replaced the Official Observer program in 2019), and they can localize a stuck-carrier station by comparing beam headings from several locations. — Source: pool G2D01, G2D02, G2D03; arrl.org/volunteer-monitor-program (verified 2026-07-24)
- **FACT:** An azimuthal projection map centered on your location shows true bearings and distances from your station — the DXer's map — and long path means pointing the beam 180 degrees from the short-path heading. — Source: pool G2D04, G2D06
- **FACT:** Keeping a station log is voluntary, not an FCC requirement, but it helps you reply if the FCC requests information about your station. — Source: pool G2D08
- **FACT:** Contest rules never override FCC identification rules — normal Part 97 station identification applies mid-contest. — Source: pool G2D09
- **FACT:** QRP means low-power transmit operation (the roughly 5-watt figure is club and award custom, not a regulation). — Source: pool G2D10; custom per §7.11

**CW operating:**

- **FACT:** The pool's five Q-signals are: QRS? = send slower; QRL? = "are you busy? / is this frequency in use?"; QSL = "I have received and understood"; QRN = troubled by static; QRV = ready to receive. — Source: pool G2C02, G2C04, G2C09, G2C10, G2C11
- **FACT:** The prosign KN means listening only for specific station(s), and the prosign AR means end of a formal message. — Source: pool G2C03, G2C08
- **FACT:** Full break-in (QSK) means the transmitting station can receive between code characters and elements. — Source: pool G2C01
- **FACT:** Answer a CW CQ no faster than the CQ was sent, and zero beat means matching your transmit frequency to the received signal. — Source: pool G2C05, G2C06
- **FACT:** CW contest shorthand includes cut numbers — letters standing in for digits (N for 9, T for 0), so "599" is sent "5NN" — and 73 means "best regards" and is already plural, never "73s." — Source: "Ethics and Operating Procedures for the Radio Amateur" ed. 3, §II.9.22, §II.1 (verified 2026-07-24)
- **FACT:** W1AW, the ARRL headquarters station, sends daily code practice from 5 to 35 WPM plus CW, digital, and voice bulletins. — Source: ARRL W1AW schedule (arrl.org/w1aw; verified 2026-07-24 via `canon/research/r5-hf-operating.md` §4)

**Digital operating:**

- **FACT:** AFSK RTTY is traditionally sent using LSB, while JT65, JT9, FT4, and FT8 are always sent using USB — on every band, including 80 and 40 meters where voice is LSB. — Source: pool G2E01, G2E05; WSJT-X 2.7 User Guide ("WSJT-X uses upper sideband mode for both transmitting and receiving") — see §7.3
- **FACT:** The most common RTTY frequency shift on the amateur HF bands is 170 Hz (850 Hz was the old commercial standard), and RTTY uses the 45.45-baud Baudot code — a 5-bit code plus start and stop bits — whose two tones are named mark and space. — Source: pool G2E06, G8C04, G8C11
- **FACT:** If a properly tuned FSK signal will not decode, the suspects are reversed mark/space, the wrong baud rate, or the wrong sideband. — Source: pool G2E14
- **FACT:** FT8 needs computer time accurate to about 1 second — the signature symptom of a bad clock is a waterfall full of signals with zero decodes. — Source: pool G2E07; WSJT-X system requirements ±1 s (see §7.11)
- **FACT:** Answer an FT8 CQ on a clear frequency in the alternate time slot — never on the caller's own offset in the caller's slot. — Source: pool G2E04
- **FACT:** The FT8 watering-hole frequencies (all USB) are 160 m 1.840, 80 m 3.573, 40 m 7.074, 30 m 10.136, 20 m 14.074, 17 m 18.100, 15 m 21.074, 12 m 24.915, 10 m 28.074 MHz, with 6 m 50.313 MHz and 60 m 5.357 MHz — and the pool keys a common FT8 location as approximately 14.074–14.077 MHz. — Source: ARRL On The Air magazine, "Discover the Excitement of FT8," Table 1; OnAllBands/DX Engineering FT8 table (6 m/60 m values); pool G2E15 (all verified 2026-07-24; re-verify before print — see §7.13)
- **FACT:** Most digital mode operations on 20 meters are found between 14.070 MHz and 14.100 MHz. — Source: pool G2E08
- **FACT:** PSK31 hangs out at 14.070 MHz on 20 meters, near the bottom of each band's data segment, and its Varicode gives common letters short codes, so uppercase letters take longer to send. — Source: "Ethics and Operating Procedures for the Radio Amateur" ed. 3, §II.10.2; pool G8C12, G8C08 (verified 2026-07-24)
- **FACT:** FT8 is 8-tone FSK exchanging minimal messages in timed 15-second transmit/receive sequences, and an FT8 signal report of "+3" means a signal-to-noise ratio of +3 dB in a 2.5 kHz bandwidth. — Source: pool G8A09, G8C15
- **FACT:** WSPR is a weak-signal propagation beacon mode sending call sign, grid locator, and power in 2-minute sequences, with reception reports uploaded to WSPRnet to map who heard whom. — Source: pool G8C02; WSJT-X 2.7 User Guide §1 (verified 2026-07-24)
- **FACT:** Winlink is amateur radio email — wireless, working on VHF and HF, and a form of packet radio, all three descriptions true — and a Winlink "Remote Message Server" is a gateway reached by transmitting a connect message on its published frequency. — Source: pool G2E12, G2E13, G2E10
- **FACT:** VARA is a digital protocol used with Winlink; PACTOR connections are strictly two-station ARQ links you cannot join in progress; and interference to a PACTOR or VARA link shows up as retries, timeouts, pauses, or failed connects. — Source: pool G2E02, G2E09, G2E03
- **FACT:** Packet frames carry their routing and handling information in the header, NAK means "please retransmit," too many failed retries drop the connection, and forward error correction sends redundant information with the data so the receiver can fix errors without a repeat. — Source: pool G8C03, G8C05, G8C06, G8C10
- **FACT:** AREDN is high-speed amateur mesh data networking for emergencies and community events — if one node fails, a packet may still reach its target via an alternate node. — Source: pool G2E11, G8C09
- **FACT:** A waterfall display has frequency on the horizontal axis, time on the vertical axis, and signal strength as color or brightness — and vertical lines flanking a signal indicate overmodulation. — Source: pool G8C14, G8C13
- **FACT:** The digital voice modes in amateur use are DMR, D-STAR, and System Fusion. — Source: pool G8C16

**Nets, DX, contests, and QSLing:**

- **FACT:** The Maritime Mobile Service Network operates on 14.300 MHz USB daily 12:00 PM–10:00 PM Eastern, and the Hurricane Watch Net activates on 14.325 MHz USB by day and 7.268 MHz LSB by night — both are centers of activity by long custom under §97.101(b), never assigned "emergency frequencies." — Source: mmsn.org/about-us; hwn.org activation plans (both verified 2026-07-24; re-check close to print — see §7.13)
- **FACT:** Good net practice includes having a backup frequency ready in case of interference or poor conditions. — Source: pool G2B10
- **FACT:** ARES is the ARRL volunteer body anyone can join and drill with, while RACES is the FCC Part 97 civil-defense service whose control operators must be certified by a civil defense organization. — Source: pool G2B09, G2B11; arrl.org/ares (verified 2026-07-24)
- **FACT:** A contest exchange is the minimum information that scores — call sign, signal report, plus whatever the sponsor defines, such as a serial number, state or province, grid square, or ITU zone. — Source: pool G2D09; ARRL contest rules (verified 2026-07-24)
- **FACT:** Real ARRL exchange formats: ARRL DX — W/VE send RST + state/province, DX sends RST + power; November Sweepstakes — serial number, precedence, your call, check (2-digit year first licensed), ARRL/RAC section; Field Day — transmitter class + section; IARU HF — RST + ITU zone; RTTY Roundup — W/VE RST + state/province, DX RST + serial; International Digital — 4-character grid square. — Source: ARRL contest rules pages (verified 2026-07-24 via `canon/research/r5-hf-operating.md` §4)
- **FACT:** In contests the signal report is a fixed formality — "59" on phone and "599" on CW are sent regardless of actual conditions — while in everyday contacts an honest report is normal and useful. — Source: "Ethics and Operating Procedures for the Radio Amateur" ed. 3; pool G2D11 (see §7.11)
- **FACT:** No contests are held on the WARC bands (30, 17, and 12 meters) — a long-standing truce because those bands are narrow. — Source: "Ethics and Operating Procedures for the Radio Amateur" ed. 3, §II.8.6 (verified 2026-07-24)
- **FACT:** Split operation means the DX station transmits on one frequency and listens on another — when a rare station announces "listening 5 to 10 up," you call 5–10 kHz above his transmit frequency, never on it. — Source: "Ethics and Operating Procedures for the Radio Amateur" ed. 3, §II.8.1, §III.1 (verified 2026-07-24)
- **FACT:** LoTW (Logbook of The World) is the ARRL's web-accessed database where submitted electronic logs cross-match into confirmations with no paper cards needed, feeding award progress for WAS and DXCC. — Source: arrl.org/logbook-of-the-world (verified 2026-07-24)
- **FACT:** The QSL bureau route: ARRL members mail prefix-sorted DX cards to the Outgoing QSL Service (published rate as of 2026-07-24: $3.00 for 1–10 cards), and incoming cards arrive via the call-district bureau — cheap but slow, months to years. — Source: arrl.org/outgoing-qsl-service (rate as of 2026-07-24; cite "as of" or omit prices — see §7.11)
- **FACT:** "QSL" as a Q-signal means "I have received and understood" — the QSL card is literally that confirmation written out. — Source: pool G2C09
- **FACT:** SSTV calling frequencies are 3.845, 7.171, 14.230, 21.340, and 28.680 MHz, and the ISS downlinks SSTV on 437.550 MHz in Robot36 mode. — Source: ARRL band plan (verified 2026-07-24); ariss.org "Contact the ISS" (verified 2026-07-24; time-sensitive — see §7.13)
- **FACT:** The NCDXF/IARU international beacon network operates on 14.100, 18.110, 21.150, 24.930, and 28.200 MHz — tuning across the five beacons is the oldest "is the band open, and to where?" check in HF. — Source: arrl.org/considerate-operator (verified 2026-07-24); pool G1E10
- **FACT:** On 20 meters the ARRL band plan places RTTY at 14.070–14.095 MHz, packet at 14.095–14.0995 and 14.1005–14.112 MHz, NCDXF beacons at 14.100 MHz, SSTV at 14.230 MHz, and the AM calling frequency at 14.286 MHz. — Source: ARRL band plan, https://www.arrl.org/band-plan (verified 2026-07-24)
- **FACT:** AM isn't dead on HF — it has calling frequencies by custom at 3.885, 7.290, and 14.286 MHz. — Source: ARRL band plan, https://www.arrl.org/band-plan (verified 2026-07-24)

### 2.6 Propagation values

- **FACT:** More sunspots mean more ionization, so higher frequencies propagate — and when solar activity is low, the highest HF bands (15, 12, and 10 meters) become the least reliable, while 20 meters supports worldwide daylight propagation at any point in the solar cycle. — Source: pool G3A01, G3A04, G3A07
- **FACT:** A solar flare's UV and X-ray burst arrives in about 8 minutes (light-travel time) and causes a Sudden Ionospheric Disturbance that hits daytime lower HF frequencies hardest, while a coronal mass ejection's particles take 15 hours to several days to arrive. — Source: pool G3A03, G3A02, G3A11
- **FACT:** A geomagnetic storm is a temporary disturbance of Earth's magnetic field: it degrades high-latitude (polar) HF paths, but the accompanying aurora can reflect VHF signals. — Source: pool G3A06, G3A08, G3A09
- **FACT:** Charged particles from coronal holes disturb HF propagation. — Source: pool G3A14
- **FACT:** The solar flux index measures solar radio emission at 10.7 cm wavelength (2800 MHz), the K-index is the short-term (3-hour) measure of geomagnetic stability, and the A-index is the long-term (daily) measure. — Source: pool G3A05, G3A12, G3A13
- **FACT:** HF propagation conditions tend to recur every 26 to 28 days because the Sun's surface rotates on its axis in that period. — Source: pool G3A10
- **FACT:** MUF is the Maximum Usable Frequency between two specific points and LUF is the Lowest Usable Frequency; between them the ionosphere refracts signals back to Earth, below the LUF absorption kills the signal, and if the LUF rises above the MUF no ordinary skywave path exists. — Source: pool G3B08, G3B07, G3B05, G3B06, G3B11
- **FACT:** The best (least-attenuated) frequency for long-distance communication is just below the MUF, and the MUF depends on the path, time of day, season, solar radiation, and ionospheric disturbances. — Source: pool G3B03, G3B02
- **FACT:** One-hop distances are approximately 2,500 miles for the F2 region and approximately 1,200 miles for the E region. — Source: pool G3B09, G3B10
- **FACT:** Hearing your own signal return via the short path and the long path produces a slightly delayed echo. — Source: pool G3B01
- **FACT:** To check propagation conditions right now from your station, use an internet network of automated receivers to see where your signal is being heard. — Source: pool G3B04
- **FACT:** The lower HF bands suffer high atmospheric static in summer. — Source: pool G3B12
- **FACT:** The ionospheric regions from lowest to highest are D, E, F1, and F2 — and because F2 is the highest region, F2 skip is the longest. — Source: pool G3C01, G3C03
- **FACT:** The daytime D region absorbs the low bands — it is the most absorbent region below 10 MHz in daylight, which is why 40, 60, 80, and 160 meters are day-useless for long distance and open at night when the D region fades. — Source: pool G3C05, G3C11
- **FACT:** The critical frequency (at a given incidence angle) is the highest frequency refracted back to Earth, and the critical angle is the highest takeoff angle that still returns to Earth — steeper than that, the signal punches through. — Source: pool G3C02, G3C04
- **FACT:** Scatter propagation fills the skip zone: only a small fraction of the signal's energy scatters, so scatter signals are weak, arrive over multiple paths, and sound distorted with a characteristic flutter. — Source: pool G3C06, G3C07, G3C08, G3C09
- **FACT:** NVIS (near vertical incidence skywave) is high-angle, short-distance MF/HF propagation — the emergency-communications workhorse for regional coverage. — Source: pool G3C10

---

## 2.7 Technical values

**Station equipment and test measurement (G4):**

- **FACT:** A notch filter removes interfering carriers inside the receiver passband, a noise blanker mutes receiver gain during each noise pulse, and DSP noise reduction turned up too far distorts the desired signal. — Source: pool G4A01, G4A03, G4A07
- **FACT:** A receive attenuator prevents overload from strong signals, and a dual-VFO radio can transmit on one frequency while listening on another — split operation. — Source: pool G4A13, G4A12
- **FACT:** When tuning up a vacuum-tube RF amplifier, adjust TUNE for a pronounced dip in plate current (resonance) and set LOAD/COUPLING for the desired power without exceeding maximum plate current. — Source: pool G4A04, G4A08
- **FACT:** An ALC connection between exciter and amplifier prevents excessive drive — but with AFSK data modes the ALC must be inactive, because its action distorts the signal. — Source: pool G4A05, G4A11
- **FACT:** Delay RF output after keying an external amplifier so its relays can switch the antenna first — hot-switching damages the relays. — Source: pool G4A09
- **FACT:** An antenna tuner increases power transfer from the transmitter to the feed line by making the transmitter see its design load — it does not change the SWR on the feed line to the antenna. — Source: pool G4A06, G9A08
- **FACT:** An electronic keyer automatically generates the dots and dashes of Morse code. — Source: pool G4A10
- **FACT:** An oscilloscope contains horizontal and vertical channel amplifiers, beats a DVM for viewing complex waveforms, is the instrument for checking a CW keying waveform, and displays an RF envelope when fed attenuated transmitter RF output into the vertical input. — Source: pool G4B01, G4B02, G4B03, G4B04
- **FACT:** Voltmeters use high input impedance to avoid loading the circuit under test; a DMM's advantage is higher precision; an analog meter wins when adjusting a circuit for a peak or a null. — Source: pool G4B05, G4B06, G4B09
- **FACT:** A two-tone test feeds two non-harmonically related audio tones into an SSB transmitter and examines the output — it analyzes linearity. — Source: pool G4B07, G4B08
- **FACT:** A directional wattmeter reads forward and reflected power, from which SWR follows; an antenna analyzer connects to the antenna and feed line, can measure coax impedance, and nearby strong signals can corrupt its SWR readings. — Source: pool G4B10, G4B11, G4B13, G4B12
- **FACT:** A bypass capacitor shunts RF to ground and cures RFI in audio circuits, and wideband interference across many frequencies indicates arcing at a poor electrical connection. — Source: pool G4C01, G4C02
- **FACT:** In a consumer audio device, SSB RFI sounds like distorted speech and CW RFI sounds like on-and-off humming or clicking. — Source: pool G4C03, G4C04
- **FACT:** RF burns and hot chassis come from a ground wire with high impedance at the operating frequency — for example a resonant ground connection — and a ferrite choke on a cable kills common-mode RFI current. — Source: pool G4C05, G4C06, G4C08
- **FACT:** Never solder lightning-protection ground joints — lightning heat destroys solder. — Source: pool G4C07
- **FACT:** Bond equipment enclosures together to minimize ground loops (whose symptom is hum on transmitted audio) and to minimize RF hot spots in the shack, and ground all metal enclosures so hazardous voltages can never appear on the chassis. — Source: pool G4C09, G4C10, G4C11, G4C12
- **FACT:** A speech processor increases apparent loudness by raising average power while the peaks stay legal; misadjusted, it produces distorted speech, excess intermodulation, and excessive background noise. — Source: pool G4D01, G4D02, G4D03
- **FACT:** One S unit on the S meter is approximately 6 dB, so raising an S8 reading to S9 takes approximately 4 times the transmit power, and "20 dB over S9" is 100 times more powerful than S9. — Source: pool G4D06, G4D07, G4D05
- **FACT:** Worked SSB band-edge arithmetic: LSB displayed at 7.178 MHz occupies 7.175–7.178 MHz, and USB displayed at 14.347 MHz occupies 14.347–14.350 MHz. — Source: pool G4D08, G4D09
- **FACT:** A capacitance hat electrically lengthens a physically short mobile whip, and a corona ball bleeds off RF voltage at the whip tip to prevent discharge. — Source: pool G4E01, G4E02
- **FACT:** A 100-watt HF mobile rig connects directly to the battery with heavy-gauge fused wire — the vehicle's cigarette-lighter/auxiliary socket wiring cannot carry the current — and vehicle receive noise comes from the charging system, the fuel delivery system, and control computers. — Source: pool G4E03, G4E04, G4E07
- **FACT:** Shortened antennas have high Q and therefore very limited operating bandwidth, and antenna efficiency is the biggest limit on an HF mobile station's performance. — Source: pool G4E06, G4E05
- **FACT:** Solar-panel cells are wired in series-parallel for useful voltage and current; one silicon photovoltaic cell produces about 0.5 V open-circuit in full sun; a series diode stops the battery discharging back through the panel at night; and lithium iron phosphate batteries require a charge controller with the panel. — Source: pool G4E08, G4E09, G4E10, G4E11

**AC theory, reactance, resonance, power, and decibels (G5):**

- **FACT:** Reactance is the opposition to AC current flow caused by capacitance or inductance — its unit is the ohm, its letter is X, and it opposes AC without dissipating power. — Source: pool G5A02, G5A03, G5A04, G5A09, G5A11
- **FACT:** An inductor's reactance rises with frequency; a capacitor's reactance falls with frequency. — Source: pool G5A05, G5A06
- **FACT:** Impedance is the ratio of voltage to current (Ohm's law generalized to AC), admittance is the reciprocal of impedance, and RF impedance matching can use a transformer, a pi-network, or a transmission-line section — all three. — Source: pool G5A08, G5A07, G5A10
- **FACT:** At resonance X_L equals X_C and the two reactances cancel: in a series LC circuit that makes the impedance very low, and in a parallel LC circuit very high. — Source: pool G5A12, G5A01
- **FACT:** The three DC power forms are P = V × I, P = I² × R, and P = V² / R — worked pool values: 400 VDC across 800 Ω dissipates 200 W; 12 V at 0.2 A is 2.4 W; 7.0 mA through 1,250 Ω is about 61 mW; and a 50 Ω load dissipating 1,200 W has about 245 V RMS across it. — Source: pool G5B03, G5B04, G5B05, G5B12
- **FACT:** RMS is the AC value that heats a resistor exactly like the same value of DC, and for a sine wave V_rms = V_peak/√2 ≈ 0.707 × V_peak and V_pp = 2√2 × V_rms ≈ 2.828 × V_rms — so 17 V peak is about 12 V RMS, and 120 V RMS is about 339.4 V peak-to-peak. — Source: pool G5B07, G5B09, G5B08
- **FACT:** PEP is computed from the peak envelope voltage using PEP = (V_pp/(2√2))²/R = V_pp²/(8R) — 200 V peak-to-peak across 50 Ω is 100 W PEP, and 500 V peak-to-peak across 50 Ω is 625 W PEP. — Source: pool G5B06, G5B14
- **FACT:** For an unmodulated carrier, PEP equals average power — a ratio of 1.00 — so a 1,060 W average carrier is 1,060 W PEP. — Source: pool G5B11, G5B13
- **FACT:** Decibels follow dB = 10·log₁₀(P₂/P₁): a power increase to double is approximately 3 dB, and a 1 dB loss leaves 0.794 of the power — a 20.6% loss. — Source: pool G5B01, G5B10
- **FACT:** In a parallel circuit, the total current equals the sum of the branch currents. — Source: pool G5B02
- **FACT:** A transformer works by mutual inductance, its voltage ratio equals its turns ratio (a 120 VAC input on a 500-turn primary with a 1,500-turn secondary gives 360 V), and a step-up transformer's primary carries the higher current and is wound with heavier wire. — Source: pool G5C01, G5C06, G5C05
- **FACT:** Impedance transforms as the square of the turns ratio — matching 600 Ω to 50 Ω is a 12:1 impedance ratio, so the turns ratio is √12 ≈ 3.5:1. — Source: pool G5C07
- **FACT:** Resistors and inductors add in series and add-by-reciprocals in parallel, while capacitors do the opposite (reciprocals in series, plain addition in parallel) — worked pool values: 10‖20‖50 Ω ≈ 5.9 Ω; 100‖200 Ω ≈ 67 Ω; 20 mH + 50 mH series = 70 mH; three 10 mH parallel = 3.3 mH; three 100 µF series = 33.3 µF; 20 µF series 50 µF ≈ 14.3 µF; 5 nF + 5 nF + 750 pF parallel = 10.750 nF. — Source: pool G5C03, G5C04, G5C11, G5C10, G5C09, G5C12, G5C08
- **FACT:** To increase capacitance add a capacitor in parallel; to increase inductance add an inductor in series. — Source: pool G5C13, G5C14

**Components (G6):**

- **FACT:** A standard 12-volt lead-acid battery should not be discharged below 10.5 V for maximum life, and a battery's internal resistance acts like a series resistor — lower internal resistance means higher available discharge current. — Source: pool G6A01, G6A02
- **FACT:** The approximate forward threshold voltage of a germanium diode is 0.3 volts and of a silicon junction diode 0.7 volts, and an LED emits light when forward biased. — Source: pool G6A03, G6A05, G6B08
- **FACT:** Electrolytic capacitors pack high capacitance into a small volume (but are leaky, loose-tolerance, polarized, and not for RF), while low-voltage ceramic capacitors are above all cheap. — Source: pool G6A04, G6A08
- **FACT:** A wire-wound resistor's inductance makes its RF behavior unpredictable, and an inductor driven above its self-resonant frequency becomes capacitive. — Source: pool G6A06, G6A11
- **FACT:** A BJT used as a switch lives at its endpoints — saturation (fully on) and cutoff (fully off) — and a MOSFET's gate is insulated from the channel by a thin insulating layer. — Source: pool G6A07, G6A09
- **FACT:** In a vacuum tube the control grid meters electron flow from cathode to plate, and the screen grid exists to reduce grid-to-plate capacitance. — Source: pool G6A10, G6A12
- **FACT:** A ferrite core's material "mix" sets the frequency range where it works; ferrite toroids give large inductance, frequency-optimized cores, and self-contained fields; and a ferrite bead on coax chokes common-mode shield current by putting impedance in that current's path. — Source: pool G6B01, G6B05, G6B10
- **FACT:** MMIC stands for Monolithic Microwave Integrated Circuit, CMOS beats TTL on power consumption, and an op-amp is an analog IC. — Source: pool G6B02, G6B03, G6B06
- **FACT:** The BNC connector is a bayonet connector usable to about 4 GHz, the type N connector is moisture-resistant and useful to 10 GHz, the SMA is a small threaded connector good to several GHz, and the RCA phono connector is the non-RF connector used for low-frequency or DC connections to a transceiver. — Source: pool G6B04, G6B07, G6B11, G6B12

**Practical circuits (G7):**

- **FACT:** A half-wave rectifier uses one diode and converts 180 degrees of each AC cycle; a full-wave rectifier converts 360 degrees, so its unfiltered output is DC pulses at twice the AC line frequency; and the center-tapped full-wave circuit uses two diodes and a center-tapped transformer. — Source: pool G7A04, G7A05, G7A06, G7A07, G7A03
- **FACT:** Power-supply filters are built from capacitors and inductors, a bleeder resistor discharges the filter capacitors when power is removed (a safety device), and a switchmode supply's high-frequency chopping is what allows smaller, lighter components. — Source: pool G7A02, G7A01, G7A08
- **FACT:** Amplifier class describes what fraction of the cycle the device conducts: class A conducts 100 percent of the cycle (linear but inefficient), class C has the highest efficiency but distorts amplitude so it suits constant-envelope modes only (FM yes; SSB and AM no), and a linear amplifier preserves the input waveform — required for SSB. — Source: pool G7B04, G7B02, G7B11, G7B10
- **FACT:** Neutralizing an amplifier cancels internal feedback to eliminate self-oscillation, and amplifier efficiency is RF output power divided by DC input power. — Source: pool G7B01, G7B08
- **FACT:** A sine-wave oscillator is a filter plus an amplifier in a feedback loop, and an LC oscillator's frequency is set by the tank circuit's inductance and capacitance. — Source: pool G7B07, G7B09
- **FACT:** An AND gate's output is high only when both inputs are high, a 3-bit counter has 2³ = 8 states, and a shift register is a clocked array passing data along in steps. — Source: pool G7B03, G7B05, G7B06
- **FACT:** A balanced modulator produces double-sideband suppressed-carrier RF, a filter strips one sideband to make SSB, and a product detector recovers the audio in an SSB receiver. — Source: pool G7C02, G7C01, G7C04
- **FACT:** Insertion loss is attenuation inside a filter's passband, the cutoff frequency is the half-power point of a low-pass filter, ultimate rejection is the maximum stopband rejection, and band-pass bandwidth is measured between the upper and lower half-power frequencies. — Source: pool G7C07, G7C12, G7C13, G7C14
- **FACT:** Receiver sensitivity depends on input gain, demodulator bandwidth, and noise figure — all three. — Source: pool G7C08
- **FACT:** DDS gives variable frequency with crystal-oscillator stability, and DSP filters realize many bandwidths and shapes an analog filter cannot. — Source: pool G7C05, G7C06
- **FACT:** In an SDR the I and Q signals are 90 degrees apart, I/Q processing lets software create any modulation type, and filtering, detection, and modulation all happen in software. — Source: pool G7C09, G7C10, G7C11

**Signals and emissions (G8):**

- **FACT:** AM varies the signal's amplitude (instantaneous power), FM varies its instantaneous frequency, and PM varies its phase angle. — Source: pool G8A05, G8A03, G8A02
- **FACT:** Direct FSK means the digital signal drives the oscillator frequency itself, and a reactance modulator attached to an RF amplifier stage after the oscillator produces phase modulation. — Source: pool G8A01, G8A04
- **FACT:** The modulation envelope is the outline made by connecting the peaks of the RF waveform; overdriving flattens the peaks (flat-topping — distortion from excessive drive or speech levels); and overmodulation splatters into excessive bandwidth. — Source: pool G8A11, G8A10, G8A08
- **FACT:** SSB is the narrowest phone emission. — Source: pool G8A07
- **FACT:** QPSK sends data as 0°/90°/180°/270° phase shifts — two bits per symbol — and QPSK31 is sideband-sensitive, has error correction, and fits about the same bandwidth as BPSK31 (all three). — Source: pool G8A12, G8A06
- **FACT:** A link budget adds transmit power and antenna gains and subtracts all losses as seen at the receiver, and link margin is the received level minus the minimum the receiver needs. — Source: pool G8A13, G8A14
- **FACT:** Mixing two signals is heterodyning — a mixer outputs the sum and difference of the local oscillator and RF frequencies, a superheterodyne receiver is tuned by varying its local oscillator, and the image is an unwanted response twice the IF away from the desired signal. — Source: pool G8B03, G8B11, G8B01, G8B02
- **FACT:** A multiplier stage outputs a harmonic of its input — that is how a VHF FM transmitter reaches its operating frequency from a lower-frequency oscillator. — Source: pool G8B04
- **FACT:** Signals combining in a non-linear circuit spawn spurious products called intermodulation; a product's order is the sum of its mixing coefficients; odd-order products land closest to the original frequencies; and 2F1 − F2 is the odd-order example (order 3). — Source: pool G8B12, G8B05, G8B13
- **FACT:** Carson's rule gives FM bandwidth as approximately 2 × (peak deviation + highest modulating frequency) — 5 kHz deviation with 3 kHz audio gives 16 kHz — and deviation multiplies through a multiplier chain by the same factor as the carrier, so a 146.52 MHz transmitter with a 12.21 MHz oscillator (factor 12) needs 5 kHz ÷ 12 = 416.7 Hz of oscillator deviation for 5 kHz output deviation. — Source: pool G8B06, G8B07
- **FACT:** High-duty-cycle modes (FT8, RTTY, FM) run the transmitter hard — average power can exceed ratings even when PEP is fine; matching receiver bandwidth to the mode gives the best signal-to-noise ratio; and higher symbol rates require wider bandwidth. — Source: pool G8B08, G8B09, G8B10

**Antennas and feed lines (G9):**

- **FACT:** A parallel-conductor feed line's characteristic impedance is set by the conductor spacing (center-to-center) and the conductor radius — not by length or frequency — and window/ladder line is approximately 450 ohms. — Source: pool G9A01, G9A03
- **FACT:** Coax loss rises with frequency and is quoted in dB per 100 feet; high SWR makes a lossy line lose more; and line loss makes SWR measured at the shack end look better than it really is. — Source: pool G9A05, G9A06, G9A02, G9A11
- **FACT:** Reflected power comes from a mismatch between the feed line and the antenna feed-point impedance, and the way to eliminate standing waves is to match the feed point to the line. — Source: pool G9A04, G9A07
- **FACT:** SWR from a resistive mismatch is Z_load ÷ Z₀ or Z₀ ÷ Z_load, whichever is greater than or equal to 1 — 200 Ω on 50 Ω coax is 4:1, and 10 Ω on 50 Ω coax is 5:1 — and SWR is always stated with the larger number first. — Source: pool G9A09, G9A10
- **FACT:** A free-space half-wave dipole radiates a figure-eight pattern broadside to the wire with nulls off the ends, while a quarter-wave ground plane is omnidirectional in azimuth. — Source: pool G9B04, G9B03
- **FACT:** Below a half-wavelength high, a horizontal dipole's high-angle pattern goes nearly omnidirectional and its feed-point impedance steadily decreases toward 0.1-wavelength height. — Source: pool G9B05, G9B07
- **FACT:** Moving a dipole's feed point from the center toward the ends raises the feed-point impedance; ground-plane radials sloped downward raise the roughly 35 Ω feed point toward 50 Ω; and radials for a ground-mounted vertical lie on the surface or buried a few inches. — Source: pool G9B08, G9B02, G9B06
- **FACT:** Horizontal polarization's HF advantage is lower ground losses, and a random wire connected directly to the rig can put significant RF current on station equipment. — Source: pool G9B09, G9B01
- **FACT:** The approximate length of a half-wave dipole in feet is 468 divided by the frequency in MHz (33 feet for 14.250 MHz, 132 feet for 3.550 MHz), and a quarter-wave monopole is 234 divided by the frequency in MHz (8 feet for 28.5 MHz) — the 468 constant includes the roughly 5 percent end-effect shortening. — Source: pool G9B10, G9B11, G9B12
- **FACT:** A Yagi's driven element is approximately a half wavelength, its reflector is longer and its director shorter than the driven element, and a longer boom with more directors gives more gain. — Source: pool G9C02, G9C03, G9C05
- **FACT:** Front-to-back ratio compares the power radiated in the main lobe to the power radiated in the opposite direction, and the main lobe is the direction of maximum radiated field. — Source: pool G9C07, G9C08
- **FACT:** Fatter antenna elements widen bandwidth, and gain, front-to-back ratio, and SWR bandwidth all trade off through boom length, element count, and spacing. — Source: pool G9C01, G9C10
- **FACT:** Antenna gain in dBi is 2.15 dB higher than the same gain in dBd — dBi = dBd + 2.15, dBi the bigger number. — Source: pool G9C04
- **FACT:** Two identical Yagis stacked a half-wavelength apart gain approximately 3 dB over one. — Source: pool G9C09
- **FACT:** A beta (hairpin) match is a shorted stub at the feed point, and a gamma match needs no insulation of the driven element from the boom. — Source: pool G9C11, G9C12
- **FACT:** NVIS antennas are horizontal dipoles 0.1 to 0.25 wavelengths up for short-skip regional coverage, and an end-fed half-wave antenna presents a very high feed-point impedance. — Source: pool G9D01, G9D02
- **FACT:** A halo antenna is omnidirectional in its own plane; traps make one antenna multiband; and multiband antennas pay with poor harmonic rejection. — Source: pool G9D03, G9D04, G9D11
- **FACT:** Stacking antennas vertically narrows the main lobe in elevation, and a log-periodic antenna trades everything for wide bandwidth with element length and spacing varying logarithmically along the boom. — Source: pool G9D05, G9D06, G9D07
- **FACT:** A screwdriver antenna tunes by varying its base-loading inductance; a Beverage is a directional receiving antenna for MF and low HF; an electrically small loop's nulls are broadside to the loop; and a dipole with a single central support is an inverted V. — Source: pool G9D08, G9D09, G9D10, G9D12

**Safety and RF exposure (G0):**

- **FACT:** RF energy's established effect on body tissue is heating — RF is non-ionizing radiation, so "radiation poisoning" is not the hazard. — Source: pool G0A01
- **FACT:** RF exposure depends on frequency, power density, and duty cycle — all three. — Source: pool G0A02
- **FACT:** All stations with a time-averaged transmission of more than one milliwatt are subject to the FCC's RF-exposure rules. — Source: pool G0A12
- **FACT:** A station that doesn't meet the exemption criteria must perform an exposure evaluation per FCC OET Bulletin 65, and acceptable ways to show compliance are OET-65 calculation, computer modeling, or measurement with calibrated field-strength equipment — any of the three. — Source: pool G0A06, G0A03
- **FACT:** The ongoing RF-safety duty is to evaluate the station routinely and keep people out of identified high-exposure areas. — Source: pool G0A08
- **FACT:** Time averaging is total exposure averaged over a period — which is why a lower duty cycle permits higher power for the same exposure. — Source: pool G0A04, G0A07
- **FACT:** If an evaluation shows limits could be exceeded, act to prevent human exposure — power down, raise the antenna, or restrict access — and if a directional antenna's main lobe could hit a neighbor's space, ensure it cannot be pointed at them while they are present. — Source: pool G0A05, G0A10; 47 CFR §97.13(c)(2)
- **FACT:** Indoor antennas must keep occupied areas under MPE limits, and measuring RF fields for compliance requires a calibrated field-strength meter with a calibrated antenna — SWR meters and receivers don't qualify. — Source: pool G0A11, G0A09
- **FACT:** In a 240 VAC four-conductor circuit, only the hot wires get fuses or breakers — never the neutral or the ground. — Source: pool G0B01
- **FACT:** Wire must handle the breaker's rating: a 20 A circuit needs AWG 12 minimum, and AWG 14 wire pairs with a 15 A fuse or breaker. — Source: pool G0B02, G0B03 (NEC ampacity, NFPA 70)
- **FACT:** The National Electrical Code (NEC) covers the electrical safety of the station, and a GFCI trips when current flows from a hot wire directly to ground — the missing return current is what it detects. — Source: pool G0B06, G0B05
- **FACT:** The lightning-protection ground system goes outside the building, lightning arrestors mount where feed lines enter the building, and all ground rods must be bonded together with the other premises grounds. — Source: pool G0B04, G0B13, G0B11
- **FACT:** Before climbing, confirm the harness is rated for the climber's weight and within its service life, and before climbing a tower with powered devices, lock out and tag every circuit feeding the tower. — Source: pool G0B07, G0B08
- **FACT:** Generators run in well-ventilated areas because carbon monoxide is the killer; lead-tin solder's danger is lead contaminating food via unwashed hands; and a power-supply interlock removes dangerous voltages when the cabinet is opened. — Source: pool G0B09, G0B10, G0B12

---

## 3. Notation & Units

One consistent style for the whole book — identical to Book 2's canon wherever the two overlap. Frequencies are in hertz with kHz/MHz/GHz as convenient; wavelength in meters; metric throughout, with US-conventional ham units only where the hobby genuinely uses them (feet for antenna lengths and tower clearances, miles for propagation hop distances — the General pool itself prints "approximately 2,500 miles," "33 feet," "dB per 100 feet").

| Symbol | Quantity | Unit | Canonical relation / note |
|---|---|---|---|
| V | Voltage (EMF) | volt (V) | **V = I × R** (Ohm's law); prose uses V, never E (see below) |
| I | Current | ampere (A) | I = V / R; the flow of electrons |
| R | Resistance | ohm (Ω) | R = V / I; dissipates power |
| P | Power | watt (W) | **P = V × I = I² × R = V² / R** |
| f | Frequency | hertz (Hz; kHz, MHz, GHz) | Cycles per second; f = 1 / T |
| λ | Wavelength | meter (m) | **λ = c / f**; the band-name basis |
| c | Speed of light | m/s | ≈ 3×10⁸ m/s = 300,000 km/s (working value); 299,792,458 m/s (exact) |
| C | Capacitance | farad (F) | Energy stored in an electric field |
| L | Inductance | henry (H) | Energy stored in a magnetic field |
| X | Reactance | ohm (Ω) | Opposition to AC from L or C; stores and returns, never dissipates |
| Z | Impedance | ohm (Ω) | Opposition to AC: resistance + reactance; magnitude **\|Z\| = √(R² + X²)** |
| N | Turns (transformer) | — | V_s = V_p × (N_s/N_p); Z_p/Z_s = (N_p/N_s)² |

**The wavelength shortcut:** the book states, as the pool's own formula family, **λ(m) = 300 / f(MHz)** — an approximation of c = f·λ with c ≈ 3×10⁸ m/s, never an exact identity (series-identical to Book 2).

**Decibels:** anchors first, series-identical to Book 2 — **3 dB ≈ double power, 6 dB ≈ four times power (so −6 dB ≈ one quarter), 10 dB = ten times power** — plus the General anchors **20 dB = 100 times power, one S unit ≈ 6 dB, and a 1 dB loss leaves 0.794 of the power (−20.6%)**. Deliberate difference from Book 2, stated openly: the defining formula **dB = 10·log₁₀(P₂/P₁)** is first-class exam math in this book (pool G5B10, G4D05), not sidebar material — the General pool tests it, so ch05 teaches it with worked numbers.

**Pool-notation equivalence (binding, series-consistent):** prose in this book uses **V** for voltage and **×** as the multiplication sign (V = I × R, P = V × I), exactly as Book 2 does. The 2023–2027 General pool states electrical quantities in words ("200 volts peak-to-peak across a 50-ohm dummy load") — no formula typography occurs anywhere in the pool text, so verbatim pool quotes never conflict with the prose convention. Where the book refers back to Book 2's E-notation equivalence ("E and V both mean volts"), a single parenthetical suffices.

**The General formula set (canonical relations — Appendix B reproduces this table; each formula is used at least once in its chapter with pool numbers):**

| Formula | Name | Pool worked example |
|---|---|---|
| X_L = 2πfL | Inductive reactance | 20 mH at 7 MHz ≈ 880 kΩ (concept per G5A05; numbers from G5C11) |
| X_C = 1/(2πfC) | Capacitive reactance | 100 µF at 60 Hz ≈ 26.5 Ω (concept per G5A06; numbers from G5C09) |
| f = 1/(2π√(LC)) | Resonant frequency | 10 mH with 100 µF ≈ 159 Hz (G5C10 with G5C09) |
| X_L = X_C at resonance | Resonance condition | Series LC → very low impedance; parallel LC → very high (G5A01, G5A12) |
| \|Z\| = √(R² + X²); φ = arctan(X/R) | Impedance magnitude and phase | 50 Ω + j50 Ω → \|Z\| ≈ 70.7 Ω, φ = 45° |
| P = V × I = I² × R = V² / R | Power | 400 V across 800 Ω → 200 W (G5B03) |
| V_rms = V_peak/√2 ≈ 0.707·V_peak | RMS of a sine | 17 V peak ≈ 12 V RMS (G5B09) |
| V_pp = 2√2·V_rms ≈ 2.828·V_rms | Peak-to-peak | 120 V RMS ≈ 339.4 V p-p (G5B08) |
| PEP = V_pp²/(8R) | Peak envelope power | 200 V p-p into 50 Ω → 100 W (G5B06); 500 V p-p → 625 W (G5B14) |
| dB = 10·log₁₀(P₂/P₁) | Decibels | ×2 ≈ 3 dB (G5B01); 1 dB loss = −20.6% (G5B10); 20 dB = ×100 (G4D05) |
| SWR = Z_load/Z₀ (or inverse, ≥ 1) | SWR, resistive mismatch | 200 Ω on 50 Ω → 4:1 (G9A09); 10 Ω on 50 Ω → 5:1 (G9A10) |
| SWR = (1+√(P_r/P_f))/(1−√(P_r/P_f)) | SWR from forward/reflected power | stated with the directional wattmeter (G4B10) |
| L(ft) = 468/f(MHz) | Half-wave dipole length | 14.250 MHz → ≈33 ft (G9B10); 3.550 MHz → ≈132 ft (G9B11) |
| L(ft) = 234/f(MHz) | Quarter-wave monopole length | 28.5 MHz → ≈8 ft (G9B12) |
| dBi = dBd + 2.15 | Gain units | dBi is the bigger number (G9C04) |
| BW ≈ 2 × (peak deviation + highest modulating frequency) | Carson's rule (FM bandwidth) | 2 × (5 kHz + 3 kHz) = 16 kHz (G8B06) |
| deviation multiplies by the chain factor | Deviation through a multiplier chain | 146.52/12.21 = 12 → 5 kHz/12 = 416.7 Hz (G8B07) |
| V_s = V_p × (N_s/N_p) | Transformer voltage ratio | 120 V, 500→1500 turns → 360 V (G5C06) |
| Z_p/Z_s = (N_p/N_s)² | Transformer impedance ratio | 600 Ω:50 Ω = 12:1 → turns √12 ≈ 3.5:1 (G5C07) |
| R, L add in series / by reciprocals in parallel; C opposite | Series-parallel combinations | G5C03–G5C14 worked set (§2.7) |
| n bits → 2ⁿ states | Binary counter | 2³ = 8 (G7B05) |
| η = P_RF-out / P_DC-in | Amplifier efficiency | definition only (G7B08) |
| full-wave ripple = 2 × line frequency | Rectifier ripple | conceptual (G7A07) |

**Unit style rules (series-identical to Book 2, with General additions):**
- Case is load-bearing: **kHz** (lowercase k), **MHz** and **GHz** (capital M/G), always capital **H**; **mA**, **µV**, **pF**, **nF**, **kV** follow the same prefix case rules. Never "KHZ," "mhz," or "Mhz."
- Prefix ladder for conversions: pico (10⁻¹²) → nano (10⁻⁹) → micro (10⁻⁶) → milli (10⁻³) → base → kilo (10³) → mega (10⁶) → giga (10⁹); moving toward a smaller unit multiplies, toward a larger unit divides. (G5C08's nF/pF mix is the pool's own drill — answer printed "10.750 nF" with the trailing zero.)
- Band names take the meter spelling with a numeral ("40 meters," "70 centimeters," "20 m" in tables); frequency ranges are written with an en dash and units once ("14.225–14.350 MHz").
- Power limits are written "200 W PEP," "1.5 kW PEP," "1500 watts," "100 W ERP," "9.15 W ERP" matching the rules' and pool's own phrasing where quoted.
- Antenna lengths from the 468/f and 234/f formulas come out in **feet** and are stated as approximate ("approximately 33 feet").
- Coax loss is quoted in **dB per 100 feet** (the pool's unit).
- SWR is always written with the larger number first — "4:1," "5:1," never "1:4."
- SSB dial readings are suppressed-carrier frequencies; sideband occupancy is written "the signal occupies 7.175–7.178 MHz," not by edge-frequency shorthand alone.
- Inline math in chapters uses the `$…$` renderer; at most one `$…$` span per paragraph and no literal `$` inside a math paragraph (write "35 dollars" in prose). The renderer's subset supports subscripts ($X_L$), $\pi$, $\sqrt{}$, and fractions — the whole General formula set above.

---

## 4. Glossary

Canonical plain-language one-line definitions, consolidated from the r3/r4/r5 vocabulary lists. These are binding — a chapter may expand a definition but must not contradict it — and this table feeds Appendix B directly. Series law: where a term also appears in Book 2's canon §4, the definition below is Book 2's **verbatim** (the only exceptions are figure cross-references, which point at this book's pool figure). Terms new to the General course carry new definitions in the same style.

| Term | Definition |
|---|---|
| A-index | The long-term (daily) index of geomagnetic stability. |
| AC (alternating current) | Current that alternates between positive and negative directions. |
| Admittance | The reciprocal of impedance — how easily AC flows. |
| AFSK | Audio frequency-shift keying — digital data sent as shifting audio tones into a voice transmitter. |
| AGC (automatic gain control) | Receiver circuit that automatically turns gain down on strong signals to keep audio level. |
| ALC (automatic level control) | The transmitter feedback circuit that limits drive to prevent overload — set it so it just begins to work on peaks. |
| Allocation | A frequency band assignment made to a radio service by regulation. |
| AM (amplitude modulation) | Impressing information on a carrier by varying its amplitude; SSB is a form of AM. |
| Amateur Extra | The highest US license class, conveying all available US amateur privileges on all bands and modes. |
| Ampere (A) | The unit of electric current. |
| Ampere-hour (Ah) | A battery capacity unit: one ampere flowing for one hour. |
| AND gate | A digital gate whose output is high only when both inputs are high. |
| Antenna analyzer | An instrument that tells whether an antenna is resonant at a chosen frequency. |
| Antenna tuner (coupler/transmatch) | A device that matches the antenna system impedance to the transceiver's 50-ohm output. |
| Anode | The diode electrode current enters in the forward direction. |
| AREDN | Amateur Radio Emergency Data Network — high-speed mesh data networking on microwave amateur allocations for emergencies and community events. |
| ARQ (automatic repeat request) | Error recovery in which the receiver detects errors and requests retransmission. |
| ARES | Amateur Radio Emergency Service — licensed amateurs who voluntarily registered their qualifications and equipment for public-service duty. |
| Attenuator (receiver) | A switchable pad that reduces incoming signal strength to prevent receiver overload. |
| Auroral backscatter | VHF signals returned by the aurora, distorted with a characteristic raspy sound. |
| Automatic control | Operation of a transmitting station by devices and procedures without the control operator present at a control point. |
| Auxiliary station | An amateur station transmitting point-to-point communications within a system of cooperating stations, such as a repeater's remote link. |
| Average power | Power averaged over a full modulation cycle — what heats the finals; PEP measures the crest instead. |
| AWG | American Wire Gauge — the wire-size scale the NEC's ampacity rules use (AWG 12 for 20 A, AWG 14 for 15 A). |
| Azimuthal projection | A map projection centered on your location showing true bearings and distances — the DXer's map. |
| Balanced modulator | The circuit that produces double-sideband suppressed-carrier RF — the first step in making SSB. |
| Band plan | A voluntary community guideline for which modes and activities live where within a band. |
| Band-reject filter | A filter that blocks a chosen band of frequencies while passing the rest. |
| Bandwidth | The width of spectrum a signal occupies (e.g., ≈3 kHz for SSB voice). |
| Basis and purpose | The five-pronged mission statement of the Amateur Radio Service in §97.1. |
| Baud | The symbol rate of a digital signal — symbols per second. |
| Baudot code | The 5-bit RTTY code sent with start and stop bits (45.45 baud on HF). |
| Beacon (propagation) | An amateur station transmitting for observation of propagation and reception (on HF, 28.200–28.300 MHz on 10 m). |
| Beam antenna | A directional antenna that concentrates signals in one direction. |
| Beta match (hairpin) | A shorted stub at the antenna feed point used for matching. |
| Beverage antenna | A long low wire used as a directional receiving antenna on MF and low HF. |
| BJT (bipolar junction transistor) | A transistor family whose electrodes are emitter, base, and collector. |
| Bleeder resistor | The resistor that discharges a power supply's filter capacitors when power is removed — a safety device. |
| BNC | A bayonet RF connector usable to about 4 GHz. |
| Bonding | Electrically connecting equipment and ground rods with low-inductance conductors so everything sits at the same potential. |
| Boom | The longitudinal spine of a Yagi that the elements mount on. |
| Break-in (full, QSK) | CW operating where the transmitting station can receive between code characters and elements. |
| Broadside | The direction perpendicular to a dipole's wire, where it radiates strongest. |
| Broadcasting | Transmissions intended for reception by the general public — prohibited in the amateur service. |
| Bypass capacitor | A capacitor that shunts RF to ground, curing RFI in audio circuits. |
| Capacitance | The ability to store energy in an electric field; unit farad. |
| Capacitance hat | The spoke-like conductor crown on a short mobile whip that electrically lengthens it. |
| Capacitor | A component that stores energy in an electric field — two conductive plates separated by a dielectric. |
| Carrier | The unmodulated RF signal onto which information is impressed. |
| Carson's rule | The FM bandwidth estimate: bandwidth ≈ 2 × (peak deviation + highest modulating frequency). |
| Cathode | The diode electrode current exits in the forward direction; the package end is often marked with a stripe. |
| Center-tapped transformer | A transformer with a mid-winding tap; with two diodes it makes a full-wave rectifier. |
| Ceramic capacitor | A capacitor valued above all for low cost, not precision. |
| Charge controller | The regulator between a solar panel and a battery; lithium iron phosphate batteries require one. |
| Chassis ground | Bonding of metal equipment enclosures so hazardous voltages can never appear on the case. |
| Checksum | Extra data in a packet that lets the receiver detect transmission errors. |
| Chirp | An unstable, drifting note on a CW signal — reported with a "C" suffix on the RST. |
| Circuit breaker | A resettable device that removes power when current exceeds its rating. |
| Class A amplifier | An amplifier conducting 100% of the cycle — linear but inefficient. |
| Class C amplifier | The highest-efficiency amplifier class — constant-envelope modes only (FM yes; SSB and AM no). |
| CMOS | The digital IC family that beats TTL on power consumption. |
| Coaxial cable (coax) | A shielded feed line with a center conductor inside a cylindrical braid; amateur coax is usually 50 ohms. |
| Cold solder joint | A defective solder joint that looks rough or lumpy instead of shiny and smooth. |
| Common-mode current | RF current flowing on the outside of a cable shield — choked with a ferrite bead. |
| Conductor | A material that carries current easily because it has many free electrons. |
| Contest exchange | The minimum information that scores a contest contact: call sign, signal report, plus the sponsor's defined fields. |
| Control grid | The vacuum-tube element that meters electron flow from cathode to plate. |
| Control operator | The licensed amateur designated by the station licensee to be responsible for the station's transmissions. |
| Control point | The location at which the control operator function is performed. |
| Controlled environment | The RF-exposure category for people aware of and able to control their exposure (occupational-level limits; may apply to household members). |
| CORES | The FCC's COmmission REgistration System, where you register to get an FRN. |
| Corona ball | The smooth ball on a mobile whip tip that bleeds off RF voltage to prevent discharge. |
| Coronal hole | A cooler solar region whose charged-particle streams disturb HF propagation. |
| Coronal mass ejection (CME) | A burst of solar particles that reaches Earth in 15 hours to several days and disturbs the geomagnetic field. |
| CQ | The general call inviting any station to reply ("calling any station") — used on simplex and HF, not on repeaters. |
| CQ DX | A CQ inviting answers only from distant stations — called from the lower 48, it invites stations outside the lower 48. |
| Critical angle | The highest takeoff angle that the ionosphere still refracts back to Earth. |
| Critical frequency | The highest frequency the ionosphere refracts back to Earth at a given incidence angle. |
| CSCE | Certificate of Successful Completion of Examination — the VEs' proof you passed, valid 365 days for element credit. |
| Current | The flow of electrons in a circuit; unit ampere. |
| Cut numbers | CW contest shorthand where letters stand in for digits (N for 9, T for 0) — "599" sent as "5NN." |
| Cutoff | The fully-off endpoint of a switching transistor's operation. |
| Cutoff frequency | The half-power point of a low-pass filter. |
| CW | Continuous wave — a carrier keyed on and off; simply another name for a Morse code transmission. |
| D region | The lowest ionospheric region — the daytime absorber of the low HF bands, fading at night. |
| dBd | Antenna gain relative to a half-wave dipole. |
| dBi | Antenna gain relative to an isotropic radiator — dBi = dBd + 2.15. |
| DC (direct current) | Current that flows steadily in one direction. |
| DDS (direct digital synthesis) | A frequency-generation technique giving variable frequency with crystal-oscillator stability. |
| Decibel (dB) | A logarithmic ratio unit: +3 dB ≈ double power, +10 dB = ten times power. |
| Deviation | The peak amount an FM carrier's frequency swings with modulation; too much is over-deviation. |
| Dielectric | The insulating material between a capacitor's plates (or inside a coaxial cable). |
| Digital mode | A mode carrying data rather than analog voice — packet radio, FT8, even IEEE 802.11 under amateur rules. |
| Digital voice | Voice sent as data — the amateur trio is DMR, D-STAR, and System Fusion. |
| Diode | A semiconductor that lets current flow in only one direction. |
| Dipole | A straight antenna, usually a half wavelength long, fed at the center. |
| Director | The Yagi element shorter than the driven element, sitting in the direction of maximum radiation. |
| Directional wattmeter | An instrument reading forward and reflected power, used to determine SWR. |
| DMM (digital multimeter) | The high-precision meter for voltage, current, and resistance. |
| DMR (Digital Mobile Radio) | A digital voice standard that time-multiplexes two conversations on one 12.5 kHz channel. |
| Driven element | The Yagi element connected to the feed line, approximately a half wavelength long. |
| DSP (digital signal processing) | Signal manipulation in software — DSP filters realize bandwidths and shapes analog filters cannot. |
| Dummy load | A fake antenna — a 50-ohm non-inductive resistor on a heat sink — for testing without going on the air. |
| Duty cycle | The percentage of time that a transmitter is transmitting during the averaging time for RF exposure. |
| Duty factor | The fraction of time a transmitter is on during an operating cycle — high-duty modes (FT8, RTTY, FM) stress the finals. |
| DX window | A voluntary band-plan segment where local stations keep quiet so weak DX can be heard (6 m: 50.100–50.125 MHz). |
| DXpedition | An expedition to activate a rare location, publishing its band, mode, and split plans in advance. |
| E region | The ionospheric region above the D region — one-hop reach about 1,200 miles. |
| Efficiency (amplifier) | RF output power divided by DC input power. |
| EIRP | Effective radiated power computed relative to an isotropic antenna — how the 2200 m/630 m limits are stated. |
| Electric field | The field between points at different voltages; a radio wave's polarization is defined by this field's orientation. |
| Electrolytic capacitor | A polarized capacitor packing high capacitance into a small volume — leaky, loose-tolerance, not for RF. |
| Electromagnetic wave | A traveling pair of electric and magnetic fields at right angles — a radio wave. |
| Electronic keyer | A device that forms Morse dits and dahs for you when you work the paddle. |
| Element credit | Examination credit for a written element, earned by a license grant or a CSCE per §97.505. |
| Emission bandwidth | The width of spectrum an emission occupies — capped at 2.8 kHz on 60 m and for HF data modes. |
| Emission mode | The type of signal a transmitter produces (CW, phone, data, image, and so on). |
| EME (Earth-Moon-Earth) | Bouncing signals off the Moon to reach distant stations. |
| End-fed half-wave | A half-wave antenna fed at one end — its feed-point impedance is very high. |
| ERP (effective radiated power) | Transmitter PEP times antenna gain relative to a half-wave dipole — how the 60 m limits are stated. |
| F region | The high ionospheric region responsible for long-distance HF skip. |
| Fading | Signal strength rising and falling, usually from multipath combining. |
| FEC (forward error correction) | Sending redundant information with the data so the receiver can fix errors without a repeat. |
| Feed line | The cable that carries RF between the transceiver and the antenna. |
| Feed-point impedance | The impedance at the antenna's feed terminals — what the feed line sees. |
| Ferrite choke | A clip-on ferrite core on a cable that blocks unwanted RF current on the outside of the cable. |
| Ferrite mix | The material formulation of a ferrite core that sets its working frequency range. |
| FET (field-effect transistor) | A transistor family whose electrodes are gate, drain, and source. |
| Figure-eight pattern | The dipole's free-space radiation pattern — strongest broadside, nulls off the ends. |
| Filter bandwidth | The width of a receiver's selectable passband, matched to the mode (≈2400 Hz for SSB). |
| Flat-topping | Envelope clipping from excessive drive or speech levels — audible distortion and splatter. |
| FM (frequency modulation) | Impressing information on a carrier by varying its frequency. |
| Form 605 | The FCC/NCVEC application form used at exam sessions and for license changes. |
| Forward power | The power traveling from transmitter toward antenna, as read by a directional wattmeter. |
| Forward threshold voltage | The minimum forward voltage for a diode to conduct — about 0.3 V for germanium, 0.7 V for silicon. |
| Fox / hound | FT8 DXpedition roles: the DX "fox" works many calling "hounds" at once. |
| Free space | Ideal empty space, where every radio wave travels at the speed of light. |
| Frequency | The number of complete cycles per second; unit hertz. |
| Frequency coordinator | A volunteer entity recognized by local amateurs that recommends repeater/auxiliary channels and parameters to minimize interference. |
| FRN | FCC Registration Number — a 10-digit identifier for all your FCC business, obtained free in CORES before exam day. |
| Front-to-back ratio | The ratio of power radiated in the main lobe to power radiated in the opposite direction. |
| FT8 | A weak-signal digital mode exchanging minimal messages in timed 15-second sequences. |
| Full-wave rectifier | A rectifier converting all 360° of each AC cycle — its ripple runs at twice the line frequency. |
| Fundamental overload | Receiver disruption caused by a strong signal the receiver cannot reject — the problem is in the receiver. |
| Fuse | A sacrificial device that melts to remove power when current exceeds its rating. |
| Gain (amplifier) | Output compared to input — of voltage, current, or power. |
| Gain (antenna) | The increase in signal strength in a specified direction compared to a reference antenna, achieved by focusing. |
| Gamma match | A Yagi feed-point matching device needing no insulation of the driven element from the boom. |
| Gateway | An amateur station that connects other amateur stations to the internet. |
| GECOA | Global Emergency Center of Activity — IARU-recognized HF emergency frequencies (e.g., 14.300 MHz). |
| Geomagnetic storm | A temporary disturbance of Earth's magnetic field that degrades high-latitude HF paths. |
| GFCI | Ground-fault circuit interrupter — trips when current flows from a hot wire directly to ground. |
| Giga- | Metric prefix for 10⁹ (GHz = gigahertz). |
| Grace period | The two years after expiration during which a license may still be renewed — with no transmitting until the renewal is granted. |
| Gray line | Earth's day/night terminator — a window of enhanced low-band propagation around sunrise and sunset. |
| Grid locator | A letter-number designator for a geographic location in the Maidenhead system (e.g., "FN31"). |
| Ground loop | Unwanted current circulating between interconnected equipment grounds — its symptom is hum on transmitted audio. |
| Ground plane | A vertical antenna working against radials — omnidirectional in azimuth. |
| Ground rod | A metal rod driven into the earth for safety and lightning grounds; amateur towers use eight-foot rods, bonded together. |
| Half-power point | The frequency where a filter's response falls to half power — band-pass bandwidth is measured between the upper and lower ones. |
| Half-wave rectifier | A one-diode rectifier converting 180° of each AC cycle. |
| Halo antenna | A horizontally polarized mobile antenna, omnidirectional in its own plane. |
| Harmful interference | Interference that seriously degrades, obstructs, or repeatedly interrupts a radio service. |
| Harmonic | A spurious emission at an integer multiple of the transmit frequency. |
| Hertz (Hz) | The unit of frequency: one cycle per second. |
| Heterodyning | Mixing two signals to produce the sum and difference frequencies. |
| HF | High frequency: 3–30 MHz — the long-distance "shortwave" amateur bands. |
| Hop | One ionospheric bounce — about 2,500 miles for F2, 1,200 miles for E. |
| Hot-switching | Keying an amplifier's RF output before its relays have switched the antenna — it damages the relays. |
| Hurricane Watch Net | The emergency net that activates on 14.325 MHz USB by day (7.268 MHz LSB by night) when a hurricane threatens land. |
| I and Q signals | The in-phase and quadrature SDR signal pair, 90 degrees apart — software can turn them into any modulation type. |
| IF (intermediate frequency) | The fixed frequency a superhet converts signals to; the image response sits twice the IF away. |
| Image response | A superhet's unwanted response, twice the IF away from the desired signal. |
| Impedance | The opposition to AC current flow — resistance plus reactance; unit ohm. |
| Impedance matching | Making a load look like the source's design impedance — by transformer, pi-network, or transmission-line section. |
| Inductance | The ability to store energy in a magnetic field; unit henry. |
| Inductor | A component that stores energy in a magnetic field — a coil of wire. |
| Input impedance | The load a measuring device presents — voltmeters use high input impedance to avoid disturbing the circuit. |
| Insertion loss | A filter's attenuation inside its own passband. |
| Insulator | A material that blocks current flow because it has few free electrons (glass, most plastics). |
| Integrated circuit (IC) | Many semiconductors and other components built into one package — a "chip." |
| Interlock | The switch that removes dangerous voltages when a power-supply cabinet is opened. |
| Intermodulation | Spurious products spawned when signals combine in a non-linear circuit; odd-order products land closest to the originals. |
| Internal resistance | A battery's hidden series resistance — lower resistance means higher available discharge current. |
| Inverted V | A dipole supported at a single central point with the legs sloping down. |
| Ionosphere | The charged upper-atmosphere region that reflects HF radio waves back to earth. |
| Ionizing radiation | Radiation energetic enough to damage cells and DNA (X-rays, gamma rays) — radio signals are not this. |
| ITU | The International Telecommunication Union, the UN agency coordinating global radio spectrum. |
| ITU Region 2 | The ITU region covering the Americas — the United States, Puerto Rico, and the US Virgin Islands. |
| K-index | The short-term (3-hour) index of geomagnetic stability. |
| Kilo- | Metric prefix for 10³ (kHz = kilohertz, kW = kilowatt, km = kilometer). |
| Ladder line | Open parallel-conductor feed line — approximately 450 ohms (also "window line"). |
| LED (light-emitting diode) | A diode that emits light when forward current flows — the standard visual indicator component. |
| LiFePO4 | Lithium iron phosphate battery chemistry — requires a charge controller with a solar panel. |
| Lightning arrester | A device on a grounded panel at the feed-line entry point that diverts lightning energy to ground. |
| Linear amplifier | An amplifier that preserves the input waveform — required for SSB. |
| Linearity | Freedom from distortion products, measured with the two-tone test. |
| Link budget | The accounting that adds transmit power and antenna gains and subtracts all losses, as seen at the receiver. |
| Link margin | The received level minus the minimum the receiver needs. |
| Loading (antenna) | Electrically lengthening an antenna by inserting inductors (coils) in the radiating elements. |
| Local control | Operation with the control operator directly manipulating the station's adjustments. |
| Local oscillator | The oscillator that sets a superheterodyne receiver's tuned frequency. |
| Lockout/tagout | De-energizing and tagging every circuit feeding a tower before climbing it. |
| Log-periodic antenna | A multi-element directional antenna with lengths and spacing varying logarithmically along the boom — wide bandwidth above all. |
| Long path | The great-circle path the long way around — point the beam 180 degrees from the short-path heading. |
| LoTW | Logbook of The World — the ARRL database where submitted electronic logs cross-match into confirmations. |
| LUF (lowest usable frequency) | The lowest frequency that survives ionospheric absorption between two points. |
| Main lobe | The direction of maximum radiated field of a directional antenna. |
| Mark and space | The two tones of an FSK signal (RTTY's 170 Hz shift separates them). |
| Mega- | Metric prefix for 10⁶ (MHz = megahertz). |
| Mesh network | An amateur data network built from commercial Wi-Fi gear with modified firmware on amateur frequencies. |
| Meteor scatter | Bouncing VHF signals off meteor ionization trails; best on 6 meters. |
| Micro- | Metric prefix for 10⁻⁶ (µV = microvolt). |
| Milli- | Metric prefix for 10⁻³ (mA = milliampere). |
| Mixer | A circuit that converts a signal from one frequency to another. |
| MMIC | Monolithic Microwave Integrated Circuit. |
| Modulation | Combining speech or data with an RF carrier signal. |
| Modulation envelope | The outline made by connecting the peaks of the RF waveform. |
| MOSFET | A field-effect transistor whose gate is insulated from the channel by a thin insulating layer. |
| MPE (maximum permissible exposure) | The FCC's RF exposure limit, which varies with frequency (lowest at 50 MHz among the pool's bands). |
| MUF (maximum usable frequency) | The highest frequency that propagates by skywave between two specific points. |
| Multimeter | A meter that measures voltage, current, and resistance. |
| Multipath | The same signal arriving over multiple paths, combining in or out of phase to cause fading. |
| Multiplier (frequency) | A stage that outputs a harmonic of its input — how a VHF FM transmitter reaches its operating frequency. |
| Mutual inductance | The changing primary current inducing voltage in the secondary — how transformers work. |
| NAK | The negative-acknowledgment signal meaning "please retransmit." |
| Nano- | Metric prefix for 10⁻⁹. |
| NCDXF beacons | The Northern California DX Foundation / IARU international beacon network on 14.100, 18.110, 21.150, 24.930, and 28.200 MHz. |
| NCS (net control station) | The station that calls a directed net to order and directs its communications. |
| NEC (National Electrical Code) | NFPA 70 — the code that covers the electrical safety of the station. |
| Net | An organized on-air meeting run under net discipline. |
| Neutralization | Canceling an amplifier's internal feedback to eliminate self-oscillation. |
| Noise blanker | A receiver circuit that mutes receiver gain during each noise pulse. |
| Non-ionizing radiation | Radiation without enough photon energy to alter cells chemically — radio signals; its hazard is heating. |
| Notch filter (receiver) | A receiver filter that removes an interfering carrier inside the passband. |
| NTS | The National Traffic System — ARRL radiogram nets running daily at local through area levels. |
| NVIS | Near vertical incidence skywave — high-angle, short-distance MF/HF propagation, the emcomm workhorse for regional coverage. |
| Odd-order product | An intermodulation product whose mixing-coefficient sum is odd — these land closest to the original frequencies. |
| OET Bulletin 65 | The FCC's RF-exposure evaluation guidance (Supplement B for the amateur service). |
| Ohm (Ω) | The unit of resistance and impedance. |
| Ohmmeter | A meter that measures resistance using its own internal battery — never on a powered circuit. |
| Ohm's law | E = I × R (equivalently V = I × R): voltage equals current times resistance. |
| Omnidirectional | Radiating equally in all azimuth directions. |
| Op-amp | The analog operational-amplifier integrated circuit. |
| Oscillator | A circuit that generates a signal at a specific frequency. |
| Oscilloscope | The instrument that draws waveforms — horizontal and vertical channel amplifiers inside. |
| Overmodulation | Too much modulation — splatter into excessive bandwidth, showing as vertical side-lines on the waterfall. |
| Packet header | The part of a packet frame carrying the routing and handling information. |
| Packet radio | Digital data sent in addressed frames with a header, checksum, and ARQ error recovery. |
| PACTOR | An HF digital protocol whose connections are strictly two-station ARQ links. |
| Parallel circuit | A circuit where components share the same two nodes, so the voltage is the same across all of them. |
| Part 97 | The FCC's amateur service rules (47 CFR Part 97). |
| Peak | The maximum instantaneous value of a waveform. |
| Peak-to-peak | The swing from negative to positive crest — 2√2 times the RMS value for a sine wave. |
| PEP (peak envelope power) | The average power during one RF cycle at the crest of the modulation envelope — how amateur power limits are stated. |
| Phase | The timing relationship between AC voltage and current — voltage leads current in an inductor and lags in a capacitor. |
| Phonetic alphabet | The standard word list (Alfa, Bravo, Charlie …) used to spell call signs and unusual words clearly. |
| Photovoltaic cell | A solar cell — one silicon cell gives about 0.5 V open-circuit in full sun. |
| Pico- | Metric prefix for 10⁻¹² (pF = picofarad). |
| PL-259 | The classic "UHF" coax connector, standard at HF and VHF but not watertight and not the best choice above 400 MHz. |
| Plate current dip | The resonance indication when tuning a vacuum-tube RF amplifier — TUNE for the dip. |
| PM (phase modulation) | Impressing information on a carrier by varying its phase — a close cousin of FM. |
| Polarization | The orientation of a radio wave's electric field — vertical whip, vertical polarization. |
| Potentiometer | An adjustable resistor — the volume-knob part. |
| Power | The rate at which electrical energy is used; unit watt. |
| Power density | The RF field strength per unit area — one of the three exposure variables. |
| PRB-1 | The 1985 FCC declaratory ruling: local antenna regulation must reasonably accommodate amateur communications and use the minimum practicable regulation. |
| Preamble (radiogram) | The block at the head of a radiogram carrying the information needed to track the message. |
| Primary service | The service with priority on shared spectrum — secondary services must protect it and accept its interference. |
| Product detector | The SSB/CW receiver detector that recovers the audio. |
| Prosign | A procedural CW sign: KN = listening only for specific station(s); AR = end of a formal message. |
| PSK | Phase shift keying — digital data carried by phase changes of the carrier. |
| PSK31 | A narrow-band keyboard-to-keyboard digital mode using Varicode — it hangs out at 14.070 MHz on 20 m. |
| PTT (push-to-talk) | The switch or line that keys the transmitter, switching the transceiver from receive to transmit when grounded. |
| Q signals | Three-letter abbreviations (QRM = interference, QSY = change frequency, QRZ = who is calling, QTH = location). |
| QPSK | Quadrature phase shift keying — 0°/90°/180°/270° shifts, two bits per symbol. |
| QRL? | The Q signal asking "are you busy? / is this frequency in use?" |
| QRM | The Q signal for man-made interference from other stations. |
| QRN | The Q signal for trouble from natural static. |
| QRP | Low-power transmit operation — roughly 5 W by club and award custom, not regulation. |
| QRS? | The Q signal request "send slower." |
| QRV | The Q signal "ready to receive." |
| QSL | The Q signal "I have received and understood" — hence the confirmation card. |
| QSL bureau | The volunteer card-forwarding system: outgoing via ARRL's Outgoing QSL Service, incoming via the call-district bureau. |
| QSK | Full break-in CW — receiving between code elements. |
| Quarter-wave vertical | A vertical antenna a quarter wavelength long (about 19 inches on 2 meters). |
| RACES | Radio Amateur Civil Emergency Service — the Part 97 civil-defense service requiring certification by a civil defense agency. |
| Radials | The ground-plane conductors of a vertical antenna — slope them downward to raise the feed point toward 50 Ω. |
| Radiogram | A formal written message relayed by traffic nets. |
| Random wire | A non-resonant wire antenna — connected directly to the rig it can put significant RF current on station equipment. |
| RCA phono | The non-RF connector used for low-frequency or DC connections to a transceiver. |
| Reactance | The opposition to AC from capacitance and inductance — the non-resistive part of impedance. |
| Reactance modulator | A stage that varies an oscillator's effective reactance — attached after the oscillator, it produces phase modulation. |
| Rectifier | A circuit (usually diodes) that changes AC into varying DC. |
| Reflected power | Power bounced back from a mismatched antenna feed point toward the transmitter. |
| Reflector | The Yagi element longer than the driven element, sitting behind it. |
| Refraction (ionospheric) | The bending that returns skywave signals to Earth between the LUF and the MUF. |
| Remote control | Operation with the control operator manipulating the station indirectly through a control link. |
| Repeater | A station that simultaneously retransmits another station's signal on a different channel to extend range. |
| Resistance | The opposition to current flow of every kind — DC, AC, and RF; unit ohm. |
| Resistor | A component whose job is to oppose (limit) current flow. |
| Resonance | The condition X_L = X_C, where the inductive and capacitive reactances cancel. |
| Resonant circuit | An inductor plus a capacitor forming a frequency-selecting tuned circuit. |
| Resonant frequency | The frequency at which an antenna (or tuned circuit) naturally responds best. |
| Reverse beacon network | An internet network of automated receivers showing where your signal is being heard. |
| RF (radio frequency) | Signals in the radio part of the spectrum — and shorthand for radio energy generally. |
| RF burn | A burn to the skin caused by touching an antenna or conductor carrying strong RF. |
| RF feedback | Transmitted RF getting back into your own equipment (e.g., down the microphone cable) and distorting your audio. |
| RFI | Radio-frequency interference — your RF getting into consumer electronics (SSB sounds like distorted speech; CW like on-and-off humming or clicking). |
| Ripple frequency | The pulse rate of rectified DC — twice the line frequency for full-wave. |
| RMS | Root-mean-square — the AC value that heats a resistor exactly like the same-value DC. |
| RST | The signal-report system: readability 1–5, strength 1–9, and tone 1–9 (tone used on CW). |
| S meter | The receiver's received-signal-strength meter; one S unit is about 6 dB. |
| Saturation | The fully-on endpoint of a switching transistor's operation. |
| Scatter | Weak multi-path propagation that fills the skip zone with fluttery, distorted signals. |
| Schematic | An electrical diagram drawn with standard component symbols, showing how components connect. |
| Screwdriver antenna | A mobile antenna tuned by varying its base-loading inductance with a motor. |
| Screen grid | The vacuum-tube grid that reduces grid-to-plate capacitance. |
| SDR (software-defined radio) | A radio whose filtering, detection, and modulation all happen in software. |
| Secondary service | A service that must not interfere with, and must accept interference from, the primary service on shared spectrum. |
| Selectivity | A receiver's ability to discriminate between nearby signals. |
| Self-resonant frequency | The frequency where a component's parasitics resonate — above it, an inductor turns capacitive. |
| Sensitivity | A receiver's ability to detect weak signals. |
| Series circuit | A circuit where the same current flows through every component in turn. |
| Series diode | The diode between solar panel and battery that stops night-time back-discharge. |
| Shift register | A clocked array passing data along in steps. |
| Short path | The direct great-circle heading to a distant station. |
| SID (sudden ionospheric disturbance) | The daytime HF fadeout that begins about 8 minutes after a solar flare's light arrives. |
| Sideband convention | LSB below 10 MHz (160/75/40 m), USB at 10 MHz and above (20–10 m and VHF/UHF) — custom, not law; AFSK RTTY uses LSB while FT8/JT modes use USB on every band. |
| Signal report | The RS (phone) or RST (CW) assessment exchanged first so both stations can adapt to conditions. |
| Simplex | Transmitting and receiving on the same frequency. |
| 60-meter band | The 5 MHz band: a contiguous 5351.5–5366.5 kHz segment at 9.15 W ERP plus four discrete channels (5332, 5348, 5373, 5405 kHz) at 100 W ERP, USB phone, 2.8 kHz maximum bandwidth. |
| Skip distance | The gap between the transmitter and where the first skywave hop lands. |
| Skip zone | The ring between ground-wave range and the first hop's landing — only scatter fills it. |
| Skywave | Ionospherically propagated signals — the long-distance mode of HF. |
| SMA | A small threaded RF connector good to several GHz. |
| Smith chart | A graphical chart of impedance and reflection used for matching design — shown once in ch09 as a "what it shows" sidebar; the General pool does not test it. |
| Solar flux index | The measure of 10.7 cm (2800 MHz) solar radio emission — the everyday solar-activity number. |
| Space station | An amateur station located more than 50 km above the Earth's surface. |
| Speech processor | A device that raises average talk power (apparent loudness) while the peaks stay legal. |
| Split operation | Transmitting on one frequency while listening on another — the DX announces "listening 5 to 10 up." |
| Spread spectrum | A wide-band emission technique limited to 10 W PEP output. |
| Spurious emission | Any unwanted emission outside the necessary bandwidth, such as a harmonic. |
| SSB (single sideband) | A bandwidth-efficient voice mode transmitting one sideband of an AM signal with the carrier suppressed. |
| Stacking | Combining two identical antennas (e.g., Yagis a half-wavelength apart) for about 3 dB more gain. |
| Step-up transformer | A transformer whose secondary voltage exceeds the primary's — its primary carries the higher current. |
| Sunspot cycle | The roughly 11-year solar activity cycle; peaks bring world-wide F-region DX on 10 and 6 meters. |
| Superheterodyne | A receiver that converts signals to a fixed intermediate frequency by varying its local oscillator. |
| Suppressed carrier | The carrier frequency an SSB rig displays while transmitting no carrier — the speech energy sits about 3 kHz to one side. |
| Switchmode power supply | A supply that chops the input at high frequency — what allows smaller, lighter components. |
| SWR (standing wave ratio) | A measure of how well a load is matched to a transmission line — 1:1 is perfect. |
| SWR meter | An instrument that reads the match between feed line and antenna (a directional wattmeter does this job). |
| Symbol rate | The digital signaling speed in symbols per second — higher symbol rates need wider bandwidth. |
| Takeoff angle | The elevation angle at which an antenna launches its main radiation. |
| Tank circuit | The parallel LC combination that sets an oscillator's or amplifier's frequency. |
| Telecommand | One-way transmissions to initiate, modify, or terminate functions of a device at a distance (e.g., a space station). |
| Telemetry | Measurements sent back by radio, such as a satellite's health data. |
| Third-party agreement | A treaty arrangement letting US amateurs pass third-party traffic with a given country. |
| Third-party communications | A message passed from one control operator to another on behalf of a non-licensed person. |
| Time averaging | Total RF exposure averaged over a period — why a lower duty cycle permits higher power. |
| Time slot | One of the two repeating time windows DMR uses to carry two conversations on one channel. |
| Time slot (FT8) | One of the alternating 15-second transmit/receive windows FT8 uses to share one dial frequency. |
| Toroid | A donut-shaped ferrite core giving large inductance with a self-contained field. |
| Traffic | Formal written messages exchanged by net stations. |
| Transceiver | A receiver and a transmitter combined in one unit. |
| Transformer | A component that changes AC voltage up or down — never to DC. |
| Transistor | A three-region semiconductor device that works as an electronic switch or an amplifier. |
| Trap antenna | A multiband antenna using parallel-resonant traps to switch effective length per band. |
| TTL | The classic digital IC family — CMOS beats it on power consumption. |
| Turns ratio | A transformer's primary-to-secondary winding-count ratio — voltage follows it, impedance its square. |
| Two-tone test | Feeding two non-harmonically related audio tones into an SSB transmitter to analyze linearity. |
| Type N connector | The weather-resistant RF connector recommended above 400 MHz. |
| UHF | Ultra high frequency: 300–3000 MHz. |
| Ultimate rejection | A filter's maximum stopband rejection. |
| ULS | The FCC's Universal Licensing System — the database whose entry for your grant is your operating authority. |
| Uncontrolled environment | The RF-exposure category for the general public (general-population limits). |
| Uplink / downlink | The ground-to-satellite path and the satellite-to-ground path (U/V mode = up on 70 cm, down on 2 m). |
| USB / LSB | Upper and lower sideband; USB is the convention on 10 meters and on VHF/UHF. |
| Vanity call sign | A call sign you request by choice rather than receiving from the sequential system. |
| VARA | A proprietary digital protocol used with Winlink. |
| Varicode | PSK31's variable-length code — common letters get short codes, so uppercase letters take longer. |
| VE (volunteer examiner) | An accredited amateur who administers license exams as part of a team of at least three. |
| VEC (volunteer examiner coordinator) | The FCC-recognized organization that coordinates exam sessions and forwards results to the FCC. |
| VFO (variable frequency oscillator) | The circuit that sets a transceiver's operating frequency. |
| VHF | Very high frequency: 30–300 MHz. |
| Volt (V) | The unit of electric potential (voltage). |
| Voltage | The electrical "pressure" whose difference drives electron flow. |
| Voltmeter | A meter that measures voltage, connected in parallel with the component. |
| Volunteer Monitor | An amateur formally enlisted — via ARRL under an FCC agreement — to watch the bands so the service self-regulates. |
| VOX | Voice-operated transmit/receive switching — hands-free keying by your voice. |
| W1AW | The ARRL headquarters station — daily code practice and bulletins. |
| WARC bands | 30, 17, and 12 meters — the 1979-conference bands where contests are avoided by long-standing truce. |
| Waterfall | The scrolling display with frequency horizontal, time vertical, and signal strength as brightness. |
| Watt (W) | The unit of electrical power. |
| Wavelength | The distance a wave travels in one cycle — inversely related to frequency. |
| Window line | TV-style parallel feed line — approximately 450 ohms (see ladder line). |
| Winlink | A system that relays email over amateur radio and internet, using call-sign-based addresses. |
| WSPR | Weak Signal Propagation Reporter — a 2-minute-sequence beacon mode whose reception reports map at WSPRnet. |
| WSJT-X | The free software suite home of FT8, also supporting EME, weak-signal beacons, and meteor scatter. |
| Yagi | A directional beam antenna with a driven element plus parasitic elements — the greatest gain of the pool's listed antennas. |
| Zener diode | A diode used as a voltage reference or regulator (symbol 5 in pool Figure G7-1). |
| Zero beat | Matching your transmit frequency exactly to the received CW signal. |

---

## 5. Subelement → Chapter Map

From the design spec §4 and the implementation plan (Phase 2, canon task): the mapping is one subelement per chapter, G1→ch01 … G0→ch10, with ch00 the upgrade welcome (no pool). Every one of the 423 pool questions is answerable after its mapped chapter; the mapping below is the ownership contract — a chapter teaches its subelement, and only that chapter quotes those questions in its Exam Focus. Exam weight (one question per group) is shown so writers see the stakes.

| Chapter | Title | Pool subelement | Groups owned | Pool questions | Exam questions |
|---|---|---|---|---:|---:|
| ch00 | The upgrade: why General, and how this book works | — (upgrade logistics, canon §2.4) | — | — | — |
| ch01 | Your HF privileges & the rules that come with them | G1 | G1A–G1E | 52 | 5 |
| ch02 | Operating on HF | G2 | G2A–G2E | 60 | 5 |
| ch03 | Propagation in depth | G3 | G3A–G3C | 37 | 3 |
| ch04 | Station setup & good practice | G4 | G4A–G4E | 60 | 5 |
| ch05 | AC theory: reactance, impedance, resonance | G5 | G5A–G5C | 40 | 3 |
| ch06 | Components & devices | G6 | G6A–G6B | 23 | 2 |
| ch07 | Practical circuits | G7 | G7A–G7C | 38 | 3 |
| ch08 | Signals & emissions | G8 | G8A–G8C | 42 | 3 |
| ch09 | Antennas & feedlines at General depth | G9 | G9A–G9D | 46 | 4 |
| ch10 | Safety & RF exposure at General depth | G0 | G0A–G0B | 25 | 2 |
| Appendix A | The complete 2023–2027 General pool | all 423 verbatim + one-line "why" | all 35 | 423 | 35 |
| Appendix B | Glossary & formulas | — (canon §3, §4) | — | — | — |
| **Total (ch01–ch10)** | | | **35** | **423** | **35** |

Per-group ownership and counts (binding):

- **ch01 (G1, 52 q):** G1A General-class privileges & primary/secondary (10); G1B antenna structures, beacons, prohibited transmissions (11); G1C power regulations, data standards, 60 m (8); G1D VEs, VECs, temporary ID, element credit, remote operation (12); G1E control categories, repeaters, third-party, ITU regions, automatic digital (11).
- **ch02 (G2, 60 q):** G2A phone procedures & USB/LSB (12); G2B operating effectively, band plans, emergencies, RACES (11); G2C CW procedures, Q signals, full break-in (11); G2D Volunteer Monitors & HF operations (11); G2E digital operating procedures (15).
- **ch03 (G3, 37 q):** G3A sunspots, solar radiation, geomagnetic indices (14); G3B MUF/LUF, short and long path, determining conditions (12); G3C ionospheric regions, critical angle/frequency, scatter, NVIS (11).
- **ch04 (G4, 60 q):** G4A station configuration and operation (13); G4B tests and test equipment (13); G4C interference, grounding, bonding (12); G4D speech processors, S meters, sideband at band edges (11); G4E mobile/portable HF and alternative energy (11).
- **ch05 (G5, 40 q):** G5A reactance, impedance, transformation, resonance (12); G5B decibels, dividers, power, RMS, PEP (14); G5C R/L/C in series and parallel, transformers (14).
- **ch06 (G6, 23 q):** G6A R/L/C, diodes, transistors, tubes, batteries (12); G6B ICs, MMICs, connectors, ferrites (11).
- **ch07 (G7, 38 q):** G7A power supplies & schematic symbols (13); G7B digital circuits, amplifiers, oscillators (11); G7C transceiver design, filters, DSP (14).
- **ch08 (G8, 42 q):** G8A carriers and modulation, envelope, link budgets (14); G8B frequency changing, bandwidths, deviation, intermodulation (13); G8C digital emission modes (15).
- **ch09 (G9, 46 q):** G9A feed lines, SWR, feed-point matching (11); G9B basic dipoles and monopoles (12); G9C directional antennas (11); G9D specialized antennas (12).
- **ch10 (G0, 25 q):** G0A RF safety principles and station evaluation (12); G0B electrical, grounding, and antenna/tower safety (13).

Notes (binding):
- **ch00 teaches no pool questions** — it covers the upgrade logistics of canon §2.4 (Element 3, CSCE, §97.9(b) immediacy with /AG, fees and the upgrade exemption, what General opens, what's next) and carries the "checklist" adaptation of the format laws (no Exam Focus; the audit enforces this).
- **Figure G7-1 belongs to ch07** (group G7A); its redrawn SVG follows §1.4 and the five figure questions (G7A09–G7A13) appear in ch07's Exam Focus.
- **ch10 treats G0A and G0B as separate sections** — RF-exposure/MPE material and shop/tower safety share no concepts (r4's split guidance).
- **ch09 carries the single Smith-chart sidebar** (§7.6): brief, "what a Smith chart shows," no exam weight, no dedicated figure.
- Appendix A quotes all 423 ids exactly once in canonical pool order (audit check #8 enforces it); Appendix B is built from canon §3 and §4 only.

---

## 6. Copyright Ledger

**This book's standing rules (identical to Book 2's canon, adapted for this pool):**

1. **Prose is always original.** Nothing is copied from any study guide, handbook, or web page.
2. **47 CFR Part 97 is public domain** (a work of the United States Government, 17 U.S.C. §105) and may be quoted verbatim; the FACT sentences in §2 quote it with section pinpoints.
3. **The NCVEC 2023–2027 General question pool is public domain** — "The NCVEC Question Pool Committee hereby releases into public domain the 2023-2027 General, Element 3, Question pool" (statement on the pool's release page, captured in `canon/source/release-page.html`, fetched 2026-07-24) — so questions, choices, answer keys, and figure *content* may be reproduced verbatim.
4. **The pool figure G7-1 is redrawn, not copied**: an original SVG conveying exactly the official content (same components, same labels, same numbered callouts), registered in `figures/figures.json` as `kind:"original"` with the note "redrawn from NCVEC pool figure G7-1" (see §1.4).
5. **Bare facts, frequencies, and formulas are not copyrightable**; exam-prep explanations are always written fresh.
6. **Archival ARRL Handbook material is optional seasoning only**, governed by the ledger below (carried over unchanged from Book 1's accuracy canon, where each status was affirmatively determined, and already governing Book 2). The book works with zero archival images.

**ARRL *Radio Amateur's Handbook* ledger (carried over — governs any optional archival figure in this book too):** determinations rest on the US Copyright Office Public Records System and the official Catalog of Copyright Entries renewal volumes; public-domain findings are affirmatively evidenced (registration age, or confirmed absence of renewal within the 28-year window), not assumed.

| Edition (year) | Status | Basis | Reproducible? |
|---|---|---|---|
| 1927 | PUBLIC DOMAIN | Published 1927; pre-1928 works are public domain under the 95-year term (entered PD 1 Jan 2023); age alone controls. | YES |
| 1931 | PUBLIC DOMAIN | 8th Edition, first published 25 Apr 1931; renewal window 1958–1959; no renewal found in the USCO ARRL-claimant RE-class search or CCE renewal volumes. Not renewed. | YES |
| 1933 | PUBLIC DOMAIN | 10th Edition, first published 4 Jan 1933; renewal window 1960–1961; zero renewal matches. Not renewed. | YES |
| 1936 | PUBLIC DOMAIN | 13th Edition, first published 13 Nov 1935 (cover-dated 1936); renewal window 1963–1964; zero renewal matches. Not renewed. | YES |
| 1940 | PUBLIC DOMAIN | 17th Edition, first published 20 Nov 1939; renewal window 1967–1968; zero renewal matches. Not renewed. | YES |
| 1941 | PUBLIC DOMAIN | 18th Edition, first published 15 Nov 1940; renewal window 1968–1969; zero renewal matches. Not renewed. | YES |
| 1951 | PUBLIC DOMAIN | 28th Edition; renewal window ~1978–1979; the comprehensive USCO ARRL-claimant RE-class query shows no Handbook renewal in any year. Not renewed. | YES |
| 1968 | PROTECTED | Published 1964–1977: renewal became automatic by statute; protected 95 years from publication. | NO |
| 1974 | PROTECTED | 1964–1977 automatic-renewal window; protected 95 years from publication. | NO |
| 1976 | PROTECTED | 1964–1977 automatic-renewal window; protected 95 years from publication. | NO |
| 1977 | PROTECTED | 1964–1977 automatic-renewal window; protected 95 years from publication. | NO |
| 1981 | PROTECTED | Published 1978 or later; protected 95 years from publication, no renewal formality applicable. | NO |
| 1983 | PROTECTED | Published 1978 or later; protected 95 years from publication, no renewal formality applicable. | NO |

**Ledger summary:** 7 of the 13 owned Handbook editions are reproducible (public domain): 1927, 1931, 1933, 1936, 1940, 1941, 1951. The 6 protected editions — 1968, 1974, 1976, 1977, 1981, 1983 — are **never reproduced** in any form: no figures, no text excerpts, no scans. `figreg.validate()` mechanically rejects any figure tagged with a protected-year source. Separately and independently of that table: FCC Part 97 and the NCVEC question pools are public domain as stated in rules 2–3 above, and everything else in this book is original prose or original SVG.

---

## 7. Resolved Uncertainties

Every uncertainty flagged during research (notes r1–r5 and the ingestion report) is closed here, with the value or wording the book will use and its source. **No open uncertainty markers remain in this canon.**

### 7.1 The 60 m rule change (91 FR 1430) — the pool is older than the rule: RESOLVED — teach current text, drill keyed answers

**What changed.** The FCC's WRC-15 Report & Order in WT Docket 23-83 (FCC 25-60, adopted 2025-09-23, released 2025-12-09; published in the Federal Register as 91 FR 1430 on 2026-01-14) replaced the channelized 60 m rules. Pool-era text (in force when the pool was written in 2022): five discrete channels only — 5332, 5348, 5358.5, 5373, 5405 kHz center (suppressed-carrier frequencies 5330.5, 5346.5, 5357.0, 5371.5, 5403.5 kHz) — USB phone/data/RTTY plus CW, emissions ≤ 2.8 kHz, and a flat 100 W ERP cap. **Current text** (47 CFR §§97.301(d), 97.303(h)(3), 97.305(c)(3)(iii), 97.307(f)(14), 97.313(i), verified 2026-07-24 against the eCFR, issue date 2026-07-20): amateurs may transmit (1) anywhere in the contiguous **5351.5–5366.5 kHz** segment at **9.15 W ERP**, and (2) on **four** of the five old channels — **5332, 5348, 5373, 5405 kHz** — at **100 W ERP**; the old 5358.5 kHz channel is gone as a discrete assignment (it lies inside the new segment); the ≤ 2.8 kHz bandwidth cap now applies to all 60 m spectrum (§97.303(h)(3)); CW carrier sits at channel center while phone/data/RTTY carriers may be set 1.5 kHz below center on the discrete channels; and the non-dipole antenna-gain record requirement survives verbatim (§97.313(i): transmitter PEP multiplied by gain relative to a half-wave dipole, a dipole presumed 0 dBd, records kept for other antennas).

**Pool impact.** The NCVEC's 6th errata (2026-02-04) already withdrew the two conflicted questions — **G1A04** ("band restricted to specific channels" — no longer true of 60 m) and **G1C09** ("maximum power on 60 m" — 100 W ERP is now segment-dependent). Two surviving questions remain literally correct under current rules: **G1C03** (maximum bandwidth 2.8 kHz) and **G1C04** (antenna-gain records for non-dipole antennas); only their provisions moved — the 2.8 kHz cap now lives in **§97.303(h)(3)** (the pool prints `[97.303(h)(1)]`) and the gain-record duty in **§97.313(i)** (the pool prints `[97.303(i)]`, a paragraph that now holds the 7.2–7.3 MHz broadcast-sharing rule). G1A01's keyed set (80/40/20/15 m) is unaffected because General keeps full 60 m access under both texts; G1D03 and G3C05 mention 60 m only in distractors or as physics.

**Binding resolution:** chapters cite the CURRENT sections — §97.303(h)(3) for the 2.8 kHz bandwidth and §97.313(i) for power and antenna-gain records — when explaining these answers; teach current 60 m practice as the two-part structure (contiguous segment plus four channels, two power limits, USB phone, 2.8 kHz maximum bandwidth); and drill the pool's keyed answers exactly as published. No prose may describe 60 m as "five channels, USB only, 100 W ERP" — that rule is dead. The 60-meter row of the §2.1 privileges FACT carries the current §97.301(d) segment plus a pointer here for the four channels.

### 7.2 Upgrade immediacy — §97.9(b) plus the /AG indicator: RESOLVED with wording law

A Technician who passes Element 3 and properly submits Form 605 to the administering VEs may exercise General privileges **immediately** — before the VEC files anything and before ULS changes — "until final disposition of the application or until 365 days following the passing of the examination, whichever comes first" (§97.9(b), verbatim in §2.4; pool G1D03, G1D09). While doing so the station must append the indicator **AG** to the call sign "for a control operator who has requested a license modification from Novice or Technician to General Class" (§97.119(f)(2)), separated by the slant mark or any suitable word denoting it (§97.119(c)); in one VEC's practice, say "temporary AG" on phone and sign call/AG on CW or digital, dropping the suffix once ULS shows General (Laurel VEC FAQ, 2026-07-24; pool G1D06 keys "whenever they operate using General class frequency privileges" until the upgrade shows in the FCC database). **Contrast with Book 2's new-license readers:** a first-time licensee has NO authority until the grant appears in ULS — the immediacy rule is for existing licensees only. **Wording law (binding): never write "transmit as soon as you pass" without both conditions (Form 605 properly submitted to the VEs + CSCE in hand) and the /AG identification requirement in the same breath.**

### 7.3 The three sideband conventions: RESOLVED — pin all three precisely

- **Voice:** LSB below 10 MHz (160, 75, 40 m), USB at 10 MHz and above (20, 17, 15, 12, 10 m, and VHF/UHF SSB). Convention, not law or physics (pool G2A01–G2A04, G2A09; the ARRL/IARU ethics manual states it flatly: "SSB transmissions below 10 MHz are done on LSB, above 10 MHz on USB").
- **AFSK RTTY → LSB** (pool G2E01, keyed D). The traditional convention; the book states the practice only — no origin story (none of the fetched references documents one; r5's exclusion upheld).
- **JT65/JT9/FT4/FT8 → USB on EVERY band**, including 80 and 40 m where voice is LSB (pool G2E05, keyed B; WSJT-X manual: "WSJT-X uses upper sideband mode for both transmitting and receiving"; ARRL's On The Air FT8 article instructs "switch your radio to upper sideband (USB)").
- **60 m phone is USB** — the one band where sideband was written into the rule (see §7.1 for the current text).
- **Anti-shorthand law (r5 watch 6):** never teach "LSB below 14 MHz." Some study aids phrase the convention that way, echoing G2A01's question wording; the boundary is 10 MHz, and 30/17/12 m are USB. The book keeps the 10 MHz framing everywhere.

### 7.4 Pool citation defects — preserved, not propagated: RESOLVED

- **G1D12 prints `[97.507]`** — an apparent misprint (§97.507 is "Preparing an examination"). The keyed answer (only that country's regulations apply) rests on territorial jurisdiction: Part 97 authorizes operation only where the FCC regulates the amateur service (§97.301 preamble: bands available "outside any area where the amateur service is regulated by any authority other than the FCC"). The answer is correct as published; the ID line is preserved verbatim in `canon/pool-general.txt`; chapters cite the §97.301 preamble when explaining G1D12 and never "repair" the printed citation.
- **G1B05 prints `[97.111((5)(b)]`** — malformed (double open-paren, lettered sub-paragraph). The intended reference is §97.111(a)(5)(b)-style; the operative permission — one-way "transmissions necessary to assisting persons learning, or improving proficiency in, the international Morse code" — is codified in the §97.111(b) list in current numbering. The ID line is preserved verbatim; chapters cite §97.111(b) for the Morse-practice permission.

### 7.5 Symbol-rate rules changed after the pool was written: RESOLVED — no exam impact

The FCC's December 2023 Order (88 FR 85127) replaced the HF symbol-rate limits with a 2.8 kHz authorized-bandwidth standard: §97.307(f)(3) now imposes the bandwidth standard below 28 MHz, the 300-baud limit survives only for 2200 m/630 m, and (f)(4) is Reserved. Verified by full-text search of `canon/pool-general.json`: **no active question tests maximum symbol rate** (only G2E14, G8B10, and G8C04 mention baud topically). Chapters teach the current 2.8 kHz bandwidth standard and never resurrect 300 baud as an exam fact.

### 7.6 Smith chart: RESOLVED — one sidebar, no exam weight

Zero pool questions test the Smith chart (verified by r4's full read of G6–G0; the 2023–2027 revision dropped the old Smith-chart items). This resolves the design spec's earlier assumption of "Smith-chart basics" figure material: **the book keeps ONE brief "what a Smith chart shows" sidebar in ch09, with no exam weight and no dedicated figure** — the ch09 figure budget goes to transmission lines, patterns, and matching instead. The glossary carries one orientation entry so the sidebar and Appendix B stay consistent.

### 7.7 Ingestion-level flags (ingestion report): RESOLVED

- **Stale syllabus count:** the printed syllabus claims G1:54 (sum 425); the parse-authoritative G1 count is 52 — the syllabus was not updated for the 6th errata's two G1 withdrawals. The parse, not the syllabus, is authoritative (§1.3).
- **G1A06 "24-hour":** the PDF rendering split the hyphen at a line break ("24- hour"); the .docx — authoritative — carries `24-hour`, and so do the canonical files. No content difference.
- **No ARRL mirror:** arrl.org hosts no separate copy of this pool (its link points back to NCVEC), so no NCVEC-vs-ARRL diff was possible; the two independent NCVEC renderings (.docx vs .pdf) were parsed separately and diffed instead — the cross-check of record.
- **Published quirks preserved verbatim:** the `G9C01 (A) ` ID-line trailing space; the G2E02 choice-D label `D.A` (no space); the deleted-question placeholder lines (printed with a double space; G1E09's with a single space) are not carried into the canonical files; G4E11 choice B's leading tab was the one stripped whitespace normalization. None is ever "fixed" in quotation.
- **Errata currency:** the 6th errata (2026-02-04) is the newest; there is no 7th errata as of 2026-07-24 (release page and document front matter agree). Re-check the release page before each reprint.
- **5th-vs-6th cross-check:** the only differences between the 5th-errata parse (425 active + 7 deleted) and the 6th (423 + 9) are the removals of G1A04 and G1C09 — zero content differences among the 423 common questions.

### 7.8 Other post-pool Part 97 amendments: RESOLVED — zero answer impact

90 FR 57712 (2025-12-12) Reserved §97.521(b) (VEC regions) and §97.315(b)(2) (pre-1978 amplifier waiver clause) and removed §§97.27 and 97.29; §97.207(g) space-station notification/debris rules were expanded (88 FR 21451, 89 FR 65223). A full 2023-07-01 vs 2026-07-20 diff confirms §§97.505, 97.509, 97.221, 97.115, 97.119, 97.407, 97.13, and 97.15 are byte-identical to pool-era text. No General answer changes; the §2.4 VEC FACT cites §97.521 with the (b) reservation noted.

### 7.9 Answers resting on practice rather than rule text (r1 W4, r3 flags): RESOLVED with careful framing

- **G1E10's five beacon frequencies** (14.100, 18.110, 21.150, 24.930, 28.200 MHz) are the NCDXF/IARU network — good amateur practice under §97.101(a), not a Part 97 set-aside; the only automatic-beacon segment Part 97 itself designates is 28.20–28.30 MHz (§97.203(d)). Chapters say exactly that.
- **G1B02's distractors** ("National Beacon Organization," internet posting requirements) have no rule basis — only §97.203(b) is real; chapters name the organization as fictional.
- **G1E06 (ITU Region 2)** additionally rests on the ITU Radio Regulations, outside Part 97; Region 2 is pinned via the Note to §97.303.
- **G1B09 vs G1E10 conflation:** the auto-beacon segment (28.20–28.30 MHz) and the beacon-network frequencies are different facts; G1B09's distractor 21.08–21.09 MHz is a real segment — for automatically controlled *digital stations* (§97.221(b)), not beacons. Chapters keep the two lists apart.
- **G1D05/G1D12 asymmetry:** running your US station from abroad requires your US operator/primary license (§97.7); running a South American station from the US puts you under only that country's rules (territorial jurisdiction, §7.4). Teach the pair together — the asymmetry surprises students.
- **G1E02:** a Technician can talk *through* a 10 m repeater only if the repeater's control operator is General or higher — privileges follow the transmitting station's control operator, not the user.

### 7.10 r3/r4 teaching watch items: RESOLVED

- **"All these choices are correct" is the keyed answer 7 times** in the pool (G0A02, G0A03, G6B05, G7C08, G7C11, G8A06, G9C10) **and a distractor at least 7 times** (G0A05, G0B05, G0B07–G0B09, G7A02, G7B11, G8C06, …). Chapters teach content, never pattern-guessing.
- **G5B10** is the only pool question requiring a non-round dB computation — give the reader the 10^(−0.1) = 0.794 derivation, not just the answer.
- **G5C08** mixes nF and pF; the keyed answer prints "10.750 nF" with the trailing zero — reproduce it exactly.
- **G4D08 cross-teach:** its LSB example (7.178 MHz displayed) lands the lower edge exactly on the General 40 m phone boundary 7.175 MHz from G1A05 — ch01 and ch04 cross-reference each other here.
- **Flag-worthy subtleties for chapter asides:** G8A04 (reactance modulator after the oscillator → PM, not FM); G9A08 (the tuner leaves the line's SWR unchanged); G9D10 (small-loop nulls are broadside to the loop — the mirror of the dipole's broadside maxima); G7B11 (class C is fine for FM); G8B13 (only 2F1 − F2 is odd-order); G7A10's distractor magnet (varactor 4 vs Zener 5).
- **Numbering gaps in owned material** (G1A04, G1C08, G1C09, G1C10, G1E09, G6B09, G8C01, G9C06, G9D13) are errata deletions per §1.3 — never hunt for or quote them.
- **Current-rule spot checks (no conflicts beyond §7.1/§7.5):** the 200 ft tower threshold (§97.15), CSCE 365 days (§97.9(b)), expired-license credit (§97.505), VE rules (§97.509), RACES 1 hour/week (§97.407(d)(4)), spread-spectrum 10 W PEP (§97.313(j)), and 30 m 200 W PEP (§97.313(c)(1)) all match current Part 97 as amended through 91 FR 1430 (2026-01-14).

### 7.11 r5 operating watch items: RESOLVED

- **Clock tolerance wording:** the exam-facing value is pool G2E07's "about 1 second" (matching the WSJT-X ±1 s system requirement). ARRL's "within 2 seconds, the closer the better" may appear only as operating color, never as the exam number.
- **Net frequencies are custom, not assignments:** 14.300 (MMSN/GECOA) and 14.325/7.268 (HWN) are traditions operating under §97.101(b) — even the Hurricane Watch Net asks permission if the frequency is busy. Never write "the emergency frequency"; teach "center of activity by long custom."
- **Contest "59(9)" vs honest reports:** G2D11's adapt-to-conditions rationale is everyday ragchew practice; in contests the report is a fixed formality sent regardless of conditions. Teach both, so a new General neither sends a real "53" in Sweepstakes nor believes every "59" in a pileup.
- **QRP power levels are custom:** the pool defines QRP only as low-power operation; the ~5 W (~10 W SSB) figures are club/award custom, presented as custom or omitted.
- **Bureau fees and QSL logistics:** the $3.00 / 1–10-card rate is pinned "as of 2026-07-24" or the process is described without prices — never a bare price without its as-of date.
- **Deliberate exclusions (upheld — none of these appears anywhere in the book):** the RTTY-on-LSB origin story; exact FT4 watering-hole frequencies (FT4 appears only in color backed by the WSJT-X manual); specific DXpedition anecdotes; and any "most operators do X" quantifications.

### 7.12 Wording laws lifted from Book 2's canon (r2 watch items): RESOLVED — adopted unchanged

- **Grant timing:** no official FCC-wide guarantee exists, and upgrades have no fee step (the pinned "next business day" figure belongs to new licenses paying the $35 fee). The safe line is "your ULS record typically updates within days" — no day count is ever printed as a promise.
- **Remote exams:** availability depends entirely on the individual VE team (Laurel runs in-person only); chapters point readers at ARRL's session finder and hamstudy.org/sessions and never promise remote testing.
- **CORES "free":** no primary sentence states FRN registration is free, and no payment step exists in the flow — the book says "carries no fee and no exam requirement" and never prints "free of charge."
- **Laurel VEC web address:** larc-vec.org (the legacy laurelvec.com domain 307-redirects there; verified 2026-07-23).

### 7.13 Time-sensitive values — verification dates, re-verify triggers, and the pool-swap procedure: RESOLVED with this register

Each value below is pinned in §2 with its verification date. **Every one must be re-verified at the stated trigger before any reprint or new edition**, and the canon updated with the new verification date:

| Item | Pinned value | Verified | Re-verify trigger |
|---|---|---|---|
| **Pool currency (the big one)** | 2023–2027 General pool valid for exams 2023-07-01 → **2027-06-30**; 6th errata (2026-02-04) incorporated; no 7th errata | 2026-07-24 (ncvec.org release page; `canon/ingestion-report.md`) | Each reprint; **check ncvec.org from December 2026 for the 2027–2031 successor pool** (expected late 2026 by analogy with the Technician cycle, but never print a release date as fact) |
| FCC application fee | $35 (new license, renewal, rule waiver, vanity request), effective 2022-04-19; **upgrades EXEMPT** | 2026-07-24 (arrl.org/fcc-application-fee) | Before each reprint (fees are set by FCC order and can change in any fiscal-year fee order) |
| ARRL VEC exam fee | $15.00 per session; $5.00 for candidates under 18 | 2026-07-24 (arrl.org/arrl-vec-exam-fees — explicitly calendar-2026 figures) | Each January |
| NCVEC Form 605 edition | 2022 edition | 2026-07-24 (ncvec.org, HTTP 200 application/pdf) | Before publication and each reprint (the form's mandatory fields drive ch00's session instructions) |
| Part 97 rule text | eCFR issue date 2026-07-20 (§97.509 quoted from the 2026-07-22 issue); includes the 60 m / 2200 m / 630 m amendment 91 FR 1430 | 2026-07-24 (eCFR versioner API; all §2.1–§2.4 rule quotes copied from those retrievals) | Re-pull every cited section before any reprint |
| FT8 watering-hole frequencies | HF list per §2.5 (ARRL OTA table); 6 m/60 m per OnAllBands/DX Engineering table | 2026-07-24 | Before print, against the current WSJT-X default frequency table and ARRL |
| ISS SSTV | 437.550 MHz, Robot36 mode | 2026-07-24 (ariss.org) | Close to print, against ariss.org / AMSAT news |
| Net schedules | MMSN 14.300 MHz daily 12:00–22:00 ET; HWN 14.325 MHz day / 7.268 MHz night | 2026-07-24 (mmsn.org; hwn.org) | Close to print |
| QSL bureau rate | $3.00 for 1–10 cards (ARRL Outgoing QSL Service) | 2026-07-24 (arrl.org/outgoing-qsl-service) | Before print — or describe the process without prices (§7.11) |
| Laurel VEC web address | https://larc-vec.org/ (laurelvec.com 307-redirects there) | 2026-07-23 | Before each reprint |

**Contained-swap procedure for the 2027–2031 pool (binding):** the book's teaching content is durable by design — only the pool-facing artifacts change with a new pool. On release of the successor pool: (1) ingest it into `canon/` with a new ingestion report (new canonical files, sha256s, errata ledger, deleted-ID list); (2) update this canon's §1 (files, counts, validity window) and any §2 FACT or §7 resolution whose rule or frequency changed; (3) refresh each chapter's Exam Focus question picks and Appendix A's verbatim pool against the new canonical files; (4) re-run the build audit and the full test suite to green; (5) nothing else changes — notation, glossary, chapter map, teaching prose, and figures stay as pinned here. Any printing of this book after mid-2027 must state which pool exams actually use.

---

*End of canon. Every claim in this book traces to this file, to `canon/pool-general.*`, or to original prose. If a chapter disagrees with this file, the chapter is wrong.*
