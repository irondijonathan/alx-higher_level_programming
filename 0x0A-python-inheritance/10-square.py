#!/usr/bin/python3
"""This module is responsible for defining a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This Represent a square."""

    def __init__(self, size):
        """This Initializes a new square.
        Args:
            size (int): The length of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
