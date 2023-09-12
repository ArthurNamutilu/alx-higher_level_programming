#!/usr/bin/python3
""" imports from json """
import json

def load_from_json_file(filename):
    """ json -> py obj """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
