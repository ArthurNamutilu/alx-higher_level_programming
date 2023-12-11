#!/usr/bin/python3
"""module that inherits list and prints its attribute"""


class MyList(list):
    """ my list class that inherits lists and prints its attribute"""
    def print_sorted(self):
        """method that prints sorted list"""
        print(sorted(self))
