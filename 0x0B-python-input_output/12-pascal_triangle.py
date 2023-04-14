#!/usr/bin/python3
"""
This module consists of a function called
`pascal_triangle` that returns a list of lists
of integers representing the Pascal's triangle
"""


def pascal_triangle(n):
    """Defines a pascal triangle
    Args:
        n (int): length (row) of triangle
    Return:
        a list of lists of integers
    """
    list_of_row = []
    if n <= 0:
        return list_of_row
    row = []
    c = 1
    for i in range(n):
        row[:] = ""
        for j in range(i + 1):
            if j == 0 or i == j:
                c = 1
            else:
                # c = c * (i - j + 1) // j
                c = list_of_row[i-1][j-1] + list_of_row[i-1][j]
            row.append(c)
        list_of_row.append(row[:])
    return list_of_row
