#!/usr/bin/python3
""" Square time """
from . rectangle import Rectangle


class Square(Rectangle):
    """ init of square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ comment method """
        self.size = size
        super().__init__(size, size, x, y, id)       

    def __str__(self):
        """ overriding the __str__ method that returns a custom string """
        Mensaje = "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)
        return (Mensaje)