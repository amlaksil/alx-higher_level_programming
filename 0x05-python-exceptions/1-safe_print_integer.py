#!/usr/bin/python3
def safe_print_integer(value):
    try:
        y = int(value)
        print("{:d}".format(y))
        return True
    except ValueError:
        return False
