#!/usr/bin/python3
"""Square"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    pass

    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def print(self):
        """print method"""
        print(self)

    def __str__(self):
        """string method"""
        return "[Square] {}/{}".format(self.__size, self.__size)
