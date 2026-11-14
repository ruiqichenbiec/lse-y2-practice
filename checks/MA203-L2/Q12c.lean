import Mathlib

/-!
Problem MA203-L2-112, part (c), copied from the prompt.

- (c) Show that $V=\{(x,y)\in\mathbb{R}^2:\ y<x^2\}$ is open. (You may adapt the argument of (b), stating the modified estimate and the radius you use.)

This file proves the claim that the set V is open in the Euclidean plane. The point (x,y) of R^2 is the vector p of EuclideanSpace over the reals indexed by Fin 2, with x = p 0 and y = p 1, and the topology is the one of the Euclidean norm. The proof uses that the map p to p 1 and the map p to p 0 squared are continuous, so V is a strict sublevel set of two continuous functions.
-/

theorem result : IsOpen {p : EuclideanSpace ℝ (Fin 2) | p 1 < (p 0) ^ 2} := by
  have hf : Continuous fun p : EuclideanSpace ℝ (Fin 2) => (p 0) ^ 2 := by fun_prop
  have hg : Continuous fun p : EuclideanSpace ℝ (Fin 2) => p 1 := by fun_prop
  exact isOpen_lt hg hf

#print axioms result
