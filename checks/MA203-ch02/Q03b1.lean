import Mathlib

/-!
- (b) In $(\mathbb{R}^2,\|\cdot\|_2)$, show that the strip $W=\{(x,y)\in\mathbb{R}^2:\ |y|<1\}$ equals $\bigcup_{t\in\mathbb{R}}B\big((t,0),1\big)$, and deduce that $W$ is open.
-/

-- This file proves only the equality in (b); the openness of W is item Q03b2.
-- The Euclidean plane is EuclideanSpace ℝ (Fin 2) with its Euclidean distance.
-- The point (x,y) is !₂[x, y], so p 0 is x and p 1 is y; the centre (t,0) is !₂[t, 0].

theorem result :
    {p : EuclideanSpace ℝ (Fin 2) | |p 1| < 1} = ⋃ t : ℝ, Metric.ball (!₂[t, 0] : EuclideanSpace ℝ (Fin 2)) 1 := by
  ext p
  simp only [Set.mem_ofPred_eq, Set.mem_iUnion, Metric.mem_ball, EuclideanSpace.dist_eq,
    Fin.sum_univ_two, Real.dist_eq, sq_abs, Matrix.cons_val_zero, Matrix.cons_val_one, sub_zero]
  constructor
  · intro h
    refine ⟨p 0, ?_⟩
    simpa [Real.sqrt_sq_eq_abs] using h
  · rintro ⟨t, ht⟩
    rw [Real.sqrt_lt' one_pos, one_pow] at ht
    have h2 : p 1 ^ 2 < 1 := by linarith [sq_nonneg (p 0 - t)]
    exact (sq_lt_one_iff_abs_lt_one _).mp h2

#print axioms result
