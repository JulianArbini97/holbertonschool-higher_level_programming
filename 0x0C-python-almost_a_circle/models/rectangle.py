#!/usr/bin/python3
""" Rectangle file"""
from . base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class Constructor """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """ Retriebe the width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set passet private attribute of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve the height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set passed private attribute of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

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

    def area(self):
        """ area of rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ printer function """
        rect = ""
        if self.__height == 0 or self.__width == 0:
            print(rect)
            return
        for new_l in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            for k in range(0, self.__x):
                rect += " "
            for j in range(0, self.__width):
                rect += "#"
            if i < self.__height - 1:
                rect += "\n"
        print(rect)

    def __str__(self):
        """ values representation """
        Mensaje = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.__x, self.__y, self.__width, self.height)
        return Mensaje

    def update(self, *args, **kwargs):
        """Updates rectangle"""
        my_attr = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, my_attr[i], args[i])
        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ dictionary of rectangle """
        the_dict = {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
        return (the_dict)
