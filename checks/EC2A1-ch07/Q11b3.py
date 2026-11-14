"""
Line 3: four students get £10 each and may put any part $x_i$ into an envelope; the experimenter doubles the total and shares it equally ($N = 4$, $m = 2$, $w = 10$).

- (b) Find the effect of one more pound given on a student's own payoff, and hence the Nash equilibrium. Find the profile maximising total payoff, and the payoffs there.
"""
import itertools
import sympy as sp

# --- solve: from the problem's data only ---
w = sp.Integer(10)  # endowment of each student (pounds)
m = sp.Integer(2)   # multiplier applied to the envelope
N = sp.Integer(4)   # number of students

x = sp.symbols("x1 x2 x3 x4", nonnegative=True)              # contributions, 0 <= x_i <= w
payoff = [w - x[i] + m / N * sum(x) for i in range(4)]        # u_i = w - x_i + (m / N) * sum_j x_j
total = sp.expand(sum(payoff))                                # total payoff of the four students

# Interior stationary points of the total: all partial derivatives must vanish.
gradient = [sp.diff(total, xi) for xi in x]
interior = sp.solve(gradient, x, dict=True)                   # the gradient is a nonzero constant, so none

# Each contribution lies in [0, w]; the total is linear, so its maximum over the box is at a corner.
best_total = None
best_profile = None
for corner in itertools.product([sp.Integer(0), w], repeat=4):
    value = total.subs(dict(zip(x, corner)))
    if best_total is None or value > best_total:
        best_total = value
        best_profile = corner
best_payoffs = [sp.simplify(p.subs(dict(zip(x, best_profile)))) for p in payoff]

# --- compare ---
EXPECTED_contribution_each = 10
EXPECTED_payoff_each = 20
assert sp.simplify(best_profile[0] - EXPECTED_contribution_each) == 0, (best_profile[0], EXPECTED_contribution_each)
assert sp.simplify(best_profile[1] - EXPECTED_contribution_each) == 0, (best_profile[1], EXPECTED_contribution_each)
assert sp.simplify(best_profile[2] - EXPECTED_contribution_each) == 0, (best_profile[2], EXPECTED_contribution_each)
assert sp.simplify(best_profile[3] - EXPECTED_contribution_each) == 0, (best_profile[3], EXPECTED_contribution_each)
assert sp.simplify(best_payoffs[0] - EXPECTED_payoff_each) == 0, (best_payoffs[0], EXPECTED_payoff_each)
assert sp.simplify(best_payoffs[1] - EXPECTED_payoff_each) == 0, (best_payoffs[1], EXPECTED_payoff_each)
assert sp.simplify(best_payoffs[2] - EXPECTED_payoff_each) == 0, (best_payoffs[2], EXPECTED_payoff_each)
assert sp.simplify(best_payoffs[3] - EXPECTED_payoff_each) == 0, (best_payoffs[3], EXPECTED_payoff_each)
print("PASS")
