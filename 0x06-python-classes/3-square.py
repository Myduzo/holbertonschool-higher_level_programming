#!/usr/bin/python3
"""insert class"""


class Square:
    """instance attribute"""
    pass

    def __init__(self, size=0):
        """init method"""
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area method"""
        return self.__size ** 2
