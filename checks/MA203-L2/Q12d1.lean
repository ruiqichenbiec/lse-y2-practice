import Mathlib

/-!
Problem MA203-L2-112, part (d), copied from the prompt. This file proves the first claim of (d), that the parabola is closed.

- (d) Show that the parabola $P=\{(x,y)\in\mathbb{R}^2:\ y=x^2\}$ is closed, but not open.

This file proves the claim that P is closed in the Euclidean plane. The point (x,y) of R^2 is the vector p of EuclideanSpace over the reals indexed by Fin 2, with x = p 0 and y = p 1. The proof uses that the two maps p to p 1 and p to p 0 squared are continuous, so P is the zero set of their difference, and a set where two continuous functions agree is closed.
-/

theorem result : IsClosed {p : EuclideanSpace ℝ (Fin 2) | p 1 = (p 0) ^ 2} := by
  have hf : Continuous fun p : EuclideanSpace ℝ (Fin 2) => p 1 := by fun_prop
  have hg : Continuous fun p : EuclideanSpace ℝ (Fin 2) => (p 0) ^ 2 := by fun_prop
  exact isClosed_eq hf hg

#print axioms result
