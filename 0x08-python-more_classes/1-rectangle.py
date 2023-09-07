#!/usr/bin/python3
"""
This code Defines a class Rectangle
"""


class Rectangle:
    """This is a representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the said  rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """this is the getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """this is the setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this is the getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """this is the setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
