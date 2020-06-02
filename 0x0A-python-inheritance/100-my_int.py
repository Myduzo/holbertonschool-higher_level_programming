#!/usr/bin/python3
"""MyInt"""

Rectangle = __import__("9-rectangle").Rectangle


class MyInt(int):
    """MyInt class that inherits from int"""
    pass

    def __eq__(self, other):
        """function that inverts == sign to !="""
        return self != other
