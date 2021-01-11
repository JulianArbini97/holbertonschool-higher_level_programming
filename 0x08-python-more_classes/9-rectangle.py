#!/usr/bin/python3
"""
Class Rectangle: Defines a Rectangle
"""


class Rectangle:
    """ comment """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=(0, 0)):
        """ comment """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ comment """
        return self.__width

    @width.setter
    def width(self, value):
        """ comment """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ comment """
        return self.__height

    @height.setter
    def height(self, value):
        """ comment """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ comment """
        return (self.__width * self.__height)

    def perimeter(self):
        """ comment """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """ comment """
        result = ""

        if self.__width == 0 or self.__height == 0:
            return result
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    result = result + str(self.print_symbol)
                result = result + '\n'
            result = result[:-1]
            return result

    def __repr__(self):
        """ comment """
        strwidth = str(self.__width)
        strheight = str(self.__height)

        return "Rectangle(" + strwidth + "," + strheight + ")"

    def __del__(self):
        """ comment """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ comment """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """ comment """
        return cls(size, size)
