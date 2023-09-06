#!/usr/bin/python3
"""This is the code to find the highest integer in a list or an array
"""


def max_integer(list=[]):
    """This sis the function that finds the highest integer in the list or array
        If the list is empty, the function returns None and code doesn't return anything
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
