#!/usr/bin/python3
"""
Tests can be found in tests/ and can be run using
    python3 -m doctest ./tests/*
    or python3 -m -v doctest ./tests/*
"""


def print_square(size):
    """ 
    args : size
    return: #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    
    square = size ** 2
    count = 0
    x = 0
    while count < square:
        if x == size:
            print()
            x = 0
        print("#", end="")
        count +=1
        x +=1
    print()
