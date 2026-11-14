import Mathlib

/-!
Work in $(C[0,1],\|\cdot\|_\infty)$, let $\mathbf{0}$ be the zero function and $f_n(x)=x^n(1-x)$. Show that $\|f_n-\mathbf{0}\|_\infty\le\frac1{n+1}$, and prove from the definition that $(f_n)_{n\in\mathbb{N}}$ converges to $\mathbf{0}$.

Statement relied on (method): **Method (proving convergence from the definition).** To prove $a_n\to L$ in a metric space from the definition: (1) compute or bound $d(a_n,L)$ by a simple expression that tends to 0, such as $\frac Cn$; (2) given $\epsilon>0$, choose $N$ from that bound (e.g. $N>\frac C\epsilon$); (3) check that every $n>N$ gives $d(a_n,L)<\epsilon$. In $(C[a,b],\|\cdot\|_\infty)$, step (1) is a maximisation over $x$.

Lean choices: C[0,1] is C(Set.Icc (0:ℝ) 1, ℝ) with Mathlib's norm, which is the sup norm for a compact domain. The sequence f_n is defined by fQ09 below, and the zero function is the zero of that space.
-/

noncomputable def fQ09 (n : ℕ) : C(Set.Icc (0:ℝ) 1, ℝ) :=
  ⟨fun x => (x : ℝ) ^ n * (1 - (x : ℝ)), by fun_prop⟩

lemma key_bound_Q09 (n : ℕ) (x : ℝ) (h0 : 0 ≤ x) (h1 : x ≤ 1) :
    ((n : ℝ) + 1) * (x ^ n * (1 - x)) ≤ 1 := by
  have hsum : ∑ i ∈ Finset.range (n + 1), x ^ i * (1 - x) = 1 - x ^ (n + 1) := by
    rw [← geom_sum_mul_neg x (n + 1), Finset.sum_mul]
  have hle : ∑ i ∈ Finset.range (n + 1), x ^ n * (1 - x)
      ≤ ∑ i ∈ Finset.range (n + 1), x ^ i * (1 - x) := by
    apply Finset.sum_le_sum
    intro i hi
    have hin : i ≤ n := by
      have := Finset.mem_range.mp hi
      omega
    exact mul_le_mul_of_nonneg_right (pow_le_pow_of_le_one h0 h1 hin) (by linarith)
  rw [hsum, Finset.sum_const, Finset.card_range, nsmul_eq_mul] at hle
  have hpow : 0 ≤ x ^ (n + 1) := pow_nonneg h0 _
  push_cast at hle
  linarith

theorem result : (∀ n : ℕ, ‖fQ09 n - 0‖ ≤ 1 / ((n : ℝ) + 1)) ∧
    Filter.Tendsto fQ09 Filter.atTop (nhds 0) := by
  have hbound : ∀ n : ℕ, ‖fQ09 n‖ ≤ 1 / ((n : ℝ) + 1) := by
    intro n
    have hn : (0 : ℝ) < (n : ℝ) + 1 := by positivity
    have hC : (0 : ℝ) ≤ 1 / ((n : ℝ) + 1) := by positivity
    rw [ContinuousMap.norm_le (fQ09 n) hC]
    intro x
    have hx0 : (0 : ℝ) ≤ (x : ℝ) := x.2.1
    have hx1 : (x : ℝ) ≤ 1 := x.2.2
    have hval : fQ09 n x = (x : ℝ) ^ n * (1 - (x : ℝ)) := rfl
    have hnn : 0 ≤ (x : ℝ) ^ n * (1 - (x : ℝ)) :=
      mul_nonneg (pow_nonneg hx0 n) (by linarith)
    rw [hval, Real.norm_eq_abs, abs_of_nonneg hnn, le_div_iff₀ hn]
    have := key_bound_Q09 n (x : ℝ) hx0 hx1
    linarith
  refine ⟨fun n => ?_, ?_⟩
  · rw [sub_zero]
    exact hbound n
  · exact squeeze_zero_norm hbound tendsto_one_div_add_atTop_nhds_zero_nat

#print axioms result
