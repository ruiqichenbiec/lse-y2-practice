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

# Option 2 with one price p: demand is q = 12 - p, so the revenue from the users is p (12 - p).
revenue = p * (12 - p)
# The lowest price that raises the fixed cost is the lower root of revenue = 27.
lowest_price = min(sp.solve(sp.Eq(revenue, fixed_cost), p))
# Corner check: the prices raising at least 27 form an interval, and its lower end is that root.
raising_prices = sp.solve_univariate_inequality(sp.Ge(revenue, fixed_cost), p, relational=False)
assert sp.simplify(raising_prices.inf - lowest_price) == 0
users_2 = 12 - lowest_price   # paying users at that price (thousands)
# Total value of the paying users = area under the demand curve from 0 to users_2.
value_2 = sp.integrate(12 - t, (t, 0, users_2))
net_2_no_admin = value_2 - fixed_cost                          # ignoring administration
admin_cost_2 = admin_cost_per_user * users_2                   # total administrative cost
net_2_admin = net_2_no_admin - admin_cost_2                    # including administration

# --- compare ---
EXPECTED_price_2 = 3
EXPECTED_users_2 = 9
EXPECTED_net_2_no_admin = sp.Rational(81, 2)   # 40.5
EXPECTED_admin_cost_2 = 9
EXPECTED_net_2_admin = sp.Rational(63, 2)      # 31.5
assert sp.simplify(lowest_price - EXPECTED_price_2) == 0, (lowest_price, EXPECTED_price_2)
assert sp.simplify(users_2 - EXPECTED_users_2) == 0, (users_2, EXPECTED_users_2)
assert sp.simplify(net_2_no_admin - EXPECTED_net_2_no_admin) == 0, (net_2_no_admin, EXPECTED_net_2_no_admin)
assert sp.simplify(admin_cost_2 - EXPECTED_admin_cost_2) == 0, (admin_cost_2, EXPECTED_admin_cost_2)
assert sp.simplify(net_2_admin - EXPECTED_net_2_admin) == 0, (net_2_admin, EXPECTED_net_2_admin)
print("PASS")
