import Mathlib

/-!
Problem Q2.12, part (b), with the sub-parts (i) and (ii) that concern this item.

- (b) Let $U=\{(x,y)\in\mathbb{R}^2:\ y>x^2\}$, let $(a,b)\in U$ and put $\delta=b-a^2>0$.
  - (i) Show that if $0<r\le1$ and $(x,y)\in\mathbb{R}^2$ satisfies $|x-a|<r$ and $|y-b|<r$, then $y-x^2>\delta-(2|a|+2)r$.
  - (ii) Deduce that $U$ is open.

This file proves the claim that the set U is open in the Euclidean plane. The point (x,y) of R^2 is the vector p of EuclideanSpace over the reals indexed by Fin 2, with x = p 0 and y = p 1, and the topology is the one of the Euclidean norm. The proof uses that the map p to p 0 squared and the map p to p 1 are continuous, so U is a strict sublevel set of two continuous functions.
-/

theorem result : IsOpen {p : EuclideanSpace ℝ (Fin 2) | p 1 > (p 0) ^ 2} := by
  have hf : Continuous fun p : EuclideanSpace ℝ (Fin 2) => (p 0) ^ 2 := by fun_prop
  have hg : Continuous fun p : EuclideanSpace ℝ (Fin 2) => p 1 := by fun_prop
  exact isOpen_lt hf hg

#print axioms result
