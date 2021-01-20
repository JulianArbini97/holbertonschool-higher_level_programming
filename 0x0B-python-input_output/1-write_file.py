#!/usr/bin/python3
""" Write a function that reads a text file to stdout """


def write_file(filename="", text=""):
    """ function that reads a text file and gives char num"""
    with open(filename, 'w', encoding='utf-8') as MyFile:
        return(MyFile.write(text))