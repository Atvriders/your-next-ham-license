"""Shared narration/text transforms used by the audiobook and TXT builders.

Pure-stdlib helpers for turning lightly-marked-up manuscript text into
narration-friendly plain text:

- strip_markup: drop figure refs, heading/blockquote markers, and
  emphasis markup, leaving plain prose.
- speak_math: turn inline ``$...$`` math spans into spoken English.
- speak_figures: expand ``{{fig:ID}}`` references into a spoken
  parenthetical using a supplied figure-description table.
"""

import re

# index 0 is unused ("") so that NUMBER_WORDS[n] gives the word for n.
NUMBER_WORDS = [
    "",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
    "Twenty",
]

_ROMAN_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral string (e.g. "XIV") to an int."""
    s = s.strip().upper()
    total = 0
    prev = 0
    for ch in reversed(s):
        val = _ROMAN_VALUES.get(ch, 0)
        if val < prev:
            total -= val
        else:
            total += val
            prev = val
    return total


_FIG_REF_RE = re.compile(r"\{\{fig:[^}]*\}\}")
_HEADING_RE = re.compile(r"(?m)^\s*#+\s*")
_BLOCKQUOTE_RE = re.compile(r"(?m)^\s*>\s*")
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
_ITALIC_RE = re.compile(r"\*(.+?)\*")
_WHITESPACE_RE = re.compile(r"\s+")


def strip_markup(s: str) -> str:
    """Strip figure refs, heading/blockquote markers, and emphasis markup."""
    s = _FIG_REF_RE.sub("", s)
    s = _HEADING_RE.sub("", s)
    s = _BLOCKQUOTE_RE.sub("", s)
    s = _BOLD_RE.sub(r"\1", s)
    s = _ITALIC_RE.sub(r"\1", s)
    s = _WHITESPACE_RE.sub(" ", s).strip()
    return s


_MATH_SPAN_RE = re.compile(r"\$(.+?)\$")

# LaTeX commands and unicode symbols spoken as ordinary words. Single-letter
# variables are not listed here: any other letter is spoken as itself, so
# runs like "IR" come out as separate letters.
_MATH_WORDS = {
    "\\Delta": "delta",
    "Δ": "delta",
    "\\lambda": "lambda",
    "λ": "lambda",
    "\\pi": "pi",
    "π": "pi",
    "\\eta": "eta",
    "\\mu": "micro",
    "µ": "micro",
    "\\Omega": "ohms",
    "Ω": "ohms",
    "\\times": "times",
    "×": "times",
    "\\cdot": "times",
    "\\approx": "approximately",
    "≈": "approximately",
    "\\angle": "angle",
    "\\leq": "less than or equal to",
    "\\geq": "greater than or equal to",
    "=": "equals",
    "/": "over",
    "+": "plus",
    "-": "minus",
}

# Words after which a following \sqrt/\frac is NOT an implied
# multiplication, so no "times" is inserted in between.
_OPERATOR_WORDS = {
    "equals",
    "over",
    "plus",
    "minus",
    "times",
    "approximately",
    "less than or equal to",
    "greater than or equal to",
    "angle",
    "of",
    "base",
}

# Subscripts spoken as words rather than spelled out, matching the book's
# prose conventions ("peak-to-peak", "RMS", "average power", "f max").
_SUB_WORDS = {
    "pp": "peak-to-peak",
    "rms": "R M S",
    "avg": "average",
    "peak": "peak",
    "max": "max",
    "load": "load",
    "out": "out",
    "in": "in",
}

_MATH_COMMAND_RE = re.compile(r"\\[A-Za-z]+|\\.")
_MATH_NUMBER_RE = re.compile(r"\d+(?:\.\d+)?")


def _ordinal(n: str) -> str:
    """Ordinal string for an integer string ("20" -> "20th")."""
    v = int(n)
    if 10 <= v % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(v % 10, "th")
    return f"{v}{suffix}"


def _read_group_raw(expr: str, i: int) -> "tuple[str, int]":
    """Raw text of a {...} group (or single char) starting at i."""
    if i < len(expr) and expr[i] == "{":
        depth = 1
        j = i + 1
        while j < len(expr) and depth:
            if expr[j] == "{":
                depth += 1
            elif expr[j] == "}":
                depth -= 1
            j += 1
        return expr[i + 1 : j - 1], j
    return (expr[i], i + 1) if i < len(expr) else ("", i)


def _read_script(expr: str, i: int) -> "tuple[str, int]":
    """Raw content of a sub/superscript starting at i."""
    if i < len(expr) and expr[i] == "{":
        return _read_group_raw(expr, i)
    m = _MATH_COMMAND_RE.match(expr, i)
    if m:
        return m.group(0), m.end()
    return (expr[i], i + 1) if i < len(expr) else ("", i)


def _read_group(expr: str, i: int) -> "tuple[list[str], int]":
    """Speak a {...} group (or a single character) starting at i."""
    if i < len(expr) and expr[i] == "{":
        words, j = _speak_atoms(expr, i + 1, "}")
        return words, (j + 1 if j < len(expr) else j)
    words, _ = _speak_atoms(expr[i : i + 1], 0, None)
    return words, min(i + 1, len(expr))


def _speak_sub(content: str) -> "list[str]":
    if content in _SUB_WORDS:
        return [_SUB_WORDS[content]]
    if len(content) == 1 or not content.isalpha():
        return [content]
    return list(content)


def _speak_super(content: str) -> "list[str]":
    if content == "2":
        return ["squared"]
    if content == "3":
        return ["cubed"]
    if content == "\\circ":
        return ["degrees"]
    if content.isdigit():
        return ["to the " + _ordinal(content)]
    words, _ = _speak_atoms(content, 0, None)
    return ["to the power of"] + words


def _speak_atoms(expr: str, i: int, closer: "str | None") -> "tuple[list[str], int]":
    """Speak math atoms from expr[i:] up to ``closer`` (or end of string).

    Returns the spoken words and the index of the closer (or len(expr)).
    """
    words: "list[str]" = []
    while i < len(expr):
        ch = expr[i]
        if closer and ch == closer:
            return words, i
        if ch.isspace() or ch in "){',":
            i += 1
        elif ch == "\\":
            m = _MATH_COMMAND_RE.match(expr, i)
            cmd = m.group(0)
            i = m.end()
            if cmd in _MATH_WORDS:
                words.append(_MATH_WORDS[cmd])
            elif cmd == "\\sqrt":
                group, i = _read_group(expr, i)
                if words and words[-1] not in _OPERATOR_WORDS:
                    words.append("times")
                words.append("the square root of")
                words.extend(group)
                # Mark the phrase boundary when more math follows the
                # radical (possibly past enclosing parentheses).
                j = i
                while j < len(expr) and expr[j] in ") \t":
                    j += 1
                if j < len(expr) and expr[j] != closer:
                    words[-1] += ","
            elif cmd == "\\frac":
                num, i = _read_group(expr, i)
                den, i = _read_group(expr, i)
                if words and words[-1] not in _OPERATOR_WORDS:
                    words.append("times")
                words.extend(num)
                words.append("over")
                words.extend(den)
            elif cmd == "\\log":
                words.append("log")
                j = i
                while j < len(expr) and expr[j].isspace():
                    j += 1
                if j < len(expr) and expr[j] == "_":
                    base, j = _read_script(expr, j + 1)
                    words.append("base")
                    words.extend(_speak_sub(base))
                    i = j
                    while j < len(expr) and expr[j].isspace():
                        j += 1
                if j < len(expr) and expr[j] == "(":
                    words.append("of")
            elif cmd == "\\mathrm":
                raw, i = _read_group_raw(expr, i)
                if raw.strip():
                    words.append(raw.strip())
            elif len(cmd) > 2:
                words.append(cmd[1:])
            # Two-character commands ("\\ " and friends) are LaTeX spacing;
            # they are not spoken.
        elif ch == "|":
            inner, j = _speak_atoms(expr, i + 1, "|")
            words.append("magnitude of")
            words.extend(inner)
            i = j + 1 if j < len(expr) else j
        elif ch == "(":
            inner, j = _speak_atoms(expr, i + 1, ")")
            j = j + 1 if j < len(expr) else j
            k = j
            while k < len(expr) and expr[k].isspace():
                k += 1
            if k < len(expr) and expr[k] == "^" and inner:
                content, k = _read_script(expr, k + 1)
                sup = _speak_super(content)
                if sup in (["squared"], ["cubed"]):
                    words.append("the quantity")
                    words.extend(inner)
                    words[-1] += ","
                    words.extend(sup)
                else:
                    words.extend(inner)
                    words.extend(sup)
                i = k
            else:
                words.extend(inner)
                i = j
        elif ch in "_^":
            content, i = _read_script(expr, i + 1)
            words.extend(_speak_sub(content) if ch == "_" else _speak_super(content))
        elif ch in _MATH_WORDS:
            words.append(_MATH_WORDS[ch])
            i += 1
        elif ch.isalpha():
            words.append(ch)
            i += 1
        elif ch.isdigit():
            m = _MATH_NUMBER_RE.match(expr, i)
            words.append(m.group(0))
            i = m.end()
        else:
            i += 1  # any other punctuation is not spoken
    return words, i


def _speak_math_span(expr: str) -> str:
    words, _ = _speak_atoms(expr, 0, None)
    return " ".join(words)


def speak_math(s: str) -> str:
    """Replace each ``$...$`` math span with spoken English."""

    def repl(m: "re.Match[str]") -> str:
        return _speak_math_span(m.group(1))

    out = _MATH_SPAN_RE.sub(repl, s)
    out = _WHITESPACE_RE.sub(" ", out).strip()
    return out


_FIG_CAPTURE_RE = re.compile(r"\{\{fig:([^}]*)\}\}")


def speak_figures(s: str, descriptions: "dict[str, tuple[str, str]]") -> str:
    """Replace ``{{fig:ID}}`` refs with a spoken figure description."""

    def repl(m: "re.Match[str]") -> str:
        fig_id = m.group(1)
        if fig_id not in descriptions:
            return ""
        num, desc = descriptions[fig_id]
        return f"(Figure {num}. {desc}.)"

    return _FIG_CAPTURE_RE.sub(repl, s)
