#!/usr/bin/python3
"""
This module consists of a single function called
``text_indentation`` which prints a text with 2 new lines
after each of these characters `.`, `?` and `:`

"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
    `.`, `?` and `:`
    Args:
        text (str): a text to be sliced
    Raises:
        TypeError: if the text is not string
    """
    i = 1
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    for char in text:
        if char == "." or char == "?" or char == ":":
            print(char)
            print()
            i = 0
            continue
        print("{}".format(char if i != 0 else char.strip()), end='')
        i = 1
