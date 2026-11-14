r"""
- (a) In $(\mathbb{R}^2,\|\cdot\|_2)$ let $a_n=\big(\frac3n,\,-\frac4n\big)$. Compute $\|a_n-\mathbf{0}\|_2$ and find the smallest $N\in\mathbb{N}$ such that $\|a_n-\mathbf{0}\|_2<0.01$ for all $n>N$.
- (b) In $(C[0,1],\|\cdot\|_\infty)$ let $f_n(x)=\frac{x^2+1}{n}$ and let $\mathbf{0}$ be the zero function. Compute $\|f_n-\mathbf{0}\|_\infty$ and find the smallest $N$ that works for $\epsilon=0.001$.
"""
import sympy as sp

# --- solve: from the problem's data only ---
n = sp.symbols("n", positive=True, integer=True)   # n in N
x = sp.symbols("x", real=True)                      # point of [0, 1]
f = (x**2 + 1) / n                                  # f_n(x)

# Sup norm over [0,1] of |f_n|: the maximum is at an endpoint or at an interior critical point.
crit = [c for c in sp.solve(sp.diff(f, x), x) if c.is_real and 0 < c < 1]   # f_n'(x) = 2x/n vanishes only at x = 0
candidates = [sp.Integer(0), sp.Integer(1)] + crit
values = [sp.Abs(f.subs(x, c)) for c in candidates]
sup_norm = values[0]
for val in values[1:]:
    if bool(val > sup_norm):
        sup_norm = val                              # keep the largest candidate value

# --- compare ---
EXPECTED_norm = 2 / n
assert sp.simplify(sup_norm - EXPECTED_norm) == 0, (sup_norm, EXPECTED_norm)
print("PASS")
