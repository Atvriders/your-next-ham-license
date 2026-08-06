"""Interactive study pages for Your Next Ham License.

Generates two self-contained, CSP-safe HTML pages from the canonical pool
data — everything (pool JSON, the redrawn figure SVG, CSS, JS) inlined, no
external references:

  practice.html    -- draws a valid General exam: exactly one question
                      per NCVEC group (35 groups -> 35 questions, 26 to
                      pass), click-to-answer, grading with score, pass/fail
                      and a per-question review (your answer, the correct
                      answer, and the one-line why), plus a per-subelement
                      drill mode with immediate feedback.
  flashcards.html  -- all 423 questions as flippable cards: front = question
                      + choices, back = correct answer + why + a hint naming
                      the published group theme and the chapter that teaches
                      it. Subelement filter, shuffle, and a "review later"
                      mark persisted in localStorage ("ynhl-study").
                      Keyboard: space/enter flips, arrows move, M marks.

Record assembly (testable in Python): each pool question becomes
  {id, group, subelement, question, choices{A..D}, answer, why, groupTheme,
   chapter, figure?}
where ``why`` comes from the ``> **Answer: X** — <why>`` lines of
``appendices/pool.md``, ``groupTheme`` is the published group heading from
``canon/pool-general.txt``, and ``chapter`` follows the subelement ->
chapter map of ``accuracy-canon.md`` §5 (one subelement per chapter:
G1 -> ch01 … G9 -> ch09, G0 -> ch10). The 5 figure questions get the
redrawn pool figure SVG (``figures/ch07-pool-fig-g71.svg``) embedded inline.

Usage:
  python3 tools/make_study.py [--out build/]
      [--pool canon/pool-general.json] [--appendix appendices/pool.md]
      [--pool-txt canon/pool-general.txt] [--figures-dir figures]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Allow running this file directly (`python3 tools/make_study.py`), where
# Python puts this script's own directory (tools/) on sys.path rather than
# the repo root. Harmless no-op when imported as `tools.make_study`.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from tools.make_exam import load_pool, pool_sort_key  # noqa: E402

DEFAULT_POOL_PATH = "canon/pool-general.json"
DEFAULT_APPENDIX_PATH = "appendices/pool.md"
DEFAULT_POOL_TXT_PATH = "canon/pool-general.txt"
DEFAULT_FIGURES_DIR = "figures"

POOL_QUESTION_COUNT = 423

# The only pool questions that reference a figure (accuracy-canon.md §1.4):
# all five point at the pool's single graphic, Figure G7-1.
FIGURE_QUESTION_IDS = frozenset({
    "G7A09", "G7A10", "G7A11", "G7A12", "G7A13",
})

# Redrawn pool figure (figures/figures.json: kind "original", redrawn from
# the NCVEC pool figure).
FIGURE_FILES = {
    "G7-1": "ch07-pool-fig-g71.svg",
}

# Subelement -> teaching chapter (accuracy-canon.md §5): one subelement per
# chapter, G1 -> ch01 … G9 -> ch09, G0 -> ch10. No splits.
_SUBELEMENT_CHAPTER = {
    "G1": 1, "G2": 2, "G3": 3, "G4": 4, "G5": 5,
    "G6": 6, "G7": 7, "G8": 8, "G9": 9, "G0": 10,
}

_GROUP_HEADING_RE = re.compile(r"^(G\d[A-F]) – (\S.*\S)\s*$")
_SUBELEMENT_RE = re.compile(r"^SUBELEMENT (G\d) – (.+?) \[\d+ Exam Questions? – \d+ [Gg]roups?\]\s*$")
_ENTRY_ID_RE = re.compile(r"^> \*\*(G\d[A-F]\d\d)\*\*")
_ANSWER_RE = re.compile(r"^> \*\*Answer: ([A-D])\*\* — (.*\S)\s*$")


def parse_group_headings(pool_txt: str) -> dict:
    """Published group headings from the canonical pool text: ``G1A`` ->
    "General class control operator frequency privileges; ...". Headings are
    published as ``G1A – <theme>`` (en dash); question ID lines
    (``G1A01 (C)``) never match: a digit, not a space, follows the group
    letter there."""
    headings = {}
    for line in pool_txt.splitlines():
        m = _GROUP_HEADING_RE.match(line)
        if m:
            headings[m.group(1)] = m.group(2)
    return headings


def parse_subelement_titles(pool_txt: str) -> dict:
    """Published subelement titles: ``G1`` -> ``COMMISSION’S RULES`` (case as
    published in the pool document; the bracket tail is en-dash punctuated
    and G4 prints "groups" lowercase)."""
    titles = {}
    for line in pool_txt.splitlines():
        m = _SUBELEMENT_RE.match(line)
        if m:
            titles[m.group(1)] = m.group(2)
    return titles


def parse_whys(appendix_md: str) -> dict:
    """The one-line "why" of every appendix entry: question id ->
    (answer letter, why text), parsed from ``> **Answer: X** — <why>``."""
    whys = {}
    current = None
    for line in appendix_md.splitlines():
        m = _ENTRY_ID_RE.match(line)
        if m:
            current = m.group(1)
        m = _ANSWER_RE.match(line)
        if m and current:
            whys[current] = (m.group(1), m.group(2))
    return whys


def chapter_for(subelement: str, group: str) -> int:
    """Chapter that teaches this question (accuracy-canon.md §5)."""
    return _SUBELEMENT_CHAPTER[subelement]


def build_records(pool: dict, whys: dict, headings: dict) -> list:
    """Assemble one study record per pool question, in canonical pool order.

    Raises ValueError on any inconsistency between the three sources (a
    missing why, an answer-letter drift, a missing group heading) — the
    pages are never generated from a partial dataset.
    """
    records = []
    for qid in sorted(pool, key=pool_sort_key):
        entry = pool[qid]
        if qid not in whys:
            raise ValueError(f"no why found in the appendix for {qid}")
        letter, why = whys[qid]
        if letter != str(entry["answer"]):
            raise ValueError(
                f"{qid}: appendix answer letter {letter} != pool answer {entry['answer']}")
        group = str(entry["group"])
        if group not in headings:
            raise ValueError(f"no published group heading found for {group} ({qid})")
        rec = {
            "id": qid,
            "group": group,
            "subelement": str(entry["subelement"]),
            "question": str(entry["question"]),
            "choices": dict(entry["choices"]),
            "answer": str(entry["answer"]),
            "why": why,
            "groupTheme": headings[group],
            "chapter": chapter_for(str(entry["subelement"]), group),
        }
        if entry.get("figure"):
            rec["figure"] = str(entry["figure"])
        records.append(rec)
    return records


def validate_records(records: list, expected_count: int = POOL_QUESTION_COUNT,
                     figure_ids=FIGURE_QUESTION_IDS) -> None:
    """Fail loudly unless the record set is exactly what the pages promise:
    the full pool, every record complete, figure references only on the
    known figure questions."""
    if len(records) != expected_count:
        raise ValueError(f"expected {expected_count} records, got {len(records)}")
    for rec in records:
        for field in ("why", "groupTheme"):
            if not str(rec.get(field, "")).strip():
                raise ValueError(f"{rec['id']}: empty {field}")
        if not rec.get("chapter"):
            raise ValueError(f"{rec['id']}: empty chapter")
    actual = {rec["id"] for rec in records if rec.get("figure")}
    if actual != set(figure_ids):
        raise ValueError(
            f"figure references {sorted(actual)} != expected {sorted(figure_ids)}")


def load_figures(figures_dir) -> dict:
    """The redrawn pool figure, inlined: ``G7-1`` -> SVG markup."""
    figures = {}
    for fig_id, name in FIGURE_FILES.items():
        path = Path(figures_dir) / name
        if not path.exists():
            raise ValueError(f"pool figure not found: {path}")
        figures[fig_id] = path.read_text(encoding="utf-8").strip()
    return figures


def subelement_summaries(records: list, titles: dict) -> list:
    """Per-subelement counts + published titles, ordered G1–G9 then G0."""
    counts: dict[str, int] = {}
    for rec in records:
        counts[rec["subelement"]] = counts.get(rec["subelement"], 0) + 1
    order = sorted(counts, key=lambda s: 10 if s == "G0" else int(s[1:]))
    return [{"id": s, "title": titles.get(s, ""), "count": counts[s]} for s in order]


def _embed_json(obj) -> str:
    """JSON safe to inline in a <script> block (``</`` can never close it)."""
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def _render(template: str, records: list, figures: dict, subelements: list) -> str:
    html = template.replace("__HEAD_CSS__", _HEAD_CSS)
    html = html.replace("__SERIES_BAR__", _SERIES_BAR)
    html = html.replace("__RECORDS_JSON__", _embed_json(records))
    html = html.replace("__FIGURES_JSON__", _embed_json(figures))
    html = html.replace("__SUBELEMENTS_JSON__", _embed_json(subelements))
    leftovers = re.findall(r"__[A-Z_]+__", html)
    if leftovers:
        raise ValueError(f"unsubstituted template tokens: {sorted(set(leftovers))}")
    return html


def render_flashcards_html(records: list, figures: dict, subelements: list) -> str:
    return _render(_FLASHCARDS_TEMPLATE, records, figures, subelements)


def render_practice_html(records: list, figures: dict, subelements: list) -> str:
    return _render(_PRACTICE_TEMPLATE, records, figures, subelements)


# ---------------------------------------------------------------------------
# Page templates. The chrome (CSS variables, series bar, header, light/dark
# handling) matches docker/audiobook-index.html.
# ---------------------------------------------------------------------------

_HEAD_CSS = """
:root {
  color-scheme: light dark;
  --paper: #f7f3ec; --ink: #2b2620; --muted: #7a7060; --rule: #cfc6b6;
  --link: #8a6a24; --panel: #efe9dd;
  --beam: #e8c877; --beam-hi: #ffe6ac; --glow: rgba(232,200,119,.55);
  --ok: #3f7d3f; --bad: #b04a32;
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #131110; --ink: #ddd6c9; --muted: #968d7c; --rule: #322d25;
    --link: #d8c390; --panel: #1b1815;
    --ok: #7fbf7f; --bad: #d98a76;
  }
}
:root[data-theme="light"] { --paper:#f7f3ec; --ink:#2b2620; --muted:#7a7060; --rule:#cfc6b6; --link:#8a6a24; --panel:#efe9dd; }
:root[data-theme="dark"] { --paper:#131110; --ink:#ddd6c9; --muted:#968d7c; --rule:#322d25; --link:#d8c390; --panel:#1b1815; }

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  background: var(--paper); color: var(--ink);
  font-family: Georgia, 'Iowan Old Style', 'Times New Roman', serif;
  font-size: 1.0625rem; line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}
.label { font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  text-transform: uppercase; letter-spacing: .22em; font-size: .68rem; }
.tnum { font-variant-numeric: tabular-nums; }
a { color: var(--link); }
.page { max-width: 46em; margin: 0 auto; padding: 2rem 1.4rem 6rem; }

.series-bar { display: flex; flex-wrap: wrap; justify-content: center; align-items: baseline;
  gap: .4em 1.6em; margin-bottom: 2.6rem; padding-bottom: .85rem;
  border-bottom: 1px solid var(--rule);
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  font-size: .7rem; text-transform: uppercase; letter-spacing: .18em; }
.series-bar a { color: var(--muted); text-decoration: none;
  padding-bottom: .15em; border-bottom: 2px solid transparent; }
.series-bar a:hover { color: var(--link); }
.series-bar a.current { color: var(--ink); border-bottom-color: var(--beam); }

header { text-align: center; margin-bottom: 2.2rem; }
.over { color: var(--muted); }
h1 { font-size: 2.5rem; font-weight: normal; letter-spacing: .05em; margin: .7rem 0 .5rem; }
.sub { font-style: italic; color: var(--muted); }
.tagline { text-align: center; color: var(--muted); font-size: .82rem; margin-top: .4rem; }
.back { margin-top: 1.1rem; }
.back a { text-decoration: none; margin: 0 .15em; }
.back a:hover { text-decoration: underline; }
.dot { color: var(--muted); }

.btn { font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  font-size: .7rem; text-transform: uppercase; letter-spacing: .14em;
  color: var(--muted); background: none; border: 1px solid var(--rule);
  border-radius: 999px; padding: .55em 1.3em; cursor: pointer;
  transition: border-color .18s, color .18s, box-shadow .25s; }
.btn:hover { border-color: var(--beam); color: var(--ink); }
.btn:focus-visible { outline: 2px solid var(--beam); outline-offset: 3px; }
.btn[aria-pressed="true"] { color: var(--ink); border-color: var(--beam);
  box-shadow: 0 0 0 1px var(--beam), 0 0 14px -4px var(--glow); }
.btn:disabled { opacity: .4; cursor: default; }
.btn:disabled:hover { border-color: var(--rule); color: var(--muted); }
select { font-family: system-ui, -apple-system, 'Segoe UI', sans-serif; font-size: .8rem;
  background: var(--panel); color: var(--ink); border: 1px solid var(--rule);
  border-radius: 8px; padding: .5em .7em; max-width: 100%; }
select:focus-visible { outline: 2px solid var(--beam); outline-offset: 2px; }

.fig { margin: .8rem auto; max-width: 30em; }
.fig svg { width: 100%; height: auto; display: block; color: var(--ink); }

.note { max-width: 34em; margin: 4.5rem auto 0; text-align: center; color: var(--muted); }
.note h2 { color: var(--muted); font-weight: normal; margin-bottom: 1.1rem; }
.note p { margin-bottom: 1em; }
.note a { text-decoration: none; }
.note a:hover { text-decoration: underline; }

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
}
"""

_SERIES_BAR = """<nav class="series-bar" aria-label="Books in this series">
  <a href="/tech/">Technician</a>
  <a class="current" href="/general/" aria-current="page">General</a>
  <a href="/extra/">Extra</a>
