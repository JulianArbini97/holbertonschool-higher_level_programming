#!/usr/bin/python3

"""Print first name and last name
Args:
first_name: string of first name
last_name: string of last name
Returns: nothing"""


def say_my_name(first_name, last_name=""):
    """print name follow format
    My name is [first_name] [last_name]
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
