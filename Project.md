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

### 3. End-Semester Organization
- **Packaged Zip Archive:** [`Endsem_Numerical_Methods.zip`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Endsem_Numerical_Methods.zip) (contains all 4 End-Semester directories with all 18 executed `.ipynb` notebooks).
- **End-Semester Examination Syllabus Sections & Mapped Materials:**

#### 1. Linear Ordinary Differential Equations
- **Directory:** [`Linear Ordinary Differential Equations/`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Ordinary%20Differential%20Equations/)
- **Primary Topics & Mathematical Concepts:**
  - First-order linear ODEs: radioactive decay $\dot{N} = -\lambda N$, truncation error (local $\mathcal{O}(h^2)$ vs global $\mathcal{O}(h)$), stability bounds for explicit Euler ($h \le 1/\lambda$ for monotonicity, $h \le 2/\lambda$ for boundedness).
  - Explicit Euler vs. Implicit Euler (backward Euler, unconditionally stable).
  - Second-order linear ODEs: Damped and driven harmonic oscillators ($m\ddot{x} + \gamma \dot{x} + kx = F(t)$), conversion into systems of first-order ODEs ($v = \dot{x}$, $\dot{v} = -(kx + \gamma v)/m$).
  - Characteristic physical timescales: oscillatory $\tau_{\text{osc}} = \sqrt{m/k}$, damping $\tau_{\text{damp}} = \gamma/k$, dissipative $\tau_{\text{diss}} = m/\gamma$, and dimensional reduction to overdamped 1st-order dynamics.
  - Multi-step / Higher-order numerical integrators: Improved Euler (Heun's 2nd-order), Runge-Kutta 4th-order (RK4) algorithm, Butcher tableau, local error $\mathcal{O}(h^5)$, global error $\mathcal{O}(h^4)$.
  - 2D Linear autonomous systems $\dot{\mathbf{x}} = \mathbf{J}\mathbf{x}$: fixed-point stability classification in the trace-determinant ($\tau$-$\Delta$) plane (saddles, stable/unstable nodes, spirals, centers), and failure/artificial energy drift of explicit Euler for centers.
- **Lecture Notes & Reference Files:**
  - [`lec9.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/lec9.pdf): 1st-order ODEs, simple vs. improved Euler, nuclear decay stability.
  - [`lec10.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/lec10.pdf): Damped harmonic oscillator, reduction to 1st-order system, timescales, overdamped limit.
  - [`lec11.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/lec11.pdf): Recap of linear ODEs, timescales, RK4 derivation and algorithm.
  - [`tutorial_10_10_26.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/tutorial_10_10_26.pdf): Step-by-step algorithms for Euler, Heun, and RK4 on harmonic oscillator.
- **Problem Sets & Exercises:**
  - [`Problem Set II.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Problem%20Set%20II.pdf) Q1: Driven damped oscillator with RK4, comparison with exact solution, overdamped limit.
  - [`Problem Set II.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Problem%20Set%20II.pdf) Q3: 2D linear autonomous systems $\dot{\mathbf{x}} = \mathbf{A}\mathbf{x}$, eigenvalues/eigenvectors, phase portraits, failure of Euler for center.
  - [`problem_set_III.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/problem_set_III.pdf) Q1: Explicit vs. implicit Euler on nuclear decay, derivation of stability bounds.
- **Relevant Code Notebooks:**
  - [`Nuclear-decay.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/n/Nuclear-decay.ipynb): Student 1st-order nuclear decay simulation.
  - [`Simple Harmonic Ocilator.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/n/Simple%20Harmonic%20Ocilator.ipynb): Student damped oscillator simulation.
  - [`SHM_rk4.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/SHM_rk4.ipynb): Professor's RK4 harmonic oscillator code.
  - [`08_ODE_Systems_and_Nonlinear_Solvers.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/08_ODE_Systems_and_Nonlinear_Solvers.ipynb): Nuclear decay explicit vs. implicit Euler, SHM RK4 implementation.
- **Created Executable Notebooks (`Notes/Linear Ordinary Differential Equations/`):**
  1. [`01_First_Order_ODEs_and_Euler_Methods.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Ordinary%20Differential%20Equations/01_First_Order_ODEs_and_Euler_Methods.ipynb): Simple Euler, Improved Euler, and Implicit Euler comparison, stability check, plus exact class code from `Nuclear-decay.ipynb`.
  2. [`02_Second_Order_ODEs_SHM_and_RK4.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Ordinary%20Differential%20Equations/02_Second_Order_ODEs_SHM_and_RK4.ipynb): 1st-order system conversion, Simple Euler vs. Euler-Cromer, professor's exact `SHM_rk4.ipynb` code, and class SHM code.
  3. [`03_2D_Linear_Autonomous_Systems.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Ordinary%20Differential%20Equations/03_2D_Linear_Autonomous_Systems.ipynb): Eigenvalue stability rules and direct RK4/Euler phase plots (stable spiral vs. center blowup).
  4. [`04_Linear_ODE_Problem_Set_Solutions.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Ordinary%20Differential%20Equations/04_Linear_ODE_Problem_Set_Solutions.ipynb): Step-by-step solutions grouped by type for Problem Set III Q1 (Type 1), Problem Set II Q1 (Type 2), and Problem Set II Q3 (Type 3).

#### 2. Nonlinear Ordinary Differential Equations
- **Directory:** [`Nonlinear Ordinary Differential Equations/`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Nonlinear%20Ordinary%20Differential%20Equations/)
- **Primary Topics & Mathematical Concepts:**
  - 1D Nonlinear dynamical systems $\dot{x} = f(x)$: fixed points $f(x^*) = 0$, linear stability criterion $f'(x^*) < 0$ (stable) vs $f'(x^*) > 0$ (unstable).
  - Bifurcations in 1D:
    - Subcritical / Supercritical Pitchfork bifurcation ($\dot{x} = rx \pm x^3 - x^5$).
    - Transcritical bifurcation ($\dot{x} = rx - \ln(1+x)$).
    - Saddle-node bifurcation & hysteresis ($\dot{x} = \frac{2x}{5}(1 - x/20) - x^2/(1+x^2)$).
  - Multivariable Nonlinear Root-Finding: Newton-Raphson for systems $\mathbf{F}(\mathbf{x}) = \mathbf{0}$, Jacobian matrix $\mathbf{J}_{ij} = \partial F_i / \partial x_j$, iteration step $\mathbf{x}_{k+1} = \mathbf{x}_k - \mathbf{J}^{-1}\mathbf{F}(\mathbf{x}_k)$.
  - 2D Nonlinear autonomous systems & Phase Plane:
    - Lotka-Volterra competition model: $\dot{x} = x(3 - x - 2y)$, $\dot{y} = y(2 - y - x)$.
    - Finding multiple fixed points, computing the Jacobian at each fixed point, eigenvalues, local linearization, and global phase plane trajectories.
  - Mechanical nonlinear systems: Bead on a rotating hoop ($mr\ddot{\varphi} = -br\dot{\varphi} - mg\sin\varphi + mr\omega^2 \sin\varphi\cos\varphi$), supercritical pitchfork bifurcation at critical rotation frequency $\omega_c = \sqrt{g/r}$, timescales $\tau = br/(mg)$, overdamped reduction.
- **Lecture Notes & Reference Files:**
  - [`Reference_nonlinear_system.pptx`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Reference_nonlinear_system.pptx): Strogatz *Nonlinear Dynamics and Chaos* reference (Chapters 2, 5, and 6).
- **Problem Sets & Exercises:**
  - [`Problem Set II.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Problem%20Set%20II.pdf) Q2: 1D nonlinear flows, fixed point stability, pitchfork, transcritical, and saddle-node bifurcations.
  - [`Problem Set II.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Problem%20Set%20II.pdf) Q4: 2D Lotka-Volterra competition model, 4 fixed points, Jacobian stability analysis.
  - [`Problem Set II.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Problem%20Set%20II.pdf) Q5: Bead on a rotating hoop, pitchfork bifurcation at critical spin speed, overdamped 1st-order approximation vs. full 2nd-order system.
- **Relevant Code Notebooks:**
  - [`Newton_SOE.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Newton_SOE.ipynb) / [`Newton_Systems.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/4/Newton_Systems.ipynb): Multivariable Newton-Raphson system solver with analytical Jacobian.
  - [`08_ODE_Systems_and_Nonlinear_Solvers.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/08_ODE_Systems_and_Nonlinear_Solvers.ipynb) (Section 3): Multivariable Newton solver with numerical finite-difference Jacobian.
- **Created Executable Notebooks (`Notes/Nonlinear Ordinary Differential Equations/`):**
  1. [`01_1D_Nonlinear_Flows_and_Bifurcations.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Nonlinear%20Ordinary%20Differential%20Equations/01_1D_Nonlinear_Flows_and_Bifurcations.ipynb): Fixed points, derivative stability test, bifurcation plot of $f(x)$, and Simple Euler trajectories.
  2. [`02_2D_Nonlinear_Systems_and_Phase_Plane.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Nonlinear%20Ordinary%20Differential%20Equations/02_2D_Nonlinear_Systems_and_Phase_Plane.ipynb): Fixed points, Jacobian eigenvalues, and direct RK4 Lotka-Volterra phase portrait.
  3. [`03_Nonlinear_System_Solvers_Newton_Method.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Nonlinear%20Ordinary%20Differential%20Equations/03_Nonlinear_System_Solvers_Newton_Method.ipynb): Clean `np.linalg.solve` Newton solver plus professor's exact `Newton_SOE.ipynb` Gaussian elimination code.
  4. [`04_Nonlinear_ODE_Problem_Set_Solutions.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Nonlinear%20Ordinary%20Differential%20Equations/04_Nonlinear_ODE_Problem_Set_Solutions.ipynb): Individual sub-question solutions grouped by type for Problem Set II Q2 (Type 1), Q4 (Type 2), and Q5 (Type 3).

#### 3. Linear Partial Differential Equations
- **Directory:** [`Linear Partial Differential Equations/`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Partial%20Differential%20Equations/)
- **Primary Topics & Mathematical Concepts:**
  - Physical symmetries: continuous translational symmetry ($x \to x+a$), parity / spatial inversion symmetry ($x \to -x$), and symmetry breaking via physical boundaries.
  - Boundary conditions: Dirichlet (fixed boundary values), Neumann (no-flux $J = -D \partial_x \rho = 0$), Periodic (toroidal wrap-around).
  - 1D Diffusion / Heat equation: $\partial_t \rho = D \partial_x^2 \rho$.
    - FTCS (Forward Time Centered Space) explicit discretization.
    - von Neumann stability analysis: derivation of the Courant stability condition $C = \frac{D\Delta t}{\Delta x^2} \le \frac{1}{2}$.
    - Fourier mode decay dynamics: $\tau_k = \frac{1}{D k^2} = \frac{\lambda^2}{4\pi^2 D}$, explaining why short wavelengths damp exponentially faster than fundamental modes.
    - Particle / mass conservation check $\sum \rho_i \Delta x = \text{const}$ under no-flux Neumann boundaries.
  - Implicit Diffusion (BTCS - Backward Time Centered Space):
    - Tridiagonal linear system $\mathbf{A}\mathbf{\rho}^{n+1} = \mathbf{\rho}^n$, Thomas algorithm / tridiagonal solve.
    - Analytical proof of unconditional stability for any $\Delta t$.
  - Multidimensional & Heterogeneous Diffusion:
    - 2D Diffusion $\partial_t \rho = D(\partial_x^2 \rho + \partial_y^2 \rho)$ and general $d$-dimensional stability limit $C \le \frac{1}{2d}$ ($1/4$ in 2D).
    - Heterogeneous diffusion $\partial_t \rho = \partial_x(D(x)\partial_x \rho)$ using conservative half-grid interface fluxes $J_{i+1/2} = -D_{i+1/2}\frac{\rho_{i+1} - \rho_i}{\Delta x}$.
  - 1st-Order Wave / Advection Equation: $\partial_t \psi + c \partial_x \psi = 0$.
    - Upwind scheme: directional choice based on sign of wave speed $c$, proof of CFL condition $\frac{c\Delta t}{\Delta x} \le 1$.
    - Failure and unconditional instability of centered-in-space scheme for advection.
  - 2nd-Order Wave Equation: $\partial_t^2 \psi = c^2 \partial_x^2 \psi$.
    - Central leap-frog explicit scheme.
    - Second-order Taylor initial velocity step $\psi(x, \Delta t) \approx \psi(x, 0) + \Delta t \, v(x) + \frac{c^2 \Delta t^2}{2} \partial_x^2 \psi(x, 0)$.
    - The "magic" time step $k = \frac{c\Delta t}{\Delta x} = 1$ yielding exact, dispersionless numerical propagation.
    - Fixed Dirichlet boundary reflections (phase inversion) vs. leftward traveling wave condition $\dot{\psi}(x, 0) = -c \partial_x \psi(x, 0)$.
- **Lecture Notes & Reference Files:**
  - [`lec_pde.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/lec_pde.pdf): Symmetries, boundary conditions, Fourier mode decay, 1st and 2nd-order wave equations.
  - [`Tutorial_03_11_26.pptx`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Tutorial_03_11_26.pptx): Diffusion and advection discretization, boundary conditions.
  - [`Notes.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Notes.pdf): Student lecture notes covering PDE discretization and wave equations.
- **Problem Sets & Exercises:**
  - [`problem_set_III.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/problem_set_III.pdf) Q2: Heterogeneous diffusion with space-dependent $D(x)$, half-grid conservative fluxes.
  - [`problem_set_III.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/problem_set_III.pdf) Q3: 2D diffusion equation, von Neumann stability derivation ($C \le 1/4$).
  - [`problem_set_III.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/problem_set_III.pdf) Q4: 2nd-order wave equation, leap-frog scheme, standing vs. leftward traveling wave condition.
  - [`problem_set_III.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/problem_set_III.pdf) Q5: 1D Implicit diffusion (BTCS), tridiagonal system, proof of unconditional stability.
  - [`problem_set_III.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/problem_set_III.pdf) Q6: Fourier modes decay timescales ($\tau_k \propto 1/k^2$), comparison between $k = 2\pi/L$ and $k = 16\pi/L$.
- **Relevant Code Notebooks:**
  - [`1D_diffusion.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/1D_diffusion.ipynb): Professor's 1D diffusion code.
  - [`1storderwaveeqn.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/n+1/1storderwaveeqn.ipynb): Student 1st-order wave upwind code.
  - [`2ndorderwaveeqn.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/n+1/2ndorderwaveeqn.ipynb): Student 2nd-order wave leap-frog code.
  - [`01_1D_Diffusion_FTCS.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/01_1D_Diffusion_FTCS.ipynb): 1D Diffusion FTCS, Dirichlet/Neumann BCs, Fourier modes.
  - [`02_1D_Diffusion_Implicit_BTCS.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/02_1D_Diffusion_Implicit_BTCS.ipynb): Implicit BTCS tridiagonal solver.
  - [`03_2D_and_Heterogeneous_Diffusion.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/03_2D_and_Heterogeneous_Diffusion.ipynb): 2D diffusion evolution & heterogeneous diffusion.
  - [`04_1st_Order_Wave_Advection.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/04_1st_Order_Wave_Advection.ipynb): 1st-order advection upwind scheme & CFL stability.
  - [`05_2nd_Order_Wave_Equation.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/05_2nd_Order_Wave_Equation.ipynb): 2nd-order wave equation leap-frog scheme & magic time step.
- **Created Executable Notebooks (`Notes/Linear Partial Differential Equations/`):**
  1. [`01_1D_Diffusion_Explicit_FTCS.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Partial%20Differential%20Equations/01_1D_Diffusion_Explicit_FTCS.ipynb): Simple FTCS 1D diffusion with Neumann BC, instability blowup demo, plus professor's exact `1D_diffusion.ipynb` code.
  2. [`02_1D_Diffusion_Implicit_BTCS.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Partial%20Differential%20Equations/02_1D_Diffusion_Implicit_BTCS.ipynb): Implicit BTCS tridiagonal solver (`scipy.linalg.solve`) showing unconditional stability at $C = 2.22$.
  3. [`03_2D_and_Heterogeneous_Diffusion.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Partial%20Differential%20Equations/03_2D_and_Heterogeneous_Diffusion.ipynb): 2D diffusion evolution across 3 timestamps plus heterogeneous $D(x)$ half-grid flux diffusion.
  4. [`04_1st_Order_Wave_Advection.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Partial%20Differential%20Equations/04_1st_Order_Wave_Advection.ipynb): Upwind scheme with periodic BC, central-difference instability demo, plus exact `1storderwaveeqn.ipynb` class code.
  5. [`05_2nd_Order_Wave_Equation.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Partial%20Differential%20Equations/05_2nd_Order_Wave_Equation.ipynb): Leap-frog scheme with magic time step ($k=1$) and fixed-end reflections, plus exact `2ndorderwaveeqn.ipynb` class code.
  6. [`06_Linear_PDE_Problem_Set_Solutions.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Linear%20Partial%20Differential%20Equations/06_Linear_PDE_Problem_Set_Solutions.ipynb): Simple step-by-step solutions for `problem_set_III.pdf` Q2–Q6 grouped by type (Type 1: Q2 & Q3; Type 2: Q5 & Q6; Type 3: Q4).

#### 4. Stochastic System
- **Directory:** [`Stochastic System/`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Stochastic%20System/)
- **Primary Topics & Mathematical Concepts:**
  - 1D Discrete Random Walk:
    - Step statistics: independent identically distributed (i.i.d.) jumps $\eta_n = \pm 1$ with probability $p$ and $q = 1-p$.
    - Unbiased random walk: $\langle x_n \rangle = 0$, Mean Squared Displacement (MSD) $\langle x_n^2 \rangle = n$.
    - Biased random walk: mean drift $\langle x_n \rangle = n(p-q)$, variance $\sigma_n^2 = 4npq$.
    - Statistical distinction between jagged individual realization trajectories vs. smooth deterministic ensemble averages.
  - 2D Isotropic Random Walk:
    - Independent Cartesian steps: $\Delta x = \pm 1$, $\Delta y = \pm 1$, total displacement $R_n^2 = x_n^2 + y_n^2$.
    - MSD scaling: $\langle R_n^2 \rangle = \langle x_n^2 \rangle + \langle y_n^2 \rangle = 2n$.
  - Brownian Motion & Langevin Dynamics:
    - Continuous-time Langevin equation: $m \frac{dv}{dt} = -\gamma v + \xi(t)$, where $\xi(t)$ is Gaussian white noise ($\langle \xi(t) \rangle = 0$, $\langle \xi(t)\xi(t') \rangle = 2\gamma k_B T \delta(t-t')$).
    - Overdamped Langevin equation: $\gamma \frac{dx}{dt} = -\nabla U(x) + \xi(t)$.
    - Euler-Maruyama algorithm for stochastic differential equations (SDEs): $\Delta W \sim \sqrt{\Delta t} \, \mathcal{N}(0, 1)$.
    - Einstein-Smoluchowski diffusion relation: $D = \frac{k_B T}{\gamma}$.
  - Fokker-Planck (Smoluchowski) Equation:
    - Derivation from conservation law $\partial_t \rho + \partial_x J = 0$.
    - Total flux $J = J_{\text{drift}} + J_{\text{diff}} = -\rho \frac{U'(x)}{\gamma} - D \partial_x \rho$.
    - Fokker-Planck PDE: $\partial_t \rho = \partial_x \left[ D \partial_x \rho + \frac{U'(x)}{\gamma} \rho \right]$.
    - Equilibrium steady-state ($J = 0$): relaxation to the Gibbs-Boltzmann distribution $\rho_{\text{eq}}(x) \propto \exp\left(-\frac{U(x)}{k_B T}\right)$.
- **Lecture Notes & Reference Files:**
  - [`lec_sde.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/lec_sde.pdf): Brownian motion, Langevin equation, 1D and 2D random walks, syllabus overview.
  - [`lec_pde.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/lec_pde.pdf) (Slides 7-9): Fokker-Planck continuity equation derivation and Gibbs-Boltzmann distribution.
- **Problem Sets & Exercises:**
  - [`lec_sde.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/lec_sde.pdf) Exercise 1: 2D unbiased random walk ($\langle \mathbf{R}_n \rangle = 0$, $\langle R_n^2 \rangle = 2n$) vs. 1D walk.
  - [`lec_sde.pdf`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/lec_sde.pdf) Exercise 2: 1D biased random walk ($p=2/3, q=1/3$): $\langle x_n \rangle$, $\langle x_n^2 \rangle$, and shifted MSD.
- **Relevant Code Notebooks:**
  - [`randomwalk_1D.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/randomwalk_1D.ipynb): Professor's 1D random walk code ($1000$ realizations, $20000$ steps).
  - [`FokkerPlanck.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/FokkerPlanck.ipynb): Professor's Fokker-Planck drift-diffusion code with harmonic potential $U(x) = \frac{1}{2} k (x - L/2)^2$.
  - [`06_Random_Walks_1D_and_2D.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/06_Random_Walks_1D_and_2D.ipynb): 1D unbiased/biased walks, MSD verification, 2D isotropic walks.
  - [`07_Fokker_Planck_and_Langevin.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Quiz2/07_Fokker_Planck_and_Langevin.ipynb): Fokker-Planck simulation & Langevin dynamics via Euler-Maruyama.
- **Created Executable Notebooks (`Notes/Stochastic System/`):**
  1. [`01_1D_and_2D_Random_Walks.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Stochastic%20System/01_1D_and_2D_Random_Walks.ipynb): 1D & 2D random walk MSD checks plus professor's exact `randomwalk_1D.ipynb` code.
  2. [`02_Langevin_Dynamics_and_Brownian_Motion.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Stochastic%20System/02_Langevin_Dynamics_and_Brownian_Motion.ipynb): 1D Langevin trajectory and overdamped Brownian $\langle x^2 \rangle = 2Dt$ verification via Euler-Maruyama.
  3. [`03_Fokker_Planck_Equation.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Stochastic%20System/03_Fokker_Planck_Equation.ipynb): Drift-diffusion relaxation in harmonic potential plus professor's exact `FokkerPlanck.ipynb` code.
  4. [`04_Stochastic_Problem_Set_Solutions.ipynb`](file:///home/nandu/Documents/IISER%205/Numerical%20Methods/Notes/Stochastic%20System/04_Stochastic_Problem_Set_Solutions.ipynb): Step-by-step solutions for `lec_sde.pdf` Exercises 1 & 2 grouped by type (Type 1: 2D vs 1D walk; Type 2: 1D biased walk).

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
