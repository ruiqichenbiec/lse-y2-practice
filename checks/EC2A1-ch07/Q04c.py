"""
Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.

Continuing: C and D now share one embankment. C builds $x_C$, D builds $x_D$, each pays its own cost, and both are protected by the total $X = x_C + x_D$. Each chooses its length taking the other's as given (a Nash equilibrium, Q7.2).

- (c) Find each farm's net utility.
"""
import sympy as sp

# --- solve: from the problem's data only ---
x_C, x_D = sp.symbols("x_C x_D", positive=True)
U_C = 36 * sp.log(x_C + x_D) - x_C**2 / 2
U_D = 24 * sp.log(x_C + x_D) - 2 * x_D
# Part (b) first: the Nash equilibrium, recomputed here from the two first-order conditions.
solutions = sp.solve([sp.Eq(sp.diff(U_C, x_C), 0), sp.Eq(sp.diff(U_D, x_D), 0)], [x_C, x_D], dict=True)
interior = [s for s in solutions if float(s[x_C]) > 0 and float(s[x_D]) > 0]
assert len(interior) == 1, interior
nash = interior[0]
# Net utilities at the Nash equilibrium, kept exact.
net_C = U_C.subs(nash)
net_D = U_D.subs(nash)

# --- compare ---
# The solution prints these to one decimal, so compare with round(value, 1).
EXPECTED_net_C = 85.0
EXPECTED_net_D = 41.6
EXPECTED_net_C_exact = 36 * sp.log(12) - sp.Rational(9, 2)
EXPECTED_net_D_exact = 24 * sp.log(12) - 18
assert round(float(net_C), 1) == EXPECTED_net_C, "C's net utility to one decimal"
assert round(float(net_D), 1) == EXPECTED_net_D, "D's net utility to one decimal"
assert sp.simplify(net_C - EXPECTED_net_C_exact) == 0, "C's net utility, exact form"
assert sp.simplify(net_D - EXPECTED_net_D_exact) == 0, "D's net utility, exact form"
print("PASS")
