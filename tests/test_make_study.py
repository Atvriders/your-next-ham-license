import json
import pathlib
import re

import pytest

from tools import make_study

FIX = pathlib.Path("tests/fixtures")
FIXTURE_IDS = {"G1A01", "G1A02", "G1B01", "G2A01", "G5A01", "G7A09"}

REAL_POOL = pathlib.Path("canon/pool-general.json")
REAL_APPENDIX = pathlib.Path("appendices/pool.md")
REAL_POOL_TXT = pathlib.Path("canon/pool-general.txt")
REAL_FIGURES = pathlib.Path("figures")


def load_fixture_inputs():
    pool = make_study.load_pool(FIX / "study_pool.json")
    whys = make_study.parse_whys((FIX / "study_appendix.md").read_text(encoding="utf-8"))
    pool_txt = (FIX / "study_pool.txt").read_text(encoding="utf-8")
    return pool, whys, pool_txt


def build_fixture_records():
    pool, whys, pool_txt = load_fixture_inputs()
    return make_study.build_records(pool, whys, make_study.parse_group_headings(pool_txt))


def fixture_figures():
    return {"G7-1": '<svg viewBox="0 0 10 10"><title>fixture figure G7-1</title></svg>'}


def assert_self_contained(html):
    """The pages must work under a strict CSP: nothing external, ever."""
    assert 'src="http' not in html and "src='http" not in html
    assert 'href="http' not in html and "href='http" not in html
    assert "<script src" not in html
    assert "<link" not in html
    assert "<img" not in html


def assert_fully_rendered(html):
    """No template tokens survive; the audiobook theme is in place."""
    assert not re.findall(r"__[A-Z_]+__", html)
    assert "--paper:" in html and "--beam:" in html  # lantern/scope CSS variables
    assert 'class="series-bar"' in html


# ---------- parsers ----------


def test_parse_group_headings_reads_only_heading_lines():
    _, _, pool_txt = load_fixture_inputs()
    headings = make_study.parse_group_headings(pool_txt)
    assert headings == {
        "G1A": "General class control operator frequency privileges; primary and secondary allocations",
        "G1B": "Antenna structure limitations; Beacon operations; Prohibited transmissions",
        "G2A": "Phone operating procedures; USB/LSB conventions",
        "G5A": "Reactance, inductance, capacitance, impedance, resonance",
        "G7A": "Power supplies and schematic symbols",
    }


def test_parse_subelement_titles():
    _, _, pool_txt = load_fixture_inputs()
    titles = make_study.parse_subelement_titles(pool_txt)
    assert titles == {
        "G1": "COMMISSION'S RULES",
        "G2": "OPERATING PROCEDURES",
        "G5": "ELECTRICAL PRINCIPLES",
        "G7": "PRACTICAL CIRCUITS",  # fixture pins the published lowercase "groups" quirk
    }


def test_parse_whys_maps_letter_and_text_for_every_entry():
    _, whys, _ = load_fixture_inputs()
    assert set(whys) == FIXTURE_IDS
    letter, why = whys["G5A01"]
    assert letter == "A"
    assert why == "impedance is the total opposition to AC — taught in chapter 5."


# ---------- chapter map (accuracy-canon.md §5) ----------


@pytest.mark.parametrize(
    "subelement,group,chapter",
    [
        ("G1", "G1E", 1),
        ("G2", "G2C", 2),
        ("G3", "G3A", 3),
        ("G4", "G4E", 4),
        ("G5", "G5C", 5),
        ("G6", "G6B", 6),
        ("G7", "G7A", 7),
        ("G8", "G8C", 8),
        ("G9", "G9D", 9),
        ("G0", "G0B", 10),
    ],
)
def test_chapter_for_matches_canon_map(subelement, group, chapter):
    assert make_study.chapter_for(subelement, group) == chapter


# ---------- record assembly ----------


def test_build_records_assembles_every_field():
    records = build_fixture_records()
    assert [r["id"] for r in records] == ["G1A01", "G1A02", "G1B01", "G2A01", "G5A01", "G7A09"]
    rec = records[0]
    assert rec["group"] == "G1A"
    assert rec["subelement"] == "G1"
    assert rec["question"].startswith("On which HF")
    assert set(rec["choices"]) == {"A", "B", "C", "D"}
    assert rec["answer"] == "C"
    assert rec["why"] == "the lower edges of 80, 40, 20, and 15 meters are Extra-only — taught in chapter 1."
    assert rec["groupTheme"].startswith("General class control operator")
    assert rec["chapter"] == 1
    assert "figure" not in rec  # figure key only present on figure questions


