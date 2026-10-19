# Answer Key — Open Only After Attempting

This is a teaching key for the **new** practice test in `practice/remedial-mock.md`, not an official marking scheme.

## A. Multiple choice

1. B: `|80−76|/80 = 4/80 = 0.05`.
2. C: bisection uses a continuous sign-changing bracket.
3. B: near-equal subtraction and round-off cancellation.
4. A: L2 adds squared-coefficient penalty.
5. C: even number of equally spaced subintervals.

## B. Calculations

6. Residuals `r = [1,-1,1]`; MSE `(1²+(-1)²+1²)/3=1`.
7. Adding equations: `4x=12` → `x=3`; `3−y=2` → `y=1`. Verify `3(3)+1=10` and `3−1=2`.
8. `f(1.5)=3.375`, `f(0.5)=0.125`, central derivative `(3.375−0.125)/(1)=3.25`; exact `f'(1)=3`; too small h worsens cancellation/rounding.
9. `y=3+(2−1)/(5−1)·(11−3)=5`; x=6 is outside observed interval `[1,5]`, where the line may no longer hold.

## C. Root-finding

10. `f(1)=1−1−1=-1`, `f(2)=8−2−1=5`; continuous polynomial and opposite signs imply a root in `(1,2)`.

| n | Starting bracket | Midpoint | f(c) | New bracket |
|---|---|---:|---:|---|
| 1 | [1,2] | 1.5 | 0.875 | [1,1.5] |
| 2 | [1,1.5] | 1.25 | -0.296875 | [1.25,1.5] |
| 3 | [1.25,1.5] | 1.375 | 0.224609375 | [1.25,1.375] |

Third estimate: 1.3750; final bracket `[1.2500,1.3750]`.

11. `f'(x)=3x²−1`; Newton formula `x_(n+1) = x_n − (x_n³−x_n−1)/(3x_n²−1)`.

From x0=1.5: `f(1.5)=0.875`, `f'(1.5)=5.75`, so `x1=1.34782608695652`. At `x1=1.34782608695652`, `f(x1)≈0.1006821731` and `f'(x1)≈4.4499054820`, giving `x2≈1.32520039895`. Thus after two updates, the estimate is **1.32520** (five decimals). Calculate with the unrounded x1.

12. Different update rules: bisection halves brackets; Newton follows derivative-based tangent updates. Bisection has reliable convergence with a valid continuous sign-changing bracket; Newton often converges rapidly near a well-behaved root.

## D. Optimization

13. Variable w; objective minimize `(w−5)²`; feasible range `[1,3]`.
14. Unconstrained minimum w=5; constrained minimum w=3.
15. w=5 violates `w≤3`; best feasible value is w=3, giving `J(3)=(3−5)²=4`.
16. `J'(w)=2(w−5)`, `J''(w)=2>0` for every w → strictly convex.
