import math

def factorial(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

def power(x, base):
    if base < 0:
        raise ValueError("Base should be non-negative")
    if base == 0:
        return 1
    return x * power(x, base - 1)

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot find square root of a negative number")
    return math.sqrt(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Log is undefined for x <= 0")
    return math.log(x)