</nav>
"""

_FLASHCARDS_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Your Next Ham License — Flashcards</title>
<style>__HEAD_CSS__
/* ---- flashcards ---- */
.controls { display: flex; flex-wrap: wrap; gap: .6rem; justify-content: center;
  align-items: center; margin: 0 0 1.6rem; }
.card { border: 1px solid var(--rule); border-radius: 14px; background: var(--panel);
  padding: 1.5rem 1.6rem 1.3rem; cursor: pointer;
  height: 28rem; overflow-y: auto; }
.card:hover { border-color: var(--beam); }
.card:focus-visible { outline: 2px solid var(--beam); outline-offset: 3px; }
.badge { color: var(--muted); }
.qtext { font-size: 1.15rem; margin: .6rem 0 1rem; }
.choices { list-style: none; }
.choices li { padding: .35em 0; border-bottom: 1px dotted var(--rule); }
.choices li:last-child { border-bottom: 0; }
.choices .l { font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  color: var(--muted); margin-right: .55em; font-size: .85rem; }
.tap { margin-top: 1rem; text-align: center; color: var(--muted); font-size: .8rem;
  font-style: italic; }
.ansline { font-size: 1.1rem; margin: .5rem 0 .8rem; }
.ansletter { color: var(--link); }
.why { margin-bottom: .4rem; }
.hint { color: var(--muted); font-style: italic; font-size: .92rem;
  border-top: 1px dotted var(--rule); padding-top: .8rem; margin-top: 1rem; }
.navrow { display: flex; flex-wrap: wrap; gap: .6rem; justify-content: center;
  align-items: center; margin-top: 1.4rem; }
.pos { color: var(--muted); min-width: 5.5em; text-align: center; }
.empty { text-align: center; color: var(--muted); border: 1px dashed var(--rule);
  border-radius: 14px; padding: 3rem 1.5rem; }
.keys { text-align: center; color: var(--muted); font-size: .78rem; margin-top: 1.2rem; }
</style>
</head>
<body>
<div class="page">

__SERIES_BAR__
<header>
  <p class="over label">Flashcards</p>
  <h1>Your Next Ham License</h1>
  <p class="sub">The General Course (2023&ndash;2027)</p>
  <p class="tagline">all 423 pool questions &middot; hints &amp; explanations &middot; marks that stick</p>
  <p class="back">
    <a href="../">&larr; Read the book</a> <span class="dot">&middot;</span>
    <a href="practice.html">Practice exam</a> <span class="dot">&middot;</span>
    <a href="../your-next-ham-license.pdf">PDF</a> <span class="dot">&middot;</span>
    <a href="../your-next-ham-license.txt">Text</a>
  </p>
</header>

<div class="controls">
  <select id="filter" aria-label="Filter by subelement"></select>
  <button class="btn" id="shuffleBtn" type="button">Shuffle</button>
  <button class="btn" id="resetBtn" type="button">Pool order</button>
  <button class="btn" id="markedOnlyBtn" type="button" aria-pressed="false">Marked only</button>
</div>

<div class="card" id="card" tabindex="0" role="button" aria-label="Flashcard — activate to flip">
  <div id="front"></div>
  <div id="back" style="display:none"></div>
</div>
<p class="empty" id="empty" style="display:none">No cards match — clear the &ldquo;marked only&rdquo; filter or pick another subelement.</p>

<div class="navrow">
  <button class="btn" id="prevBtn" type="button">&larr; Prev</button>
  <button class="btn" id="flipBtn" type="button">Flip</button>
  <button class="btn" id="nextBtn" type="button">Next &rarr;</button>
  <span class="pos tnum" id="pos"></span>
  <button class="btn" id="markBtn" type="button" aria-pressed="false">&#9734; Review later</button>
</div>
<p class="keys">Space / enter flips &middot; &larr; &rarr; move &middot; M marks for review &middot; <span id="markCount" class="tnum"></span></p>

<section class="note">
  <h2 class="label">About these cards</h2>
  <p>Every question, choice, and answer key is verbatim from the NCVEC 2023&ndash;2027 General pool (public domain; valid for exams 2023-07-01 through 2027-06-30). The one-line explanations are this book&rsquo;s own, and each card&rsquo;s hint names the published pool group and the chapter that teaches it. Figure G7-1 is redrawn from the pool original.</p>
  <p><a href="../">Read the book</a> &middot; <a href="practice.html">Take a practice exam</a></p>
</section>

</div>

<script>
(function () {
  "use strict";
  var RECORDS = __RECORDS_JSON__;
  var SUBELEMENTS = __SUBELEMENTS_JSON__;
  var FIGURES = __FIGURES_JSON__;
  var STORE = "ynhl-study";

  function loadMarks() {
    try {
      var d = JSON.parse(localStorage.getItem(STORE) || "{}");
      var s = {};
      (d.reviewLater || []).forEach(function (id) { s[id] = true; });
      return s;
    } catch (e) { return {}; }
  }
  function saveMarks() {
    try { localStorage.setItem(STORE, JSON.stringify({ reviewLater: Object.keys(marks) })); } catch (e) {}
  }

  var marks = loadMarks();
  var filter = "ALL", markedOnly = false, view = [], pos = 0, flipped = false;

  var filterSel = document.getElementById("filter"),
      shuffleBtn = document.getElementById("shuffleBtn"),
      resetBtn = document.getElementById("resetBtn"),
      markedOnlyBtn = document.getElementById("markedOnlyBtn"),
      cardEl = document.getElementById("card"),
      frontEl = document.getElementById("front"),
      backEl = document.getElementById("back"),
      emptyEl = document.getElementById("empty"),
      prevBtn = document.getElementById("prevBtn"),
      flipBtn = document.getElementById("flipBtn"),
      nextBtn = document.getElementById("nextBtn"),
      markBtn = document.getElementById("markBtn"),
      posEl = document.getElementById("pos"),
      markCountEl = document.getElementById("markCount");

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  var ALL_LABEL = "All subelements (" + RECORDS.length + ")";
  filterSel.appendChild(el("option", null, ALL_LABEL)).value = "ALL";
  SUBELEMENTS.forEach(function (s) {
    var opt = el("option", null, s.id + " — " + s.title + " (" + s.count + ")");
    opt.value = s.id;
    filterSel.appendChild(opt);
  });

  function poolFiltered() {
    return RECORDS.filter(function (r) {
      return (filter === "ALL" || r.subelement === filter) && (!markedOnly || marks[r.id]);
    });
  }
  function resetView() { view = poolFiltered(); pos = 0; flipped = false; render(); }

  function renderCardFace(rec) {
    frontEl.innerHTML = "";
    frontEl.appendChild(el("div", "badge label",
      rec.id + " · " + rec.group + (rec.figure ? " · Figure " + rec.figure : "")));
    if (rec.figure && FIGURES[rec.figure]) {
      var f = el("div", "fig");
      f.innerHTML = FIGURES[rec.figure];
      frontEl.appendChild(f);
    }
    frontEl.appendChild(el("p", "qtext", rec.question));
    var ul = el("ul", "choices");
    ["A", "B", "C", "D"].forEach(function (L) {
      var li = el("li");
      li.appendChild(el("span", "l", L + "."));
      li.appendChild(document.createTextNode(rec.choices[L]));
      ul.appendChild(li);
    });
    frontEl.appendChild(ul);
    frontEl.appendChild(el("p", "tap", "Click or press space to flip"));

    backEl.innerHTML = "";
    backEl.appendChild(el("div", "badge label", rec.id + " · " + rec.group));
    if (rec.figure && FIGURES[rec.figure]) {
      var fb = el("div", "fig");
      fb.innerHTML = FIGURES[rec.figure];
      backEl.appendChild(fb);
    }
    var ans = el("p", "ansline");
    var strong = el("span", "ansletter", "Correct answer: " + rec.answer);
    ans.appendChild(strong);
    ans.appendChild(document.createTextNode(" — " + rec.choices[rec.answer]));
    backEl.appendChild(ans);
    backEl.appendChild(el("p", "why", rec.why));
    backEl.appendChild(el("p", "hint",
      "Hint: this is " + rec.groupTheme + " — review chapter " + rec.chapter + "."));
  }

  function render() {
    var n = view.length;
    posEl.textContent = n ? (pos + 1) + " / " + n : "0 / 0";
    cardEl.style.display = n ? "" : "none";
    emptyEl.style.display = n ? "none" : "";
    if (n) {
      var rec = view[pos];
      renderCardFace(rec);
      frontEl.style.display = flipped ? "none" : "";
      backEl.style.display = flipped ? "" : "none";
      markBtn.innerHTML = marks[rec.id] ? "&#9733; Marked" : "&#9734; Review later";
      markBtn.setAttribute("aria-pressed", marks[rec.id] ? "true" : "false");
      prevBtn.disabled = pos === 0;
      nextBtn.disabled = pos === n - 1;
    }
    markCountEl.textContent = Object.keys(marks).length + " marked for review";
  }

  function flip() { if (view.length) { flipped = !flipped; render(); } }
  function move(d) {
    if (!view.length) return;
    pos = Math.min(view.length - 1, Math.max(0, pos + d));
    flipped = false;
    render();
  }
  function toggleMark() {
    if (!view.length) return;
    var rec = view[pos];
    if (marks[rec.id]) delete marks[rec.id]; else marks[rec.id] = true;
    saveMarks();
    if (markedOnly && !marks[rec.id]) {
      view = poolFiltered();
      pos = Math.min(pos, Math.max(0, view.length - 1));
      flipped = false;
    }
    render();
  }

  cardEl.addEventListener("click", flip);
  flipBtn.addEventListener("click", flip);
  prevBtn.addEventListener("click", function () { move(-1); });
  nextBtn.addEventListener("click", function () { move(1); });
  markBtn.addEventListener("click", toggleMark);
  shuffleBtn.addEventListener("click", function () {
    for (var i = view.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = view[i]; view[i] = view[j]; view[j] = t;
    }
    pos = 0; flipped = false;
    render();
  });
  resetBtn.addEventListener("click", resetView);
  markedOnlyBtn.addEventListener("click", function () {
    markedOnly = !markedOnly;
    markedOnlyBtn.setAttribute("aria-pressed", markedOnly ? "true" : "false");
    resetView();
  });
  filterSel.addEventListener("change", function () { filter = filterSel.value; resetView(); });

  document.addEventListener("keydown", function (e) {
    if (/^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
    if (e.target.tagName === "BUTTON" && (e.key === " " || e.key === "Enter")) return;
    if (e.key === " " || e.key === "Enter") { e.preventDefault(); flip(); }
    else if (e.key === "ArrowLeft") { e.preventDefault(); move(-1); }
    else if (e.key === "ArrowRight") { e.preventDefault(); move(1); }
    else if (e.key === "m" || e.key === "M") toggleMark();
  });

  resetView();
})();
</script>
</body>
</html>
"""

