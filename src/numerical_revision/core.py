"""Numerical algorithms with clear contracts and classroom-sized examples.

These functions are instructional, not a replacement for production solvers.
"""

from __future__ import annotations
import math
from typing import Callable
import numpy as np


def absolute_error(true: float, approx: float) -> float:
    return abs(true - approx)


def relative_error(true: float, approx: float) -> float:
    if true == 0:
        raise ValueError("Relative error is undefined when the true value is zero")
    return absolute_error(true, approx) / abs(true)


def percentage_error(true: float, approx: float) -> float:
    return 100 * relative_error(true, approx)


def residuals(actual, predicted) -> np.ndarray:
    a = np.asarray(actual, dtype=float)
    p = np.asarray(predicted, dtype=float)
    if a.ndim != 1 or p.ndim != 1 or len(a) != len(p) or len(a) == 0:
        raise ValueError("Expected two nonempty, equally sized 1D sequences")
    return a - p


def mse(actual, predicted) -> float:
    r = residuals(actual, predicted)
    return float(np.mean(r ** 2))


def rmse(actual, predicted) -> float:
    return math.sqrt(mse(actual, predicted))


def _safe_eval(f: Callable[[float], float], x: float) -> float:
    value = float(f(x))
    if not math.isfinite(value):
        raise ValueError("Function returned a nonfinite value")
    return value


def bisection(f: Callable[[float], float], a: float, b: float, iterations: int = 3):
    """Return iteration history with starting bracket, midpoint, and updated bracket."""
    if not a < b or iterations < 1:
        raise ValueError("Require a < b and a positive iteration count")
    fa, fb = _safe_eval(f, a), _safe_eval(f, b)
    if fa * fb > 0:
        raise ValueError("Initial endpoints must bracket a sign change")
    if fa == 0 or fb == 0:
        return []  # A root is already at an endpoint.
    steps = []
    for k in range(1, iterations + 1):
        start_a, start_b = a, b
        c = (a + b) / 2
        fc = _safe_eval(f, c)
        if fc == 0:
            a = b = c
        elif fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
        steps.append({"n": k, "a": start_a, "b": start_b,
                      "c": c, "f_c": fc, "new_a": a, "new_b": b})
        if fc == 0:
            break
    return steps


def newton(f: Callable[[float], float], df: Callable[[float], float],
           x0: float, iterations: int = 2):
    if iterations < 1:
        raise ValueError("iterations must be positive")
    x = float(x0)
    steps = []
    for n in range(iterations):
        fx, dfx = _safe_eval(f, x), _safe_eval(df, x)
        if dfx == 0:
            raise ZeroDivisionError("Newton update undefined when derivative is zero")
        next_x = x - fx / dfx
        if not math.isfinite(next_x):
            raise ValueError("Newton update became nonfinite")
        steps.append({"n": n, "x": x, "f_x": fx, "df_x": dfx, "next_x": next_x})
        x = next_x
    return steps


def secant(f: Callable[[float], float], x0: float, x1: float,
           iterations: int = 2):
    if iterations < 1:
        raise ValueError("iterations must be positive")
    previous, current = float(x0), float(x1)
    result = []
    for n in range(iterations):
        fprev, fcurrent = _safe_eval(f, previous), _safe_eval(f, current)
        denominator = fcurrent - fprev
        if denominator == 0:
            raise ZeroDivisionError("Secant slope denominator is zero")
        next_x = current - fcurrent * (current - previous) / denominator
        if not math.isfinite(next_x):
            raise ValueError("Secant update became nonfinite")
        result.append({"n": n, "x_previous": previous, "x_current": current,
                       "next_x": next_x})
        previous, current = current, next_x
    return result


def linear_interpolate(x0: float, y0: float, x1: float, y1: float, x: float) -> float:
    if x0 == x1:
        raise ValueError("Distinct x values are required")
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)


def central_difference(f: Callable[[float], float], x: float, h: float) -> float:
    if h <= 0:
        raise ValueError("Step size h must be positive")
    return (f(x + h) - f(x - h)) / (2 * h)


def solve_system(A, b) -> np.ndarray:
    A, b = np.asarray(A, dtype=float), np.asarray(b, dtype=float)
    return np.linalg.solve(A, b)


def linear_residual(A, x, b) -> np.ndarray:
    return np.asarray(A, dtype=float) @ np.asarray(x, dtype=float) - np.asarray(b, dtype=float)


def matrix_condition_number(A) -> float:
    return float(np.linalg.cond(np.asarray(A, dtype=float)))


def least_squares_fit(X, y) -> np.ndarray:
    """Solve min ||X beta - y||^2 with a robust least-squares routine."""
    X, y = np.asarray(X, dtype=float), np.asarray(y, dtype=float)
    return np.linalg.lstsq(X, y, rcond=None)[0]


def composite_trapezoid(y_values, h: float) -> float:
    y = np.asarray(y_values, dtype=float)
    if y.ndim != 1 or len(y) < 2 or h <= 0:
        raise ValueError("Provide at least two samples with positive uniform spacing")
    return float(h * (y[0] / 2 + y[-1] / 2 + np.sum(y[1:-1])))


def simpson_one_third(y_values, h: float) -> float:
    y = np.asarray(y_values, dtype=float)
    if y.ndim != 1 or len(y) < 3 or (len(y) - 1) % 2 != 0 or h <= 0:
        raise ValueError("Simpson 1/3 needs an even number of equal subintervals")
    return float(h / 3 * (y[0] + y[-1] + 4 * sum(y[1:-1:2])
                          + 2 * sum(y[2:-1:2])))


def quadratic_loss(w: float, target: float = 3) -> float:
    return (w - target) ** 2


def constrained_quadratic_minimum(target: float, low: float, high: float) -> float:
    """For J(w)=(w-target)^2, the constrained minimizer is target clipped to [low, high]."""
    if low > high:
        raise ValueError("Empty feasible interval")
    return float(min(max(target, low), high))
