# Figure Plan — Your Next Ham License (General)

33 original figures across ch00–ch10. Canon is law (`accuracy-canon.md`); the G7-1 pool-figure redraw follows canon §1.4's binding component-level specification.

## Conventions (binding — identical to the Technician book)

- **Themeable:** strokes/fills/text use `currentColor`; **no hardcoded black/white**; transparent background; `viewBox` set; legible at ~600–800 px.
- **Hand-authored SVG** for diagrams/schematics; **matplotlib→SVG** for plots (generator saved as `figures/_gen_<id>.py`, post-process black→`currentColor`; see `/home/kasm-user/your-first-ham-license/figures/_gen_*.py` for the pattern).
- Style reference: the Tech book's figures at `/home/kasm-user/your-first-ham-license/figures/` (read 1–2).
- Ground symbols in the G7-1 redraw: three slanted strokes of decreasing length (canon §1.4).
- Metadata: `figures/fragments/<id>.json` — exactly `{"id", "chapter": <INT 0–10>, "caption", "kind": "original", "source", "spoken"}` (`figreg` accepts chapter 0–10 in this repo). `source` is `"original"` except the pool redraw: `"redrawn from NCVEC pool figure G7-1"`.
- Pool-facing numbers from canon/pool only (468/f and 234/f antenna formulas; dBi = dBd + 2.15; FT8 frequencies per canon §2 with their verification date).
- Numbering by **first-reference order** per chapter (assign at write time: the assembler re-checks).
- Self-check before finishing: XML-parse each SVG, render to PNG via `google-chrome --headless --screenshot`, view with ReadMediaFile, fix clipping/overlap/legibility.

## Figures

