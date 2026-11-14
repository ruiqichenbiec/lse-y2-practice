"""
A pharmaceutical firm holds a patent on a new vaccine. Each year the demand is $p = 10 - q$ and the marginal cost of a dose is $MC = 2$ ($q$: million doses; $p$: £ per dose; money in £ million a year). While the patent lasts, the firm is the only seller and charges one price. (Total 10 marks.)

- (a) Find the firm's price, output and annual profit (before development costs). (3 marks)
"""
import sympy as sp

# --- solve: from the problem's data only ---
q = sp.symbols("q", nonnegative=True)
p_of_q = 10 - q                                   # demand: p = 10 - q (q in million doses)
MC = 2                                            # marginal cost of a dose (£ per dose)
MR = sp.diff(p_of_q * q, q)                       # marginal revenue of the single-price seller
q_m = sp.solve(sp.Eq(MR, MC), q)[0]               # monopoly output: MR = MC
p_m = p_of_q.subs(q, q_m)                         # monopoly price, read off the demand curve
profit_m = (p_m - MC) * q_m                       # annual profit before development costs
# second-order check: the profit (p - MC) q has a negative second derivative, so q_m is a maximum
assert sp.diff((p_of_q - MC) * q, q, 2) < 0

# --- compare ---
EXPECTED_price = 6
EXPECTED_output = 4
EXPECTED_profit = 16
assert sp.simplify(p_m - EXPECTED_price) == 0, (p_m, EXPECTED_price)
assert sp.simplify(q_m - EXPECTED_output) == 0, (q_m, EXPECTED_output)
assert sp.simplify(profit_m - EXPECTED_profit) == 0, (profit_m, EXPECTED_profit)
print("PASS")
