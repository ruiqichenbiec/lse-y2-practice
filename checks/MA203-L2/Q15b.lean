import Mathlib

/-!
Equip $\mathbb{R}$ with $|\cdot|$ and $\mathbb{R}^2$ with the Euclidean norm $\|\cdot\|_2$. For $A,B\subset\mathbb{R}$ write $A\times B=\{(x,y)\in\mathbb{R}^2:\ x\in A,\ y\in B\}$.

- (b) Let $U,V\subset\mathbb{R}$ be open. Show that $U\times V$ is open in $\mathbb{R}^2$. **(5 marks)**
-/

theorem result (U V : Set ℝ) (hU : IsOpen U) (hV : IsOpen V) :
    IsOpen {p : EuclideanSpace ℝ (Fin 2) | p 0 ∈ U ∧ p 1 ∈ V} := by
  have h0 : Continuous (fun p : EuclideanSpace ℝ (Fin 2) => p 0) :=
    PiLp.continuous_apply 2 _ 0
  have h1 : Continuous (fun p : EuclideanSpace ℝ (Fin 2) => p 1) :=
    PiLp.continuous_apply 2 _ 1
  have hc : Continuous (fun p : EuclideanSpace ℝ (Fin 2) => (p 0, p 1)) :=
    h0.prodMk h1
  have hset : {p : EuclideanSpace ℝ (Fin 2) | p 0 ∈ U ∧ p 1 ∈ V}
      = (fun p : EuclideanSpace ℝ (Fin 2) => (p 0, p 1)) ⁻¹' (U ×ˢ V) := by
    ext p
    simp [Set.mem_prod]
  rw [hset]
  exact (hU.prod hV).preimage hc

#print axioms result
