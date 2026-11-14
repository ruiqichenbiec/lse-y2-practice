import Mathlib

/-!
Equip $\mathbb{R}$ with $|\cdot|$ and $\mathbb{R}^2$ with the Euclidean norm $\|\cdot\|_2$. For $A,B\subset\mathbb{R}$ write $A\times B=\{(x,y)\in\mathbb{R}^2:\ x\in A,\ y\in B\}$.

- (d) Determine whether $S=[0,1]\times(0,1)$ is open, closed, both or neither in $\mathbb{R}^2$. Justify your answer. **(4 marks)**
-/

theorem result :
    ¬ IsOpen {p : EuclideanSpace ℝ (Fin 2) | p 0 ∈ Set.Icc (0:ℝ) 1 ∧ p 1 ∈ Set.Ioo (0:ℝ) 1} := by
  intro h
  have hp0 : (EuclideanSpace.single (1 : Fin 2) (1/2 : ℝ) : EuclideanSpace ℝ (Fin 2)) 0 = 0 := by
    simp
  have hp1 : (EuclideanSpace.single (1 : Fin 2) (1/2 : ℝ) : EuclideanSpace ℝ (Fin 2)) 1 = 1/2 := by
    simp
  have hpS : (EuclideanSpace.single (1 : Fin 2) (1/2 : ℝ) : EuclideanSpace ℝ (Fin 2)) ∈
      {p : EuclideanSpace ℝ (Fin 2) | p 0 ∈ Set.Icc (0:ℝ) 1 ∧ p 1 ∈ Set.Ioo (0:ℝ) 1} := by
    simp only [Set.mem_setOf_eq]
    rw [hp0, hp1]
    exact ⟨Set.mem_Icc.mpr ⟨le_refl _, zero_le_one⟩, Set.mem_Ioo.mpr ⟨by norm_num, by norm_num⟩⟩
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp h _ hpS
  have hq_ball : (EuclideanSpace.single (0 : Fin 2) (-(ε/2)) + EuclideanSpace.single (1 : Fin 2) (1/2 : ℝ) : EuclideanSpace ℝ (Fin 2)) ∈
      Metric.ball (EuclideanSpace.single (1 : Fin 2) (1/2 : ℝ) : EuclideanSpace ℝ (Fin 2)) ε := by
    rw [Metric.mem_ball, dist_eq_norm, add_sub_cancel_right, PiLp.norm_single, Real.norm_eq_abs,
      abs_neg, abs_of_pos (show (0:ℝ) < ε / 2 by linarith)]
    linarith
  have hq_S := hball hq_ball
  have hq0 : (EuclideanSpace.single (0 : Fin 2) (-(ε/2)) + EuclideanSpace.single (1 : Fin 2) (1/2 : ℝ) : EuclideanSpace ℝ (Fin 2)) 0 = -(ε/2) := by
    simp
  have hq_mem : (EuclideanSpace.single (0 : Fin 2) (-(ε/2)) + EuclideanSpace.single (1 : Fin 2) (1/2 : ℝ) : EuclideanSpace ℝ (Fin 2)) 0 ∈ Set.Icc (0:ℝ) 1 :=
    hq_S.1
  rw [hq0] at hq_mem
  linarith [(Set.mem_Icc.mp hq_mem).1]

#print axioms result
