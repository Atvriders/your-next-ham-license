# R4 Teaching Notes — Subelements G6–G0 (General pool 2023–2027)

Researcher: R4. Source: `canon/pool-general.json` (423 questions; 174 owned here). Audience: chapter writers. Teaching voice: a
licensed Technician upgrading to General — assume Ohm's law, basic components, VHF operating habits; assume nothing about
amplifier classes, transmission-line theory, or RF exposure rules.

**Basis notation:** `[TB]` = standard textbook canon (ARRL Handbook / license-manual theory); `[§…]` = FCC rule citation carried
on the pool's own ID line in `canon/pool-general.txt`; `[FACT]` = pure-memorization value, pin as a FACT line.

**Group map (174 questions):**

| Subelement | Group | Count | IDs | Theme |
|---|---|---|---|---|
| G6 Circuit components | G6A | 12 | G6A01–G6A12 | Component behavior & characteristics |
| | G6B | 11 | G6B01–G6B08, G6B10–G6B12 | ICs, ferrites, connectors |
| G7 Practical circuits | G7A | 13 | G7A01–G7A13 | Power supplies; figure G7-1 |
| | G7B | 11 | G7B01–G7B11 | Amplifiers, oscillators, digital |
| | G7C | 14 | G7C01–G7C14 | Filters, detectors, SDR |
| G8 Signals & emissions | G8A | 14 | G8A01–G8A14 | Modulation types |
| | G8B | 13 | G8B01–G8B13 | Mixing, bandwidth, deviation |
| | G8C | 15 | G8C02–G8C16 | Digital modes |
| G9 Antennas & feedlines | G9A | 11 | G9A01–G9A11 | Transmission lines & SWR |
| | G9B | 12 | G9B01–G9B12 | Basic antennas & patterns |
| | G9C | 11 | G9C01–G9C05, G9C07–G9C12 | Yagis & directional antennas |
| | G9D | 12 | G9D01–G9D12 | Specialized antennas |
| G0 Safety | G0A | 12 | G0A01–G0A12 | RF exposure |
| | G0B | 13 | G0B01–G0B13 | Electrical & antenna safety |

**Numbering gaps (errata deletions — do not hunt for these):** G6B09, G8C01, G9C06 do not exist in the 2023–2027 pool. All other
IDs in each range are present.

---

## G6 — Circuit components (23)

### Topic inventory
- **G6A (12):** batteries ×2 (G6A01–G6A02), diode thresholds ×2 (G6A03, G6A05), capacitor types ×2 (G6A04, G6A08),
  resistor/inductor parasitics ×2 (G6A06, G6A11), transistor and tube structure/operating points ×4 (G6A07, G6A09, G6A10, G6A12).
- **G6B (11):** ferrites ×3 (G6B01, G6B05, G6B10), IC families ×3 (G6B02, G6B03, G6B06), RF connectors ×4 (G6B04, G6B07, G6B11,
  G6B12), LED bias ×1 (G6B08).

### What the reader must understand
- **Batteries:** a "12-volt" lead-acid battery is flat well above 0 V — discharging below **10.5 V** shortens its life (G6A01)
  `[FACT/TB]`. Internal resistance acts like a series resistor inside the battery; lower resistance means less voltage sag under
  load, hence **higher available discharge current** (G6A02) `[TB]`.
- **Diode thresholds:** a diode needs a minimum forward voltage to conduct: **germanium ≈ 0.3 V** (G6A03), **silicon ≈ 0.7 V**
  (G6A05) `[FACT/TB]`. An LED is a diode that emits light **when forward biased** (G6B08) `[TB]`.
- **Capacitor personalities:** electrolytics pack **high capacitance into a small volume** but are leaky, loose-tolerance,
  polarized, and not for RF (G6A04); low-voltage ceramics are above all **cheap** (G6A08) `[TB]`. Neither is "precise" — that's
  the trap.
- **Parasitics:** a wire-wound resistor is a coil — its **inductance** makes RF behavior unpredictable (G6A06). An inductor's
  winding capacitance creates a self-resonant frequency; **above** it the part **becomes capacitive** (G6A11) `[TB]`.
- **Transistors/tubes:** a BJT used as a switch lives at its endpoints — **saturation (fully on) and cutoff (fully off)** (G6A07).
  A MOSFET's gate is **insulated from the channel by a thin insulating layer** (G6A09). In a vacuum tube the **control grid**
  meters electron flow from cathode to plate (G6A10); the **screen grid** exists to **reduce grid-to-plate capacitance** (G6A12)
  `[TB]`.
- **Ferrites:** the material **"mix"** sets the frequency range where a core works (G6B01); ferrite toroids give large inductance,
  frequency-optimized cores, and self-contained fields — all three (G6B05); a ferrite bead on coax chokes **common-mode** shield
  current by **putting impedance in that current's path** (G6B10) `[TB]`.
