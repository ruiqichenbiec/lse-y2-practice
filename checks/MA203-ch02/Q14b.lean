import Mathlib

/-!
Let $(X,d)$ be a metric space.

- (b) In $\mathbb{R}^2$ with the Euclidean norm, let $a_n=\Big(\dfrac{n}{n+1},\ \dfrac{(-1)^n}{\sqrt n}\Big)$. Prove, using the definition, that $(a_n)_{n\in\mathbb{N}}$ converges to $(1,0)$. **(4 marks)**

Statement relied on (definition, part (a)): $(a_n)_{n\in\mathbb{N}}$ is convergent with limit $L\in X$ if for every $\epsilon>0$ there exists $N\in\mathbb{N}$ such that $d(a_n,L)<\epsilon$ for all $n>N$.

Lean choices: the Euclidean plane is EuclideanSpace ℝ (Fin 2), whose distance is the Euclidean norm distance. Convergence is stated with Mathlib's Filter.Tendsto along atTop, which is equivalent to the epsilon-N definition above. The value of the sequence at n = 0 does not affect convergence.
-/

theorem result :
    Filter.Tendsto
      (fun n : ℕ => (!₂[(n : ℝ) / ((n : ℝ) + 1), (-1 : ℝ) ^ n / Real.sqrt (n : ℝ)] : EuclideanSpace ℝ (Fin 2)))
      Filter.atTop (nhds (!₂[(1 : ℝ), (0 : ℝ)] : EuclideanSpace ℝ (Fin 2))) := by
  have h0 : Filter.Tendsto (fun n : ℕ => (n : ℝ) / ((n : ℝ) + 1)) Filter.atTop (nhds 1) :=
    tendsto_natCast_div_add_atTop (1 : ℝ)
  have h2 : Filter.Tendsto (fun n : ℕ => (Real.sqrt (n : ℝ))⁻¹) Filter.atTop (nhds 0) :=
    tendsto_inv_atTop_zero.comp (Real.tendsto_sqrt_atTop.comp tendsto_natCast_atTop_atTop)
  have h1 : Filter.Tendsto (fun n : ℕ => (-1 : ℝ) ^ n / Real.sqrt (n : ℝ)) Filter.atTop (nhds 0) := by
    refine squeeze_zero_norm (fun n : ℕ => ?_) h2
    have e : ‖(-1 : ℝ) ^ n / Real.sqrt (n : ℝ)‖ = (Real.sqrt (n : ℝ))⁻¹ := by
      rw [norm_div, norm_pow, norm_neg, norm_one, one_pow, Real.norm_of_nonneg (Real.sqrt_nonneg _),
        one_div]
    exact e.le
  have hg : Filter.Tendsto
      (fun n : ℕ => ![(n : ℝ) / ((n : ℝ) + 1), (-1 : ℝ) ^ n / Real.sqrt (n : ℝ)])
      Filter.atTop (nhds ![(1 : ℝ), (0 : ℝ)]) := by
    rw [tendsto_pi_nhds]
    intro i
    fin_cases i
    · simpa using h0
    · simpa using h1
  have hc : Continuous (WithLp.toLp 2 : (Fin 2 → ℝ) → EuclideanSpace ℝ (Fin 2)) := by
    fun_prop
  exact (hc.tendsto _).comp hg

#print axioms result
