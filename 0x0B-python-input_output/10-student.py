#!/usr/bin/python3
"""This Defines a class Student."""


class Student:
    """This Represent a student."""

    def __init__(self, first_name, last_name, age):
        """This Initializes a new Student.
        Args:
            first_name (str):This is The first name of the student.
            last_name (str):This is The last name of the student.
            age (int):This is The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This Gets a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
