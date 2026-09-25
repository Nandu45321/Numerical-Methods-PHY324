# Lessons Learned

## Mathematical Formulas vs. Numerical Implementations (Newton's Method for Systems)
**Context:** When implementing Newton's Method for Systems of Equations, the standard mathematical formula taught in class is $\mathbf{x}_{i+1} = \mathbf{x}_i - [\mathbf{J}(\mathbf{x}_i)]^{-1} \mathbf{F}(\mathbf{x}_i)$.
**The Wrong Assumption:** It is a common mistake to assume that the code must explicitly compute the inverse of the Jacobian matrix (using something like `np.linalg.inv()`) to multiply with $\mathbf{F}$.
**The Correct Mental Model:** In numerical computing, calculating the explicit inverse of a matrix is both computationally expensive ($O(N^3)$ operations) and numerically unstable (highly susceptible to floating-point errors). 
**The Fix:** Instead of computing the inverse, we restructure the equation to solve for a "step vector" $\mathbf{s}_i$:
$$ \mathbf{J}(\mathbf{x}_i) \mathbf{s}_i = -\mathbf{F}(\mathbf{x}_i) $$
We solve this linear system using standard Gaussian elimination or LU decomposition (e.g., `np.linalg.solve(J, -F)`). Once we have the step vector, we simply update our guess: $\mathbf{x}_{i+1} = \mathbf{x}_i + \mathbf{s}_i$. This yields the exact same mathematical result but is drastically faster and much more stable. Never compute matrix inverses directly if you only need to solve a linear system! 

**User Preference Exception:** Despite the numerical instability of calculating the explicit matrix inverse, the user explicitly requires the direct inverse formula ($ \mathbf{x}_{i+1} = \mathbf{x}_i - [\mathbf{J}(\mathbf{x}_i)]^{-1} \mathbf{F}(\mathbf{x}_i) $) to be used in all code and documentation for their coursework revision. Always honor this preference.
