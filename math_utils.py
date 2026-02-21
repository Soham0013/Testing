def add(a, b):
    #BUG: Using subtraction instead of addition
    return a - b


def multiply(x, y):
    # BUG: Using addition instead of multiplication
    return x + y


def divide(a, b)
    # BUG: Missing colon
    if b == 0:
        return None
    return a / b


def subtract(x, y):
    # This one is correct
    return x - y


     # BUG: Indentation error - function body not indented
def modulo(a, b):
    return a % b


def power(base, exponent):
    # BUG: Using multiplication instead of power
    return base * exponent