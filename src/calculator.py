# ------------------------------------------------------------
# calculator.py — A simple calculator module
# This is the "app" we will use to learn CI/CD.
# It is intentionally simple so we can focus on the pipeline.
# ------------------------------------------------------------

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the result of a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the result of a divided by b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b