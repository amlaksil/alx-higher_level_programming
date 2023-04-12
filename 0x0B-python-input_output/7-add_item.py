#!/usr/bin/python3
"""
This module contains two other functions from previous
task namely from 5-save_to_json_file.py module `save_to_json_file`
and from 6-load_from_json_file.py module `load_from_json_file`
the first one writes json object to a file and the second function
creates object from json file respectvely.
"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    """We can also use os.path.exists(path) instead of this try block our main
    goal is to check whether the given file is empty or not"""
    objct = load_from_json_file("add_item.json")
except Exception:
    objct = []

for arg in sys.argv[1:]:
    objct.append(arg)


save_to_json_file(objct, "add_item.json")
