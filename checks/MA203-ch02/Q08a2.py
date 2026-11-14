r"""
- (a) In $(\mathbb{R}^2,\|\cdot\|_2)$ let $a_n=\big(\frac3n,\,-\frac4n\big)$. Compute $\|a_n-\mathbf{0}\|_2$ and find the smallest $N\in\mathbb{N}$ such that $\|a_n-\mathbf{0}\|_2<0.01$ for all $n>N$.
- (b) In $(C[0,1],\|\cdot\|_\infty)$ let $f_n(x)=\frac{x^2+1}{n}$ and let $\mathbf{0}$ be the zero function. Compute $\|f_n-\mathbf{0}\|_\infty$ and find the smallest $N$ that works for $\epsilon=0.001$.
"""
import sympy as sp

# --- solve: from the problem's data only ---
n = sp.symbols("n", positive=True)                # real variable for the inequality in n
a_n = sp.Matrix([3 / n, -4 / n])                  # a_n in R^2
v = a_n - sp.Matrix([0, 0])
norm_a = sp.simplify(sp.sqrt(v.dot(v)))           # ||a_n - 0||_2 = 5/n (recomputed from part (a1))
eps = sp.Rational("0.01")

# Solve ||a_n - 0||_2 < 0.01 for n > 0 (n is an index, so the domain is the positive reals):
# the solution set is an open interval (threshold, oo).
S = sp.solve_univariate_inequality(norm_a < eps, n, relational=False, domain=sp.Interval.open(0, sp.oo))
threshold = S.inf
# S is upward closed, so every n > N satisfies the inequality exactly when N + 1 > threshold.
N_min = sp.floor(threshold)

# N works: the norm decreases in n, so it suffices that n = N + 1 satisfies the inequality.
assert bool(sp.diff(norm_a, n) < 0)
assert bool(norm_a.subs(n, N_min + 1) < eps)
# N - 1 does not work: n = N violates the inequality.
assert not bool(norm_a.subs(n, N_min) < eps)

# --- compare ---
EXPECTED_N = 500
assert sp.simplify(N_min - EXPECTED_N) == 0, (N_min, EXPECTED_N)
print("PASS")
