"""
Continuing: $p = 12 - q$, $MC = 0$; a fixed cost of 27 must be covered.

- Option 1: free access; taxes raise 27, at an extra cost of 9 to society.

- (a) Find Option 1's net benefit: users' total value minus the fixed cost and the extra tax cost.
"""
import sympy as sp

# --- solve: from the problem's data only ---
t = sp.symbols("t", positive=True)   # t = number of users (thousands), also the integration variable
# Free access: the price is 0, so the users are those demanding q with 12 - q = 0 (the demand at p = 0).
q_free = sp.solve(sp.Eq(12 - t, 0), t)[0]
# Total value of the users = area under the demand curve p = 12 - t from 0 to q_free.
total_value = sp.integrate(12 - t, (t, 0, q_free))
fixed_cost = 27
extra_tax_cost = 9   # extra cost to society of raising the 27 by taxes
# Net benefit: users' total value minus the fixed cost minus the extra tax cost.
net_benefit_1 = total_value - fixed_cost - extra_tax_cost

# --- compare ---
EXPECTED_total_value = 72
EXPECTED_net_benefit_1 = 36   # printed solution: 72 - 27 - 9 = 36
assert sp.simplify(total_value - EXPECTED_total_value) == 0, (total_value, EXPECTED_total_value)
assert sp.simplify(net_benefit_1 - EXPECTED_net_benefit_1) == 0, (net_benefit_1, EXPECTED_net_benefit_1)
print("PASS")
