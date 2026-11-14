"""
Data from Q7.3 (prompt): Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.
Data from Q7.3 (statement): Own costs and net utility. Each farm has its own cost $C_i(x)$, in money, with marginal cost $C_i'(x)$. Its net utility is its benefit from the barrier minus this cost.
Data from Q7.4 (prompt): Continuing: C and D now share one embankment. C builds $x_C$, D builds $x_D$, each pays its own cost, and both are protected by the total $X = x_C + x_D$. Each chooses its length taking the other's as given (a Nash equilibrium, Q7.2).
Problem Q7.5, part (a) (prompt): Continuing: a planner chooses $x_C$ and $x_D$ to maximise the sum of the two net utilities of Q7.4.
- (a) Compare the farms' marginal costs, $x_C$ and 2. Up to what length should C build, and who builds the rest?
"""
import sympy as sp

# Model from Q7.3-Q7.4: C's own cost is xC**2/2, D's is 2*xD; both benefits depend on the
# total X = xC + xD (36 ln X for C, 24 ln X for D). Net utility = benefit minus own cost.
# The planner maximises the sum of the two net utilities.
xC, xD = sp.symbols("x_C x_D", positive=True)
X = xC + xD
net_C = 36 * sp.log(X) - xC**2 / 2
net_D = 24 * sp.log(X) - 2 * xD
W = net_C + net_D

# First-order conditions: both partial derivatives of W are zero.
sol = sp.solve([sp.diff(W, xC), sp.diff(W, xD)], [xC, xD], dict=True)[0]
xC_planner = sp.simplify(sol[xC])

# Corner check (both farms build a positive length) and second-order check (Hessian negative definite).
assert sol[xC] > 0 and sol[xD] > 0, "corner solution"
H = sp.hessian(W, (xC, xD)).subs(sol)
assert H[0, 0] < 0 and H.det() > 0, "critical point is not a maximum"

# Least-cost check: for a total T, C's share minimises xC**2/2 + 2*(T - xC), i.e. each unit goes to the cheaper farm.
T = sp.symbols("T", positive=True)
split_cost = xC**2 / 2 + 2 * (T - xC)
xC_least_cost = sp.simplify(sp.solve(sp.diff(split_cost, xC), xC)[0])
assert sp.diff(split_cost, xC, 2) > 0, "least-cost split is not a minimum"

print("planner x_C:", xC_planner, "| least-cost x_C:", xC_least_cost)

# --- compare ---
EXPECTED_x_C = 2
assert sp.simplify(xC_planner - EXPECTED_x_C) == 0, (xC_planner, EXPECTED_x_C)
assert sp.simplify(xC_least_cost - EXPECTED_x_C) == 0, (xC_least_cost, EXPECTED_x_C)
print("PASS")
