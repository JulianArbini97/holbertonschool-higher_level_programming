#!/usr/bin/python3
""" Base of the project """


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
