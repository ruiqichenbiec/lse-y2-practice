import Mathlib

/-!
**Lemma (arbitrary unions of open sets are open).** Let $U_i$ ($i\in I$) be any family of open sets in a metric space $(X,d)$, indexed by an arbitrary set $I$. Then $\bigcup_{i\in I}U_i$ is open.

Let $(X,d)$ be a metric space.

- (a) Prove the lemma above (arbitrary unions of open sets are open).
-/

theorem result {X : Type*} [MetricSpace X] {I : Type*} (U : I → Set X) (hU : ∀ i, IsOpen (U i)) :
    IsOpen (⋃ i, U i) := by
  rw [Metric.isOpen_iff]
  intro x hx
  obtain ⟨i, hi⟩ := Set.mem_iUnion.mp hx
  obtain ⟨r, hr, hball⟩ := Metric.isOpen_iff.mp (hU i) x hi
  exact ⟨r, hr, hball.trans (Set.subset_iUnion U i)⟩

#print axioms result
