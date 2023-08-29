#!/usr/bin/python3
"""Square class - creating a private size attribute"""


class Square:
    """Square class with private instance attribute size"""
    def __init__(self, size=0):
    """ Initializing square class
    Args:
        size: size os square
    Raises:
        TypeError: if size not int
        ValueError: if size less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
