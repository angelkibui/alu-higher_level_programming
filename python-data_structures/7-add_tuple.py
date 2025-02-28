#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples."""
    # Extend tuples to ensure they have at least two elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Only take the first two elements from each tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
