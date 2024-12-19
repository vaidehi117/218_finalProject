import pytest
from app.operations import addition, subtraction, multiplication, division 

# Test addition function
def test_addition():
    # Basic test case
    assert addition(2, 3) == 5
    # Test addition with negative numbers
    assert addition(-1, -1) == -2
    # Test addition with floats
    assert addition(2.5, 3.5) == 6.0
    # Test addition with zero
    assert addition(0, 5) == 5

# Test subtraction function
def test_subtraction():
    # Basic test case
    assert subtraction(5, 3) == 2
    # Test subtraction with negative numbers
    assert subtraction(-1, -1) == 0
    # Test subtraction with floats
    assert subtraction(5.5, 3.0) == 2.5
    # Test subtraction with zero
    assert subtraction(5, 0) == 5

# Test multiplication function
def test_multiplication():
    # Basic test case
    assert multiplication(2, 3) == 6
    # Test multiplication with a negative number
    assert multiplication(-2, 3) == -6
    # Test multiplication with floats
    assert multiplication(2.5, 2) == 5.0
    # Test multiplication by zero
    assert multiplication(5, 0) == 0

# Test division function
def test_division():
    # Basic test case
    assert division(6, 3) == 2
    # Test division with floats
    assert division(5.5, 2) == 2.75
    # Test division by a negative number
    assert division(-6, 3) == -2
    # Edge case: Division by zero
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(5, 0)
