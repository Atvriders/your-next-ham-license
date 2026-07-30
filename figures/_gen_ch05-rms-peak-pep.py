"""Generate figures/ch05-rms-peak-pep.svg — RMS/peak/peak-to-peak and PEP.

Left: one sine wave, three yardsticks — V_pk, V_pp, and V_rms = 0.707 x V_pk,
the value that heats a resistor like the same DC voltage (G5B07). The pool's
own drills: 17 V peak ~= 12 V RMS (G5B09), 120 V RMS ~= 339.4 V p-p (G5B08).

Right: an SSB signal's power lives at the envelope peak. PEP uses the peak RF
voltage: PEP = V_pp^2 / (8R), so 200 V p-p into 50 ohms is 100 W (G5B06) and
500 V p-p is 625 W (G5B14). Average voice power sits well below; for an
unmodulated carrier PEP equals average power, ratio 1.00 (G5B11).

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
fig.suptitle("RMS, Peak, Peak-to-Peak — and PEP for SSB",
             fontsize=13.5, color=INK)

# ---- left: one sine wave, three yardsticks ----------------------------------
t = np.linspace(0, 2, 600)     # two cycles
v = 100 * np.sin(2 * np.pi * t)

axl.plot(t, v, color=INK, linewidth=2.2, solid_capstyle="round")
axl.axhline(0, color=INK, linewidth=0.9, alpha=0.6)
axl.axhline(70.7, color=INK, linewidth=1.3, linestyle=(0, (5, 3)))
axl.text(1.30, 106, "dashed: $V_{rms} = 0.707 \\times V_{pk} \\approx 70.7$ V\n"
         "— heats a resistor like 70.7 V DC",
         fontsize=9.5, color=INK, ha="center", va="bottom")
# V_pk arrow: 0 -> +100 at the first peak
axl.annotate("", xy=(0.25, 100), xytext=(0.25, 0),
             arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
axl.text(0.27, 106, "$V_{pk}$ = 100 V", fontsize=9.5, color=INK,
         ha="center", va="bottom")
# V_pp arrow: -100 -> +100 at the second peak
axl.annotate("", xy=(1.25, 100), xytext=(1.25, -100),
             arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
axl.text(1.25, -110, "$V_{pp}$ = 200 V", fontsize=9.5, color=INK,
         ha="center", va="top")
axl.set_xlim(0, 2)
axl.set_ylim(-140, 150)
axl.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
axl.set_xlabel("time (cycles of the AC sine)", fontsize=10, color=INK)
axl.set_ylabel("volts", fontsize=10, color=INK)
axl.set_title("One sine wave, three yardsticks", fontsize=11.5, color=INK)

# ---- right: SSB envelope — PEP vs average -----------------------------------
t2 = np.linspace(0, 1, 2400)   # one second of speech
env = (0.42 + 0.28 * np.sin(2 * np.pi * 2.3 * t2)
       + 0.18 * np.sin(2 * np.pi * 3.7 * t2 + 1.1)
       + 0.12 * np.sin(2 * np.pi * 5.9 * t2 + 0.5))
env = np.clip(env, 0.04, None)
env = env / env.max()          # normalize the envelope peak to 1
rf = env * np.sin(2 * np.pi * 60 * t2)
avg_power = np.mean(env ** 2)  # average power ~ mean of envelope^2

axr.plot(t2, rf, color=INK, linewidth=0.5, alpha=0.75)
axr.plot(t2, env, color=INK, linewidth=2.0, linestyle=(0, (5, 3)))
axr.axhline(1.0, color=INK, linewidth=1.4)
axr.axhline(avg_power, color=INK, linewidth=1.3, linestyle=(0, (2, 2.5)))
axr.annotate("PEP = $V_{pp}^2\\,/\\,(8R)$",
             xy=(env.argmax() / 2400, 1.0), xytext=(0.03, 1.14),
             fontsize=10, color=INK, ha="left", va="bottom",
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axr.text(0.5, -1.17, "dashed: average voice power — it sits well below PEP",
         fontsize=9.5, color=INK, ha="center", va="bottom", style="italic")
axr.set_xlim(0, 1)
axr.set_ylim(-1.30, 1.50)
axr.set_xticks([])
axr.set_yticks([-1, -0.5, 0, 0.5, 1])
axr.set_xlabel("time — a second of speech", fontsize=10, color=INK)
axr.set_ylabel("RF voltage (normalized)", fontsize=10, color=INK)
axr.set_title("SSB: PEP lives at the envelope peak", fontsize=11.5, color=INK)

for ax in (axl, axr):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(INK)
    ax.tick_params(colors=INK, labelsize=9.5)
    ax.grid(axis="y", color=INK, alpha=0.15, linewidth=0.7)

fig.text(0.5, 0.033,
         "the pool's drill: 17 V peak ≈ 12 V RMS · 120 V RMS ≈ 339.4 V p-p",
         fontsize=9.5, color=INK, ha="center", va="bottom", style="italic")
fig.text(0.5, 0.003,
         "PEP into 50 Ω: 200 V p-p → 100 W · 500 V p-p → 625 W · "
         "unmodulated carrier: PEP = average (ratio 1.00)",
         fontsize=9.5, color=INK, ha="center", va="bottom", style="italic")

fig.tight_layout(rect=[0, 0.06, 1, 0.93])

out = "figures/ch05-rms-peak-pep.svg"
fig.savefig(out, transparent=True, bbox_inches="tight")

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
