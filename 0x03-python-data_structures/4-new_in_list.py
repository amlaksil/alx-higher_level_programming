#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    n = len(my_list)
    new_list = my_list.copy()
    if idx < 0 or idx > n - 1:
        return new_list
    for i in range(n):
        if idx == i:
            new_list[idx] = element
            return new_list
