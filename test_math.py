import pytest
from math_utils import add, multiply, subtract, divide


def test_add():
         # This will fail because add() uses subtraction
    assert add(2, 3) == 5
    assert add(10, 5) == 15
    assert add(-1, 1) == 0


def test_multiply():
         # This will fail because multiply() uses addition
    assert multiply(3, 4) == 12
    assert multiply(5, 5) == 25
    assert multiply(0, 10) == 0


def test_subtract():
         # This should pass
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5


def test_divide():
         # This will fail due to syntax error in divide()
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3


def test_power():
         # This will fail because power() uses multiplication
    from math_utils import power
    assert power(2, 3) == 8
    assert power(5, 2) == 25