_PRACTICE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Your Next Ham License — Practice Exam</title>
<style>__HEAD_CSS__
/* ---- practice exam ---- */
.rule { text-align: center; color: var(--muted); max-width: 34em; margin: 0 auto 1.6rem; }
.rule b { color: var(--ink); font-weight: normal; }
.tabs { display: flex; gap: .6rem; justify-content: center; margin-bottom: 1.8rem; }
.controls { display: flex; flex-wrap: wrap; gap: .6rem; justify-content: center;
  align-items: center; margin: 0 0 1.6rem; }
.progress { color: var(--muted); }
.qblock { border: 1px solid var(--rule); border-radius: 12px; background: var(--panel);
  padding: 1.2rem 1.3rem; margin-bottom: 1.2rem; }
.qhead { color: var(--muted); margin-bottom: .3rem; }
.qtext { font-size: 1.08rem; margin: .4rem 0 .8rem; }
.choice { display: block; width: 100%; text-align: left; background: none;
  border: 1px solid transparent; border-radius: 8px; padding: .45em .6em;
  cursor: pointer; color: inherit; font: inherit; font-size: .98rem; line-height: 1.5; }
.choice:hover { border-color: var(--rule); }
.choice:focus-visible { outline: 2px solid var(--beam); outline-offset: 1px; }
.choice .l { font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  color: var(--muted); margin-right: .55em; font-size: .85rem; }
.choice.sel { border-color: var(--beam); box-shadow: 0 0 0 1px var(--beam), 0 0 12px -4px var(--glow); }
.choice.ok { border-color: var(--ok); }
.choice.ok .l { color: var(--ok); }
.choice.bad { border-color: var(--bad); }
.choice.bad .l { color: var(--bad); }
.choice.locked { cursor: default; }
.review { border-top: 1px dotted var(--rule); margin-top: .8rem; padding-top: .7rem;
  font-size: .95rem; }
