#!/usr/bin/python3
"""
This module contains the function called
``lazy_matrix_mul`` that multiplies 2 matrices
using NumPy module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy module
    Args:
        m_a (matrix): list of lists of integers or floats
        m_b (matrix): list of lists of integers or floats
    Raises:
        TypeError: if element of list of lists in not an integer or a
                   float, and if m_a or m_b is not a rectangle (all `rows`
                   should be of the same size)

        ValueError: if m_a or m_b is empty or if the number of columns of the
                    first matrix is not equal to the number of rows of the
                    second matrix meaning they can't be multiplied
    """
    return (np.matmul(m_a, m_b))
