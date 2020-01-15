#!/usr/bin/python3
"""
Class that defines a Rectangle with private properties width and height
Prototype: class Rectangle()
"""


class Rectangle():
    """
    Class Rectangle that defines a Rectangle

    Args:

        width: width of rectangle
        height: height of rectangle

    Returns:
        Nothing

    """

    def __init__(self, width=0, height=0):
        """Instantiation of values width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets value of width only if value is an integer greather than zero
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        else:
            if value < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = value

    @property
    def height(self):
        """Returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets value of height only if value is an integer greather than zero
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        else:
            if value < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = value

    def area(self):
        """Returns the area of Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """String representation of rectangle with character #"""
        figure = ''
        if self.__width == 0 or self.__height == 0:
            return figure
        else:
            for i in range(0, self.__height - 1):
                figure += '#' * self.__width + '\n'
            figure += '#' * self.__width
            return figure
