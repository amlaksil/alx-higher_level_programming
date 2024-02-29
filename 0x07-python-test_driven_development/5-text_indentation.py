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
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    init = 0
    for char in text:
        if char in punctuation_marks:
            str_t = text[init:text.index(char) + 1]
            init = text.index(char) + 1
            print(f"{str_t.strip()}\n")
    if "." not in text[init:] and "?" not in text[init:] and\
            ":" not in text[init:]:
        print(text[init:].strip(), end="")
