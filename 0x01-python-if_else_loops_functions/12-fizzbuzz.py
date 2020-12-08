#!/usr/bin/python3
def fizzbuzz():
    for s in range (1, 101):
        if (s % 15 == 0):
            print("FizzBuzz", end=" ")
        elif (s % 3 == 0):
            print("Fizz", end=" ")
        elif (s % 5 == 0):
            print("Buzz", end=" ")
        else:
            print("{:d}".format(s), end=" ")

