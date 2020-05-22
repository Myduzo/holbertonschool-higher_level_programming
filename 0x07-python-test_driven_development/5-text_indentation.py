#!/usr/bin/python3
"""
Tests can be found in tests/ and can be run using
    python3 -m doctest ./tests/*
    or python3 -m -v doctest ./tests/*
"""


def text_indentation(text):
    """ 
    args : text
    return: text with 2 new lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if text == "":
        return print()
    text = text.replace(". ", ".")
    text = text.replace("? ", "?")
    text = text.replace(": ", ":")
    text = text.strip(" ")

    for x in text:
        if (x == "." or x == "?" or x == ":"):
            print("{:s}".format(x))
            print()
        else:
            print("{:s}".format(x), end="")
