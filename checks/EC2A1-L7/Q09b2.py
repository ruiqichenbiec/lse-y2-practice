"""
Continuing: $p = 12 - q$, $MC = 0$. A private firm digitises the maps at a fixed cost of 27 (£ thousand) and holds the copyright; without it, copies would sell at 0.

- (b) Find consumer surplus and the deadweight loss. Compare total surplus net of the fixed cost under copyright, with free access, and with no archive.
"""
import sympy as sp

# --- solve: from the problem's data only ---
q = sp.symbols("q", positive=True)      # users, in thousands
MC = 0                                  # marginal cost of a copy
FC = 27                                 # fixed cost of digitising, in £ thousand
p_of_q = 12 - q                         # demand curve: the price at which q thousand users buy

revenue = p_of_q * q                    # revenue of the copyright holder
profit_fn = revenue - MC * q - FC       # profit as a function of the number of users
MR = sp.diff(revenue, q)                # marginal revenue

# Copyright: the monopoly outcome (MR = MC, positive root), recomputed here.
q_star = [r for r in sp.solve(sp.Eq(MR, MC), q) if r.is_positive][0]
p_star = p_of_q.subs(q, q_star)
profit = profit_fn.subs(q, q_star)
assert sp.diff(profit_fn, q, 2) < 0     # second-order check: maximum

# Consumer surplus under copyright; total surplus net of the fixed cost = consumer surplus + profit.
CS = sp.integrate(p_of_q - p_star, (q, 0, q_star))
TS_copyright = CS + profit
# Same total from the users' total value: value of the q_star users, minus the variable and fixed costs.
assert sp.simplify(TS_copyright - (sp.integrate(p_of_q, (q, 0, q_star)) - MC * q_star - FC)) == 0

# Free access: price 0, so every user with a positive value uses the archive.
price_free = 0
q_free = [r for r in sp.solve(sp.Eq(p_of_q, price_free), q) if r.is_positive][0]
value_free = sp.integrate(p_of_q, (q, 0, q_free))     # total value of the users
# The fixed cost is still incurred; how it is raised is ignored (any tax is a transfer).
TS_free = value_free - MC * q_free - FC

# No archive: no users and no fixed cost, so total surplus is zero.
users_none = 0
TS_none = sp.integrate(p_of_q, (q, 0, users_none))

# Ordering check: free access > copyright > no archive.
assert TS_free > TS_copyright
assert TS_copyright > TS_none

# --- compare ---
EXPECTED_copyright = 27
EXPECTED_free_access = 45
EXPECTED_no_archive = 0
assert sp.simplify(TS_copyright - EXPECTED_copyright) == 0, (TS_copyright, EXPECTED_copyright)
assert sp.simplify(TS_free - EXPECTED_free_access) == 0, (TS_free, EXPECTED_free_access)
assert sp.simplify(TS_none - EXPECTED_no_archive) == 0, (TS_none, EXPECTED_no_archive)
print("PASS")
