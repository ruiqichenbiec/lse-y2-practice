import Mathlib

/-!
Work in $(\mathbb{R},|\cdot|)$.

- (b) Show that $G=[0,5)$ is neither open nor closed.

Statement relied on (closed set): In a metric space $(X,d)$: $F\subset X$ is closed if $X\setminus F$ is open.

Statement relied on (open set): In a metric space $(X,d)$: $U\subset X$ is open if for every $x\in U$ there exists $r>0$ with $B(x,r)\subset U$. Negation: $U$ is not open if there is an $x\in U$ such that for every $r>0$ some point of $B(x,r)$ is not in $U$.

Statement relied on (open ball): Let $(X,d)$ be a metric space, $x\in X$ and $r>0$. The open ball with centre $x$ and radius $r$ is $B(x,r)=\{y\in X:\ d(y,x)<r\}$ (strict inequality). In $(\mathbb{R},|\cdot|)$ it is the interval $(x-r,\,x+r)$.
-/

theorem result : ¬ IsClosed (Set.Ico (0:ℝ) 5) := by
  intro hclosed
  have hopen : IsOpen (Set.Ico (0:ℝ) 5)ᶜ := isOpen_compl_iff.mpr hclosed
  have h5 : (5:ℝ) ∉ Set.Ico (0:ℝ) 5 := fun h => lt_irrefl (5:ℝ) (Set.mem_Ico.mp h).2
  obtain ⟨r, hr, hball⟩ := Metric.isOpen_iff.mp hopen 5 (Set.mem_compl h5)
  have hm : 0 < min r 5 := lt_min hr (by norm_num)
  have hm5 : min r 5 ≤ 5 := min_le_right r 5
  have hmr : min r 5 ≤ r := min_le_left r 5
  have hmem : (5 - min r 5 / 2 : ℝ) ∈ Metric.ball (5:ℝ) r := by
    rw [Metric.mem_ball, Real.dist_eq, abs_lt]
    constructor <;> linarith
  have hp : (5 - min r 5 / 2 : ℝ) ∈ Set.Ico (0:ℝ) 5 := by
    rw [Set.mem_Ico]
    constructor <;> linarith
  exact hball hmem hp

#print axioms result
