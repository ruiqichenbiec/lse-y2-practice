import Mathlib

/-!
Work in $(\mathbb{R},|\cdot|)$, where $B(x,r)=(x-r,\,x+r)$.

- (b) Show that $V=(-1,4]$ is not open: name a point $x\in V$ where openness fails and, for an arbitrary $r>0$, give an explicit point of $B(x,r)$ that is not in $V$.

Statement relied on (open set): In a metric space $(X,d)$: $U\subset X$ is open if for every $x\in U$ there exists $r>0$ with $B(x,r)\subset U$. Negation: $U$ is not open if there is an $x\in U$ such that for every $r>0$ some point of $B(x,r)$ is not in $U$.

Statement relied on (open ball): Let $(X,d)$ be a metric space, $x\in X$ and $r>0$. The open ball with centre $x$ and radius $r$ is $B(x,r)=\{y\in X:\ d(y,x)<r\}$ (strict inequality). In $(\mathbb{R},|\cdot|)$ it is the interval $(x-r,\,x+r)$.
-/

theorem result : ¬ IsOpen (Set.Ioc (-1:ℝ) 4) := by
  intro h
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp h 4 ⟨by norm_num, le_refl (4:ℝ)⟩
  have hmem : (4 + ε / 2 : ℝ) ∈ Metric.ball (4:ℝ) ε := by
    rw [Metric.mem_ball, Real.dist_eq, abs_lt]
    constructor <;> linarith
  obtain ⟨_, h3⟩ := hball hmem
  linarith

#print axioms result
