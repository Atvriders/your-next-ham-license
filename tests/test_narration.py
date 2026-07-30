from tools.narration import strip_markup, speak_math, speak_figures

def test_strip_markup_removes_emphasis_and_refs():
    assert strip_markup("*hi* and **bold** {{fig:x}}") == "hi and bold"

def test_speak_math_ohms_law():
    assert speak_math("by $E = IR$ here") == "by E equals I R here"

def test_speak_math_symbols():
    assert speak_math("$c = f\\lambda$") == "c equals f lambda"
    assert speak_math("$\\Delta f \\approx f v / c$") == "delta f approximately f v over c"

def test_speak_math_greek_letters():
    assert speak_math("$\\lambda = 300 / f$") == "lambda equals 300 over f"
    assert speak_math("$\\eta = P_{out} / P_{in}$") == "eta equals P out over P in"
    assert speak_math("$X_L = 2\\pi f L$") == "X L equals 2 pi f L"

def test_speak_math_subscripts_are_spoken_plain():
    assert speak_math("$X_L = X_C$") == "X L equals X C"
    assert speak_math("$SWR = Z_{load}/Z_0$") == "S W R equals Z load over Z 0"

def test_speak_math_conventional_subscripts():
    # The book's own prose conventions: peak-to-peak, RMS, average, max.
    assert speak_math("$V_{rms} = V_{peak}/\\sqrt{2} \\approx 0.707 \\times V_{peak}$") == \
        "V R M S equals V peak over the square root of 2, approximately 0.707 times V peak"
    assert speak_math("$V_{pp} = 2\\sqrt{2} \\times V_{rms} \\approx 2.828 \\times V_{rms}$") == \
        "V peak-to-peak equals 2 times the square root of 2, times V R M S approximately 2.828 times V R M S"
    assert speak_math("$BW \\approx 2 \\times (D + f_{max})$") == \
        "B W approximately 2 times D plus f max"
    assert speak_math("$P_{avg} = 100 \\times 0.4 \\times 0.5 = 20\\ W$") == \
        "P average equals 100 times 0.4 times 0.5 equals 20 W"

def test_speak_math_square_root():
    assert speak_math("$|Z| = \\sqrt{R^2 + X^2}$") == \
        "magnitude of Z equals the square root of R squared plus X squared"
    assert speak_math("$|Z| = \\sqrt{50^2 + 50^2} \\approx 70.7\\ \\Omega$") == \
        "magnitude of Z equals the square root of 50 squared plus 50 squared, approximately 70.7 ohms"

def test_speak_math_square_root_in_denominator():
    assert speak_math("$f = 1/(2\\pi\\sqrt{LC})$") == \
        "f equals 1 over 2 pi times the square root of L C"
    assert speak_math("$X_C = 1/(2\\pi f C)$") == "X C equals 1 over 2 pi f C"

def test_speak_math_fraction():
    assert speak_math("$f = \\frac{1}{2\\pi\\sqrt{LC}}$") == \
        "f equals 1 over 2 pi times the square root of L C"

def test_speak_math_swr_from_power_ratio():
    assert speak_math("$SWR = (1+\\sqrt{P_r/P_f})/(1-\\sqrt{P_r/P_f})$") == \
        "S W R equals 1 plus the square root of P r over P f, over 1 minus the square root of P r over P f"

def test_speak_math_powers():
    assert speak_math("$2^2 = 4$") == "2 squared equals 4"
    assert speak_math("$10^{20}$") == "10 to the 20th"
    assert speak_math("$10^{20/10} = 100$") == "10 to the power of 20 over 10 equals 100"

def test_speak_math_squared_parenthesized_group():
    assert speak_math("$Z_p/Z_s = (N_p/N_s)^2$") == \
        "Z p over Z s equals the quantity N p over N s, squared"
    assert speak_math("$PEP = V_{pp}^2/(8R)$") == \
        "P E P equals V peak-to-peak squared over 8 R"

def test_speak_math_decibels():
    assert speak_math("$dB = 10 \\log_{10}(P_2/P_1)$") == \
        "d B equals 10 log base 10 of P 2 over P 1"
    assert speak_math("$dBi = dBd + 2.15$") == "d B i equals d B d plus 2.15"
    assert speak_math("$\\mathrm{dB}$") == "dB"

def test_speak_math_times_and_plain_formulas():
    assert speak_math("$V = I \\times R$") == "V equals I times R"
    assert speak_math("$P = V \\times I = I^2 \\times R = V^2 / R$") == \
        "P equals V times I equals I squared times R equals V squared over R"
    assert speak_math("$V_s = V_p \\times (N_s/N_p)$") == \
        "V s equals V p times N s over N p"

def test_speak_math_antenna_lengths():
    assert speak_math("$L = 468 / f$") == "L equals 468 over f"
    assert speak_math("$L = 234 / f$") == "L equals 234 over f"

def test_speak_math_arithmetic():
    assert speak_math("$14.205 + 0.005 = 14.210$") == "14.205 plus 0.005 equals 14.210"

def test_speak_math_degrees_and_angles():
    assert speak_math("$45^\\circ$") == "45 degrees"
    assert speak_math("$V \\angle 45^\\circ$") == "V angle 45 degrees"

def test_speak_math_comparison_and_misc_commands():
    assert speak_math("$a \\leq b \\geq c$") == \
        "a less than or equal to b greater than or equal to c"
    assert speak_math("$a \\cdot b$") == "a times b"
    assert speak_math("$\\mu F$") == "micro F"

def test_speak_figures_inserts_description():
    out = speak_figures("see {{fig:tank}} now", {"tank": ("4", "a spark-gap tank circuit")})
    assert out == "see (Figure 4. a spark-gap tank circuit.) now"
