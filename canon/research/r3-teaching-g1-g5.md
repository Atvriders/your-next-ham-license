# R3 Teaching Notes — General Pool Subelements G1–G5

Researcher: R3. Scope: subelements G1 (rules), G2 (operating procedures), G3 (propagation), G4 (amateur practices & station setup), G5 (electrical principles) — 249 active questions: G1 = 52 (G1A×10, G1B×11, G1C×8, G1D×12, G1E×11), G2 = 60 (G2A×12, G2B×11, G2C×11, G2D×11, G2E×15), G3 = 37 (G3A×14, G3B×12, G3C×11), G4 = 60 (G4A×13, G4B×13, G4C×12, G4D×11, G4E×11), G5 = 40 (G5A×12, G5B×14, G5C×14).

Basis: verified pool `canon/pool-general.json` / `canon/pool-general.txt` (NCVEC 2023–2027 General pool, 6th errata 2026-02-04, exams through 2027-06-30). Part 97 citations in square brackets are the sections printed on the pool's own ID lines. Propagation/physics/electronics facts are standard textbook knowledge unless noted. Pitch: reader holds a Technician license — Ohm's law, basic DC circuits, VHF/UHF rules and repeater basics are assumed; HF privileges, AC theory, and ionospheric propagation are NOT.

Reader-facing promise: if a chapter teaches every "Teach" bullet and pins every "Watch items" FACT line, the reader can answer every question cited.

---

## G1 — Commission's Rules (52 questions, 5 groups)

### G1A — General class frequency privileges; primary/secondary (10 q)

Topic inventory: which band portions are closed to Generals (G1A01, G1A05, G1A08, G1A09, G1A11 — 5 q); per-band mode limits, 30 m is CW/data only (G1A02, G1A03, G1A07 — 3 q); secondary allocation meaning (G1A06 — 1 q); 10 m repeater segment (G1A10 — 1 q).

Teach:

- General class does NOT get every kHz of the classic HF bands. The lower edges of the 80, 40, 20, and 15 m bands are Amateur Extra (and partly Advanced) only (G1A01, G1A08) [97.301(b), 97.301(d)]. Memorize the four: 80, 40, 20, 15. Generals DO get all of 160, 60, 30, 17, 12, and 10 m.
- Where the General voice segment is shorter than the full voice segment, Generals get the UPPER portion of it (G1A11) [97.301].
- 40 m worked example of the split: Generals are excluded from 7.125–7.175 MHz (G1A05) [97.301(d)]; on 15 m the General phone segment starts at 21.275 MHz, so 21.300 MHz is in (G1A09).
- 30 m (10.1 MHz) is CW, RTTY, and data only — no phone, no image (G1A02, G1A03) [97.305]. On 10 m, Generals may run CW on the ENTIRE band, 28.0–29.7 MHz (G1A07) [97.305(a)].
- "Secondary" allocation: don't cause harmful interference to primary users, and accept interference from them (G1A06) [97.303].
- 10 m repeaters live above 29.5 MHz (G1A10) [97.205(b)].

Common confusions: distractors swap the Extra-only band set for the WARC/60 m set (60, 30, 17, 12 — those are fully General). G1A05's distractors 28.000–28.025 and 21.275–21.300 are segments Generals CAN use.

Vocabulary: primary/secondary allocation, harmful interference, control operator, WARC bands, repeater segment.

Watch items (FACT lines): Extra-only portions = 80/40/20/15 m lower edges; General excluded 7.125–7.175 MHz; 30 m = no phone, no image; 10 m repeaters > 29.5 MHz; General 15 m phone starts 21.275 MHz.

### G1B — Antennas, beacons, prohibited communications (11 q)

Topic inventory: antenna structure regulation (G1B01, G1B06 — 2 q); beacon rules (G1B02, G1B03, G1B09, G1B10 — 4 q); one-way/permitted transmissions and international contacts (G1B04, G1B05, G1B07, G1B08 — 4 q); "good engineering and good amateur practice" (G1B11 — 1 q).

Teach:

- 200 feet above ground is the antenna-structure threshold: below it (and not near a public-use airport) no FAA notification / FCC registration (G1B01) [97.15(a)].
- Local zoning may regulate amateur towers but must "reasonably accommodate" amateur communications and use the minimum practical regulation — this is the PRB-1 doctrine (G1B06) [97.15(b), PRB-1].
- Beacons: one per band per location (G1B02) [97.203(b)]; purpose = observation of propagation and reception (G1B03) [97.3(a)(9)]; automatically controlled beacons on HF only in 28.20–28.30 MHz (G1B09) [97.203(d)]; power limit 100 W PEP (G1B10) [97.203(c)].
- Permitted one-way transmissions: code-practice transmissions (learning Morse) (G1B05) [97.111(a)(5)(b)]; occasional retransmission of US government weather and propagation forecasts (G1B04) [97.113(c)].
- Q signals and abbreviations are fine if they don't obscure meaning (G1B07) [97.113(a)(4)]. You may talk to any country except those whose administrations have objected to the ITU (G1B08) [97.111(a)(1)].
- Where Part 97 is silent, the FCC defines "good engineering and good amateur practice" (G1B11) [97.101(a)].

Common confusions: "National Beacon Organization" (G1B02-B) does not exist; beacon power is 100 W, not the usual 1500 W; unidentified transmissions and encryption are never the right answer.

Vocabulary: beacon station, one-way transmission, PRB-1, reasonable accommodation, third-party communication (used in G1E too).

Watch items: 200 ft tower threshold; beacon 100 W PEP; auto beacons 28.20–28.30 MHz (HF); pool prints G1B05's citation as "[97.111((5)(b)]" — typo for 97.111(a)(5)(b), flag for the assembler.

### G1C — Emission standards, power limits, 60 m (8 q)

Topic inventory: power limits by band (G1C01, G1C02, G1C05, G1C06, G1C11 — 5 q); 60 m specifics (G1C03, G1C04 — 2 q); new digital protocols (G1C07 — 1 q).

Teach:

