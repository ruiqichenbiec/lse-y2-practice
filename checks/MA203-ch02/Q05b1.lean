import Mathlib

/-!
**Lemma (finite intersections of open sets are open).** If $U_1,\dots,U_n$ are open in a metric space $(X,d)$, then $U_1\cap\dots\cap U_n$ is open. The word "finite" cannot be dropped (part (b) below gives a counterexample).

- (b) In $(\mathbb{R}^2,\|\cdot\|_2)$ let $D_n=B\big(\mathbf{0},1+\frac1n\big)$ for $n\in\mathbb{N}$. Determine $\bigcap_{n\in\mathbb{N}}D_n$ and show that it is not open. Where exactly does the proof of (a) break down for this infinite family?
-/

theorem result :
    (⋂ (n : ℕ) (_ : 1 ≤ n), Metric.ball (0 : EuclideanSpace ℝ (Fin 2)) (1 + 1 / (n : ℝ))) =
      {p : EuclideanSpace ℝ (Fin 2) | ‖p‖ ≤ 1} := by
  ext p
  simp only [Set.mem_iInter, Metric.mem_ball, dist_zero_right, Set.mem_setOf_eq]
  constructor
  · -- if ‖p‖ > 1, the Archimedean property gives n with 1/(n+1) < ‖p‖ - 1, and D_{n+1} excludes p
    intro h
    by_contra hp
    push_neg at hp
    obtain ⟨n, hn⟩ := exists_nat_one_div_lt (sub_pos.mpr hp)
    have h2 := h (n + 1) (by omega)
    push_cast at h2
    linarith
  · -- if ‖p‖ ≤ 1, then ‖p‖ < 1 + 1/n for every n ≥ 1
    intro hp n hn
    have hnpos : (0 : ℝ) < n := by exact_mod_cast (show 0 < n by omega)
    have hpos : 0 < 1 / (n : ℝ) := one_div_pos.mpr hnpos
    linarith

#print axioms result
