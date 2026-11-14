import Mathlib

/-!
Equip $\mathbb{R}$ with $|\cdot|$ and $\mathbb{R}^2$ with the Euclidean norm $\|\cdot\|_2$. For $A,B\subset\mathbb{R}$ write $A\times B=\{(x,y)\in\mathbb{R}^2:\ x\in A,\ y\in B\}$.

- (c) Let $F,G\subset\mathbb{R}$ be closed. Show that $F\times G$ is closed in $\mathbb{R}^2$. *Hint: write $\mathbb{R}^2\setminus(F\times G)$ using sets of the form $A\times\mathbb{R}$ and $\mathbb{R}\times B$.* **(4 marks)**
-/

theorem result (F G : Set ℝ) (hF : IsClosed F) (hG : IsClosed G) :
    IsClosed {p : EuclideanSpace ℝ (Fin 2) | p 0 ∈ F ∧ p 1 ∈ G} := by
  have h0 : Continuous (fun p : EuclideanSpace ℝ (Fin 2) => p 0) :=
    PiLp.continuous_apply 2 _ 0
  have h1 : Continuous (fun p : EuclideanSpace ℝ (Fin 2) => p 1) :=
    PiLp.continuous_apply 2 _ 1
  have hc : Continuous (fun p : EuclideanSpace ℝ (Fin 2) => (p 0, p 1)) :=
    h0.prodMk h1
  have hset : {p : EuclideanSpace ℝ (Fin 2) | p 0 ∈ F ∧ p 1 ∈ G}
      = (fun p : EuclideanSpace ℝ (Fin 2) => (p 0, p 1)) ⁻¹' (F ×ˢ G) := by
    ext p
    simp [Set.mem_prod]
  rw [hset]
  exact (hF.prod hG).preimage hc

#print axioms result
