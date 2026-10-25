
import pytest

from student_work.gradient_descent_practice import (
    loss,
    gradient,
    gradient_descent,
)


def test_loss_and_gradient():
    assert loss(0) == 9
    assert gradient(0) == -6
    assert loss(3) == 0


def test_first_two_updates():
    history = gradient_descent(iterations=2)

    assert history[1][1] == pytest.approx(1.5)
    assert history[2][1] == pytest.approx(2.25)


def test_loss_decreases():
    history = gradient_descent(iterations=5)
    losses = [record[2] for record in history]

    assert all(
        losses[i + 1] < losses[i]
        for i in range(len(losses) - 1)
    )


def test_invalid_learning_rate():
    with pytest.raises(ValueError):
        gradient_descent(learning_rate=0)
