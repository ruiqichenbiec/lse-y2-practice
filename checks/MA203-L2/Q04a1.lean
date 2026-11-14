import Mathlib

/-!
Definition the problem relies on: for $f:X\to Y$ and $V\subset Y$: $f^{-1}(V)=\{x\in X:\ f(x)\in V\}$.

- (a) Let $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2-2x$. Compute $f^{-1}\big((-1,3)\big)$ and $f^{-1}\big((-\infty,-1)\big)$, and say whether each is open in $\mathbb{R}$.
-/

theorem result : (fun x : ℝ => x ^ 2 - 2 * x) ⁻¹' Set.Ioo (-1) 3 = Set.Ioo (-1) 1 ∪ Set.Ioo 1 3 := by
  ext x
  simp only [Set.mem_preimage, Set.mem_Ioo, Set.mem_union]
  constructor
  · rintro ⟨h1, h2⟩
    have hlo : -1 < x := by nlinarith [sq_nonneg (x + 1)]
    have hhi : x < 3 := by nlinarith [sq_nonneg (x - 3)]
    rcases lt_trichotomy x 1 with hx | hx | hx
    · exact Or.inl ⟨hlo, hx⟩
    · subst hx
      norm_num at h1
    · exact Or.inr ⟨hx, hhi⟩
  · rintro (⟨h1, h2⟩ | ⟨h1, h2⟩)
    · constructor
      · nlinarith [mul_pos (by linarith : (0:ℝ) < 1 - x) (by linarith : (0:ℝ) < 1 - x)]
      · nlinarith [mul_pos (by linarith : (0:ℝ) < x + 1) (by linarith : (0:ℝ) < 3 - x)]
    · constructor
      · nlinarith [mul_pos (by linarith : (0:ℝ) < x - 1) (by linarith : (0:ℝ) < x - 1)]
      · nlinarith [mul_pos (by linarith : (0:ℝ) < x + 1) (by linarith : (0:ℝ) < 3 - x)]

#print axioms result
