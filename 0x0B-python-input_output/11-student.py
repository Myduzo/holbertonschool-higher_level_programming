#!/usr/bin/python3
"""student"""


class Student:
    """A class name Student"""
    pass

    def __init__(self, first_name, last_name, age):
        """Initialisation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """public instance method"""
        return self.__dict__
