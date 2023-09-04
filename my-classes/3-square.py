#!/usr/bin/python3
"""This Module defines a square"""


class Square:
    """Creat size& self attributes"""

    def __init__(self, size=0):
        """Initializing square class
        Args:
            size: size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size ** 2
