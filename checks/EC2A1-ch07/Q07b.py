"""
Line 2: a council's online map archive; one more user costs nothing ($MC = 0$). Demand is $p = 12 - q$ ($q$ in thousand users, $p$ in £). At price $p_0$ in the figure, A is revenue, B consumer surplus, C the value lost by excluded users.

![Demand](fig:EC2A1 Chapter 7/demand)

- (b) At $p_0 = 4$, find users, excluded users, revenue (A) and deadweight loss (C).
"""
import sympy as sp

# --- solve: from the problem's data only ---
q = sp.symbols("q", nonnegative=True)     # users, in thousands
p = 12 - q                                # demand: valuation (in £) of the marginal user when q thousand are served
MC = 0                                    # one more user costs nothing
p0 = 4                                    # the price in part (b), in £

# Users at price p0 are those whose valuation is at least p0, so q0 solves p(q0) = p0.
q0 = sp.solve(sp.Eq(p, p0), q)[0]
# Users with a positive valuation under free access: the q at which demand falls to MC = 0.
q_max = sp.solve(sp.Eq(p, MC), q)[0]
excluded = q_max - q0                     # valued above MC but not served at p0

# Revenue A: price times the users who pay it.
revenue_A = p0 * q0
# Consumer surplus B: area between demand and p0 over the users served (reference only).
consumer_surplus_B = sp.integrate(p - p0, (q, 0, q0))
# Deadweight loss C: value lost by the excluded users, the area between demand and MC over them.
dwl_C = sp.integrate(p - MC, (q, q0, q_max))

# range check: the price cuts the demand strictly inside (0, q_max)
assert 0 < q0 < q_max
# total surplus check: revenue + consumer surplus = free-access total value minus the deadweight loss
assert sp.simplify(revenue_A + consumer_surplus_B - (sp.integrate(p - MC, (q, 0, q_max)) - dwl_C)) == 0

# --- compare ---
EXPECTED_users = 8
EXPECTED_excluded = 4
EXPECTED_revenue_A = 32
EXPECTED_dwl_C = 8
assert sp.simplify(q0 - EXPECTED_users) == 0, (q0, EXPECTED_users)
assert sp.simplify(excluded - EXPECTED_excluded) == 0, (excluded, EXPECTED_excluded)
assert sp.simplify(revenue_A - EXPECTED_revenue_A) == 0, (revenue_A, EXPECTED_revenue_A)
assert sp.simplify(dwl_C - EXPECTED_dwl_C) == 0, (dwl_C, EXPECTED_dwl_C)
print("PASS")
