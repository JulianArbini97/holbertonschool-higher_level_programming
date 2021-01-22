#!/usr/bin/python3
""" Rectangle file"""
from . base import Base


class Rectangle(Base):
    """ Class rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width of rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set passet private attribute of width """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve the height of rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set passed private attribute of height """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x coord """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ value of x  """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ value of y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ value of y """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of rectangle """
        return (self.width * self.height)

    def display(self):
        """ printer function """
        if self.width == 0 or self.height == 0:
            print()
        for i in range(self.__y):
            print(" " * self.__x)
        for j in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """ values representation """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates rectangle"""
        attributes = ["id", "width", "height", "x", "y"]
        for arg in range(len(args)):
            setattr(self, attributes[arg], args[arg])
