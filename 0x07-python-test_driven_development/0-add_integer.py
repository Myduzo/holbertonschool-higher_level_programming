#!/usr/bin/python3
"""
Tests can be found in tests/ and can be run using
    python3 -m doctest ./tests/*
    or python3 -m -v doctest ./tests/*
"""


def add_integer(a, b=98):
    """ args : a and b
        return: int (a + b)
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
