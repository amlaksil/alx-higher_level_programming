#!/usr/bin/python3
"""
This module contains a function find_peak which
finds a peak element in a list of integers.
"""


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

    start, end = 0, len(list_of_integers) - 1
    while start < end:
        mid = (start + end) // 2
        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_of_integers[start]