| # | id | ch | type | content |
|---|---|---|---|---|
| 1 | ch00-what-general-opens | 00 | SVG | Technician vs General privileges concept map: local VHF/UHF ↔ worldwide HF (phone/data segments light up) |
| 2 | ch00-upgrade-journey | 00 | SVG | Flow: pass Element 3 → CSCE + Form 605 → operate immediately with /AG (per canon §7.2 wording law) → ULS shows General → drop /AG |
| 3 | ch01-general-band-chart | 01 | plot | General HF privileges by band (80/60/40/30/20/17/15/12/10 m + VHF/UHF unchanged): phone/CW/data segments, 200 W PEP bands marked (canon §2 values only) |
| 4 | ch01-60m-structure | 01 | SVG | 60 m as it exists NOW (canon §7.1): contiguous 5351.5–5366.5 kHz @ 9.15 W ERP + four channels (5332/5348/5373/5405) @ 100 W ERP, 2.8 kHz max |
| 5 | ch01-ag-indicator | 01 | SVG | Call-sign with /AG indicator: what it means, when required (CSCE+605, pre-grant), when dropped |
| 6 | ch02-split-operation | 02 | SVG | DX split: DX station transmits on one frequency, listens "up" 5–10 kHz; your VFO split; "listening up" pileup etiquette |
| 7 | ch02-bandplan-map | 02 | SVG | A typical HF band's plan map (20 m example): CW → digital → beacons → SSB segments; LSB/USB convention note (canon §7.3 trio) |
| 8 | ch02-contest-exchange | 02 | SVG | A contest QSO timeline: CQ → exchange (RST + section/info) → log; real ARRL exchange examples from canon |
| 9 | ch03-ionosphere-layers | 03 | SVG | D/E/F1/F2 layers day vs night: absorption, refraction, which layers matter when |
| 10 | ch03-muf-angles | 03 | SVG | Critical frequency vs takeoff angle vs skip distance; MUF concept; why higher bands open longer |
| 11 | ch03-nvis | 03 | SVG | NVIS geometry: near-vertical launch, blanket coverage ~0–300 mi, no skip zone |
| 12 | ch03-grayline | 03 | SVG | Gray-line (terminator) propagation: the twilight band around the globe, enhanced paths along it |
| 13 | ch04-hf-station | 04 | SVG | HF station block: transceiver, PSU, computer/interface, tuner, wattmeter, feedline, antenna; signal + control flows |
| 14 | ch04-grounding-bonding | 04 | SVG | HF shack grounding: single-point ground bus, bonded chassis, entrance panel, arrestors |
| 15 | ch04-test-gear | 04 | SVG | Test bench basics: dummy load, wattmeter/SWR meter, antenna analyzer — what each measures and where it connects |
| 16 | ch05-reactance-curves | 05 | plot | X_L rises with f, X_C falls with f (log or linear); one worked point each from the pool's numbers |
| 17 | ch05-resonance-curves | 05 | plot | Series vs parallel resonance: impedance vs frequency (min at resonance series / max parallel); Q effect on sharpness |
| 18 | ch05-impedance-vectors | 05 | SVG | R–X impedance plane: Z = R + jX as a vector; |Z| = √(R²+X²) with 50+j50 → 70.7 Ω worked example; phase angle |
| 19 | ch05-time-constants | 05 | plot | RC charge/discharge and RL current curves; τ marked |
| 20 | ch05-transformer | 05 | SVG | Transformer: turns ratio → voltage ratio; turns² → impedance ratio (√12 ≈ 3.5:1 example from pool) |
| 21 | ch05-rms-peak-pep | 05 | plot | Sine with V_rms/V_pk/V_pp marked; PEP envelope vs average for SSB; the pool's V_pp²/(8R) shortcut example |
| 22 | ch06-device-panel | 06 | SVG | Component panel at General depth: PN/Zener/varactor/LED diodes, NPN/PNP/FET, op-amp, IC, ferrite bead/toroid, crystal — name + one-line role each |
| 23 | ch07-pool-fig-g71 | 07 | SVG redraw | **Pool figure G7-1** (varactor-tuned VFO + amplifier): positions 1–11 exact per canon §1.4 |
| 24 | ch07-power-supply | 07 | SVG | Linear power supply chain: transformer → rectifier → filter → regulator; ripple at each stage (small insets) |
| 25 | ch07-amp-classes | 07 | plot | Amplifier classes A/AB/B/C: conduction-angle waveforms; linearity vs efficiency tradeoff (class C for FM/CW note) |
| 26 | ch07-filter-responses | 07 | plot | Low/high/band-pass/notch response curves on one frequency axis |
| 27 | ch08-heterodyne | 08 | SVG | Mixing/heterodyne: two inputs → sum + difference products; superhet IF concept |
| 28 | ch08-emission-designator | 08 | SVG | Anatomy of an emission designator (e.g. 2K80J3E): bandwidth / modulation / signal / information fields decoded |
| 29 | ch08-digital-waterfalls | 08 | plot | Stylized waterfalls: FT8 (narrow tones in slots), PSK31 (single narrow trace), RTTY (two marks 170 Hz apart) |
| 30 | ch09-feedline-basics | 09 | SVG | Coax vs open-wire/ladder line: construction, characteristic impedance, velocity factor, loss vs frequency |
| 31 | ch09-standing-waves | 09 | plot | Voltage standing wave on a mismatched line; SWR = V_max/V_min; matched vs 2:1 |
| 32 | ch09-antenna-heights | 09 | SVG | Dipole at low vs high height (in wavelengths): pattern change, NVIS vs DX takeoff |
| 33 | ch09-yagi-stack | 09 | SVG | Yagi elements (driven/reflector/director) + why stacking adds ~3 dB; front-to-back idea |
| 34 | ch10-mpe-evaluation | 10 | SVG | RF-exposure evaluation flow at General depth: estimate (OET-65 tables) → model (calc) → measure; re-evaluate on any station change |
| 35 | ch10-duty-factor | 10 | plot | Duty factor vs average exposure: mode duty (SSB voice vs CW vs FT8) × transmit duty; averaging window concept |

**Merging:** the figures assembler merges `figures/fragments/*.json` into `figures/figures.json` (assign `number` by each chapter's first-reference order once chapters exist — for now plan order), runs `figreg.validate()` (empty), XML-parses all 33, renders ≥8 incl. the G7-1 redraw to PNG for visual inspection (G7-1 compared against `canon/source/G7-1.pdf` for content equality).
