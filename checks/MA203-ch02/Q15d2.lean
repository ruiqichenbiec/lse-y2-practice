import Mathlib

/-!
Equip $\mathbb{R}$ with $|\cdot|$ and $\mathbb{R}^2$ with the Euclidean norm $\|\cdot\|_2$. For $A,B\subset\mathbb{R}$ write $A\times B=\{(x,y)\in\mathbb{R}^2:\ x\in A,\ y\in B\}$.

- (d) Determine whether $S=[0,1]\times(0,1)$ is open, closed, both or neither in $\mathbb{R}^2$. Justify your answer. **(4 marks)**
-/

theorem result :
    ¬ IsClosed {p : EuclideanSpace ℝ (Fin 2) | p 0 ∈ Set.Icc (0:ℝ) 1 ∧ p 1 ∈ Set.Ioo (0:ℝ) 1} := by
  intro h
  have hc1 : (EuclideanSpace.single (1 : Fin 2) (1 : ℝ) : EuclideanSpace ℝ (Fin 2)) 1 = 1 := by
    simp
  have hcmem : (EuclideanSpace.single (1 : Fin 2) (1 : ℝ) : EuclideanSpace ℝ (Fin 2)) ∈
      {p : EuclideanSpace ℝ (Fin 2) | p 0 ∈ Set.Icc (0:ℝ) 1 ∧ p 1 ∈ Set.Ioo (0:ℝ) 1}ᶜ := by
    intro hS
    have hS1 : (EuclideanSpace.single (1 : Fin 2) (1 : ℝ) : EuclideanSpace ℝ (Fin 2)) 1 ∈
        Set.Ioo (0:ℝ) 1 := hS.2
    rw [hc1] at hS1
    exact lt_irrefl 1 (Set.mem_Ioo.mp hS1).2
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp h.isOpen_compl _ hcmem
  have hmin_pos : 0 < min ε 1 := lt_min hε one_pos
  have hmin_le : min ε 1 ≤ ε := min_le_left ε 1
  have hmin_le1 : min ε 1 ≤ 1 := min_le_right ε 1
  have hdiff : (EuclideanSpace.single (1 : Fin 2) (1 - min ε 1 / 2) : EuclideanSpace ℝ (Fin 2)) -
      (EuclideanSpace.single (1 : Fin 2) (1 : ℝ) : EuclideanSpace ℝ (Fin 2)) =
      EuclideanSpace.single (1 : Fin 2) (-(min ε 1 / 2)) := by
    rw [← PiLp.single_sub]
    congr 1
    ring
  have hq_ball : (EuclideanSpace.single (1 : Fin 2) (1 - min ε 1 / 2) : EuclideanSpace ℝ (Fin 2)) ∈
      Metric.ball (EuclideanSpace.single (1 : Fin 2) (1 : ℝ) : EuclideanSpace ℝ (Fin 2)) ε := by
    rw [Metric.mem_ball, dist_eq_norm, hdiff, PiLp.norm_single, Real.norm_eq_abs, abs_neg,
      abs_of_pos (show (0:ℝ) < min ε 1 / 2 by linarith)]
    linarith
  have hq_S : (EuclideanSpace.single (1 : Fin 2) (1 - min ε 1 / 2) : EuclideanSpace ℝ (Fin 2)) ∈
      {p : EuclideanSpace ℝ (Fin 2) | p 0 ∈ Set.Icc (0:ℝ) 1 ∧ p 1 ∈ Set.Ioo (0:ℝ) 1} := by
    have hq0 : (EuclideanSpace.single (1 : Fin 2) (1 - min ε 1 / 2) : EuclideanSpace ℝ (Fin 2)) 0 = 0 := by
      simp
    have hq1 : (EuclideanSpace.single (1 : Fin 2) (1 - min ε 1 / 2) : EuclideanSpace ℝ (Fin 2)) 1 = 1 - min ε 1 / 2 := by
      simp
    simp only [Set.mem_setOf_eq]
    rw [hq0, hq1]
    exact ⟨Set.mem_Icc.mpr ⟨le_refl _, zero_le_one⟩, Set.mem_Ioo.mpr ⟨by linarith, by linarith⟩⟩
  exact hball hq_ball hq_S

#print axioms result
