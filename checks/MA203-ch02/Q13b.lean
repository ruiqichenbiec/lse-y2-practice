import Mathlib

/-!
Let $X=C[0,1]$, the vector space of continuous functions $f:[0,1]\to\mathbb{R}$ with pointwise operations, and consider the norms
$$\|f\|_\infty=\max_{x\in[0,1]}|f(x)|,\qquad\|f\|_1=\int_0^1|f(x)|\,dx .$$
Let $P=\{f\in X:\ f(x)>0\text{ for all }x\in[0,1]\}$ and $Q=\{f\in X:\ f(x)\ge0\text{ for all }x\in[0,1]\}$.

(b) Show that $P$ is open in $(X,\|\cdot\|_\infty)$.
-/

-- Lean choices: C[0,1] is C(Set.Icc (0:ℝ) 1, ℝ) with Mathlib's norm, which is the sup norm
-- for a compact domain (ContinuousMap.dist_apply_le_dist gives dist (g x) (f x) <= dist g f).
-- P is the set of f with 0 < f x for every point x of Set.Icc 0 1.
-- Proof: f attains a minimum f x0 > 0 on the compact interval (IsCompact.exists_isMinOn).
-- Every g with dist g f < f x0 satisfies g x > f x - f x0 >= 0 at every point x.

theorem result : IsOpen {f : C(Set.Icc (0:ℝ) 1, ℝ) | ∀ x : Set.Icc (0:ℝ) 1, 0 < f x} := by
  rw [Metric.isOpen_iff]
  intro f hf
  have hf' : ∀ x : Set.Icc (0:ℝ) 1, 0 < f x := hf
  have hne : (Set.univ : Set (Set.Icc (0:ℝ) 1)).Nonempty :=
    ⟨⟨0, by norm_num⟩, Set.mem_univ _⟩
  obtain ⟨x0, -, hx0⟩ := isCompact_univ.exists_isMinOn hne f.continuous.continuousOn
  refine ⟨f x0, hf' x0, fun g hg => ?_⟩
  have hg' : dist g f < f x0 := hg
  show ∀ x : Set.Icc (0:ℝ) 1, 0 < g x
  intro x
  have h1 : dist (g x) (f x) ≤ dist g f := ContinuousMap.dist_apply_le_dist x
  rw [Real.dist_eq] at h1
  have h2 : f x0 ≤ f x := isMinOn_iff.mp hx0 x (Set.mem_univ x)
  have h4 := (abs_le.mp h1).1
  linarith

#print axioms result
