#!/usr/bin/python3
"""The Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle with\
         private instance attributes"""
    pass

    def __init__(self, size, x=0, y=0, id=None):
        """Class contructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method str"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """public method update"""
        if len(args) > 0 and args is not None:
            idx = len(args)
            if idx >= 1:
                self.id = args[0]
            if idx >= 2:
                self.size = args[1]
            if idx >= 3:
                self.x = args[2]
            if idx >= 4:
                self.y = args[3]
        else:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """public method to_dictonary"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}

    @property
    def size(self):
        """Getter for the private size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the private size attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
