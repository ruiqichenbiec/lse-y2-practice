import Mathlib

/-!
Let $(X,d)$ be a metric space.

- (c) Prove or disprove: if $(a_n)_{n\in\mathbb{N}}$ is a sequence in $X$ with $d(a_n,a_{n+1})\le2^{-n}$ for all $n\in\mathbb{N}$, then $(a_n)_{n\in\mathbb{N}}$ is a Cauchy sequence. **(4 marks)**

Statement relied on (definition, part (a)): $(a_n)_{n\in\mathbb{N}}$ is a Cauchy sequence if for every $\epsilon>0$ there exists $N\in\mathbb{N}$ such that $d(a_m,a_n)<\epsilon$ for all $m,n>N$.

Lean choices: X is an arbitrary type with a MetricSpace instance, so dist is d. The natural numbers are 1, 2, 3, ... as in the course, so the hypothesis is required only for n >= 1. This is the stronger statement, since it implies the version with the hypothesis for every n. The bound 2^(-n) is written (2:ℝ) ^ (-(n:ℤ)). Cauchy is Mathlib's CauchySeq.
-/

theorem result (X : Type*) [MetricSpace X] (a : ℕ → X)
    (h : ∀ n : ℕ, 1 ≤ n → dist (a n) (a (n + 1)) ≤ (2 : ℝ) ^ (-(n : ℤ))) :
    CauchySeq a := by
  have hb : ∀ k : ℕ, dist (a (k + 1)) (a (k + 1 + 1)) ≤ 1 / 2 / 2 ^ k := by
    intro k
    have h1 := h (k + 1) (by omega)
    have e : (2 : ℝ) ^ (-((k + 1 : ℕ) : ℤ)) = 1 / 2 / 2 ^ k := by
      rw [zpow_neg, zpow_natCast]
      ring1
    rw [e] at h1
    exact h1
  have hc : CauchySeq (fun n : ℕ => a (n + 1)) :=
    cauchySeq_of_le_geometric_two (C := 1) hb
  exact (cauchySeq_shift (u := a) 1).mp hc

#print axioms result
