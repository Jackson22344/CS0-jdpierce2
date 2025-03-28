"""
CSCI 110
List Lab

By: Jackson Pierce
Date: 3/27/2025

Program prompts user to enter 10 integers and stores the entered numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
and print the largest and smallest values in the list.
Program will also print the indices of the largest and smallest numbers in the list.
"""

totalInts = 10


def getIntegers():
    intList = []
    i = 0
    while i < totalInts:
        num = int(input("Enter an integer: "))
        intList.append(num) # FIXME add num into integers list   #Fixed
        i += 1
    return intList


def sortListInAscendingOrder(intList):
    intList.sort()


def sortListInDescendingOrder(intList):
    # FIXME3 (20 points)   #Fixed
    intList.sort(reverse=True) 
    pass


def printList(intList):
    for val in intList:
        print(val, end=' ')
    print()


def main():
    integers = []  # empty list to store integers
    integers = getIntegers()
    print("Numbers entered are: ")
    printList(integers)
    print()

    # sort numbers
    sortListInAscendingOrder(integers)
    print("Numbers in ascending order: ")
    printList(integers)
    
    # FIXME4 (10 points)        #Fixed
    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers)

    # FIXME5 (10 points)        #Fixed
    # Print the sorted list in descending order
    print("Numbers in descending order: ")   
    printList(integers) 

    # FIXME6 (10 points)        #Fixed
    # Print the largest number
    largest = max(integers)  
    print(f"Largest number: {largest}")

    # FIXME7 (10 points)        #Fixed
    # Print the smallest number
    smallest = min(integers)  
    print(f"Smallest number: {smallest}")

    # FIXME8 (10 points)         #Fixed
    # Find and print the index of the smallest number
    index_smallest = integers.index(smallest)  
    print(f"Index of smallest number: {index_smallest}")

    # FIXME9 (10 points)           #Fixed
    # Print the index of the largest number
    index_largest = integers.index(largest)  
    print(f"Index of largest number: {index_largest}")


# FIXME10 (20 points)         #Fixed
# Call main function if this file is run as the main module
# print('call main() function to see partial outputs of the program...') <--(Didn't know what this is for so I just commented it out)
if __name__ == "__main__": 
    main()