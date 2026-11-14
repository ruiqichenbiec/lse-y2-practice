"""
Three villages X, Y and Z in a valley share a flood-warning mast. A mast of height $G$ gives village $i$ the benefit $B_i(G) = a_iG - \\tfrac12 G^2$, so its marginal benefit is $MB_i(G) = a_i - G$, with $a_X = 10$, $a_Y = 9$ and $a_Z = 8$. Each metre of mast costs 6 (money in £ thousand). Village $i$ pays for the $g_i \\ge 0$ metres it contributes, so its payoff is $B_i(G) - 6g_i$, where $G = g_X + g_Y + g_Z$. The villages choose their contributions simultaneously. (Total 20 marks.)

- (d) Three more villages, each with $a = 9$ like Y, join the valley (six villages in all). Find the Nash equilibrium and the efficient height, and compute the deadweight loss. (5 marks)
"""
import itertools

import sympy as sp

# --- solve: from the problem's data only ---
cost = 6                                        # money per metre of mast
a = {"X": 10, "Y": 9, "Z": 8}                   # a_i: intercepts of the marginal benefits
for k in (1, 2, 3):                             # three newcomers, each with a = 9 like Y
    a[f"N{k}"] = a["Y"]
g = sp.Symbol("g")                              # village i's own contribution (metres)
R = sp.Symbol("R")                              # total contributed by the other villages, G_{-i}


def best_response(a_i):
    G = g + R                                   # the height when village i adds g to R
    payoff = a_i * G - G**2 / 2 - cost * g      # village i's payoff as a function of g
    assert sp.diff(payoff, g, 2) < 0            # concave in its own contribution: a maximum
    root = sp.solve(sp.Eq(sp.diff(payoff, g), 0), g)[0]   # first-order condition a_i - G - cost = 0
    return sp.Max(0, root)                      # corner solution g = 0 when the root is negative


BR = {name: best_response(a_i) for name, a_i in a.items()}


def nash_candidates():
    # Try each set S of contributing villages (all others give 0). Each contributor's first-order
    # condition fixes the common height at a_i - cost, and every other village must sit at its corner there.
    names = list(a)
    found = []
    for k in range(len(names) + 1):
        for S in itertools.combinations(names, k):
            if S:
                heights = {a[i] - cost for i in S}
                if len(heights) != 1 or min(heights) < 0:
                    continue
                height = sp.Integer(heights.pop())
            else:
                height = sp.Integer(0)
            if all(BR[j].subs(R, height) == 0 for j in names if j not in S):
                found.append((S, height))
    return found


equilibria = nash_candidates()
S_ne, G_nash = equilibria[0]                    # the Nash height (uniqueness is checked below)

G = sp.Symbol("G", nonnegative=True)            # mast height (total metres)
B = {name: a_i * G - G**2 / 2 for name, a_i in a.items()}     # benefit of each village
sum_mb = sum(sp.diff(B[name], G) for name in a)               # vertical sum of the six marginal benefits
W = sum(B.values()) - cost * G                  # total net benefit
assert sp.diff(W, G, 2) < 0
G_eff = sp.solve(sp.Eq(sum_mb, cost), G)[0]     # efficient height

# Deadweight loss at the Nash height: the surplus lost on the heights between the Nash and the efficient one.
DWL = sp.integrate(sum_mb - cost, (G, G_nash, G_eff))
base = G_eff - G_nash                           # width of the triangle
height = (sum_mb - cost).subs(G, G_nash)        # gap between the vertical sum and MC at the Nash height
assert sp.simplify(DWL - sp.Rational(1, 2) * base * height) == 0   # the same as the triangle's area

# --- compare ---
EXPECTED_count = 1
EXPECTED_G_nash = 4
EXPECTED_G_eff = 8
EXPECTED_base = 4
EXPECTED_height = 24
EXPECTED_DWL = 48
assert len(equilibria) == EXPECTED_count, (equilibria, EXPECTED_count)
assert sp.simplify(G_nash - EXPECTED_G_nash) == 0, (G_nash, EXPECTED_G_nash)
assert sp.simplify(G_eff - EXPECTED_G_eff) == 0, (G_eff, EXPECTED_G_eff)
assert sp.simplify(base - EXPECTED_base) == 0, (base, EXPECTED_base)
assert sp.simplify(height - EXPECTED_height) == 0, (height, EXPECTED_height)
assert sp.simplify(DWL - EXPECTED_DWL) == 0, (DWL, EXPECTED_DWL)
print("PASS")
