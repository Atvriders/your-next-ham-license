"""Generate figures/ch07-filter-responses.svg — low/high/band-pass/notch curves.

Pool vocabulary drawn (2023–2027 General, G7C):
- G7C12: cutoff frequency = the half-power point of a low-pass filter
- G7C14: band-pass bandwidth is measured between the half-power frequencies
- G4A01: a notch filter removes an interfering carrier inside the passband

Schematic (not measured) responses on a shared normalized log-frequency axis;
the dashed line marks the half-power (0.707 amplitude) level. Single-color
(black) matplotlib output on a transparent background, then post-processed:
every #000000 becomes currentColor (established pattern from Book 2's
figures/_gen_*.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "black"

f = np.logspace(-1, 1, 800)          # normalized frequency, 0.1..10
fc = 1.0                              # cutoff / center
hp = 0.707                            # half-power amplitude

lp = 1.0 / np.sqrt(1.0 + (f / fc) ** 6)
hpc = (f / fc) ** 3 / np.sqrt(1.0 + (f / fc) ** 6)
bp = 1.0 / np.sqrt(1.0 + ((f ** 2 - fc ** 2) / (0.45 * f)) ** 4)
nt = 1.0 - 1.0 / np.sqrt(1.0 + ((f ** 2 - fc ** 2) / (0.16 * f)) ** 4)

panels = [
    ("LOW-PASS", lp, "passes below the cutoff —", "energy above it is rejected"),
    ("HIGH-PASS", hpc, "passes above the cutoff —", "low-frequency energy rejected"),
    ("BAND-PASS", bp, "passes one band — bandwidth spans", "the two half-power points"),
    ("NOTCH (band-reject)", nt, "digs out one narrow band —", "e.g., an interfering carrier"),
]

fig, axes = plt.subplots(2, 2, figsize=(8.6, 6.4))
fig.subplots_adjust(left=0.07, right=0.97, top=0.76, bottom=0.09,
                    hspace=0.85, wspace=0.16)

fig.suptitle("FILTER RESPONSES — GAIN vs FREQUENCY (schematic)",
             fontsize=13, fontweight="bold", color=INK, y=0.96)

for ax, (name, g, l1, l2) in zip(axes.flat, panels):
    ax.semilogx(f, g, color=INK, linewidth=2.4)
    ax.axhline(hp, color=INK, linewidth=0.9, linestyle=(0, (4, 3)))
    ax.axvline(fc, color=INK, linewidth=0.9, linestyle=(0, (1.5, 2.5)))
    ax.set_title(name, fontsize=11, fontweight="bold", color=INK, pad=30)
    ax.text(0.5, 1.03, l1 + "\n" + l2, fontsize=8.5, ha="center", va="bottom",
            color=INK, transform=ax.transAxes)
    ax.set_xlim(0.1, 10)
    ax.set_ylim(0, 1.15)
    ax.set_yticks([0, hp, 1.0])
    ax.set_yticklabels(["0", "0.707", "1.0"], fontsize=7.5, color=INK)
    ax.set_xticks([0.1, 1, 10])
    ax.set_xticklabels(["0.1", "1", "10"], fontsize=7.5, color=INK)
    ax.set_xlabel("frequency (normalized)", fontsize=8, color=INK)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("bottom", "left"):
        ax.spines[s].set_color(INK)
    ax.tick_params(colors=INK, length=3)

fig.text(0.5, 0.015,
         "dashed = half-power level (0.707) · cutoff and bandwidth are measured "
         "at that level · insertion loss = loss inside the passband",
         fontsize=8, ha="center", color=INK)

out = "figures/ch07-filter-responses.svg"
fig.savefig(out, transparent=True)

with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
