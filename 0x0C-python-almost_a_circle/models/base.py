#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """New Base class with private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method to_json_string returns \
            JSON representation"""
        if list_dictionaries is None or list_dictionaries == []:
                return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method save_to_file that saves \
            list of objects to a file"""
        l = []
        if list_objs is not None:
            for obj in list_objs:
                l.append(obj.to_dictionary())
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(Base.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string \
            representation"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes \
            already set"""
        if cls.__name__ == "Square":
            dummy = cls(5)
        else:
            dummy = cls(5, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instance"""
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                conv = cls.from_json_string(f.read())
        except Exception:
            return []
        return [cls.create(**data) for data in conv]
