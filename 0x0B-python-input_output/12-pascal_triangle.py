#!/usr/bin/python3
""" defines a function that returns a list of lists
of integers representing the pascal's triangle of n"""


def pascal_triangle(n):
    """ a function returns pascals triangle representation list """
    if n <= 0:
        return []
    tr = []
    for i in range(n):
        tr.append([])
        for j in range(i + 1):
            tr[i].append(1)

    for i in range(2, n):
        for j in range(1, len(tr[i]) - 1):
            tr[i][j] = tr[i - 1][j - 1] + tr[i - 1][j]

    return tr
