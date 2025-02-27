#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Check if the number of arguments is exactly 3
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])  # First number
    operator = argv[2]  # Operator
    b = int(argv[3])  # Second number

    # Dictionary to map operators to functions
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    # Check if the operator is valid
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # Perform the operation and print the result
    result = operators[operator](a, b)
    print(f"{a} {operator} {b} = {result}")
