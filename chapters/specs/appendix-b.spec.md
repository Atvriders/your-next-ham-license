# Writer Spec — Appendix B. Glossary & Formulas

**Output file:** `appendices/glossary-and-formulas.md` (this exact filename — the audit's TOC check #3 looks for it)
**Target length:** reference material, excluded from the prose target; the glossary alone is 402 entries × one line.
**Pool coverage:** none — no pool quotes required here. Content comes from canon §4 (glossary) and canon §3 (notation & units), which are binding.

## 1. Purpose

The upgrading ham's back-of-book reference: every term the book uses, defined plainly in one line, plus the General course's formula set — each formula with a worked micro-example using the pool's own numbers. Not narrated in the audiobook (chapters 00–10 only).

## 2. Structure

- First line: `## Appendix B: Glossary & Formulas` (appendices are exempt from the chapter format laws — the audit's `check_format_laws` only applies to `chNN` stems — but keep the `## Appendix …` heading shape for the TOC; the colon form mirrors Book 2's shipped appendix).
- One short intro paragraph: how to use the appendix (definitions match the chapters; formulas carry micro-examples with the pool's own numbers).
- `### Glossary` — the full table from canon §4.
- `### Formulas` — the canon §3 General formula set with micro-examples (§4 below).
- `### Notation & Units` — the short note block (§5 below).

## 3. The glossary (`### Glossary`)

- **Source is canon §4 and only canon §4.** It carries **402 terms** as `| Term | Definition |` — consolidate them into this appendix **byte-exact**, terms alphabetical as published (the canon table is already A→Z, running "A-index" through "Zero beat").
- Keep the canon's one-line definitions verbatim — they are binding (canon §4: "a chapter may expand a definition but must not contradict it"). Do not add terms of your own, do not drop any, do not reword.
- Format: a two-column markdown table (`| Term | Definition |` with the `|---|---|` separator) mirrors the canon and renders cleanly in the build. Group-letter subheadings (A, B, C …) are optional; if used, they are plain bold lines, not `####` headings, so the TOC stays flat.
- Sanity check before finishing: the row count is exactly 402 and a `diff` of the two tables shows no wording drift (mechanical copy, not retype — watch the µ in "µV" entries, the en dashes in ranges, and the curly apostrophes).

## 4. The formulas (`### Formulas`)

Present each relation from canon §3's General formula set with a one-line plain statement and a worked micro-example using the pool's own numbers. Cover exactly these (the book's complete formula set — nothing more, nothing less):

| Formula | Plain statement | Micro-example (pool numbers) |
|---|---|---|
| **V = I × R** (Ohm's law) | Voltage equals current times resistance; rearranged I = V / R, R = V / I. (Book 2 carry-over.) | 12 V across a resistor with 1.5 A through it: R = 12 ÷ 1.5 = 8 Ω. |
| **P = V × I = I² × R = V² / R** | The three DC power forms. | 400 VDC across 800 Ω: 400² ÷ 800 = 200 W (G5B03); 12 V × 0.2 A = 2.4 W (G5B04); 7.0 mA through 1,250 Ω ≈ 61 mW (G5B05). |
| **λ(m) = 300 / f(MHz)** | Wavelength in meters equals 300 divided by frequency in megahertz — the pool's own approximation of λ = c / f with c ≈ 3×10⁸ m/s, never an exact identity. (Book 2 carry-over.) | 300 ÷ 14.250 ≈ 21 m — the 15-meter band's neighbor, 20 m, sits at 14 MHz. |
| **Prefix ladder** | pico (10⁻¹²) → nano (10⁻⁹) → micro (10⁻⁶) → milli (10⁻³) → base → kilo (10³) → mega (10⁶) → giga (10⁹); toward a smaller unit multiply, toward a larger unit divide. | G5C08's own drill: 5 nF + 5 nF + 750 pF = 10.750 nF. |
| **X_L = 2πfL** | Inductive reactance rises with frequency. | 20 mH at 7 MHz ≈ 880 kΩ; the same inductor at 60 Hz ≈ 7.5 Ω (G5A05 concept, G5C11 numbers). |
| **X_C = 1/(2πfC)** | Capacitive reactance falls with frequency. | 100 µF at 60 Hz ≈ 26.5 Ω (G5A06 concept, G5C09 numbers). |
| **f = 1/(2π√(LC))** | Resonant frequency of an LC combination. | 10 mH with 100 µF ≈ 159 Hz (G5C10 with G5C09). |
| **X_L = X_C at resonance** | The reactances cancel: series LC → very low impedance; parallel LC → very high. | G5A01, G5A12 (concept row — no numbers). |
| **\|Z\| = √(R² + X²); φ = arctan(X/R)** | Impedance magnitude and phase from resistance and reactance. | 50 Ω + j50 Ω → \|Z\| ≈ 70.7 Ω, φ = 45°. |
| **V_rms = V_peak/√2 ≈ 0.707·V_peak** | RMS of a sine — the AC value that heats like the same-value DC. | 17 V peak ≈ 12 V RMS (G5B09). |
| **V_pp = 2√2·V_rms ≈ 2.828·V_rms** | Peak-to-peak of a sine. | 120 V RMS ≈ 339.4 V peak-to-peak (G5B08). |
| **PEP = V_pp²/(8R)** | Peak envelope power from peak-to-peak voltage. | 200 V p-p across 50 Ω → 100 W (G5B06); 500 V p-p → 625 W (G5B14). |
| **dB = 10·log₁₀(P₂/P₁)** | The decibel definition — first-class exam math in this book. | ×2 ≈ 3 dB (G5B01); a 1 dB loss leaves 10^(−0.1) = 0.794 of the power (G5B10); 20 dB = ×100 (G4D05). |
| **SWR = Z_load ÷ Z₀ (or inverse, ≥ 1)** | SWR from a resistive mismatch, larger number first. | 200 Ω on 50 Ω → 4:1 (G9A09); 10 Ω on 50 Ω → 5:1 (G9A10). |
| **SWR = (1+√(P_r/P_f))/(1−√(P_r/P_f))** | SWR from forward and reflected power (the directional wattmeter's job). | Stated with G4B10 — concept row; one worked ratio may be shown (e.g., P_r/P_f = 1/9 → SWR = 2:1). |
| **L(ft) = 468 / f(MHz)** | Approximate half-wave dipole length (includes ~5 % end-effect shortening). | 14.250 MHz → ≈ 33 ft (G9B10); 3.550 MHz → ≈ 132 ft (G9B11). |
| **L(ft) = 234 / f(MHz)** | Approximate quarter-wave monopole length. | 28.5 MHz → ≈ 8 ft (G9B12). |
| **dBi = dBd + 2.15** | Gain referenced to isotropic vs to a dipole — dBi is the bigger number. | A 5 dBd Yagi = 7.15 dBi (G9C04). |
| **BW ≈ 2 × (peak deviation + highest modulating frequency)** | Carson's rule (FM bandwidth). | 2 × (5 kHz + 3 kHz) = 16 kHz (G8B06). |
| **Deviation multiplies by the chain factor** | Deviation through a frequency-multiplier chain scales like the carrier. | 146.52 ÷ 12.21 = 12 → 5 kHz ÷ 12 = 416.7 Hz (G8B07). |
| **V_s = V_p × (N_s/N_p)** | Transformer voltage ratio follows turns ratio. | 120 V, 500→1500 turns → 360 V (G5C06). |
| **Z_p/Z_s = (N_p/N_s)²** | Impedance transforms as the square of the turns ratio. | 600 Ω:50 Ω = 12:1 → turns √12 ≈ 3.5:1 (G5C07). |
| **Series/parallel combinations** | R and L add in series, add-by-reciprocals in parallel; C does the opposite. | 10‖20‖50 Ω ≈ 5.9 Ω (G5C03); three 10 mH parallel = 3.3 mH (G5C10); three 100 µF series = 33.3 µF (G5C09). |
| **n bits → 2ⁿ states** | Binary counter state count. | 2³ = 8 (G7B05). |
| **η = P_RF-out ÷ P_DC-in** | Amplifier efficiency (definition). | 100 W RF from 138 W DC ≈ 72 % (G7B08 concept). |
| **Full-wave ripple = 2 × line frequency** | Why full-wave is easier to filter. | 60 Hz mains → 120 Hz ripple (G7A07). |

## 5. The notation block (`### Notation & Units`)

A short note block carrying the canon §3 laws a reader will meet in the pool and the book:

- This book's prose uses **V** for voltage and **×** for multiplication (V = I × R), exactly as Book 2 does. The 2023–2027 General pool states electrical quantities in **words** ("200 volts peak-to-peak across a 50-ohm dummy load") — no formula typography occurs anywhere in the pool text, so verbatim quotes never conflict. E and V both mean volts (Book 2's equivalence, one parenthetical).
- Unit case is load-bearing: **kHz** (lowercase k), **MHz**/**GHz** (capital M/G), always capital H; **mA**, **µV**, **pF**, **nF**, **kV** follow the same prefix case rules.
- c = 3×10⁸ m/s = 300,000 km/s is the working value; f = 1/T.
- Antenna lengths from 468/f and 234/f come out in **feet** and are approximate; coax loss is quoted in **dB per 100 feet**; hop distances in **miles**; SWR is always written larger-number-first ("4:1").
- Inline math in this appendix uses the same `$…$` style as the chapters where an expression is displayed — at most one `$…$` span per paragraph.

## 6. Integrity notes

- Appendices are exempt from the chapter format laws (no Exam Focus, no Key Takeaways, no FACT-line requirement) — but banned phrases still apply nowhere ("little did they know", "in that moment", "a testament to").
- Everything here traces to canon §3/§4 or to pool numbers already pinned in the canon — introduce no new facts, no new terms, no new formulas.
- Alphabetization, spelling, and punctuation of terms match the canon byte-exactly; the formula micro-examples use the pool's own numbers exactly as pinned in canon §3's formula table.