- **ICs:** MMIC = **Monolithic Microwave Integrated Circuit** (G6B02) `[FACT]`; CMOS beats TTL on **power consumption** (G6B03);
  an op-amp is an **analog** IC (G6B06) `[TB]`.
- **Connectors (all `[FACT]`):** BNC — bayonet, low-SWR use to about **4 GHz** (G6B04); type N — **moisture-resistant, useful to
  10 GHz** (G6B07); SMA — **small threaded**, good to several GHz (G6B11); **RCA phono** is the non-RF connector used for
  low-frequency/DC connections to a transceiver (G6B12).

### Common confusions
- G6A03 vs G6A05 deliberately share the option set (0.1 / 0.3 / 0.7 / 1.0); each answer is the other's distractor. Teach as a
  pair: **Ge 0.3, Si 0.7**.
- G6A04 vs G6A08: "high capacitance for volume" belongs to the *electrolytic*; the ceramic answer is "low cost." The pool swaps
  these.
- G6A07: the "active region" is where a *linear* transistor lives; a *switch* uses the endpoints only.
- G6B12: PL-259/BNC/N are all RF connectors; the question wants the non-RF one (RCA phono).

### Vocabulary (glossary)
internal resistance, forward threshold voltage, electrolytic capacitor, ceramic capacitor, self-resonant frequency, saturation,
cutoff, MOSFET, control grid, screen grid, ferrite mix, toroid, common-mode current, MMIC, CMOS, TTL, op-amp, BNC, type N, SMA,
RCA phono.

### Math required
None beyond reading volts; threshold values are memorized (0.3 / 0.7 V).

### Watch items `[FACT]`
10.5 V minimum discharge (G6A01); Ge 0.3 V / Si 0.7 V (G6A03, G6A05); BNC 4 GHz (G6B04); type N 10 GHz (G6B07); MMIC expansion
(G6B02). G6B09 does not exist.

---

## G7 — Practical circuits (38)

### Topic inventory
- **G7A (13):** power-supply circuits ×8 (G7A01–G7A08), figure G7-1 symbols ×5 (G7A09–G7A13).
- **G7B (11):** amplifier classes & linearity ×5 (G7B01, G7B02, G7B04, G7B10, G7B11), efficiency ×1 (G7B08), oscillators ×2
  (G7B07, G7B09), digital basics ×3 (G7B03, G7B05, G7B06).
- **G7C (14):** SSB generation/detection ×3 (G7C01, G7C02, G7C04), filter terminology ×4 (G7C07, G7C12–G7C14), receiver
  sensitivity ×1 (G7C08), DDS/DSP ×2 (G7C05, G7C06), SDR/I-Q ×3 (G7C09–G7C11), impedance matching ×1 (G7C03).

### What the reader must understand
- **Power supplies (G7A, all `[TB]`):** rectifiers turn AC into pulsed DC. A **half-wave** rectifier uses **one diode** and
  converts **180°** of each cycle (G7A04, G7A05); a **full-wave** rectifier converts **360°** (G7A06), so its unfiltered output is
  **DC pulses at twice the AC line frequency** (G7A07) — the fact that explains why full-wave is easier to filter. The
  **center-tapped full-wave** circuit uses **two diodes and a center-tapped transformer** (G7A03). Filters are built from
  **capacitors and inductors** (G7A02). A **bleeder resistor discharges the filter capacitors when power is removed** — a safety
  device (G7A01). A **switchmode** supply chops at high frequency, which is what allows **smaller, lighter components** (G7A08).
- **Amplifier classes (G7B, `[TB]`):** class describes what fraction of the cycle the device conducts. **Class A conducts 100 %**
  (G7B04) — linear but inefficient. **Class C has the highest efficiency** (G7B02) but distorts amplitude, so it suits constant-
  envelope modes only: **FM yes; SSB/AM no** (G7B11). A **linear amplifier preserves the input waveform** (G7B10) — required for
  SSB. **Neutralizing** cancels internal feedback to **eliminate self-oscillation** (G7B01). Efficiency = **RF output ÷ DC input
  power** (G7B08).
- **Oscillators (G7B, `[TB]`):** a sine-wave oscillator = **a filter plus an amplifier in a feedback loop** (G7B07); an **LC**
  oscillator's frequency is set by the **tank-circuit inductance and capacitance** (G7B09).
- **Digital basics (G7B, `[TB]`):** an AND gate's output is high **only when both inputs are high** (G7B03); a 3-bit counter has
  **2³ = 8 states** (G7B05); a shift register is a **clocked array passing data along in steps** (G7B06).
