#!/usr/bin/python3
"""MyInt"""

Rectangle = __import__("9-rectangle").Rectangle


class MyInt(int):
    """MyInt class that inherits from int"""
    pass

    def my_invert(self, number):
        """function that inverts == sign to !="""
        return (False if self is number else True)
