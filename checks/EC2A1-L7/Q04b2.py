"""
Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.

Continuing: C and D now share one embankment. C builds $x_C$, D builds $x_D$, each pays its own cost, and both are protected by the total $X = x_C + x_D$. Each chooses its length taking the other's as given (a Nash equilibrium, item 102).

- (b) Solve the two conditions together (you should get $x_C = 3$, $x_D = 9$, $X = 12$), and check that each length is a best response to the other.
"""
import sympy as sp

# --- solve: from the problem's data only ---
x_C, x_D = sp.symbols("x_C x_D", positive=True)
U_C = 36 * sp.log(x_C + x_D) - x_C**2 / 2
U_D = 24 * sp.log(x_C + x_D) - 2 * x_D
foc_C = sp.diff(U_C, x_C)                  # 36/(x_C + x_D) - x_C
foc_D = sp.diff(U_D, x_D)                  # 24/(x_C + x_D) - 2

# Best response of C to a given length y of D: its first-order condition solved for x_C.
y = sp.symbols("y", positive=True)
roots_C = sp.solve(sp.Eq(foc_C.subs(x_D, y), 0), x_C)
# x_C^2 + y x_C - 36 = 0 has roots with product -36, so exactly one root is positive for y > 0.
BR_C = [r for r in roots_C if float(r.subs(y, 1)) > 0]
assert len(BR_C) == 1, roots_C
BR_C = BR_C[0]

# Best response of D to a given length z of C.
z = sp.symbols("z", positive=True)
roots_D = sp.solve(sp.Eq(foc_D.subs(x_C, z), 0), x_D)
BR_D = [r for r in roots_D if float(r.subs(z, 1)) > 0]
assert len(BR_D) == 1, roots_D
BR_D = BR_D[0]

# Second-order and corner checks: each objective is strictly concave, and C's marginal benefit
# at x_C = 0 is positive, so C's best response is interior. D's is checked below (it is positive).
assert sp.diff(foc_C, x_C).is_negative
assert sp.diff(foc_D, x_D).is_negative
assert foc_C.subs(x_C, 0).is_positive

# --- compare ---
EXPECTED_BR_C_at_9 = 3
EXPECTED_BR_D_at_3 = 9
EXPECTED_zero = 0
assert sp.simplify(BR_C.subs(y, 9) - EXPECTED_BR_C_at_9) == 0, "C's best response to x_D = 9"
assert sp.simplify(BR_D.subs(z, 3) - EXPECTED_BR_D_at_3) == 0, "D's best response to x_C = 3"
assert sp.simplify(BR_C.subs(y, 9) - EXPECTED_zero) > 0, "C's best response is interior"
assert sp.simplify(BR_D.subs(z, 3) - EXPECTED_zero) > 0, "D's best response is interior"
print("PASS")