- **SSB chain (G7C, `[TB]`):** a **balanced modulator** produces **double-sideband suppressed-carrier** RF (G7C02); a **filter**
  strips one sideband to make SSB (G7C01); a **product detector** recovers the audio in an SSB receiver (G7C04).
- **Filter vocabulary (G7C, `[TB]`):** **insertion loss** = attenuation *inside* the passband (G7C07); **cutoff frequency** = the
  half-power point of a low-pass filter (G7C12); **ultimate rejection** = maximum stopband rejection (G7C13); band-pass bandwidth
  is measured between the **upper and lower half-power frequencies** (G7C14).
- **Receivers & SDR (G7C, `[TB]`):** sensitivity depends on input gain, demodulator bandwidth, and noise figure — all of them
  (G7C08). DDS gives **variable frequency with crystal-oscillator stability** (G7C05). DSP filters realize **many bandwidths and
  shapes** an analog filter can't (G7C06). In SDR the **I and Q signals are 90° apart** (G7C09); I/Q processing lets software
  create **any modulation type** (G7C10), and filtering, detection, and modulation all happen in software (G7C11).

### ★ Figure G7-1 (G7A09–G7A13) — precise description for the SVG redraw

Source inspected: `canon/source/G7-1.pdf` rendered at 200 dpi (2203×1703 px); every numbered symbol verified by close-up crops and
cross-checked against the pool answers. This is the only figure in the owned subelements.

**Overall:** a black-and-white line schematic of a **two-stage circuit — a variable-frequency oscillator (left, built around the
FET) feeding an amplifier/buffer stage (right, built around the NPN transistor)** — with a single +DC supply rail across the top
and an RF output terminal at the right. Open-circle terminals labeled **“+DC”** (top right) and **“OUT”** (right). Caption
**“Figure G7-1”** centered beneath. **Ground symbols are three slanted (diagonal) strokes of decreasing length, longest on top** —
same style as the Tech book's T-1/T-2/T-3 redraws. Unnumbered support parts (bias resistors, bypass and coupling capacitors, a
series resistor in the +DC rail) appear as in any discrete two-stage design; only the 11 numbered symbols are exam-relevant.

**Numbered symbols** (identity — position in drawing — asked by):
- **1 = field effect transistor (N-channel JFET)** — center; circle containing a vertical channel bar, gate lead entering from the
  left with a **filled arrowhead pointing inward (right) into the channel**; top of channel wired up toward the +DC rail, bottom
  of channel wired down toward the tapped inductor. **Asked by G7A09 (answer C).**
- **2 = NPN junction transistor** — right-center; circle with vertical base bar on its left half, base lead from the left,
  collector line exiting the top to the transformer primary, emitter line exiting downward with a **filled arrowhead pointing
  outward / down-right, away from the base** (“Not Pointing iN” = NPN); label “2” to the right. **Asked by G7A11 (answer B).**
- **3 = ordinary PN junction diode** — left of symbol 1, vertical branch to ground; **filled triangle pointing DOWN** onto a
  horizontal cathode bar (anode top). Not asked.
