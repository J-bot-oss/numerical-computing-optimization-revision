"""Small, inspectable numerical algorithms for learning and revision."""

from .core import (
    absolute_error, relative_error, percentage_error, residuals, mse, rmse,
    bisection, newton, secant, linear_interpolate, central_difference,
    solve_system, linear_residual, least_squares_fit, matrix_condition_number,
    composite_trapezoid, simpson_one_third, quadratic_loss,
    constrained_quadratic_minimum,
)
