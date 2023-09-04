#!/usr/bin/python3
"""Defining square class module"""


class Square:
    """Creating square"""
    def __init__(self, size=0, position=(0, 0)):
        """size and position attribute"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """.setter() setting size and value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """return curr position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter()- sets position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """sets area"""
        return self.size ** 2

    def my_print(self):
        """this func prints attributes"""
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
