#!/usr/bin/python3
for first_number in range(0, 10):
    for second_number in range(0, 10):
        if first_number < second_number:
            print('{}{}'.format(first_number, second_number), end='')
            if first_number == 8 and second_number == 9:
                pass
            else:
                print(end=', ')
print()
