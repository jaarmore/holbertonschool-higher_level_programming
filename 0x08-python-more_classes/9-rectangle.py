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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation of values width and height"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        symb = str(Rectangle.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return figure
        else:
            for i in range(0, self.__height - 1):
                figure += symb * self.__width + '\n'
            figure += symb * self.__width
            return figure

    def __repr__(self):
        """
        Return a string representation of the rectangle
        to recreate a new instance by using eval().
        """
        return ('Rectangle({:d}, {:d})'.format(self.__width, self.__height))

    def __del__(self):
        """Print message when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        return print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that compares two rectangles.

        Args:
            rect_1: first object Rectangle
            rect_2: second object Rectangle

        Returns:
            The biggest rectangle based on the area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() >= rect_2.area():
            return rect_1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area

        Args:
            rect_1: first object Rectangle
            rect_2: second object Rectangle

        Returns:
            The biggest rectangle based on the area.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() >= rect_2.area():
            return rect_1
