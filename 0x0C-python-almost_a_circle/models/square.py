#!/usr/bin/python3
""" Square time """
from . rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    @property
    def size(self):
        """ Retriebe the size of square """
        return self.__width

    def __str__(self):
        """ overriding the __str__ method that returns a custom string """
        Mensaje = "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.__x, self.__y, self.__width)
        return Mensaje

    @property
    def size(self):
        """ value of size """
        return self.__width

    @size.setter
    def size(self, value):
        """ value of size """
        if type(value) is int:
            if value > 0:
                self.__width = value
            elif value <= 0:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def x(self):
        """ Retrieve private instance attribute x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set private instance attribute x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrieve private instance sttribute y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ set private instance attribute y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """Updates square"""
        my_attr = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, my_attr[i], args[i])
        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ dictionary of square """
        the_dict = {
            'id': self.id,
            'size': self.__width,
            'x': self.__x,
            'y': self.__y
        }
        return the_dict
