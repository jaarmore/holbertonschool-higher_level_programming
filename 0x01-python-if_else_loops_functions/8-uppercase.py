#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        ascii_val = ord(letter)
        if ascii_val >= 97 and ascii_val <= 122:
            ascii_val -= 32
        print('{}'.format(chr(ascii_val)), end='')
    print()
