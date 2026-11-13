# Numerical Methods Coursework Documentation

## Project Overview
This repository contains lecture notes, problem sets, Python implementations, and examination reference sheets for the **IISER 5 Numerical Methods** course.

---

## Examination References

### 1. Mid-Semester Reference
- **Source:** `Numerical_Methods_Reference.tex` / `Notes/premid/Mid-Numerical_Methods_Python_Code_Reference (2).pdf`
- **Topics Covered:**
  - Root-Finding Methods (Bisection, Newton-Raphson, Secant, Inverse Quadratic Interpolation)
  - Polynomial Interpolation (Lagrange, Newton's Divided-Difference, Natural Cubic Spline)
  - Numerical Quadrature (Trapezoidal, Simpson's, Midpoint, Gauss-Legendre Quadrature)
  - Linear Systems & Multivariable Solvers (Gaussian Elimination with Partial Pivoting, LU / PA=LU Decomposition)

### 2. Quiz 2 Reference
- **Directory:** `Notes/Quiz2/`
- **Source:** [`Notes/Quiz2/Quiz2_Numerical_Methods_Reference.tex`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/Quiz2_Numerical_Methods_Reference.tex)
- **Compiled PDF:** [`Notes/Quiz2/Quiz2_Numerical_Methods_Reference.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/Quiz2_Numerical_Methods_Reference.pdf)
- **Theory Questionnaire:** [`Notes/Quiz2/quiz2_questionnaire.txt`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/quiz2_questionnaire.txt)
- **Model Answer Key:** [`Notes/Quiz2/quiz2_answers.txt`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/quiz2_answers.txt)

#### Individual Executable Jupyter Notebooks in `Notes/Quiz2/`:
1. [`01_1D_Diffusion_FTCS.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/01_1D_Diffusion_FTCS.ipynb): 1D Diffusion FTCS scheme, professor's Dirichlet and Neumann boundary conditions, particle conservation check, stable vs. unstable step demonstration, and Fourier mode decay comparison ($k=16\pi/L$ vs $k=2\pi/L$).
2. [`02_1D_Diffusion_Implicit_BTCS.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/02_1D_Diffusion_Implicit_BTCS.ipynb): Implicit BTCS tridiagonal linear system, proof and verification of unconditional stability ($C = 2.22 \gg 0.5$), and direct head-to-head comparison with explicit FTCS.
3. [`03_2D_and_Heterogeneous_Diffusion.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/03_2D_and_Heterogeneous_Diffusion.ipynb): 2D diffusion simulation ($C \le 0.25$) with temporal evolution across multiple timestamps ($t=0.0, 1.0, 3.0$), 3-panel 2D heatmaps, central 1D cross-section slice $\rho(x, y=0)$ showing peak flattening, and heterogeneous medium diffusion with spatially varying $D(x)$ and conservative half-grid fluxes.
4. [`04_1st_Order_Wave_Advection.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/04_1st_Order_Wave_Advection.ipynb): Professor's 1st-order wave upwind scheme, periodic boundary wrap-around, exact analytical translation, space-time trajectory heatmap, and demonstration of central-difference instability.
5. [`05_2nd_Order_Wave_Equation.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/05_2nd_Order_Wave_Equation.ipynb): Professor's 2nd-order wave equation leap-frog scheme with initial velocity step, exact magic time step ($k=1$), Dirichlet boundary inversion, space-time heatmap, and leftward traveling wave condition.
6. [`06_Random_Walks_1D_and_2D.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/06_Random_Walks_1D_and_2D.ipynb): Professor's 1D random walk code ($1000$ realizations, $20000$ steps), $\langle x \rangle$ and MSD $\langle x^2 \rangle = n$, and 2D isotropic random walk ($\langle R^2 \rangle = 2n$).
7. [`07_Fokker_Planck_and_Langevin.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/07_Fokker_Planck_and_Langevin.ipynb): Professor's Fokker-Planck simulation with harmonic potential $U(x)$, drift + diffusion currents, relaxation to Gibbs-Boltzmann distribution, and 1D Langevin dynamics with Euler-Maruyama.
8. [`08_ODE_Systems_and_Nonlinear_Solvers.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/08_ODE_Systems_and_Nonlinear_Solvers.ipynb): Nuclear decay explicit vs. implicit Euler stability ($\Delta t \le 2/\lambda$), professor's SHM RK4 damped oscillator, and multivariable Newton-Raphson system solver.
- **Scope & Syllabus Covered:**
  - **Finite Difference Discretization & Boundary Conditions:**
    - Forward, backward, and central first-derivative approximations.
    - Central second-derivative approximation (Taylor expansion & nested difference derivations).
    - Dirichlet (fixed value), Neumann (no-flux $J = -D \partial_x \rho = 0$), and Periodic boundary conditions.
    - Physical symmetries (translation, parity) and symmetry breaking by boundaries.
  - **Linear Partial Differential Equations (Diffusion):**
    - 1D Diffusion / Heat equation with Forward Time Centered Space (FTCS) explicit scheme.
    - Step-by-step von Neumann stability analysis deriving $\frac{D \Delta t}{\Delta x^2} \le \frac{1}{2}$.
    - Fourier mode decay dynamics ($\tau_k \propto 1/k^2 \propto \lambda^2$); comparison of decay rates across wavelengths.
    - Implicit Backward Time Centered Space (BTCS) scheme, tridiagonal matrix formulation, and proof of unconditional stability.
    - 2D Diffusion equation and general $d$-dimensional stability criterion $\frac{D\Delta t}{\delta^2} \le \frac{1}{2d}$.
    - Heterogeneous diffusion with spatially varying $D(x)$ using half-grid conservative flux discretization.
  - **Wave & Advection Equations:**
    - 1D First-order advection equation $\partial_t \psi + c \partial_x \psi = 0$.
    - Upwind scheme directional stability ($c > 0$ vs. $c < 0$), proof of CFL condition $\frac{c\Delta t}{\Delta x} \le 1$.
    - Numerical diffusion and dispersion analysis.
    - 1D Second-order wave equation $\partial_t^2 \psi = c^2 \partial_x^2 \psi$ using central leap-frog scheme.
    - The "magic" time step $k = \frac{c\Delta t}{\Delta x} = 1$ with zero numerical dispersion.
    - Second-order Taylor step initialization for initial velocity $\dot{\psi}(x, 0) = v(x)$, traveling wave conditions, and fixed-end reflections.
  - **Stochastic Systems & SDEs:**
    - 1D Discrete Random Walk: step statistics, unbiased vs. biased walk drift, variance, and mean squared displacement (MSD $\langle x^2 \rangle = n$).
    - Distinction between individual stochastic realizations and smooth ensemble averages.
    - 2D isotropic random walk ($\langle R^2 \rangle = 2n$).
    - Brownian motion & Langevin dynamics ($m \dot{v} = -\gamma v + \xi(t)$), Einstein relation $D = k_B T / \gamma$, Euler-Maruyama algorithm.
    - Fokker-Planck (Smoluchowski) equation derived from continuity equation $\partial_t \rho + \partial_x J = 0$ with drift and diffusion currents; Gibbs-Boltzmann relaxation.
  - **Advanced ODEs & Nonlinear Systems:**
    - First-order ODEs: Nuclear decay $\dot{N} = -\lambda N$, explicit Euler stability ($\Delta t \le 2/\lambda$) vs. unconditionally stable implicit Euler.
    - Second-order ODEs: Damped and driven harmonic oscillators, characteristic timescales ($\tau_{\text{osc}}, \tau_{\text{damp}}, \tau_{\text{drive}}$), overdamped approximation.
    - Scheme comparison: simple Euler instability vs. symplectic Euler-Cromer vs. 4th-order Runge-Kutta (RK4).
    - 1D and 2D dynamical systems: fixed-point classification (trace-determinant plane), nullclines, phase portraits.
    - Multivariable Newton-Raphson system solver ($\mathbf{x}_{k+1} = \mathbf{x}_k - [\mathbf{J}(\mathbf{x}_k)]^{-1}\mathbf{F}(\mathbf{x}_k)$).