- **4 = varactor diode** — far left, vertical; filled triangle pointing UP into a straight cathode bar with a **curved
  (arc-shaped) second plate above it** — diode-plus-capacitor = voltage-variable capacitor, used for tuning. Not asked.
  (Distractor magnet: looks almost like a Zener — see G7A10's option A.)
- **5 = Zener diode** — top center-right, shunt from the +DC rail to ground; filled triangle pointing UP into a cathode bar whose
  **two ends are bent diagonally into the classic “Z” wings**. **Asked by G7A10 (answer D).**
- **6 = solid-core transformer** — right; primary coil (left, more humps) and secondary coil (right, fewer humps) separated by
  **two straight vertical core lines** (the solid/laminated core); secondary bottom grounded, secondary top to the OUT terminal.
  **Asked by G7A12 (answer C).**
- **7 = tapped inductor** — lower left; single vertical coil, bottom end grounded, with a **connection (tap) leaving the coil
  partway up** toward the right. **Asked by G7A13 (answer A).**
- **8 = polarized (electrolytic) capacitor** — top center, vertical shunt from +DC rail to ground; **one straight plate, one
  curved plate**. Not asked.
- **9 = fixed resistor** — lower right, vertical zigzag from the transistor-2 emitter node to ground (an unnumbered bypass
  capacitor parallels it). Not asked.
- **10 = polarized (electrolytic) coupling capacitor** — left-center, horizontal in the long gate/signal wire; one straight plate,
  one curved plate. Not asked.
- **11 = variable resistor** — upper left, vertical zigzag between the +DC feed and the left-hand circuitry, with a **diagonal
  arrow drawn through the zigzag**. Not asked.

**Question→position map:** G7A09→1 (FET); G7A10→5 (Zener); G7A11→2 (NPN); G7A12→6 (solid-core transformer); G7A13→7 (tapped
inductor). The five questions raid each other: options come from {1, 2, 4, 5, 6, 7, 11}, so partial knowledge still faces
plausible distractors. Teaching strategy: drill all 11 as one symbol-recognition table; the three diode variants (3 plain / 4
varactor / 5 Zener) are the discrimination students miss.

### Common confusions (G7, non-figure)
- G7A05 vs G7A06 (180° vs 360°) and G7A07 (twice line frequency) are one idea — teach as a unit; distractors swap the numbers
  between half- and full-wave.
- G7A03: a “full-wave bridge” uses **four** diodes; two diodes + center-tap = plain “full-wave.”
- G7B02/G7B11: highest efficiency (class C) does **not** mean usable for SSB — constant-envelope only.
- G7B01: neutralization kills self-oscillation; it has nothing to do with modulation.
- G7C07 vs G7C13: insertion loss is *inside* the passband; ultimate rejection is *outside*.

### Vocabulary (glossary)
bleeder resistor, half-wave rectifier, full-wave rectifier, center-tapped transformer, ripple frequency, switchmode power supply,
neutralization, class A / AB / B / C amplifier, linear amplifier, efficiency, tank circuit, AND gate, binary counter, shift
register, balanced modulator, product detector, DDS, DSP filter, insertion loss, cutoff frequency, ultimate rejection, half-power
point, I and Q signals, SDR.

### Math required
- **Counter states:** n bits → 2ⁿ states. G7B05: 2³ = **8**.
- **Amplifier efficiency:** η = P_RF-out ÷ P_DC-in (G7B08) — definition only, no numbers.
- **Ripple frequency:** full-wave ripple = 2 × line frequency (G7A07, conceptual).

### Watch items `[FACT]`
180°/360° conduction (G7A05–G7A06); class A = 100 % conduction (G7B04); 2-diode center-tap = full-wave (G7A03); I/Q = 90° (G7C09);
figure symbols 1/2/5/6/7 (G7A09–G7A13).

---

## G8 — Signals and emissions (42)

### Topic inventory
- **G8A (14):** modulation definitions ×5 (G8A01–G8A05), digital modulation ×3 (G8A06, G8A09, G8A12), AM characteristics ×4
  (G8A07, G8A08, G8A10, G8A11), link budget/margin ×2 (G8A13, G8A14).
- **G8B (13):** mixer/superhet behavior ×4 (G8B01–G8B03, G8B11), frequency multiplication ×1 (G8B04), intermodulation ×3 (G8B05,
  G8B12, G8B13), FM bandwidth ×2 (G8B06, G8B07), duty cycle/bandwidth/symbol rate ×3 (G8B08–G8B10).
- **G8C (15):** mode identification ×5 (G8C02, G8C07, G8C08, G8C12, G8C16), protocol mechanics ×5 (G8C03–G8C06, G8C10), mesh ×1
  (G8C09), FSK/waterfall/report terms ×4 (G8C11, G8C13–G8C15).

### What the reader must understand
- **The three modulations (G8A, `[TB]`):** AM varies the signal's **amplitude/instantaneous power** (G8A05); FM varies its
  **instantaneous frequency** (G8A03); PM varies its **phase angle** (G8A02). Direct FSK means the digital signal **drives the
  oscillator frequency itself** (G8A01). A **reactance modulator** attached to an **RF amplifier stage** (after the oscillator)
  produces **phase modulation** (G8A04) — the pool's subtlest modulation question; teach as “reactance stage after the oscillator
  = PM.”
- **AM specifics (G8A, `[TB]`):** the **modulation envelope** is the outline made by **connecting the peaks** of the RF waveform
  (G8A11). Overdriving flattens the peaks — **flat-topping**, distortion from **excessive drive or speech levels** (G8A10) — and
  overmodulation splatters: **excessive bandwidth** (G8A08). Among phone emissions, **SSB is the narrowest** (G8A07).
- **Digital modulation (G8A):** QPSK sends data as **0°/90°/180°/270° phase shifts, two bits per symbol** (G8A12) `[TB]`; QPSK31
  is sideband-sensitive, has error correction, and fits about the same bandwidth as BPSK31 — all three (G8A06) `[FACT]`. **FT8 =
  8-tone FSK** (G8A09) `[FACT]`.
- **Link arithmetic (G8A, `[TB]`):** a **link budget** adds transmit power and antenna gains and subtracts all losses, as seen at
  the receiver (G8A13); **link margin** = received level minus the minimum the receiver needs (G8A14).
- **Mixers (G8B, `[TB]`):** mixing two signals = **heterodyning** (G8B03); a mixer outputs the **sum and difference** of LO and RF
  (G8B11); a superhet is tuned by varying the **local oscillator** (G8B01). The **image** is an unwanted response **twice the IF
  away** from the desired signal (G8B02). A **multiplier** stage outputs a harmonic of its input — how a VHF FM transmitter
  reaches its operating frequency (G8B04).
- **Intermodulation (G8B, `[TB]`):** signals combining in a **non-linear** circuit spawn spurious products = **intermodulation**
  (G8B12). A product's “order” is the sum of its mixing coefficients; **odd-order** products land **closest** to the original
  frequencies (G8B05), and **2F1 − F2** is the odd-order example (order 3) (G8B13).
- **Duty cycle & bandwidth (G8B, `[TB]`):** high-duty-cycle modes (FT8, RTTY, FM) run the transmitter hard — average power can
  exceed ratings even when PEP is fine (G8B08). Matching receiver bandwidth to the mode gives the **best signal-to-noise ratio**
  (G8B09). **Higher symbol rate requires wider bandwidth** (G8B10).
- **Digital modes (G8C):** **WSPR** = weak-signal propagation beacon (G8C02) `[FACT]`; **FT8** decodes far below the noise (G8C07)
  and its “+3” report means **SNR of +3 dB in a 2.5 kHz bandwidth** (G8C15) `[TB]`; packet frames carry routing in the **header**
  (G8C03); **Baudot/RTTY = 5-bit code plus start and stop bits** (G8C04) `[FACT]`; ARQ: **NAK = please retransmit** (G8C05), and
  too many failed retries **drop the connection** (G8C06); **FEC sends redundant information with the data** (G8C10) `[TB]`;
  **PSK31 uses Varicode** — common letters get short codes, so **uppercase letters take longer** (G8C12, G8C08) `[FACT]`; FSK's
  two tones are **mark and space** (G8C11) `[FACT]`; mesh networks reroute around failed nodes (G8C09) `[TB]`; digital voice =
  **DMR, D-STAR, System Fusion** (G8C16) `[FACT]`.
- **Waterfall (G8C, `[TB]`):** axes are **frequency horizontal, signal strength as color/intensity, time vertical** (G8C14);
  **vertical lines flanking a signal = overmodulation** (G8C13).

### Common confusions
- G8A02/G8A03/G8A05 share invented distractors (“phase convolution,” “frequency transformation”) — teach the three definitions as
  one table.
- G8A04: the reflex answer “FM” is wrong precisely because the modulator follows the oscillator; flag it.
- G8B02: the image is 2× IF away, not 2× the signal frequency.
- G8B13: check coefficient sums — 5F1−3F2 is order 8 and 3F1−F2 is order 4 (both even); only 2F1−F2 (order 3) is odd.
- G8C13: vertical side lines mean **too much** modulation, not too little.
- G8C15: an FT8 report is SNR in a standardized 2.5 kHz bandwidth — not S-units, not “3× noise,” not dB over S9.

### Vocabulary (glossary)
AM/FM/PM, reactance modulator, FSK, mark and space, PSK, QPSK, modulation envelope, flat-topping, overmodulation, link budget,
link margin, heterodyning, mixer, local oscillator, IF, image response, multiplier, intermodulation, odd-order product, Carson's
rule, deviation, duty cycle, symbol rate, WSPR, FT8, PSK31, Varicode, Baudot code, ARQ, NAK, FEC, packet header, mesh network,
waterfall display, digital voice (DMR/D-STAR/System Fusion).

### Math required (exact formulas + worked pool examples)
- **Carson's rule (FM bandwidth):** BW ≈ 2 × (peak deviation + highest modulating frequency). Worked from G8B06: 2 × (5 kHz + 3
  kHz) = **16 kHz**.
