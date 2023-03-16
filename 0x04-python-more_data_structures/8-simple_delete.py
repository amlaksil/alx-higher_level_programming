#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    for k, v in a_dictionary.items():
        if key == k:
            del a_dictionary[key]
            break
    return a_dictionary
