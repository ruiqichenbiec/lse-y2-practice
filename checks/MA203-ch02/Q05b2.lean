import Mathlib

/-!
**Lemma (finite intersections of open sets are open).** If $U_1,\dots,U_n$ are open in a metric space $(X,d)$, then $U_1\cap\dots\cap U_n$ is open. The word "finite" cannot be dropped (part (b) below gives a counterexample).

- (b) In $(\mathbb{R}^2,\|\cdot\|_2)$ let $D_n=B\big(\mathbf{0},1+\frac1n\big)$ for $n\in\mathbb{N}$. Determine $\bigcap_{n\in\mathbb{N}}D_n$ and show that it is not open. Where exactly does the proof of (a) break down for this infinite family?
-/

theorem result : ¬ IsOpen {p : EuclideanSpace ℝ (Fin 2) | ‖p‖ ≤ 1} := by
  intro h
  -- a vector e of norm 1 (for instance (1,0) = EuclideanSpace.single 0 1)
  obtain ⟨e, he⟩ : ∃ e : EuclideanSpace ℝ (Fin 2), ‖e‖ = 1 :=
    ⟨EuclideanSpace.single 0 1, by simp⟩
  have hmem : e ∈ {p : EuclideanSpace ℝ (Fin 2) | ‖p‖ ≤ 1} := le_of_eq he
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp h e hmem
  -- the point (1 + ε/2) e (the point (1 + ε/2, 0)) lies in the ball B(e, ε)
  have hq : (1 + ε / 2) • e ∈ Metric.ball e ε := by
    rw [Metric.mem_ball, dist_eq_norm]
    have hsub : (1 + ε / 2) • e - e = (ε / 2) • e := by
      rw [add_smul, one_smul]; abel
    rw [hsub, norm_smul, he, Real.norm_of_nonneg (by linarith : (0:ℝ) ≤ ε / 2)]
    linarith
  -- but its norm is 1 + ε/2 > 1, so it is not in the closed disc
  have hK : ‖(1 + ε / 2) • e‖ ≤ 1 := hball hq
  rw [norm_smul, he, Real.norm_of_nonneg (by linarith : (0:ℝ) ≤ 1 + ε / 2)] at hK
  linarith

#print axioms result
