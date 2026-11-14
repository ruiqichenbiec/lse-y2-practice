"""
Problem Q7.12 (statement): **Condition for free riding.** A pound contributed returns only $m/N$ to the contributor but $m$ to the group. Contributing nothing is dominant if $m/N < 1$; contributing everything is efficient if $m > 1$.

Problem Q7.12, part (a) (prompt): Continuing: $w = 10$ and $u_i = 10 - x_i + \\tfrac{m}{N}\\sum_j x_j$.

- (a) Keep $m = 2$. For which $N$ is contributing nothing dominant? What happens for $N = 2$?
"""
import sympy as sp

# --- solve: from the problem's data only ---
N, m, x, S = sp.symbols("N m x S", positive=True)   # group size N, multiplier m, own gift x, total S of the others' gifts
w = 10                                              # endowment

# Payoff of one student: u_i = w - x_i + (m/N) * sum_j x_j; the sum includes her own gift, so sum_j x_j = x + S.
u = w - x + (m / N) * (x + S)

# Part (a) with m = 2: one more pound changes her own payoff by the derivative in x, which does not involve S.
effect = sp.simplify(sp.diff(u, x).subs(m, 2))                  # 2/N - 1
# Payoff of giving x instead of nothing, for any S: x * (2/N - 1).
gain_vs_nothing = sp.simplify((u - u.subs(x, 0)).subs(m, 2))

# The effect is zero at N = 2, and its derivative in N is -2/N**2 < 0, so it is negative for every N above 2.
N_boundary = sp.solve(sp.Eq(effect, 0), N)[0]                   # 2
slope_in_N = sp.simplify(sp.diff(effect, N))                    # -2/N**2

# Group of three: a pound returns m/N = 2/3, and the effect is -1/3.
return_N3 = (m / N).subs({m: 2, N: 3})                          # 2/3
effect_N3 = effect.subs(N, 3)                                   # -1/3

# Corner check: the largest possible gift is w = 10. Giving nothing still beats giving everything when N = 3.
corner_gain_N3 = sp.simplify(gain_vs_nothing.subs({x: w, N: 3}))   # 10 * (2/3 - 1) = -10/3

# --- compare ---
EXPECTED_zero = 0
EXPECTED_one = 1
EXPECTED_boundary_N = 2                  # the effect 2/N - 1 is zero at N = 2 and negative above it
EXPECTED_return_N3 = sp.Rational(2, 3)   # with N = 3 a pound returns 2/3
assert sp.simplify(N_boundary - EXPECTED_boundary_N) == 0, (N_boundary, EXPECTED_boundary_N)
assert slope_in_N < EXPECTED_zero, (slope_in_N, EXPECTED_zero)
assert effect_N3 < EXPECTED_zero, (effect_N3, EXPECTED_zero)
assert corner_gain_N3 < EXPECTED_zero, (corner_gain_N3, EXPECTED_zero)
assert return_N3 == EXPECTED_return_N3, (return_N3, EXPECTED_return_N3)
assert return_N3 < EXPECTED_one, (return_N3, EXPECTED_one)
print("PASS")
