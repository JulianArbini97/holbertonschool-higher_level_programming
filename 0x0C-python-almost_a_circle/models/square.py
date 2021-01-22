#!/usr/bin/python3
""" Square time """
from . rectangle import Rectangle


class Square(Rectangle):
    """ init of square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ comment method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overriding the __str__ method that returns a custom string """
        Mensaje = "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)
        return (Mensaje)

    @property
    def size(self):
        """ value of y """
        return (self.height)

    @size.setter
    def size(self, value):
        """ value of size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates square"""
        attributes = ["id", "size", "x", "y"]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for arg in range(len(args)):
                setattr(self, attributes[arg], args[arg])

        def to_dictionary(self):
            """ dictionary of square """
            the_dict = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
            }
            return (the_dict)        