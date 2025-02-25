"""
Math and Variables Lab
By: Jackson Pierce
CSCI 110 Lab
Date: 2/21/2025

Read and solve: Add Two Numbers - https://open.kattis.com/problems/addtwonumbers 

Algorithm steps:
  1. Read data as a line
  2. Split the line into two integers
  3. Add them up
  4. print the result
"""

import sys


def main():
    """Main function that solves the problem
    """

    # FIXME1 - read input data into a variable #fixed#
    line = input("Input a value for a and b: ")

    # split the data into two numbers
    a, b = line.split()
    
    # check to see if the data split is correct
    print(f'{a=}, {b=}', file=sys.stderr)

    # FIXME 2: convert string a into integer #fixed#
    a = int(a)

    # FIXME 3: convert string b into integer #fixed#
    b = int(b)

    # FIXME 4: add two numbers and store the result into ans variable #fixed#
    ans = a + b

    # FIXME 5: print the answer as shown in the sample output #fixed#
    print(ans)


main()  # call main function