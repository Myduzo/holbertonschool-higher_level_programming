#!/usr/bin/python3
"""
Tests can be found in tests/ and can be run using
    python3 -m doctest ./tests/*
    or python3 -m -v doctest ./tests/*
"""


def matrix_divided(matrix, div):
    """ args : matrix and div
        return: new_matrix
    """
    if type(matrix) not in [list, int, float]:
        raise TypeError("matrix must be a matrix \
    (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    in_mat = []
    result = 0
    x = 0
    for x in matrix:
        if len(x) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            x = y / div
            result = float("{:.2f}".format(x))
            in_mat.append(result)
            result = 0
            x = 0
        new_matrix.append(in_mat)
        in_mat = []
    return new_matrix
