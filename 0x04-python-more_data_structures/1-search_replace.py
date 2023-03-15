#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = len(my_list)
    if search not in my_list:
        return my_list
    for i in range(n):
        if my_list[i] == search:
            my_list[i] = replace
            new_list = my_list[:i] + my_list[i:]
            my_list[i] = search
        else:
            new_list = my_list
    return new_list
