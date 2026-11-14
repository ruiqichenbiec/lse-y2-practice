import Mathlib

/-!
Work in $(\mathbb{R},|\cdot|)$.

- (a) Let $a_n=\frac1{n^2}$. For $\epsilon=0.01$, find an $N$ such that $|a_m-a_n|<\epsilon$ for all $m,n>N$.

Statement relied on (Cauchy sequence): $(a_n)$ in $(X,d)$ is Cauchy if $\forall\epsilon>0\ \exists N\in\mathbb{N}\ \forall m,n>N:\ d(a_m,a_n)<\epsilon$. In $\mathbb{R}$: $|a_m-a_n|<\epsilon$.
-/

theorem result : ∀ m n : ℕ, 9 < m → 9 < n → |1 / (m : ℝ) ^ 2 - 1 / (n : ℝ) ^ 2| < 0.01 := by
  intro m n hm hn
  have hm10 : (10 : ℝ) ≤ (m : ℝ) := by
    have : 10 ≤ m := by omega
    exact_mod_cast this
  have hn10 : (10 : ℝ) ≤ (n : ℝ) := by
    have : 10 ≤ n := by omega
    exact_mod_cast this
  have hm2 : (100 : ℝ) ≤ (m : ℝ) ^ 2 := by nlinarith
  have hn2 : (100 : ℝ) ≤ (n : ℝ) ^ 2 := by nlinarith
  have hs : 0 < 1 / (m : ℝ) ^ 2 := one_div_pos.mpr (by linarith)
  have ht : 0 < 1 / (n : ℝ) ^ 2 := one_div_pos.mpr (by linarith)
  have hsle : 1 / (m : ℝ) ^ 2 ≤ 1 / 100 := one_div_le_one_div_of_le (by norm_num) hm2
  have htle : 1 / (n : ℝ) ^ 2 ≤ 1 / 100 := one_div_le_one_div_of_le (by norm_num) hn2
  have h001 : (0.01 : ℝ) = 1 / 100 := by norm_num
  rw [h001, abs_sub_lt_iff]
  constructor <;> linarith

#print axioms result
