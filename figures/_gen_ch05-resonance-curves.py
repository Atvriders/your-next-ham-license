"""Generate figures/ch05-resonance-curves.svg — series vs parallel resonance.

At resonance X_L = X_C and the reactances cancel (G5A12). A SERIES LC
circuit's impedance dips very low at resonance, bottoming at the circuit's
resistance; a PARALLEL LC circuit's impedance peaks very high (G5A01 — the
swapped pairing is the classic distractor). Higher Q sharpens the notch or
the peak, which is why Q sets selectivity.

Curves use the standard resonant shapes with X0 = 880 Ohm at f0 = 7.0 MHz
(the 40 m band): series |Z| = sqrt(R^2 + (X0*u)^2), parallel
|Z| = R_p / sqrt(1 + (Q*u)^2), with u = f/f0 - f0/f.

Single-color (black) matplotlib output on a transparent background, then
post-processed: every #000000 becomes currentColor (established pattern from
Book 2's figures/_gen_*.py and this repo's _gen_ch01-general-band-chart.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "black"

f0 = 7.0                       # resonance at 7.0 MHz (40 m)
f = np.linspace(6.5, 7.5, 4000)
u = f / f0 - f0 / f            # normalized detuning
X0 = 880.0                     # reactance of L and C at f0, ohms

fig, (axl, axr) = plt.subplots(1, 2, figsize=(8.8, 4.5))
fig.suptitle("At Resonance $X_L = X_C$ — and the Reactances Cancel",
             fontsize=13.5, color=INK)

# ---- left: series LC — impedance minimum -----------------------------------
for R, q, ls, lw in ((10, 88, "solid", 2.4), (100, 9, (0, (5, 3)), 2.0)):
    axl.plot(f, np.sqrt(R ** 2 + (X0 * u) ** 2), color=INK,
             linewidth=lw, linestyle=ls, solid_capstyle="round")
axl.axvline(f0, color=INK, linewidth=1.0, linestyle=(0, (2, 3)), alpha=0.5)
axl.plot([f0, f0], [10, 100], marker="o", markersize=7, color=INK)
axl.annotate("sharp, deep notch — high Q:\n$|Z|$ bottoms at R = 10 Ω",
             xy=(f0, 10), xytext=(7.18, 55),
             fontsize=10, color=INK,
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axl.annotate("more resistance, lower Q —\nshallow and broad (R = 100 Ω)",
             xy=(f0, 100), xytext=(7.08, 140),
             fontsize=10, color=INK,
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axl.text(f0, 176, "$f_0$", fontsize=10.5, color=INK, ha="center", va="top")
axl.set_xlim(6.5, 7.5)
axl.set_ylim(0, 185)
axl.set_xlabel("frequency (MHz)", fontsize=10, color=INK)
axl.set_ylabel("$|Z|$ (Ω)", fontsize=10, color=INK)
axl.set_title("SERIES LC — impedance dips LOW at resonance",
              fontsize=11.5, color=INK)

# ---- right: parallel LC — impedance maximum --------------------------------
for Rp, q, ls, lw in ((88e3, 100, "solid", 2.4), (8.8e3, 10, (0, (5, 3)), 2.0)):
    axr.plot(f, Rp / np.sqrt(1 + (q * u) ** 2) / 1e3, color=INK,
             linewidth=lw, linestyle=ls, solid_capstyle="round")
axr.axvline(f0, color=INK, linewidth=1.0, linestyle=(0, (2, 3)), alpha=0.5)
axr.plot([f0, f0], [88, 8.8], marker="o", markersize=7, color=INK)
axr.annotate("tall, narrow peak — high Q:\n$|Z|$ tops out at 88 kΩ",
             xy=(f0, 88), xytext=(7.16, 68),
             fontsize=10, color=INK,
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axr.annotate("lossy tank, low Q —\na low, broad hump (8.8 kΩ)",
             xy=(f0, 8.8), xytext=(7.2, 26),
             fontsize=10, color=INK,
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axr.text(6.53, 93, "$f_0$", fontsize=10.5, color=INK, ha="left", va="top")
axr.set_xlim(6.5, 7.5)
axr.set_ylim(0, 98)
axr.set_xlabel("frequency (MHz)", fontsize=10, color=INK)
axr.set_ylabel("$|Z|$ (kΩ)", fontsize=10, color=INK)
axr.set_title("PARALLEL LC — impedance peaks HIGH at resonance",
              fontsize=11.5, color=INK)

for ax in (axl, axr):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(INK)
    ax.tick_params(colors=INK, labelsize=9.5)
    ax.grid(axis="y", color=INK, alpha=0.15, linewidth=0.7)

fig.text(0.5, 0.005,
         "series low, parallel high — and the higher the Q, the sharper the "
         "notch or peak (Q is selectivity)",
         fontsize=10, color=INK, ha="center", va="bottom", style="italic")

fig.tight_layout(rect=[0, 0.045, 1, 0.93])

out = "figures/ch05-resonance-curves.svg"
fig.savefig(out, transparent=True, bbox_inches="tight")

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
