import Mathlib

/-!
Problem Q2.12, part (b)(i), together with the setting of part (b) that it uses.

- (b) Let $U=\{(x,y)\in\mathbb{R}^2:\ y>x^2\}$, let $(a,b)\in U$ and put $\delta=b-a^2>0$.
  - (i) Show that if $0<r\le1$ and $(x,y)\in\mathbb{R}^2$ satisfies $|x-a|<r$ and $|y-b|<r$, then $y-x^2>\delta-(2|a|+2)r$.

In the formal statement, the hypothesis $(a,b)\in U$ is written as $b>a^2$, and $\delta=b-a^2$ is written out in full (no new name is introduced).
-/

theorem result (a b : ℝ) (hab : b > a ^ 2) (r : ℝ) (hr0 : 0 < r) (hr1 : r ≤ 1)
    (x y : ℝ) (hx : |x - a| < r) (hy : |y - b| < r) :
    y - x ^ 2 > (b - a ^ 2) - (2 * |a| + 2) * r := by
  obtain ⟨hx1, hx2⟩ := abs_lt.mp hx
  obtain ⟨hy1, hy2⟩ := abs_lt.mp hy
  -- a * (x - a) <= |a| * |x - a| <= |a| * r
  have hprod : a * (x - a) ≤ |a| * r := by
    have h := le_abs_self (a * (x - a))
    rw [abs_mul] at h
    exact le_trans h (mul_le_mul_of_nonneg_left (le_of_lt hx) (abs_nonneg a))
  -- (x - a)^2 = |x - a|^2 < r^2 <= r, because 0 < r <= 1
  have hsq : (x - a) ^ 2 < r := by
    have h0 : 0 ≤ |x - a| := abs_nonneg _
    have h1 : |x - a| ^ 2 < r ^ 2 := by nlinarith
    have h2 : r ^ 2 ≤ r := by nlinarith
    rw [sq_abs] at h1
    linarith
  nlinarith [hprod, hsq, hy1]

#print axioms result
