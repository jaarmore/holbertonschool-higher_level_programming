#!/usr/bin/python3
from add_0 import add


def my_add_0():
    """My add_0 function

    Args:
        a: first integer equals to 1
        b: second integer equal to 2

    Result:
        Prints the add of a + b.
    """
    a = 1
    b = 2

    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))

if __name__ == '__main__':
    my_add_0()
