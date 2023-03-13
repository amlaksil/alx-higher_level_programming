#!/usr/bin/python3


def no_c(my_string):
    for i in my_string:
        if ord(i) == 67 or ord(i) == 99:
            n = my_string.index(i)
            my_string = my_string[: n] + my_string[n + 1:]
    return my_string