- Default amateur ceiling is 1500 W PEP output — that is the answer on 12 m, 28 MHz, and 1.8 MHz for a General (G1C02, G1C05, G1C06) [97.313].
- The big exception below 30 MHz: 30 m is 200 W PEP (G1C01, asked as 10.140 MHz) [97.313(c)(1)].
- The legal measurement is PEP output from the transmitter (G1C11) [97.313] — not RMS, not "input to the antenna." PEP = average power during one RF cycle at the crest of the modulation envelope.
- 60 m: max emission bandwidth 2.8 kHz (G1C03) [97.303(h)(1) as printed; now 97.303(h)(3) — see flags]; if you use an antenna other than a dipole, keep a record of its gain (G1C04) [97.303(i) as printed; now 97.313(i)].
- Before using a new digital protocol on the air, its technical characteristics must be publicly documented (G1C07) [97.309(a)(4)].

Common confusions: power distractors 50/200/1000/1500/2000 W are other bands' limits or invented; 2000 W and "RMS" never appear in Part 97 answers; the 60 m bandwidth trap is 3 kHz ("close enough") vs the correct 2.8 kHz.

Vocabulary: PEP (peak envelope power), ERP, emission bandwidth, protocol documentation.

Watch items: 1500 W PEP general limit; 200 W PEP on 30 m; 2.8 kHz on 60 m.

### G1D — Volunteer examiners, CSCEs, license credit, remote control (12 q)

Topic inventory: VE accreditation and exam sessions (G1D02, G1D04, G1D07, G1D08, G1D10 — 5 q); expired-license credit (G1D01, G1D11 — 2 q); CSCE and upgrade mechanics (G1D03, G1D06, G1D09 — 3 q); remote control across borders (G1D05, G1D12 — 2 q).

Teach:

- A General-class VE may administer Technician exams ONLY (G1D02) [97.509(b)(3)(i)]; a Tech exam session needs at least THREE VEs of General class or higher observing (G1D04) [97.509(3)(i)(c)]. VEs are accredited by a Volunteer Examiner Coordinator (VEC), not the FCC (G1D07) [97.509(b)(1)]; must be 18+ (G1D10) [97.509(b)(2)]; a non-US citizen CAN be a VE if they hold an FCC General-or-higher license (G1D08) [97.509(b)(3)].
- CSCE = 365 days of exam-element credit (G1D09) [97.9(b)]. A Tech with a General CSCE may operate on ANY General or Technician segment immediately (G1D03) [97.9(b)], signing call + "AG" until the upgrade shows in the FCC database (G1D06) [97.119(f)(2)].
- Anyone who once held an FCC General, Advanced, or Extra license (not revoked) gets partial credit (G1D01) [97.501, 97.505(a)]; past the 2-year grace period: show proof of the old grant AND pass Element 2 (current Tech exam) to get a new General license (G1D11) [97.505].
- Remote control: run your US station from abroad and YOU still need the US operator/primary station license (G1D05) [97.7]; run a South American station from the US and ONLY that country's rules apply (G1D12) [97.507].

Common confusions: "two VEs" vs the required three; CSCE validity 30/180 days vs 365; "AG" only on General-privilege frequencies, not all the time; remote-control distractors invent "special remote station permits."

Vocabulary: VE, VEC, CSCE, grace period, Element 2, local vs remote control.

Watch items: 3 VEs, General+, for a Tech exam; VE minimum age 18; CSCE 365 days; "AG" suffix rule.

### G1E — Third-party traffic, automatic control, special rules (11 q)

Topic inventory: third-party communications (G1E01, G1E05, G1E12 — 3 q); automatic control of digital stations (G1E03, G1E11 — 2 q); interference avoidance duties (G1E04, G1E10 — 2 q); misc: repeater retransmission, ITU region, Wi-Fi, spread spectrum (G1E02, G1E06, G1E07, G1E08 — 4 q).

Teach:

- Third-party: a person whose own amateur license was revoked (not reinstated) is disqualified (G1E01) [97.115(b)(2)]. Messages to third parties in agreement countries must relate to amateur radio, be personal remarks, or be emergency/disaster traffic (G1E05) [97.115(a)(2), 97.117]. Third-party via remote control is OK whenever third-party traffic itself is OK (G1E12) [97.115].
- Automatic control: to contact an automatically controlled digital station OUTSIDE the auto-control segments, the initiating station must be under local or remote control (G1E03) [97.221]. Auto RTTY/data stations may operate anywhere on 6 m and shorter wavelengths, plus limited HF segments (G1E11) [97.221, 97.305].
- You must take steps to avoid harmful interference near FCC monitoring stations, on secondary-allocation bands, and with spread spectrum (G1E04) [97.13(b), 97.303, 97.311(b)]. Avoid 14.100, 18.110, 21.150, 24.930, 28.200 MHz — the international propagation beacon network (G1E10) [97.101].
- A 10 m repeater may retransmit a Technician's 2 m signal only if the repeater's control operator holds General or higher (G1E02) [97.205(b)] — the repeater is the transmitting station on 10 m.
- North and South America = ITU Region 2 (G1E06) [97.301, ITU RR]. Amateurs may NOT communicate with unlicensed Wi-Fi stations anywhere in 2.4 GHz (G1E07) [97.111]. Spread spectrum max = 10 W PEP (G1E08) [97.313(j)].

Common confusions: G1E07's "channels 1–4" sounds plausible (2.4 GHz overlaps Wi-Fi) but the rule is no communication with non-licensed stations, period; Region 1/2/3 mixups; beacon frequencies vs "emergency frequencies."

Vocabulary: third-party agreement, automatic control, local/remote control, spread spectrum, ITU Region 2, propagation beacon network.

Watch items: SS = 10 W PEP; beacon net freqs 14.100/18.110/21.150/24.930/ 28.200 MHz; Region 2 = the Americas.

---

## G2 — Operating Procedures (60 questions, 5 groups)

### G2A — Phone operating and SSB conventions (12 q)

