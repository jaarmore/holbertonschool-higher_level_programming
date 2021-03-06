#!/usr/bin/python3
"""Square Module"""


class Square():
    """class Square that defines a Square"""
    def __init__(self, size=0):
        """check if the size of square is an integer."""
        self.__size = size

    def area(self):
        """Return the area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Retrieved the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of size to value"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
