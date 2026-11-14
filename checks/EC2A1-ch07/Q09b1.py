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

# Copyright: the monopoly outcome, recomputed from the demand curve (MR = MC, positive root).
q_star = [r for r in sp.solve(sp.Eq(MR, MC), q) if r.is_positive][0]
p_star = p_of_q.subs(q, q_star)

# Second-order check: the outcome is a maximum.
assert sp.diff(profit_fn, q, 2) < 0
# Corner check: the price is above MC, so the copyright outcome falls short of the efficient one.
assert p_star > MC

# Consumer surplus: area between the demand curve and the monopoly price, over the q_star users who buy.
CS = sp.integrate(p_of_q - p_star, (q, 0, q_star))

# Deadweight loss: triangle between demand and MC over the excluded users, from q_star up to the efficient quantity (price = MC).
q_eff = [r for r in sp.solve(sp.Eq(p_of_q, MC), q) if r.is_positive][0]
DWL = sp.integrate(p_of_q - MC, (q, q_star, q_eff))

# Cross-check: DWL = (efficient total surplus) - (copyright total surplus, both before the fixed cost).
TS_eff = sp.integrate(p_of_q - MC, (q, 0, q_eff))
TS_copyright_gross = sp.integrate(p_of_q - MC, (q, 0, q_star))
assert sp.simplify(DWL - (TS_eff - TS_copyright_gross)) == 0

# --- compare ---
EXPECTED_consumer_surplus = 18
EXPECTED_deadweight_loss = 18
assert sp.simplify(CS - EXPECTED_consumer_surplus) == 0, (CS, EXPECTED_consumer_surplus)
assert sp.simplify(DWL - EXPECTED_deadweight_loss) == 0, (DWL, EXPECTED_deadweight_loss)
print("PASS")
