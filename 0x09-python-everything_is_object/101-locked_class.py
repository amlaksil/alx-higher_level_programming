#!/usr/bin/python3
"""a module that contains LokedClass """


class LockedClass:
    """This class prevents the user from dynamically crating new instance
    attributes, except if the new instance attribute is called first_name.
    To do this we have to define a list with the name __slots__ which cotains
    all the attributes, we want to use. Anything not in this list can't be used
    as an attribute.
    """
    __slots__ = ['first_name']
