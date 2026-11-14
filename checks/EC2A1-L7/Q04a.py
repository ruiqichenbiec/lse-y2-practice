"""
Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.

Continuing: C and D now share one embankment. C builds $x_C$, D builds $x_D$, each pays its own cost, and both are protected by the total $X = x_C + x_D$. Each chooses its length taking the other's as given (a Nash equilibrium, item 102).

- (a) Write each farm's net utility as a function of $x_C$ and $x_D$, and its first-order condition.
"""
import sympy as sp

# --- solve: from the problem's data only ---
x_C, x_D = sp.symbols("x_C x_D", positive=True)
total = x_C + x_D                          # X: both farms are protected by the total length
benefit_C = 36 * sp.log(total)             # C's benefit from the embankment (its utility is m + 36 ln X)
benefit_D = 24 * sp.log(total)             # D's benefit (its utility is m + 24 ln X)
cost_C = x_C**2 / 2                        # C builds with its own labour: effort cost x_C^2 / 2
cost_D = 2 * x_D                           # D pays a contractor: cost 2 x_D
U_C = benefit_C - cost_C                   # net utility: benefit minus the farm's own cost (money m aside)
U_D = benefit_D - cost_D
foc_C = sp.diff(U_C, x_C)                  # first-order condition: derivative with respect to its OWN length
foc_D = sp.diff(U_D, x_D)

# --- compare ---
EXPECTED_U_C = 36 * sp.log(x_C + x_D) - x_C**2 / 2
EXPECTED_U_D = 24 * sp.log(x_C + x_D) - 2 * x_D
EXPECTED_foc_C = 36 / (x_C + x_D) - x_C
EXPECTED_foc_D = 24 / (x_C + x_D) - 2
assert sp.simplify(U_C - EXPECTED_U_C) == 0, (U_C, EXPECTED_U_C)
assert sp.simplify(U_D - EXPECTED_U_D) == 0, (U_D, EXPECTED_U_D)
assert sp.simplify(foc_C - EXPECTED_foc_C) == 0, (foc_C, EXPECTED_foc_C)
assert sp.simplify(foc_D - EXPECTED_foc_D) == 0, (foc_D, EXPECTED_foc_D)
print("PASS")
