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
p_m = p_of_q.subs(q, q_m)                                 # patent monopoly price
q_c = sp.solve(sp.Eq(p_of_q, MC), q)[0]                   # output at which price equals marginal cost
# second-order check: the profit (p - MC) q is concave, so q_m is a maximum
assert sp.diff((p_of_q - MC) * q, q, 2) < 0
# consumer surplus during the patent: area under demand above the monopoly price, up to q_m
CS_patent = sp.integrate(p_of_q - p_m, (q, 0, q_m))
# deadweight loss during the patent: doses between q_m and q_c, valued at demand minus marginal cost
DWL_patent = sp.integrate(p_of_q - MC, (q, q_m, q_c))

# --- compare ---
EXPECTED_consumer_surplus = 8
EXPECTED_deadweight_loss = 8
assert sp.simplify(CS_patent - EXPECTED_consumer_surplus) == 0, (CS_patent, EXPECTED_consumer_surplus)
assert sp.simplify(DWL_patent - EXPECTED_deadweight_loss) == 0, (DWL_patent, EXPECTED_deadweight_loss)
print("PASS")
