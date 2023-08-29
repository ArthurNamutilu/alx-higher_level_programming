#!/usr/bin/python3
"""This Module defines a square"""

class Square:
    """defining sqaure class"""
    def __init__(self, size=0):
        """size variable initialization"""
        self.size = size

    @property
    def size(self):
        """returns _attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """checkss value passed"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """seting the area"""
        return self.__size ** 2

    def my_print(self):
        """shows the size"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)


"""

**************
class Square:
    """Creat size& self attributes"""

    def __init__(self, size=0):
        """ Iitializing size var """
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
"""
