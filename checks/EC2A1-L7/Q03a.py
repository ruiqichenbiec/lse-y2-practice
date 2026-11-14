"""
Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.

- (a) The fields are far apart, so each farm builds its own embankment. Find each farm's length.
"""
import sympy as sp

# --- solve: from the problem's data only ---
x = sp.symbols("x", positive=True)
# Each farm maximises its own benefit minus its own cost.
net_C = 36 * sp.log(x) - x**2 / 2   # farm C: benefit 36 ln x, own cost x^2/2
net_D = 24 * sp.log(x) - 2 * x      # farm D: benefit 24 ln x, contractor cost 2x

# First-order condition for each farm; keep the positive root (a length).
length_C = [s for s in sp.solve(sp.diff(net_C, x), x) if s.is_positive][0]
length_D = [s for s in sp.solve(sp.diff(net_D, x), x) if s.is_positive][0]

# Second-order check: both net utilities are concave on x > 0, so each root is a maximum.
assert sp.diff(net_C, x, 2).is_negative
assert sp.diff(net_D, x, 2).is_negative

# --- compare ---
EXPECTED_length_C = 6
EXPECTED_length_D = 12
assert sp.simplify(length_C - EXPECTED_length_C) == 0, (length_C, EXPECTED_length_C)
assert sp.simplify(length_D - EXPECTED_length_D) == 0, (length_D, EXPECTED_length_D)
print("PASS")
