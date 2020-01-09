#!/usr/bin/python3
class Square:
    """class Square that defines a Square"""

    def __init_(self, size=0):
        """check if the size of square is an integer."""
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
