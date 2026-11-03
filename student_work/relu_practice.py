"""ReLU activation and derivative practice for neural networks."""


def relu(x):
    """Return the ReLU activation."""
    return max(0, x)


def relu_derivative(x):
    """Return the ReLU derivative, using zero at x=0."""
    return 1 if x > 0 else 0


if __name__ == "__main__":
    for x in [-3, -1, 0, 1, 3]:
        print(
            f"x={x:>2} | "
            f"ReLU={relu(x):>2} | "
            f"Derivative={relu_derivative(x)}"
        )
