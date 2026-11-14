"""
Line 2: a council's online map archive; one more user costs nothing ($MC = 0$). Demand is $p = 12 - q$ ($q$ in thousand users, $p$ in £).

Continuing: the same demand and $MC = 0$ in each of 10 years (no discounting), but creating the archive now costs 90 once. The firm charges the monopoly price while protected, and 0 afterwards, and creates the archive if its protected profits cover 90.

- (c) If the government pays the 90 and access is free, find total surplus (ignore the cost of raising the money).
"""
import sympy as sp

# --- solve: from the problem's data only ---
q = sp.symbols("q", nonnegative=True)
p_of_q = 12 - q                                      # demand p = 12 - q (thousand users, £)
MC = 0                                               # one more user costs nothing
years_horizon = 10                                   # the horizon: 10 years, no discounting
setup_cost = 90                                      # creating the archive, paid by the government

# free access: the price is 0, so everybody with a positive value uses the archive
q_free = sp.solve(sp.Eq(p_of_q, 0), q)[0]
assert 0 < q_free                                    # there are users at price 0
# total surplus in one year: value of the users served minus their cost
S_free_year = sp.integrate(p_of_q, (q, 0, q_free)) - MC * q_free
# total surplus over the horizon, net of the setup cost
total_net = years_horizon * S_free_year - setup_cost

# --- compare ---
EXPECTED_total_free_access = 630
assert total_net == EXPECTED_total_free_access, (total_net, EXPECTED_total_free_access)
print("PASS")
