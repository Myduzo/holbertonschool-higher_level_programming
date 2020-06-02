#!/usr/bin/python3
"""inherits from"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of\
         a class that inherited dir or indir"""
    return isinstance(obj, a_class) and type(obj) is not a_class
