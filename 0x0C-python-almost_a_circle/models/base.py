#!/usr/bin/python3
""" Base class """


class Base:
    __nb_objects = 0  # class attribute

    def __init__(self, id=None):
        """ assigns id """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
