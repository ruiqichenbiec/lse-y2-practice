"""
A pharmaceutical firm holds a patent on a new vaccine. Each year the demand is $p = 10 - q$ and the marginal cost of a dose is $MC = 2$ ($q$: million doses; $p$: £ per dose; money in £ million a year). While the patent lasts, the firm is the only seller and charges one price. (Total 10 marks.)

- (c) Developing the vaccine costs 30, paid before any sales. Find the shortest patent term, in whole years, for which the firm develops it (no discounting). (2 marks)
"""
import sympy as sp

# --- solve: from the problem's data only ---
q = sp.symbols("q", nonnegative=True)
p_of_q = 10 - q                                           # demand: p = 10 - q (q in million doses)
MC = 2                                                    # marginal cost of a dose (£ per dose)
dev_cost = 30                                             # development cost, paid before any sales (£ million)
q_m = sp.solve(sp.Eq(sp.diff(p_of_q * q, q), MC), q)[0]   # patent monopoly output: MR = MC
p_m = p_of_q.subs(q, q_m)                                 # patent monopoly price
annual_profit = (p_m - MC) * q_m                          # profit in each year of the patent (no discounting)
# second-order check: the profit (p - MC) q is concave, so q_m is a maximum
assert sp.diff((p_of_q - MC) * q, q, 2) < 0
# shortest whole-year term T whose total profit covers the development cost
T = 1
while annual_profit * T < dev_cost:
    T += 1
profit_one_year = annual_profit * 1
profit_two_years = annual_profit * 2

# --- compare ---
EXPECTED_profit_one_year = 16
EXPECTED_profit_two_years = 32
EXPECTED_development_cost = 30
EXPECTED_term = 2
assert sp.simplify(profit_one_year - EXPECTED_profit_one_year) == 0, (profit_one_year, EXPECTED_profit_one_year)
assert profit_one_year < EXPECTED_development_cost, (profit_one_year, EXPECTED_development_cost)
assert sp.simplify(profit_two_years - EXPECTED_profit_two_years) == 0, (profit_two_years, EXPECTED_profit_two_years)
assert profit_two_years >= EXPECTED_development_cost, (profit_two_years, EXPECTED_development_cost)
assert T == EXPECTED_term, (T, EXPECTED_term)
print("PASS")
