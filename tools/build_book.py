"""Build the "Your Next Ham License" HTML, TXT, and (best-effort) PDF editions.

Parses the book's chapter markdown files (a small, fixed dialect — see the
module-level regexes below), splices in figures from the figure registry and
inline math rendered as SVG, and produces:

  - build_html(chapter_paths, figreg) -> str
      A single self-contained HTML document. Every figure and math
      expression is embedded as inline ``<svg>``; all CSS is inline. No
      external resource references (no ``<link>``, no ``@import``, no
      ``src="http..."``), so the file works fully offline.

  - build_txt(chapter_paths) -> str
      A plain-text edition: markdown markup stripped, math spoken as
      English words, figures rendered as ``[Figure: ID]`` placeholders.

  - build_pdf(html_path, out_pdf) -> bool
      Best-effort PDF rendering of an already-built HTML file via a
      headless Chromium/Chrome binary, falling back to weasyprint, and
      returning False (non-fatal) if neither is available.

Chapter markdown format (fixed; spec §5 skeleton):
    line 1:  "## <N>. <Title>"               e.g. "## 4. Antennas & Feedlines"
    (blank line(s))
    body:    one plain-language opener paragraph, then "### Section"
             subheads, "{{fig:ID}}" figure refs (own line), "$...$" inline
             math, "***" section rules, "> ..." blockquotes (a blockquote
             starting "**The math, if you want it:**" is a sidebar; one
             starting "**Worked example:**" is a worked example),
             "**bold**" / "*italic*" emphasis, and pipe tables: a block of
             consecutive "| ... |" lines whose second line is a "|---|"-style
             separator renders as a real <table>.

Appendix files (appendices/pool.md, appendices/glossary-and-formulas.md)
use the same dialect but head with "## Appendix A: ..." / "## Appendix B: ..."
and render as the final TOC sections, after ch10, without chapter numbers.
pool.md also uses "#### Group ..." headings, rendered as anchored <h4>s;
like h3s, they never enter the chapter-level TOC.
"""

from __future__ import annotations

import argparse
import html
import pathlib
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass

# Allow running this file directly (`python3 tools/build_book.py`), where
# Python puts this script's own directory (tools/) on sys.path rather than
# the repo root, which would otherwise break the `tools.*` absolute imports
# below. Harmless no-op when already imported as the `tools.build_book`
# package (e.g. under pytest, where pyproject.toml's pythonpath already
# includes the repo root).
_REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from tools.figreg import load, validate
from tools.mathsvg import render
from tools.narration import speak_math, strip_markup

# --------------------------------------------------------------------------
# Series site: book-switcher bar
# --------------------------------------------------------------------------

# (label, mount path, shipped?) for each book of the series. Unshipped books
# render as inert "coming soon" labels; flip the flag when that book ships.
# These paths are the only absolute links allowed in the generated HTML
# (asserted in tests/test_build_book.py).
SERIES_BOOKS = [
    ("Technician", "/tech/", True),
    ("General", "/general/", True),
    ("Extra", "/extra/", False),
]
SERIES_CURRENT = "General"  # this book; retargeted per book in the series

# --------------------------------------------------------------------------
# Chapter parsing
# --------------------------------------------------------------------------

_FIG_LINE_RE = re.compile(r"^\{\{fig:([^}]+)\}\}$")
_FIG_TXT_RE = re.compile(r"\{\{fig:([^}]*)\}\}")
_MATH_SPAN_RE = re.compile(r"\$(.+?)\$")
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
_ITALIC_RE = re.compile(r"\*(.+?)\*")
_CHAPTER_STEM_RE = re.compile(r"^ch\d\d$")
_LEADING_NUMBER_RE = re.compile(r"^(\d+)\.")
_APPENDIX_HEADING_RE = re.compile(r"^Appendix\s+([A-Za-z])\b")
_SLUG_RE = re.compile(r"[^a-z0-9]+")
_TABLE_SEP_CELL_RE = re.compile(r"^:?-+:?$")


@dataclass
class Chapter:
    path: pathlib.Path
    id: str
    heading: str
    blocks: list


