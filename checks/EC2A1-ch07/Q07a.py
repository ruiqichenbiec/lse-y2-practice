"""
Line 2: a council's online map archive; one more user costs nothing ($MC = 0$). Demand is $p = 12 - q$ ($q$ in thousand users, $p$ in £). At price $p_0$ in the figure, A is revenue, B consumer surplus, C the value lost by excluded users.

![Demand](fig:EC2A1 Chapter 7/demand)

- (a) With free access, find the users and their total value.
"""
import sympy as sp

# --- solve: from the problem's data only ---
q = sp.symbols("q", nonnegative=True)     # users, in thousands
p = 12 - q                                # demand: valuation (in £) of the marginal user when q thousand are served

# Free access means price 0: every user whose valuation is at least 0 uses the archive,
# so the number of users is the q at which demand falls to 0.
q_free = sp.solve(sp.Eq(p, 0), q)[0]

# Their total value is the area under the demand curve from 0 to q_free.
total_value_free = sp.integrate(p, (q, 0, q_free))

# corner check: demand is positive below q_free and zero at it, so q_free is the boundary of the user group
assert p.subs(q, 0) > 0
assert p.subs(q, q_free) == 0

# --- compare ---
EXPECTED_users_free = 12
EXPECTED_total_value_free = 72
assert sp.simplify(q_free - EXPECTED_users_free) == 0, (q_free, EXPECTED_users_free)
assert sp.simplify(total_value_free - EXPECTED_total_value_free) == 0, (total_value_free, EXPECTED_total_value_free)
print("PASS")
