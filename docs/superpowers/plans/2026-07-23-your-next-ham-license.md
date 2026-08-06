# Your Next Ham License — Implementation Plan

> **For agentic workers:** implement this plan task-by-task (subagent-driven development recommended). Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce *Your Next Ham License: The General Course (2023–2027)* — an ~48–52k-word (chapters), ~25–35-figure upgrade course + exam-prep book aligned to the **2023–2027 NCVEC General pool (Element 3)** — expected ~423 active questions across 10 subelements (G1–G9, G0) and 35 groups, exact counts **verified at ingestion** — as self-contained HTML/PDF/TXT editions plus Docker site, practice-exam generator, and 8-voice audiobook, built by a multi-agent workflow against a verified accuracy canon that carries the pool verbatim.

**Architecture:** Same two tracks as Book 2. **(A) Tooling** — the Technician repo's toolchain copied wholesale (it is the newest base: h4 support, series machinery, 50-test suite, `make_exam.py`, 8-check audit incl. pool fidelity) and retargeted at constants level only, plus one TDD extension (`mathsvg` for the General formula set). **(B) Content** — canon (incl. verbatim pool) → figures → 11 chapters + 2 appendices, produced by parallel writer/figure/auditor agents and gated by the Track-A harness. Track A first so Track B writes into a green gate. Spec phase letters: A = spec/plan (done) · B = scaffold (Phases 0–1) · C1 = canon (Phase 2) · C2 = figures (Phase 3) · C3 = chapters (Phase 4) · D = front matter (Phase 5) · E = verify & ship (Phase 6).

**Tech Stack:** Python 3 (stdlib + `edge-tts`, `matplotlib`), headless `google-chrome` for PDF, `ffmpeg` for audio, nginx/Docker, GitHub Actions → GHCR. Base for all copying: `/home/kasm-user/your-first-ham-license/` (the Technician repo — it carries the newer machinery). Design spec: `docs/superpowers/specs/2026-07-23-your-next-ham-license-design.md` (approved).

## Global Constraints

- **ONE commit at the very end**, after full verification (pytest green + `audit_book.py` exit 0 + real build + spot-reads). No per-task/phase commits. The only allowed exception is the cross-repo series-bar touch in the Technician repo (Phase 6) — its own tiny commit, **approved by the human at that moment, never assumed**.
- **Parallel fan-out when building**: figures, chapters, appendix annotations, audits run as parallel agents.
- **All repos/packages public.** Repo `Atvriders/your-next-ham-license`, branch `master`, GitHub-primary (no Gitea CI — dead path; do not copy `.gitea/`). Push only after the ship gate.
- **Never the `gh` CLI** — GitHub REST API via curl with the token from `~/.config/gh/hosts.yml`.
- **Pool fidelity is law:** question text, choices, and answer letters are quoted only from `canon/pool-general.*`, byte-exact. Never paraphrase a question; never repair a published quirk; **never retype pool text by hand** — quotes are pulled from the canonical files with script assistance (grep/awk/python extraction) and pasted mechanically.
- **Pool expiry is prominent:** this pool is valid 2023-07-01 → **2027-06-30**. The README carries the currency notice + swap procedure; the canon's time-sensitive register pins the expiry; the canon design keeps the pool as a single replaceable file pair so the 2027–2031 swap is contained (replace `canon/pool-general.*`, re-audit, patch drifted quotes).
- **Prose original; facts/Part 97/pool free.** No fabricated quotations; anecdotes framed as illustrative scenarios, never attributed to real people.
- **Depth law:** the book **assumes Book 2 knowledge — no more, no less**. Concepts beyond Technician scope are taught before use; Technician-scope material gets at most a one-line refresher + pointer to Book 2. Span auditors enforce this per chapter (Task 4.4).
- **Self-contained output:** inline SVG figures, math pre-rendered to inline SVG, inline CSS; no external refs (`src="http"`, `<link rel="stylesheet">`, `@import` are failures; SVG `xmlns` URIs are fine).
- **Environment:** `python3` (not `python`); `matplotlib`, `edge-tts`, `ffmpeg`, `google-chrome` present; no local Docker (CI builds the image).
- **Naming:** title *Your Next Ham License: The General Course (2023–2027)* (US spelling); audio ID3 `artist=Kimi K3`, `album=Your Next Ham License`; GHCR image `ghcr.io/atvriders/your-next-ham-license`; audiobook player `localStorage` key `ynhl-audio`; series mount path `/general/`.
- **sys.path gotcha:** every runnable script keeps `sys.path.insert(0, str(Path(__file__).resolve().parent.parent))`.
- **CI gotcha:** copy the Tech repo's *fixed* workflow (`seq -f "%02g"`, not `seq -w`), then adjust repo/image names and release URLs.
- **Notation law (series consistency):** identical to Book 2 — prose uses V and ×, verbatim pool quotes keep the pool's E/x form, unit case (kHz, MHz, mA, µV, pF) is load-bearing, λ(m) = 300 / f(MHz) taught as the pool's own approximation of c = f·λ.

