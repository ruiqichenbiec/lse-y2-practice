r"""
- (a) In $(\mathbb{R}^2,\|\cdot\|_2)$ let $a_n=\big(\frac3n,\,-\frac4n\big)$. Compute $\|a_n-\mathbf{0}\|_2$ and find the smallest $N\in\mathbb{N}$ such that $\|a_n-\mathbf{0}\|_2<0.01$ for all $n>N$.
- (b) In $(C[0,1],\|\cdot\|_\infty)$ let $f_n(x)=\frac{x^2+1}{n}$ and let $\mathbf{0}$ be the zero function. Compute $\|f_n-\mathbf{0}\|_\infty$ and find the smallest $N$ that works for $\epsilon=0.001$.
"""
import sympy as sp

# --- solve: from the problem's data only ---
n = sp.symbols("n", positive=True, integer=True)   # n in N
x = sp.symbols("x", real=True)                      # point of [0, 1]
f = (x**2 + 1) / n                                  # f_n(x)

# Part (b1), recomputed here: the sup norm of f_n on [0,1] is the largest |f_n| at an endpoint or an interior critical point.
crit = [c for c in sp.solve(sp.diff(f, x), x) if c.is_real and 0 < c < 1]   # f_n'(x) = 2x/n vanishes only at x = 0
candidates = [sp.Integer(0), sp.Integer(1)] + crit
values = [sp.Abs(f.subs(x, c)) for c in candidates]
sup_norm = values[0]
for val in values[1:]:
    if bool(val > sup_norm):
        sup_norm = val                              # keep the largest candidate value

# Solve sup_norm < eps for n > 0: the solution set is an open interval (threshold, oo).
eps = sp.Rational("0.001")
S = sp.solve_univariate_inequality(sup_norm < eps, n, relational=False, domain=sp.Interval.open(0, sp.oo))
threshold = S.inf
# S is upward closed, so every n > N satisfies the inequality exactly when N + 1 > threshold.
N_min = sp.floor(threshold)

# N works: the norm decreases in n, so it suffices that n = N + 1 satisfies the inequality.
assert bool(sp.diff(sup_norm, n) < 0)
assert bool(sup_norm.subs(n, N_min + 1) < eps)
# N - 1 does not work: n = N violates the inequality (there the norm equals eps exactly, not less).
assert not bool(sup_norm.subs(n, N_min) < eps)

# --- compare ---
EXPECTED_N = 2000
assert sp.simplify(N_min - EXPECTED_N) == 0, (N_min, EXPECTED_N)
print("PASS")