.review .yours { margin-bottom: .3rem; }
.review .right { color: var(--ok); }
.review .wrong { color: var(--bad); }
.review .why { color: var(--ink); }
.review .hint { color: var(--muted); font-style: italic; font-size: .88rem; margin-top: .3rem; }
.banner { text-align: center; border: 1px solid var(--rule); border-radius: 12px;
  padding: 1.3rem 1rem; margin: 0 0 1.8rem; }
.banner .score { font-size: 1.6rem; }
.banner.pass { border-color: var(--ok); box-shadow: 0 0 18px -6px var(--ok); }
.banner.pass .verdict { color: var(--ok); }
.banner.fail { border-color: var(--bad); box-shadow: 0 0 18px -6px var(--bad); }
.banner.fail .verdict { color: var(--bad); }
.verdict { font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  text-transform: uppercase; letter-spacing: .2em; font-size: .75rem; margin-top: .3rem; }
.feedback { border-top: 1px dotted var(--rule); margin-top: .8rem; padding-top: .7rem; }
.feedback .verdict2 { font-size: 1.02rem; margin-bottom: .3rem; }
.feedback.ok .verdict2 { color: var(--ok); }
.feedback.bad .verdict2 { color: var(--bad); }
.tally { color: var(--muted); }
</style>
</head>
<body>
<div class="page">

