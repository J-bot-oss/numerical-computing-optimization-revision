
import pytest

from student_work.bisection_practice import bisection, f


def test_bisection_finds_correct_root():
    root, history = bisection(f, 1, 2)

    assert root == pytest.approx(1.5213797, abs=1e-6)
    assert len(history) > 0


def test_first_three_midpoints():
    root, history = bisection(
        f, 1, 2, tolerance=1e-12, max_iterations=3
    )

    midpoints = [record[3] for record in history]

    assert midpoints == [1.5, 1.75, 1.625]


def test_invalid_interval():
    with pytest.raises(ValueError):
        bisection(f, 2, 1)


def test_interval_without_sign_change():
    with pytest.raises(ValueError):
        bisection(f, 3, 4)
