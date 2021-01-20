#!/usr/bin/python3
"""  function that returns the dictionary description with simple data structure """
MyClass = __import__('8-my_class').MyClass


def class_to_json(obj):
    return(obj.__dict__)