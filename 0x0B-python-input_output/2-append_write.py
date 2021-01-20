#!/usr/bin/python3
""" Write a function that reads a text file to stdout """


def append_write(filename="", text=""):
    """ append text to a created or not text """
    with open(filename, 'a', encoding='utf-8') as MyFile:
        return(MyFile.write(text))