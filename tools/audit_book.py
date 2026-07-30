"""Verification harness ("test suite") for the finished Your Next Ham License book.

Cross-checks the book against the accuracy canon, the 2023–2027 General
question pool, and the design spec's §5 format laws, and exits non-zero if
anything fails. Reuses the existing tooling modules rather than
re-implementing their logic:

    tools.figreg      -- figure registry load/validate
    tools.mathsvg     -- inline math -> SVG rendering
    tools.build_book  -- HTML assembly (TOC/anchor check)

Run as a script:

    python3 tools/audit_book.py

Consumes (all optional at this stage of the project -- the checks that
depend on missing inputs are skipped, not failed):

    chapters/ch*.md            -- chapter markdown files
    appendices/pool.md         -- Appendix A (the verbatim pool)
    figures/figures.json       -- figure registry (via figreg.load())
    accuracy-canon.md          -- the accuracy canon / "bible"
    canon/pool-general.json    -- structured pool: id -> {group, subelement,
                                  question, choices{A..D}, answer, figure}

Runs eight checks:
    1. Figure integrity      (registry refs + files-on-disk + orphans)
    2. Copyright tags        (figreg.validate)
    3. TOC/anchor consistency (build_book.build_html)
    4. Math rendering        (mathsvg.render on every $...$ span)
    5. Canon cross-check     (**FACT:** claims appear verbatim in the canon)
    6. Flagged uncertainties (no UNVERIFIED markers left in the canon)
    7. Format laws           (spec §5 skeleton + banned phrases)
    8. Pool fidelity         (verbatim quotes, answer letters, Appendix A
                              coverage -- SKIPS gracefully when the pool
                              file has not been ingested yet)

Pool-quote convention (what check #8 parses -- chapter writers must follow):
    > **G1A01** <question text, verbatim from the pool>
    > A. <choice text, verbatim>
    > B. <choice text, verbatim>
    > C. <choice text, verbatim>
    > D. <choice text, verbatim>
    > **Answer: A** — one-line why.
The question text is compared byte-exact modulo whitespace normalization;
choice lines and the answer letter are checked only where present.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
from glob import glob

# Allow running this file directly (`python3 tools/audit_book.py`), where
# Python puts this script's own directory (tools/) on sys.path rather than
# the repo root, which would otherwise break the `tools.*` absolute imports
# below. Harmless no-op when already imported as the `tools.audit_book`
# package (e.g. under pytest, where pyproject.toml's pythonpath already
# includes the repo root).
_REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from tools.figreg import load, validate
from tools.mathsvg import render
from tools.build_book import build_html

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

BANNED_PHRASES = ("little did they know", "in that moment", "a testament to")

_FIG_REF_RE = re.compile(r"\{\{fig:([^}]+)\}\}")
_MATH_SPAN_RE = re.compile(r"\$(.+?)\$")
_FACT_RE = re.compile(r"(?m)^\s*\*\*FACT:\*\*\s*(.+?)\s*$")
_HREF_RE = re.compile(r'href="#(ch\d\d|appendix-[a-z])"')
_ID_RE = re.compile(r'id="(ch\d\d|appendix-[a-z])"')
_HEADING_RE = re.compile(r"^##\s+(\d+)\.\s+.+")
_EXAM_FOCUS_RE = re.compile(r"(?m)^### Exam Focus\s*$")
_KEY_TAKEAWAYS_RE = re.compile(r"(?m)^### Key Takeaways\s*$")
_WORKED_EXAMPLE_RE = re.compile(r">\s*\*\*Worked example")
_CHAPTER_STEM_RE = re.compile(r"^ch(0\d|10)$")

CANON_PATH = "accuracy-canon.md"
FIGREG_PATH = "figures/figures.json"
CHAPTERS_GLOB = "chapters/ch*.md"
APPENDIX_POOL_PATH = "appendices/pool.md"
POOL_JSON_PATH = "canon/pool-general.json"

# Chapters exempt from the worked-example / Exam Focus format laws (only the
# ch00 welcome is not a teaching chapter here -- ch10 owns subelement G0 and
# is a full teaching chapter in this book).
_EXEMPT_FROM_TEACHING_LAWS = ("ch00",)

# Check #8: pool-quote markup (see module docstring for the convention).
_POOL_QUOTE_RE = re.compile(r"^\s*>\s*\*\*(G\d[A-F]\d\d)\*\*\s+(.+?)\s*$")
_POOL_ANSWER_RE = re.compile(r"\*\*Answer:\s*([A-D])\*\*")
_POOL_CHOICE_RE = re.compile(r"^([A-D])[.)]\s+(.+?)\s*$")
_POOL_ID_RE = re.compile(r"^G(\d)([A-F])(\d\d)$")


# --------------------------------------------------------------------------
# Pure check functions (unit-tested directly)
# --------------------------------------------------------------------------

def check_banned_phrases(text: str) -> list[str]:
    """Flag any banned "moralizing"/cliche phrase in ``text`` (case-insensitive).

    Returns one error string per hit (containing the offending phrase).
    Empty list if the text is clean.
    """
    errors = []
    lowered = text.lower()
    for phrase in BANNED_PHRASES:
        if phrase in lowered:
            errors.append(f"banned phrase found: '{phrase}'")
    return errors


def check_figure_integrity(chapter_texts: list[str], registry: dict) -> list[str]:
    """Check that every ``{{fig:ID}}`` reference across ``chapter_texts`` is
    registered in ``registry``.

    Does NOT check that the registered file exists on disk -- that's a
    separate, filesystem-touching check performed in main().
    """
    errors = []
    for text in chapter_texts:
        for m in _FIG_REF_RE.finditer(text):
            fig_id = m.group(1)
            if fig_id not in registry:
                errors.append(f"figure ref '{fig_id}' is not registered in figures.json")
    return errors


def check_format_laws(stem: str, text: str) -> list[str]:
    """Check one chapter (file stem ``chNN``, raw markdown ``text``) against
    the spec §5 skeleton:

      - first line is a ``## <N>. <Title>`` heading whose number matches the
        file stem;
      - an opener paragraph follows the heading (plain text, not a subhead,
        blockquote, figure ref, or rule);
      - teaching chapters ch01–ch10 carry ≥1 ``> **Worked example:**``
        blockquote and a ``### Exam Focus`` section; ch00 must NOT have
        an Exam Focus section;
      - every chapter carries a ``### Key Takeaways`` section and 3–5
        ``**FACT:**`` lines.

    Banned phrases are a separate check (check_banned_phrases).
    """
    errors = []
    lines = text.splitlines()

    m = _HEADING_RE.match(lines[0]) if lines else None
    if not m:
        errors.append(f"{stem}: first line is not a '## <N>. <Title>' heading")
    elif int(m.group(1)) != int(stem[2:]):
        errors.append(
            f"{stem}: heading number {int(m.group(1))} does not match the file stem"
        )

    idx = 1
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    if idx >= len(lines) or re.match(r"^\s*(#|>|\{\{|\*\*\*|-|\*)", lines[idx]):
        errors.append(f"{stem}: no opener paragraph after the heading")

    if stem in _EXEMPT_FROM_TEACHING_LAWS:
        if _EXAM_FOCUS_RE.search(text):
            errors.append(f"{stem}: '### Exam Focus' must not appear in {stem}")
    else:
        if not _WORKED_EXAMPLE_RE.search(text):
            errors.append(f"{stem}: no worked-example blockquote ('> **Worked example')")
        if not _EXAM_FOCUS_RE.search(text):
            errors.append(f"{stem}: missing '### Exam Focus' section")

    if not _KEY_TAKEAWAYS_RE.search(text):
        errors.append(f"{stem}: missing '### Key Takeaways' section")

    fact_count = len(_FACT_RE.findall(text))
    if not (3 <= fact_count <= 5):
        errors.append(f"{stem}: {fact_count} '**FACT:**' line(s) (must be 3–5)")

    return errors


# --------------------------------------------------------------------------
# Check #8: pool fidelity (pure functions, unit-tested directly)
# --------------------------------------------------------------------------

def _norm_ws(s: str) -> str:
    """Whitespace-normalize for byte-exact-modulo-whitespace comparison."""
    return " ".join(s.split())


def extract_pool_quotes(text: str) -> list[dict]:
    """Extract pool-question quote blocks from markdown ``text``.

    Each block starts with a line ``> **G#X##** <question>`` and continues
    through the following consecutive ``>`` lines, within which an
    ``**Answer: X**`` marker and ``A.``–``D.`` choice lines are picked up.
    Returns a list of dicts: {id, question, answer|None, choices{letter: text}}.
    """
    quotes = []
    lines = text.splitlines()
    i = 0
    n = len(lines)
    while i < n:
        m = _POOL_QUOTE_RE.match(lines[i])
        if not m:
            i += 1
            continue
        qid, question = m.group(1), m.group(2)
        answer = None
        choices: dict[str, str] = {}
        j = i + 1
        while j < n and lines[j].lstrip().startswith(">"):
            body = lines[j].lstrip()[1:].strip()
            am = _POOL_ANSWER_RE.search(body)
            if am:
                answer = am.group(1)
            cm = _POOL_CHOICE_RE.match(body)
            if cm:
                choices[cm.group(1)] = cm.group(2)
            j += 1
        quotes.append({"id": qid, "question": question, "answer": answer,
                       "choices": choices})
        i = j
    return quotes


def check_pool_quotes(quotes: list[dict], pool: dict) -> list[str]:
    """Check extracted pool quotes against the structured pool.

    Every quoted question must match the pool text byte-exact (whitespace-
    normalized); every stated choice line must match verbatim; every stated
    answer letter must match the pool key.
    """
    errors = []
    for q in quotes:
        qid = q["id"]
        entry = pool.get(qid)
        if entry is None:
            errors.append(f"pool fidelity: {qid}: not a pool question id")
            continue
        if _norm_ws(q["question"]) != _norm_ws(str(entry.get("question", ""))):
            errors.append(
                f"pool fidelity: {qid}: question text does not match the pool "
                f"verbatim: {q['question']!r}"
            )
        for letter, choice_text in sorted(q["choices"].items()):
            want = entry.get("choices", {}).get(letter)
            if want is None or _norm_ws(choice_text) != _norm_ws(str(want)):
                errors.append(
                    f"pool fidelity: {qid}: choice {letter} does not match the "
                    f"pool verbatim: {choice_text!r}"
                )
        if q["answer"] is not None and q["answer"] != entry.get("answer"):
            errors.append(
                f"pool fidelity: {qid}: stated answer {q['answer']} does not "
                f"match the pool key {entry.get('answer')}"
            )
    return errors


def pool_sort_key(qid: str) -> tuple:
    """Canonical pool order: subelements G1–G9 then G0, group A–F, number."""
    m = _POOL_ID_RE.match(qid)
    if not m:
        return (99, "Z", 99, qid)
    sub, group, num = m.group(1), m.group(2), int(m.group(3))
    sub_order = 10 if sub == "0" else int(sub)
    return (sub_order, group, num)


def check_appendix_pool_coverage(appendix_text: str, pool: dict) -> list[str]:
    """Check that Appendix A (``appendices/pool.md``) quotes every pool id
    exactly once, in canonical pool order.
    """
    errors = []
    ids = [q["id"] for q in extract_pool_quotes(appendix_text)]

    seen: dict[str, int] = {}
    for qid in ids:
        seen[qid] = seen.get(qid, 0) + 1
    for qid in sorted(seen, key=pool_sort_key):
        if seen[qid] > 1:
            errors.append(
                f"pool fidelity: appendix A: {qid} appears {seen[qid]} times "
                f"(must appear exactly once)"
            )
    for qid in sorted(seen, key=pool_sort_key):
        if qid not in pool:
            errors.append(f"pool fidelity: appendix A: {qid} is not a pool question id")

    want = sorted(pool, key=pool_sort_key)
    missing = [qid for qid in want if qid not in seen]
    for qid in missing:
        errors.append(f"pool fidelity: appendix A: missing pool question {qid}")

    if not errors and ids != want:
        errors.append("pool fidelity: appendix A: questions are not in pool order")

    return errors


# --------------------------------------------------------------------------
# main() -- runs the full audit against the real repo
# --------------------------------------------------------------------------

def main() -> int:
    errors = []
    warnings = []

    chapter_paths = sorted(glob(CHAPTERS_GLOB))
    chapter_texts = []
    for p in chapter_paths:
        chapter_texts.append(pathlib.Path(p).read_text(encoding="utf-8"))

    registry = load(FIGREG_PATH)

    canon_path = pathlib.Path(CANON_PATH)
    canon_text = canon_path.read_text(encoding="utf-8") if canon_path.exists() else None

    print("=== Your Next Ham License: book audit ===\n")

    # 1. Figure integrity -------------------------------------------------
    print("[1/8] Figure integrity")
    fig_errors = check_figure_integrity(chapter_texts, registry)
    for e in fig_errors:
        errors.append(f"figure integrity: {e}")

    referenced_ids = set()
    for text in chapter_texts:
        for m in _FIG_REF_RE.finditer(text):
            referenced_ids.add(m.group(1))

    for fig_id, entry in registry.items():
        file_ = entry.get("file")
        if not file_ or not pathlib.Path(file_).exists():
            errors.append(f"figure integrity: '{fig_id}' file does not exist on disk: {file_!r}")

    orphans = sorted(set(registry) - referenced_ids)
    if orphans:
        for fig_id in orphans:
            warnings.append(f"figure integrity: '{fig_id}' is registered but never referenced by any chapter (orphan)")

    if not chapter_texts:
        print("  skipped (no chapters): no {{fig:ID}} refs to check")
    print(f"  {len([e for e in errors if e.startswith('figure integrity')])} error(s), {len(orphans)} orphan warning(s)")

    # 2. Copyright tags -----------------------------------------------------
    print("[2/8] Copyright tags")
    copyright_errors = validate(registry)
    for e in copyright_errors:
        errors.append(f"copyright tag: {e}")
    print(f"  {len(copyright_errors)} error(s)")

    # 3. TOC/anchors ----------------------------------------------------
    print("[3/8] TOC/anchor consistency")
    toc_paths = list(chapter_paths)
    for app in ("appendices/pool.md", "appendices/glossary-and-formulas.md"):
        if pathlib.Path(app).exists():
            toc_paths.append(app)
    if toc_paths:
        try:
            html = build_html(toc_paths, registry)
            hrefs = set(_HREF_RE.findall(html))
            ids = set(_ID_RE.findall(html))
            missing = sorted(hrefs - ids)
            for m in missing:
                errors.append(f"toc/anchor: TOC link '#{m}' has no matching id=\"{m}\"")
            print(f"  {len(missing)} error(s)")
        except Exception as exc:  # noqa: BLE001 -- surface build failures as audit failures
            errors.append(f"toc/anchor: build_html raised: {exc}")
            print(f"  1 error(s) (build_html raised)")
    else:
        print("  skipped (no chapters or appendices)")

    # 4. Math -------------------------------------------------------------
    print("[4/8] Math rendering")
    math_errors = 0
    if chapter_texts:
        for path, text in zip(chapter_paths, chapter_texts):
            for m in _MATH_SPAN_RE.finditer(text):
                expr = m.group(1)
                try:
                    render(expr)
                except Exception as exc:  # noqa: BLE001
                    math_errors += 1
                    errors.append(f"math: {path}: '{expr}' failed to render: {exc}")
        print(f"  {math_errors} error(s)")
    else:
        print("  skipped (no chapters)")

    # 5. Canon cross-check --------------------------------------------------
    print("[5/8] Canon cross-check (**FACT:** claims)")
    if canon_text is None:
        print("  skipped (no canon)")
    elif not chapter_texts:
        print("  skipped (no chapters)")
    else:
        fact_errors = 0
        for path, text in zip(chapter_paths, chapter_texts):
            for m in _FACT_RE.finditer(text):
                claim = m.group(1).strip()
                if claim not in canon_text:
                    fact_errors += 1
                    errors.append(f"canon cross-check: {path}: FACT not found verbatim in canon: {claim!r}")
        print(f"  {fact_errors} error(s)")

    # 6. Flagged uncertainties -----------------------------------------
    print("[6/8] Flagged uncertainties")
    if canon_text is None:
        print("  skipped (no canon)")
    else:
        unverified_count = canon_text.count("UNVERIFIED")
        if unverified_count:
            errors.append(f"flagged uncertainties: {unverified_count} UNVERIFIED marker(s) remain in {CANON_PATH}")
        print(f"  {unverified_count} error(s)")

    # 7. Format laws ------------------------------------------------------
    print("[7/8] Format laws")
    if not chapter_paths:
        print("  skipped (no chapters)")
    else:
        format_errors = 0
        for path, text in zip(chapter_paths, chapter_texts):
            stem = pathlib.Path(path).stem
            if not _CHAPTER_STEM_RE.match(stem):
                continue

            for fe in check_format_laws(stem, text):
                format_errors += 1
                errors.append(f"format law: {path}: {fe}")

            for pe in check_banned_phrases(text):
                format_errors += 1
                errors.append(f"format law: {path}: {pe}")

        print(f"  {format_errors} error(s)")

    # 8. Pool fidelity ------------------------------------------------------
    print("[8/8] Pool fidelity (verbatim quotes, answer keys, Appendix A coverage)")
    pool_path = pathlib.Path(POOL_JSON_PATH)
    if not pool_path.exists():
        print(f"  skipped (no {POOL_JSON_PATH}): pool not ingested yet")
    else:
        pool = json.loads(pool_path.read_text(encoding="utf-8"))
        pool_errors = 0
        scan = list(zip(chapter_paths, chapter_texts))
        app_path = pathlib.Path(APPENDIX_POOL_PATH)
        app_text = None
        if app_path.exists():
            app_text = app_path.read_text(encoding="utf-8")
            scan.append((APPENDIX_POOL_PATH, app_text))

        for path, text in scan:
            for pe in check_pool_quotes(extract_pool_quotes(text), pool):
                pool_errors += 1
                errors.append(f"{path}: {pe}")

        if app_text is None:
            print(f"  appendix coverage skipped (no {APPENDIX_POOL_PATH})")
        else:
            for ce in check_appendix_pool_coverage(app_text, pool):
                pool_errors += 1
                errors.append(f"{APPENDIX_POOL_PATH}: {ce}")
        print(f"  {pool_errors} error(s)")

    # ----------------------------------------------------------------
    print("\n=== Report ===")
    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  WARN: {w}")

    if errors:
        print(f"\n{len(errors)} error(s):")
        for e in errors:
            print(f"  FAIL: {e}")
        print(f"\nAudit FAILED: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1

    print(f"\nAudit PASSED: 0 errors, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
