#!/usr/bin/python3
"""
This module contains a function called
`append_after` that inserts a line of text
to a file, after each line containing a specific
string
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after specific string
    Args:
        filename (str): the name of a file
        search_string (str): string to be searched
        new_string (str): a string to be added after search_string
    """
    position = 0
    with open(filename, 'r+', encoding="utf-8") as f:
        contents = f.readlines()
        cpy_contents = contents.copy()
        for line in contents:
            if search_string in line:
                cpy_contents.insert(position + 1, new_string)
                position += 1
            position += 1

        '''set the reference point(pointer) at the beginning of the file
        or open a file again in write mode to trancate'''

        f.seek(0)
        f.truncate()  # Clear previous content
        f.writelines(cpy_contents)
