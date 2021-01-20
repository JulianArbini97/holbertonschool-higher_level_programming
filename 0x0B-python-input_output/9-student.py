#!/usr/bin/python3
""" Write a class Student """


class Student():
    """ Class student """
    def __init__(self, first_name, last_name, age):
        """ function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ function """
        return self.__dict__
