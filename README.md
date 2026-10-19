# Numerical Computing & Optimisation — Revision Lab

A **study-first, code-backed** revision project for Weeks 1–4 of Numerical Computing and Optimisation. Topics follow the supplied *Weeks 1–4 Test Revision Guide* and the themes of the October 2026 semester test. **The examples and practice questions in this repository are newly authored**, not a copy of the scanned examination paper.

## What this repository demonstrates

- Mathematical definitions, formulas, assumptions and failure conditions.
- Step-by-step worked examples and examination-style explanations.
- Testable Python implementations of the numerical algorithms.
- New exam-style questions with a separate answer key.
- A record of genuine learning, fixes and implementation progress.

## Priority revision order

1. **High-mark exam calculations:** bisection, Newton–Raphson, constrained optimization.
2. **Short-answer calculations:** MSE, simultaneous equations, central differences, interpolation.
3. **Concepts:** rounding vs truncation, conditioning vs stability, convexity, secant, L2.
4. **Deeper Week 2–4 skills:** Gaussian elimination, least squares, QR/SVD, gradient checking and integration.

## Getting started

Requires Python 3.10+.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Windows Git Bash:
# source .venv/Scripts/activate
python -m pip install -e ".[dev]"
python -m pytest -q
python -m numerical_revision.demo
```

If you want to use Colab, open `notebooks/01_exam_walkthrough.ipynb`. The notebook's self-contained cells work without installing this repository; the package-based code and tests are for local VS Code/GitHub use.

## Study materials

| Topic | Teaching notes | Core code |
|---|---|---|
| Week 1 — error analysis and regression | [Week 1](notes/week01-errors-regression.md) | `absolute_error`, `mse`, `rmse` |
| Week 2 — root-finding, linear systems | [Week 2](notes/week02-roots-linear-systems.md) | `bisection`, `newton`, `secant`, `solve_system` |
| Week 3 — interpolation and calculus | [Week 3](notes/week03-interpolation-calculus.md) | `linear_interpolate`, `central_difference`, `simpson_one_third` |
| Week 4 — optimization | [Week 4](notes/week04-optimization.md) | `quadratic_loss`, `constrained_quadratic_minimum` |

Work on [exam practice](practice/remedial-mock.md) first, then check the [separate answer key](solutions/remedial-mock-answers.md). Update [study progress](progress/REVISION_LOG.md) honestly after each session.

## Working with GitHub

See [GitHub workflow](notes/github-workflow.md) for initializing the repository, pushing it, and making meaningful commits. Do **not** upload private academic credentials, other students' personal information, or the scanned test paper without permission.

### Commit examples

- `docs: explain rounding and truncation with examples`
- `feat: implement bisection with interval history`
- `test: cover zero derivative in Newton method`
- `study: record mistakes and corrections for interpolation`

> Aim for quality and traceable learning—not artificial contribution counts, copied code you cannot explain, or backdated commits.

## Attribution

The syllabus organization is adapted for personal study from the course materials provided by the student. Mathematical definitions and formulas are standard. **The initial notes, examples, practice questions and code scaffold were drafted with AI assistance and then checked using automated tests**; review, correct and extend them with your own understanding before claiming work as your own. Use and share in line with your institution's academic-integrity rules.
