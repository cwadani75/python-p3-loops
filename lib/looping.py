#!/usr/bin/env python3

def happy_new_year():
    # Countdown from 10 to 1 and then print "Happy New Year!"
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square_integers(int_list):
    # Return a new list containing the squares of the integers
    return [x ** 2 for x in int_list]

def fizzbuzz():
    # Print numbers from 1 to 100
    # For multiples of 3 print "Fizz" instead of the number
    # For multiples of 5 print "Buzz"
    # For multiples of both 3 and 5 print "FizzBuzz"
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