- **Deviation through a multiplier chain:** deviation multiplies by the same factor as the carrier. Worked from G8B07: factor =
  146.52 MHz ÷ 12.21 MHz = 12, so oscillator deviation = 5 kHz ÷ 12 = **416.7 Hz**.
- **IMD order:** order = |coeff₁| + |coeff₂|. G8B13: 2F1 − F2 → 2 + 1 = 3 (odd).
- **dB concept:** FT8 reports are plain decibel SNR values in 2.5 kHz (G8C15); state once here that +3 dB ≈ double power — no
  further computation required.
- **Symbol rate vs bandwidth:** qualitative proportionality only (G8B10).

### Watch items `[FACT]`
FT8 = 8-tone FSK (G8A09); SSB narrowest phone mode (G8A07); image = 2× IF (G8B02); Baudot = 5 bits + start/stop (G8C04);
mark/space (G8C11); digital voice trio (G8C16); QPSK31 triple-truth (G8A06). G8C01 does not exist.

---

## G9 — Antennas and feedlines (46)

### Topic inventory
- **G9A (11):** feed-line impedance & loss ×5 (G9A01, G9A02, G9A05, G9A06, G9A11), SWR cause/effect ×6 (G9A03, G9A04,
  G9A07–G9A10).
- **G9B (12):** dipole/vertical patterns & impedance ×8 (G9B02–G9B09), antenna lengths ×3 (G9B10–G9B12), random wire ×1 (G9B01).
- **G9C (11):** Yagi structure & behavior ×7 (G9C01–G9C03, G9C05, G9C07, G9C09, G9C10), gain units ×1 (G9C04), pattern terms ×1
  (G9C08), matching devices ×2 (G9C11, G9C12).