def test_build_records_marks_only_the_figure_question():
    records = build_fixture_records()
    with_fig = {r["id"]: r["figure"] for r in records if "figure" in r}
    assert with_fig == {"G7A09": "G7-1"}


def test_build_records_fails_on_missing_why():
    pool, whys, pool_txt = load_fixture_inputs()
    del whys["G2A01"]
    with pytest.raises(ValueError, match="G2A01"):
        make_study.build_records(pool, whys, make_study.parse_group_headings(pool_txt))


def test_build_records_fails_on_answer_letter_mismatch():
    pool, whys, pool_txt = load_fixture_inputs()
    whys["G5A01"] = ("C", whys["G5A01"][1])
    with pytest.raises(ValueError, match="G5A01"):
        make_study.build_records(pool, whys, make_study.parse_group_headings(pool_txt))


def test_build_records_fails_on_missing_group_heading():
    pool, whys, pool_txt = load_fixture_inputs()
    headings = make_study.parse_group_headings(pool_txt)
    del headings["G7A"]
    with pytest.raises(ValueError, match="G7A"):
        make_study.build_records(pool, whys, headings)


# ---------- validation ----------


def test_validate_records_accepts_the_fixture_set():
    records = build_fixture_records()
    make_study.validate_records(records, expected_count=6, figure_ids={"G7A09"})


def test_validate_records_rejects_an_unexpected_figure_reference():
    records = build_fixture_records()
    records[0]["figure"] = "G7-1"  # G1A01 is not one of the known figure questions
    with pytest.raises(ValueError, match="G1A01"):
        make_study.validate_records(records, expected_count=6, figure_ids={"G7A09"})


def test_validate_records_rejects_empty_fields():
    records = build_fixture_records()
    records[1]["why"] = ""
    with pytest.raises(ValueError, match="G1A02"):
        make_study.validate_records(records, expected_count=6, figure_ids={"G7A09"})


def test_validate_records_checks_the_count():
    records = build_fixture_records()
    with pytest.raises(ValueError):
        make_study.validate_records(records[:-1], expected_count=6, figure_ids={"G7A09"})


# ---------- the real canon data ----------


def build_real_records():
    pool = make_study.load_pool(REAL_POOL)
    whys = make_study.parse_whys(REAL_APPENDIX.read_text(encoding="utf-8"))
    headings = make_study.parse_group_headings(REAL_POOL_TXT.read_text(encoding="utf-8"))
    return make_study.build_records(pool, whys, headings)


def test_real_pool_assembles_423_valid_records():
    records = build_real_records()
    assert len(records) == 423
    make_study.validate_records(records)  # defaults: 423 records, the 5 known figure ids


def test_real_pool_discovers_all_35_groups_despite_deleted_id_gaps():
    # Nine errata-deleted IDs leave numbering gaps (G1A04, G1C08–G1C10, G1E09,
    # G6B09, G9C06 internal; G8C01 a leading gap; G9D13 a truncated tail).
    # Group discovery is by group key, so the exam draw still sees 35 groups.
    records = build_real_records()
    groups = {r["group"] for r in records}
    assert len(groups) == 35
    assert {"G1A", "G1C", "G1E", "G6B", "G8C", "G9C", "G9D"} <= groups


def test_real_pool_subelement_summaries_cover_g1_through_g0():
    records = build_real_records()
    titles = make_study.parse_subelement_titles(REAL_POOL_TXT.read_text(encoding="utf-8"))
    subs = make_study.subelement_summaries(records, titles)
    assert [s["id"] for s in subs] == ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G0"]
    assert sum(s["count"] for s in subs) == 423
    assert all(s["title"] for s in subs)
    assert subs[0]["count"] == 52  # G1 — Commission's Rules
    assert subs[-1]["count"] == 25  # G0 — Electrical and RF Safety


