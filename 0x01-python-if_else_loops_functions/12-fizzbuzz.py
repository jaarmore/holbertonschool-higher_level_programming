#!/usr/bin/phyton3
def fizzbuzz():
    for fizz_num in range(1, 101):
        if (fizz_num % 5) == 0 and (fizz_num % 3) == 0:
            print('{}'.format('FizzBuzz'), end=' ')
        elif (fizz_num % 3) == 0:
            print('{}'.format('Fizz'), end=' ')
        elif (fizz_num % 5) == 0:
            print('{}'.format('Buzz'), end=' ')
        else:
            print('{}'.format(fizz_num), end=' ')
