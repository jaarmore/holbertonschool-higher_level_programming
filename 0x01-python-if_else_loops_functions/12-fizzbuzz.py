#!/usr/bin/phyton3
def fizzbuzz():
    fizz_num = 1
    while fizz_num <= 100:
        if (fizz_num % 5) == 0 and (fizz_num % 3) == 0:
            print('FizzBuzz', end=' ')
        elif (fizz_num % 3) == 0:
            print('Fizz', end=' ')
        elif (fizz_num % 5) == 0:
            print('Buzz', end=' ')
        else:
            print(fizz_num, end=' ')
        fizz_num += 1
