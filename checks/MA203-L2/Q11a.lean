import Mathlib

/-!
**Two model examples.** $(\frac1n)$ is Cauchy: given $\epsilon>0$ take $N>\frac2\epsilon$ and use $|\frac1n-\frac1m|\le\frac1n+\frac1m<\frac2N$. $(\sqrt n)$ is not Cauchy, although $\sqrt{n+1}-\sqrt n\to0$: for $\epsilon=1$ and any $N$, the terms with $n=(N+3)^2$ and $m=(N+1)^2$ are 2 apart. **Method:** to prove Cauchy, bound $|a_m-a_n|$ by an expression in $\min\{m,n\}$ that tends to 0, then choose $N$; to disprove it, use the negation $\exists\epsilon>0\ \forall N\ \exists m,n>N:\ |a_m-a_n|\ge\epsilon$ and exhibit $m,n$.

- (a) Let $s_n=\sum_{k=1}^n\frac1{k^2}$. Using $\frac1{k^2}\le\frac1{k-1}-\frac1k$ for $k\ge2$, prove that $(s_n)_{n\in\mathbb{N}}$ is a Cauchy sequence.
-/

-- s_n is the sum over k from 1 to n of 1/k^2, indexed by n in N; Cauchy means CauchySeq for the usual metric on R.
theorem result : CauchySeq (fun n : ℕ => ∑ k ∈ Finset.Icc 1 n, (1 : ℝ) / (k : ℝ) ^ 2) := by
  have hsum : Summable (fun k : ℕ => (1 : ℝ) / (k : ℝ) ^ 2) :=
    (Real.summable_one_div_nat_pow (p := 2)).mpr (by norm_num)
  have key : ∀ n : ℕ, ∑ k ∈ Finset.Icc 1 n, (1 : ℝ) / (k : ℝ) ^ 2
      = ∑ k ∈ Finset.range (n + 1), (1 : ℝ) / (k : ℝ) ^ 2 := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
      rw [Finset.sum_Icc_succ_top (by omega : 1 ≤ n + 1), ih, Finset.sum_range_succ _ (n + 1)]
  have hfun : (fun n : ℕ => ∑ k ∈ Finset.Icc 1 n, (1 : ℝ) / (k : ℝ) ^ 2)
      = fun n : ℕ => ∑ k ∈ Finset.range (n + 1), (1 : ℝ) / (k : ℝ) ^ 2 := funext key
  have hcs : CauchySeq (fun n : ℕ => ∑ k ∈ Finset.range (n + 1), (1 : ℝ) / (k : ℝ) ^ 2) :=
    ((hsum.tendsto_sum_tsum_nat).comp (Filter.tendsto_add_atTop_nat 1)).cauchySeq
  rw [hfun]
  exact hcs

#print axioms result
