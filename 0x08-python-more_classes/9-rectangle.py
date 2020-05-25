#!/usr/bin/python3
"""Empty class"""


class Rectangle:
    """A class name Rectangle"""
    pass
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def area(self):
        """Public instance method area"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Public instance method perimeter"""
        if (self.__width == 0) or (self.__height == 0):
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

    @property
    def height(self):
        """A method which is used for getting a value
         is decorated with @property"""
        return self.__height

    @height.setter
    def height(self, value):
        """A method which is used for getting a value
         is decorated with @height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def __str__(self):
        """method str"""
        x = 0
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        for x in range(self.__height):
            rec += str(Rectangle.print_symbol) * self.__width
            if x != self.__height - 1:
                rec += "\n"
            else:
                rec += ""
        return rec

    def __repr__(self):
        """method repr"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """method del"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
