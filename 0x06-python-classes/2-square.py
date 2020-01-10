#!/usr/bin/python3
"""Square Module"""


class Square():
    """class Square that defines a Square"""
    def __init__(self, size=0):
        """check if the size of square is an integer."""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
