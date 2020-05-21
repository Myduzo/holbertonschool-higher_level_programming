#!/usr/bin/python3
"""
Tests can be found in tests/ and can be run using
    python3 -m doctest ./tests/*
    or python3 -m -v doctest ./tests/*
"""


def say_my_name(first_name, last_name=""):
    """ 
    args : first_name and last_name
    return: str
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    return print("My name is {:s} {:s}".format(first_name, last_name))
