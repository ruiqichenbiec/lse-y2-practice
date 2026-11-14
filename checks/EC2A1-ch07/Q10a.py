"""
Line 2: a council's online map archive; one more user costs nothing ($MC = 0$). Demand is $p = 12 - q$ ($q$ in thousand users, $p$ in £).

Continuing: the same demand and $MC = 0$ in each of 10 years (no discounting), but creating the archive now costs 90 once. The firm charges the monopoly price while protected, and 0 afterwards, and creates the archive if its protected profits cover 90.

- (a) Find the shortest term, in whole years, that induces creation.
"""
import sympy as sp

# --- solve: from the problem's data only ---
q = sp.symbols("q", nonnegative=True)
p_of_q = 12 - q                                      # demand p = 12 - q (thousand users, £)
MC = 0                                               # one more user costs nothing
years_horizon = 10                                   # terms are searched within the 10 years
setup_cost = 90                                      # creating the archive, paid once

# monopoly price while protected: choose q where marginal revenue equals MC
profit_year = sp.expand((p_of_q - MC) * q)           # profit in one protected year (revenue minus cost)
q_m = sp.solve(sp.diff(profit_year, q), q)[0]       # MR = 12 - 2q = MC = 0
assert sp.diff(profit_year, q, 2).subs(q, q_m) < 0  # second-order condition: a maximum
assert 0 < q_m < 12                                 # interior solution
pi_year = profit_year.subs(q, q_m)                  # protected profit in each year

# protected profits over T whole years must cover the setup cost
creates = [T for T in range(1, years_horizon + 1) if T * pi_year >= setup_cost]
T_min = creates[0]                                  # shortest whole-year term
assert (T_min - 1) * pi_year < setup_cost           # one year less does not induce creation

# --- compare ---
EXPECTED_shortest_term = 3
assert T_min == EXPECTED_shortest_term, (T_min, EXPECTED_shortest_term)
print("PASS")