## File Structure

```
your-next-ham-license/
├── accuracy-canon.md                 # THE BIBLE: pinned facts, notation, glossary, copyright ledger
├── canon/
│   ├── pool-general.txt              # the 2023–2027 General pool, byte-exact (human-readable)
│   ├── pool-general.json             # structured: id → {group, subelement, question, choices{A-D}, answer, figure?}
│   ├── source/                       # original NCVEC downloads (docx/pdf) + errata pages
│   └── ingestion-report.md           # double-parse evidence, counts, errata ledger, quirks
├── AI-CONTEXT.md                     # full machine context dump (Phase 5)
├── README.md                         # overview + formats + stats block + POOL-CURRENCY NOTICE (Phase 5/6)
├── requirements.txt  .gitignore  docker-compose.yml  Dockerfile
├── chapters/
│   ├── ch00.md … ch10.md             # 11 chapters (ch00 welcome + ch01–ch10 ↔ G1–G0)
│   └── specs/ch00.spec.md … ch10.spec.md
├── figures/
│   ├── <id>.svg  +  _gen_*.py        # original SVGs + matplotlib generators
│   └── figures.json                  # id, chapter, number (first-reference order), caption, kind, source, spoken
├── appendices/
│   ├── pool.md                       # Appendix A: the full General pool verbatim + one-line why
│   └── glossary-and-formulas.md      # Appendix B: glossary + General formula set
├── tools/                            # copied from the Technician repo, retargeted
│   ├── narration.py  figreg.py       # as-is (protected-years set unchanged, 1968–1983)
│   ├── mathsvg.py                    # copied + EXTENDED for the General formula set (Task 1.4)
│   ├── build_book.py                 # retargeted titles/colophon; SERIES_CURRENT="General"
│   ├── audit_book.py                 # G-IDs + G-sort-key + pool-driven coverage count; same 8 checks
│   ├── make_audiobook.py             # chapters 00–10 only; retargeted ID3/headings
│   ├── make_intro.py                 # new INTRO text (the upgrade welcome)
│   └── make_exam.py                  # same tool; default --pool canon/pool-general.json
├── docker/audiobook-index.html       # retargeted player (12 tracks; STORE key ynhl-audio)
├── series/                           # nginx.conf + index.html: Tech live, General live/current, Extra "coming soon"
├── series-docker-compose.yml         # tech + general live; extra behind `future` profile
├── .github/workflows/build.yml       # copied fixed version, retargeted
├── tests/                            # the 50-test suite, retargeted fixtures (G-IDs, deleted-ID gap)
│   └── fixtures/                     # ch_sample.md, ch_h4_sample.md, appendix_sample.md, fig_sample.svg, pool_sample.txt/json
└── docs/superpowers/{specs,plans}/…  # spec + this plan
```

---

## PHASE 0 — Scaffold (spec Phase B, part 1)

