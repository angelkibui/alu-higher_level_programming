#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Replicate the behavior of the provided bytecode."""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
