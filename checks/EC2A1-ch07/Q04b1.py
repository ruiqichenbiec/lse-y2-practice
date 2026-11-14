"""
Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.

Continuing: C and D now share one embankment. C builds $x_C$, D builds $x_D$, each pays its own cost, and both are protected by the total $X = x_C + x_D$. Each chooses its length taking the other's as given (a Nash equilibrium, Q7.2).

- (b) Solve the two conditions together (you should get $x_C = 3$, $x_D = 9$, $X = 12$), and check that each length is a best response to the other.
"""
import sympy as sp

# --- solve: from the problem's data only ---
x_C, x_D = sp.symbols("x_C x_D", positive=True)
X = x_C + x_D
U_C = 36 * sp.log(X) - x_C**2 / 2
U_D = 24 * sp.log(X) - 2 * x_D
foc_C = sp.diff(U_C, x_C)                  # 36/X - x_C
foc_D = sp.diff(U_D, x_D)                  # 24/X - 2
# Both first-order conditions must hold together.
solutions = sp.solve([sp.Eq(foc_C, 0), sp.Eq(foc_D, 0)], [x_C, x_D], dict=True)
# Corner check: keep the solution in which both lengths are strictly positive.
interior = [s for s in solutions if float(s[x_C]) > 0 and float(s[x_D]) > 0]
assert len(interior) == 1, interior
x_C_star = interior[0][x_C]
x_D_star = interior[0][x_D]
X_star = x_C_star + x_D_star
# Second-order check: each farm's own second derivative is negative at the solution.
point = {x_C: x_C_star, x_D: x_D_star}
assert float(sp.diff(foc_C, x_C).subs(point)) < 0
assert float(sp.diff(foc_D, x_D).subs(point)) < 0

# --- compare ---
EXPECTED_X = 12
EXPECTED_x_C = 3
EXPECTED_x_D = 9
assert sp.simplify(X_star - EXPECTED_X) == 0, "total length X"
assert sp.simplify(x_C_star - EXPECTED_x_C) == 0, "length of C"
assert sp.simplify(x_D_star - EXPECTED_x_D) == 0, "length of D"
print("PASS")
