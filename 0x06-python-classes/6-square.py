#!/usr/bin/python3
"""Square Module"""


class Square():
    """class Square that defines a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """check if the size of square is an integer."""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieved the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of position"""
        if (isinstance(value, tuple) and len(value) != 2 and
            isinstance(value[0], int) and isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
                self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        """Prints the square with char # on stdout"""
        if self.__size == 0:
            print()
        else:
            if self.__position:
                for x in range(self.__position[1]):
                    print()
                for x in range(self.__size):
                    print(' ' * self.__position[0], end='')
                    print('#' * self.__size)
            else:
                for fil in range(self.__size):
                        print('#' * self.__size)