def compute_chapter_id(path: pathlib.Path, heading: str) -> str:
    """id = file stem if it matches ch\\d\\d; else ch + 2-digit chapter number
    parsed from a "<N>. <Title>" heading; else appendix-<letter> parsed from
    an "Appendix X: ..." heading.
    """
    stem = pathlib.Path(path).stem
    if _CHAPTER_STEM_RE.match(stem):
        return stem
    h = heading.strip()
    m = _LEADING_NUMBER_RE.match(h)
    if m:
        return f"ch{int(m.group(1)):02d}"
    m = _APPENDIX_HEADING_RE.match(h)
    if m:
        return f"appendix-{m.group(1).lower()}"
    raise ValueError(f"{path}: cannot determine chapter id from heading {heading!r}")


def _parse_body(body_lines: list) -> list:
    blocks = []
    buf = []

    def flush():
        if buf:
            blocks.append(("p", " ".join(buf)))
            buf.clear()

    i = 0
    n = len(body_lines)
    while i < n:
        raw = body_lines[i]
        stripped = raw.strip()

        if stripped == "":
            flush()
            i += 1
            continue

        if stripped.startswith("#### "):
            flush()
            blocks.append(("h4", stripped[5:].strip()))
            i += 1
            continue

        if stripped.startswith("### "):
            flush()
            blocks.append(("h3", stripped[4:].strip()))
            i += 1
            continue

        m = _FIG_LINE_RE.match(stripped)
        if m:
            flush()
            blocks.append(("fig", m.group(1)))
            i += 1
            continue

        if stripped == "***":
            flush()
            blocks.append(("hr", None))
            i += 1
            continue

        if stripped.startswith(">"):
            flush()
            quote_lines = []
            while i < n and body_lines[i].strip().startswith(">"):
                q = body_lines[i].strip()[1:].strip()
                quote_lines.append(q)
                i += 1
            blocks.append(("quote", " ".join(quote_lines)))
            continue

        if stripped.startswith("|"):
            table_lines = []
            while i < n and body_lines[i].strip().startswith("|"):
                table_lines.append(body_lines[i].strip())
                i += 1
            table = _parse_table(table_lines)
            if table is None:  # not a table: keep the old join-into-paragraph behavior
                buf.extend(table_lines)
            else:
                flush()
                blocks.append(("table", table))
            continue

        buf.append(stripped)
        i += 1

    flush()
    return blocks


def _split_table_row(line: str) -> list:
    """Split one ``| a | b |`` line into its stripped cell texts."""
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _is_table_separator(line: str) -> bool:
    """True for a ``|---|``/``:---``-style separator row (every cell only
    dashes with optional alignment colons)."""
    cells = _split_table_row(line)
    return bool(cells) and all(_TABLE_SEP_CELL_RE.match(cell) for cell in cells)


def _parse_table(lines: list):
    """Parse a block of consecutive ``| ... |`` lines into a
    ``(header_cells, body_rows)`` pair, or return None when the second line
    is not a separator row -- then the lines are not a pipe table at all."""
    if len(lines) < 2 or not _is_table_separator(lines[1]):
        return None
    header = _split_table_row(lines[0])
    rows = [_split_table_row(line) for line in lines[2:]]
    return (header, rows)


def parse_chapter(path: pathlib.Path) -> Chapter:
    path = pathlib.Path(path)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or not lines[0].startswith("## "):
        raise ValueError(f"{path}: expected first line to start with '## '")
    heading = lines[0][3:].strip()

    blocks = _parse_body(lines[1:])
    cid = compute_chapter_id(path, heading)
    return Chapter(path=path, id=cid, heading=heading, blocks=blocks)


# --------------------------------------------------------------------------
# HTML rendering
# --------------------------------------------------------------------------

def _format_plain(s: str) -> str:
    s = html.escape(s, quote=False)
    s = _BOLD_RE.sub(r"<strong>\1</strong>", s)
    s = _ITALIC_RE.sub(r"<em>\1</em>", s)
    return s


def _inline_html(text: str) -> str:
    out = []
    pos = 0
    for m in _MATH_SPAN_RE.finditer(text):
        out.append(_format_plain(text[pos:m.start()]))
        svg = render(m.group(1))
        out.append(f'<span class="math">{svg}</span>')
        pos = m.end()
    out.append(_format_plain(text[pos:]))
    return "".join(out)


