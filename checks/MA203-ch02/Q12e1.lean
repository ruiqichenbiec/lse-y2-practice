import Mathlib

/-!
Problem Q2.12, part (e), copied from the prompt. This file proves the first claim of (e): G is not open.

- (e) Is $G=\{(x,y)\in\mathbb{R}^2:\ y\ge x^2\text{ and }x>0\}$ open, closed, both or neither? Justify your answer.

This file proves the claim that G is not open in the Euclidean plane. The witness is the point (1,1), which lies in G because 1 >= 1^2 and 1 > 0. For every r > 0 the point (1, 1 - r/2) lies in the open ball of radius r about (1,1), because its distance from (1,1) is r/2 < r, but it does not lie in G, because 1 - r/2 < 1 = 1^2. The statement is the negation of IsOpen for G, and the witness is the proof.

The point (x,y) of R^2 is the vector p of EuclideanSpace over the reals indexed by Fin 2, with x = p 0 and y = p 1. The helper lemma dist_pair_E gives the Euclidean distance between two vectors written in coordinates.
-/

theorem dist_pair_E (a b c d : ℝ) :
    dist (!₂[a, b] : EuclideanSpace ℝ (Fin 2)) (!₂[c, d] : EuclideanSpace ℝ (Fin 2))
      = Real.sqrt ((a - c) ^ 2 + (b - d) ^ 2) := by
  rw [EuclideanSpace.dist_eq, Fin.sum_univ_two]
  simp [Real.dist_eq, sq_abs]

theorem result : ¬ IsOpen {p : EuclideanSpace ℝ (Fin 2) | p 1 ≥ (p 0) ^ 2 ∧ p 0 > 0} := by
  intro h
  have hmem : (!₂[1, 1] : EuclideanSpace ℝ (Fin 2)) ∈
      {p : EuclideanSpace ℝ (Fin 2) | p 1 ≥ (p 0) ^ 2 ∧ p 0 > 0} := by
    show (!₂[1, 1] : EuclideanSpace ℝ (Fin 2)) 1 ≥ ((!₂[1, 1] : EuclideanSpace ℝ (Fin 2)) 0) ^ 2 ∧
      (!₂[1, 1] : EuclideanSpace ℝ (Fin 2)) 0 > 0
    norm_num
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp h _ hmem
  have hq : (!₂[1, 1 - ε / 2] : EuclideanSpace ℝ (Fin 2)) ∈
      Metric.ball (!₂[1, 1] : EuclideanSpace ℝ (Fin 2)) ε := by
    rw [Metric.mem_ball, dist_pair_E, Real.sqrt_lt' hε]
    nlinarith
  have hG : ((!₂[1, 1 - ε / 2] : EuclideanSpace ℝ (Fin 2)) 1 ≥
      ((!₂[1, 1 - ε / 2] : EuclideanSpace ℝ (Fin 2)) 0) ^ 2) ∧
      (!₂[1, 1 - ε / 2] : EuclideanSpace ℝ (Fin 2)) 0 > 0 := hball hq
  have hG1 := hG.1
  norm_num at hG1
  linarith

#print axioms result
