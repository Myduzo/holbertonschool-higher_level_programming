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

    @property
    def size(self):
        """A method which is used for getting a value
         is decorated with @property"""
        return self.__size

    @size.setter
    def size(self, value):
        """A method which is used for setting a value
         is decorated with @size.setter"""
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size