- **G9D (12):** one specialized antenna per question — NVIS, end-fed, halo, traps, stacking, log-periodic ×2, screwdriver,
  Beverage, small loop, multiband, inverted V (G9D01–G9D12).

### What the reader must understand
- **Transmission lines (G9A, `[TB]`):** a parallel-conductor line's characteristic impedance is set by **conductor spacing
  (center-to-center) and conductor radius** — not length, not frequency (G9A01). Coax loss **rises with frequency** (G9A05) and is
  quoted in **dB per 100 feet** (G9A06) `[FACT]`. Reflected power comes from a **mismatch between feed-line and antenna feed-point
  impedance** (G9A04); to kill standing waves, **match the feed point to the line** (G9A07). Two subtle effects: high SWR makes a
  *lossy* line lose **more** (G9A02), and line loss makes SWR measured *at the shack end* look **better than it really is**
  (G9A11). **Window/ladder line ≈ 450 ohms** (G9A03) `[FACT]`. A tuner at the transmitter does **not** change the SWR on the feed
  line — it stays 5:1; the tuner only presents 1:1 to the radio (G9A08).
- **Basic antennas (G9B, `[TB]`):** a free-space dipole radiates a **figure-eight broadside to the wire** (nulls off the ends)
  (G9B04); a quarter-wave ground plane is **omnidirectional in azimuth** (G9B03). Height matters: below ½ wavelength a horizontal
  dipole's high-angle pattern goes **nearly omnidirectional** (G9B05) and its feed-point impedance **steadily decreases** toward
  0.1 λ height (G9B07). Moving the feed point from center toward the ends **raises** impedance (G9B08). Ground-plane radials
  **sloped downward** raise the ~35 Ω feed point toward 50 Ω (G9B02); radials for a ground-mounted vertical lie **on the surface
  or buried a few inches** (G9B06). Horizontal polarization's HF advantage is **lower ground losses** (G9B09). A random wire
  connected directly to the rig can put **significant RF current on station equipment** (G9B01).
- **Yagis (G9C, `[TB]`):** driven element ≈ **½ wavelength** (G9C02); **reflector longer, director shorter** than the driven
  element (G9C03); longer boom + more directors = **more gain** (G9C05); **front-to-back ratio** compares main-lobe power to the
  opposite direction (G9C07); **main lobe** = direction of maximum radiated field (G9C08); fatter elements widen bandwidth
  (G9C01); gain, F/B, and SWR bandwidth all trade off through boom length, element count, and spacing (G9C10); two Yagis stacked ½
  λ apart gain **≈ 3 dB** (G9C09). **dBi = dBd + 2.15** (G9C04) `[FACT]`. Matching: a **beta/hairpin** is a **shorted stub at the
  feed point** (G9C11); a **gamma match** needs **no insulation of the driven element from the boom** (G9C12).
- **Specialized antennas (G9D, `[TB]` unless noted):** NVIS = **horizontal dipole 0.1–0.25 λ up** for short-skip daytime 40 m
  (G9D01); end-fed half-wave feed-point impedance is **very high** (G9D02); a halo is **omnidirectional in its own plane**
  (G9D03); traps make one antenna **multiband** (G9D04) — and multiband antennas pay with **poor harmonic rejection** (G9D11);
  vertical stacking narrows the main lobe in **elevation** (G9D05); a log-periodic trades everything for **wide bandwidth**,
  element length and spacing varying **logarithmically** along the boom (G9D06, G9D07); a screwdriver antenna tunes by **varying
  base-loading inductance** (G9D08); a **Beverage** is a **directional receiving** antenna for MF/low HF (G9D09) `[FACT]`; an
  electrically small loop's nulls are **broadside to the loop** (G9D10); a dipole with a single central support is an **inverted
  V** (G9D12).

### Common confusions
- G9B04 vs G9D10: dipole maxima are **broadside to the wire**, but a small loop's **nulls** are broadside to the loop (loop maxima
  lie in the loop's plane) — students swap these. Draw both patterns.
