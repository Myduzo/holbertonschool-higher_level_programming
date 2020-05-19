#!/usr/bin/python3
"""insert class"""


class Square:
    """instance attribute"""
    pass

    def __init__(self, size=0):
        """Instantiation with optional size"""
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method my_print"""
        area = self.__size ** 2
        count = 0
        x = 0
        while count < area:
            if (x == self.__size):
                print()
                x = 0
            print("#", end="")
            count += 1
            x += 1
        print()

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
