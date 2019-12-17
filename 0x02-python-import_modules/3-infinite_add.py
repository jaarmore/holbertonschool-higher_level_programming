#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    arg_len = len(argv) - 1

    if arg_len == 0:
        print('{:d}'.format(arg_len))
    elif arg_len > 0:
        sum_arg = 0
        count = 1
        while count <= arg_len:
            sum_arg += int(argv[count])
            count += 1
        print('{:d}'.format(sum_arg))
