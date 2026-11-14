"""
Continuing: $p = 12 - q$, $MC = 0$; a fixed cost of 27 must be covered.

- Option 1: free access; taxes raise 27, at an extra cost of 9 to society.
- Option 2: one price, the lowest that raises 27; each paying user costs 1 to administer.

- (a) Find Option 1's net benefit: users' total value minus the fixed cost and the extra tax cost.
- (b) Find Option 2's price and net benefit, ignoring and then including the administrative cost. Which option is better?
"""
import sympy as sp

# --- solve: from the problem's data only ---
t, p = sp.symbols("t p", positive=True)   # t = number of users (thousands); p = price
fixed_cost = 27
admin_cost_per_user = 1

# Part (a), recomputed here: free access (price 0), so the users are those demanding q with 12 - q = 0.
q_free = sp.solve(sp.Eq(12 - t, 0), t)[0]
value_free = sp.integrate(12 - t, (t, 0, q_free))   # users' total value = area under the demand curve
extra_tax_cost = 9
net_1 = value_free - fixed_cost - extra_tax_cost     # Option 1's net benefit

# Part (b), recomputed here: the lowest single price that raises the fixed cost, and its net benefits.
revenue = p * (12 - p)
lowest_price = min(sp.solve(sp.Eq(revenue, fixed_cost), p))
# Corner check: the prices raising at least 27 form an interval, and its lower end is that root.
raising_prices = sp.solve_univariate_inequality(sp.Ge(revenue, fixed_cost), p, relational=False)
assert sp.simplify(raising_prices.inf - lowest_price) == 0
users_2 = 12 - lowest_price
value_2 = sp.integrate(12 - t, (t, 0, users_2))
net_2_no_admin = value_2 - fixed_cost
net_2_admin = net_2_no_admin - admin_cost_per_user * users_2   # Option 2's net benefit including administration

# --- compare ---
EXPECTED_net_1 = 36
EXPECTED_net_2_admin = sp.Rational(63, 2)   # 31.5
assert sp.simplify(net_1 - EXPECTED_net_1) == 0, (net_1, EXPECTED_net_1)
assert sp.simplify(net_2_admin - EXPECTED_net_2_admin) == 0, (net_2_admin, EXPECTED_net_2_admin)
# Option 1 (36) is larger than Option 2 including administration (31.5).
assert net_1 > EXPECTED_net_2_admin, (net_1, EXPECTED_net_2_admin)
print("PASS")
