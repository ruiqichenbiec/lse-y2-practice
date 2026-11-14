import Mathlib

/-!
**Lemma (finite intersections of open sets are open).** If $U_1,\dots,U_n$ are open in a metric space $(X,d)$, then $U_1\cap\dots\cap U_n$ is open. The word "finite" cannot be dropped (part (b) below gives a counterexample).

- (a) Prove the lemma above directly for $n$ sets, without induction: for $x\in U_1\cap\dots\cap U_n$, construct one radius that works for all $n$ sets at once.
-/

theorem result {X : Type*} [MetricSpace X] (n : ℕ) (hn : 1 ≤ n) (U : Fin n → Set X)
    (hU : ∀ i, IsOpen (U i)) : IsOpen (⋂ i, U i) := by
  rw [Metric.isOpen_iff]
  intro x hx
  -- each U k supplies its own radius at x
  have hr : ∀ k : Fin n, ∃ r > 0, Metric.ball x r ⊆ U k := fun k =>
    Metric.isOpen_iff.mp (hU k) x (Set.mem_iInter.mp hx k)
  choose r hrpos hball using hr
  -- the minimum of finitely many radii is one of them, hence positive
  have hne : (Finset.univ : Finset (Fin n)).Nonempty := ⟨⟨0, by omega⟩, Finset.mem_univ _⟩
  obtain ⟨j, -, hj⟩ := Finset.exists_min_image Finset.univ r hne
  refine ⟨r j, hrpos j, ?_⟩
  intro z hz
  refine Set.mem_iInter.mpr (fun k => ?_)
  exact hball k (Metric.ball_subset_ball (hj k (Finset.mem_univ k)) hz)

#print axioms result
