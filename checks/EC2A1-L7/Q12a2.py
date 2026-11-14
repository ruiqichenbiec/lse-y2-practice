"""
Problem EC2A1-L7-112 (statement): **Condition for free riding.** A pound contributed returns only $m/N$ to the contributor but $m$ to the group. Contributing nothing is dominant if $m/N < 1$; contributing everything is efficient if $m > 1$.

Problem EC2A1-L7-112, part (a) (prompt): Continuing: $w = 10$ and $u_i = 10 - x_i + \\tfrac{m}{N}\\sum_j x_j$.

- (a) Keep $m = 2$. For which $N$ is contributing nothing dominant? What happens for $N = 2$?
"""
import sympy as sp

# --- solve: from the problem's data only ---
N, m, x, S = sp.symbols("N m x S", positive=True)   # group size N, multiplier m, own gift x, total S of the others' gifts
w = 10                                              # endowment

# Payoff of one student: u_i = w - x_i + (m/N) * sum_j x_j; the sum includes her own gift, so sum_j x_j = x + S.
u = w - x + (m / N) * (x + S)

# Part (a) with N = 2 and m = 2: the return per pound is m/N = 1.
u_N2 = u.subs({N: 2, m: 2})                                     # 10 + S: her own gift x has cancelled out
effect_N2 = sp.simplify(sp.diff(u_N2, x))                       # effect of one more pound on her own payoff
return_N2 = (m / N).subs({N: 2, m: 2})                          # a pound returns exactly 1
gain_vs_nothing_N2 = sp.simplify(u_N2 - u_N2.subs(x, 0))        # payoff of giving x instead of nothing, for any S

# --- compare ---
EXPECTED_effect_N2 = 0      # with N = 2 the effect of one more pound is 0
EXPECTED_return_N2 = 1      # a pound returns exactly 1
EXPECTED_gain_N2 = 0        # so giving nothing or giving any amount leaves her payoff unchanged
assert sp.simplify(effect_N2 - EXPECTED_effect_N2) == 0, (effect_N2, EXPECTED_effect_N2)
assert sp.simplify(return_N2 - EXPECTED_return_N2) == 0, (return_N2, EXPECTED_return_N2)
assert sp.simplify(gain_vs_nothing_N2 - EXPECTED_gain_N2) == 0, (gain_vs_nothing_N2, EXPECTED_gain_N2)
print("PASS")
