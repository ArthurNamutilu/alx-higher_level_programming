#!/usr/bin/python3
"""
   This Module checks if an object is an instance,
   or inherited from a sub-class
"""


def is_kind_of_class(obj, a_class):
    """checks for object instance"""
    return (isinstance(obj, a_class))
