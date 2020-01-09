#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    try:
        for val in range(0, x):
            if isinstance(my_list[val], int):
                print("{:d}".format(my_list[val]), end='')
                cont += 1
    except ValueError:
        pass
    print()
    return cont
