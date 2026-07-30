"""Generate figures/ch08-digital-waterfalls.svg — three stylized waterfall
panels teaching G8C mode identification on the display (pool G8C14: frequency
horizontal, time vertical, signal strength as brightness).

Panel facts, all from the accuracy canon (§2.5 digital operating; §2.7 G8):
- FT8: 8-tone FSK in timed 15-second transmit/receive sequences (pool G8A09);
  many stations share one dial frequency at different audio offsets, and
  answers go in the ALTERNATE time slot (pool G2E04). Each burst keys ~13 s
  inside its 15 s slot and is ~50 Hz wide.
- PSK31: one narrow continuous trace (~31 Hz) for the whole QSO — it hangs
  out near the bottom of each band's data segment (pool G8C12, canon §2.5).
- RTTY: two tones named mark and space (pool G8C11); the most common HF shift
  is 170 Hz (pool G2E06, canon value).

Single-color (black) matplotlib output on a transparent background, then
post-processed here: every #000000 becomes currentColor so the SVG themes
with the book's text color (established pattern from the Tech and General
books' figures/_gen_*.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

rng = np.random.default_rng(7)

T_MAX = 60.0     # seconds of waterfall history shown
F_MAX = 3000.0   # audio passband width, Hz
INK = "black"

fig, axes = plt.subplots(1, 3, figsize=(7.8, 4.3), sharex=True, sharey=True)


def style(ax, title):
    ax.set_xlim(0, F_MAX)
    ax.set_ylim(T_MAX, 0)  # time flows down the screen
    ax.set_title(title, fontsize=10.5, color=INK)
    ax.tick_params(colors=INK, labelsize=9)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(INK)


# ---------- panel 1: FT8 — tone bursts in 15-second slots ------------------
ax = axes[0]
for t in (15, 30, 45):
    ax.axhline(t, color=INK, alpha=0.25, linewidth=0.8, linestyle=(0, (4, 3)))
# three stations at different audio offsets; slots alternate transmit/receive
# (answer a CQ in the alternate slot — pool G2E04)
stations = [(600, (0, 30)), (1400, (15, 45)), (2200, (0, 30))]
for f0, slots in stations:
    for s in slots:
        ax.add_patch(Rectangle((f0 - 25, s + 0.6), 50, 12.6, facecolor=INK,
                               alpha=0.85, edgecolor="none"))
ax.text(2880, 58.5, "15 s slots", fontsize=9, style="italic", color=INK,
        ha="right", va="bottom")
ax.annotate("each burst ~13 s,\n~50 Hz wide (8 tones)", xy=(2225, 37),
            xytext=(2470, 20), ha="center", fontsize=9, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
ax.text(450, 52, "many stations share\none dial frequency",
        fontsize=9, style="italic", color=INK, ha="center", va="center")
style(ax, "FT8 — 8-tone FSK in 15 s slots")

# ---------- panel 2: PSK31 — one narrow continuous trace -------------------
ax = axes[1]
t = np.linspace(0, T_MAX, 400)
trace = 1000 + 6 * np.sin(t * 1.7) + rng.normal(0, 2.5, t.size)
ax.plot(trace, t, color=INK, linewidth=2.2, solid_capstyle="round")
ax.annotate("one narrow trace,\n~31 Hz wide,\nruns the whole QSO",
            xy=(1008, 32), xytext=(1750, 22), ha="center", fontsize=9,
            color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
style(ax, "PSK31 — a single narrow trace")

# ---------- panel 3: RTTY — mark and space, 170 Hz apart -------------------
ax = axes[2]
mark = 1200 + 4 * np.sin(t * 1.3) + rng.normal(0, 2.5, t.size)
space = 1370 + 4 * np.sin(t * 1.3 + 0.8) + rng.normal(0, 2.5, t.size)
ax.plot(mark, t, color=INK, linewidth=2.2, solid_capstyle="round")
ax.plot(space, t, color=INK, linewidth=2.2, solid_capstyle="round")
ax.annotate("mark", xy=(1196, 22), xytext=(800, 22), ha="center",
            va="center", fontsize=9.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
ax.annotate("space", xy=(1374, 14), xytext=(1900, 14), ha="center",
            va="center", fontsize=9.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
ax.annotate("", xy=(1370, 50), xytext=(1200, 50),
            arrowprops=dict(arrowstyle="<->", color=INK, lw=1.2))
ax.text(1600, 50, "170 Hz shift", fontsize=9.5, color=INK, ha="left",
        va="center")
style(ax, "RTTY — mark and space tones")

# ---------- shared axes + caption ------------------------------------------
axes[0].set_yticks([0, 15, 30, 45, 60])
axes[0].set_yticklabels(["0", "15", "30", "45", "60 s"])
axes[0].set_ylabel("time flows down", fontsize=10, color=INK)
fig.text(0.5, 0.015, "audio frequency in the receiver passband (Hz)",
         fontsize=10, color=INK, ha="center")
fig.suptitle("reading a waterfall: frequency across, time down, strength as brightness",
             fontsize=12, color=INK)

fig.tight_layout(rect=[0, 0.05, 1, 0.94])

out = "figures/ch08-digital-waterfalls.svg"
fig.savefig(out, transparent=True, bbox_inches="tight", pad_inches=0.05)

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
