#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """function that read and prints file text"""
    with open(filename, "r") as f:
        print(f.read(), end="")
