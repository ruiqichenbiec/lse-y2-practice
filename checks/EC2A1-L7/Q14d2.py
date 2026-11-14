"""
Three villages X, Y and Z in a valley share a flood-warning mast. A mast of height $G$ gives village $i$ the benefit $B_i(G) = a_iG - \\tfrac12 G^2$, so its marginal benefit is $MB_i(G) = a_i - G$, with $a_X = 10$, $a_Y = 9$ and $a_Z = 8$. Each metre of mast costs 6 (money in £ thousand). Village $i$ pays for the $g_i \\ge 0$ metres it contributes, so its payoff is $B_i(G) - 6g_i$, where $G = g_X + g_Y + g_Z$. The villages choose their contributions simultaneously. (Total 20 marks.)

- (d) Three more villages, each with $a = 9$ like Y, join the valley (six villages in all). Find the Nash equilibrium and the efficient height, and compute the deadweight loss. (5 marks)
"""
import sympy as sp

# --- solve: from the problem's data only ---
cost = 6                                        # money per metre of mast
a = {"X": 10, "Y": 9, "Z": 8}                   # a_i: intercepts of the marginal benefits
for k in (1, 2, 3):                             # three newcomers, each with a = 9 like Y
    a[f"N{k}"] = a["Y"]
G = sp.Symbol("G", nonnegative=True)            # mast height (total metres)
B = {name: a_i * G - G**2 / 2 for name, a_i in a.items()}     # benefit of each village
sum_mb = sum(sp.diff(B[name], G) for name in a)               # vertical sum of the six marginal benefits
# The efficient height maximises total net benefit: the sum of the benefits minus the cost of the mast.
W = sum(B.values()) - cost * G
assert sp.diff(W, G, 2) < 0                     # second-order condition: a maximum
G_eff = sp.solve(sp.Eq(sum_mb, cost), G)[0]     # first-order condition: sum of marginal benefits = marginal cost
assert sp.simplify(sp.diff(W, G).subs(G, G_eff)) == 0
sum_mb0 = sum_mb.subs(G, 0)                     # intercept of the sum of marginal benefits
slope = sp.diff(sum_mb, G)                      # slope of the sum of marginal benefits

# --- compare ---
EXPECTED_sum_mb0 = 54
EXPECTED_slope = -6
EXPECTED_G_eff = 8
assert sp.simplify(sum_mb0 - EXPECTED_sum_mb0) == 0, (sum_mb0, EXPECTED_sum_mb0)
assert sp.simplify(slope - EXPECTED_slope) == 0, (slope, EXPECTED_slope)
assert sp.simplify(G_eff - EXPECTED_G_eff) == 0, (G_eff, EXPECTED_G_eff)
print("PASS")
