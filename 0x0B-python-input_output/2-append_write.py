#!/usr/bin/python3
""" This module appends a file """


def append_write(filename="", text=""):
    """ functions that opens and append file """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
