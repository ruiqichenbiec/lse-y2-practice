import Mathlib

/-!
Problem MA203-L2-112, part (e), copied from the prompt. This file proves the second claim of (e): G is not closed.

- (e) Is $G=\{(x,y)\in\mathbb{R}^2:\ y\ge x^2\text{ and }x>0\}$ open, closed, both or neither? Justify your answer.

This file proves the claim that G is not closed in the Euclidean plane. The origin (0,0) lies outside G, because its x-coordinate is not greater than 0. For every r > 0 put s = min(r/2, 1/2); the point (s, s^2) lies in G, because s > 0 and s^2 >= s^2, and it lies in the open ball of radius r about (0,0), because its distance from (0,0) is sqrt(s^2 + s^4), which is less than r since s <= r/2 and s <= 1/2. So every ball about the origin meets G, the complement of G is not open, and G is not closed. The statement is the negation of IsClosed for G, and the witness is the proof.

The point (x,y) of R^2 is the vector p of EuclideanSpace over the reals indexed by Fin 2, with x = p 0 and y = p 1. The helper lemma dist_pair_E gives the Euclidean distance between two vectors written in coordinates.
-/

theorem dist_pair_E (a b c d : ℝ) :
    dist (!₂[a, b] : EuclideanSpace ℝ (Fin 2)) (!₂[c, d] : EuclideanSpace ℝ (Fin 2))
      = Real.sqrt ((a - c) ^ 2 + (b - d) ^ 2) := by
  rw [EuclideanSpace.dist_eq, Fin.sum_univ_two]
  simp [Real.dist_eq, sq_abs]

theorem result : ¬ IsClosed {p : EuclideanSpace ℝ (Fin 2) | p 1 ≥ (p 0) ^ 2 ∧ p 0 > 0} := by
  intro hc
  have hopen := hc.isOpen_compl
  have hmem : (!₂[0, 0] : EuclideanSpace ℝ (Fin 2)) ∈
      ({p : EuclideanSpace ℝ (Fin 2) | p 1 ≥ (p 0) ^ 2 ∧ p 0 > 0})ᶜ := by
    show ¬ ((!₂[0, 0] : EuclideanSpace ℝ (Fin 2)) 1 ≥ ((!₂[0, 0] : EuclideanSpace ℝ (Fin 2)) 0) ^ 2 ∧
      (!₂[0, 0] : EuclideanSpace ℝ (Fin 2)) 0 > 0)
    norm_num
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp hopen _ hmem
  obtain ⟨s, hs⟩ : ∃ s : ℝ, s = min (ε / 2) (1 / 2) := ⟨_, rfl⟩
  have hs_pos : 0 < s := by
    rw [hs]
    exact lt_min (by linarith) (by norm_num)
  have hs_le : s ≤ ε / 2 := by
    rw [hs]
    exact min_le_left _ _
  have hs_half : s ≤ 1 / 2 := by
    rw [hs]
    exact min_le_right _ _
  have hA : s ^ 2 ≤ (ε / 2) ^ 2 := by
    nlinarith [mul_nonneg (sub_nonneg.mpr hs_le) hs_pos.le, mul_nonneg (sub_nonneg.mpr hs_le) hε.le]
  have hB : s ^ 2 ≤ 1 / 4 := by
    nlinarith [mul_nonneg (sub_nonneg.mpr hs_half) hs_pos.le]
  have hC : s ^ 2 * s ^ 2 ≤ s ^ 2 * (1 / 4) := mul_le_mul_of_nonneg_left hB (sq_nonneg s)
  have hD : 0 < ε ^ 2 := pow_pos hε 2
  have hq : (!₂[s, s ^ 2] : EuclideanSpace ℝ (Fin 2)) ∈
      Metric.ball (!₂[0, 0] : EuclideanSpace ℝ (Fin 2)) ε := by
    rw [Metric.mem_ball, dist_pair_E, Real.sqrt_lt' hε]
    nlinarith [hA, hC, hD]
  have hnot := hball hq
  have hin : (!₂[s, s ^ 2] : EuclideanSpace ℝ (Fin 2)) ∈
      {p : EuclideanSpace ℝ (Fin 2) | p 1 ≥ (p 0) ^ 2 ∧ p 0 > 0} := by
    show (!₂[s, s ^ 2] : EuclideanSpace ℝ (Fin 2)) 1 ≥ ((!₂[s, s ^ 2] : EuclideanSpace ℝ (Fin 2)) 0) ^ 2 ∧
      (!₂[s, s ^ 2] : EuclideanSpace ℝ (Fin 2)) 0 > 0
    norm_num [hs_pos]
  exact hnot hin

#print axioms result
