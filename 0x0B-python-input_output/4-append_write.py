#!/usr/bin/python3
"""append write"""


def append_write(filename="", text=""):
    """appends string at the end of the text"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
