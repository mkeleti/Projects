"""
By: Michael Keleti
**Find PI to the Nth Digit** - Enter a number and have the program generate PI
up to that many decimal places. Keep a limit to how far the program will go.
"""

x = input("Enter a number: ")

print(round(float(math.PI), x)