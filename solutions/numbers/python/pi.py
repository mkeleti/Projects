# 1.py
# Author: Michael Keleti

# Find PI to the Nth Digit Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

import math
import unittest
import numbers

def PI():
    x = input("Enter a number to limit the the digits of pi: ")

    pi = math.pi
    pi = round(pi, x - 1)

    print(pi)

if __name__ == '__main__':
    PI()
    
    