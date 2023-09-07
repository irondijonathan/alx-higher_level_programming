#!/usr/bin/python3
"""
This code defines a rectangle class
"""


class Rectangle:
    """This is a Representation of  rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the said rectangle"""
        self.width = width
        self.height = height

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

    def area(self):
        """this method returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """this method returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """this returns printable string representation of the said  rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
