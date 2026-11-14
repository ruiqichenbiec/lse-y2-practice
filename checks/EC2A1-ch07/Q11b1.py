"""
Line 3: four students get £10 each and may put any part $x_i$ into an envelope; the experimenter doubles the total and shares it equally ($N = 4$, $m = 2$, $w = 10$).

- (b) Find the effect of one more pound given on a student's own payoff, and hence the Nash equilibrium. Find the profile maximising total payoff, and the payoffs there.
"""
import sympy as sp

# --- solve: from the problem's data only ---
w = sp.Integer(10)  # endowment of each student (pounds)
m = sp.Integer(2)   # multiplier applied to the envelope
N = sp.Integer(4)   # number of students

x1 = sp.symbols("x1", nonnegative=True)            # student 1's contribution
others = sp.symbols("x2 x3 x4", nonnegative=True)  # the other three contributions, left general
total = x1 + sum(others)                           # everything in the envelope
payoff = w - x1 + m / N * total                    # u_1 = w - x_1 + (m / N) * sum_j x_j

# Effect of one more pound given by student 1, with the others' gifts held fixed.
effect_one_pound = sp.simplify(payoff.subs(x1, x1 + 1) - payoff)
effect_derivative = sp.simplify(sp.diff(payoff, x1))

# --- compare ---
EXPECTED_effect = sp.Rational(-1, 2)
assert sp.simplify(effect_one_pound - EXPECTED_effect) == 0, (effect_one_pound, EXPECTED_effect)
assert sp.simplify(effect_derivative - EXPECTED_effect) == 0, (effect_derivative, EXPECTED_effect)
print("PASS")
