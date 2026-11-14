r"""
Let $(X,d)$ be a metric space, $p,q\in X$ and $R>0$. Define
$$E=\{y\in X:\ d(y,p)+d(y,q)<R\}$$
(in the plane with the Euclidean metric this is the inside of an ellipse with foci $p$ and $q$).

- (a) Prove directly from the definition that $E$ is open: for $y\in E$, give an explicit $r>0$ with $B(y,r)\subset E$, and justify every inequality.
- (b) In $(\mathbb{R}^2,\|\cdot\|_2)$ (the Euclidean norm [appendix]) with $p=(-2,0)$, $q=(2,0)$ and $R=6$, check that $y=(0,\,1.5)$ and $y=(2,\,0)$ lie in $E$, and compute the radius $r$ given by your proof at each of them.
"""
import sympy as sp

# --- solve: from the problem's data only ---
# Model: the Euclidean plane, p = (-2,0), q = (2,0), R = 6, and the point y = (0, 1.5).
p = sp.Matrix([-2, 0])
q = sp.Matrix([2, 0])
R = sp.Integer(6)
y = sp.Matrix([0, sp.Rational("1.5")])

d_yp = sp.sqrt((y - p).dot(y - p))     # ||y - p||_2
d_yq = sp.sqrt((y - q).dot(y - q))     # ||y - q||_2

# y lies in E, i.e. d(y,p) + d(y,q) < R.
assert sp.simplify(d_yp + d_yq - R) < 0

# The proof in (a): the room left to the edge is delta = R - d(y,p) - d(y,q) > 0,
# and the two distances can grow together by at most 2 d(z,y), so the radius is r = delta / 2.
delta = R - d_yp - d_yq
r = delta / 2

# --- compare ---
EXPECTED_r = sp.Rational(1, 2)
assert sp.simplify(r - EXPECTED_r) == 0, (r, EXPECTED_r)
print("PASS")
