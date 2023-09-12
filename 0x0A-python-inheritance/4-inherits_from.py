#!/usr/bin/python3
"""This module is responsible for checking an inherited class-checking function."""


def inherits_from(obj, a_class):
    """This Checks if an object is an inherited instance of a class.
    Args:
        obj (any): This is The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If object is an inherited instance of a_class - True.
        If it's not - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
