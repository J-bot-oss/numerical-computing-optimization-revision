import math
import numpy as np
import pytest

from numerical_revision.core import (
    absolute_error, relative_error, percentage_error, residuals, mse, rmse,
    bisection, newton, secant, linear_interpolate, central_difference,
    solve_system, linear_residual, matrix_condition_number, least_squares_fit,
    composite_trapezoid, simpson_one_third, quadratic_loss,
    constrained_quadratic_minimum,
)


def test_error_measures():
    assert absolute_error(25, 23) == 2
    assert relative_error(25, 23) == pytest.approx(0.08)
    assert percentage_error(25, 23) == pytest.approx(8)
    with pytest.raises(ValueError):
        relative_error(0, 0.01)


def test_residuals_mse_rmse():
    assert residuals([5, 7, 9], [4, 8, 7]).tolist() == [1, -1, 2]
    assert mse([5, 7, 9], [4, 8, 7]) == pytest.approx(2)
    assert rmse([5, 7, 9], [4, 8, 7]) == pytest.approx(math.sqrt(2))
    with pytest.raises(ValueError):
        mse([1, 2], [1])


def test_bisection_three_iterations():
    f = lambda x: x**3 - x - 2
    steps = bisection(f, 1, 2, 3)
    assert [s['c'] for s in steps] == [1.5, 1.75, 1.625]
    assert (steps[-1]['new_a'], steps[-1]['new_b']) == (1.5, 1.625)
    with pytest.raises(ValueError):
        bisection(f, 2, 3)


def test_bisection_exact_root_and_endpoint():
    assert bisection(lambda x: x - 2, 1, 3, 5)[-1]['c'] == 2
    assert bisection(lambda x: x - 2, 2, 3, 5) == []


def test_newton_two_iterations():
    f = lambda x: x*x - 9
    df = lambda x: 2*x
    steps = newton(f, df, 4, 2)
    assert steps[0]['next_x'] == pytest.approx(3.125)
    assert steps[1]['next_x'] == pytest.approx(3.0025)
    with pytest.raises(ZeroDivisionError):
        newton(f, df, 0)


def test_secant():
    steps = secant(lambda x: x*x - 4, 1, 3, 2)
    assert steps[0]['next_x'] == pytest.approx(1.75)
    assert steps[1]['next_x'] == pytest.approx(1.9473684210526316)
    with pytest.raises(ZeroDivisionError):
        secant(lambda x: x*x, -1, 1)


def test_interpolation_and_central_difference():
    assert linear_interpolate(1, 2, 3, 10, 2) == pytest.approx(6)
    assert central_difference(lambda x: x**3, 2, .5) == pytest.approx(12.25)
    with pytest.raises(ValueError):
        central_difference(lambda x: x, 2, 0)


def test_linear_system_and_residual():
    A, b = [[2, 1], [1, -1]], [7, 2]
    x = solve_system(A, b)
    assert x == pytest.approx([3, 1])
    assert np.linalg.norm(linear_residual(A, x, b)) < 1e-12
    assert matrix_condition_number(A) >= 1


def test_least_squares():
    X = [[1, 1], [2, 1], [3, 1]]
    y = [3, 5, 7]
    slope, intercept = least_squares_fit(X, y)
    assert slope == pytest.approx(2)
    assert intercept == pytest.approx(1)


def test_numerical_integration():
    # Integral of x from 0 to 2: exact 2; equally spaced samples [0,1,2].
    assert composite_trapezoid([0, 1, 2], 1) == pytest.approx(2)
    # Simpson integrates polynomials up to degree 3 exactly, here x^2 on [0,2].
    assert simpson_one_third([0, 1, 4], 1) == pytest.approx(8 / 3)
    with pytest.raises(ValueError):
        simpson_one_third([0, 1, 4, 9], 1)


def test_constrained_optimization():
    assert quadratic_loss(3) == 0
    assert constrained_quadratic_minimum(3, 0, 2) == 2
    assert constrained_quadratic_minimum(-2, 0, 2) == 0
    with pytest.raises(ValueError):
        constrained_quadratic_minimum(2, 3, 1)
