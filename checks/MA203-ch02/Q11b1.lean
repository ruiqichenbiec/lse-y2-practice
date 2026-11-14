import Mathlib

/-!
**Two model examples.** $(\frac1n)$ is Cauchy: given $\epsilon>0$ take $N>\frac2\epsilon$ and use $|\frac1n-\frac1m|\le\frac1n+\frac1m<\frac2N$. $(\sqrt n)$ is not Cauchy, although $\sqrt{n+1}-\sqrt n\to0$: for $\epsilon=1$ and any $N$, the terms with $n=(N+3)^2$ and $m=(N+1)^2$ are 2 apart. **Method:** to prove Cauchy, bound $|a_m-a_n|$ by an expression in $\min\{m,n\}$ that tends to 0, then choose $N$; to disprove it, use the negation $\exists\epsilon>0\ \forall N\ \exists m,n>N:\ |a_m-a_n|\ge\epsilon$ and exhibit $m,n$.

- (b) Let $h_n=\sum_{k=1}^n\frac1k$. Show that $h_{n+1}-h_n\to0$, but that $(h_n)_{n\in\mathbb{N}}$ is not a Cauchy sequence.
-/

-- h_n is the sum over k from 1 to n of 1/k. Claim: h_{n+1} - h_n tends to 0 as n runs over N.
theorem result :
    Filter.Tendsto (fun n : ℕ => (∑ k ∈ Finset.Icc 1 (n + 1), (1 : ℝ) / (k : ℝ))
      - ∑ k ∈ Finset.Icc 1 n, (1 : ℝ) / (k : ℝ)) Filter.atTop (nhds 0) := by
  have hdiff : (fun n : ℕ => (∑ k ∈ Finset.Icc 1 (n + 1), (1 : ℝ) / (k : ℝ))
      - ∑ k ∈ Finset.Icc 1 n, (1 : ℝ) / (k : ℝ)) = fun n : ℕ => 1 / ((n : ℝ) + 1) := by
    funext n
    rw [Finset.sum_Icc_succ_top (by omega : 1 ≤ n + 1), Nat.cast_add, Nat.cast_one]
    ring
  rw [hdiff]
  exact tendsto_one_div_add_atTop_nhds_zero_nat

#print axioms result
