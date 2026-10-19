# Week 4 — Optimization Formulation, Constraints and Convexity

## Formulate the problem before solving

An optimization problem specifies:

1. **Decision variable:** what the solver can change (e.g. parameter `w`).
2. **Objective:** scalar quantity to minimize or maximize, e.g. loss `J(w)`.
3. **Constraints:** equalities, inequalities or bounds that define feasible values.

**Worked example (same topic as the previous exam):** minimize `J(w)=(w-3)²`, subject to `0≤w≤2`.

- Unconstrained: `J'(w)=2(w-3)=0` → `w=3`, loss 0.
- Feasible region: `[0,2]`; 3 is not feasible.
- Constrained minimizer: `w=2`, loss 1, because this is the permitted value closest to 3.
- Convexity: `J''(w)=2>0`, so J is strictly convex; the unconstrained minimizer is unique and global.

**Exam mistake to avoid:** `J'(w)=0` only identifies a stationary point, not necessarily a minimum. For `f(x)=-x²`, the stationary point at x=0 is a maximum.

## Chain rule refresher

For `f(x)=[u(x)]^n`:

`f'(x)=n[u(x)]^(n−1)u'(x)`.

Example: `f(x)=(3x-2)²`; outer derivative `2(3x-2)`, inner derivative 3, final `6(3x-2)`.

## Convexity and feasibility

For twice-differentiable scalar f, `f''(x)≥0` throughout an interval implies convexity there; `f''(x)>0` implies strict convexity. For differentiable convex objectives over convex feasible regions, local minima are global minima.

A **feasible** candidate obeys every constraint; an **infeasible** candidate violates at least one.

## Penalties and regularization

- **Hard constraint:** enforce `g(w)≤0` directly.
- **Penalty method:** add a cost such as `ρ·max(0,g(w))²` for violations; a finite penalty may allow some violations.
- **L1:** add `α Σ |wᵢ|`; can promote sparse coefficients.
- **L2:** add `α Σ wᵢ²`; discourages large coefficients. **It does not repair missing observations.**

The regularization coefficient `α≥0` controls strength. Stronger regularization trades fitting training data against complexity; its effect must be evaluated on appropriate validation data.

## Lagrange multipliers: equality constraints

To minimize `f(x,y)` subject to `h(x,y)=0`, define `L(x,y,λ)=f(x,y)+λh(x,y)` and solve `∂L/∂x=0`, `∂L/∂y=0` and `h=0` for candidates. Then check feasibility and the objective; these stationary equations alone do not rule out every maximum/saddle in general.

## Check yourself

1. Explain why a constrained optimum may occur at a boundary where J' is nonzero.
2. Write the derivative of `(2w+1)³` using the chain rule.
3. Why is `w=3` infeasible under `0≤w≤2`?
4. What do L1 and L2 regularization discourage?
5. Why must a solver result be checked against the constraints?
