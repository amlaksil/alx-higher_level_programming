#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    n = len(my_list)
    if idx < 0 or idx > n - 1:
        return my_list
    for i in range(n):
        if i == idx:
            my_list[idx] = element
            return my_list