- G9A08: the perennial trap — “the tuner fixed the antenna.” It didn't; the line still runs 5:1.
- G9C04: direction of the 2.15 — **dBi is the bigger number**.
- G9C03: reflector **longer** / director **shorter** — mnemonic “the reflector is the big one behind.”
- G9A09/G9A10: SWR is always stated **larger number first** (4:1, 5:1 — never 1:4, 1:5).
- G9D01: NVIS wants the antenna **low** (0.1–0.25 λ) — the opposite instinct from DX.

### Vocabulary (glossary)
characteristic impedance, SWR, reflected power, window line, attenuation (dB/100 ft), feed-point impedance, ground plane, radials,
figure-eight pattern, omnidirectional, NVIS, Yagi, driven element, reflector, director, boom, main lobe, front-to-back ratio, dBi,
dBd, stacking, beta/hairpin match, gamma match, trap antenna, log-periodic, screwdriver antenna, Beverage antenna, small loop,
inverted V, end-fed half-wave, random wire, halo.

### Math required (exact formulas + worked pool examples)
- **Half-wave dipole length (feet):** L = 468 ÷ f(MHz). G9B10: 468 ÷ 14.250 = 32.8 → **≈ 33 feet**. G9B11: 468 ÷ 3.550 = 131.8 →
  **≈ 132 feet**.
- **Quarter-wave monopole (feet):** L = 234 ÷ f(MHz). G9B12: 234 ÷ 28.5 = 8.2 → **≈ 8 feet**. (468 includes the ~5 % end-effect
  shortening; the exam only needs the formula and “approximate.”)
- **SWR from a resistive mismatch:** SWR = Z_load ÷ Z₀ or Z₀ ÷ Z_load, whichever is ≥ 1. G9A09: 200 Ω on 50 Ω → 200/50 = **4:1**.
  G9A10: 10 Ω on 50 Ω → 50/10 = **5:1**.
- **Gain units:** dBi = dBd + 2.15 (G9C04). **Stacking:** two identical antennas ≈ +3 dB (G9C09) — tie to “+3 dB doubles power.”
- **Smith chart: NOT in this pool.** Zero questions reference it (the 2023–2027 revision dropped the old Smith-chart items);
  chapters should not spend exam-prep space on it.

### Watch items `[FACT]`
window line ≈ 450 Ω (G9A03); dB per 100 feet (G9A06); dBi = dBd + 2.15 (G9C04); stack = +3 dB (G9C09); Beverage = directional
receiving (G9D09); 468/234 constants (G9B10–G9B12). G9C06 does not exist.

---

## G0 — Safety and RF exposure (25)

> **Chapter-split guidance:** G0A (12) is RF-exposure/MPE material; G0B (13) is shop,
> wiring, tower, and lightning safety. The two groups share no concepts — treat them in
> separate sections.

### G0A — RF exposure (12)
**Inventory:** RF effect on tissue (G0A01), exposure variables (G0A02), compliance methods (G0A03, G0A06, G0A08), time averaging
(G0A04), duty cycle (G0A07), exceeding limits (G0A05, G0A10), measurement (G0A09), antenna siting (G0A11), applicability (G0A12).

**What the reader must understand:**
- RF energy's established effect on tissue is **heating** — RF is non-ionizing, so ignore the "radiation poisoning" distractors
  (G0A01) `[TB]`. Exposure depends on **frequency, power density, and duty cycle — all three** (G0A02): frequency because the body
  absorbs some bands more efficiently, duty cycle because exposure averages over time `[TB]`.
- **Compliance (the rule core):** every station with time-averaged transmission over **one milliwatt** is subject to the rules
  (G0A12) `[§1.1307(1)(b)(3)(i)(A)]`. A station that doesn't meet the exemption criteria must **perform an exposure evaluation per
  FCC OET Bulletin 65** (G0A06) `[§97.13(c)(2), §1.1307(1)(b)(3)(i)]`. Acceptable ways to show compliance: **OET-65 calculation,
  computer modeling, or calibrated field-strength measurement — any of the three** (G0A03) `[§97.13(c)(1)]`. The ongoing duty:
  **evaluate routinely and keep people out of identified high-exposure areas** (G0A08) `[§97.13(c)(2)]`.
- **Time averaging** = total exposure averaged over a period (G0A04), which is why **a lower duty cycle permits higher power**
  (G0A07) `[TB]`.
- **If you exceed limits:** act to **prevent human exposure** — power down, raise the antenna, restrict access (G0A05)
  `[§97.13(c)(2), §1.1307(b)]`. If a directional antenna's main lobe could hit a neighbor's space, **ensure it can't be pointed at
  them while they're present** (G0A10); indoor antennas must keep occupied areas under MPE limits (G0A11) `[TB]`.
