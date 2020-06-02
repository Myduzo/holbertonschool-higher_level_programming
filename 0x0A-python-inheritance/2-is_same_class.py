#!/usr/bin/python3
"""is same class"""
def is_same_class(obj, a_class):
    """function that check if the obj is an instance of the class"""
    return issubclass(a_class, type(obj))
