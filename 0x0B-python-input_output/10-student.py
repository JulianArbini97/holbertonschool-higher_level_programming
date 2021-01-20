#!/usr/bin/python3
""" Write a class Student """


class Student():
    """ Class student """
    def __init__(self, first_name, last_name, age):
        """ function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function """
        if type(attrs) is not list:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
