import Mathlib

/-!
Work in $(\mathbb{R},|\cdot|)$.

- (b) Let $b_n=(-1)^n\big(1+\frac1n\big)$. Show that $\epsilon=1$ has no such $N$: for every $N$, give $m,n>N$ with $|b_m-b_n|\ge1$.

Statement relied on (Cauchy sequence): $(a_n)$ in $(X,d)$ is Cauchy if $\forall\epsilon>0\ \exists N\in\mathbb{N}\ \forall m,n>N:\ d(a_m,a_n)<\epsilon$. In $\mathbb{R}$: $|a_m-a_n|<\epsilon$.
-/

noncomputable def bQ10b (n : ℕ) : ℝ := (-1 : ℝ) ^ n * (1 + 1 / (n : ℝ))

theorem result : (∀ N : ℕ, N < N + 1 ∧ N < N + 2 ∧ 2 < |bQ10b (N + 2) - bQ10b (N + 1)|) ∧
    ¬ ∃ N : ℕ, ∀ m n : ℕ, N < m → N < n → |bQ10b m - bQ10b n| < 1 := by
  have key : ∀ N : ℕ, 2 < |bQ10b (N + 2) - bQ10b (N + 1)| := by
    intro N
    have hsplit : bQ10b (N + 2) - bQ10b (N + 1)
        = (-1 : ℝ) ^ N * (2 + 1 / ((N : ℝ) + 2) + 1 / ((N : ℝ) + 1)) := by
      unfold bQ10b
      push_cast
      ring
    have hs : |(-1 : ℝ) ^ N| = 1 := by simp
    have h1 : 0 < 1 / ((N : ℝ) + 2) := by positivity
    have h2 : 0 < 1 / ((N : ℝ) + 1) := by positivity
    have hpos : 0 < 2 + 1 / ((N : ℝ) + 2) + 1 / ((N : ℝ) + 1) := by linarith
    rw [hsplit, abs_mul, hs, one_mul, abs_of_pos hpos]
    linarith
  refine ⟨fun N => ⟨by omega, by omega, key N⟩, ?_⟩
  rintro ⟨N, hN⟩
  have h1 := hN (N + 2) (N + 1) (by omega) (by omega)
  have h2 := key N
  linarith

#print axioms result