def _render_figure(fig_id: str, figreg: dict) -> str:
    safe_id = html.escape(fig_id, quote=False)
    entry = figreg.get(fig_id)
    if entry is None:
        return (
            f'<figure id="fig-{safe_id}" class="figure figure-missing">'
            f'<figcaption>[missing figure: {safe_id}]</figcaption></figure>'
        )
    file_path = pathlib.Path(entry["file"])
    svg_content = file_path.read_text(encoding="utf-8").strip()
    number = html.escape(str(entry.get("number", "")), quote=False)
    caption = _inline_html(str(entry.get("caption", "")))
    kind = html.escape(str(entry.get("kind", "")), quote=False)
    return (
        f'<figure id="fig-{safe_id}" class="figure figure-{kind}">'
        f'<div class="figure-media">{svg_content}</div>'
        f'<figcaption>Figure {number}. {caption}</figcaption>'
        f'</figure>'
    )


def _render_quote(raw: str) -> str:
    cls = "quote"
    if raw.startswith("**The math, if you want it:**"):
        cls = "sidebar"
    elif raw.startswith("**Worked example:**"):
        cls = "worked-example"
    return f'<blockquote class="{cls}"><p>{_inline_html(raw)}</p></blockquote>'


def _render_table(header: list, rows: list) -> str:
    parts = ['<table class="md-table"><thead><tr>']
    for cell in header:
        parts.append(f"<th>{_inline_html(cell)}</th>")
    parts.append("</tr></thead><tbody>")
    for row in rows:
        parts.append("<tr>")
        for cell in row:
            parts.append(f"<td>{_inline_html(cell)}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table>")
    return "".join(parts)


def _h4_id(chapter_id: str, text: str) -> str:
    """Anchor id for an h4: the chapter id plus a slug of the heading text,
    e.g. "appendix-a-group-t1a-purpose-and-permissible-use-...". Chapter-
    scoped so identical heading texts in different chapters cannot collide."""
    return f"{chapter_id}-{_SLUG_RE.sub('-', text.lower()).strip('-')}"


def _render_chapter(c: Chapter, figreg: dict) -> str:
    parts = [f'<section class="chapter" aria-labelledby="{c.id}">']
    parts.append(f'<h2 id="{c.id}">{html.escape(c.heading, quote=False)}</h2>')
    for kind, content in c.blocks:
        if kind == "p":
            parts.append(f'<p>{_inline_html(content)}</p>')
        elif kind == "h3":
            parts.append(f'<h3>{_inline_html(content)}</h3>')
        elif kind == "h4":
            parts.append(f'<h4 id="{_h4_id(c.id, content)}">{_inline_html(content)}</h4>')
        elif kind == "fig":
            parts.append(_render_figure(content, figreg))
        elif kind == "hr":
            parts.append('<hr class="rule">')
        elif kind == "quote":
            parts.append(_render_quote(content))
        elif kind == "table":
            header, rows = content
            parts.append(_render_table(header, rows))
    parts.append("</section>")
    return "".join(parts)


def _render_series_bar() -> str:
    """Slim bar linking the three books of the series (spec §9). Shipped
    books are links; unshipped ones are inert "coming soon" labels."""
    items = []
    for label, path, shipped in SERIES_BOOKS:
        esc = html.escape(label, quote=False)
        if label == SERIES_CURRENT:
            items.append(f'<a class="current" href="{path}" aria-current="page">{esc}</a>')
        elif shipped:
            items.append(f'<a href="{path}">{esc}</a>')
        else:
            items.append(f'<span class="soon">{esc} &middot; <em>coming soon</em></span>')
    return ('<nav class="series-bar" aria-label="Books in this series">'
            + "".join(items) + "</nav>\n")


