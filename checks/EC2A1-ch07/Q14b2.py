"""
Three villages X, Y and Z in a valley share a flood-warning mast. A mast of height $G$ gives village $i$ the benefit $B_i(G) = a_iG - \\tfrac12 G^2$, so its marginal benefit is $MB_i(G) = a_i - G$, with $a_X = 10$, $a_Y = 9$ and $a_Z = 8$. Each metre of mast costs 6 (money in £ thousand). Village $i$ pays for the $g_i \\ge 0$ metres it contributes, so its payoff is $B_i(G) - 6g_i$, where $G = g_X + g_Y + g_Z$. The villages choose their contributions simultaneously. (Total 20 marks.)

- (a) Find each village's best response as a function of the total $G_{-i}$ contributed by the other two. Find the Nash equilibrium, and check that Y and Z do not want to contribute. (5 marks)
- (b) Find the efficient mast height using the sum of the marginal benefits. Compare it with the Nash height. (3 marks)
"""
import itertools

import sympy as sp

# --- solve: from the problem's data only ---
cost = 6                                        # money per metre of mast
a = {"X": 10, "Y": 9, "Z": 8}                   # a_i: intercepts of the marginal benefits
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
S_ne, G_nash = equilibria[0]                    # the Nash height from part (a) (uniqueness is checked below)

G = sp.Symbol("G", nonnegative=True)            # mast height (total metres)
B = {name: a_i * G - G**2 / 2 for name, a_i in a.items()}     # benefit of each village
sum_mb = sum(sp.diff(B[name], G) for name in a)               # sum of the marginal benefits
W = sum(B.values()) - cost * G                  # total net benefit
assert sp.diff(W, G, 2) < 0
G_eff = sp.solve(sp.Eq(sum_mb, cost), G)[0]     # efficient height from part (b)
sum_mb_nash = sum_mb.subs(G, G_nash)            # sum of the marginal benefits at the Nash height

# --- compare ---
EXPECTED_count = 1
EXPECTED_G_nash = 4
EXPECTED_G_eff = 7
EXPECTED_sum_mb = 15
EXPECTED_mc = 6
assert len(equilibria) == EXPECTED_count, (equilibria, EXPECTED_count)
assert sp.simplify(G_nash - EXPECTED_G_nash) == 0, (G_nash, EXPECTED_G_nash)
assert sp.simplify(G_eff - EXPECTED_G_eff) == 0, (G_eff, EXPECTED_G_eff)
assert G_nash < EXPECTED_G_eff, (G_nash, EXPECTED_G_eff)
assert sp.simplify(sum_mb_nash - EXPECTED_sum_mb) == 0, (sum_mb_nash, EXPECTED_sum_mb)
assert sum_mb_nash > EXPECTED_mc, (sum_mb_nash, EXPECTED_mc)
print("PASS")
