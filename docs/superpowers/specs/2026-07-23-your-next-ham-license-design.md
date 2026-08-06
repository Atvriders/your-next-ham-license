# Your Next Ham License — Design Spec

**Full title:** *Your Next Ham License: The General Course (2023–2027)*
**Repo:** `Atvriders/your-next-ham-license` (public), local dir `~/your-next-ham-license/`
**Type:** Educational nonfiction — upgrade course + exam prep for the US General class license
**Date:** 2026-07-23
**Status:** Draft — awaiting human sign-off before implementation planning.

This is **the middle book of the three-book series**, following *Your First Ham License: The Technician Course* (shipped from `~/your-first-ham-license/`). It reuses the Technician book's production machinery and method — the same toolchain, audit discipline (incl. pool-fidelity check), series-site machinery, and multi-agent workflow — per `/home/kasm-user/ham-book-program-plan.md` and the approved series plan. The Extra course follows with the same template.

> **Series note:** mounted at `/general/` on the series site; the book-switcher bar shows General highlighted, Technician live, Extra "coming soon."

---

## 1. Purpose & audience

A single-volume **upgrade course** that takes a **licensed Technician** to a passed **General class exam (Element 3, 2023–2027 pool)**. The reader already knows Ohm's law, repeater basics, and Part 97 fundamentals — this book assumes Book 2's knowledge and goes deeper: HF operating, real AC theory (reactance, impedance, resonance), practical circuits, and antennas/feedlines at a working level.

Two jobs at once, same method as Book 2:
- **Teaches** the deeper radio craft the General ticket opens up (HF bands, more power, more modes, more theory).
- **Prepares for the exam**: after each chapter, the reader can answer every question in the mapped pool subelement(s).

**Spine (organizing idea):** *going farther* — the upgrade from local VHF life to worldwide HF: what changes when your signal can cross oceans, and the deeper theory that makes it work.

