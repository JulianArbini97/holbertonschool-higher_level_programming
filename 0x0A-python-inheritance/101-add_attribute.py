#!/usr/bin/python3
""" Write a function that adds a new attribute to an object if its possible """


def add_attribute(object, name, value):
    """ funct to add object to a class """

    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
