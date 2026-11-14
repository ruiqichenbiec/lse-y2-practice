import Mathlib

/-!
Work in $(\mathbb{R},|\cdot|)$.

- (a) Show that $F=(-\infty,-2]\cup[3,\infty)$ is closed, and that it is not open.

Statement relied on (closed set): In a metric space $(X,d)$: $F\subset X$ is closed if $X\setminus F$ is open.

Statement relied on (open set): In a metric space $(X,d)$: $U\subset X$ is open if for every $x\in U$ there exists $r>0$ with $B(x,r)\subset U$. Negation: $U$ is not open if there is an $x\in U$ such that for every $r>0$ some point of $B(x,r)$ is not in $U$.

Statement relied on (open ball): Let $(X,d)$ be a metric space, $x\in X$ and $r>0$. The open ball with centre $x$ and radius $r$ is $B(x,r)=\{y\in X:\ d(y,x)<r\}$ (strict inequality). In $(\mathbb{R},|\cdot|)$ it is the interval $(x-r,\,x+r)$.
-/

theorem result : IsClosed (Set.Iic (-2:ℝ) ∪ Set.Ici (3:ℝ)) := by
  exact IsClosed.union isClosed_Iic isClosed_Ici

#print axioms result
