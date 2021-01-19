#!/usr/bin/python3
""" Write a class MyInt that inherits from int """


class MyInt(int):
    """ comment """
    def __eq__(self, number):
        """ comment """
        return False

    def __ne__(self, number):
        """ comment """
        return True
