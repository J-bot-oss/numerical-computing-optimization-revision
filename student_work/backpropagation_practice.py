
# Practical 03: Backpropagation From Scratch
# Week 6 - Optimization Methods

def relu(z):
    """Return the ReLU activation."""
    return max(0, z)


def forward(x, w, b, target):
    """Calculate the prediction and squared-error loss."""
    z = w * x + b
    h = relu(z)
    loss = (h - target) ** 2

    return z, h, loss


def backward(x, z, h, target):
    """Calculate gradients manually using the chain rule."""
    dL_dh = 2 * (h - target)

    dh_dz = 1 if z > 0 else 0

    dz_dw = x
    dz_db = 1

    dL_dw = dL_dh * dh_dz * dz_dw
    dL_db = dL_dh * dh_dz * dz_db

    return dL_dw, dL_db


def main():
    x = 2
    w = 1.0
    b = 0.0
    target = 3
    learning_rate = 0.01

    # Forward propagation
    z, h, loss = forward(x, w, b, target)

    print("FORWARD PROPAGATION")
    print(f"z = {z}")
    print(f"h = {h}")
    print(f"Loss = {loss}")

    # Backpropagation
    dw, db = backward(x, z, h, target)

    print("\nBACKPROPAGATION")
    print(f"dL/dw = {dw}")
    print(f"dL/db = {db}")

    # Gradient descent update
    w = w - learning_rate * dw
    b = b - learning_rate * db

    print("\nUPDATED PARAMETERS")
    print(f"New weight = {w}")
    print(f"New bias = {b}")

    # Verify the loss decreased
    _, _, new_loss = forward(x, w, b, target)
    print(f"New loss = {new_loss}")

    assert new_loss < loss, "The loss should decrease."

    print("\nValidation passed!")


if __name__ == "__main__":
    main()
