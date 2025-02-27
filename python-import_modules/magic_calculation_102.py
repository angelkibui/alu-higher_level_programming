#!/usr/bin/env python3

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print("Testing magic_calculation function")
    from _102_magic_calculation import magic_calculation
    result1 = magic_calculation(2, 3)
    result2 = magic_calculation(10, 5)
    print(f"magic_calculation(2, 3) = {result1}")
    print(f"magic_calculation(10, 5) = {result2}")
