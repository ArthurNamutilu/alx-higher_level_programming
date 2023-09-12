#!/usr/bin/python3
""" This module saves """
import json


def save_to_json_file(my_obj, filename):
    """py obj to json"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
