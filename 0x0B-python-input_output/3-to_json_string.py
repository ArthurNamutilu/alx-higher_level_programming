#!/usr/bin/python3
""" This module returns JSON rep of an obj (string) """
import json


def to_json_string(my_obj):
    """ return json """
    return json.dumps(my_obj)
