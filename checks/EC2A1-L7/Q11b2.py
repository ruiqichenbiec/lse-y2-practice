"""
Line 3: four students get £10 each and may put any part $x_i$ into an envelope; the experimenter doubles the total and shares it equally ($N = 4$, $m = 2$, $w = 10$).

- (b) Find the effect of one more pound given on a student's own payoff, and hence the Nash equilibrium. Find the profile maximising total payoff, and the payoffs there.
"""
import sympy as sp

# --- solve: from the problem's data only ---
w = sp.Integer(10)  # endowment of each student (pounds)
m = sp.Integer(2)   # multiplier applied to the envelope
N = sp.Integer(4)   # number of students

x = sp.symbols("x1 x2 x3 x4", nonnegative=True)                # contributions, 0 <= x_i <= w
payoff = [w - x[i] + m / N * sum(x) for i in range(4)]          # u_i = w - x_i + (m / N) * sum_j x_j

def best_response(i):
    # Student i chooses her own contribution in [0, w] with the others held fixed.
    # Her payoff is linear in x_i, so the maximum is at a stationary point or at a corner.
    u = payoff[i]
    stationary = sp.solve(sp.diff(u, x[i]), x[i])  # empty when the slope is a nonzero constant
    candidates = [sp.Integer(0), w] + stationary
    best = candidates[0]
    for c in candidates[1:]:
        if sp.simplify(u.subs(x[i], c) - u.subs(x[i], best)) > 0:
            best = c
    return best

# Nash equilibrium: every contribution is a best response to the others.
brs = [best_response(i) for i in range(4)]
ne = sp.solve([sp.Eq(x[i], brs[i]) for i in range(4)], x, dict=True)[0]
ne_profile = [ne[xi] for xi in x]
ne_payoffs = [sp.simplify(payoff[i].subs(dict(zip(x, ne_profile)))) for i in range(4)]

# --- compare ---
EXPECTED_contribution_each = 0
EXPECTED_payoff_each = 10
assert sp.simplify(ne_profile[0] - EXPECTED_contribution_each) == 0, (ne_profile[0], EXPECTED_contribution_each)
assert sp.simplify(ne_profile[1] - EXPECTED_contribution_each) == 0, (ne_profile[1], EXPECTED_contribution_each)
assert sp.simplify(ne_profile[2] - EXPECTED_contribution_each) == 0, (ne_profile[2], EXPECTED_contribution_each)
assert sp.simplify(ne_profile[3] - EXPECTED_contribution_each) == 0, (ne_profile[3], EXPECTED_contribution_each)
assert sp.simplify(ne_payoffs[0] - EXPECTED_payoff_each) == 0, (ne_payoffs[0], EXPECTED_payoff_each)
assert sp.simplify(ne_payoffs[1] - EXPECTED_payoff_each) == 0, (ne_payoffs[1], EXPECTED_payoff_each)
assert sp.simplify(ne_payoffs[2] - EXPECTED_payoff_each) == 0, (ne_payoffs[2], EXPECTED_payoff_each)
assert sp.simplify(ne_payoffs[3] - EXPECTED_payoff_each) == 0, (ne_payoffs[3], EXPECTED_payoff_each)
print("PASS")
