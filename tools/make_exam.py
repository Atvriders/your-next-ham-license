"""Practice-exam generator for Your Next Ham License.

Draws a valid General class practice exam from the structured question
pool (``canon/pool-general.json``): exactly one question per NCVEC group
(35 groups -> 35 questions on the real pool), uniform random within each
group, reproducible with ``--seed``. Emits a printable exam sheet (questions
and choices A–D only — never the answers) and a separate answer key with a
subelement tally.

Usage:
  python3 tools/make_exam.py [--seed N] [--out build/] [--pool canon/pool-general.json]

Pool JSON format: ``{id: {group, subelement, question, choices: {A..D},
answer, figure}}`` — ids like ``G1A01`` … ``G0E##``.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# Allow running this file directly (`python3 tools/make_exam.py`), where
# Python puts this script's own directory (tools/) on sys.path rather than
# the repo root. Harmless no-op when imported as `tools.make_exam`.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

DEFAULT_POOL_PATH = "canon/pool-general.json"

_POOL_ID_RE = re.compile(r"^G(\d)([A-F])(\d\d)$")


@dataclass
class Question:
    id: str
    group: str
    subelement: str
    question: str
    choices: dict
    answer: str
    figure: str | None = None


def load_pool(json_path) -> dict:
    """Load the structured question pool: ``{id: {group, subelement,
    question, choices{A..D}, answer, figure}}``."""
    return json.loads(Path(json_path).read_text(encoding="utf-8"))


def pool_sort_key(qid: str) -> tuple:
    """Canonical pool order: subelements G1–G9 then G0, group A–F, number."""
    m = _POOL_ID_RE.match(qid)
    if not m:
        return (99, "Z", 99, qid)
    sub, group, num = m.group(1), m.group(2), int(m.group(3))
    sub_order = 10 if sub == "0" else int(sub)
    return (sub_order, group, num)


def draw_exam(pool: dict, seed=None) -> list[Question]:
    """Draw exactly one question per group, uniform random within group.

    ``seed`` makes the draw reproducible. The returned list is in canonical
    pool order.
    """
    rng = random.Random(seed)
    by_group: dict[str, list[str]] = {}
    for qid, entry in pool.items():
        by_group.setdefault(str(entry["group"]), []).append(qid)

    drawn = []
    for group in sorted(by_group, key=lambda g: pool_sort_key(sorted(by_group[g])[0])):
        qid = rng.choice(sorted(by_group[group]))
        entry = pool[qid]
        drawn.append(Question(
            id=qid,
            group=str(entry["group"]),
            subelement=str(entry.get("subelement", "")),
            question=str(entry["question"]),
            choices=dict(entry["choices"]),
            answer=str(entry["answer"]),
            figure=entry.get("figure"),
        ))
    drawn.sort(key=lambda q: pool_sort_key(q.id))
    return drawn


def render_exam(questions: list[Question]) -> str:
    """Render the printable exam sheet: questions + choices A–D, NO answers."""
    lines = [
        "# General Class Practice Exam",
        "",
        f"{len(questions)} questions — one per pool group. "
        "Circle the best choice for each.",
        "",
    ]
    for i, q in enumerate(questions, start=1):
        lines.append(f"{i}. ({q.id}) {q.question}")
        for letter in ("A", "B", "C", "D"):
            lines.append(f"   {letter}. {q.choices[letter]}")
        lines.append("")
    return "\n".join(lines)


def render_key(questions: list[Question]) -> str:
    """Render the answer key: one letter per question + a subelement tally."""
    lines = ["# Practice Exam Answer Key", ""]
    for i, q in enumerate(questions, start=1):
        lines.append(f"{i}. {q.answer}")
    lines.append("")
    lines.append("## Subelement tally")
    tally: dict[str, int] = {}
    for q in questions:
        tally[q.subelement] = tally.get(q.subelement, 0) + 1
    for sub in sorted(tally, key=lambda s: (10 if s == "G0" else int(s[1:]) if s[1:].isdigit() else 99, s)):
        lines.append(f"{sub}: {tally[sub]}")
    lines.append("")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Draw a General class practice exam from the question pool.")
    parser.add_argument("--seed", type=int, default=None,
                        help="random seed for a reproducible draw")
    parser.add_argument("--out", default="build",
                        help="output directory (default: build/)")
    parser.add_argument("--pool", default=DEFAULT_POOL_PATH,
                        help=f"pool JSON path (default: {DEFAULT_POOL_PATH})")
    args = parser.parse_args(argv)

    pool_path = Path(args.pool)
    if not pool_path.exists():
        print(f"pool not found: {pool_path} (ingest the pool first — plan task 2.1)")
        return 1

    pool = load_pool(pool_path)
    questions = draw_exam(pool, seed=args.seed)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    exam_path = out_dir / "practice-exam.md"
    key_path = out_dir / "practice-exam-key.md"
    exam_path.write_text(render_exam(questions), encoding="utf-8")
    key_path.write_text(render_key(questions), encoding="utf-8")

    groups = len({q.group for q in questions})
    print(f"drew {len(questions)} questions ({groups} groups)"
          + (f", seed {args.seed}" if args.seed is not None else ""))
    print(f"wrote {exam_path}")
    print(f"wrote {key_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
