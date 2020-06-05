#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base with\
         private instance attributes"""
    pass

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class contructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """Getter for the private width attribute"""
            self.__width = width

        @width.setter
        def width(self):
            """Setter for the private width attribute"""
            return self.__width

        @property
        def height(self):
            """Getter for the private height attribute"""
            self.__height = height

        @height.setter
        def height(self):
            """Setter for the private height attribute"""
            return self.__height

        @property
        def x(self):
            """Getter for the private x attribute"""
            self.__x = x

        @x.setter
        def x(self):
            """Setter for the private x attribute"""
            return self.__x

        @property
        def y(self):
            """Getter for the private y attribute"""
            self.__y = y

        @y.setter
        def width(self):
            """Setter for the private y attribute"""
            return self.__y
