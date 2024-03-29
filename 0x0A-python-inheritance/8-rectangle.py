#!/usr/bin/python3
"""It inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class defining rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
