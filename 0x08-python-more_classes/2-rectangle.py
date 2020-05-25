#!/usr/bin/python3
"""Empty class"""


class Rectangle:
    """A class name Rectangle"""
    pass

    def __init__(self, width=0, height=0):
        """Instantiation with optional width"""
        if not isinstance(width, int):
            raise TypeError("width must be integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def area(self):
        """Public instance method area"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Public instance method perimeter"""
        if (self.__width is 0) or (self.__height is 0):
            return 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    @property
    def width(self):
        """A method which is used for getting a value
         is decorated with @property"""
        return self.__width

    @width.setter
    def width(self, value):
        """A method which is used for getting a value
         is decorated with @width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value
        return value

    @property
    def height(self):
        """A method which is used for getting a value
         is decorated with @property"""

    @height.setter
    def height(self, value):
        """A method which is used for getting a value
         is decorated with @height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
        return value
