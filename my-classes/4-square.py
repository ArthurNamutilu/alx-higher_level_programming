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

    @property
    def size(self):
        """returns the size attribute ie setter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size value setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """defines the area"""
        return self.__size ** 2
