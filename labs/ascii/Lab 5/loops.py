"""
Lab - Playing with Loops
Updated By: Jackson Pierce
CSCI 110
Date: 3/11/2025
Program prints geometric shapes of given height with * using loops
"""
import os
import sys


def printTriangle(height):
    """
    Function takes height as an argument to print the triangle
    of that height with *
    """
    i = 1
    while i <= height:
        print('*  '*i)
        i += 1
    print()  # print an empty line


def printFlippedTriangle(height):
    """
    # Implement the function that takes height as an argument
    # and prints a triangle with * of given height.
    # Triangle of height 5, e.g., should look like the following.
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    i = height
    while i >= 1:
        print('*  ' * i)
        i -= 1
    print()  # print an empty line

    # FIXME3 ...        *Fixed*
    pass


# FIXME4           *Fixed*
# Design and implement a function that takes a number as height and
# prints square of the given height with *.
# Square of height 5, e.g., would look like the following.
"""
*  *  *  *  *  
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
"""

def printSquare(height):
    
    for i in range(height):
        print('*  ' * height)
    print()  

def clearScreen():
    """
    function to clear screen based on the operating system
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    
    # FIXME7 add a loop to make the program to continue to run until the user wants to quit while True:      *Fixed*  
    # FIXME8 call clearScreen function to clear the screen for each round of the loop            *Fixed*

    while True:
        clearScreen()

        print('Program prints geometric shapes of given height with *')
        height = int(input('Please enter the height of the shape: '))
        # call printTriangle function passing user entered height
        printTriangle(height)

    # FIXME5          *Fixed*
    # Call printFlippedTriangle passing proper argument
    # Manually test the function

        printFlippedTriangle(height)

    # FIXME6              *Fixed*
    # Call the function defined in FIXME4 passing proper argument
    # Manually test the function

        printSquare(height)

    # FIXME9                      *Fixed*
    # prompt user to enter y/Y to continue anything else to quit

        continue_choice = input("Enter 'y' to continue or any other key to quit: ")

    # FIXME10                 *Fixed*
    # Use conditional statements to break the loop or continue in the loop
        if continue_choice != 'y':
            print("Goodbye!")
            break



if __name__ == "__main__":
    main()