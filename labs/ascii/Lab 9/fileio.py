"""
File I/O Lab
By: Jackson Pierce

CSCI 110
Date: 4/17/2025

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""


totalInts = 10


def readData():
    intList = []
    # FIXME1 (20 points):              #Fixed#
    # Prompt user to input file name
    # open the file; read each number one line at a time;
    # and store it into intList list
    # close the file
    # return the intList
    fileName = input("Enter the input filename: ")  
    with open(fileName, 'r') as file:
        for line in file:
            intList.append(int(line.strip()))
    return intList


def sortListInAscendingOrder(lstInts):
    # FIXME2                                   #Fixed#
    # sort lstInts list in ascending order

    lstInts.sort() 
    pass


def sortListInDescendingOrder(lstInts):
    # FIXME3                                  #Fixed#
    # sort lstInts in descending order
    
    lstInts.sort(reverse=True)  
    pass


def printList(printFile, lstInts):
    for i in lstInts:
        # FIXME4                      #Fixed#
        # write each value one line at a time to file
        # handled by printFile object.
        printFile.write(str(i) + '\n')
        pass
    printFile.write('\n')


def main():
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)
    # sort numbers
    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)

    # FIXME5                             #Fixed#
    # Call sortListInDescendingOrder function
    
    sortListInDescendingOrder(integers)


    # FIXME6                                    #Fixed#
    # Write the sorted list in descending order to the output file

    printFile.write("Numbers sorted in descending order:\n")
    printList(printFile, integers)

    # FIXME7              #Fixed#
    # Print the largest number to the output file

    printFile.write("Largest number: " + str(integers[0]) + '\n')

    # FIXME8              #Fixed# 
    # Print the smallest number to the output file

    printFile.write("Smallest number: " + str(integers[-1]) + '\n')

    printFile.close()
    print('Done executing the program! Check the output file for results.')


# FIXME9          #Fixed#
# Call main function if this module is run as the main module

if __name__ == '__main__':
    main()