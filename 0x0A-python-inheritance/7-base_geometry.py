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
