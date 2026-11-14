import Mathlib

/-!
Work in $(\mathbb{R},|\cdot|)$, where $B(x,r)=(x-r,\,x+r)$.

- (a) Let $U=(-1,4)$. For each of the points $x=0$, $x=3.5$ and $x=3.99$, give a radius $r>0$ with $B(x,r)\subset U$ and write $B(x,r)$ as an interval. Then give a formula for such an $r$ that works for every $x\in U$.

Statement relied on (open set): In a metric space $(X,d)$: $U\subset X$ is open if for every $x\in U$ there exists $r>0$ with $B(x,r)\subset U$. Negation: $U$ is not open if there is an $x\in U$ such that for every $r>0$ some point of $B(x,r)$ is not in $U$.

Statement relied on (open ball): Let $(X,d)$ be a metric space, $x\in X$ and $r>0$. The open ball with centre $x$ and radius $r$ is $B(x,r)=\{y\in X:\ d(y,x)<r\}$ (strict inequality). In $(\mathbb{R},|\cdot|)$ it is the interval $(x-r,\,x+r)$.
-/

theorem result : ∀ x ∈ Set.Ioo (-1:ℝ) 4,
    0 < min (x + 1) (4 - x) ∧ Metric.ball x (min (x + 1) (4 - x)) ⊆ Set.Ioo (-1:ℝ) 4 := by
  intro x hx
  rcases hx with ⟨hx1, hx4⟩
  have hL : min (x + 1) (4 - x) ≤ x + 1 := min_le_left _ _
  have hR : min (x + 1) (4 - x) ≤ 4 - x := min_le_right _ _
  refine ⟨lt_min (by linarith) (by linarith), ?_⟩
  intro y hy
  rw [Metric.mem_ball, Real.dist_eq, abs_lt] at hy
  rcases hy with ⟨hy1, hy2⟩
  exact ⟨by linarith, by linarith⟩

#print axioms result
