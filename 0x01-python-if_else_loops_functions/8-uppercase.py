#!/usr/bin/python3
# Prints a string in uppercase followed by a new line


def uppercase(str):
    j = ''
    for elem in str:
        if ord(elem) >= 97 and ord(elem) <= 122:
            char = j + chr(ord(elem) - 32)
        else:
            char = elem
        print("{}".format(char), end="")
    print()
