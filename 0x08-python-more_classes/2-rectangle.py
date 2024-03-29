#!/usr/bin/python3
""" class defining a rectangle """


class Rectangle:
    """ rect class """
    def __init__(self, width=0, height=0):
        """ initializing the instancces """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieves the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves the height """
        return self.__height

    @height.setter
    def height(self, value):
        """" sets the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangular perimeter """
        if self.__width == 0 and self.height == 0:
            per = 0
            return per
        else:
            per = 2 * (self.__height + self.__width)
            return per
