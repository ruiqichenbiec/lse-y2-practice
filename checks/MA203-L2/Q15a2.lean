import Mathlib

/-!
Equip $\mathbb{R}$ with $|\cdot|$ and $\mathbb{R}^2$ with the Euclidean norm $\|\cdot\|_2$. For $A,B\subset\mathbb{R}$ write $A\times B=\{(x,y)\in\mathbb{R}^2:\ x\in A,\ y\in B\}$.

- (a) Show that $|p_1-q_1|\le\|p-q\|_2$ and $|p_2-q_2|\le\|p-q\|_2$ for all $p=(p_1,p_2)$, $q=(q_1,q_2)\in\mathbb{R}^2$. **(2 marks)**
-/

theorem result : ∀ p q : EuclideanSpace ℝ (Fin 2), |p 1 - q 1| ≤ ‖p - q‖ := by
  intro p q
  rw [EuclideanSpace.norm_eq, Fin.sum_univ_two]
  apply Real.abs_le_sqrt
  simp only [PiLp.sub_apply, Real.norm_eq_abs, sq_abs]
  nlinarith [sq_nonneg (p 0 - q 0)]

#print axioms result
