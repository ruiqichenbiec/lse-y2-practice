import Mathlib

/-!
**Proposition (open balls are open).** In any metric space $(X,d)$, every open ball $B(x,R)$ is an open set. **Method:** for $y\in B(x,R)$ take $r=R-d(y,x)$, the room left to the edge, and control any $z\in B(y,r)$ with the triangle inequality [appendix]: $d(z,x)\le d(z,y)+d(y,x)<r+d(y,x)=R$.

Let $(X,d)$ be a metric space, $p,q\in X$ and $R>0$. Define
$$E=\{y\in X:\ d(y,p)+d(y,q)<R\}$$
(in the plane with the Euclidean metric this is the inside of an ellipse with foci $p$ and $q$).

- (b) In $(\mathbb{R}^2,\|\cdot\|_2)$ (the Euclidean norm [appendix]) with $p=(-2,0)$, $q=(2,0)$ and $R=6$, check that $y=(0,\,1.5)$ and $y=(2,\,0)$ lie in $E$, and compute the radius $r$ given by your proof at each of them.
-/

theorem result :
    (!₂[2, 0] : EuclideanSpace ℝ (Fin 2)) ∈
      {y : EuclideanSpace ℝ (Fin 2) |
        ‖y - (!₂[-2, 0] : EuclideanSpace ℝ (Fin 2))‖ + ‖y - (!₂[2, 0] : EuclideanSpace ℝ (Fin 2))‖ < 6} := by
  have h1 : ‖(!₂[2, 0] : EuclideanSpace ℝ (Fin 2)) - (!₂[-2, 0] : EuclideanSpace ℝ (Fin 2))‖ < 5 := by
    rw [EuclideanSpace.norm_eq, Real.sqrt_lt' (by norm_num : (0:ℝ) < 5)]
    norm_num [Fin.sum_univ_two]
  have h2 : ‖(!₂[2, 0] : EuclideanSpace ℝ (Fin 2)) - (!₂[2, 0] : EuclideanSpace ℝ (Fin 2))‖ < 1 := by
    rw [EuclideanSpace.norm_eq, Real.sqrt_lt' (by norm_num : (0:ℝ) < 1)]
    norm_num [Fin.sum_univ_two]
  show ‖(!₂[2, 0] : EuclideanSpace ℝ (Fin 2)) - (!₂[-2, 0] : EuclideanSpace ℝ (Fin 2))‖ +
    ‖(!₂[2, 0] : EuclideanSpace ℝ (Fin 2)) - (!₂[2, 0] : EuclideanSpace ℝ (Fin 2))‖ < 6
  linarith

#print axioms result
