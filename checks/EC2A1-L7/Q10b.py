"""
Line 2: a council's online map archive; one more user costs nothing ($MC = 0$). Demand is $p = 12 - q$ ($q$ in thousand users, $p$ in £).

Continuing: the same demand and $MC = 0$ in each of 10 years (no discounting), but creating the archive now costs 90 once. The firm charges the monopoly price while protected, and 0 afterwards, and creates the archive if its protected profits cover 90.

- (a) Find the shortest term, in whole years, that induces creation.
- (b) Find total surplus over 10 years, net of the 90, for that term and for a 10-year term.
"""
import sympy as sp

# --- solve: from the problem's data only ---
q = sp.symbols("q", nonnegative=True)
p_of_q = 12 - q                                      # demand p = 12 - q (thousand users, £)
MC = 0                                               # one more user costs nothing
years_horizon = 10                                   # the horizon: 10 years, no discounting
setup_cost = 90                                      # creating the archive, paid once

# monopoly price while protected: choose q where marginal revenue equals MC
profit_year = sp.expand((p_of_q - MC) * q)           # profit in one protected year (revenue minus cost)
q_m = sp.solve(sp.diff(profit_year, q), q)[0]       # MR = 12 - 2q = MC = 0
assert sp.diff(profit_year, q, 2).subs(q, q_m) < 0  # second-order condition: a maximum
assert 0 < q_m < 12                                 # interior solution: some users are priced out
pi_year = profit_year.subs(q, q_m)                  # protected profit in each year

# total surplus in one protected year: value of the users served minus their cost (= CS + profit)
S_protected = sp.integrate(p_of_q, (q, 0, q_m)) - MC * q_m
# free access: the price is 0, so everybody with a positive value uses the archive
q_free = sp.solve(sp.Eq(p_of_q, 0), q)[0]
S_free = sp.integrate(p_of_q, (q, 0, q_free)) - MC * q_free


def net_total(term):
    # the archive is created only if protected profits over the term cover the setup cost
    if term * pi_year < setup_cost:
        return 0
    return term * S_protected + (years_horizon - term) * S_free - setup_cost


# part (a): shortest whole-year term that induces creation
creates = [T for T in range(1, years_horizon + 1) if T * pi_year >= setup_cost]
T_min = creates[0]
assert (T_min - 1) * pi_year < setup_cost           # one year less does not induce creation

# part (b): total surplus over 10 years, net of the setup cost, for that term and for 10 years
S_min_term = net_total(T_min)
S_full_term = net_total(years_horizon)

# --- compare ---
EXPECTED_total_shortest_term = 576
EXPECTED_total_10_year_term = 450
assert S_min_term == EXPECTED_total_shortest_term, (S_min_term, EXPECTED_total_shortest_term)
assert S_full_term == EXPECTED_total_10_year_term, (S_full_term, EXPECTED_total_10_year_term)
print("PASS")
