#!/usr/bin/env python3
magic_calculation = __import__('102-magic_calculation').magic_calculation

print(magic_calculation(1, 2, 3))  # a < b → return c
print(magic_calculation(3, 2, 1))  # c > b → return a + b
print(magic_calculation(3, 2, 3))  # c <= b → return (a * b) - c
