#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        str = s.translate({ord(i): None for i in 'cC'})
        return str
