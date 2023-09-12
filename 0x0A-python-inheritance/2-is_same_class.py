#!/usr/bin/python3
"""This module is responsible for checking a class-checking function."""


def is_same_class(obj, a_class):
    """This Checks if an object is exactly an instance of a given class.
    Args:
        obj (any): This is the  object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        if the object is exactly an instance of a_class - True.
        otherwise, if it's not - False.
    """
    if type(obj) == a_class:
        return True
    return False
