#!/usr/bin/python3
""" number of lines"""


def number_of_lines(filename=""):
    """function that returns number of lines"""
    count = 0
    with open(filename, "r") as f:
        for lines_count in f:
            count += 1
        return count
