
# Practical Revision 02: Gradient Descent
# Week 5 - Optimization Methods


def loss(w):
    """Calculate J(w) = (w - 3)^2."""
    return (w - 3) ** 2


def gradient(w):
    """Calculate the derivative of the loss."""
    return 2 * (w - 3)


def gradient_descent(initial_w=0.0, learning_rate=0.25, iterations=5):
    """Perform gradient descent and record each iteration."""

    if learning_rate <= 0:
        raise ValueError("Learning rate must be positive.")

    if iterations < 1:
        raise ValueError("Iterations must be positive.")

    w = initial_w
    history = [(0, w, loss(w))]

    for step in range(1, iterations + 1):
        g = gradient(w)
        w = w - learning_rate * g
        history.append((step, w, loss(w)))

    return history


if __name__ == "__main__":
    results = gradient_descent()

    print("Iteration | Weight | Loss")
    print("-" * 35)

    for step, w, current_loss in results:
        print(f"{step:^9} | {w:^8.5f} | {current_loss:.6f}")
