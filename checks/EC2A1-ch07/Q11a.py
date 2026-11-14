"""
Line 3: four students get £10 each and may put any part $x_i$ into an envelope; the experimenter doubles the total and shares it equally ($N = 4$, $m = 2$, $w = 10$).

- (a) Find the payoff of a student who gives £0 when the others give £10 each, and of one who gives £10 when the others give nothing.
"""
import sympy as sp

# --- solve: from the problem's data only ---
w = sp.Integer(10)  # endowment of each student (pounds)
m = sp.Integer(2)   # multiplier applied to the envelope
N = sp.Integer(4)   # number of students

# Payoff u_i = w - x_i + (m / N) * (sum of all contributions, her own included).
def payoff(own, others_total):
    total = own + others_total
    return w - own + m / N * total

# (a) She gives 0 and each of the other N - 1 students gives w.
gives_0_others_give_w = payoff(sp.Integer(0), (N - 1) * w)

# She gives w and the others give 0.
gives_w_others_give_0 = payoff(w, sp.Integer(0))

# --- compare ---
EXPECTED_payoff_gives_0 = 25
EXPECTED_payoff_gives_10 = 5
assert sp.simplify(gives_0_others_give_w - EXPECTED_payoff_gives_0) == 0, (gives_0_others_give_w, EXPECTED_payoff_gives_0)
assert sp.simplify(gives_w_others_give_0 - EXPECTED_payoff_gives_10) == 0, (gives_w_others_give_0, EXPECTED_payoff_gives_10)
print("PASS")
