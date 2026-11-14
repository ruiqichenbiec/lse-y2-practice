"""
Data from Q7.3 (prompt): Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.
Data from Q7.3 (statement): Own costs and net utility. Each farm has its own cost $C_i(x)$, in money, with marginal cost $C_i'(x)$. Its net utility is its benefit from the barrier minus this cost.
Data from Q7.4 (prompt): Continuing: C and D now share one embankment. C builds $x_C$, D builds $x_D$, each pays its own cost, and both are protected by the total $X = x_C + x_D$. Each chooses its length taking the other's as given (a Nash equilibrium, Q7.2).
Problem Q7.5, part (b) (prompt): Continuing: a planner chooses $x_C$ and $x_D$ to maximise the sum of the two net utilities of Q7.4.
- (b) Find the efficient length $X^*$ (you should get 30) and each farm's share.
"""
import sympy as sp

# Planner's problem from Q7.3-Q7.4: maximise the sum of the two net utilities over xC and xD.
# Net utility = benefit minus own cost (C: 36 ln X - xC**2/2; D: 24 ln X - 2*xD), with X = xC + xD.
xC, xD = sp.symbols("x_C x_D", positive=True)
X = xC + xD
net_C = 36 * sp.log(X) - xC**2 / 2
net_D = 24 * sp.log(X) - 2 * xD
W = net_C + net_D

# First-order conditions: both partial derivatives of W are zero.
sol = sp.solve([sp.diff(W, xC), sp.diff(W, xD)], [xC, xD], dict=True)[0]
x_C_star = sp.simplify(sol[xC])
x_D_star = sp.simplify(sol[xD])
X_star = sp.simplify(x_C_star + x_D_star)

# Checks: both lengths positive (interior solution), negative definite Hessian (a maximum).
assert x_C_star > 0 and x_D_star > 0, "corner solution"
H = sp.hessian(W, (xC, xD)).subs(sol)
assert H[0, 0] < 0 and H.det() > 0, "critical point is not a maximum"

# Samuelson rule: the sum of marginal benefits (36/T + 24/T) equals the marginal cost of total T.
# Least-cost cost of total T: C builds 2 (where its marginal cost x_C equals 2) and D builds the rest, so cost = 2*T - 2.
T = sp.symbols("T", positive=True)
xC_lc = sp.solve(sp.diff(xC**2 / 2 + 2 * (T - xC), xC), xC)[0]
cost_T = sp.simplify(xC_lc**2 / 2 + 2 * (T - xC_lc))
MC_T = sp.diff(cost_T, T)
MB_T = sp.diff(36 * sp.log(T), T) + sp.diff(24 * sp.log(T), T)
gap = sp.simplify((MB_T - MC_T).subs(T, X_star))
assert gap == 0, "Samuelson rule does not hold at X_star"

print("X* =", X_star, "| x_C =", x_C_star, "| x_D =", x_D_star)

# --- compare ---
EXPECTED_X_star = 30
EXPECTED_x_C = 2
EXPECTED_x_D = 28
assert sp.simplify(X_star - EXPECTED_X_star) == 0, (X_star, EXPECTED_X_star)
assert sp.simplify(x_C_star - EXPECTED_x_C) == 0, (x_C_star, EXPECTED_x_C)
assert sp.simplify(x_D_star - EXPECTED_x_D) == 0, (x_D_star, EXPECTED_x_D)
print("PASS")
