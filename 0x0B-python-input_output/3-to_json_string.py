#!/usr/bin/python3
""" function that returns the JSON of an object """
import json


def to_json_string(my_obj):
    """ function that returns the JSON of an object """
    return(json.dumps(my_obj))