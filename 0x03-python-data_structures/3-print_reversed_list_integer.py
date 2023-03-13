#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        n = len(my_list) - 1
        k = 0
        while n >= k:
            print("{:d}".format(my_list[n]))
            n -= 1
