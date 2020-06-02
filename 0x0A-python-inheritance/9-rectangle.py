#!/usr/bin/python3
"""base geometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry class"""
    pass

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """public instance method"""
        return self.__width * self.__height

    def print(self):
        """print method"""
        print(self)

    def __str__(self):
        """string method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
