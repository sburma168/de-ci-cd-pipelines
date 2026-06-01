# ------------------------------------------------------------
# test_calculator.py — Unit tests for our calculator app
# pytest will automatically find and run these tests.
# Each function that starts with "test_" is one test case.
# ------------------------------------------------------------

import pytest
from src.calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    # This checks that our app raises an error when dividing by zero
    with pytest.raises(ValueError):
        divide(5, 0)