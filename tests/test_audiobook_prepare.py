from tools.make_audiobook import spoken_heading, prepare_text, parse_chapters

def test_spoken_heading_numbered_chapter():
    assert spoken_heading("4. Antennas & Feedlines") == \
        "Chapter Four. Antennas & Feedlines."

def test_spoken_heading_chapter_zero():
    assert spoken_heading("0. Welcome: What Ham Radio Is & How Licensing Works") == \
        "Chapter Zero. Welcome: What Ham Radio Is & How Licensing Works."

def test_spoken_heading_passthrough():
    assert spoken_heading("Something unexpected") == "Something unexpected"

def test_parse_chapters_defaults_to_eleven():
    assert parse_chapters("") == list(range(11))
    assert parse_chapters("0-12") == list(range(11))  # clamped to 0..10

def test_prepare_text_speaks_math_and_drops_fig_markup():
    out = prepare_text("The tank obeys $E = IR$ here.\n\n{{fig:x}}\n", {"x": ("1", "a tank")})
    assert "E equals I R" in out
    assert "{{fig" not in out
    assert "Figure 1" in out
