#!/usr/bin/python3


# a function that prints all integers of a list
def print_list_integer(my_list=[]):
    n = len(my_list)
    for i in range(n):
        print("{}".format(my_list[i]))
