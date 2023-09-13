#!/usr/bin/python3
"""This is responsible for defining a class Student."""


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

    def to_json(self):
        """This Gets a dictionary representation of the Student."""
        return self.__dict__
