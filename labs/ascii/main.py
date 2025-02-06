"""
    StdIO Lab
    ASCII Art - using literals and variables
    
    Updated By: Jackson Pierce
    Date: 1/30/25
    
    This program produces an ASCII art on the console.

    Algorithm steps: 
    1. Use variables to store data/values
    2. Write a series of print statements to print the data/values to the console
"""

print("Welcome to ASCII Art Program...\n")

name = input("What is your name? ")   
print("Nice meeting you " + name + "\n")   

# prompt user to enter the semester and store the value into semester variable using input function
semester = input("What semester is this [Fall/Spring]? ")
print("This is " + semester + " semester.\n")

year = input("What year is it? ")
print("This is " + year + ".\n")

print("Hope you like my ASCII art...\n\n")

line1: str = "  |\\_/|   **********************    (\\_/)\n"
print(line1)

line2: str = " / @ @ \   * ASCII Lab           * (='.'=)\n"
print(line2)

line3: str = "( > 0 < )  * Jackson Pierce   *  ( \" )_( \" )\n"
print(line3)

line4: str ="  >>x<<    * 2025 *\n"
print(line4)

line5: str = "  / O \  *   CSCI 111 *\n"
print(line5)

line4b = "stuff"

# FIXME8: print the third line of the graphics
# FIXME9: use variable to print the fourth line
# FIXME10: use variable to print the fifth line
# Note: You can add more lines or print more ASCII arts of your choice if you'd like...

print("\nGood bye...  \n")