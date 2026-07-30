"""Generate figures/ch07-amp-classes.svg — amplifier classes A/AB/B/C conduction angle.

Pool facts drawn (2023–2027 General, subelement G7B):
- G7B04: class A conducts 100 % of the cycle
- G7B02: class C has the highest efficiency
- G7B11: class C suits constant-envelope modes (FM) — not SSB
- G7B10: a linear amplifier preserves the input waveform

Each panel: dashed = input drive sine, solid = output current. The double arrow
under each trace marks the conduction angle. Single-color (black) matplotlib
output on a transparent background, then post-processed: every #000000 becomes
currentColor (established pattern from Book 2's figures/_gen_*.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "black"

deg = np.linspace(-90, 270, 721)
x = np.radians(deg)
drive = np.sin(x)

# output current per class (0..1), conduction window in degrees
panels = [
    ("CLASS A", 0.5 + 0.5 * drive, (-90, 270), "conducts 100 % of the cycle",
     "most linear, least efficient"),
    ("CLASS AB", np.maximum(drive + 0.3, 0), (-17.5, 197.5),
     "conducts more than half", "a compromise"),
    ("CLASS B", np.maximum(drive, 0), (0, 180), "conducts 180° — half",
     "push-pull restores the shape"),
    ("CLASS C", np.maximum(drive - 0.55, 0), (56.6, 123.4),
     "conducts less than half", "most efficient, distorts"),
]

fig, axes = plt.subplots(1, 4, figsize=(10.4, 3.4))
fig.subplots_adjust(left=0.02, right=0.98, top=0.66, bottom=0.30, wspace=0.18)

fig.suptitle("AMPLIFIER CLASSES — HOW MUCH OF EACH CYCLE THE DEVICE CONDUCTS",
             fontsize=13, fontweight="bold", color=INK, y=0.93)
fig.text(0.5, 0.815, "dashed = input drive      solid = output current      "
         "double arrow = conduction angle", fontsize=9, ha="center", color=INK)

for ax, (name, out, win, sub, note) in zip(axes, panels):
    ax.plot(deg, drive, color=INK, linewidth=1.1, linestyle=(0, (4, 3)))
    ax.plot(deg, out, color=INK, linewidth=2.4)
    ax.axhline(0, color=INK, linewidth=0.8)
    ax.annotate("", xy=(win[0], -0.32), xytext=(win[1], -0.32),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.2))
    ax.set_title(name, fontsize=11.5, fontweight="bold", color=INK, pad=4)
    ax.text(90, 1.34, sub, fontsize=8, ha="center", color=INK)
    ax.text(90, -0.72, note, fontsize=8, ha="center", color=INK, style="italic")
    ax.set_xlim(-90, 270)
    ax.set_ylim(-0.95, 1.52)
    ax.set_xticks([0, 90, 180, 270])
    ax.set_xticklabels(["0°", "90°", "180°", "270°"], fontsize=7.5, color=INK)
    ax.set_yticks([])
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(INK)
    ax.tick_params(colors=INK, length=3)

fig.text(0.5, 0.065,
         "Linearity and efficiency pull opposite ways: class A conducts all cycle but wastes power; class C is the most efficient\n"
         "but distorts amplitude — fine for constant-envelope modes (FM, CW), never for SSB, which needs a linear amplifier.",
         fontsize=9, ha="center", color=INK)

out = "figures/ch07-amp-classes.svg"
fig.savefig(out, transparent=True)

with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
