#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """class method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this method validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
