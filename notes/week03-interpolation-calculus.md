# Week 3 — Interpolation, Numerical Differentiation and Integration

## Interpolation versus extrapolation

**Interpolation** estimates *inside* the range of given data; **extrapolation** estimates *outside* it, where assumed trends may break down.

Linear interpolation from `(x0,y0)` to `(x1,y1)`:

`y = y0 + (x-x0)/(x1-x0)·(y1-y0)`.

**Worked example:** `(1,2)`, `(3,10)`, estimate at `x=2`:
`y=2 + (2-1)/(3-1)·(10-2)=6`.

**Lagrange interpolation:** for distinct sample x coordinates, construct the unique degree ≤(n−1) polynomial through n observations:

`P(x)=Σᵢ yᵢ Lᵢ(x)`, where `Lᵢ(x)=Π_{j≠i}(x-xⱼ)/(xᵢ-xⱼ)`.

At each supplied node `xᵢ`, `P(xᵢ)=yᵢ`. High-degree polynomials can oscillate badly between points; outside-range extrapolation is risky.

## Numerical differentiation

- Forward: `f'(x) ≈ (f(x+h)-f(x))/h`.
- Backward: `f'(x) ≈ (f(x)-f(x-h))/h`.
- Central: `f'(x) ≈ (f(x+h)-f(x-h))/(2h)`.

**Worked example:** `f(x)=x³`, `x=2`, `h=0.5`.

`f(2.5)=15.625`, `f(1.5)=3.375`, so central derivative `(15.625-3.375)/1 = 12.25`. Analytical derivative `3x²` gives `12` at x=2; absolute error 0.25.

**Why not extremely small h?** Smaller h reduces truncation error up to a point; subtracting nearly equal floating-point values leads to cancellation and magnified round-off.

## Gradient checking in machine learning

An analytical gradient can be compared with a numerical central-difference estimate to detect implementation mistakes. Good agreement at selected points supports correctness but does not prove a global minimum or that every case works.

For a vector of model parameters, perturb one coordinate at a time to estimate each component of the gradient. Automatic differentiation computes derivatives by applying derivative rules through a computation graph rather than naively choosing finite differences.

## Numerical integration

With equally spaced samples `y0...yn` and `h=(b-a)/n`:

- Composite trapezoidal: `T = h [ (y0+yn)/2 + Σ interior yᵢ ]`.
- Composite Simpson 1/3: `S = (h/3)[y0+yn+4Σ odd interior yᵢ+2Σ even interior yᵢ]`.

**Important:** composite Simpson 1/3 requires an **even number of equal subintervals**.

**Worked example:** integrate `f(x)=x²` from 0 to 2, `h=1`, samples `[0,1,4]`.
Simpson result `1/3 [0+4+4(1)] = 8/3` (exact for this quadratic).

## Check yourself

1. Why is x=4 an extrapolation for data observed only from x=1 to x=3?
2. Write the central-difference formula and explain the choice of h.
3. State the even-subinterval requirement for Simpson 1/3.
4. Does a small numerical-vs-analytical gradient difference prove a global minimum?
