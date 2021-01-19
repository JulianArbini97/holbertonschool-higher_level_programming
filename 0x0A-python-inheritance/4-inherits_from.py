#!/usr/bin/python3
""" True if the object is instance of class that inherited, otherwise False """


def inherits_from(obj, a_class):
    """ what says up there """
    if (type(obj) == a_class):
        return False
    return(isinstance(obj, a_class))
