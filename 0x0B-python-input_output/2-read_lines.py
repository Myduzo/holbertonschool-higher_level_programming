#!/usr/bin/python3
"""read lines"""


def read_lines(filename="", nb_lines=0):
    """function that read lines"""
    with open(filename, "r") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for num_line in range(nb_lines):
                print(f.readline(), end="")
