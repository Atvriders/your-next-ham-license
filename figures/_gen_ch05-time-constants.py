"""Generate figures/ch05-time-constants.svg — RC and RL time constants.

The time constant tau sets how fast energy moves in and out of storage:
capacitor voltage charges toward the supply with tau = R x C, reaching 63%
after one tau and 99%+ by five tau; discharging falls to 37% after one tau.
Inductor current builds on the same clock with tau = L / R. This store-and-
release is the mechanism behind the G5A concept family: inductors and
capacitors oppose AC by storing and returning energy, never by dissipating
it. (The 2023-2027 General pool tests no time-constant arithmetic; this
figure underpins the reactance concepts of G5A02-A06.)

Single-color (black) matplotlib output on a transparent background, then
post-processed: every #000000 becomes currentColor (established pattern from
Book 2's figures/_gen_*.py and this repo's _gen_ch01-general-band-chart.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "black"

t = np.linspace(0, 5, 400)     # time in units of tau
rise = 1 - np.exp(-t)          # charging / current build-up
fall = np.exp(-t)              # discharging / current decay

fig, (axl, axr) = plt.subplots(1, 2, figsize=(8.8, 4.5))
fig.suptitle("The Time Constant τ — How Fast L and C Store and Release Energy",
             fontsize=13.5, color=INK)


def style(ax):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(INK)
    ax.tick_params(colors=INK, labelsize=9.5)
    ax.grid(color=INK, alpha=0.15, linewidth=0.7)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel("time, in time constants (τ)", fontsize=10, color=INK)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])


# ---- left: capacitor voltage, tau = R x C -----------------------------------
axl.plot(t, rise, color=INK, linewidth=2.4, solid_capstyle="round",
         label="charging")
axl.plot(t, fall, color=INK, linewidth=2.0, linestyle=(0, (5, 3)),
         label="discharging")
axl.axvline(1, color=INK, linewidth=1.0, linestyle=(0, (2, 3)), alpha=0.5)
axl.plot([1, 1], [0.632, 0.368], marker="o", markersize=7, color=INK)
axl.annotate("after 1τ: 63% of the supply", xy=(1, 0.632),
             xytext=(1.9, 0.78), fontsize=10, color=INK,
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axl.annotate("after 1τ: 37% left", xy=(1, 0.368),
             xytext=(2.1, 0.22), fontsize=10, color=INK,
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axl.text(4.95, 0.90, "by 5τ: effectively full (99%+)", fontsize=9.5,
         color=INK, ha="right", va="top", style="italic")
axl.set_ylabel("capacitor voltage, % of supply", fontsize=10, color=INK)
axl.set_title("Capacitor voltage — τ = R × C", fontsize=11.5, color=INK)
axl.legend(loc="center right", fontsize=9.5, frameon=False,
           labelcolor=INK, bbox_to_anchor=(1.0, 0.42))
style(axl)

# ---- right: inductor current, tau = L / R -----------------------------------
axr.plot(t, rise, color=INK, linewidth=2.4, solid_capstyle="round",
         label="current builds")
axr.plot(t, fall, color=INK, linewidth=2.0, linestyle=(0, (5, 3)),
         label="current decays")
axr.axvline(1, color=INK, linewidth=1.0, linestyle=(0, (2, 3)), alpha=0.5)
axr.plot([1, 1], [0.632, 0.368], marker="o", markersize=7, color=INK)
axr.annotate("after 1τ: 63% of the final current", xy=(1, 0.632),
             xytext=(1.9, 0.78), fontsize=10, color=INK,
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axr.annotate("after 1τ: 37% left", xy=(1, 0.368),
             xytext=(2.1, 0.22), fontsize=10, color=INK,
             arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
axr.set_ylabel("inductor current, % of final value", fontsize=10, color=INK)
axr.set_title("Inductor current — τ = L / R", fontsize=11.5, color=INK)
axr.legend(loc="center right", fontsize=9.5, frameon=False,
           labelcolor=INK, bbox_to_anchor=(1.0, 0.42))
style(axr)

fig.text(0.5, 0.005,
         "energy moves in and out on the τ clock — reactance stores and "
         "returns energy, never dissipates it",
         fontsize=10, color=INK, ha="center", va="bottom", style="italic")

fig.tight_layout(rect=[0, 0.045, 1, 0.93])

out = "figures/ch05-time-constants.svg"
fig.savefig(out, transparent=True, bbox_inches="tight")

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)
