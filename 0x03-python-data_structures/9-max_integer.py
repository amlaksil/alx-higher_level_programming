#!/usr/bin/python3


def max_integer(my_list=[]):
    n = len(my_list)
    num = 0
    if n == 0:
        return None
    while num < n - 1:
        if (my_list[num] > my_list[num + 1]):
            temp = my_list[num]
            my_list[num] = my_list[num + 1]
            my_list[num + 1] = temp
        num += 1
    return (my_list[n - 1])
