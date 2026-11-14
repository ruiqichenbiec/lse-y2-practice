"""
Items 103-105, the data this part relies on:

Item 103: Continuing downstream: farms C and D build an earth embankment of length $x$ (hundreds of metres). C uses its own labour, effort cost $C_C(x) = \\tfrac12 x^2$; D pays a contractor, $C_D(x) = 2x$. Utilities: $m + 36\\ln x$ (C) and $m + 24\\ln x$ (D), $m$ = money for consumption. Use $\\ln 6 \\approx 1.792$, $\\ln 12 \\approx 2.485$, $\\ln 30 \\approx 3.401$; round to one decimal.

Item 104: Continuing: C and D now share one embankment. C builds $x_C$, D builds $x_D$, each pays its own cost, and both are protected by the total $X = x_C + x_D$. Each chooses its length taking the other's as given (a Nash equilibrium, item 102).

Item 105: Continuing: a planner chooses $x_C$ and $x_D$ to maximise the sum of the two net utilities of item 104.

Item 106: Continuing, with the one-decimal net utilities of items 104 and 105 (work with these values).

- (b) At the optimum C pays D a sum $T$. Find the values of $T$ that leave both farms better off than in the Nash equilibrium.
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

# At the optimum C pays D a sum T (money enters the utilities one for one): C keeps C_opt - T, and D gets D_opt + T.
# C is better off than in Nash iff C_opt - T > C_nash, i.e. T < C_opt - C_nash.
# D is better off than in Nash iff D_opt + T > D_nash, i.e. T > D_nash - D_opt.
T_low = one_dp(D_nash - D_opt)
T_high = one_dp(C_opt - C_nash)
T_mid = one_dp((T_low + T_high) / 2)

def C_after(T):
    return one_dp(C_opt - T)

def D_after(T):
    return one_dp(D_opt + T)

# At each bound one farm is exactly at its Nash level (so not strictly better off); at the midpoint both are better off.
C_at_high = C_after(T_high)
D_at_low = D_after(T_low)
C_mid = C_after(T_mid)
D_mid = D_after(T_mid)

# Brute-force check of "exactly when" on payments in steps of 0.1, using the rounded utilities.
grid = [k / 10 for k in range(-50, 500)]
both_better = [C_after(t) > C_nash and D_after(t) > D_nash for t in grid]
inside = [T_low < t < T_high for t in grid]
assert both_better == inside

print("T low:", T_low, "| T high:", T_high, "| T mid:", T_mid, "| C at high:", C_at_high, "| D at low:", D_at_low, "| C mid:", C_mid, "| D mid:", D_mid)

# --- compare ---
EXPECTED_T_low = 16.0
EXPECTED_T_high = 35.4
EXPECTED_T_mid = 25.7
EXPECTED_C_nash = 85.0
EXPECTED_D_nash = 41.6
EXPECTED_C_mid = 94.7
EXPECTED_D_mid = 51.3
assert T_low == EXPECTED_T_low, (T_low, EXPECTED_T_low)
assert T_high == EXPECTED_T_high, (T_high, EXPECTED_T_high)
assert T_mid == EXPECTED_T_mid, (T_mid, EXPECTED_T_mid)
assert C_at_high == EXPECTED_C_nash, (C_at_high, EXPECTED_C_nash)
assert D_at_low == EXPECTED_D_nash, (D_at_low, EXPECTED_D_nash)
assert C_mid == EXPECTED_C_mid, (C_mid, EXPECTED_C_mid)
assert D_mid == EXPECTED_D_mid, (D_mid, EXPECTED_D_mid)
print("PASS")