### Task 0.1: Repo skeleton + scaffold copy
- [x] Create `~/your-next-ham-license/` with dirs: `tools/ tests/ tests/fixtures/ chapters/ chapters/specs/ figures/ canon/ canon/source/ appendices/ docker/ series/ .github/workflows/ build/ audiobook/ docs/superpowers/specs/ docs/superpowers/plans/` (last two already exist with spec+plan).
- [x] Copy from the **Technician repo** `/home/kasm-user/your-first-ham-license/` (verbatim, then retarget in Phase 1): `tools/*.py` (incl. `__init__.py`), `tests/` (all 7 test files + fixtures), `pyproject.toml`, `requirements.txt`, `.gitignore`, `docker/audiobook-index.html`, `Dockerfile`, `docker-compose.yml`, `series/`, `series-docker-compose.yml`, `.github/workflows/build.yml`.
- [x] **Do NOT copy:** `chapters/`, `figures/*.svg`, `figures/figures.json`, `accuracy-canon.md`, `canon/`, `AI-CONTEXT.md`, `README.md`, `audiobook/`, `build/`, `appendices/`, `.git/`, `docs/`.
- [x] `git init -b master` (no commits until the end).
- [x] **Verify:** tree matches File Structure; `python3 -m pytest` collects (failures expected until retarget — that's Phase 1).

---

## PHASE 1 — Tooling retarget + extensions (spec Phase B, part 2; TDD)

### Task 1.1: Copy-through modules
- [x] `narration.py`, `figreg.py`: copy unchanged (book-agnostic; protected-years set already 1968–1983). Their tests should pass as-is.
- [x] **Verify:** `pytest tests/test_narration.py tests/test_figreg.py` green.

### Task 1.2: `build_book.py` retarget
- [x] Title/colophon/heading constants to this book; chapter glob `ch*.md` (11 chapters); include `appendices/pool.md` + `appendices/glossary-and-formulas.md` as final TOC sections (after ch10), without chapter numbers in headings.
- [x] Series constants: `SERIES_CURRENT = "General"`; `SERIES_BOOKS = [("Technician","/tech/",True), ("General","/general/",True), ("Extra","/extra/",False)]` — General flips to live in this repo now (the flag is inert until push; the book is live the moment it ships). Keep `/tech/`, `/general/`, `/extra/` as the only allowed absolute links (relative-links test unchanged).
- [x] Keep: repo-root sys.path bootstrap; self-contained HTML; h4 support (`####` group lines in Appendix A render as anchored `<h4>`s, never in TOC); PDF probe order `chromium/chromium-browser/google-chrome/google-chrome-stable` → weasyprint → skip.
- [x] Update `tests/test_build_book.py` + fixtures to this book's skeleton (same §5 format laws as Book 2: opener, `### Exam Focus`, `### Key Takeaways`, `**FACT:**`).
- [x] **Verify:** `pytest tests/test_build_book.py` green; fixture builds HTML+TXT; PDF builds via google-chrome.

### Task 1.3: `audit_book.py` retarget (same 8 checks, G-shaped)
- [x] Format-law checks stay the Book 2 skeleton with **one change: only ch00 is exempt** from Exam Focus / worked-example (ch10 owns subelement G0 here and is a full teaching chapter — Book 2 exempted ch00+ch10). Keep: `## <N>. <Title>` first line; opener paragraph; ≥1 `> **Worked example:**` in ch01–ch10; `### Exam Focus` in ch01–ch10; `### Key Takeaways`; 3–5 `**FACT:**` lines matching `accuracy-canon.md` verbatim; banned phrases unchanged ("little did they know", "in that moment", "a testament to").
- [x] Check #8 retarget: pool-quote regex `> **G#X##** <text>` + `**Answer: L**` (IDs G1A01…G0E##); `pool_sort_key` orders subelements G1…G9 then G0; coverage = **all ids in `canon/pool-general.json` exactly once, in canonical pool order** (count derived from the JSON, not hardcoded — the ingestion fixes the number); answer letters verified against the pool key; skips gracefully with a printed note when the pool JSON is absent.
- [x] Update fixtures: `tests/fixtures/pool_sample.txt/json` with G-style IDs **including a deleted-ID gap** (e.g. G1A03, G1A05 with no G1A04) so the coverage check tolerates non-contiguous numbering; keep the four #8 fixture tests (correct quote passes; one-word-off fails; wrong letter fails; missing pool → skip).
- [x] **Verify:** `pytest tests/test_audit_book.py` green; `python3 tools/audit_book.py` exits 0 on the empty scaffold (check #8 skipping gracefully).

### Task 1.4: `mathsvg.py` capability check + extension (TDD) — NEW SCOPE vs Book 2
- [x] Book 2's pool math was arithmetic-only; the General course teaches real formulas. Probe the copied `mathsvg.py` subset against the Appendix B formula list: reactance ($X_L = 2\pi f L$, $X_C = 1/(2\pi f C)$), resonance ($f = 1/(2\pi\sqrt{LC})$), decibels, SWR, impedance magnitude, plus subscripts ($X_L$), $\pi$, $\sqrt{}$, fractions.
- [x] Extend the subset with tests first (`tests/test_mathsvg.py`): one render test per formula above; every span must render to SVG at build time (audit check #4 is the backstop).
- [x] Keep the writer-facing law unchanged: **at most one `$…$` span per paragraph**, no literal `$` inside a math paragraph (write "35 dollars" in prose).
- [x] **Verify:** `pytest tests/test_mathsvg.py` green incl. the new formula tests.

### Task 1.5: `make_audiobook.py` + `make_intro.py` retarget
- [x] Chapter range 00–10 (11 chapters); `spoken_heading()` for `## <N>. <Title>`; ID3 `album=Your Next Ham License`, `artist=Kimi K3`; exclude `appendices/` from narration (Appendix A is print-only — decision carried from Book 2); keep sys.path bootstrap, chunking/retries, ffmpeg stitch.
- [x] New INTRO text (~1 min spoken): welcome to the upgrade — for licensed Technicians going farther to HF; keep `--dry`.
- [x] **Verify:** `pytest tests/test_audiobook_prepare.py` green; `python3 tools/make_intro.py --dry` prints sane text.

### Task 1.6: `make_exam.py` retarget
- [x] Logic unchanged (the General exam is also 35 Q, one per group, 26 to pass — §97.503(a)); change only the default `--pool` path to `canon/pool-general.json` and any T-flavored strings/fixtures to G.
- [x] Confirm the group model tolerates the deleted-ID gaps (one uniform-random draw per group from whatever ids exist).
- [x] **Verify:** `pytest tests/test_make_exam.py` green (count = one per group, seed reproducibility, no answers in the exam sheet, key correctness).

### Task 1.7: Docker + CI + player retarget
- [x] `Dockerfile`: serve this book's build artifacts; `docker-compose.yml`: image `ghcr.io/atvriders/your-next-ham-license:latest`.
- [x] `docker/audiobook-index.html`: title + 12 track labels (intro + ch00–ch10); **`localStorage` key `ynhl-audio`** (voice/track/position/auto-next); keep resume, visualizer, voice switcher, auto-play-next toggle, and the series bar (General highlighted).
- [x] `.github/workflows/build.yml`: copy the Tech repo's fixed version; repo/image names → this book; audio-fetch loop stays `seq -f "%02g" 0 10` (11 chapters, same count as Book 2); release `v1.0` on `Atvriders/your-next-ham-license`.
- [x] **Verify:** `python3 -m pytest` all green; `python3 tools/build_book.py --html --txt --pdf --out build/` succeeds on fixtures.

### Task 1.8: Series-site machinery retarget
- [x] `series/nginx.conf`: `/` → landing page; `/tech/` → tech container (active); `/general/` → general container (active — this book ships live); `/extra/` stays commented out.
- [x] `series/index.html`: three cards — Technician **live**, General **live + current highlight**, Extra **"coming soon"**.
- [x] `series-docker-compose.yml`: tech + general services live (General drops the `future` profile); extra stays behind `future`; proxy still the only published port (:8080).
- [x] **Verify:** YAML parses (validate with python — no local Docker); rebuilt fixture HTML shows the bar with General highlighted; player page shows bar + toggle (code review or rendered screenshot).

---

## PHASE 2 — Canon workflow (spec Phase C1; content gate 1)

### Task 2.1: Obtain + ingest the pool (serial, first)
- [x] Download the **2023–2027 General pool (Element 3), final document with all errata**, from the top of `https://ncvec.org/index.php/2023-2027-general-question-pool-release` (Word **and** PDF; also grab the standalone pool-figure graphic if posted separately). **URL correction:** the spec's draft URL (`…/2023-2027-general-question-pool`) 404s — the release page above is the verified page (checked 2026-07-24). Cross-check against the ARRL mirror at `https://www.arrl.org/question-pools`. Save originals under `canon/source/` and record sha256s.
- [x] Convert to `canon/pool-general.txt` (byte-exact human-readable: ID lines `G1A01 (B) [97.301]`, `~~` separators, published headings) and structured `canon/pool-general.json`. **Double-parse discipline, same as Book 2:** parse the `.docx` (authoritative) and independently re-parse the `.pdf` (`pdftotext -layout`); reconcile every question, choice, answer letter, and heading; write `canon/ingestion-report.md` with the full evidence.
- [x] **Errata ledger (pin in canon §1 — verified 2026-07-24 against the NCVEC release page):** released into the public domain by the NCVEC QPC (re-released with errata 2024-03-06 and 2024-11-08); six errata — Errata 1 (9 questions modified; **G9C06, G9D13 withdrawn**), Errata 2 (G1A05/G1E10/G9D01 modified; **G6B09 withdrawn**), 3rd errata 2023-12-01 (**G1C08, G1C10 withdrawn**; syllabus G1 count 57→55; G2E12 answer D modified), 4th errata 2024-03-06 (**G1E09 withdrawn**), 5th errata 2024-11-08 (**G8C01 withdrawn**), 6th errata 2026-02-04 (**G1A04, G1C09 withdrawn** — FCC 60 m rule change). The book always uses the fully-errata'd form. **Deleted IDs were never renumbered** — G1A has no 04, G1C no 08/09/10, G1E no 09, G6B no 09, G8C no 01, G9C no 06, G9D no 13.
- [x] **Verify (hard gate):** expected **~423 active questions** (432 at release − 9 withdrawn; the parse produces the authoritative number — record it in the canon and update any derived constants); 10 subelements G1–G9 + G0; **35 groups total** (syllabus confirms G1 = 5 groups / 5 exam questions; record the full group list + per-subelement counts in the canon); exam = 35 Q, one per group, 26 to pass; every active question has exactly 4 choices A–D and one keyed answer; zero parse drops — IDs contiguous within each group **except the nine pinned deletions**; the pool's figure-referencing questions flagged with their figure id (the 2023–2027 pool ships with a **single graphic** — historically Figure G7-1; exact id and referencing question ids come from the document, not memory); published quirks (typo'd citations, Unicode punctuation, spacing oddities) preserved byte-exactly, cataloged in the ingestion report, never repaired.
- [x] **Confirm at ingestion:** any errata posted **after** 2026-02-04 (the 6th) — check the release page top and the ARRL question-pool news; if a 7th errata exists, fold it in and extend the ledger before any writing starts.

### Task 2.2: Parallel researchers (fan-out)
- [ ] R1: Part 97 pinned facts for General — §97.301/§97.305 General band & emission privileges exact, §97.313 power limits, control-operator rules, repeater/auxiliary rules, **current 60 m privileges from eCFR §97.303** (the rule change that withdrew G1A04/G1C09 — pin the present text; never teach the withdrawn wording as current), with eCFR issue date + pull date recorded.
- [ ] R2: Exam & upgrade logistics — exam structure (35 Q, 26 pass, one per group), CSCE/upgrade credit, finding sessions, fees (re-verify against Book 2's register: FCC $35, ARRL VEC $15/$5, Form 605 2022 edition, Laurel VEC address), pool validity window **2023-07-01 → 2027-06-30** + the six-errata revision record.
- [ ] R3: Per-subelement teaching notes G1–G5 (what a **Technician** must learn to answer every question in the subelement; common confusions; calibrated to "assumes Book 2, no more").
- [ ] R4: Per-subelement teaching notes G6–G0 (same).
- [ ] R5: HF operating-practice color — contest & DX basics, net discipline on HF, FT8/digital culture, DXpedition/pileup etiquette, Q-signals in HF context.

### Task 2.3: Assembler
- [ ] One agent writes `accuracy-canon.md`: §1 pool record (files, sha256s, provenance, errata ledger, deleted-ID gap list, figure spec); §2 pinned FACTs with sources; §3 notation & units (**carried from Book 2 essentially unchanged** — series consistency); §4 glossary (shared entries stay byte-consistent with Book 2 where they overlap); §5 subelement→chapter map (**finalizes the chapter split from the ingested group sizes** — default: one subelement per chapter, G1→ch01 … G0→ch10; adjust only if a subelement's size demands it, before any chapter spec is written); §6 copyright ledger (carried over; pool PD, Part 97 PD, pool figure(s) redrawn, Handbook protected-years rule); §7 resolved uncertainties — **wording-law approach: every research flag closed to a sourced value or a deliberately careful wording, zero open markers**; time-sensitive register with **pool expiry 2027-06-30 prominent** and fees re-verified at build time.
- [ ] **Verify (gate):** 0 `UNVERIFIED` markers; `python3 tools/audit_book.py` canon checks pass (check #8 now live against the real pool); spot-read the canon.

---

## PHASE 3 — Figures workflow (spec Phase C2; content gate 2)

### Task 3.1: Figure list
- [x] Orchestrator writes `figures/figure-plan.md`: **~25–35 figures** across ch01–ch10 — General-privileges band charts (per-band, General vs Technician segments), ionosphere layers / MUF / critical-frequency diagrams, NVIS & gray-line geometry, reactance & resonance plots (matplotlib), filter/amplifier/power-supply block diagrams, modulation & sideband spectra, transmission-line figures (standing waves, velocity factor, loss), Smith-chart basics (reading, not deriving), antenna patterns & gain, RF-exposure geometry, station grounding/bonding at HF — **plus the pool figure(s) redrawn as original SVGs** (same components/labels as the NCVEC graphic; canon §1.4 is the binding redraw spec; registered `kind:"original"` with the note "redrawn from NCVEC pool figure …").
- [x] **Numbering law:** figure display numbers follow **first-reference order within each chapter** (pinned in `figures.json` at assembly, Task 3.3) — never by authoring order, so late insertions don't scramble the book.

### Task 3.2: Parallel figure agents
- [x] One agent per chapter authors that chapter's figures: hand-authored themeable SVG with `currentColor` for schematics/diagrams; matplotlib→SVG for plots (paired `_gen_<id>.py` scripts, post-process black→`currentColor`); each with caption + one-line **spoken** description (audio degradation).

### Task 3.3: Assembler + verify (gate)
- [x] Assembler writes `figures/figures.json` (id, chapter, number in first-reference order, caption, kind, source, spoken).
- [x] **Verify:** `figreg.validate()` → empty; all SVGs parse (XML); render ≥6 to PNG and **look at them**; the pool redraw(s) compared side-by-side with the official NCVEC graphic for content equality.

---

## PHASE 4 — Chapters workflow (spec Phase C3; content gate 3)

### Task 4.1: Chapter specs
- [ ] Orchestrator writes `chapters/specs/ch00.spec.md … ch10.spec.md`: per chapter — subelement(s) + pool groups owned (from canon §5), **exact first-line heading string in title case** (`## <N>. <Title>`, taken from the spec §4 table as finalized at 2.3 — writers may not improvise headings; this is what lets 11 parallel writers produce one TOC), required figure IDs (from 3.2), teaching beats, Exam Focus question selection (5–10 per chapter), worked-example topic (**a real calculation with pool-relevant numbers** — arithmetic-only is a defect at this level), and for ch00 the "Your upgrade checklist" adaptation (no pool, no Exam Focus).

### Task 4.2: Parallel chapter writers (11 agents)
- [ ] Each agent: reads canon + its pool slice + its spec + figure registry; writes `chapters/chNN.md` obeying the format laws (identical skeleton to Book 2): exact heading; opener paragraph (a concrete upgrade scenario + "in this chapter you'll learn …"); `###` teaching sections; `{{fig:id}}` on its own line; ≥1 `> **Worked example:**`; optional `> **The math, if you want it:**` sidebars; `### Exam Focus` (coverage line + 5–10 verbatim questions + answer + one-line why); `### Key Takeaways`; 3–5 `**FACT:**` lines copied **byte-exact** from `accuracy-canon.md` as standalone plain paragraphs (never inside blockquotes).
- [ ] **Build-dialect laws (carry the hard-won lessons — violations break the build):** consecutive non-blank lines join into one paragraph, so bullets are **blank-line-separated**; a blockquote is consecutive `>` lines joined with spaces (six-line quote blocks; no stray adjacent `>` lines); **at most one `$…$` span per paragraph**, no literal `$` in a math paragraph; blockquote classes by prefix (`**Worked example:**`, `**The math, if you want it:**`); `***` is a section rule; emphasis `**bold**` / `*italic*` only.
- [ ] **Pool-quote law:** every Exam Focus quote is extracted **script-assisted** from `canon/pool-general.*` (grep/awk/python — never hand-typed); correct answer letter from the pool key; why lines are one line, plain language, ending **"— taught in chapter N."** where cross-referencing, and never paraphrase the question.
- [ ] Depth: worked examples are real calculations (reactance, resonance, dB, SWR, impedance); where a formula appears it is used at least once with pool-relevant numbers; anything beyond Book 2 scope is taught before use; Book 2 material gets a one-line refresher at most.

### Task 4.3: Appendices (parallel)
- [x] **Appendix A, fragment-per-subelement (10 agents, G1–G0):** each agent emits one fragment file with its subelement's section — every active question exactly once, in canonical order (group A→last, ascending number, **skipping the nine pinned deletions**), each entry one six-line blockquote (`> **G1A01** <verbatim question>` / `> A. …` … / `> **Answer: B** — <one-line why, naming the teaching chapter: "… — taught in chapter 1.">`), followed by the **Published ID line on a separate plain-text line after the blockquote, in backticks** (never inside the quote — the audit would read it as question text); redrawn pool figure embedded on the line before its first referencing quote and named thereafter. All quotes script-extracted, never retyped.
- [x] **Assemble + byte-exact gate:** the assembler concatenates fragments in canonical order (G1…G9 then G0), normalizes each `###` subelement heading to the **published title + counts** (optional `####` group lines render as h4), then runs the **fragment byte-exact gate**: re-extract every question from the assembled `appendices/pool.md` and diff mechanically against `canon/pool-general.json` (audit check #8 does this book-wide; run it per-fragment at handoff too). Print-only — never narrated.
- [ ] **Appendix B (one agent):** glossary as a two-column table (canon §4 definitions verbatim) + the **General formula set** — reactance, resonance, dB, SWR, impedance (+ the Book 2 carry-overs: Ohm's law, power, wavelength shortcut, prefix ladder) — each with a plain statement and one worked micro-example using the pool's own numbers, plus the notation-and-units subsection (E/x vs V/×, unit case, c, f = 1/T).

### Task 4.4: Span auditors (parallel, 3–4 agents)
- [ ] Each audits a span of chapters: every fact/value/frequency/privilege against canon; every question quote + letter against the pool (mechanically assisted by check #8); format laws; build-dialect laws; fix surgically in place.
- [ ] **Depth-calibration check (explicit, per chapter):** grade "assumes Book 2 knowledge — no more, no less". Flag any paragraph that re-teaches Technician material at length, and any that uses post-Technician theory without teaching it first. G5/G6/G7 are the risk chapters — read them hardest.
- [ ] Tone: competent colleague-to-colleague; banned-phrase grep clean.

### Task 4.5: Verify (gate)
- [ ] `python3 tools/audit_book.py` — all 8 checks green (incl. #8: full active-pool coverage in Appendix A exactly once in canonical order, all quotes verbatim, all letters correct).
- [ ] Full build HTML/PDF/TXT; spot-read 1 full chapter + 20 random Appendix A entries against the official NCVEC document; banned-phrase grep clean.

---

## PHASE 5 — Front matter (spec Phase D)

- [ ] `AI-CONTEXT.md`: full machine dump in Book 2's shape (canon summary, outline, pool facts + six-errata revision record + deleted-ID list, format laws, build-dialect laws, figure pipeline, tooling, series machinery, time-sensitive register with the 2027-06-30 expiry, production history; no credentials).
- [ ] `README.md`: overview, formats table, Docker/audiobook instructions, `make_exam.py` usage, **pool-currency notice (prominent): valid 2023-07-01 → 2027-06-30**, plus the swap procedure (replace `canon/pool-general.*` → re-audit — check #8 flags every drifted quote and coverage gap → patch quotes script-assisted → update FACT lines → rebuild; note that only Exam Focus picks and Appendix A change with the pool — the teaching content is durable), "How it was made" stats block (clearly-labeled token estimate + wall-time; finalized at push).

---

## PHASE 6 — Verify & ship (spec Phase E)

- [ ] Clean rebuild from scratch; `pytest` green; `audit_book.py` exit 0; human-style spot-read.
- [ ] **Ship gate (human confirms before outward actions).**
- [ ] One commit (trailer `Co-Authored-By: Kimi K3 <noreply@moonshot.cn>`).
- [ ] Create GitHub repo via REST API (`POST /user/repos`, `private:false`; token from `~/.config/gh/hosts.yml`; never `gh`); push `master`.
- [ ] Generate audiobook: `make_audiobook.py --all` (8 voices × 11 chapters, chapters only) + `make_intro.py`.
- [ ] Create release **v1.0**; upload audio assets (audio ships on the release, not in git).
- [ ] `workflow_dispatch` the CI; confirm image builds and `ghcr.io/atvriders/your-next-ham-license:latest` is anonymously pullable (`docker pull` unauthenticated or manifest check via curl).
- [ ] **Series site flip — General goes live:** this repo already ships with General highlighted + `/general/` active (Task 1.8); verify the series bar and landing render General live, Technician live, Extra "coming soon" once the image is public.
- [ ] **Cross-repo touch (its own tiny commit — human approves at this moment, not assumed):** in `/home/kasm-user/your-first-ham-license/`, flip General's `SERIES_BOOKS` flag to `True` in `tools/build_book.py` (and the player's bar if it carries its own copy), update `series/index.html` so the General card shows live, rebuild, run pytest + audit, and commit that change **alone** in the Technician repo (message e.g. "Series: General is live"). Push after its own verification. This is the one approved exception to the one-commit rule and requires explicit human sign-off at the time.
- [ ] Write final token/time stats into README (amend or second tiny README-only commit if the human allows; otherwise include in the one commit by generating audio before committing).

---

## Tracking & cost notes

- Book 2 cost reference: ~47 subagent launches; this book reuses its toolchain nearly unchanged (no new audit check, one mathsvg extension) but adds a messier pool (6 errata, 9 deletions, non-contiguous IDs) — budget ~45–55 agents, ~5–6M tokens, ~2 h wall-time.
- Mark plan checkboxes as tasks complete; keep the human informed at each content gate (2.3, 3.3, 4.5) and the ship gate.
