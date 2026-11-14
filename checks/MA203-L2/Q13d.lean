import Mathlib

/-!
Let $X=C[0,1]$, the vector space of continuous functions $f:[0,1]\to\mathbb{R}$ with pointwise operations, and consider the norms
$$\|f\|_\infty=\max_{x\in[0,1]}|f(x)|,\qquad\|f\|_1=\int_0^1|f(x)|\,dx .$$
Let $P=\{f\in X:\ f(x)>0\text{ for all }x\in[0,1]\}$ and $Q=\{f\in X:\ f(x)\ge0\text{ for all }x\in[0,1]\}$.

(d) Show that $Q$ is closed in $(X,\|\cdot\|_\infty)$.
-/

-- Lean choices: C[0,1] is C(Set.Icc (0:ℝ) 1, ℝ) with Mathlib's norm, which is the sup norm
-- for a compact domain, so IsClosed refers to the sup-norm topology.
-- Q is the intersection over the points x of [0,1] of the sets {f | 0 <= f x}. Each of these is
-- closed, because evaluation at x is continuous for the compact-open (sup-norm) topology and the
-- constant 0 is continuous.

theorem result : IsClosed {f : C(Set.Icc (0:ℝ) 1, ℝ) | ∀ x : Set.Icc (0:ℝ) 1, 0 ≤ f x} := by
  have h : {f : C(Set.Icc (0:ℝ) 1, ℝ) | ∀ x : Set.Icc (0:ℝ) 1, 0 ≤ f x} =
      ⋂ x : Set.Icc (0:ℝ) 1, {f : C(Set.Icc (0:ℝ) 1, ℝ) | 0 ≤ f x} := by
    ext f
    simp
  rw [h]
  exact isClosed_iInter fun x => isClosed_le continuous_const (continuous_eval_const x)

#print axioms result
