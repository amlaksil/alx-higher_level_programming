#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    newList = []
    n = len(my_list)
    for i in range(n):
        if my_list[i] % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
    return newList
