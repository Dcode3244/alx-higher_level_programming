#!/usr/bin/python3
"""
my matrix_divide module
divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """ divides all elements of a matrix
    Args:
        matrix (list): list containing list of numbers
        div (int, float): the number dividing the matrix
    """
    new = []
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for li in matrix:
        if not isinstance(li, list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        new.append([])
        for num in li:
            if (not isinstance(num, int) and
                    not isinstance(num, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    if len(matrix) > 1:
        for i in range(len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must "
                                "have the same size")
    if (not isinstance(div, int) and
            not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new[i].append(round(matrix[i][j] / div, 2))
    return new
