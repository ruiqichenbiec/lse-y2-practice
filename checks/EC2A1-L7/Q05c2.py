"""
Data from item 103 (prompt): Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.
Data from item 103 (statement): Own costs and net utility. Each farm has its own cost $C_i(x)$, in money, with marginal cost $C_i'(x)$. Its net utility is its benefit from the barrier minus this cost.
Data from item 104 (prompt): Continuing: C and D now share one embankment. C builds $x_C$, D builds $x_D$, each pays its own cost, and both are protected by the total $X = x_C + x_D$. Each chooses its length taking the other's as given (a Nash equilibrium, item 102).
Problem EC2A1-L7-105, part (c) (prompt): Continuing: a planner chooses $x_C$ and $x_D$ to maximise the sum of the two net utilities of item 104.
- (c) Find each farm's net utility and their sum, and the sum of marginal benefits at the Nash length 12.
"""
import sympy as sp

# Net utilities of item 104 as functions of the two lengths (benefit from X = xC + xD minus own cost).
xC, xD = sp.symbols("x_C x_D", positive=True)
X = xC + xD
net_C = 36 * sp.log(X) - xC**2 / 2
net_D = 24 * sp.log(X) - 2 * xD

# Nash equilibrium of item 104: each farm's first-order condition, taking the other's length as given.
nash = sp.solve([sp.diff(net_C, xC), sp.diff(net_D, xD)], [xC, xD], dict=True)[0]
X_nash = sp.simplify(nash[xC] + nash[xD])

# Checks: each farm's own objective is concave in its own length (the FOC gives its best response),
# and both lengths are positive (interior, no corner).
assert sp.diff(net_C, xC, 2).subs(nash) < 0 and sp.diff(net_D, xD, 2).subs(nash) < 0, "not a best response"
assert nash[xC] > 0 and nash[xD] > 0, "corner solution"

# Sum of marginal benefits at total T: 36/T from C plus 24/T from D, evaluated at the Nash total.
T = sp.symbols("T", positive=True)
MB_sum = sp.simplify(sp.diff(36 * sp.log(T), T) + sp.diff(24 * sp.log(T), T))
MB_sum_nash = sp.simplify(MB_sum.subs(T, X_nash))

# Marginal cost of the length: the least-cost cost of total T is 2*T - 2 (C builds 2, D builds the rest),
# so one more unit costs 2; evaluated at the Nash total.
xC_lc = sp.solve(sp.diff(xC**2 / 2 + 2 * (T - xC), xC), xC)[0]
cost_T = sp.simplify(xC_lc**2 / 2 + 2 * (T - xC_lc))
MC_nash = sp.simplify(sp.diff(cost_T, T).subs(T, X_nash))

print("Nash lengths:", nash, "| X_nash =", X_nash)
print("sum of marginal benefits at Nash:", MB_sum_nash, "| marginal cost at Nash:", MC_nash)

# --- compare ---
EXPECTED_X_nash = 12
EXPECTED_MB_sum = 5
EXPECTED_MC = 2
assert sp.simplify(X_nash - EXPECTED_X_nash) == 0, (X_nash, EXPECTED_X_nash)
assert sp.simplify(MB_sum_nash - EXPECTED_MB_sum) == 0, (MB_sum_nash, EXPECTED_MB_sum)
assert sp.simplify(MC_nash - EXPECTED_MC) == 0, (MC_nash, EXPECTED_MC)
print("PASS")
