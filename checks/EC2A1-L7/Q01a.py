"""
Line 1: a river valley. A flood barrier of height $x$ metres costs 1 per metre and other consumption $c$ has price 1, so a farm paying for its own barrier from an endowment of 100 has $c = 100 - x$. Farm A's utility is $U_A = c + 6\\ln x$, farm B's is $U_B = c + 2\\ln x$. Each farm lives on its own river.

- (a) Find the height each farm builds.
"""
import sympy as sp

# --- solve: from the problem's data only ---
x = sp.symbols("x", positive=True)              # barrier height in metres
endowment = 100
cost_per_metre = 1
c = endowment - cost_per_metre * x              # other consumption left after paying for the barrier
a_A, a_B = 6, 2                                 # weights on ln x in the two utilities
U_A = c + a_A * sp.log(x)
U_B = c + a_B * sp.log(x)

# first-order condition dU/dx = 0; keep the positive root as the height
x_A = [s for s in sp.solve(sp.diff(U_A, x), x) if s.is_positive][0]
x_B = [s for s in sp.solve(sp.diff(U_B, x), x) if s.is_positive][0]

# second-order check: d2U/dx2 < 0 at the critical point, so it is a maximum
assert sp.diff(U_A, x, 2).subs(x, x_A) < 0
assert sp.diff(U_B, x, 2).subs(x, x_B) < 0
# corner check: U tends to minus infinity as x tends to 0 (ln x does), so the boundary x = 0 is never best
assert sp.limit(U_A, x, 0, "+") == -sp.oo
assert sp.limit(U_B, x, 0, "+") == -sp.oo
# the critical heights lie inside the feasible range, since the barrier cannot cost more than the endowment
assert 0 < x_A < endowment
assert 0 < x_B < endowment

# --- compare ---
EXPECTED_height_A = 6
EXPECTED_height_B = 2
assert sp.simplify(x_A - EXPECTED_height_A) == 0, (x_A, EXPECTED_height_A)
assert sp.simplify(x_B - EXPECTED_height_B) == 0, (x_B, EXPECTED_height_B)
print("PASS")
