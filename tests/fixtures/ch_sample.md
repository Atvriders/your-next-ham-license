## 1. AC Theory: Reactance, Impedance & Resonance

Your Technician ticket taught you Ohm's law for DC; on HF the same ideas stretch into AC, where capacitors and inductors oppose the flow with a frequency-dependent reactance. In this chapter you'll learn how reactance, impedance, and resonance fit together, and how little extra math you actually need.

### Reactance and Impedance
An inductor's reactance rises with frequency: $X_L = 2\pi f L$.

Impedance ties resistance and net reactance into one number: $Z = \sqrt{R^2 + X^2}$.

{{fig:sample}}

> **The math, if you want it:** at 7 MHz a one-microhenry inductor presents $X_L = 2\pi f L \approx 44$ ohms of reactance.

> **Worked example:** a circuit with 30 ohms of resistance and 40 ohms of reactance has $Z = \sqrt{30^2 + 40^2} = 50$ ohms of impedance.

**FACT:** The FCC regulates the amateur service in the United States.
**FACT:** The General exam has 35 questions, one drawn from each pool group.
**FACT:** Impedance combines resistance and reactance as the square root of the sum of their squares.

### Exam Focus
This chapter covers pool group G5B (sample).

> **G5B02** What is the impedance of a circuit with 30 ohms resistance and 40 ohms reactance?
> A. 10 ohms
> B. 35 ohms
> C. 50 ohms
> D. 70 ohms
> **Answer: C** — impedance is the root of the sum of the squares, so $\sqrt{30^2 + 40^2} = 50$.

### Key Takeaways
- Reactance opposes AC and depends on frequency.
- Impedance combines resistance and reactance: $Z = \sqrt{R^2 + X^2}$.
- Resonance is the frequency where inductive and capacitive reactance cancel.
