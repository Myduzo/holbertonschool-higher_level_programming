#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base with\
         private instance attributes"""
    pass

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class contructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """Public method area"""
        return self.width * self.height

    def display(self):
        """Public method display"""
        for i in range(self.y):
            print()
        for x in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for y in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """__str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """Public method update"""
        if len(args) > 0 and args is not None:
            idx = len(args)
            if idx >= 1:
                self.id = args[0]
            if idx >= 2:
                self.width = args[1]
            if idx >= 3:
                self.height = args[2]
            if idx >= 4:
                self.x = args[3]
            if idx >= 5:
                self.y = args[4]
        else:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """public method to_dictionary"""
        return {"x": self.x, "y": self.y, "id": self.id, 
                "height": self.height, "width": self.width}

    @property
    def width(self):
        """Getter for the private width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the private x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the private x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the private y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the private y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
