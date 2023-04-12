#!/usr/bin/python3
"""
This moudle contains a single function called
`write_file` which writes a string to a text file
"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    Args:
        filename (str): the name of a file
        text (str): the string to be written to a file
    Return:
        the number of character written
    """
    with open(filename, mode='w', encoding="utf-8") as content:
        num_char_written = content.write(text)
    return num_char_written
