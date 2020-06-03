#!/usr/bin/python3
"""save to json file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open(filename, mode="w") as f:
        return json.writes(my_obj)
