import Mathlib

/-!
Problem Q2.7, part (a), copied from the prompt:

Let $(X,d)$ be a metric space, $U\subset X$ open and $F\subset X$ closed.

- (a) Prove that $U\setminus F$ is open and that $F\setminus U$ is closed.

Statement the problem relies on (the statement field of Q2.7):

**Corollaries (finite unions and arbitrary intersections of closed sets).** In a metric space, a finite union of closed sets is closed, and an arbitrary intersection of closed sets is closed. **Method:** pass to complements with De Morgan's laws, which turn unions into intersections and vice versa, and then use the properties of open sets (finite intersections of open sets are open [Q2.5]; arbitrary unions of open sets are open [Q2.3]).

This file proves the second conclusion only: if $U$ is open and $F$ is closed, then $F\setminus U$ is closed. The metric space is an arbitrary type $X$ with a MetricSpace instance; IsOpen and IsClosed are Mathlib's notions.
-/

theorem result {X : Type*} [MetricSpace X] (U F : Set X) (hU : IsOpen U) (hF : IsClosed F) :
    IsClosed (F \ U) := by
  exact hF.sdiff hU

#print axioms result
