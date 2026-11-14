import Mathlib

/-!
Problem Q2.7, part (b), copied from the prompt:

- (b) In $(\mathbb{R}^2,\|\cdot\|_2)$, use (a) and results stated in this unit, including closed balls are closed [appendix], to show that the crescent $K=\{p\in\mathbb{R}^2:\ \|p\|_2\le2\ \text{and}\ \|p-(1,0)\|_2\ge1\}$ is closed. Is $K$ open?

Recall entry the part refers to (closed balls are closed [appendix]):

Let $(X,d)$ be a metric space, $x\in X$ and $r>0$. The closed ball $\overline{B(x,r)}:=\{y\in X:\ d(y,x)\le r\}$ is a closed set. (If $d(z,x)>r$, then by the triangle inequality the open ball $B\big(z,\,d(z,x)-r\big)$ contains no point of $\overline{B(x,r)}$, so the complement is open.) Here the overline is only a name for this set, the closed ball; it carries no other meaning in this unit.

This file proves the first claim only: the crescent $K$ is closed in the Euclidean plane. The plane is EuclideanSpace over the reals indexed by Fin 2, whose norm is the Euclidean norm $\|\cdot\|_2$, and the point $(1,0)$ is written with the notation for vectors of EuclideanSpace. The set $K$ is written in full as the intersection of the two conditions $\|p\|_2\le2$ and $\|p-(1,0)\|_2\ge1$. The proof uses that each condition defines a closed set, since the norm is continuous.
-/

theorem result :
    IsClosed {p : EuclideanSpace ℝ (Fin 2) |
      ‖p‖ ≤ 2 ∧ 1 ≤ ‖p - (!₂[1, 0] : EuclideanSpace ℝ (Fin 2))‖} := by
  rw [Set.ofPred_and]
  refine IsClosed.inter ?_ ?_
  · exact isClosed_le continuous_norm continuous_const
  · exact isClosed_le continuous_const (by fun_prop)

#print axioms result
