#!/usr/bin/python3
for first in range(0, 9):
       for second in range (second, 9):
              if (second < first or second == first):
                     continue
                     if (first != 8):
                            print("{:d}{:d}".format(first, second), end=", ")
                     else:
                            print("{:d}{;d}".format(first, second))
