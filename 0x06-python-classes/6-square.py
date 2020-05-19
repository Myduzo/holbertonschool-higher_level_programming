#!/usr/bin/python3
"""insert class"""


class Square:
    """instance attribute"""
    pass

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size"""
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """Public instance method area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method my_print"""
        area = self.__size ** 2
        pos = self.__position
        count = 0
        x = 0
        y = 0
        if self.__size == 0 or pos[1] != 0:
            print()
        while count < area:
            if (x == self.__size):
                print()
                x = 0
                y = 0
            if pos[0]:
                while y < pos[0]:
                    print("_", end="")
                    y += 1
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

    @property
    def position(self):
        """A method which is used for getting a value
         is decorated with @property"""
        return self.__position

    @position.setter
    def position(self, value):
        """A method which is used for setting a value
         is decorated with @position.setter"""
        if not((isinstance(value[0])) and (isinstance(value[1]))):
            print("position must be a tuple of 2 positive integers")
        if value[1] > 0:
            print(" ")
        self.__position = value
        return self.__position
