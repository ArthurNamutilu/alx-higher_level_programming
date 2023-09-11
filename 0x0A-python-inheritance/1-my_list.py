#!/usr/bin/python3
"""inherits a list and prints the element"""


class MyList(list):
    """class that inherits list and prints its attribute"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
