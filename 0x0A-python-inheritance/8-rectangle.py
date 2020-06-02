#!/usr/bin/python3
"""Rectangle"""

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
