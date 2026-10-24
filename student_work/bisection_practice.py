
# Numerical Computing & Optimisation
# Practical Revision 01: Bisection Method


def f(x):
    return x**3 - x - 2


def bisection(func, a, b, tolerance=1e-6, max_iterations=100):
    """
    Approximate a root using the bisection method.

    Returns the estimated root and iteration history.
    """

    # Check that the interval is valid
    if a >= b:
        raise ValueError("The lower bound must be smaller than the upper bound.")

    if tolerance <= 0 or max_iterations < 1:
        raise ValueError("Tolerance and maximum iterations must be positive.")

    fa = func(a)
    fb = func(b)

    # An endpoint may already be a root
    if fa == 0:
        return a, []
    if fb == 0:
        return b, []

    # The endpoints must have opposite signs
    if fa * fb > 0:
        raise ValueError("The interval must bracket a root.")

    history = []

    for iteration in range(1, max_iterations + 1):

        # Step 1: Find the midpoint
        c = (a + b) / 2

        # Step 2: Evaluate the function
        fc = func(c)

        # Step 3: Record our calculation
        history.append((iteration, a, b, c, fc))

        # Step 4: Check whether we are accurate enough
        if abs(fc) < tolerance or (b - a) / 2 < tolerance:
            return c, history

        # Step 5: Keep the interval containing the root
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc

    # Return the latest approximation if we reach the limit
    return c, history


if __name__ == "__main__":

    root, history = bisection(f, 1, 2)

    print("BISECTION METHOD RESULTS")
    print("-" * 70)

    print(f"{'Iter':<8}{'a':<12}{'b':<12}{'Midpoint':<16}{'f(c)':<16}")

    for iteration, a, b, c, fc in history:
        print(f"{iteration:<8}{a:<12.6f}{b:<12.6f}"
              f"{c:<16.6f}{fc:<16.6f}")

    print("-" * 70)
    print(f"Estimated root: {root:.8f}")
    print(f"Iterations used: {len(history)}")