Topic inventory: USB/LSB conventions (G2A01, G2A02, G2A03, G2A04, G2A07, G2A09 — 6 q); SSB properties (G2A05, G2A06 — 2 q); operating practice: breaking in, CQ DX, VOX, ALC (G2A08, G2A10, G2A11, G2A12 — 4 q).

Teach:

- The sideband convention: LSB below 10 MHz (160/75/40 m), USB at 10 MHz and above — including 17/12 m and VHF/UHF SSB (G2A01–G2A04). It is convention, not law or physics (G2A09). HF voice = single sideband, period (G2A05).
- SSB transmits ONE sideband; the carrier and the other sideband are suppressed (G2A07). Advantages vs AM/FM: less bandwidth, better power efficiency (G2A06).
- Break into a phone QSO by saying your call sign once, between transmissions (G2A08). "CQ DX" from the lower 48 invites answers from outside the lower 48 (G2A11). VOX = hands-free transmit/receive switching by voice (G2A10). ALC is set with the mic gain / transmit audio control — drive it until ALC just starts working (G2A12).

Common confusions: "suppressed sideband" and "double sideband" are invented modes; G2A07-A says one sideband AND carrier (that's AM-with-one-sideband, wrong); "Breaker Breaker" is CB talk.

Vocabulary: USB/LSB, carrier suppression, VOX, PTT, ALC, CQ DX, break-in.

Watch items: LSB on 160/75/40 m; USB on 20 m and up + VHF/UHF.

### G2B — Operating courtesy, band plans, emergencies (11 q)

Topic inventory: frequency courtesy and conflict (G2B01, G2B03, G2B06, G2B07 — 4 q); minimum separations (G2B04, G2B05 — 2 q); distress/RACES (G2B02, G2B09, G2B11 — 3 q); net management (G2B10 — 1 q); 6 m DX window (G2B08 — 1 q).

Teach:

- Except during emergencies, NO amateur has priority on any frequency — not nets, not QSOs in progress, not contests (G2B01) [97.101(b), (c)]. If propagation shifts create interference, work it out mutually (G2B03). Before calling: send "QRL?" on CW or ask "is this frequency in use?" on phone, followed by your call (G2B06); follow the voluntary band plan (G2B07).
- Separations (pure FACT): CW 150–500 Hz (G2B04); SSB 2–3 kHz (G2B05).
- Hear a station in distress: acknowledge it and find out what help is needed — first (G2B02). RACES control operator must hold an FCC amateur license (G2B09) [97.407(a)]; routine RACES drills max 1 hour per week (G2B11) [97.407(d)(4)].
- Good net practice: have a backup frequency ready (G2B10).
- 50.1–50.125 MHz is a voluntary DX window: US-48 stations use it only for contacts OUTSIDE the 48 contiguous states (G2B08) — band plan, not FCC law.

Common confusions: "cease all transmissions" (G2B02-D) abandons someone in distress; RACES drill limits 1-vs-2 hours and per-week-vs-per-month; the 6 m window is voluntary, so "FCC rules prohibit" framings are wrong.

Vocabulary: voluntary band plan, QRL?, RACES, net control, DX window.

Watch items: CW 150–500 Hz; SSB 2–3 kHz; RACES 1 hour/week; 50.1–50.125 DX window.

### G2C — CW operating (11 q)

Topic inventory: Q signals (G2C02, G2C04, G2C09, G2C10, G2C11 — 5 q); prosigns (G2C03, G2C08 — 2 q); technique: QSK, speed, zero beat, RST (G2C01, G2C05, G2C06, G2C07 — 4 q).

Teach:

- Q-signal set: QRS? = send slower (G2C02); QRL? = "are you busy? / is this frequency in use?" (G2C04); QSL = "I have received and understood" (G2C09); QRN = troubled by static (G2C10); QRV = ready to receive (G2C11).
- Prosigns: KN = listening only for specific station(s) (G2C03); AR = end of a formal message (G2C08). (SK = end of contact; BK = break — the distractors.)
- Full break-in (QSK): you can hear between code elements (G2C01). Answer a CQ no FASTER than it was sent (G2C05). Zero beat = match your transmit frequency to the received signal (G2C06). RST with a "C" suffix = chirpy, unstable signal (G2C07).

Common confusions: QRN (natural static) vs QRM (man-made interference — not asked but a classic swap); QSL vs "we have worked before"; AR vs SK vs KN; zero beat is about frequency, not keying speed.

Vocabulary: Q signal, prosign, QSK/full break-in, zero beat, RST, chirp.

Watch items: the five Q signals and two prosigns above, verbatim.

### G2D — Volunteer Monitors, maps, DX and general operating (11 q)

Topic inventory: Volunteer Monitor program (G2D01, G2D02, G2D03 — 3 q); maps and paths (G2D04, G2D06 — 2 q); phonetics (G2D07 — 1 q); everyday operating: CQ, logs, contests, QRP, reports (G2D05, G2D08, G2D09, G2D10, G2D11 — 5 q).

Teach:

- Volunteer Monitors are amateurs formally enlisted (via ARRL, under FCC agreement) to watch the bands for rules violations; the goal is self-regulation and compliance, not enforcement (G2D01, G2D02). They can localize a stuck-carrier station by comparing beam headings from several locations (G2D03).
- Azimuthal projection map: true bearings and distances from YOUR location — the DXer's map (G2D04). Long path = point the beam 180 degrees from the short-path heading (G2D06).
- NATO phonetics: Alpha, Bravo, Charlie, Delta... (G2D07); the old Able/Baker set and police-style Adam/Boy are distractors.
- CQ procedure: "CQ" a few times, "this is," your call a few times, listen, repeat (G2D05). Station logs are voluntary but help you answer FCC inquiries (G2D08). Contest rules never override FCC ID rules (G2D09). QRP = low-power operation (G2D10). Exchange signal reports first so both stations can adapt to conditions (G2D11).

Common confusions: VM ≠ VE (exams) and VM ≠ frequency coordinators; "long path = along the gray line" is a different concept; FCC does NOT require a log (distractors A/B in G2D08).

Vocabulary: Volunteer Monitor, azimuthal projection, short/long path, QRP, signal report, contest exchange.

### G2E — Digital operating (15 q)

Topic inventory: RTTY (G2E01, G2E06, G2E14 — 3 q); FT8/JT family (G2E04, G2E05, G2E07, G2E15 — 4 q); Winlink/PACTOR/VARA (G2E02, G2E03, G2E09, G2E10, G2E12, G2E13 — 6 q); digital watering holes (G2E08 — 1 q); AREDN (G2E11 — 1 q).

Teach:

- Sideband conventions for AFSK digital: RTTY traditionally LSB (G2E01); JT65/JT9/FT4/FT8 USB (G2E05). Most common RTTY shift on HF: 170 Hz (G2E06). If an FSK signal won't decode: mark/space may be reversed, wrong baud rate, or wrong sideband (G2E14).
- FT8 needs computer time accurate to ~1 second (G2E07); answer a CQ on the ALTERNATE time slot on a clear frequency, not the caller's (G2E04); a common FT8 spot is 14.074–14.077 MHz (G2E15). Most HF digital activity on 20 m sits in 14.070–14.100 MHz (G2E08).
- Winlink = amateur radio email: wireless, VHF and HF, a form of packet radio — all three descriptions true (G2E12). VARA is a digital protocol used with Winlink (G2E02). A Winlink "Remote Message Server" is a gateway (G2E13); connect by transmitting a connect message on its published frequency (G2E10). PACTOR connections are strictly two-station — you cannot join one in progress (G2E09). Interference to PACTOR/VARA causes retries, timeouts, pauses, or failed connects (G2E03).
- AREDN mesh = high-speed data networking for emergencies/community events (G2E11).

Common confusions: RTTY-LSB vs FT8-USB (opposite conventions — the pool tests both); 850 Hz was the old commercial RTTY shift; "special hardware modem" for FT8 is wrong (sound card + accurate clock is all).

Vocabulary: AFSK, mark/space, shift, baud, Winlink, VARA, PACTOR, gateway, SSID, AREDN, waterfall, time slot.

Watch items: 170 Hz RTTY shift; 14.070–14.100 digital segment; FT8 14.074–14.077 MHz; FT8 clock ~1 s.

---

## G3 — Radio Wave Propagation (37 questions, 3 groups)

All standard textbook knowledge (ARRL Handbook / propagation primers); no Part 97 content in this subelement. Pitch: the Technician already knows VHF line-of-sight and sporadic-E/tropo buzzwords; the ionosphere-as-mirror model is new.

### G3A — Sunspot cycle, solar indices, disturbances (14 q)

Topic inventory: solar activity and HF (G3A01, G3A04, G3A07 — 3 q); solar and geomagnetic disturbances (G3A02, G3A03, G3A06, G3A08, G3A09, G3A11, G3A14 — 7 q); the three indices (G3A05, G3A12, G3A13 — 3 q); the 27-day cycle (G3A10 — 1 q).

Teach:

- More sunspots ⇒ more ionization ⇒ higher frequencies propagate. Low solar activity kills the high bands first: 15, 12, and 10 m become least reliable (G3A01, G3A04). 20 m supports worldwide daylight propagation at ANY point in the cycle (G3A07).
- Timing (the pool's favorite trap): a solar flare's UV/X-ray burst arrives in ~8 minutes (light-travel time) causing a Sudden Ionospheric Disturbance (G3A03); a coronal mass ejection's particles take 15 hours to several days (G3A11). SID hits daytime lower HF frequencies hardest (G3A02).
- Geomagnetic storm = temporary disturbance of Earth's magnetic field (G3A06); it DEGRADES high-latitude (polar) HF paths (G3A08), but the accompanying aurora can reflect VHF signals (G3A09). Charged particles from coronal holes disturb HF (G3A14).
- Indices: solar flux index = 10.7 cm (2800 MHz) solar radio emission (G3A05); K-index = SHORT-term (3-hour) geomagnetic stability (G3A12); A-index = LONG-term (daily) geomagnetic stability (G3A13).
- Conditions recur every ~26–28 days because the Sun's surface rotates on its axis in that period (G3A10).

Common confusions: 8 minutes vs 20–40 hours vs 15 h–several days vs 28 days — four timings for four mechanisms (light, old-CME answer, particles, rotation); K vs A (short vs long); solar flux is NOT a sunspot count.

Vocabulary: sunspot number, solar flux index (SFI), SID, geomagnetic storm, coronal hole, coronal mass ejection, aurora, K-index, A-index.

Watch items: 8 minutes (flare light); 15 h–several days (CME); 10.7 cm flux; 26–28 day rotation.

### G3B — MUF, LUF, skip distance, checking conditions (12 q)

Topic inventory: MUF/LUF concepts (G3B02, G3B03, G3B05, G3B06, G3B07, G3B08, G3B11 — 7 q); hop distances (G3B09, G3B10 — 2 q); path oddities (G3B01 — 1 q); measuring current propagation (G3B04 — 1 q); summer static (G3B12 — 1 q).

Teach:

- MUF = Maximum Usable Frequency between two specific points (G3B08); LUF = Lowest Usable Frequency (G3B07). Between them, the ionosphere refracts signals back to Earth (G3B05); below the LUF, absorption kills the signal before it arrives (G3B06). If the LUF rises above the MUF, no ordinary skywave path exists (G3B11).
- Best (least-attenuated) long-distance frequency: JUST BELOW the MUF (G3B03). MUF depends on path, time of day, season, solar radiation, and disturbances — everything (G3B02).
- One-hop distances (FACT): F2 region ≈ 2,500 miles (G3B09); E region ≈ 1,200 miles (G3B10).
- Hearing your own signal back via short + long path produces a slightly delayed echo (G3B01).
- To check propagation NOW from your station: use an internet network of automated receivers (e.g., RBN-style) to see where you are heard (G3B04).
- Lower HF in summer = high atmospheric static (G3B12).

Common confusions: "Minimum Usable Frequency" is a planted expansion of MUF (G3B08-A); just-below-MUF vs just-above-LUF vs critical frequency (G3B03 mixes all three); 180/1,200/2,500/12,000-mile distance ladder.

Vocabulary: MUF, LUF, skip, hop, refraction, absorption, long path, reverse beacon network.

Watch items: F2 hop 2,500 mi; E hop 1,200 mi.

### G3C — Ionospheric regions, critical frequency/angle, scatter, NVIS (11 q)

Topic inventory: the layers (G3C01, G3C03, G3C05, G3C11 — 4 q); critical frequency and angle (G3C02, G3C04 — 2 q); scatter (G3C06, G3C07, G3C08, G3C09 — 4 q); NVIS (G3C10 — 1 q).

Teach:

- Layers bottom-up: D (closest), E, F1, F2 (G3C01). F2 is highest, so F2 skip is longest (G3C03).
- Daytime D region ABSORBS the low bands — that's why 40/60/80/160 m are day-useless for long distance (G3C05) and the D region is the most absorbent below 10 MHz in daylight (G3C11). It fades at night; the low bands open.
- Critical frequency (at a given incidence angle): highest frequency refracted back to Earth (G3C02). Critical angle: the HIGHEST takeoff angle that still returns to Earth (G3C04). Steeper than that punches through.
- Scatter fills the skip zone: only a small fraction of energy scatters, so signals are weak (G3C08), arrive over multiple paths, and sound distorted with a flutter (G3C06, G3C07). Scatter is what lets you hear anything in the skip zone at all (G3C09).
- NVIS = near vertical incidence skywave: high-angle, short-distance MF/HF propagation, the EMCOM workhorse for regional coverage (G3C10).

Common confusions: D absorbs, F refracts — distractors swap them; critical frequency vs critical angle (frequency-vs-angle axes); "highest" vs "lowest" takeoff angle wording in G3C04.

Vocabulary: D/E/F1/F2 region, critical frequency, critical angle, skip zone, scatter, NVIS, takeoff angle, absorption.

Watch items: layer order D < E < F1 < F2; D-region daytime absorption of 40/60/80/160 m.

---

## G4 — Amateur Radio Practices & Station Setup (60 questions, 5 groups)

Electronics facts here are standard textbook knowledge; rule-flavored items (RFI duties) trace to Part 97 generally.

### G4A — Station equipment: receivers, amplifiers, tuners, keyers (13 q)

Topic inventory: receiver features (G4A01, G4A02, G4A03, G4A07, G4A12, G4A13 — 6 q); tube amplifiers and ALC (G4A04, G4A05, G4A08, G4A09, G4A11 — 5 q); antenna tuner (G4A06 — 1 q); electronic keyer (G4A10 — 1 q).

Teach:

- Notch filter: removes interfering carriers inside the receiver passband (G4A01). Noise blanker: mutes receiver gain during each noise pulse (G4A03). DSP noise reduction turned up too far distorts the desired signal (G4A07). Receive attenuator: prevents overload from strong signals (G4A13). "Reverse" sideband on CW can move an interfering signal out of the passband (G4A02). Dual VFO: transmit on one frequency, listen on another — split operation (G4A12).
- Vacuum-tube RF amplifier tune-up: TUNE for a pronounced DIP in plate current (resonance) (G4A04); set LOAD/COUPLING for desired power without exceeding max plate current (G4A08). ALC between exciter and amplifier prevents excessive drive (G4A05) — and with AFSK data modes the ALC must be inactive because its action distorts the signal (G4A11). Delay RF output after keying an external amp so its relays can switch the antenna first (hot-switching damages them) (G4A09).
- Antenna tuner: increases power transfer from transmitter to feed line by making the transmitter see its design load — it does NOT change the SWR on the feed line to the antenna (G4A06).
- Electronic keyer: automatically generates dots and dashes (G4A10).

Common confusions: notch filter (carrier) vs noise blanker (pulses) vs noise reduction (random noise) — the pool tests all three separately; "tuner fixes SWR at the antenna" is the classic wrong mental model.

Vocabulary: notch filter, noise blanker, DSP noise reduction, attenuator, split operation, ALC, plate current dip, hot-switching, antenna tuner (transmatch), keyer.

### G4B — Test and measurement equipment (13 q)

Topic inventory: meters and scopes (G4B01, G4B02, G4B03, G4B04, G4B05, G4B06, G4B09 — 7 q); two-tone testing (G4B07, G4B08 — 2 q); wattmeters and antenna analyzers (G4B10, G4B11, G4B12, G4B13 — 4 q).

Teach:

- Oscilloscope = horizontal and vertical channel amplifiers (G4B01); it beats a DVM for complex waveforms (G4B02) and is THE instrument for a CW keying waveform (G4B03). To view an RF envelope, feed attenuated transmitter RF output into the vertical input (G4B04).
- Voltmeters use high input impedance to avoid loading the circuit under test (G4B05). DMM advantage: higher precision (G4B06); analog meter wins when peaking/nulling — adjusting for max/min (G4B09).
- Two-tone test: feed two NON-harmonically related audio tones into an SSB transmitter and look at the output; it analyzes LINEARITY (G4B07, G4B08).
- Directional wattmeter reads forward and reflected power, from which SWR follows (G4B10). An antenna analyzer connects to the antenna + feed line (G4B11), can measure coax impedance (G4B13), and nearby strong signals can corrupt its SWR readings (G4B12).

Common confusions: scope vs DMM "advantage" framings (precision belongs to the DMM, waveforms to the scope); two-tone test measures linearity, not carrier suppression; an analyzer cannot measure front-to-back ratio or transmitter power.

Vocabulary: oscilloscope, DMM, input impedance/loading, two-tone test, linearity, IMD, directional wattmeter, forward/reflected power, antenna analyzer.

### G4C — Interference, grounding, bonding (12 q)

Topic inventory: RFI causes and cures (G4C01, G4C02, G4C03, G4C04, G4C05, G4C08 — 6 q); grounding, ground loops, bonding (G4C06, G4C07, G4C09, G4C10, G4C11, G4C12 — 6 q).

Teach:

- A bypass capacitor shunts RF to ground and cures RFI in audio circuits (G4C01). Wideband interference across many frequencies = arcing at a poor electrical connection (G4C02).
- What RFI sounds like in a consumer audio device: SSB = distorted speech (G4C03); CW = on-and-off humming or clicking (G4C04).
- RF burns / hot chassis come from a ground wire with high impedance at that frequency — e.g., a resonant ground connection (G4C05, G4C06).
- Never solder lightning-protection ground joints — lightning heat destroys solder (G4C07). A ferrite choke on a cable kills common-mode RFI current (G4C08).
- Ground loops: bond equipment enclosures together to minimize them (G4C09); their symptom is hum on your transmitted audio (G4C10); bonding also minimizes RF hot spots in the shack (G4C11). Ground all metal enclosures so hazardous voltages can never appear on the chassis (G4C12).

Common confusions: SSB-RFI "clearly audible speech" is wrong (rectification mangles it); grounding the CENTER conductor of an audio cable is nonsense — ferrite choke is the cure; "series" vs "bonded star" grounding.

Vocabulary: RFI, bypass capacitor, arcing, common-mode current, ferrite choke, ground loop, bonding, hot spot, chassis ground.

### G4D — Speech processors, S meters, sideband bandwidth (11 q)

Topic inventory: speech processing (G4D01, G4D02, G4D03 — 3 q); S-meter and dB (G4D04, G4D05, G4D06, G4D07 — 4 q); sideband width vs band edges (G4D08, G4D09, G4D10, G4D11 — 4 q).

Teach:

- Speech processor: increases apparent loudness by raising AVERAGE power (peaks stay legal) (G4D01, G4D02); misadjusted = distorted speech, excess IMD, excessive background noise — all three (G4D03).
- S meter measures received signal strength (G4D04). FACT: one S unit ≈ 6 dB (G4D06); 6 dB = 4× power, so S8→S9 needs 4× the transmit power (G4D07); "20 dB over S9" = 10^(20/10) = 100× power (G4D05). Math: dB = 10·log10(P2/P1).
- Displayed-frequency arithmetic for SSB (the rig shows the suppressed carrier): USB occupies carrier → carrier+3 kHz; LSB occupies carrier−3 kHz → carrier. Worked: LSB at 7.178 MHz fills 7.175–7.178 (G4D08 — note it lands exactly on the General 40 m phone edge from G1A05); USB at 14.347 fills 14.347–14.350 (G4D09). Rules of thumb: with 3 kHz LSB stay at least 3 kHz ABOVE the lower edge (G4D10); with 3 kHz USB stay at least 3 kHz BELOW the upper edge (G4D11).

Common confusions: processor "increases peak power" is the trap (it raises average, not peak); "20 dB = 20×" linear thinking (it's 100×); 1.5 kHz ("half the bandwidth") and 1 kHz edge-spacing distractors.

Vocabulary: speech processor, average vs peak power, S meter, S unit, suppressed carrier, occupied bandwidth.

Watch items (FACT): 1 S unit = 6 dB; 6 dB = 4× power; 20 dB = 100× power; 3 kHz SSB edge-spacing rules.

### G4E — Mobile and portable power (11 q)

Topic inventory: HF mobile (G4E01, G4E02, G4E03, G4E04, G4E05, G4E06, G4E07 — 7 q); solar power (G4E08, G4E09, G4E10, G4E11 — 4 q).

Teach:

- Capacitance hat: electrically lengthens a physically short whip (G4E01). Corona ball: bleeds off RF voltage at the whip tip, preventing discharge (G4E02). Shortened antennas have high Q ⇒ very limited operating bandwidth (G4E06), and antenna efficiency is the biggest limit on an HF mobile station (G4E05).
- Mobile DC wiring: 100 W HF rig connects DIRECTLY to the battery with heavy-gauge wire, fused (G4E03); the cigarette-lighter/aux socket wiring can't carry the current (G4E04). Vehicle receive noise sources: charging system, fuel delivery (fuel pump), and control computers — all of them (G4E07).
- Solar: cells in a panel are wired series-parallel (for useful voltage AND current) (G4E08); one silicon photovoltaic cell ≈ 0.5 V open-circuit in full sun (G4E09); series diode stops the battery discharging back through the panel at night (G4E10); lithium iron phosphate batteries REQUIRE a charge controller with the panel (G4E11).

Common confusions: capacitance hat ≠ power-handling device; corona ball ≠ bandwidth or Q fix; 0.02/0.2/1.38 V distractors (1.38 V is a mercury cell); alternator vs battery wiring.

Vocabulary: capacitance hat, corona ball, electrically short antenna, loading, photovoltaic cell, series diode, charge controller, LiFePO4.

Watch items (FACT): silicon PV cell ≈ 0.5 V.

---

## G5 — Electrical Principles: AC, Reactance, Impedance, Resonance (40 questions, 3 groups)

All standard textbook knowledge. This is the math subelement — the book does real calculations here. Everything the reader needs is below, each formula followed by pool-number worked examples (all verified by computation against the keyed answers).

### G5A — Reactance, impedance, resonance concepts (12 q)

Topic inventory: reactance definition and behavior (G5A02, G5A03, G5A04, G5A05, G5A06, G5A09, G5A11 — 7 q); impedance family (G5A07, G5A08, G5A10 — 3 q); resonance (G5A01, G5A12 — 2 q).

Teach:

- Reactance X is opposition to AC current flow caused by capacitance or inductance (G5A02, G5A03, G5A04); unit = ohms (G5A09); letter = X (G5A11). It opposes AC without dissipating power (resistance dissipates, reactance stores-and-returns).
- Frequency dependence (pure concept, two directions to memorize): inductor — X rises with frequency (G5A05); capacitor — X falls with frequency (G5A06). Amplitude does not change reactance (distractors).
- Impedance Z = voltage/current ratio (Ohm's law generalized to AC) (G5A08). Admittance = 1/impedance (G5A07). Impedance matching at RF can use a transformer, a pi-network, or a transmission-line section — all three (G5A10).
- Resonance: X_L = X_C and the two reactances CANCEL (G5A12). In a SERIES LC circuit that makes impedance very LOW (G5A01); in a parallel LC circuit it makes impedance very HIGH (distractor A in G5A01 swaps them).

Common confusions: reactance vs resistance ("opposition to DC" distractors); conductance/susceptance/admittance/reluctance four-way vocabulary swap; series-low vs parallel-high impedance at resonance.

Vocabulary: reactance, impedance, admittance, susceptance, conductance, resonance, series/parallel LC, impedance matching.

MATH (formulas the pool tests only conceptually, but the book teaches):

- Inductive reactance: X_L = 2πfL (f in Hz, L in henries, X in ohms). Example (pool's own 20 mH inductor from G5C11): at 7 MHz, X_L = 2π × 7×10^6 × 0.020 ≈ 880,000 Ω. At 60 Hz the same inductor is only 2π × 60 × 0.020 ≈ 7.5 Ω — frequency moves reactance, exactly the G5A05 concept.
- Capacitive reactance: X_C = 1/(2πfC) (C in farads). Example (pool's 100 µF from G5C09): at 60 Hz, X_C = 1/(2π × 60 × 100×10^-6) ≈ 26.5 Ω. Double the frequency and X_C halves (G5A06).
- Resonant frequency: f = 1/(2π√(LC)). Example (pool's 10 mH from G5C10 with 100 µF from G5C09): f = 1/(2π√(0.010 × 100×10^-6)) = 1/(2π × 0.001) ≈ 159 Hz — at 159 Hz X_L = X_C ≈ 10 Ω and they cancel (G5A12).
- Impedance magnitude with resistance and reactance: |Z| = √(R² + X²), and phase angle φ = arctan(X/R) — the phase concept behind "voltage leads current in an inductor, lags in a capacitor." Example (pool's 50 Ω dummy-load number from G5B06): R = 50 Ω in series with X = 50 Ω gives |Z| = √(50² + 50²) ≈ 70.7 Ω, φ = 45°.

### G5B — Power, RMS, PEP, and decibels (14 q)

Topic inventory: power calculations (G5B03, G5B04, G5B05, G5B12 — 4 q); RMS/peak conversions (G5B07, G5B08, G5B09 — 3 q); PEP (G5B06, G5B11, G5B13, G5B14 — 4 q); decibels (G5B01, G5B10 — 2 q); parallel current (G5B02 — 1 q).

Teach:

- The three power forms (Technician review, one step harder numbers): P = V×I, P = I²R, P = V²/R. Worked (pool numbers): 400 VDC across 800 Ω → P = 400²/800 = 200 W (G5B03). 12 V × 0.2 A = 2.4 W (G5B04). 7.0 mA through 1,250 Ω → P = 0.007² × 1250 = 0.06125 W ≈ 61 mW (G5B05). Inverse: RMS voltage across a 50 Ω load dissipating 1,200 W → V = √(1200 × 50) ≈ 245 V (G5B12).
- RMS: the AC value that heats a resistor like the same-value DC (G5B07). For a sine wave: V_rms = V_peak/√2 = 0.707·V_peak; V_pp = 2√2·V_rms ≈ 2.828·V_rms. Worked: 17 V peak → 17/√2 ≈ 12 V RMS (G5B09). 120 V RMS → 2√2 × 120 ≈ 339.4 V peak-to-peak (G5B08).
- PEP (peak envelope power): compute power at the envelope peak using RMS of the peak RF voltage: PEP = (V_pp/(2√2))²/R = V_pp²/(8R). Worked: 200 V p-p across 50 Ω → (100/√2)²/50 = 5,000/50 = 100 W (G5B06). 500 V p-p across 50 Ω → 500²/(8×50) = 625 W (G5B14). For an UNMODULATED carrier PEP = average power, ratio 1.00 (G5B11) — so 1,060 W average carrier = 1,060 W PEP (G5B13).
- Decibels: dB = 10·log10(P2/P1). FACT: ×2 power ≈ 3 dB (G5B01); a 1 dB loss leaves 10^(-0.1) = 0.794 of the power, i.e., a 20.6% loss (G5B10). (Cross-links: 6 dB = 4× and 20 dB = 100× live in G4D05–G4D07.)
- Parallel branches: total current = sum of branch currents (G5B02).

Common confusions: using V_pp or V_peak directly in P = V²/R (yields the plausible 400 W / 2,500 W / 353 W distractors in G5B06/G5B14 — the √2 conversion is the whole game); "PEP = 2× average" (that's a 100%-modulated AM envelope, not a carrier); dB as a linear multiplier; 11 W vs 61 mW unit slips in G5B05.

Vocabulary: RMS, peak, peak-to-peak, PEP, average power, decibel, dummy load.

Watch items (FACT): ×2 power = ~3 dB; 1 dB loss = 20.6%; PEP = average for unmodulated carrier.

### G5C — Transformers; series and parallel R, L, C (14 q)

Topic inventory: transformers (G5C01, G5C02, G5C05, G5C06, G5C07 — 5 q); resistors (G5C03, G5C04 — 2 q); inductors (G5C10, G5C11, G5C14 — 3 q); capacitors (G5C08, G5C09, G5C12, G5C13 — 4 q).

Teach:

- Transformer action = mutual inductance: changing primary current makes a changing magnetic field that induces voltage in the secondary (G5C01). Voltage ratio = turns ratio; running it backwards inverts the ratio (4:1 step-down fed into the secondary multiplies by 4) (G5C02). A step-UP transformer's primary carries the HIGHER current, hence heavier wire (G5C05).
- Turns-ratio math: V_s = V_p × (N_s/N_p). Worked: 120 VAC into 500-turn primary, 1,500-turn secondary → 120 × 3 = 360 V (G5C06).
- Impedance transforms as the SQUARE of the turns ratio: Z_p/Z_s = (N_p/N_s)². Worked: match 600 Ω to 50 Ω → ratio 12:1, turns ratio √12 ≈ 3.5:1 (G5C07). The 12:1 and 144:1 distractors are for students who forget the square (or square twice).
- Combination rules — R and L behave alike, C behaves opposite: series R: add; parallel R: reciprocals add. Series L: add; parallel L: reciprocals add. Series C: RECIPROCALS add; parallel C: add. Worked (all pool numbers): 10‖20‖50 Ω → 1/(1/10+1/20+1/50) ≈ 5.9 Ω (G5C03); 100‖200 Ω ≈ 67 Ω (G5C04). 20 mH + 50 mH series = 70 mH (G5C11); three 10 mH parallel = 3.3 mH (G5C10). Three 100 µF series = 33.3 µF (G5C09); 20 µF series 50 µF = 1/(1/20+1/50) ≈ 14.3 µF (G5C12); 5 nF + 5 nF + 750 pF parallel = 10.750 nF (G5C08 — unit conversion is the test). To INCREASE capacitance add a capacitor in PARALLEL (G5C13); to increase inductance add an inductor in SERIES (G5C14).

Common confusions: capacitor rules feel "backwards" vs resistors — parallel-adds for C, series-adds for R/L; mixed units in G5C08 (nF vs pF) and G5C09 (0.33 vs 33.3 µF decimal slips); turns ratio vs impedance ratio.

Vocabulary: mutual inductance, turns ratio, step-up/step-down, impedance transformation, series/parallel equivalents.

### SWR note (cross-subelement)

No numeric SWR question exists in G1–G5 (that math lives in G9), but G4B10 asks what a directional wattmeter can determine. The book should state: SWR = (1+√(P_r/P_f))/(1−√(P_r/P_f)) from forward/reflected power, and for a resistive mismatch SWR = Z_load/Z_line (or its inverse, ≥ 1) — e.g., a 100 Ω load on 50 Ω coax is 2:1. One example suffices at this level.

---

## Flags for the canon assembler

### 60 m / current-rule status (as of 2026-07)

The FCC Report & Order in WT Docket 23-83 (FCC 25-60, adopted 2025-09-23, released 2025-12-09; Federal Register 91 FR 1430, 2026-01-14; effective 2026-02-13) implemented WRC-15 for 60 m:

- NEW: contiguous secondary allocation 5351.5–5366.5 kHz, max 9.15 W ERP, max 2.8 kHz bandwidth.
- KEPT: four discrete channels (center 5332, 5348, 5373, 5405 kHz) at 100 W ERP (PEP referenced to a half-wave dipole).
- REMOVED: the old 5358.5 kHz channel (inside the new sub-band).
- Current rule text: 47 CFR 97.303(h)(3) (frequencies + 2.8 kHz for ALL 60 m spectrum) and 97.313(i) (power limits + the antenna-gain record-keeping requirement survives verbatim).

Question-level impact:

- NO active pool question conflicts with current rules. The NCVEC 6th errata (2026-02-04) already withdrew the two questions the rule change broke: G1A04 ("band restricted to specific channels" — 60 m, now false) and G1C09 ("maximum power on 60 m" — 100 W ERP, now segment-dependent).
- G1C03 (2.8 kHz) — answer still CORRECT; printed citation [97.303(h)(1)] is stale, the provision is now 97.303(h)(3).
- G1C04 (gain records for non-dipole antennas) — answer still CORRECT; requirement moved to 97.313(i); printed citation [97.303(i)] is stale (that paragraph is now the 7.2–7.3 MHz broadcast-sharing rule).
- G1A01 and G1D03 mention 60 m only in distractors — unaffected. G3C05 mentions the 60 m band as physics — unaffected.
- Chapter guidance: teach the new two-part structure (segment + four channels, two power limits) as context, but exam answers are as keyed.

### Other current-rule spot checks (no conflicts found)

200 ft tower threshold (97.15), CSCE 365 days (97.9(b)), expired-license Element 2 credit (97.505), VE rules (97.509), RACES 1 hr/week (97.407(d)(4)), SS 10 W PEP (97.313(j)), 30 m 200 W PEP (97.313(c)(1)) — all match current Part 97 as amended through 91 FR 1431 (2026-01-14).

### Ambiguous / surprising items worth a chapter aside

- G1B05's printed citation "[97.111((5)(b)]" is malformed (source typo); intended 97.111(a)(5)(b).
- G1B09 vs G1E10: two different beacon facts (auto-beacon segment 28.20–28.30 MHz vs beacon-network frequencies to avoid). G1B09's distractor 21.08–21.09 MHz is a real segment — for auto-controlled digital stations, not beacons; easy conflation.
- G2E01 (RTTY AFSK → LSB) contradicts the student's instinct from G2E05 (FT8/JT → USB). Both conventions are tested; teach them as a pair.
- G4D08's LSB example (7.178 MHz displayed) lands its lower edge exactly on the General 40 m phone boundary 7.175 MHz (G1A05) — nice cross-reference.
- G5B10 (20.6% per dB) is the only pool question requiring a non-round dB computation; give the reader the 10^(-0.1) = 0.794 derivation.
- G5C08 mixes nF and pF; answer 10.750 nF with the trailing zero as printed.
- G1D05/G1D12 asymmetry (US license needed to run a US station from abroad; only foreign rules when running a foreign station from the US) surprises students.
- G1E02: a Technician can talk THROUGH a 10 m repeater only if the repeater's control operator is General+ — repeater privilege follows the repeater's control operator, not the user.
- Numbering gaps G1A04, G1C08, G1C09, G1C10, G1E09 are errata deletions (see canon/ingestion-report.md), not omissions in this analysis.

## Coverage verification

Owned question IDs (249): all IDs in pool-general.json with subelement in {G1,G2,G3,G4,G5}. A script check (python3, re-scan of this file) confirms every owned ID is cited at least once in the matching subelement section above. Groups named: G1A–G1E, G2A–G2E, G3A–G3C, G4A–G4E, G5A–G5C (21/21).
