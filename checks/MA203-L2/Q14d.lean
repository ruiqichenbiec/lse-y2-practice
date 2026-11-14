import Mathlib

/-!
Let $(X,d)$ be a metric space.

- (d) Prove or disprove: if $(a_n)_{n\in\mathbb{N}}$ is a sequence in $X$ with $d(a_n,a_{n+1})\le\frac1n$ for all $n\in\mathbb{N}$, then $(a_n)_{n\in\mathbb{N}}$ is a Cauchy sequence. **(4 marks)**

Statement relied on (definition, part (a)): $(a_n)_{n\in\mathbb{N}}$ is a Cauchy sequence if for every $\epsilon>0$ there exists $N\in\mathbb{N}$ such that $d(a_m,a_n)<\epsilon$ for all $m,n>N$.

Lean choices: the claim is that the statement is false, so the theorem states two things as a conjunction. First, the negation of the universal statement: it is not true that for every metric space X (in Type) and every sequence a : ℕ → X with d(a_n,a_{n+1}) <= 1/n for all n >= 1, the sequence a is Cauchy. Second, the counterexample named in the claim: in ℝ with the usual metric, the sequence n ↦ log n satisfies the hypothesis for all n >= 1 and is not Cauchy. The natural numbers are 1, 2, 3, ... as in the course, so the hypothesis is for n >= 1. Cauchy is Mathlib's CauchySeq.
-/

theorem result :
    (¬ ∀ (X : Type) [MetricSpace X] (a : ℕ → X),
        (∀ n : ℕ, 1 ≤ n → dist (a n) (a (n + 1)) ≤ 1 / (n : ℝ)) → CauchySeq a) ∧
      ((∀ n : ℕ, 1 ≤ n → dist (Real.log (n : ℝ)) (Real.log ((n + 1 : ℕ) : ℝ)) ≤ 1 / (n : ℝ)) ∧
        ¬ CauchySeq (fun n : ℕ => Real.log (n : ℝ))) := by
  have hyp : ∀ n : ℕ, 1 ≤ n →
      dist (Real.log (n : ℝ)) (Real.log ((n + 1 : ℕ) : ℝ)) ≤ 1 / (n : ℝ) := by
    intro n hn
    have hn' : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
    have hpos : (0 : ℝ) < (n : ℝ) := by linarith
    have hy0 : (n : ℝ) ≠ 0 := hpos.ne'
    have hx0 : (n : ℝ) + 1 ≠ 0 := by positivity
    have hcast : ((n + 1 : ℕ) : ℝ) = (n : ℝ) + 1 := Nat.cast_succ n
    have hlog : Real.log ((n + 1 : ℕ) : ℝ) - Real.log (n : ℝ)
        = Real.log (((n : ℝ) + 1) / (n : ℝ)) := by
      rw [Real.log_div hx0 hy0, hcast]
    have hbound : Real.log (((n : ℝ) + 1) / (n : ℝ)) ≤ ((n : ℝ) + 1) / (n : ℝ) - 1 :=
      Real.log_le_sub_one_of_pos (div_pos (by linarith) hpos)
    have hfrac : ((n : ℝ) + 1) / (n : ℝ) - 1 = 1 / (n : ℝ) := by
      rw [div_sub_one hy0]
      ring
    have hnonneg : 0 ≤ Real.log (((n : ℝ) + 1) / (n : ℝ)) := by
      apply Real.log_nonneg
      rw [le_div_iff₀ hpos]
      linarith
    have hdiff : 0 ≤ Real.log ((n + 1 : ℕ) : ℝ) - Real.log (n : ℝ) := by linarith
    rw [Real.dist_eq, abs_sub_comm, abs_of_nonneg hdiff]
    linarith
  have hnc : ¬ CauchySeq (fun n : ℕ => Real.log (n : ℝ)) := by
    intro hc
    obtain ⟨x, hx⟩ := cauchySeq_tendsto_of_complete hc
    have hlog : Filter.Tendsto (fun n : ℕ => Real.log (n : ℝ)) Filter.atTop Filter.atTop :=
      Real.tendsto_log_atTop.comp tendsto_natCast_atTop_atTop
    have h1 : ∀ᶠ n : ℕ in Filter.atTop, Real.log (n : ℝ) < x + 1 :=
      hx.eventually (gt_mem_nhds (lt_add_one x))
    have h2 : ∀ᶠ n : ℕ in Filter.atTop, x + 1 < Real.log (n : ℝ) :=
      hlog.eventually_gt_atTop (x + 1)
    obtain ⟨n, hn1, hn2⟩ := (h1.and h2).exists
    linarith
  exact ⟨fun hall => hnc (hall ℝ (fun n : ℕ => Real.log (n : ℝ)) hyp), hyp, hnc⟩

#print axioms result