**Non-goals:** not a beginner book (that's the Technician book); not the full reference depth of the Extra course; not a history book.

**Tone:** competent colleague-to-colleague — respects the reader's Technician knowledge, still plain-language, still worked and repeated for retention. Math is expected now (reactance, impedance, resonance, dB, power calculations), taught step by step with worked examples.

## 2. Relationship to Book 2 (what we reuse)

| Reused from Book 2 | Retargeted to this book |
|---|---|
| Toolchain (`tools/`, tests, CI, Docker, series machinery) | Copied; constants retargeted (title, chapters, ID3, GHCR image, `/general/` series highlight) |
| Canon discipline + pool-fidelity audit (check #8) | Same law; canon carries the **2023–2027 General pool verbatim** |
| Chapter skeleton & exam-prep integration | Same format laws (opener, teaching sections, worked examples, Exam Focus, Key Takeaways, FACT lines) |
| Audiobook (8 voices, chapters only) + player w/ auto-play-next | Same; new intro; chapters-only narration |
| `make_exam.py` | Same tool (General exam is also 35 Q, one per group, 26 to pass) |
| Series site | General highlighted; Technician live; Extra "coming soon" |

**Depth change (the real difference):** content ramps from Book 2's no-background beginner level to intermediate — real formulas, phasor-free but honest AC theory, Smith-chart *basics* (what it shows, not how to derive), more involved figures.

## 3. Source materials

- **NCVEC Element 3, 2023–2027 General pool** (public domain) — subelements **G1–G0**; question count and group structure verified at ingestion (expected ~400–460 questions across ~35 groups; exam = 35 Q, one per group, 26 to pass). Valid **2023-07-01 → 2027-06-30** — **this pool expires mid-2027**; the currency notice is prominent in the README, and the canon keeps the pool as a single replaceable file so the 2027–2031 swap is contained (replace pool files, re-audit, patch affected quotes).
- Source: <https://ncvec.org/index.php/2023-2027-general-question-pool> (verify exact URL at ingestion; ARRL mirror if hosted). Any errata since release incorporated, with the revision record pinned in the canon.
- **FCC Part 97** (public domain) — especially §97.301/§97.305 General privileges, §97.313 power limits.
- **Owned references:** ARRL Handbooks 1927–1983 at `~/leehite-callbooks/handbooks-arrl/` (depth reference only; reproduction only from the 7 PD editions, same ledger).
- **Book 2 itself** — this book references it as the series' foundation (cross-series consistency: same notation, same voice).
- Research workflow as before: pool ingestion → parallel researchers (Part 97 General privileges, per-subelement teaching notes G1–G5 / G6–G0, HF operating-practice color) → assembler writes `accuracy-canon.md` with zero UNVERIFIED.

## 4. Chapter outline (~9–11 chapters + 2 appendices, ~45–60k words, ~25–35 figures)

Mapping per handoff §5.2 Part I; the exact chapter set is finalized in the implementation plan after pool ingestion (group sizes may shift the split).

| # | Chapter (working titles) | Pool subelement(s) | Teaches |
|---|---|---|---|
| 00 | **The upgrade: why General, and how this book works** | — | What General opens (HF phone privileges, more bands); exam logistics refresher; how the book maps to the pool. ~2.5–3k |
| 01 | **Your HF privileges & the rules that come with them** | G1 | General band privileges exact; control operators; repeater/auxiliary; power limits. |
| 02 | **Operating on HF** | G2 | HF phone/CW/digital procedures; contests & DXing basics; band plans in depth; net discipline on HF. |
| 03 | **Propagation in depth** | G3 | The ionosphere properly (layers, MUF, critical frequency); NVIS; gray line; solar indices in plain terms; VHF+ propagation beyond line-of-sight. |
| 04 | **Station setup & good practice** | G4 | HF station design; grounding & bonding at HF; mobile/portable; interference management (RFI/TVI), test equipment basics. |
| 05 | **AC theory: reactance, impedance, resonance** | G5 | AC in components; X_L, X_C, impedance, phase (conceptual, honest math); series/parallel resonance, Q; impedance matching concepts. |
| 06 | **Components & devices** | G6 | Diodes/transistors in depth; amplifiers; oscillators; mixers; digital logic basics the pool tests. |
| 07 | **Practical circuits** | G7 | Power supplies (rectifiers, filters, regulators); amplifier classes; filters; oscillators/synthesizers at block level. |
| 08 | **Signals & emissions** | G8 | Modulation in depth (AM/SSB/FM/PM math-adjacent concepts); mixing & sidebands; digital modes on HF (FT8/PSK/RTTY); bandwidth & emission designators. |
| 09 | **Antennas & feedlines at General depth** | G9 | Antenna patterns & gain in depth; transmission lines (characteristic impedance, velocity factor, loss); SWR & matching; Smith-chart basics (reading, not deriving). |
| 10 | **Safety & RF exposure at General depth** | G0 | RF exposure evaluation & mitigation (MPE in depth); electrical/antenna safety at higher power. |
| A | **Appendix A: the complete 2023–2027 General pool** | all | Every question verbatim + one-line why naming the teaching chapter. Print-only. |
| B | **Appendix B: glossary & formulas** | — | Glossary from canon; the General formula set with micro-examples (reactance, resonance, dB, SWR). |

**Exam-prep integration:** identical to Book 2 — every teaching chapter ends with **Exam Focus** (pool IDs covered + 5–10 verbatim questions + answer + one-line why); Appendix A carries the full pool annotated; audit check #8 enforces byte-exact quotes and answer keys mechanically.

## 5. Per-chapter anatomy (format laws)

Identical skeleton to Book 2 (the audit enforces it): exact heading; opener paragraph; teaching `###` sections; figures via `{{fig:id}}`; ≥1 `> **Worked example:**`; optional `> **The math, if you want it:**` sidebars; `### Exam Focus`; `### Key Takeaways`; 3–5 `**FACT:**` lines verbatim from the canon; banned phrases unchanged; no fabricated quotations. Chapters 00 keeps the "checklist" adaptation (no pool); every other chapter owns its subelement(s) completely.

Depth-specific additions for this book: worked examples are real calculations (not arithmetic-only); where a formula appears, it is used at least once with pool-relevant numbers.

## 6. The accuracy canon

Same law as Book 2: canonical pool files (`canon/pool-general.txt` + `.json` with sha256s), pinned FACTs with sources, notation & units (identical standard as Book 2 — series consistency), glossary, subelement→chapter map, copyright ledger (carried over), resolved uncertainties (zero open markers), time-sensitive register (pool expiry 2027-06-30 prominently; fees re-verified at build time against the Book 2 register).

## 7. Copyright discipline

Identical rules: prose original; Part 97 + NCVEC pool public domain (verbatim reproduction); any pool figures redrawn as original SVGs; archival Handbook material only from the 7 PD editions, tagged; `figreg` enforces.

## 8. Production architecture

Identical to Book 2: Phase A (this spec → sign-off → task plan) → Phase B (scaffold copy from Book 2's repo — which now includes the h4 support, series machinery, and 50-test suite — retarget constants, verify pytest + fixture build + audit skip-state) → Phase C1 (pool ingestion + canon workflow) → Phase C2 (figures) → Phase C3 (chapters + appendix + span auditors) → Phase D (front matter) → Phase E (verify, one commit, GitHub repo via REST API, push, audiobook, release v1.0, CI→GHCR public, series-site flip: General goes live). Parallel fan-out; one commit at the end.

## 9. Deliverables

Same as Book 2: self-contained HTML/PDF/TXT; `make_exam.py`; 8-voice audiobook (chapters only) on release v1.0; Docker image `ghcr.io/atvriders/your-next-ham-license:latest`; series-site integration (General highlighted, `/general/` live); `AI-CONTEXT.md`; README with honest stats block; pool-currency notice incl. the **2027-06-30 expiry** and swap procedure.

## 10. Verification

Same gates: pytest green; `audit_book.py` exit 0 (8 checks incl. pool fidelity); real build; figure eyeballing; human-style spot-read of a chapter + appendix sample; then ship.

## 11. Open items / risks

- **Pool expiry (the big one):** this pool dies 2027-06-30, plausibly within a year of the build. Mitigation: contained-swap canon design + README notice + a documented swap procedure; the book's teaching content is durable — only Exam Focus picks and Appendix A change with the pool.
- **Depth calibration:** the G5/G6/G7 theory chapters risk either patronizing Technicians or outrunning them. Mitigation: span auditors explicitly grade "assumes Book 2, no more" per chapter.
- **Question count/structure unknown until ingestion** — chapter split may adjust; the implementation plan finalizes it.
- **Series consistency:** notation/voice must match Book 2 exactly (shared glossary entries stay byte-consistent where they overlap).
