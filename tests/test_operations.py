import pytest
from app.operations import add, subtract, multiply, divide

# Test addition function
def test_addition():
    # Basic test case
    assert add(2, 3) == 5
    # Test add with negative numbers
    assert add(-1, -1) == -2
    # Test addition with floats
    assert add(2.5, 3.5) == 6.0
    # Test addition with zero
    assert add(0, 5) == 5

# Test subtraction function
def test_subtraction():
    # Basic test case
    assert subtract(5, 3) == 2
    # Test subtraction with negative numbers
    assert subtract(-1, -1) == 0
    # Test subtraction with floats
    assert subtract(5.5, 3.0) == 2.5
    # Test subtraction with zero
    assert subtract(5, 0) == 5

# Test multiplication function
def test_multiplication():
    # Basic test case
    assert multiply(2, 3) == 6
    # Test multiplication with a negative number
    assert multiply(-2, 3) == -6
    # Test multiplication with floats
    assert multiply(2.5, 2) == 5.0
    # Test multiplication by zero
    assert multiply(5, 0) == 0

# Test division function
def test_division():
    # Basic test case
    assert divide(6, 3) == 2
    # Test division with floats
    assert divide(5.5, 2) == 2.75
    # Test division by a negative number
    assert divide(-6, 3) == -2
    # Edge case: Division by zero
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        divide(5, 0)