def test_load_figures_reads_the_redrawn_pool_svg():
    figures = make_study.load_figures(REAL_FIGURES)
    assert set(figures) == {"G7-1"}
    for svg in figures.values():
        assert svg.lstrip().startswith("<svg")


# ---------- page rendering ----------


def test_flashcards_page_embeds_every_record_with_hints_and_marks():
    records = build_fixture_records()
    titles = make_study.parse_subelement_titles((FIX / "study_pool.txt").read_text(encoding="utf-8"))
    html = make_study.render_flashcards_html(
        records, fixture_figures(), make_study.subelement_summaries(records, titles))
    for qid in FIXTURE_IDS:
        assert qid in html
    assert "ynhl-study" in html            # localStorage namespace for review-later marks
    assert "Hint: this is" in html         # hint line template
    assert "review chapter" in html        # chapter pointer in the hint
    assert "fixture figure G7-1" in html   # figure SVG embedded inline
    assert "COMMISSION'S RULES" in html    # subelement labels for the filter
    assert_self_contained(html)
    assert_fully_rendered(html)


def test_flashcards_card_has_fixed_height_and_internal_scroll():
    records = build_fixture_records()
    titles = make_study.parse_subelement_titles((FIX / "study_pool.txt").read_text(encoding="utf-8"))
    html = make_study.render_flashcards_html(
        records, fixture_figures(), make_study.subelement_summaries(records, titles))
    # fixed-height card box: flipping must never move the controls below the card
    assert "height: 28rem" in html
    # the rare longer card scrolls inside the card instead of growing it
    assert "overflow-y: auto" in html


def test_practice_page_states_the_35_26_rule_and_drill_mode():
    records = build_fixture_records()
    titles = make_study.parse_subelement_titles((FIX / "study_pool.txt").read_text(encoding="utf-8"))
    html = make_study.render_practice_html(
        records, fixture_figures(), make_study.subelement_summaries(records, titles))
    assert "35 questions" in html
    assert "26 to pass" in html
    assert "New exam" in html
    assert "Drill" in html                 # per-subelement drill mode
    for qid in FIXTURE_IDS:
        assert qid in html                 # pool embedded as JSON
    assert_self_contained(html)
    assert_fully_rendered(html)


def test_flashcards_page_contains_every_real_pool_id():
    records = build_real_records()
    titles = make_study.parse_subelement_titles(REAL_POOL_TXT.read_text(encoding="utf-8"))
    html = make_study.render_flashcards_html(
        records, make_study.load_figures(REAL_FIGURES),
        make_study.subelement_summaries(records, titles))
    assert len(re.findall(r'"id": "G\d[A-F]\d\d"', html)) == 423
    for qid in ("G1A01", "G5C14", "G0B13", "G7A09", "G7A13"):
        assert qid in html
    assert_self_contained(html)


# ---------- CLI ----------


def test_main_writes_both_pages(tmp_path):
    rc = make_study.main([
        "--pool", str(FIX / "study_pool.json"),
        "--appendix", str(FIX / "study_appendix.md"),
        "--pool-txt", str(FIX / "study_pool.txt"),
        "--figures-dir", str(REAL_FIGURES),
        "--out", str(tmp_path),
        "--expect", "6", "--figure-ids", "G7A09",
    ])
    assert rc == 0
    flash = (tmp_path / "flashcards.html").read_text(encoding="utf-8")
    practice = (tmp_path / "practice.html").read_text(encoding="utf-8")
    for qid in FIXTURE_IDS:
        assert qid in flash and qid in practice
    assert "35 questions" in practice and "26 to pass" in practice
    assert "ynhl-study" in flash
    assert_self_contained(flash)
    assert_self_contained(practice)
    assert_fully_rendered(flash)
    assert_fully_rendered(practice)


def test_main_refuses_an_invalid_record_set(tmp_path):
    # expecting 7 records from a 6-question fixture must fail validation
    rc = make_study.main([
        "--pool", str(FIX / "study_pool.json"),
        "--appendix", str(FIX / "study_appendix.md"),
        "--pool-txt", str(FIX / "study_pool.txt"),
        "--figures-dir", str(REAL_FIGURES),
        "--out", str(tmp_path),
        "--expect", "7", "--figure-ids", "G7A09",
    ])
    assert rc == 1
    assert not (tmp_path / "flashcards.html").exists()
