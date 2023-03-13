#!/usr/bin/python3


def element_at(my_list, idx):
    n = len(my_list)
    if idx < 0 or idx > n - 1:
        return None
    for i in range(n):
        if i == idx:
            return my_list[idx]
