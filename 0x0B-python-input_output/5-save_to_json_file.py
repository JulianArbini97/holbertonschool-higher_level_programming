#!/usr/bin/python3
""" function that writes an Object to a text file, using JSON """
import json


def save_to_json_file(my_obj, filename):
    """ comment about the function """
    with open(filename, 'w') as MyFile:
        json.dump(my_obj, MyFile)
