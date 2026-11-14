import Mathlib

/-!
Work in $(\mathbb{R},|\cdot|)$.

- (b) Show that $G=[0,5)$ is neither open nor closed.

Statement relied on (closed set): In a metric space $(X,d)$: $F\subset X$ is closed if $X\setminus F$ is open.

Statement relied on (open set): In a metric space $(X,d)$: $U\subset X$ is open if for every $x\in U$ there exists $r>0$ with $B(x,r)\subset U$. Negation: $U$ is not open if there is an $x\in U$ such that for every $r>0$ some point of $B(x,r)$ is not in $U$.

Statement relied on (open ball): Let $(X,d)$ be a metric space, $x\in X$ and $r>0$. The open ball with centre $x$ and radius $r$ is $B(x,r)=\{y\in X:\ d(y,x)<r\}$ (strict inequality). In $(\mathbb{R},|\cdot|)$ it is the interval $(x-r,\,x+r)$.
-/

theorem result : ¬ IsOpen (Set.Ico (0:ℝ) 5) := by
  intro hopen
  have h0 : (0:ℝ) ∈ Set.Ico (0:ℝ) 5 := Set.mem_Ico.mpr ⟨le_refl (0:ℝ), by norm_num⟩
  obtain ⟨r, hr, hball⟩ := Metric.isOpen_iff.mp hopen 0 h0
  have hmem : (-(r / 2) : ℝ) ∈ Metric.ball (0:ℝ) r := by
    rw [Metric.mem_ball, Real.dist_eq, abs_lt]
    constructor <;> linarith
  linarith [(Set.mem_Ico.mp (hball hmem)).1]

#print axioms result
