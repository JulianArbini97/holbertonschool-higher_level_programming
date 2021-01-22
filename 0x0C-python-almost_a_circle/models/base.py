#!/usr/bin/python3
""" Base of the project """
import json


class Base:
    """ start of a new class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializion of the init function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """ passing dict to json string """
        if list_dictionaries is None:
            return []
        else:
            json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """ json to string """
        if (json_string is None or len(json_string) == 0):
            return ([])
        else:
            return (json.loads(json_string))