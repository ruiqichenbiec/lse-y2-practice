import Mathlib

/-!
Problem Q2.12, part (d), copied from the prompt. This file proves the second claim of (d), that the parabola is not open.

- (d) Show that the parabola $P=\{(x,y)\in\mathbb{R}^2:\ y=x^2\}$ is closed, but not open.

This file proves the claim that P is not open in the Euclidean plane. The witness is the point (0,0), which lies in P. For every r > 0 the point (0, r/2) lies in the open ball of radius r about (0,0), because its distance from (0,0) is r/2 < r, but it does not lie in P, because r/2 is not equal to 0 = 0^2. The statement is the negation of IsOpen for P, and the witness is the proof.

The point (x,y) of R^2 is the vector p of EuclideanSpace over the reals indexed by Fin 2, with x = p 0 and y = p 1. The helper lemma dist_pair_E gives the Euclidean distance between two vectors written in coordinates.
-/

theorem dist_pair_E (a b c d : ℝ) :
    dist (!₂[a, b] : EuclideanSpace ℝ (Fin 2)) (!₂[c, d] : EuclideanSpace ℝ (Fin 2))
      = Real.sqrt ((a - c) ^ 2 + (b - d) ^ 2) := by
  rw [EuclideanSpace.dist_eq, Fin.sum_univ_two]
  simp [Real.dist_eq, sq_abs]

theorem result : ¬ IsOpen {p : EuclideanSpace ℝ (Fin 2) | p 1 = (p 0) ^ 2} := by
  intro h
  have hmem : (!₂[0, 0] : EuclideanSpace ℝ (Fin 2)) ∈
      {p : EuclideanSpace ℝ (Fin 2) | p 1 = (p 0) ^ 2} := by
    show (!₂[0, 0] : EuclideanSpace ℝ (Fin 2)) 1 = ((!₂[0, 0] : EuclideanSpace ℝ (Fin 2)) 0) ^ 2
    norm_num
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp h _ hmem
  have hq : (!₂[0, ε / 2] : EuclideanSpace ℝ (Fin 2)) ∈
      Metric.ball (!₂[0, 0] : EuclideanSpace ℝ (Fin 2)) ε := by
    rw [Metric.mem_ball, dist_pair_E, Real.sqrt_lt' hε]
    nlinarith
  have hG : (!₂[0, ε / 2] : EuclideanSpace ℝ (Fin 2)) 1
      = ((!₂[0, ε / 2] : EuclideanSpace ℝ (Fin 2)) 0) ^ 2 := hball hq
  norm_num at hG
  linarith

#print axioms result
