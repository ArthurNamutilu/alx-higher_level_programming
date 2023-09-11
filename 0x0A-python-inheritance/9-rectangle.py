#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class using BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() & str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
