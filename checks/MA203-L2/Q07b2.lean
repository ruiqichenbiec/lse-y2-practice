import Mathlib

/-!
Problem MA203-L2-107, part (b), copied from the prompt:

- (b) In $(\mathbb{R}^2,\|\cdot\|_2)$, use (a) and results stated in this unit, including closed balls are closed [appendix], to show that the crescent $K=\{p\in\mathbb{R}^2:\ \|p\|_2\le2\ \text{and}\ \|p-(1,0)\|_2\ge1\}$ is closed. Is $K$ open?

Definition the claim uses (the open-set entry of the unit): In a metric space $(X,d)$: $U\subset X$ is open if for every $x\in U$ there exists $r>0$ with $B(x,r)\subset U$. Negation: $U$ is not open if there is an $x\in U$ such that for every $r>0$ some point of $B(x,r)$ is not in $U$.

This file proves the second claim only: the crescent $K$ is not open in the Euclidean plane. The witness is the point $(2,0)$, which lies in $K$ because $\|(2,0)\|_2=2\le2$ and $\|(2,0)-(1,0)\|_2=1\ge1$; for every $r>0$ the point $(2+r/2,0)$ lies in $B((2,0),r)$ but not in $K$, because its norm $2+r/2$ is larger than $2$. The statement is that the set $K$ is not open (the negation of IsOpen), and the witness is the proof.

The Euclidean plane is EuclideanSpace over the reals indexed by Fin 2, whose norm is the Euclidean norm. The points $(a,0)$ and $(1,0)$ are written with the vector notation of EuclideanSpace.
-/

theorem q07b2_norm_pair (a : ℝ) :
    ‖(!₂[a, 0] : EuclideanSpace ℝ (Fin 2))‖ = |a| := by
  simp [EuclideanSpace.norm_eq, Fin.sum_univ_two, Real.sqrt_sq_eq_abs]

theorem q07b2_sub_pair (a b : ℝ) :
    ‖(!₂[a, 0] : EuclideanSpace ℝ (Fin 2)) - (!₂[b, 0] : EuclideanSpace ℝ (Fin 2))‖ = |a - b| := by
  simp [EuclideanSpace.norm_eq, Fin.sum_univ_two, Real.sqrt_sq_eq_abs]

theorem result :
    ¬ IsOpen {p : EuclideanSpace ℝ (Fin 2) |
      ‖p‖ ≤ 2 ∧ 1 ≤ ‖p - (!₂[1, 0] : EuclideanSpace ℝ (Fin 2))‖} := by
  intro hopen
  have hmem : (!₂[2, 0] : EuclideanSpace ℝ (Fin 2)) ∈
      {p : EuclideanSpace ℝ (Fin 2) | ‖p‖ ≤ 2 ∧ 1 ≤ ‖p - (!₂[1, 0] : EuclideanSpace ℝ (Fin 2))‖} := by
    show ‖(!₂[2, 0] : EuclideanSpace ℝ (Fin 2))‖ ≤ 2 ∧
      1 ≤ ‖(!₂[2, 0] : EuclideanSpace ℝ (Fin 2)) - (!₂[1, 0] : EuclideanSpace ℝ (Fin 2))‖
    rw [q07b2_norm_pair, q07b2_sub_pair]
    norm_num
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp hopen _ hmem
  have hq : (!₂[2 + ε / 2, 0] : EuclideanSpace ℝ (Fin 2)) ∈
      Metric.ball (!₂[2, 0] : EuclideanSpace ℝ (Fin 2)) ε := by
    rw [Metric.mem_ball, dist_eq_norm, q07b2_sub_pair, abs_lt]
    constructor <;> linarith
  have hK : ‖(!₂[2 + ε / 2, 0] : EuclideanSpace ℝ (Fin 2))‖ ≤ 2 ∧
      1 ≤ ‖(!₂[2 + ε / 2, 0] : EuclideanSpace ℝ (Fin 2)) - (!₂[1, 0] : EuclideanSpace ℝ (Fin 2))‖ :=
    hball hq
  have hpos : (0 : ℝ) < 2 + ε / 2 := by linarith
  have h1 : ‖(!₂[2 + ε / 2, 0] : EuclideanSpace ℝ (Fin 2))‖ ≤ 2 := hK.1
  rw [q07b2_norm_pair, abs_of_pos hpos] at h1
  linarith

#print axioms result
