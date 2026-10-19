# Week 2 — Roots, Linear Systems and Least Squares

## Roots and the Intermediate Value Theorem

A root of `f(x)` satisfies `f(x)=0`. For continuous `f` on `[a,b]`, if `f(a)f(b)<0`, at least one root lies in `(a,b)` (IVT). A sign change is sufficient, but not necessary, for a root.

## Bisection

Midpoint `c=(a+b)/2`. Evaluate `f(c)` and retain the half with opposite-sign endpoint values.

**Worked example:** `f(x)=x^3-x-2`, initial `[1,2]`: `f(1)=-2`, `f(2)=4`.

| n | Starting interval | c | f(c) | Updated bracket |
|---|---|---:|---:|---|
| 1 | [1,2] | 1.5 | -0.125 | [1.5,2] |
| 2 | [1.5,2] | 1.75 | 1.609375 | [1.5,1.75] |
| 3 | [1.5,1.75] | 1.625 | 0.666015625 | [1.5,1.625] |

The **third bisection estimate** is `1.625`; the **final bracket** is `[1.5,1.625]`. Do not put `f(a)` and `f(c)` into the interval: intervals contain x-values.

Bracket width halves each iteration; standard bisection converges for continuous functions with a valid sign-changing bracket.

## Newton–Raphson

`x_(n+1) = x_n - f(x_n)/f'(x_n)`.

**Worked example:** `f(x)=x^2-9`, `f'(x)=2x`, `x0=4`.

- `x1=4-(16-9)/8=3.125`.
- `x2=3.125-(3.125²-9)/(2·3.125)=3.0025`.

**Common mistake:** the derivative of a constant is zero (`d/dx(x²-9)=2x`, not `2x-9`). Use x1 for the second iteration, not x0 again. Newton can fail if derivative is zero or a starting guess is poor.

## Secant

`x_(n+1) = x_n - f(x_n)·(x_n-x_(n-1))/(f(x_n)-f(x_(n-1)))`.

Starts from two estimates, approximates slope without explicit derivative. Its denominator cannot be zero; convergence is not guaranteed for arbitrary guesses.

## Stopping criteria

- Bracket width small enough (bisection).
- Residual `|f(x)|` sufficiently small.
- Difference `|x_(n+1)-x_n|` sufficiently small.
- Maximum iteration cap reached (a safety stop, not a proof of convergence).

**Caution:** small residual does not always mean small error in x if the problem is ill-conditioned.

## Linear systems and verification

`A x = b`. Example `2x+y=7`, `x-y=2` gives `x=3`, `y=1`.

Elimination: add equations to get `3x=9`; substitute to obtain `y=1`. Verify: `2·3+1=7`, `3-1=2`.

**Gaussian elimination:** use row operations to create an upper-triangular system, then solve it using back-substitution. **Partial pivoting:** at each column, swap in the row having the largest available absolute pivot to reduce problems caused by tiny pivots.

Check numerical solution with residual `r=A x_hat-b`. A small residual is reassuring but may not guarantee small solution error when `A` is ill-conditioned. The condition number estimates sensitivity.

## Least squares and ML

When observed data cannot be fitted exactly, seek coefficients β minimizing `||Xβ-y||²`. The normal equations are `XᵀXβ=Xᵀy` (only solve directly when the matrix is sufficiently well behaved). QR and SVD are often more numerically reliable than explicitly forming `XᵀX`, especially for poorly conditioned problems.

**Direct vs iterative:** direct linear solvers work by a finite sequence of factorization/elimination steps; iterative methods refine approximate solutions over multiple updates. In optimization, a stationarity equation `J'(θ)=0` can itself be treated as a root-finding problem, but stationarity alone does not prove a minimum.

## Check yourself

1. Why does bisection need a sign-changing bracket?
2. Write Newton's update for `f(x)=x³-x-2`; identify the derivative.
3. State one reason a secant update may fail.
4. Solve a 2×2 system and verify both original equations.
5. Explain why QR/SVD are preferred to normal equations in poorly conditioned least squares.
