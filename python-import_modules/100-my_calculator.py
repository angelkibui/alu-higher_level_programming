#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculate(a, operator, b):
    """Perform the calculation based on the operator."""
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)
    elif operator == '/':
        return div(a, b)
    else:
        return None


if __name__ == "__main__":
    # Check if the number of arguments is exactly 3
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Extract arguments
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Perform the calculation
    result = calculate(a, operator, b)

    # Handle invalid operators
    if result is None:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Print the result
    print("{} {} {} = {}".format(a, operator, b, result))
