import Mathlib

/-!
Problem MA203-L2-107, part (a), copied from the prompt:

Let $(X,d)$ be a metric space, $U\subset X$ open and $F\subset X$ closed.

- (a) Prove that $U\setminus F$ is open and that $F\setminus U$ is closed.

Statement the problem relies on (the statement field of MA203-L2-107):

**Corollaries (finite unions and arbitrary intersections of closed sets).** In a metric space, a finite union of closed sets is closed, and an arbitrary intersection of closed sets is closed. **Method:** pass to complements with De Morgan's laws, which turn unions into intersections and vice versa, and then use the properties of open sets (finite intersections of open sets are open [item 105]; arbitrary unions of open sets are open [item 103]).

This file proves the first conclusion only: if $U$ is open and $F$ is closed, then $U\setminus F$ is open. The metric space is an arbitrary type $X$ with a MetricSpace instance; IsOpen and IsClosed are Mathlib's notions.
-/

theorem result {X : Type*} [MetricSpace X] (U F : Set X) (hU : IsOpen U) (hF : IsClosed F) :
    IsOpen (U \ F) := by
  exact hU.sdiff hF

#print axioms result
