import json
import pathlib

from tools.make_exam import draw_exam, load_pool, render_exam, render_key

POOL_PATH = pathlib.Path("tests/fixtures/pool_sample.json")
POOL = json.loads(POOL_PATH.read_text(encoding="utf-8"))
GROUPS = {"G1A", "G1B", "G2A", "G5B"}  # 4 groups x 3 questions in the fixture


def test_load_pool_returns_all_entries():
    pool = load_pool(POOL_PATH)
    assert len(pool) == 12
    entry = pool["G5B02"]
    assert entry["group"] == "G5B"
    assert entry["subelement"] == "G5"
    assert set(entry["choices"]) == {"A", "B", "C", "D"}
    assert entry["answer"] in "ABCD"


def test_draw_exam_picks_exactly_one_question_per_group():
    exam = draw_exam(load_pool(POOL_PATH), seed=1)
    assert len(exam) == len(GROUPS)
    assert {q.group for q in exam} == GROUPS


def test_draw_exam_tolerates_deleted_id_gaps():
    # group G1A in the fixture has a deleted-ID gap (01, 03, 05 — no 02/04);
    # every draw from that group must still be a real pool question
    for seed in range(25):
        exam = draw_exam(load_pool(POOL_PATH), seed=seed)
        picked = [q.id for q in exam if q.group == "G1A"]
        assert len(picked) == 1 and picked[0] in {"G1A01", "G1A03", "G1A05"}


def test_draw_exam_is_reproducible_with_seed():
    first = [q.id for q in draw_exam(load_pool(POOL_PATH), seed=42)]
    second = [q.id for q in draw_exam(load_pool(POOL_PATH), seed=42)]
    assert first == second


def test_draw_exam_only_draws_pool_questions_in_order():
    exam = draw_exam(load_pool(POOL_PATH), seed=7)
    ids = [q.id for q in exam]
    assert all(qid in POOL for qid in ids)
    assert ids == sorted(ids)  # canonical pool order (G1 < G2 < G5 here)


def test_render_exam_has_questions_and_choices_but_no_answers():
    exam = draw_exam(load_pool(POOL_PATH), seed=3)
    sheet = render_exam(exam)
    for q in exam:
        assert q.question in sheet
        for text in q.choices.values():
            assert text in sheet
    # nothing on the exam sheet may reveal the key
    lowered = sheet.lower()
    assert "answer" not in lowered
    assert "key" not in lowered
    for i, q in enumerate(exam, start=1):
        assert f"{i}. {q.answer}" not in sheet  # no "1. D"-style key rows


def test_render_key_lists_correct_letters_and_subelement_tally():
    exam = draw_exam(load_pool(POOL_PATH), seed=3)
    key = render_key(exam)
    for i, q in enumerate(exam, start=1):
        assert f"{i}. {q.answer}" in key
    # fixture tally: G1 x2 groups, G2 x1, G5 x1
    assert "G1: 2" in key
    assert "G2: 1" in key
    assert "G5: 1" in key


def test_cli_writes_exam_and_key(tmp_path):
    from tools.make_exam import main
    rc = main(["--seed", "5", "--pool", str(POOL_PATH), "--out", str(tmp_path)])
    assert rc == 0
    exam_md = (tmp_path / "practice-exam.md").read_text(encoding="utf-8")
    key_md = (tmp_path / "practice-exam-key.md").read_text(encoding="utf-8")
    assert "G1" in exam_md and "answer" not in exam_md.lower()
    assert "G1: 2" in key_md
