"""Generate figures/ch05-reactance-curves.svg — reactance versus frequency.

X_L = 2*pi*f*L rises in direct proportion to frequency (G5A05); X_C =
1/(2*pi*f*C) falls inversely (G5A06). One worked point each from the pool's
own numbers (canon section 3 formula set, r3 G5A math):
- 20 mH inductor (G5C11's value) at 7 MHz -> X_L ~= 880 kOhm
- 100 uF capacitor (G5C09's value) at 60 Hz -> X_C ~= 26.5 Ohm, halving to
  13.3 Ohm at 120 Hz ("double the frequency, half the reactance")

Single-color (black) matplotlib output on a transparent background, then
post-processed: every #000000 becomes currentColor (established pattern from
Book 2's figures/_gen_*.py and this repo's _gen_ch01-general-band-chart.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "black"

fig, (axl, axr) = plt.subplots(1, 2, figsize=(8.8, 4.5))
fig.suptitle("Reactance Opposes AC — and Frequency Moves It",
             fontsize=13.5, color=INK)

# ---- left: inductive reactance rises with frequency ------------------------
L = 20e-3  # 20 mH, the pool's G5C11 inductor
f_mhz = np.linspace(0, 14, 200)
xl_kohm = 2 * np.pi * f_mhz * 1e6 * L / 1e3

axl.plot(f_mhz, xl_kohm, color=INK, linewidth=2.4, solid_capstyle="round")
axl.plot([7], [880], marker="o", markersize=7, color=INK)
axl.annotate("the pool's 20 mH inductor at 7 MHz:\n"
             "$X_L = 2\\pi f L \\approx 880$ kΩ",
             xy=(7, 880), xytext=(2.2, 1250),
             fontsize=10, color=INK,
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axl.text(0.96, 0.05,
         "a straight line through the origin —\ndouble the frequency, double $X_L$",
         transform=axl.transAxes, fontsize=9.5, color=INK,
         ha="right", va="bottom", style="italic")
axl.set_xlim(0, 14)
axl.set_ylim(0, 1900)
axl.set_xlabel("frequency (MHz) — the HF range", fontsize=10, color=INK)
axl.set_ylabel("$X_L$ (kΩ)", fontsize=10, color=INK)
axl.set_title("Inductor: $X_L = 2\\pi f L$ rises with frequency",
              fontsize=11.5, color=INK)

# ---- right: capacitive reactance falls with frequency ----------------------
C = 100e-6  # 100 uF, the pool's G5C09 capacitor
f_hz = np.linspace(10, 120, 400)
xc = 1 / (2 * np.pi * f_hz * C)

axr.plot(f_hz, xc, color=INK, linewidth=2.4, solid_capstyle="round")
axr.plot([60, 120], [26.5, 13.3], marker="o", markersize=7, color=INK)
axr.annotate("the pool's 100 µF capacitor at 60 Hz:\n"
             "$X_C = 1\\,/\\,(2\\pi f C) \\approx 26.5$ Ω",
             xy=(60, 26.5), xytext=(24, 90),
             fontsize=10, color=INK,
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axr.annotate("at 120 Hz it has halved: 13.3 Ω",
             xy=(120, 13.3), xytext=(64, 46),
             fontsize=9.5, color=INK,
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axr.set_xlim(0, 125)
axr.set_ylim(0, 170)
axr.set_xlabel("frequency (Hz) — the AC-mains range", fontsize=10, color=INK)
axr.set_ylabel("$X_C$ (Ω)", fontsize=10, color=INK)
axr.set_title("Capacitor: $X_C = 1\\,/\\,(2\\pi f C)$ falls with frequency",
              fontsize=11.5, color=INK)

for ax in (axl, axr):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(INK)
    ax.tick_params(colors=INK, labelsize=9.5)
    ax.grid(axis="y", color=INK, alpha=0.15, linewidth=0.7)

fig.tight_layout(rect=[0, 0, 1, 0.93])

out = "figures/ch05-reactance-curves.svg"
fig.savefig(out, transparent=True, bbox_inches="tight")

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
