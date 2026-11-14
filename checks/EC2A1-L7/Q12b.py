"""
Problem EC2A1-L7-112 (statement): **Condition for free riding.** A pound contributed returns only $m/N$ to the contributor but $m$ to the group. Contributing nothing is dominant if $m/N < 1$; contributing everything is efficient if $m > 1$.

Problem EC2A1-L7-112, part (b) (prompt): Continuing: $w = 10$ and $u_i = 10 - x_i + \\tfrac{m}{N}\\sum_j x_j$.

- (b) Keep $N = 4$. Find the smallest whole-number $m$ for which contributing everything is dominant.
"""
import sympy as sp

# --- solve: from the problem's data only ---
m, x, S = sp.symbols("m x S", positive=True)        # multiplier m, own gift x, total S of the others' gifts
N = 4                                               # group size (part (b): keep N = 4)
w = 10                                              # endowment

# Payoff of one student: u_i = w - x_i + (m/N) * sum_j x_j; the sum includes her own gift, so sum_j x_j = x + S.
u = w - x + (m / N) * (x + S)

# One more pound changes her own payoff by m/N - 1, whatever the others give (S does not enter).
effect = sp.diff(u, x)                                          # m/4 - 1

# Contributing everything (x = w) against a gift x: the payoff difference is (w - x) * (m/N - 1).
gain_full_vs_x = sp.simplify(u.subs(x, w) - u)

# Smallest whole number m with a positive effect: search the whole numbers 0, 1, 2, ...
m_min = next(k for k in range(0, 100) if effect.subs(m, k) > 0)   # 5
# The effect is zero at m = 4 and positive above it.
m_threshold = sp.solve(sp.Eq(effect, 0), m)[0]                    # 4

# Checks at m = 5: a pound returns 5/4 > 1, and giving everything beats giving nothing (corner x = 0).
return_min = sp.Rational(m_min, N)                                # 5/4
gain_corner = sp.simplify(gain_full_vs_x.subs({x: 0, m: m_min}))  # 10 * (5/4 - 1) = 5/2
effect_at_4 = effect.subs(m, N)                                   # 0 at m = 4, so m = 4 does not make it dominant

# --- compare ---
EXPECTED_m_min = 5                       # the smallest whole-number m for which contributing everything is dominant
EXPECTED_m_threshold = 4                 # the effect m/4 - 1 is positive if m > 4
EXPECTED_zero = 0                        # at m = 4 the effect is exactly 0
EXPECTED_one = 1
EXPECTED_return_min = sp.Rational(5, 4)  # a pound returns 5/4 at m = 5
assert m_min == EXPECTED_m_min, (m_min, EXPECTED_m_min)
assert sp.simplify(m_threshold - EXPECTED_m_threshold) == 0, (m_threshold, EXPECTED_m_threshold)
assert effect_at_4 == EXPECTED_zero, (effect_at_4, EXPECTED_zero)
assert sp.simplify(return_min - EXPECTED_return_min) == 0, (return_min, EXPECTED_return_min)
assert return_min > EXPECTED_one, (return_min, EXPECTED_one)
assert gain_corner > EXPECTED_zero, (gain_corner, EXPECTED_zero)
print("PASS")
