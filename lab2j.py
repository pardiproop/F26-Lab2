# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 30/9/2026
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py

# TO DO 1: 
# Import the `math` module.
# Define a variable named num. Prompt the user to input a number and assign it to the variable num.
# Convert the user input to a floating-point number and assign it to num.
from math import sqrt

# TO DO 2: 
# Create an infinite loop using while True. Inside the loop:
# Check if num is negative:
# If it is, print "Invalid number." and continue to the next iteration of the loop.
while True:
    num=int(input("Enter a Number: "))
    if num<0:
        print("Invalid Number.")
        print()
        continue

# TO DO 3: 
# Check if num is zero:
# If it is, print "Exiting..." and break out of the loop.
    if num==0:
        print("Exiting...")
        break

# TO DO 4: 
#Calculate the square root of num using the math.sqrt function.
# TO DO 1: Import the `math` module.
    print(sqrt(num))
    print()


# TO DO 2: Create an infinite loop using while True.

    # TO DO 3: Check if num is zero:
   

    # TO DO 4: Calculate the square root of num using the math.sqrt function.

