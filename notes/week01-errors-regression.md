# Week 1 — Numerical Reliability, Errors and Regression

**Definitions → worked example → interpretation → common mistakes.**

## Error measurements

For true value `t` and approximation `a`:

- Absolute error: `|t-a|`.
- Relative error: `|t-a|/|t|`, defined for `t != 0`.
- Percentage error: `100 × relative error`.

**Worked example:** true value 80, approximation 76.8.
Absolute error = 3.2, relative error = 3.2/80 = 0.04, percentage error = 4%.

**Explain:** relative error allows comparisons across quantities of different magnitudes. Its usual definition is undefined when the true value is zero.

## Sources of numerical error

| Type | Exam-ready definition | Example |
|---|---|---|
| Rounding | Inexact representation or arithmetic due to finite precision | Storing π as 3.14 |
| Truncation | Replacing an exact mathematical process with a finite approximation | Finite-difference derivative |
| Accumulated | Small errors build up across successive operations | Many repeated rounded additions |
| Measurement | Observed data differs from the measured quantity | Miscalibrated sensor |
| Model | Mathematical model inadequately describes reality | Predicting marks from one feature only |

**Floating-point example:** `0.1 + 0.2 == 0.3` can be false in Python. Use suitable relative/absolute tolerances (`numpy.isclose`) rather than testing exact equality for approximate results.

**Numerical differentiation warning:** decreasing h initially reduces truncation error, but extremely small h magnifies floating-point cancellation and rounding effects.

## Numerical reliability

- **Conditioning** describes sensitivity of the *problem* to input perturbations.
- **Stability** describes how the *algorithm* propagates computational errors.
- **Convergence** means successive approximations approach a target; it does not mean the exact solution has already been reached.
- **Computational cost** usually considers time and memory.
- **Vectorization** uses optimized array operations instead of explicit Python loops; often faster but not automatically O(1).

## Regression loss

For `ŷᵢ = w xᵢ + b`, residual `rᵢ = yᵢ - ŷᵢ`, MSE `= (Σ rᵢ²)/n`, RMSE `= sqrt(MSE)`.

**Worked example:** actual `[5,7,9]`, predicted `[4,8,7]`.
Residuals `[1,-1,2]`, squared residuals `[1,1,4]`, MSE `(1+1+4)/3 = 2`.

**Exam tip:** write the formula and substitution, not just the final answer. Squaring the *sum* of residuals is **not** MSE.

## Check yourself

1. Define truncation error and give a derivative approximation example.
2. Explain the difference between conditioning and stability.
3. Why does a small residual alone not identify the source of an inaccurate prediction?
4. Derive RMSE from the worked-example MSE.
