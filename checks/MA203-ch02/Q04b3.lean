import Mathlib

/-!
Definition the problem relies on: for $f:X\to Y$ and $V\subset Y$: $f^{-1}(V)=\{x\in X:\ f(x)\in V\}$.

A later result, the open-set characterisation of continuity [appendix], says that a map between metric spaces is continuous exactly when the inverse image of every open set is open.

- (b) Let $g:\mathbb{R}\to\mathbb{R}$ be given by $g(x)=-1$ for $x\le2$ and $g(x)=x$ for $x>2$. Compute $g^{-1}\big((-2,1)\big)$ and decide whether it is open. What does the open-set characterisation of continuity [appendix] then tell you about $g$?
-/

theorem result : ¬ Continuous (fun x : ℝ => if x ≤ 2 then (-1 : ℝ) else x) := by
  intro hc
  have hopen : IsOpen ((fun x : ℝ => if x ≤ 2 then (-1 : ℝ) else x) ⁻¹' Set.Ioo (-2) 1) :=
    IsOpen.preimage hc isOpen_Ioo
  have heq : (fun x : ℝ => if x ≤ 2 then (-1 : ℝ) else x) ⁻¹' Set.Ioo (-2) 1 = Set.Iic 2 := by
    ext x
    by_cases h : x ≤ 2
    · have hg : (if x ≤ 2 then (-1 : ℝ) else x) = -1 := if_pos h
      simp only [Set.mem_preimage, Set.mem_Ioo, Set.mem_Iic, hg]
      norm_num [h]
    · have h2 : 2 < x := not_le.mp h
      have hg : (if x ≤ 2 then (-1 : ℝ) else x) = x := if_neg h
      simp only [Set.mem_preimage, Set.mem_Ioo, Set.mem_Iic, hg]
      constructor
      · rintro ⟨_, h1⟩
        linarith
      · intro h3
        exact absurd h3 h
  rw [heq] at hopen
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp hopen 2 (Set.mem_Iic.mpr le_rfl)
  have hmem : (2 + ε / 2 : ℝ) ∈ Metric.ball (2 : ℝ) ε := by
    rw [Metric.mem_ball, Real.dist_eq, abs_lt]
    constructor <;> linarith
  have hle : 2 + ε / 2 ≤ (2 : ℝ) := Set.mem_Iic.mp (hball hmem)
  linarith

#print axioms result
