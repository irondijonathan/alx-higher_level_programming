#!/usr/bin/python3
"""This is responsible for defining a Python class-to-JSON function."""


def class_to_json(obj):
    """This Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
