import Mathlib

/-!
Definition the problem relies on: for $f:X\to Y$ and $V\subset Y$: $f^{-1}(V)=\{x\in X:\ f(x)\in V\}$.

- (a) Let $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2-2x$. Compute $f^{-1}\big((-1,3)\big)$ and $f^{-1}\big((-\infty,-1)\big)$, and say whether each is open in $\mathbb{R}$.
-/

theorem result : (fun x : ℝ => x ^ 2 - 2 * x) ⁻¹' Set.Iio (-1) = ∅ := by
  ext x
  simp only [Set.mem_preimage, Set.mem_Iio, Set.mem_empty_iff_false, iff_false, not_lt]
  nlinarith [sq_nonneg (x - 1)]

#print axioms result
