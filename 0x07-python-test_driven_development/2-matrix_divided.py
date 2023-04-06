#!/usr/bin/python3
"""
This module calculates the ratio of each element in the matrix
by a given divisor

"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and round to 2 decimal places
    Args:
        matrix (list): a list of integer or float
        div (int or float): an integer or float variable
    Raises:
        TypeError: if matrix is not a list of int or float
                   and if the row of the matrix do not have the same size
        ZeroDivisionError:
                   if div equals to 0
    Return:
        a new matrix
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    tmp = []
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            n = matrix[i][k]
            if type(n) is not int and type(n) is not float:
                msg = "matrix must be a matrix (list of lists)"
                raise TypeError(msg + " of integers/floats")
            m = len(matrix[0])
            if len(matrix[i]) != m:
                msg1 = "Each row of the matrix must have the "
                raise TypeError(msg1 + "same size")

            result = round((matrix[i][k] / div), 2)
            tmp.append(result)
        new_matrix.append(tmp)
        tmp = []

    return new_matrix
