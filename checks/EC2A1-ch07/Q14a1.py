"""
Three villages X, Y and Z in a valley share a flood-warning mast. A mast of height $G$ gives village $i$ the benefit $B_i(G) = a_iG - \\tfrac12 G^2$, so its marginal benefit is $MB_i(G) = a_i - G$, with $a_X = 10$, $a_Y = 9$ and $a_Z = 8$. Each metre of mast costs 6 (money in £ thousand). Village $i$ pays for the $g_i \\ge 0$ metres it contributes, so its payoff is $B_i(G) - 6g_i$, where $G = g_X + g_Y + g_Z$. The villages choose their contributions simultaneously. (Total 20 marks.)

- (a) Find each village's best response as a function of the total $G_{-i}$ contributed by the other two. Find the Nash equilibrium, and check that Y and Z do not want to contribute. (5 marks)
"""
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
points = range(7)                               # other villages' total G_{-i} = 0, 1, ..., 6
vals_X = [BR["X"].subs(R, t) for t in points]
vals_Y = [BR["Y"].subs(R, t) for t in points]
vals_Z = [BR["Z"].subs(R, t) for t in points]

# --- compare ---
EXPECTED_X = [4, 3, 2, 1, 0, 0, 0]
EXPECTED_Y = [3, 2, 1, 0, 0, 0, 0]
EXPECTED_Z = [2, 1, 0, 0, 0, 0, 0]
assert vals_X == EXPECTED_X, (vals_X, EXPECTED_X)
assert vals_Y == EXPECTED_Y, (vals_Y, EXPECTED_Y)
assert vals_Z == EXPECTED_Z, (vals_Z, EXPECTED_Z)
print("PASS")