_CSS = """
:root {
  --bg: #fdfaf3;
  --fg: #1b1b1b;
  --muted: #666666;
  --rule: #cccccc;
  --link: #2a5db0;
  --sidebar-bg: #eef3f8;
  --worked-bg: #fff7e6;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #181818;
    --fg: #eaeaea;
    --muted: #aaaaaa;
    --rule: #444444;
    --link: #8ab4f8;
    --sidebar-bg: #1f2937;
    --worked-bg: #332b1a;
  }
}
:root[data-theme="light"] {
  --bg: #fdfaf3;
  --fg: #1b1b1b;
  --muted: #666666;
  --rule: #cccccc;
  --link: #2a5db0;
  --sidebar-bg: #eef3f8;
  --worked-bg: #fff7e6;
}
:root[data-theme="dark"] {
  --bg: #181818;
  --fg: #eaeaea;
  --muted: #aaaaaa;
  --rule: #444444;
  --link: #8ab4f8;
  --sidebar-bg: #1f2937;
  --worked-bg: #332b1a;
}
* { box-sizing: border-box; }
html, body { background: var(--bg); }
body {
  color: var(--fg);
  font-family: Georgia, "Times New Roman", serif;
  max-width: 40rem;
  margin: 0 auto;
  padding: 2rem 1.25rem 4rem;
  line-height: 1.65;
  overflow-x: hidden;
}
h1, h2, h3, h4 { line-height: 1.25; }
h4 { font-size: 1.05rem; color: var(--muted); margin: 2rem 0 0.5rem; }
a { color: var(--link); }
header.title-block { text-align: center; margin-bottom: 2.5rem; }
nav.toc { margin-bottom: 3rem; border-bottom: 1px solid var(--rule); padding-bottom: 1.5rem; }
nav.toc ul { list-style: none; padding: 0; }
nav.toc li { margin: 0.35rem 0; }
section.chapter { margin-bottom: 4rem; }
blockquote.quote {
  border-left: 3px solid var(--rule);
  margin: 1.5rem 0;
  padding: 0.25rem 0 0.25rem 1.25rem;
  color: var(--muted);
}
blockquote.sidebar {
  background: var(--sidebar-bg);
  border-left: 3px solid var(--link);
  margin: 1.5rem 0;
  padding: 1rem 1.25rem;
  border-radius: 4px;
}
blockquote.worked-example {
  background: var(--worked-bg);
  border-left: 3px solid #c98a1a;
  margin: 1.5rem 0;
  padding: 1rem 1.25rem;
  border-radius: 4px;
}
figure.figure { margin: 2rem 0; text-align: center; }
figure.figure .figure-media { overflow-x: auto; }
figure.figure svg { max-width: 100%; height: auto; }
figure.figure .figure-media svg { max-width: none; }
figcaption { font-size: 0.85em; color: var(--muted); margin-top: 0.5rem; }
span.math { display: inline-block; vertical-align: middle; line-height: 0; }
span.math svg { height: 1em; width: auto; vertical-align: middle; }
table.md-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5rem 0;
  font-size: 0.85rem;
}
table.md-table th, table.md-table td {
  padding: 0.3rem 0.6rem;
  text-align: left;
  vertical-align: top;
}
table.md-table thead th { font-weight: bold; border-bottom: 2px solid var(--rule); }
table.md-table tbody tr { border-bottom: 1px solid var(--rule); }
hr.rule { border: none; border-top: 1px solid var(--rule); width: 4rem; margin: 2.5rem auto; }
footer.colophon {
  margin-top: 4rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--rule);
  font-size: 0.85em;
  color: var(--muted);
}
nav.series-bar {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: baseline;
  gap: 0.4rem 1.5rem;
  margin-bottom: 2.5rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--rule);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.14em;
}
nav.series-bar a {
  color: var(--muted);
  text-decoration: none;
  padding-bottom: 0.15em;
  border-bottom: 2px solid transparent;
}
nav.series-bar a:hover { color: var(--link); text-decoration: underline; }
nav.series-bar a.current { color: var(--fg); border-bottom-color: var(--link); }
nav.series-bar span.soon { color: var(--muted); opacity: 0.75; }
nav.series-bar span.soon em {
  font-style: normal;
  font-size: 0.62rem;
  letter-spacing: 0.08em;
}
"""


def build_html(chapter_paths: list, figreg: dict) -> str:
    """Build a single self-contained HTML edition from chapter markdown files."""
    chapters = [parse_chapter(pathlib.Path(p)) for p in chapter_paths]

    toc_items = "".join(
        f'<li><a href="#{c.id}">{html.escape(c.heading, quote=False)}</a></li>'
        for c in chapters
    )
    sections = "".join(_render_chapter(c, figreg) for c in chapters)

    document = (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>Your Next Ham License</title>\n"
        f"<style>{_CSS}</style>\n"
        "</head>\n"
        "<body>\n"
        f"{_render_series_bar()}"
        '<header class="title-block"><h1>Your Next Ham License</h1>'
        "<p>The General Course (2023–2027)</p></header>\n"
        '<nav class="toc" aria-label="Table of contents">'
        f"<h2>Contents</h2><ul>{toc_items}</ul></nav>\n"
        f"<main>{sections}</main>\n"
        '<footer class="colophon">'
        "<h2>About this edition</h2>"
        "<p>This is a self-contained digital edition: every figure and "
        "mathematical expression is embedded directly as inline SVG, and "
        "all styling lives in this one file, so it reads correctly with no "
        "network connection and adapts to your system's light or dark "
        "theme.</p>"
        "</footer>\n"
        "</body>\n"
        "</html>\n"
    )
    return document


