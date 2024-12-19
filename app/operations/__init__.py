def add(a: float, b: float) -> float:
    """
    Returns:
    float: The result of adding `a` and `b`.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Returns:
    float: The result of subtracting `b` from `a`.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Returns:
    float: The result of multiplying `a` by `b`.
    """
    return a * b 

def divide(a: float, b: float) -> float:
    """
    Returns:
    float: The result of dividing `a` by `b`.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")  # Guard against division by zero
    return a / b
