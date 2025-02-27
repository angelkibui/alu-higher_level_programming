#!/usr/bin/python3
import sys


def add_arguments(args):
    """Add all arguments and return the result."""
    total = 0
    for arg in args:
        total += int(arg)
    return total


if __name__ == "__main__":
    # Skip the first argument (script name) and add the rest
    result = add_arguments(sys.argv[1:])
    print(result)
