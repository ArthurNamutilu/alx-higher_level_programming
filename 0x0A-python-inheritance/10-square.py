#!/usr/bin/python3
"""Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square representation"""

    def __init__(self, size):
        """Initializes a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
