import Mathlib

/-!
Work in $(\mathbb{R},|\cdot|)$.

- (a) Show that $F=(-\infty,-2]\cup[3,\infty)$ is closed, and that it is not open.

Statement relied on (closed set): In a metric space $(X,d)$: $F\subset X$ is closed if $X\setminus F$ is open.

Statement relied on (open set): In a metric space $(X,d)$: $U\subset X$ is open if for every $x\in U$ there exists $r>0$ with $B(x,r)\subset U$. Negation: $U$ is not open if there is an $x\in U$ such that for every $r>0$ some point of $B(x,r)$ is not in $U$.

Statement relied on (open ball): Let $(X,d)$ be a metric space, $x\in X$ and $r>0$. The open ball with centre $x$ and radius $r$ is $B(x,r)=\{y\in X:\ d(y,x)<r\}$ (strict inequality). In $(\mathbb{R},|\cdot|)$ it is the interval $(x-r,\,x+r)$.
-/

theorem result : ¬ IsOpen (Set.Iic (-2:ℝ) ∪ Set.Ici (3:ℝ)) := by
  intro hopen
  have h3 : (3:ℝ) ∈ Set.Iic (-2:ℝ) ∪ Set.Ici (3:ℝ) :=
    Set.mem_union_right (Set.Iic (-2:ℝ)) (Set.mem_Ici.mpr le_rfl)
  obtain ⟨r, hr, hball⟩ := Metric.isOpen_iff.mp hopen 3 h3
  have hm : 0 < min r 5 := lt_min hr (by norm_num)
  have hm5 : min r 5 ≤ 5 := min_le_right r 5
  have hmr : min r 5 ≤ r := min_le_left r 5
  have hmem : (3 - min r 5 / 2 : ℝ) ∈ Metric.ball (3:ℝ) r := by
    rw [Metric.mem_ball, Real.dist_eq, abs_lt]
    constructor <;> linarith
  rcases hball hmem with h | h
  · linarith [Set.mem_Iic.mp h]
  · linarith [Set.mem_Ici.mp h]

#print axioms result
