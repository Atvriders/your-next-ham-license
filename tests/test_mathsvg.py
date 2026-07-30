from tools.mathsvg import render

def test_render_returns_inline_svg():
    svg = render("E = IR")
    assert svg.strip().startswith("<svg") and "</svg>" in svg

def test_render_is_self_contained():
    svg = render("c = f\\lambda")
    # namespace decls (xmlns="http://www.w3.org/2000/svg") are fine; external RESOURCE refs are not:
    assert "<image" not in svg
    assert 'xlink:href="http' not in svg and 'href="http' not in svg.replace('xmlns', '')
    assert "@import" not in svg

def test_render_handles_subscripts_and_abs():
    svg = render("f_{IF} = |f_{RF} - f_{LO}|")
    assert svg.strip().startswith("<svg")


# --- The General formula set (Appendix B): every form the course teaches ---
# must render to inline SVG at build time (audit check #4 is the backstop).

def _renders_svg(expr):
    svg = render(expr)
    assert svg.strip().startswith("<svg") and "</svg>" in svg
    return svg

def test_render_inductive_reactance():
    _renders_svg("X_L = 2\\pi f L")

def test_render_capacitive_reactance_fraction():
    _renders_svg("X_C = \\frac{1}{2\\pi f C}")

def test_render_capacitive_reactance_paren_form():
    _renders_svg("X_C = 1/(2\\pi f C)")

def test_render_resonant_frequency():
    _renders_svg("f_r = \\frac{1}{2\\pi\\sqrt{LC}}")

def test_render_impedance_magnitude():
    _renders_svg("Z = \\sqrt{R^2 + X^2}")

def test_render_swr_gamma_form():
    _renders_svg("SWR = \\frac{1 + |\\Gamma|}{1 - |\\Gamma|}")

def test_render_swr_impedance_form():
    _renders_svg("SWR = \\frac{Z_{load}}{Z_0}")

def test_render_db_power_form():
    _renders_svg("dB = 10 \\log_{10}(P_1/P_0)")

def test_render_db_voltage_form():
    _renders_svg("dB = 20 \\log_{10}(V_1/V_0)")
