#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list:
        cont = 0
        try:
            for val in range(0, x):
                print('{}'.format(my_list[val]), end='')
                cont += 1
        except IndexError:
            pass
        print()
        return cont