- **Measurement** requires a **calibrated field-strength meter with a calibrated antenna** — SWR meters and receivers don't
  qualify (G0A09) `[TB]`.

**Common confusions (G0A):** "All these choices are correct" is genuinely keyed on G0A02 and G0A03 but is a distractor on G0A05 —
teach content, not patterns. G0A01's distractors borrow ionizing-radiation language. G0A12's **1 milliwatt** is the
most-misremembered number in the subelement.

### G0B — Electrical & antenna safety (13)
**Inventory:** AC wiring/NEC (G0B01–G0B03, G0B06), GFCI (G0B05), lightning/grounding (G0B04, G0B11, G0B13), tower work (G0B07,
G0B08), shop hazards (G0B09, G0B10, G0B12).

**What the reader must understand:**
- **AC wiring:** in a 4-conductor 240 VAC circuit, **only the hot wires** get fuses or breakers — never the neutral or ground
  (G0B01) `[TB]`. Wire must handle the breaker: **20 A circuit → AWG 12 minimum** (G0B02) and **AWG 14 wire → 15 A fuse/breaker**
  (G0B03) `[FACT — NEC ampacity, NFPA 70]`. The **NEC covers the electrical safety of the station** — not bandwidth, not RF
  exposure (G0B06) `[TB]`. A **GFCI trips when current flows from a hot wire directly to ground** — the missing return current is
  what it detects (G0B05) `[TB]`.
- **Lightning & grounding:** the lightning-protection ground system goes **outside the building** (G0B04); arrestors mount **where
  feed lines enter the building** (G0B13); and **all ground rods must be bonded together** with the other premises grounds —
  separate "independent" grounds are the hazard (G0B11) `[TB/NEC]`.
- **Tower work:** confirm the harness is **rated for the climber's weight and within its service life** (G0B07); before climbing a
  tower with powered devices, **lock out and tag every circuit feeding the tower** (G0B08) `[TB]`.
- **Shop hazards:** generators run **in well-ventilated areas** — carbon monoxide is the killer (G0B09); lead-tin solder's danger
  is **lead contaminating food via unwashed hands** (G0B10); a power-supply **interlock removes dangerous voltages when the
  cabinet is opened** (G0B12) `[TB]`.

**Common confusions (G0B):** G0B11's right-angle-bend option inverts real guidance (avoid sharp bends — but the keyed answer is
bonding grounds together). G0B02/G0B03 are an inverse pair (breaker→wire vs wire→breaker): 20 A ↔ AWG 12, 15 A ↔ AWG 14. G0B09's
"insulate from ground" and "store fuel nearby" are both deliberately backwards. G0B01: fusing the neutral is the classic wrong
answer — if it blows first, chassis can sit at line voltage.

### Vocabulary (glossary)
MPE, OET Bulletin 65, time averaging, duty factor, power density, controlled/uncontrolled environment, field-strength meter, NEC
(NFPA 70), AWG, GFCI, hot/neutral/ground, interlock, lockout/tagout, lightning arrestor, ground-rod bonding, carbon monoxide, lead
solder hygiene.

### Math required
None computational. Two quantitative ideas only: duty factor as a multiplier on average exposure (G0A04, G0A07 — concept), and the
wire/ampacity number pairs `[FACT]`.

### Watch items `[FACT]`
1 mW applicability threshold (G0A12); OET Bulletin 65 by name (G0A03, G0A06); 20 A = AWG 12 (G0B02); AWG 14 = 15 A (G0B03);
grounds bonded together (G0B11); arrestors at the feed-line entry point (G0B13).

---

## Cross-subelement notes for writers
- **“All these choices are correct”** is the keyed answer 7 times in owned material (G0A02, G0A03, G6B05, G7C08, G7C11, G8A06,
  G9C10) and a distractor at least 7 times (G0A05, G0B05, G0B07–G0B09, G7A02, G7B11, G8C06…). Never teach pattern-guessing.
- **Subtle/flag-worthy questions:** G8A04 (reactance modulator after the oscillator → PM), G9A08 (tuner leaves line SWR
  unchanged), G9D10 (small-loop nulls are broadside), G0A12 (1 mW threshold), G7B11 (class C is fine for FM), G8B13 (only 2F1−F2
  is odd-order).
- **Missing IDs:** G6B09, G8C01, G9C06 (errata deletions). **No Smith-chart content anywhere in this pool.**

*Coverage: G6A, G6B, G7A (incl. figure G7-1), G7B, G7C, G8A, G8B, G8C, G9A, G9B, G9C,
G9D, G0A, G0B — all 14 owned groups, 174/174 questions referenced by ID. Verified with a citation script (every owned ID appears
in this file).*

