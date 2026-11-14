"""
Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.

- (a) The fields are far apart, so each farm builds its own embankment. Find each farm's length.
- (b) Find each farm's net utility.
"""
import sympy as sp

# --- solve: from the problem's data only ---
x = sp.symbols("x", positive=True)
# Each farm maximises its own benefit minus its own cost.
net_C = 36 * sp.log(x) - x**2 / 2   # farm C: benefit 36 ln x, own cost x^2/2
net_D = 24 * sp.log(x) - 2 * x      # farm D: benefit 24 ln x, contractor cost 2x

# Part (a), recomputed here: first-order condition, positive root (the length).
length_C = [s for s in sp.solve(sp.diff(net_C, x), x) if s.is_positive][0]
length_D = [s for s in sp.solve(sp.diff(net_D, x), x) if s.is_positive][0]

# Second-order check: both net utilities are concave on x > 0, so each root is a maximum.
assert sp.diff(net_C, x, 2).is_negative
assert sp.diff(net_D, x, 2).is_negative

# Part (b): net utility at each farm's own length, in exact form.
net_utility_C = net_C.subs(x, length_C)
net_utility_D = net_D.subs(x, length_D)

# --- compare ---
# The printed solution rounds to one decimal place, so compare after round(..., 1).
EXPECTED_net_utility_C = 46.5
EXPECTED_net_utility_D = 35.6
assert round(float(net_utility_C), 1) == EXPECTED_net_utility_C, (float(net_utility_C), EXPECTED_net_utility_C)
assert round(float(net_utility_D), 1) == EXPECTED_net_utility_D, (float(net_utility_D), EXPECTED_net_utility_D)
print("PASS")
