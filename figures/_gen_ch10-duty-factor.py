"""Generate figures/ch10-duty-factor.svg — duty factor vs average exposure.

The G0A teaching points (accuracy-canon §2.7, pool 2023–2027):
- RF exposure depends on frequency, power density, and duty cycle (G0A02);
  exposure limits are judged on the time average (G0A04), so a lower duty
  cycle permits higher power for the same exposure (G0A07).
- Average = PEP x mode duty x key-down fraction. Typical OET-65-style mode
  duty factors: conversational SSB voice ~0.2, CW ~0.4, constant-carrier
  modes (FT8, FM, RTTY) 1.0. Key down half the window and the averages come
  out 10 % / 20 % / 50 % of PEP.
- Canon G8B08: high-duty-cycle modes (FT8, RTTY, FM) run the transmitter
  hard — the same physics that raises the average exposure.

Top panel: a 60-second averaging window with three transmit timelines —
bar height is the mode duty (average vs PEP while keyed), bar width is the
key-down time. Bottom panel: the resulting averages, same PEP throughout.
Single-color (black) on transparent, then post-processed:
#000000 -> currentColor (established book pattern).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "black"

fig = plt.figure(figsize=(7.4, 6.6))
gs = fig.add_gridspec(2, 1, height_ratios=[1, 1.15], hspace=0.68,
                      top=0.88, bottom=0.14, left=0.13, right=0.97)

fig.suptitle("Duty Factor Sets the Average Exposure", fontsize=14,
             fontweight="bold", color=INK, y=0.965)

# ---- panel A: one averaging window, three timelines ------------------------
a = fig.add_subplot(gs[0])
W = 60.0  # the averaging window, seconds

# lanes: (y, label, tx segments, mode duty, math note)
lanes = [
    (2.5, "SSB voice", [(0, 15), (30, 15)], 0.2,
     "voice ~0.2 mode duty\n× 50 % key-down\n= 10 % of PEP"),
    (1.5, "CW", [(0, 15), (30, 15)], 0.4,
     "~0.4 mode duty\n× 50 % key-down\n= 20 % of PEP"),
    (0.5, "FT8", [(15, 15), (45, 15)], 1.0,
     "100 % mode duty\n× 50 % key-down\n= 50 % of PEP"),
]
for y, lab, segs, duty, note in lanes:
    a.plot([0, W], [y, y], color=INK, linewidth=0.8, alpha=0.45)
    a.broken_barh(segs, (y, 0.62 * duty), facecolors=INK)
    a.annotate(note, xy=(63, y + 0.31), fontsize=8.8, color=INK,
               ha="left", va="center")
a.set_xlim(0, 88)
a.set_ylim(0.1, 3.9)
a.set_yticks([l[0] + 0.31 for l in lanes])
a.set_yticklabels([l[1] for l in lanes], fontsize=10)
a.set_xticks([0, 15, 30, 45, 60])
a.set_xlabel("time (seconds)", fontsize=9.5, color=INK)
a.set_title("one averaging window — bar height = mode duty, "
            "bar width = key-down time", fontsize=11, color=INK)
for side in ("top", "right", "left"):
    a.spines[side].set_visible(False)
a.spines["bottom"].set_color(INK)
a.tick_params(colors=INK, labelsize=9)
# bracket: the averaging window
a.annotate("", xy=(0, 3.62), xytext=(60, 3.62),
           arrowprops=dict(arrowstyle="<->", color=INK, lw=1.2))
a.annotate("the averaging window", xy=(30, 3.7), fontsize=9.5, color=INK,
           ha="center", va="bottom")

# ---- panel B: the resulting averages --------------------------------------
b = fig.add_subplot(gs[1])
modes = ["SSB voice", "CW", "FT8", "FM / RTTY\n(continuous)"]
vals = [10, 20, 50, 100]
bars = b.bar(modes, vals, width=0.58, color=INK)
for rect, v in zip(bars, vals):
    b.annotate(f"{v} %", xy=(rect.get_x() + rect.get_width() / 2, v),
               xytext=(0, 4), textcoords="offset points", fontsize=10.5,
               fontweight="bold", color=INK, ha="center")
b.set_ylim(0, 122)
b.set_yticks([0, 20, 40, 60, 80, 100])
b.set_ylabel("average power\n(% of PEP)", fontsize=10, color=INK)
b.set_title("same radio, same 100 W PEP — the mode decides the average",
            fontsize=11, color=INK)
for side in ("top", "right"):
    b.spines[side].set_visible(False)
for side in ("left", "bottom"):
    b.spines[side].set_color(INK)
b.tick_params(colors=INK, labelsize=9.5)
b.grid(axis="y", color=INK, alpha=0.15, linewidth=0.7)
b.annotate("lower duty factor → lower average →\nmore headroom under the limits",
           xy=(1.5, 78), fontsize=9.5, color=INK, ha="center", va="center")

fig.text(0.5, 0.042,
         "Time averaging: exposure is judged on the average over the window —",
         fontsize=10, color=INK, ha="center", va="bottom")
fig.text(0.5, 0.008,
         "a lower duty factor permits higher power for the same exposure.",
         fontsize=10, color=INK, ha="center", va="bottom")

out = "figures/ch10-duty-factor.svg"
fig.savefig(out, transparent=True)

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
