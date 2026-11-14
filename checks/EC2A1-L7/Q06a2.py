"""
Items 103-105, the data this part relies on:

Item 103: Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.

Item 104: Continuing: C and D now share one embankment. C builds $x_C$, D builds $x_D$, each pays its own cost, and both are protected by the total $X = x_C + x_D$. Each chooses its length taking the other's as given (a Nash equilibrium, item 102).

Item 105: Continuing: a planner chooses $x_C$ and $x_D$ to maximise the sum of the two net utilities of item 104.

Item 106: Continuing, with the one-decimal net utilities of items 104 and 105 (work with these values).

- (a) Compare each farm's net utility at the optimum with the Nash equilibrium. Is the move a Pareto improvement [appendix]?
"""
import sympy as sp

# --- solve: from the problem's data only ---
x_C, x_D = sp.symbols("x_C x_D", positive=True)
X = x_C + x_D

# Net utility = benefit from the embankment minus the farm's own cost (items 103-104).
U_C = 36 * sp.log(X) - x_C**2 / 2    # C's own cost is its effort, x_C^2 / 2
U_D = 24 * sp.log(X) - 2 * x_D       # D's own cost is its contractor bill, 2 x_D

# Nash equilibrium (item 104): each farm's first-order condition, the other's length taken as given.
nash = sp.solve([sp.diff(U_C, x_C), sp.diff(U_D, x_D)], [x_C, x_D], dict=True)[0]

# Planner (item 105): maximise the sum of the two net utilities.
W = U_C + U_D
opt = sp.solve([sp.diff(W, x_C), sp.diff(W, x_D)], [x_C, x_D], dict=True)[0]

# Second-order and corner checks: each own second derivative is negative at its equilibrium,
# the planner's Hessian is negative definite, and every length is positive (interior solutions).
assert float(sp.diff(U_C, x_C, 2).subs(nash)) < 0
assert float(sp.diff(U_D, x_D, 2).subs(nash)) < 0
assert sp.hessian(W, (x_C, x_D)).subs(opt).is_negative_definite
assert min(float(v) for v in list(nash.values()) + list(opt.values())) > 0

# The printed solution gives the net utilities to one decimal, and the prompt says to work with these values.
# So each number is rounded with round(float(value), 1) before it is compared; this is the solution's rounding.
def one_dp(value):
    return round(float(value), 1)

C_nash = one_dp(U_C.subs(nash))
D_nash = one_dp(U_D.subs(nash))
C_opt = one_dp(U_C.subs(opt))
D_opt = one_dp(U_D.subs(opt))

# Pareto improvement: nobody is worse off and somebody is better off than in the Nash equilibrium.
C_change = one_dp(C_opt - C_nash)
D_change = one_dp(D_opt - D_nash)
nobody_worse = (C_change >= 0) and (D_change >= 0)
somebody_better = (C_change > 0) or (D_change > 0)
pareto_improvement = nobody_worse and somebody_better
print("Nash:", C_nash, D_nash, "| optimum:", C_opt, D_opt, "| changes:", C_change, D_change, "| Pareto improvement:", pareto_improvement)

# --- compare ---
EXPECTED_D_nash = 41.6
EXPECTED_D_opt = 25.6
EXPECTED_pareto_improvement = False
assert D_nash == EXPECTED_D_nash, (D_nash, EXPECTED_D_nash)
assert D_opt == EXPECTED_D_opt, (D_opt, EXPECTED_D_opt)
assert D_opt < EXPECTED_D_nash, (D_opt, EXPECTED_D_nash)
assert pareto_improvement == EXPECTED_pareto_improvement, (pareto_improvement, EXPECTED_pareto_improvement)
print("PASS")
