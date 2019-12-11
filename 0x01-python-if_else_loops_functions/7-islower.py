#!/usr/bin/python3
def islower(c):
    number_ascii = ord(c)
    if number_ascii >= 97 and number_ascii <= 122:
        return True
    else:
        return False
