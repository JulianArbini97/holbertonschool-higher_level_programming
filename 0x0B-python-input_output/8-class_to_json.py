#!/usr/bin/python3
"""  function that returns the dict descr with simple data structure """
MyClass = __import__('8-my_class').MyClass


def class_to_json(obj):
    """ comment about the funct """
    return(obj.__dict__)
