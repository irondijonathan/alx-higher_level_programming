#!/usr/bin/python3
"""This Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """This checks if an object is an instance or inherited instance of a class.
    Args:
        obj (any): This is  the  object to check.
        a_class (type): This is the class to match the type of obj to.
    Returns:
        If the object is an instance or inherited instance of a_class - True.
        if it's not - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
