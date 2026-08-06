import pathlib

import pytest

from tools.make_audiobook import (
    dest_name, parse_chapters, parse_sections, prepare, prepare_text,
    spoken_heading,
)

def test_spoken_heading_numbered_chapter():
    assert spoken_heading("4. Antennas & Feedlines") == \
        "Chapter Four. Antennas & Feedlines."

def test_spoken_heading_chapter_zero():
    assert spoken_heading("0. Welcome: What Ham Radio Is & How Licensing Works") == \
        "Chapter Zero. Welcome: What Ham Radio Is & How Licensing Works."

def test_spoken_heading_preface():
    # "Preface — Why & How ..." speaks the em dash as a colon and & as "and"
    assert spoken_heading("Preface — Why & How This Book Was Made") == \
        "Preface: Why and How This Book Was Made."

def test_spoken_heading_passthrough():
    assert spoken_heading("Something unexpected") == "Something unexpected"

def test_parse_chapters_defaults_to_eleven():
    assert parse_chapters("") == list(range(11))
    assert parse_chapters("0-12") == list(range(11))  # clamped to 0..10

def test_audiobook_never_narrates_preface():
    # chapter sources are synthesized as ch{n:02d}.md for n in 0..10, so the
    # ch*.md glob can never pick up chapters/preface.md by accident — the
    # preface is narrated only via the explicit "preface" section
    sources = [f"ch{n:02d}.md" for n in parse_chapters("")]
    assert not any("preface" in s for s in sources)
    names = [p.name for p in pathlib.Path("chapters").glob("ch*.md")]
    assert "preface.md" not in names

def test_dest_name_preface():
    assert dest_name("ryan", "preface") == "preface.mp3"
    assert dest_name("sonia", "preface") == "sonia-preface.mp3"
    assert dest_name("emily", "preface") == "emily-preface.mp3"
    # chapter naming is unchanged
    assert dest_name("ryan", 3) == "ch03.mp3"
    assert dest_name("ava", 3) == "ava-ch03.mp3"

def test_parse_sections_default_covers_chapters_and_preface():
    assert parse_sections("") == ["chapters", "preface"]
    assert parse_sections("preface") == ["preface"]
    assert parse_sections("chapters") == ["chapters"]
    assert parse_sections("preface,chapters") == ["preface", "chapters"]

def test_parse_sections_rejects_unknown():
    with pytest.raises(ValueError):
        parse_sections("glossary")

def test_prepare_preface_fixture():
    title, text = prepare(pathlib.Path("tests/fixtures/preface.md"), None)
    assert title == "Preface: Why and How This Book Was Made."
    assert text.startswith(title + "\n\n")
    # subheadings drop to plain spoken lines, no markup survives
    assert "###" not in text
    assert "Why This Book Exists" in text
    assert "A short opener paragraph" in text
    # the book-title preamble is ch00's alone, not the preface's
    assert "Your Next Ham License. The General Course" not in text

def test_prepare_text_speaks_math_and_drops_fig_markup():
    out = prepare_text("The tank obeys $E = IR$ here.\n\n{{fig:x}}\n", {"x": ("1", "a tank")})
    assert "E equals I R" in out
    assert "{{fig" not in out
    assert "Figure 1" in out
