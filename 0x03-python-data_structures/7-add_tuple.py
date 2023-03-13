#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    n = len(tuple_a)
    m = len(tuple_b)
    if n < 2:
        if n == 0:
            tuple_a = (0, 0)
        elif n == 1:
            tuple_a = (tuple_a[0], 0)
    if m < 2:
        if m == 0:
            tuple_b = (0, 0)
        elif m == 1:
            tuple_b = (tuple_b[0], 0)
    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return tuple_c
