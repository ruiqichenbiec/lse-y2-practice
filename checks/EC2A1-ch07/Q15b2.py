"""
A pharmaceutical firm holds a patent on a new vaccine. Each year the demand is $p = 10 - q$ and the marginal cost of a dose is $MC = 2$ ($q$: million doses; $p$: £ per dose; money in £ million a year). While the patent lasts, the firm is the only seller and charges one price. (Total 10 marks.)

- (b) Find consumer surplus and the deadweight loss each year during the patent. By how much does annual total surplus rise when the patent expires and the price falls to marginal cost? (3 marks)
"""
import sympy as sp

# --- solve: from the problem's data only ---
q = sp.symbols("q", nonnegative=True)
p_of_q = 10 - q                                           # demand: p = 10 - q (q in million doses)
MC = 2                                                    # marginal cost of a dose (£ per dose)
q_m = sp.solve(sp.Eq(sp.diff(p_of_q * q, q), MC), q)[0]   # patent monopoly output: MR = MC
q_c = sp.solve(sp.Eq(p_of_q, MC), q)[0]                   # output at which price equals marginal cost
# second-order check: the profit (p - MC) q is concave, so q_m is a maximum
assert sp.diff((p_of_q - MC) * q, q, 2) < 0
# total surplus during the patent: area between demand and marginal cost up to q_m
# (this equals consumer surplus plus the monopoly profit)
TS_patent = sp.integrate(p_of_q - MC, (q, 0, q_m))
# total surplus after expiry: price equals marginal cost, so output is q_c and profit is zero
TS_expired = sp.integrate(p_of_q - MC, (q, 0, q_c))
rise = TS_expired - TS_patent

# --- compare ---
EXPECTED_total_before = 24
EXPECTED_total_after = 32
EXPECTED_rise = 8
assert sp.simplify(TS_patent - EXPECTED_total_before) == 0, (TS_patent, EXPECTED_total_before)
assert sp.simplify(TS_expired - EXPECTED_total_after) == 0, (TS_expired, EXPECTED_total_after)
assert sp.simplify(rise - EXPECTED_rise) == 0, (rise, EXPECTED_rise)
print("PASS")
