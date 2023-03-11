#!/usr/bin/python3
import sys
import hidden_4


def print_name():
    name = dir(hidden_4)

    for n in range(0, len(name)):
        if name[n][0] != '_':
            print("{}".format(name[n]))


if __name__ == "__main__":
    print_name()
