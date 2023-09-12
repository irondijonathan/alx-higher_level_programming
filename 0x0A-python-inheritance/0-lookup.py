#!/usr/bin/python3
"""This module Defines an object attribute lookup function."""


def lookup(obj):
    """This will return a list of an object's available attributes."""
    return (dir(obj))
