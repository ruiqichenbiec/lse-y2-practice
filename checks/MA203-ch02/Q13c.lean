import Mathlib

/-!
Let $X=C[0,1]$, the vector space of continuous functions $f:[0,1]\to\mathbb{R}$ with pointwise operations, and consider the norms
$$\|f\|_\infty=\max_{x\in[0,1]}|f(x)|,\qquad\|f\|_1=\int_0^1|f(x)|\,dx .$$
Let $P=\{f\in X:\ f(x)>0\text{ for all }x\in[0,1]\}$ and $Q=\{f\in X:\ f(x)\ge0\text{ for all }x\in[0,1]\}$.

(c) Show that $P$ is not open in $(X,\|\cdot\|_1)$.
-/

-- Lean choices: the functions of C[0,1] are modelled by functions g : ℝ → ℝ that are
-- ContinuousOn [0,1]. Membership in P and the 1-norm only involve the values on [0,1], so this
-- is the same space. The 1-norm is written out as the integral over [0,1] of |g x - 1|, so no
-- Mathlib norm instance is used (Mathlib's instance on C(Set.Icc 0 1, ℝ) is the sup norm).
-- Unfolding of the claim: P is open for the 1-norm distance d1 f g = integral over [0,1] of
-- |f x - g x| iff every f in P has some eps > 0 such that every g with d1 f g < eps lies in P
-- (IsOpen in a metric space, via balls). Taking the point f = 1, which lies in P, the negation
-- is: for every eps > 0 some continuous g with d1 1 g < eps is not in P. The statement below is
-- exactly this conjunction (1 lies in P, and for every r > 0 there is such a g), so proving it
-- proves that P is not open for the 1-norm.
-- Witness: g x = 1 - 2 x^n on [0,1]. Then g 1 = -1 <= 0, and the integral of |g x - 1|
-- over [0,1] equals the integral of 2 x^n, which is 2/(n+1) < r for n large.
theorem result :
    (ContinuousOn (fun _ : ℝ => (1:ℝ)) (Set.Icc (0:ℝ) 1) ∧
      ∀ x ∈ Set.Icc (0:ℝ) 1, (0:ℝ) < (fun _ : ℝ => (1:ℝ)) x) ∧
    ∀ r : ℝ, 0 < r → ∃ g : ℝ → ℝ, ContinuousOn g (Set.Icc (0:ℝ) 1) ∧
      ¬ (∀ x ∈ Set.Icc (0:ℝ) 1, 0 < g x) ∧
      (∫ x in (0:ℝ)..1, |g x - 1|) < r := by
  refine ⟨⟨continuousOn_const, fun x _ => one_pos⟩, ?_⟩
  intro r hr
  obtain ⟨n, hn⟩ := exists_nat_gt (2 / r)
  have hn1 : (0:ℝ) < (n:ℝ) + 1 := by positivity
  refine ⟨fun x => 1 - 2 * x ^ n, ?_, ?_, ?_⟩
  · exact Continuous.continuousOn (by fun_prop)
  · intro h
    have h1 := h 1 ⟨zero_le_one, le_refl _⟩
    norm_num at h1
  · have hcongr : (∫ x in (0:ℝ)..1, |(1 - 2 * x ^ n) - 1|) = ∫ x in (0:ℝ)..1, 2 * x ^ n := by
      apply intervalIntegral.integral_congr
      intro x hx
      rw [Set.uIcc_of_le (zero_le_one : (0:ℝ) ≤ 1)] at hx
      have hx0 : 0 ≤ x := hx.1
      have hnn : (0:ℝ) ≤ 2 * x ^ n := mul_nonneg (by norm_num) (pow_nonneg hx0 n)
      show |(1 - 2 * x ^ n) - 1| = 2 * x ^ n
      rw [show (1 - 2 * x ^ n) - 1 = -(2 * x ^ n) by ring, abs_neg, abs_of_nonneg hnn]
    have hint : (∫ x in (0:ℝ)..1, x ^ n) = 1 / ((n:ℝ) + 1) := by
      rw [integral_pow, one_pow, zero_pow (by norm_num : n + 1 ≠ 0), sub_zero]
    show (∫ x in (0:ℝ)..1, |(1 - 2 * x ^ n) - 1|) < r
    rw [hcongr, intervalIntegral.integral_const_mul, hint, mul_one_div, div_lt_iff₀ hn1]
    have h2 : 2 < (n:ℝ) * r := (div_lt_iff₀ hr).mp hn
    nlinarith

#print axioms result
