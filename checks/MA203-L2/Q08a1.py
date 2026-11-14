r"""
- (a) In $(\mathbb{R}^2,\|\cdot\|_2)$ let $a_n=\big(\frac3n,\,-\frac4n\big)$. Compute $\|a_n-\mathbf{0}\|_2$ and find the smallest $N\in\mathbb{N}$ such that $\|a_n-\mathbf{0}\|_2<0.01$ for all $n>N$.
- (b) In $(C[0,1],\|\cdot\|_\infty)$ let $f_n(x)=\frac{x^2+1}{n}$ and let $\mathbf{0}$ be the zero function. Compute $\|f_n-\mathbf{0}\|_\infty$ and find the smallest $N$ that works for $\epsilon=0.001$.
"""
import sympy as sp

# --- solve: from the problem's data only ---
n = sp.symbols("n", positive=True, integer=True)   # n in N
a_n = sp.Matrix([3 / n, -4 / n])                  # a_n = (3/n, -4/n) in R^2
v = a_n - sp.Matrix([0, 0])                       # a_n - 0
norm_a = sp.simplify(sp.sqrt(v.dot(v)))           # ||a_n - 0||_2, for every n

# --- compare ---
EXPECTED_norm = 5 / n
assert sp.simplify(norm_a - EXPECTED_norm) == 0, (norm_a, EXPECTED_norm)
print("PASS")
