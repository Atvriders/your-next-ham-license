import pathlib
import re

from tools.build_book import SERIES_BOOKS, build_html, build_txt, compute_chapter_id


def test_build_html_embeds_figure_toc_and_math():
    figreg = {"sample": {"id":"sample","chapter":1,"number":"1.1","caption":"A sample",
              "kind":"original","source":"authored","file":"tests/fixtures/fig_sample.svg"}}
    html = build_html([pathlib.Path("tests/fixtures/ch_sample.md")], figreg)
    assert '<svg' in html                       # figure (and math) inlined
    assert 'Figure 1.1' in html                 # caption numbered
    assert 'id="ch01"' in html                  # chapter anchor
    assert 'href="#ch01"' in html               # TOC link resolves
    assert 'equals' not in html                 # math is SVG glyphs, NOT the spoken word
    assert 'The math, if you want it' in html   # sidebar blockquote
    assert 'Worked example' in html             # worked-example blockquote
    assert 'Exam Focus' in html and 'Key Takeaways' in html
    assert 'Your Next Ham License' in html      # retargeted title
    # self-contained: no external RESOURCE fetches (namespace xmlns http URIs are fine)
    assert 'src="http' not in html
    assert '<link ' not in html.lower()
    assert '@import' not in html


def test_build_html_appendix_is_final_toc_section():
    html = build_html(
        [pathlib.Path("tests/fixtures/ch_sample.md"),
         pathlib.Path("tests/fixtures/appendix_sample.md")],
        {},
    )
    assert 'id="appendix-a"' in html            # appendix anchor
    assert 'href="#appendix-a"' in html         # appendix TOC link resolves
    # appendix renders after the chapter, without a chapter number
    assert html.index('href="#ch01"') < html.index('href="#appendix-a"')
    assert html.index('id="ch01"') < html.index('id="appendix-a"')


def test_compute_chapter_id_numbered_and_appendix_headings():
    assert compute_chapter_id("chapters/ch04.md", "4. Antennas & Feedlines") == "ch04"
    assert compute_chapter_id("appendices/pool.md",
                              "Appendix A: The Complete 2023–2027 Pool") == "appendix-a"
    assert compute_chapter_id("appendices/glossary-and-formulas.md",
                              "Appendix B: Glossary & Formulas") == "appendix-b"


def test_txt_strips_markup_and_math():
    txt = build_txt([pathlib.Path("tests/fixtures/ch_sample.md")])
    assert "*" not in txt and "{{fig" not in txt
    assert "X L equals 2 pi f L" in txt
    assert "[Figure" in txt


def test_h4_group_headings_render_anchored_but_not_in_toc():
    html = build_html([pathlib.Path("tests/fixtures/ch_h4_sample.md")], {})
    # h4 parses to a heading with a stable chapter-scoped anchor, not literal text
    assert '<h4 id="ch02-group-g1a-sample-group-heading-with-topics">' in html
    assert 'Group G1A — Sample group heading; with topics' in html
    assert '<h4 id="ch02-group-g1b-another-group-heading">' in html
    assert '####' not in html
    # TOC stays chapter-level (h3s aren't listed either; h4s must not flood it)
    toc_start = html.index('<nav class="toc"')
    toc = html[toc_start:html.index('</nav>', toc_start)]
    assert toc.count('<li>') == 1
    assert 'Group G1A' not in toc


def test_txt_strips_h4_group_headings():
    txt = build_txt([pathlib.Path("tests/fixtures/ch_h4_sample.md")])
    assert '####' not in txt
    assert 'Group G1A — Sample group heading; with topics' in txt


def test_series_bar_renders_with_current_book_highlighted():
    html = build_html([pathlib.Path("tests/fixtures/ch_sample.md")], {})
    assert 'class="series-bar"' in html           # the bar renders
    # General is this book: highlighted, links to its series mount path
    assert '<a class="current" href="/general/" aria-current="page">General</a>' in html
    # Technician is live: a plain link
    assert '<a href="/tech/">Technician</a>' in html
    # only Extra remains an inert "coming soon" label
    assert html.count("coming soon") == 1
    assert 'href="/extra/"' not in html
    # slim bar at the top, before the title block; TOC anchors still resolve
    assert html.index('class="series-bar"') < html.index('class="title-block"')
    assert 'href="#ch01"' in html


def test_no_absolute_links_beyond_series_paths():
    # sub-path proxying (spec §9) requires every link to be relative/anchor,
    # except the configurable series mount paths in the switcher bar
    html = build_html(
        [pathlib.Path("tests/fixtures/ch_sample.md"),
         pathlib.Path("tests/fixtures/appendix_sample.md")],
        {},
    )
    abs_links = re.findall(r'(?:href|src)="(/[^"]*)"', html)
    allowed = {path for _label, path, _shipped in SERIES_BOOKS}
    assert abs_links, "expected at least the current book's series path"
    assert set(abs_links) <= allowed


def test_html_renders_pipe_table_as_real_table():
    html = build_html([pathlib.Path("tests/fixtures/ch_table_sample.md")], {})
    assert '<table class="md-table">' in html          # real table, not a paragraph
    assert '<th>Term</th>' in html and '<th>Meaning</th>' in html
    assert html.count('<tr>') == 4                     # 1 header + 3 body rows
    assert '<td>SWR</td>' in html
    assert 'Standing-wave ratio' in html
    assert '<td><span class="math">' in html           # $X_L$ in a cell renders as SVG math
    assert 'R &lt; X' in html                          # cell text is HTML-escaped
    assert ':-----' not in html                        # separator row is consumed
    assert '<p>|' not in html                          # no run-on pipe paragraph
    assert 'A closing paragraph after the table.' in html  # parsing resumes after


def test_txt_drops_table_separator_but_keeps_rows():
    txt = build_txt([pathlib.Path("tests/fixtures/ch_table_sample.md")])
    assert '<table' not in txt and '<th' not in txt    # no HTML markup in the TXT edition
    assert ':-----' not in txt and ':--------' not in txt  # separator row dropped
    assert '| SWR |' in txt                            # data rows stay raw/greppable
    assert 'Standing-wave ratio' in txt
