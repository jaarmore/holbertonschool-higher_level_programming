#!/usr/bin/python3
"""
Geometry module
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """
        Empty method area() that raises an Exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Public method that validates value
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

"""
Class Rectangle that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """
    def __init__(self, width, height):
        """
        Initializes values of width and height

        Args:
           width: integer of width
           height: integer of height
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Method that returns the area of Rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Prints the Rectangle description
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


"""
Class Square that inherits from Rectangle
"""


class Square(Rectangle):
    """
    Class Square
    """
    def __init_(self, size):
        """
        initializes values of size

        Args:
            size: size of Square
        """
        self.integer_validator('size', size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        """Returns the area of Square"""
        return (self.__size**2)
