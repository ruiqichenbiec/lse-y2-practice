"""
Data from Q7.3 (prompt): Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.
Data from Q7.3 (statement): Own costs and net utility. Each farm has its own cost $C_i(x)$, in money, with marginal cost $C_i'(x)$. Its net utility is its benefit from the barrier minus this cost.
Data from Q7.4 (prompt): Continuing: C and D now share one embankment. C builds $x_C$, D builds $x_D$, each pays its own cost, and both are protected by the total $X = x_C + x_D$. Each chooses its length taking the other's as given (a Nash equilibrium, Q7.2).
Problem Q7.5, part (c) (prompt): Continuing: a planner chooses $x_C$ and $x_D$ to maximise the sum of the two net utilities of Q7.4.
- (c) Find each farm's net utility and their sum, and the sum of marginal benefits at the Nash length 12.
"""
import sympy as sp

# Planner's problem from Q7.3-Q7.4: maximise the sum of the two net utilities over xC and xD.
# Net utility = benefit minus own cost (C: 36 ln X - xC**2/2; D: 24 ln X - 2*xD), with X = xC + xD.
xC, xD = sp.symbols("x_C x_D", positive=True)
X = xC + xD
net_C = 36 * sp.log(X) - xC**2 / 2
net_D = 24 * sp.log(X) - 2 * xD
W = net_C + net_D

# Efficient split from the first-order conditions (both partial derivatives of W are zero).
sol = sp.solve([sp.diff(W, xC), sp.diff(W, xD)], [xC, xD], dict=True)[0]

# Checks: both lengths positive (interior solution), negative definite Hessian (a maximum).
assert sol[xC] > 0 and sol[xD] > 0, "corner solution"
H = sp.hessian(W, (xC, xD)).subs(sol)
assert H[0, 0] < 0 and H.det() > 0, "critical point is not a maximum"

# Net utilities at the efficient split: exact values, then rounded to one decimal as the prompt asks.
u_C = sp.N(net_C.subs(sol), 30)
u_D = sp.N(net_D.subs(sol), 30)
u_C_1dp = round(float(u_C), 1)
u_D_1dp = round(float(u_D), 1)
# The printed sum adds the one-decimal values (not the rounded exact sum).
total_1dp = round(u_C_1dp + u_D_1dp, 1)

print("exact:", u_C, u_D)
print("one decimal:", u_C_1dp, u_D_1dp, "| sum of one-decimal values:", total_1dp)

# --- compare ---
EXPECTED_u_C = 120.4
EXPECTED_u_D = 25.6
EXPECTED_total = 146.0
assert u_C_1dp == EXPECTED_u_C, (u_C_1dp, EXPECTED_u_C)
assert u_D_1dp == EXPECTED_u_D, (u_D_1dp, EXPECTED_u_D)
assert total_1dp == EXPECTED_total, (total_1dp, EXPECTED_total)
print("PASS")
