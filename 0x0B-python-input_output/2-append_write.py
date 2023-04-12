#!/usr/bin/python3
"""
This module contains a function called
`append_write` that appends a string at
the end of a text file (UTF8).
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    Args:
        filename (str): name of text file
        text    (str): string to be added
    Return:
        the number of characters added
    """
    with open(filename, mode='a', encoding="utf-8") as content:
        num_char_append = content.write(text)
    return num_char_append
