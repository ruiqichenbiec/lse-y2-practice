import Mathlib

/-!
**Proposition (open balls are open).** In any metric space $(X,d)$, every open ball $B(x,R)$ is an open set. **Method:** for $y\in B(x,R)$ take $r=R-d(y,x)$, the room left to the edge, and control any $z\in B(y,r)$ with the triangle inequality [appendix]: $d(z,x)\le d(z,y)+d(y,x)<r+d(y,x)=R$.

Let $(X,d)$ be a metric space, $p,q\in X$ and $R>0$. Define
$$E=\{y\in X:\ d(y,p)+d(y,q)<R\}$$
(in the plane with the Euclidean metric this is the inside of an ellipse with foci $p$ and $q$).

- (a) Prove directly from the definition that $E$ is open: for $y\in E$, give an explicit $r>0$ with $B(y,r)\subset E$, and justify every inequality.
-/

theorem result {X : Type*} [MetricSpace X] (p q : X) (R : ℝ) (hR : 0 < R) :
    IsOpen {y : X | dist y p + dist y q < R} ∧
    ∀ y ∈ {y : X | dist y p + dist y q < R},
      0 < (R - dist y p - dist y q) / 2 ∧
      Metric.ball y ((R - dist y p - dist y q) / 2) ⊆ {y : X | dist y p + dist y q < R} := by
  have key : ∀ y ∈ {y : X | dist y p + dist y q < R},
      0 < (R - dist y p - dist y q) / 2 ∧
      Metric.ball y ((R - dist y p - dist y q) / 2) ⊆ {y : X | dist y p + dist y q < R} := by
    intro y hy
    have hy' : dist y p + dist y q < R := hy
    refine ⟨by linarith, ?_⟩
    intro z hz
    have hz' : dist z y < (R - dist y p - dist y q) / 2 := Metric.mem_ball.mp hz
    have h1 : dist z p ≤ dist z y + dist y p := dist_triangle z y p
    have h2 : dist z q ≤ dist z y + dist y q := dist_triangle z y q
    show dist z p + dist z q < R
    linarith
  refine ⟨Metric.isOpen_iff.mpr ?_, key⟩
  intro y hy
  obtain ⟨hpos, hsub⟩ := key y hy
  exact ⟨(R - dist y p - dist y q) / 2, hpos, hsub⟩

#print axioms result
