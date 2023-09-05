#!/usr/bin/python3
""" square class"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """
        Initialize a square with an optional size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Finds the area of square
        Returns:
            float: area of square
        """
        return self.__size ** 2
