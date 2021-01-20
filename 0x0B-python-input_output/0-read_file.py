#!/usr/bin/python3
""" Write a function that reads a text file to stdout """


def read_file(filename=""):
    """ function that reads a text file """
    with open (filename, encoding='utf-8') as MyFile:
        print(MyFile.read(), end='')