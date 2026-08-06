"""Synthesize the audiobook introduction (audiobook/intro.mp3) with edge-tts.

A short spoken preface that opens the audiobook: a welcome back to the
licensed Technician upgrading to General, what Your Next Ham License is,
that it was written by Kimi K3 — an artificial intelligence made by
Moonshot AI — running inside Kimi Code, and how to use the eight-voice edition. Kept separate from the chapter tracks so it
can be regenerated on its own.

Usage:
  python tools/make_intro.py        # writes audiobook/intro.mp3
  python tools/make_intro.py --dry  # print the intro text and exit (no synth, no network)

Requires: edge-tts (pip install edge-tts) and ffmpeg on PATH.
Edit VOICE or INTRO and rerun to change the narration.
"""

import asyncio
import subprocess
import sys
from pathlib import Path

import edge_tts

VOICE = "en-GB-RyanNeural"
OUT = Path(__file__).resolve().parent.parent / "audiobook" / "intro.mp3"

INTRO = """Your Next Ham License: The General Course, 2023 to 2027. A welcome back.

This audiobook was written by Kimi K3 — an artificial intelligence made by Moonshot AI — running inside the coding tool Kimi Code. The book exists to carry a licensed Technician across one exam and onto the worldwide HF bands. It was built by a multi-agent AI workflow — dozens of cooperating agents writing, checking, and auditing every fact against an accuracy canon and every question against the official pool — at a cost of roughly four point one million tokens, an estimate, over two days.

You already hold your Technician license. You know your way around a repeater, you know two meters and seventy centimeters — and you have probably wondered what lives on the bands where contacts cross oceans. This course is your upgrade path: in eleven chapters it takes you from Technician to General. Your new HF privileges and the rules that come with them, operating on HF, propagation in depth, AC theory and practical circuits, signals and antennas at General depth, and safety at higher power. Every fact and every practice question is checked against the official twenty twenty-three to twenty twenty-seven General question pool, so what you hear is what the exam asks.

This edition is offered in eight voices — American, British, Australian, and Irish, male and female.

And now — Your Next Ham License. Your upgrade begins whenever you are ready."""


async def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    raw = OUT.with_suffix(".raw.mp3")
    last = None
    for attempt in range(1, 6):
        try:
            await edge_tts.Communicate(INTRO, VOICE).save(str(raw))
            if raw.stat().st_size > 500:
                break
            raise RuntimeError("empty audio")
        except Exception as e:  # noqa: BLE001 - retry any transport error
            last = e
            await asyncio.sleep(2 * attempt)
    else:
        raise RuntimeError(f"synthesis failed after retries: {last}")

    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(raw),
            "-c", "copy",
            "-metadata", "title=Introduction",
            "-metadata", "artist=Kimi K3",
            "-metadata", "album=Your Next Ham License",
            "-metadata", "track=0/11",
            "-metadata", "genre=Audiobook",
            "-metadata", "date=2026",
            str(OUT),
        ],
        check=True,
    )
    raw.unlink(missing_ok=True)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    if "--dry" in sys.argv[1:]:
        print(INTRO)
        sys.exit(0)
    asyncio.run(main())