__SERIES_BAR__
<header>
  <p class="over label">Practice exam</p>
  <h1>Your Next Ham License</h1>
  <p class="sub">The General Course (2023&ndash;2027)</p>
  <p class="tagline">drawn fresh every time &middot; graded with explanations</p>
  <p class="back">
    <a href="../">&larr; Read the book</a> <span class="dot">&middot;</span>
    <a href="flashcards.html">Flashcards</a> <span class="dot">&middot;</span>
    <a href="../your-next-ham-license.pdf">PDF</a> <span class="dot">&middot;</span>
    <a href="../your-next-ham-license.txt">Text</a>
  </p>
</header>

<p class="rule">The real General exam draws <b>35 questions</b> from this pool — one
from each of the <b>35 groups</b> — and you need <b>26 to pass</b>. Draw a valid exam
below, or drill a single subelement with immediate feedback.</p>

<div class="tabs">
  <button class="btn" id="examTab" type="button" aria-pressed="true">Full exam</button>
  <button class="btn" id="drillTab" type="button" aria-pressed="false">Drill one subelement</button>
</div>

<section id="examSection">
  <div class="controls">
    <button class="btn" id="newExamBtn" type="button">New exam</button>
    <span class="progress tnum" id="progress"></span>
    <button class="btn" id="gradeBtn" type="button">Grade exam</button>
  </div>
  <div class="banner" id="banner" style="display:none"></div>
  <div id="examList"></div>
  <div class="controls">
    <button class="btn" id="gradeBtn2" type="button">Grade exam</button>
  </div>
