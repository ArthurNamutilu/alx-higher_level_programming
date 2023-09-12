#!/usr/bin/python3
""" This module deserializes json string to object """
import json


def from_json_string(my_str):
    """ JSON -> object """
    return json.loads(my_str)
