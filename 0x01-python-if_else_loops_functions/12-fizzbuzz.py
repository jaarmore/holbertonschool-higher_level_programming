#!/usr/bin/phyton3
def fizzbuzz():
    for fizz_num in range(1, 101):
        if (fizz_num % 5) == 0 and (fizz_num % 3) == 0:
            print('FizzBuzz', end=' ')
        elif (fizz_num % 3) == 0:
            print('Fizz', end=' ')
        elif (fizz_num % 5) == 0:
            print('Buzz', end=' ')
        else:
            print('{:d}'.format(fizz_num), end=' ')
