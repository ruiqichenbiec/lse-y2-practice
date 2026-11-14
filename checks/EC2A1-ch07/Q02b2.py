"""
Line 1: a river valley. A flood barrier of height $x$ metres costs 1 per metre and other consumption $c$ has price 1, so a farm paying for its own barrier from an endowment of 100 has $c = 100 - x$. Farm A's utility is $U_A = c + 6\\ln x$, farm B's is $U_B = c + 2\\ln x$. Each farm lives on its own river.

Continuing: the two farms share one river and one barrier. Farm $i$ contributes $g_i \\ge 0$ metres (1 per metre); the height is $G = g_A + g_B$ and protects both: $U_A = 100 - g_A + 6\\ln G$, $U_B = 100 - g_B + 2\\ln G$.

- (b) Find the Nash equilibrium, and compare farm B's marginal utility with its marginal cost there.
"""
import sympy as sp

# --- solve: from the problem's data only ---
g_A, g_B = sp.symbols("g_A g_B")              # contributions in metres, g_i >= 0
G = g_A + g_B                                  # the height protects both farms
U_A = 100 - g_A + 6 * sp.log(G)                # farm A
U_B = 100 - g_B + 2 * sp.log(G)                # farm B

# Second-order check: each utility is concave in its own contribution (second derivatives -6/G^2 and -2/G^2).
assert sp.diff(U_A, g_A, 2).subs({g_A: 1, g_B: 1}) < 0
assert sp.diff(U_B, g_B, 2).subs({g_A: 1, g_B: 1}) < 0

# Best responses on g >= 0: interior root of the first-order condition, or the corner 0.
root_A = sp.solve(sp.Eq(sp.diff(U_A, g_A), 0), g_A)[0]    # 6 - g_B
root_B = sp.solve(sp.Eq(sp.diff(U_B, g_B), 0), g_B)[0]    # 2 - g_A
BR_A = sp.Max(0, root_A)                                   # max{0, 6 - g_B}
BR_B = sp.Max(0, root_B)                                   # max{0, 2 - g_A}

# A Nash equilibrium is a pair in which each contribution is the other's best response.
# Candidates: both farms contribute (both first-order conditions hold), only A, only B, or nobody (corners).
both = sp.solve([sp.Eq(sp.diff(U_A, g_A), 0), sp.Eq(sp.diff(U_B, g_B), 0)], [g_A, g_B], dict=True)
candidates = [(s[g_A], s[g_B]) for s in both]
candidates.append((BR_A.subs(g_B, 0), 0))                  # only A contributes: g_B = 0
candidates.append((0, BR_B.subs(g_A, 0)))                  # only B contributes: g_A = 0
candidates.append((0, 0))                                  # nobody contributes


def is_nash(a, b):
    # each contribution must be a best response to the other's
    ok_A = sp.simplify(a - BR_A.subs(g_B, b)) == 0
    ok_B = sp.simplify(b - BR_B.subs(g_A, a)) == 0
    return ok_A and ok_B


equilibria = [(a, b) for (a, b) in candidates if is_nash(a, b)]
g_A_star, g_B_star = equilibria[0]
G_star = g_A_star + g_B_star                               # total height at the equilibrium

# Farm B's marginal utility from the height H: U_B = 100 - g_B + 2 ln H, so dU_B/dH = 2/H.
H = sp.symbols("H", positive=True)
MU_B = sp.diff(2 * sp.log(H), H).subs(H, G_star)
# Farm B's marginal cost: a metre costs 1, so its cost is 1 * g_B.
cost_B = 1 * g_B
MC_B = sp.diff(cost_B, g_B)

# --- compare ---
EXPECTED_G = 6
EXPECTED_MU_B = sp.Rational(1, 3)
EXPECTED_MC_B = 1
assert sp.simplify(G_star - EXPECTED_G) == 0, (G_star, EXPECTED_G)
assert sp.simplify(MU_B - EXPECTED_MU_B) == 0, (MU_B, EXPECTED_MU_B)
assert sp.simplify(MC_B - EXPECTED_MC_B) == 0, (MC_B, EXPECTED_MC_B)
assert MU_B < EXPECTED_MC_B, (MU_B, EXPECTED_MC_B)
print("PASS")
