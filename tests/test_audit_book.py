import json
import pathlib

import pytest

from tools.audit_book import (
    check_appendix_pool_coverage,
    check_banned_phrases,
    check_figure_integrity,
    check_format_laws,
    check_pool_quotes,
    extract_pool_quotes,
    main,
    pool_sort_key,
)

POOL_PATH = "tests/fixtures/pool_sample.json"
POOL = json.loads(pathlib.Path(POOL_PATH).read_text(encoding="utf-8"))

CH_SAMPLE = pathlib.Path("tests/fixtures/ch_sample.md").read_text(encoding="utf-8")


# --- Book 1 carry-overs ---------------------------------------------------

def test_banned_phrases_flagged():
    errs = check_banned_phrases("…and little did they know it would grow.")
    assert errs and "little did they know" in errs[0]

def test_banned_phrases_clean():
    assert check_banned_phrases("The lamp is lit and the exam begins.") == []

def test_figure_integrity_missing():
    errs = check_figure_integrity(["{{fig:ghost}}"], registry={})
    assert any("ghost" in e for e in errs)

def test_figure_integrity_ok():
    reg = {"tank": {"id":"tank","chapter":1,"number":"1.1","caption":"c","kind":"original","source":"authored","file":"figures/tank.svg"}}
    assert check_figure_integrity(["see {{fig:tank}}"], registry=reg) == []


# --- Format laws (spec §5 skeleton) ----------------------------------------

def test_format_laws_accept_teaching_chapter_fixture():
    assert check_format_laws("ch01", CH_SAMPLE) == []

def test_format_laws_require_exam_focus_in_teaching_chapters():
    text = CH_SAMPLE.replace("### Exam Focus", "### Focus")
    assert any("Exam Focus" in e for e in check_format_laws("ch01", text))

def test_format_laws_forbid_exam_focus_only_in_ch00():
    # only the ch00 welcome is exempt; ch10 owns subelement G0 in this book
    assert any("Exam Focus" in e for e in check_format_laws("ch00", CH_SAMPLE))

def test_format_laws_treat_ch10_as_teaching_chapter():
    text = CH_SAMPLE.replace("## 1.", "## 10.")
    assert check_format_laws("ch10", text) == []
    no_focus = text.replace("### Exam Focus", "### Focus")
    assert any("Exam Focus" in e for e in check_format_laws("ch10", no_focus))
    no_example = text.replace("> **Worked example:**", "> **Example:**")
    assert any("worked example" in e.lower() for e in check_format_laws("ch10", no_example))

def test_format_laws_require_worked_example_in_teaching_chapters():
    text = CH_SAMPLE.replace("> **Worked example:**", "> **Example:**")
    assert any("worked example" in e.lower() for e in check_format_laws("ch01", text))

def test_format_laws_require_key_takeaways():
    text = CH_SAMPLE.replace("### Key Takeaways", "### Takeaways")
    assert any("Key Takeaways" in e for e in check_format_laws("ch01", text))

def test_format_laws_heading_number_must_match_file():
    assert any("heading" in e.lower() for e in check_format_laws("ch03", CH_SAMPLE))

def test_format_laws_require_opener_paragraph():
    text = CH_SAMPLE.replace(
        "Your Technician ticket taught you Ohm's law for DC; on HF the same ideas "
        "stretch into AC, where capacitors and inductors oppose the flow with a "
        "frequency-dependent reactance. In this chapter you'll learn how reactance, "
        "impedance, and resonance fit together, and how little extra math you "
        "actually need.\n\n",
        "",
    )
    assert any("opener" in e.lower() for e in check_format_laws("ch01", text))

def test_format_laws_fact_line_count():
    text = CH_SAMPLE.replace("**FACT:** Impedance combines resistance and reactance as the square root of the sum of their squares.\n", "")
    assert any("FACT" in e for e in check_format_laws("ch01", text))


# --- Check #8: pool fidelity -----------------------------------------------

def _quote(qid, question, letter, choices):
    lines = [f"> **{qid}** {question}"]
    lines += [f"> {k}. {v}" for k, v in choices.items()]
    lines.append(f"> **Answer: {letter}** — because the fixture says so.")
    return "\n".join(lines)


def test_pool_quote_correct_passes():
    entry = POOL["G5B02"]
    text = _quote("G5B02", entry["question"], entry["answer"], entry["choices"])
    assert check_pool_quotes(extract_pool_quotes(text), POOL) == []

def test_pool_quote_one_word_off_fails():
    entry = POOL["G5B02"]
    bad = entry["question"].replace("30 ohms", "35 ohms")
    text = _quote("G5B02", bad, entry["answer"], entry["choices"])
    errs = check_pool_quotes(extract_pool_quotes(text), POOL)
    assert errs and "G5B02" in errs[0]

def test_pool_quote_wrong_answer_letter_fails():
    entry = POOL["G5B02"]
    wrong = "A" if entry["answer"] != "A" else "B"
    text = _quote("G5B02", entry["question"], wrong, entry["choices"])
    errs = check_pool_quotes(extract_pool_quotes(text), POOL)
    assert errs and "answer" in errs[0].lower()

def test_pool_quote_unknown_id_fails():
    text = _quote("G9F01", "Not a real pool question?", "A", POOL["G5B02"]["choices"])
    errs = check_pool_quotes(extract_pool_quotes(text), POOL)
    assert errs and "G9F01" in errs[0]

def _appendix_text(ids):
    return "\n\n".join(
        _quote(qid, POOL[qid]["question"], POOL[qid]["answer"], POOL[qid]["choices"])
        for qid in ids
    )

def test_appendix_coverage_complete_and_in_order_passes():
    # note the deleted-ID gap in group G1A: 01, 03, 05 (no 02 or 04) —
    # coverage must tolerate non-contiguous numbering
    ordered = ["G1A01", "G1A03", "G1A05", "G1B01", "G1B02", "G1B03",
               "G2A01", "G2A02", "G2A03", "G5B01", "G5B02", "G5B03"]
    assert check_appendix_pool_coverage(_appendix_text(ordered), POOL) == []

def test_appendix_coverage_missing_id_fails():
    ids = [qid for qid in POOL if qid != "G2A02"]
    errs = check_appendix_pool_coverage(_appendix_text(ids), POOL)
    assert any("G2A02" in e and "missing" in e for e in errs)

def test_appendix_coverage_duplicate_id_fails():
    ids = sorted(POOL) + ["G2A02"]
    errs = check_appendix_pool_coverage(_appendix_text(ids), POOL)
    assert any("G2A02" in e and "once" in e for e in errs)

def test_appendix_coverage_out_of_order_fails():
    ids = sorted(POOL)
    ids[0], ids[1] = ids[1], ids[0]
    errs = check_appendix_pool_coverage(_appendix_text(ids), POOL)
    assert any("order" in e for e in errs)

def test_pool_sort_key_orders_g0_after_g9():
    assert pool_sort_key("G1A01") < pool_sort_key("G9F12")
    assert pool_sort_key("G9F12") < pool_sort_key("G0A01")
    assert pool_sort_key("G0E10") > pool_sort_key("G0A01")


# --- Check #8 on the empty scaffold: skip, not fail -------------------------

def test_audit_main_skips_pool_check_on_empty_scaffold(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    assert main() == 0
    out = capsys.readouterr().out.lower()
    assert "pool" in out and "skip" in out
