#!/usr/bin/python3
def read_file(filename=""):
    """ Functions that opens a file """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
