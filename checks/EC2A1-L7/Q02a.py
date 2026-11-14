"""
Line 1: a river valley. A flood barrier of height $x$ metres costs 1 per metre and other consumption $c$ has price 1, so a farm paying for its own barrier from an endowment of 100 has $c = 100 - x$. Farm A's utility is $U_A = c + 6\\ln x$, farm B's is $U_B = c + 2\\ln x$. Each farm lives on its own river.

Continuing: the two farms share one river and one barrier. Farm $i$ contributes $g_i \\ge 0$ metres (1 per metre); the height is $G = g_A + g_B$ and protects both: $U_A = 100 - g_A + 6\\ln G$, $U_B = 100 - g_B + 2\\ln G$.

- (a) Find each farm's best response to the other's contribution.
"""
import sympy as sp

# --- solve: from the problem's data only ---
g_A, g_B = sp.symbols("g_A g_B")              # contributions in metres, g_i >= 0
G = g_A + g_B                                  # the height protects both farms
U_A = 100 - g_A + 6 * sp.log(G)                # farm A: cost 1 per metre of its own contribution
U_B = 100 - g_B + 2 * sp.log(G)                # farm B

# First-order conditions in each farm's own contribution: marginal utility of the height minus marginal cost 1.
foc_A = sp.diff(U_A, g_A)                      # 6/G - 1
foc_B = sp.diff(U_B, g_B)                      # 2/G - 1

# Interior roots of the first-order conditions.
root_A = sp.solve(sp.Eq(foc_A, 0), g_A)[0]     # 6 - g_B
root_B = sp.solve(sp.Eq(foc_B, 0), g_B)[0]     # 2 - g_A

# Second-order check: each utility is concave in its own contribution (second derivatives -6/G^2 and -2/G^2).
assert sp.diff(U_A, g_A, 2).subs({g_A: 1, g_B: 1}) < 0
assert sp.diff(U_B, g_B, 2).subs({g_A: 1, g_B: 1}) < 0
# Corner check: when the root is negative (g_B > 6 for A, g_A > 2 for B), the marginal utility at 0 is already
# negative, so the best response is the corner 0. Checked at g_B = 8 and g_A = 5.
assert foc_A.subs({g_A: 0, g_B: 8}) < 0
assert foc_B.subs({g_A: 5, g_B: 0}) < 0

# Best response on g >= 0: the interior root if it is nonnegative, otherwise the corner 0.
BR_A = sp.Max(0, root_A)                       # max{0, 6 - g_B}
BR_B = sp.Max(0, root_B)                       # max{0, 2 - g_A}

# --- compare ---
EXPECTED_BR_A_at_gB_0 = 6
EXPECTED_BR_A_at_gB_2 = 4
EXPECTED_BR_A_at_gB_8 = 0
EXPECTED_BR_B_at_gA_0 = 2
EXPECTED_BR_B_at_gA_1 = 1
EXPECTED_BR_B_at_gA_5 = 0
assert sp.simplify(BR_A.subs(g_B, 0) - EXPECTED_BR_A_at_gB_0) == 0, (BR_A.subs(g_B, 0), EXPECTED_BR_A_at_gB_0)
assert sp.simplify(BR_A.subs(g_B, 2) - EXPECTED_BR_A_at_gB_2) == 0, (BR_A.subs(g_B, 2), EXPECTED_BR_A_at_gB_2)
assert sp.simplify(BR_A.subs(g_B, 8) - EXPECTED_BR_A_at_gB_8) == 0, (BR_A.subs(g_B, 8), EXPECTED_BR_A_at_gB_8)
assert sp.simplify(BR_B.subs(g_A, 0) - EXPECTED_BR_B_at_gA_0) == 0, (BR_B.subs(g_A, 0), EXPECTED_BR_B_at_gA_0)
assert sp.simplify(BR_B.subs(g_A, 1) - EXPECTED_BR_B_at_gA_1) == 0, (BR_B.subs(g_A, 1), EXPECTED_BR_B_at_gA_1)
assert sp.simplify(BR_B.subs(g_A, 5) - EXPECTED_BR_B_at_gA_5) == 0, (BR_B.subs(g_A, 5), EXPECTED_BR_B_at_gA_5)
print("PASS")
