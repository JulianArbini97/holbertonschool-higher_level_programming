#!/usr/bin/python3
for first in range (0, 9):
       second = first + 1
       for second in range (second, 9):
              print("{:d}".format(first), end ="")
              print("{:d}, ".format(second), end ="")
print("89")
