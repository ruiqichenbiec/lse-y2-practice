"""
Continuing: $p = 12 - q$, $MC = 0$. A private firm digitises the maps at a fixed cost of 27 (£ thousand) and holds the copyright; without it, copies would sell at 0.

- (a) Use the monopoly rule [appendix] to find the firm's price, users and profit. Does it create the archive?
"""
import sympy as sp

# --- solve: from the problem's data only ---
q = sp.symbols("q", positive=True)      # users, in thousands
MC = 0                                  # marginal cost of a copy
FC = 27                                 # fixed cost of digitising, in £ thousand
p_of_q = 12 - q                         # demand curve: the price at which q thousand users buy

revenue = p_of_q * q                    # revenue of the copyright holder
profit_fn = revenue - MC * q - FC       # profit net of the fixed cost
MR = sp.diff(revenue, q)                # marginal revenue

# Monopoly rule under copyright: MR = MC, positive root.
q_star = [r for r in sp.solve(sp.Eq(MR, MC), q) if r.is_positive][0]
profit = profit_fn.subs(q, q_star)      # profit of the copyright holder at the monopoly outcome

# Second-order check: the critical point is a maximum.
assert sp.diff(profit_fn, q, 2) < 0
# Corner check: the interior outcome beats the corner q = 0, where profit is -FC.
assert profit > profit_fn.subs(q, 0)

# The firm creates the archive only if its profit under copyright is positive.

# --- compare ---
EXPECTED_profit = 9
EXPECTED_zero = 0
assert sp.simplify(profit - EXPECTED_profit) == 0, (profit, EXPECTED_profit)
assert profit > EXPECTED_zero, (profit, EXPECTED_zero)
print("PASS")
