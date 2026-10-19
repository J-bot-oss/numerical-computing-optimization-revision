"""Run with: python -m numerical_revision.demo"""
from .core import bisection, newton, residuals, mse, central_difference, constrained_quadratic_minimum


def f(x):
    return x**3 - x - 2


def df(x):
    return 3*x*x - 1


def main():
    print("Revision Lab — sample numerical calculations")
    actual, predicted = [5, 7, 9], [4, 8, 7]
    print("Residuals:", residuals(actual, predicted))
    print("MSE:", mse(actual, predicted))
    print("\nBisection: f(x) = x^3 - x - 2")
    for row in bisection(f, 1, 2, 3):
        print(f"n={row['n']}  [{row['a']:.4f}, {row['b']:.4f}]  "
              f"c={row['c']:.4f}  f(c)={row['f_c']:.4f}  "
              f"new bracket=[{row['new_a']:.4f}, {row['new_b']:.4f}]")
    print("\nNewton:")
    for row in newton(f, df, 1.5, 2):
        print(f"n={row['n']}  x={row['x']:.5f}  f(x)={row['f_x']:.5f}  "
              f"f'(x)={row['df_x']:.5f}  next={row['next_x']:.5f}")
    print("\nCentral difference x^3 at 2, h=0.5:", central_difference(lambda x: x**3, 2, .5))
    print("Constrained minimum of (w-3)^2 on [0,2]:", constrained_quadratic_minimum(3,0,2))


if __name__ == "__main__":
    main()
