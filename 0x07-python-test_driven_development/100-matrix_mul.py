#!/usr/bin/python3
"""
This module contains the function called
``matrix_mul`` that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices
    Args:
        m_a (matrix): is a list of lists of integers or floats
        m_b (matrix): is a list of lists of integers or floats
    Raises:
        TypeError: if m_a or m_b is not a list of lists,
                   if element of those list of lists in not an integer or a
                   float, and if m_a or m_b is not a rectangle (all `rows`
                   should be of the same size)

        ValueError: if m_a or m_b is empty or if the number of columns of the
                    first matrix is not equal to the number of rows of the
                    second matrix meaning they can't be multiplied
    """
    if isinstance(m_a, list) is not True:
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list) is not True:
        raise TypeError("m_b must be a list")
    if m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if all(type(elem) is list for elem in m_a) is False:
        raise TypeError("m_a must be a list of lists")
    if all(type(var) is list for var in m_b) is False:
        raise TypeError("m_b must be a list of lists")
    for i in range(len(m_b)):
        if len(m_b[0]) != len(m_b[i]):
            raise TypeError("each row of m_b must be of the same size")
    for k in range(len(m_a)):
        if len(m_a[0]) != len(m_a[k]):
            raise TypeError("each row of m_a must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    tmp = []
    mul_list = []
    trans = [[m_b[j][k] for j in range(len(m_b))]for k in range(len(m_b[0]))]
    n = len(trans[0])
    for a in range(len(m_a)):
        for b in range(len(trans)):
            sum = 0
            for c in range(n):
                if type(m_a[a][c]) not in [int, float]:
                    raise TypeError("m_a should contain only integers or"
                                    + " floats")
                if type(trans[b][c]) not in [int, float]:
                    raise TypeError("m_b should contain only integers or"
                                    + " floats")
                sum += m_a[a][c] * trans[b][c]
            tmp.append(sum)
        mul_list.append(tmp)
        tmp = []
    return mul_list