</section>

<section id="drillSection" style="display:none">
  <div class="controls">
    <select id="drillSel" aria-label="Subelement to drill"></select>
    <button class="btn" id="drillStartBtn" type="button">Start drill</button>
    <span class="tally tnum" id="drillTally"></span>
  </div>
  <div id="drillCard"></div>
  <div class="controls">
    <button class="btn" id="drillNextBtn" type="button" style="display:none">Next question &rarr;</button>
  </div>
</section>

<section class="note">
  <h2 class="label">About this exam</h2>
  <p>Every question, choice, and answer key is verbatim from the NCVEC 2023&ndash;2027 General pool (public domain; valid for exams 2023-07-01 through 2027-06-30), drawn one per group exactly as the real exam does. The explanations are this book&rsquo;s own. Figure G7-1 is redrawn from the pool original.</p>
  <p><a href="../">Read the book</a> &middot; <a href="flashcards.html">Study the flashcards</a></p>
</section>

</div>

<script>
(function () {
  "use strict";
  var RECORDS = __RECORDS_JSON__;
  var SUBELEMENTS = __SUBELEMENTS_JSON__;
  var FIGURES = __FIGURES_JSON__;
  var PASS_SCORE = 26;

  function poolKey(id) {
    var m = /^G(\\d)([A-F])(\\d\\d)$/.exec(id);
    if (!m) return [99, "Z", 99];
    var s = +m[1];
    return [s === 0 ? 10 : s, m[2], +m[3]];
  }
  function cmpId(a, b) {
    var x = poolKey(a), y = poolKey(b);
    return (x[0] - y[0]) || (x[1] < y[1] ? -1 : x[1] > y[1] ? 1 : 0) || (x[2] - y[2]);
  }
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function shuffleInPlace(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  /* ---------- mode tabs ---------- */
  var examTab = document.getElementById("examTab"),
      drillTab = document.getElementById("drillTab"),
      examSection = document.getElementById("examSection"),
      drillSection = document.getElementById("drillSection");
  function setMode(exam) {
    examSection.style.display = exam ? "" : "none";
    drillSection.style.display = exam ? "none" : "";
    examTab.setAttribute("aria-pressed", exam ? "true" : "false");
    drillTab.setAttribute("aria-pressed", exam ? "false" : "true");
  }
  examTab.addEventListener("click", function () { setMode(true); });
  drillTab.addEventListener("click", function () { setMode(false); });

  /* ---------- figure + choice helpers ---------- */
  function figureDiv(rec) {
    if (rec.figure && FIGURES[rec.figure]) {
      var f = el("div", "fig");
      f.innerHTML = FIGURES[rec.figure];
      return f;
    }
    return null;
  }
  function choiceBtn(rec, L, onPick) {
    var b = el("button", "choice");
    b.type = "button";
    b.dataset.letter = L;
    b.appendChild(el("span", "l", L + "."));
    b.appendChild(document.createTextNode(rec.choices[L]));
    b.addEventListener("click", function () { onPick(b, L); });
    return b;
  }
  function reviewDiv(rec, yourLetter) {
    var d = el("div", "review");
    var right = yourLetter === rec.answer;
    var yours = el("p", "yours " + (right ? "right" : "wrong"));
    yours.textContent = right
      ? "Your answer: " + yourLetter + " — correct."
      : (yourLetter
          ? "Your answer: " + yourLetter + " — the correct answer is " + rec.answer + "."
          : "Not answered — the correct answer is " + rec.answer + ".");
    d.appendChild(yours);
    d.appendChild(el("p", "why", rec.why));
    d.appendChild(el("p", "hint",
      "Hint: this is " + rec.groupTheme + " — review chapter " + rec.chapter + "."));
    return d;
  }

  /* ---------- full exam ---------- */
  var exam = [], answers = {}, graded = false;
  var progressEl = document.getElementById("progress"),
      banner = document.getElementById("banner"),
      examList = document.getElementById("examList");

  function drawExam() {
    var byGroup = {};
    RECORDS.forEach(function (r) {
      (byGroup[r.group] = byGroup[r.group] || []).push(r);
    });
    var groups = Object.keys(byGroup).sort(function (a, b) {
      return cmpId(byGroup[a][0].id, byGroup[b][0].id);
    });
    exam = groups.map(function (g) {
      var list = byGroup[g];
      return list[Math.floor(Math.random() * list.length)];
    });
    exam.sort(function (a, b) { return cmpId(a.id, b.id); });
    answers = {};
    graded = false;
    renderExam();
  }

  function renderExam() {
    banner.style.display = "none";
    examList.innerHTML = "";
    exam.forEach(function (rec, i) {
      var block = el("div", "qblock");
      block.appendChild(el("div", "qhead label",
        (i + 1) + " · " + rec.id + " · " + rec.group +
        (rec.figure ? " · Figure " + rec.figure : "")));
      var fig = figureDiv(rec);
      if (fig) block.appendChild(fig);
      block.appendChild(el("p", "qtext", rec.question));
      ["A", "B", "C", "D"].forEach(function (L) {
        block.appendChild(choiceBtn(rec, L, function (btn, letter) {
          if (graded) return;
          answers[rec.id] = letter;
          var sibs = block.querySelectorAll(".choice");
          for (var k = 0; k < sibs.length; k++) sibs[k].classList.remove("sel");
          btn.classList.add("sel");
          updateProgress();
        }));
      });
      examList.appendChild(block);
    });
    updateProgress();
  }

  function updateProgress() {
    progressEl.textContent = "Answered " + Object.keys(answers).length + " / " + exam.length;
  }

  function grade() {
    if (!exam.length) return;
    graded = true;
    var score = 0;
    exam.forEach(function (rec) { if (answers[rec.id] === rec.answer) score++; });
    var pass = score >= PASS_SCORE;
    banner.className = "banner " + (pass ? "pass" : "fail");
    banner.innerHTML = "";
    banner.appendChild(el("div", "score tnum", "You scored " + score + " / " + exam.length));
    banner.appendChild(el("div", "verdict",
      (pass ? "Pass" : "Not yet") + " — " + PASS_SCORE + " to pass"));
    banner.style.display = "";

    examList.innerHTML = "";
    exam.forEach(function (rec, i) {
      var block = el("div", "qblock");
      block.appendChild(el("div", "qhead label",
        (i + 1) + " · " + rec.id + " · " + rec.group +
        (rec.figure ? " · Figure " + rec.figure : "")));
      var fig = figureDiv(rec);
      if (fig) block.appendChild(fig);
      block.appendChild(el("p", "qtext", rec.question));
      var mine = answers[rec.id];
      ["A", "B", "C", "D"].forEach(function (L) {
        var btn = choiceBtn(rec, L, function () {});
        btn.classList.add("locked");
        if (L === rec.answer) btn.classList.add("ok");
        else if (L === mine) btn.classList.add("bad");
        block.appendChild(btn);
      });
      block.appendChild(reviewDiv(rec, mine));
      examList.appendChild(block);
    });
    banner.scrollIntoView({ block: "start" });
  }

  document.getElementById("newExamBtn").addEventListener("click", drawExam);
  document.getElementById("gradeBtn").addEventListener("click", grade);
  document.getElementById("gradeBtn2").addEventListener("click", grade);

  /* ---------- subelement drill ---------- */
  var drillSel = document.getElementById("drillSel"),
      drillTally = document.getElementById("drillTally"),
      drillCard = document.getElementById("drillCard"),
      drillNextBtn = document.getElementById("drillNextBtn");
  var drillQueue = [], drillIdx = 0, drillAnswered = 0, drillCorrect = 0, drillLocked = false;

  SUBELEMENTS.forEach(function (s) {
    var opt = el("option", null, s.id + " — " + s.title + " (" + s.count + " questions)");
    opt.value = s.id;
    drillSel.appendChild(opt);
  });

  function startDrill() {
    drillQueue = shuffleInPlace(RECORDS.filter(function (r) { return r.subelement === drillSel.value; }));
    drillIdx = 0; drillAnswered = 0; drillCorrect = 0;
    renderDrill();
  }

  function renderDrill() {
    drillLocked = false;
    drillNextBtn.style.display = "none";
    drillCard.innerHTML = "";
    if (!drillQueue.length) { drillTally.textContent = ""; return; }
    var rec = drillQueue[drillIdx];
    var block = el("div", "qblock");
    block.appendChild(el("div", "qhead label",
      rec.id + " · " + rec.group + (rec.figure ? " · Figure " + rec.figure : "")));
    var fig = figureDiv(rec);
    if (fig) block.appendChild(fig);
    block.appendChild(el("p", "qtext", rec.question));
    var feedback = el("div", "feedback");
    feedback.style.display = "none";
    feedback.setAttribute("role", "status");
    ["A", "B", "C", "D"].forEach(function (L) {
      block.appendChild(choiceBtn(rec, L, function (btn, letter) {
        if (drillLocked) return;
        drillLocked = true;
        drillAnswered++;
        var right = letter === rec.answer;
        if (right) drillCorrect++;
        var sibs = block.querySelectorAll(".choice");
        for (var k = 0; k < sibs.length; k++) {
          sibs[k].classList.add("locked");
          if (sibs[k].dataset.letter === rec.answer) sibs[k].classList.add("ok");
        }
        if (!right) btn.classList.add("bad");
        feedback.className = "feedback " + (right ? "ok" : "bad");
        feedback.appendChild(el("p", "verdict2",
          right ? "Correct." : "Not quite — the answer is " + rec.answer + "."));
        feedback.appendChild(el("p", null, rec.why));
        feedback.appendChild(el("p", "hint",
          "Hint: this is " + rec.groupTheme + " — review chapter " + rec.chapter + "."));
        feedback.style.display = "";
        drillNextBtn.style.display = "";
        drillTally.textContent = drillCorrect + " / " + drillAnswered + " correct";
      }));
    });
    block.appendChild(feedback);
    drillCard.appendChild(block);
    drillTally.textContent = drillCorrect + " / " + drillAnswered + " correct" +
      " · question " + (drillIdx + 1) + " of " + drillQueue.length;
  }

  document.getElementById("drillStartBtn").addEventListener("click", startDrill);
  drillSel.addEventListener("change", startDrill);
  drillNextBtn.addEventListener("click", function () {
    drillIdx++;
    if (drillIdx >= drillQueue.length) {
      shuffleInPlace(drillQueue);
      drillIdx = 0;
    }
    renderDrill();
  });

  /* ---------- init ---------- */
  drawExam();
  startDrill();
})();
</script>
</body>
</html>
"""


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate the self-contained practice-exam and flashcards pages.")
    parser.add_argument("--out", default="build",
                        help="output directory (default: build/)")
    parser.add_argument("--pool", default=DEFAULT_POOL_PATH,
                        help=f"pool JSON path (default: {DEFAULT_POOL_PATH})")
    parser.add_argument("--appendix", default=DEFAULT_APPENDIX_PATH,
                        help=f"pool appendix markdown path (default: {DEFAULT_APPENDIX_PATH})")
    parser.add_argument("--pool-txt", default=DEFAULT_POOL_TXT_PATH,
                        help=f"canonical pool text path (default: {DEFAULT_POOL_TXT_PATH})")
    parser.add_argument("--figures-dir", default=DEFAULT_FIGURES_DIR,
                        help=f"figures directory (default: {DEFAULT_FIGURES_DIR})")
    parser.add_argument("--expect", type=int, default=POOL_QUESTION_COUNT,
                        help=f"expected question count (default: {POOL_QUESTION_COUNT})")
    parser.add_argument("--figure-ids", default=",".join(sorted(FIGURE_QUESTION_IDS)),
                        help="comma-separated ids allowed to reference a figure")
    args = parser.parse_args(argv)

    try:
        pool = load_pool(args.pool)
        whys = parse_whys(Path(args.appendix).read_text(encoding="utf-8"))
        pool_txt = Path(args.pool_txt).read_text(encoding="utf-8")
        headings = parse_group_headings(pool_txt)
        titles = parse_subelement_titles(pool_txt)
        records = build_records(pool, whys, headings)
        figure_ids = {q.strip() for q in args.figure_ids.split(",") if q.strip()}
        validate_records(records, expected_count=args.expect, figure_ids=figure_ids)
        figures = load_figures(args.figures_dir)
        missing = {r["figure"] for r in records if r.get("figure")} - set(figures)
        if missing:
            raise ValueError(f"no redrawn SVG for figure(s): {sorted(missing)}")
        subelements = subelement_summaries(records, titles)
        practice = render_practice_html(records, figures, subelements)
        flashcards = render_flashcards_html(records, figures, subelements)
    except (ValueError, OSError, KeyError) as exc:
        print(f"make_study: {exc}")
        return 1

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    practice_path = out_dir / "practice.html"
    flashcards_path = out_dir / "flashcards.html"
    practice_path.write_text(practice, encoding="utf-8")
    flashcards_path.write_text(flashcards, encoding="utf-8")
    print(f"assembled {len(records)} study records")
    print(f"wrote {practice_path}")
    print(f"wrote {flashcards_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
