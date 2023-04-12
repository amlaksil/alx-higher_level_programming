#!/usr/bin/python3
"""This module reads the content of text file"""


def read_file(filename=""):
    """Reads the content of UTF8 file
    Args:
       filename (str): the name of file
    """
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    print(content, end="")
