#!/usr/bin/python3
"""
This module contains a function find_peak which
finds a peak element in a list of integers.
"""
import sys


def find_peak(list_of_integers):
    """
    Find a peak element in a list of integers using binary search.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int: The peak element in the list
    """
    if not list_of_integers:
        return None

    m = list_of_integers
    peak = m[0]

    while len(m):
        index = len(m) // 2
        if m[index] > peak:
            peak = m[index]
            m = m[index:]
        else:
            m = m[:index]
    return peak