# --------------------------------------------------------------------------
# TXT rendering
# --------------------------------------------------------------------------

def build_txt(chapter_paths: list) -> str:
    """Build a plain-text edition from chapter markdown files.

    For each line: (1) turn ``{{fig:ID}}`` into ``[Figure: ID]``, (2) speak
    math spans as English, (3) strip remaining markdown markup. The ``***``
    section-rule marker is converted to a blank line first, since
    narration.strip_markup's emphasis stripping would otherwise leave a
    stray "*" behind (it turns "***" into "*", not ""). Pipe-table data
    rows are kept as raw ``| ... |`` lines (still greppable), but the
    ``|---|`` separator row is dropped as pure markup.
    """
    chapter_texts = []
    for p in chapter_paths:
        path = pathlib.Path(p)
        lines = path.read_text(encoding="utf-8").splitlines()
        out_lines = []
        for line in lines:
            if line.strip() == "***":
                out_lines.append("")
                continue
            if line.strip().startswith("|") and _is_table_separator(line):
                continue
            line = _FIG_TXT_RE.sub(lambda m: f"[Figure: {m.group(1)}]", line)
            line = speak_math(line)
            line = strip_markup(line)
            out_lines.append(line)
        chapter_texts.append("\n".join(out_lines))
    return "\n\n".join(chapter_texts)


# --------------------------------------------------------------------------
# PDF rendering (best-effort)
# --------------------------------------------------------------------------

_CHROME_BINARIES = ["chromium", "chromium-browser", "google-chrome", "google-chrome-stable"]


def build_pdf(html_path, out_pdf) -> bool:
    """Best-effort PDF rendering of a built HTML file. Non-fatal on failure."""
    html_path = pathlib.Path(html_path).resolve()
    out_pdf = pathlib.Path(out_pdf).resolve()
    out_pdf.parent.mkdir(parents=True, exist_ok=True)

    for binary in _CHROME_BINARIES:
        exe = shutil.which(binary)
        if not exe:
            continue
        cmd = [
            exe,
            "--headless=new",
            "--no-sandbox",
            "--disable-gpu",
            f"--print-to-pdf={out_pdf}",
            f"file://{html_path}",
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, timeout=120)
        except Exception:
            continue
        if result.returncode == 0 and out_pdf.exists() and out_pdf.stat().st_size > 0:
            return True

    try:
        import weasyprint  # type: ignore

        weasyprint.HTML(filename=str(html_path)).write_pdf(str(out_pdf))
        if out_pdf.exists() and out_pdf.stat().st_size > 0:
            return True
    except Exception:
        pass

    print("PDF skipped: no chromium/weasyprint")
    return False


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Build the Your Next Ham License editions.")
    parser.add_argument("--html", action="store_true", help="build the HTML edition")
    parser.add_argument("--txt", action="store_true", help="build the TXT edition")
    parser.add_argument("--pdf", action="store_true", help="build the PDF edition (best-effort)")
    parser.add_argument("--out", default="build", help="output directory (default: build/)")
    args = parser.parse_args(argv)

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    figreg = load()
    errors = validate(figreg)
    for err in errors:
        print(f"figure registry warning: {err}")

    # Chapters first (ch00..ch10), then the appendices as final TOC sections.
    chapter_paths = sorted(pathlib.Path("chapters").glob("ch*.md"))
    for app in ("appendices/pool.md", "appendices/glossary-and-formulas.md"):
        app_path = pathlib.Path(app)
        if app_path.exists():
            chapter_paths.append(app_path)

    html_path = out_dir / "index.html"
    if args.html or args.pdf:
        document = build_html(chapter_paths, figreg)
        html_path.write_text(document, encoding="utf-8")
        if args.html:
            print(f"wrote {html_path}")

    if args.txt:
        txt = build_txt(chapter_paths)
        txt_path = out_dir / "your-next-ham-license.txt"
        txt_path.write_text(txt, encoding="utf-8")
        print(f"wrote {txt_path}")

    if args.pdf:
        pdf_path = out_dir / "your-next-ham-license.pdf"
        if build_pdf(html_path, pdf_path):
            print(f"wrote {pdf_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
