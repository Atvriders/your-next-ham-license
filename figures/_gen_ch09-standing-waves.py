"""Generate figures/ch09-standing-waves.svg — voltage along a feed line for a
matched line vs a 2:1 mismatch.

The G9A teaching points (accuracy-canon §2.7, pool 2023–2027):
- Reflected power comes from a mismatch between the feed line and the antenna
  feed-point impedance (G9A04); the reflected wave travels back and sets up a
  standing wave along the line.
- SWR = V_max / V_min along the line; on a matched line the forward and
  reflected waves don't fight, so the voltage magnitude is flat (1:1).
- SWR from a resistive mismatch: SWR = Z_load / Z0 (or Z0 / Z_load, whichever
  is >= 1) — a 100 ohm load on 50 ohm line is 2:1 (G9A09/G9A10 pattern).
- |Gamma| = (SWR - 1)/(SWR + 1): at 2:1 a third of the voltage reflects, so
  the line voltage swings between 2/3 and 4/3 of the forward value.

Top panel: matched line — flat voltage, everything forward. Bottom panel:
2:1 mismatch — the standing-wave envelope with V_max and V_min marked.
Single-color (black) on transparent, then post-processed:
#000000 -> currentColor (established book pattern).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "black"

fig, (a, b) = plt.subplots(
    2, 1, figsize=(7.4, 5.6), sharex=True,
    gridspec_kw=dict(hspace=0.85, top=0.88, bottom=0.13, left=0.12, right=0.96))

fig.suptitle("Standing Waves: What Mismatch Does Along the Feed Line",
             fontsize=13.5, fontweight="bold", color=INK, y=0.965)

x = np.linspace(0, 2.0, 800)  # position along the line, in wavelengths


def dress(ax):
    ax.set_xlim(0, 2.0)
    ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
    ax.set_xticklabels(["0", "λ/2", "λ", "3λ/2", "2λ"])
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(INK)
    ax.tick_params(colors=INK, labelsize=9)
    # line direction labels (bottom corners, clear of the curves)
    ax.annotate("from the transmitter", xy=(0, 0), xytext=(0.005, 0.05),
                xycoords=("axes fraction", "axes fraction"),
                fontsize=9, color=INK, ha="left", va="bottom")
    ax.annotate("to the antenna", xy=(1, 0), xytext=(0.995, 0.05),
                xycoords=("axes fraction", "axes fraction"),
                fontsize=9, color=INK, ha="right", va="bottom")


# ---- panel A: matched line ------------------------------------------------
dress(a)
a.plot(x, np.ones_like(x), color=INK, linewidth=2.4, solid_capstyle="round")
a.set_ylim(0, 2.3)
a.set_yticks([1])
a.set_yticklabels(["V"])
a.set_title("matched: Z_load = Z₀ → no reflection, voltage flat along "
            "the line — SWR 1:1", fontsize=11, color=INK)
a.annotate("all the power flows one way", xy=(1.0, 1.0), xytext=(1.0, 1.62),
           fontsize=10, color=INK, ha="center",
           arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))

# ---- panel B: 2:1 mismatch -------------------------------------------------
dress(b)
G = 1.0 / 3.0                       # |Gamma| for SWR = 2
v = np.sqrt(1 + G**2 + 2 * G * np.cos(4 * np.pi * x))  # |1 + G e^{-j2βx}|
b.plot(x, v, color=INK, linewidth=2.4, solid_capstyle="round")
b.axhline(1 + G, color=INK, linewidth=1.0, linestyle=(0, (6, 4)), alpha=0.7)
b.axhline(1 - G, color=INK, linewidth=1.0, linestyle=(0, (6, 4)), alpha=0.7)
b.set_ylim(0, 2.3)
b.set_yticks([1 - G, 1 + G])
b.set_yticklabels(["V_min", "V_max"], fontsize=9)
b.set_title("mismatched: 100 Ω load on 50 Ω line → SWR = 100/50 = 2:1",
            fontsize=11, color=INK)
b.annotate("reflected wave adds here\nV_max = V_fwd × (1 + |Γ|)",
           xy=(0.5, 1 + G), xytext=(0.74, 2.02), fontsize=9.5, color=INK,
           ha="center",
           arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
b.annotate("and cancels here\nV_min = V_fwd × (1 − |Γ|)",
           xy=(0.75, 1 - G), xytext=(0.85, 0.16), fontsize=9.5, color=INK,
           ha="center",
           arrowprops=dict(arrowstyle="->", color=INK, lw=1.0))
b.set_xlabel("position along the feed line (wavelengths from the antenna)",
             fontsize=10, color=INK)

fig.text(0.5, 0.012,
         "SWR = V_max ÷ V_min = (4/3) ÷ (2/3) = 2:1 — always stated with "
         "the larger number first.",
         fontsize=10.5, color=INK, ha="center", va="bottom")

out = "figures/ch09-standing-waves.svg"
fig.savefig(out, transparent=True)

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
