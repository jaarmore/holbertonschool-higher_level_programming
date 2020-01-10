#!/usr/bin/python3
"""Square Module"""


class Square():
    """class Square that defines a Square"""
    def __init__(self, size=0, position=(0, 0)):
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

    def my_print(self):
        """Prints the square with char # on stdout"""
        if self.__size == 0:
            print()
        else:
            for fil in range(self.__size):
                for col in range(self.__size):
                    print('#', end='')
                print()

    def position(self):
        """Retieve the position"""
        pass

    def position(self, value):
        """Set the value to position"""
        pass
