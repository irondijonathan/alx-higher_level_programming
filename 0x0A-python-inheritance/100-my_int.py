#!/usr/bin/python3
"""This module is responsible for defining a class MyInt that inherits from int."""


class MyInt(int):
    """This Invert int operators == and !=."""

    def __eq__(self, value):
        """THis Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """This Override != operator with == behavior."""
        return self.real == value
