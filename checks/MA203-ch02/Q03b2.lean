import Mathlib

/-!
**Lemma (arbitrary unions of open sets are open).** Let $U_i$ ($i\in I$) be any family of open sets in a metric space $(X,d)$, indexed by an arbitrary set $I$. Then $\bigcup_{i\in I}U_i$ is open.

- (b) In $(\mathbb{R}^2,\|\cdot\|_2)$, show that the strip $W=\{(x,y)\in\mathbb{R}^2:\ |y|<1\}$ equals $\bigcup_{t\in\mathbb{R}}B\big((t,0),1\big)$, and deduce that $W$ is open.
-/

-- This file proves only the openness of W in (b); the equality in (b) is item Q03b1.
-- The Euclidean plane is EuclideanSpace ℝ (Fin 2) with its Euclidean distance.
-- The point (x,y) is !₂[x, y], so p 0 is x and p 1 is y.

theorem result : IsOpen {p : EuclideanSpace ℝ (Fin 2) | |p 1| < 1} := by
  rw [Metric.isOpen_iff]
  intro p hp
  have hp' : |p 1| < 1 := hp
  refine ⟨1 - |p 1|, by linarith, fun q hq => ?_⟩
  have hq' : dist q p < 1 - |p 1| := Metric.mem_ball.mp hq
  have h1 : dist (q 1) (p 1) ≤ dist q p := PiLp.dist_apply_le q p 1
  rw [Real.dist_eq] at h1
  have h2 : |q 1 - p 1| < 1 - |p 1| := lt_of_le_of_lt h1 hq'
  obtain ⟨h3, h4⟩ := abs_lt.mp h2
  have h5 := le_abs_self (p 1)
  have h6 := neg_abs_le (p 1)
  show |q 1| < 1
  exact abs_lt.mpr ⟨by linarith, by linarith⟩

#print axioms result
