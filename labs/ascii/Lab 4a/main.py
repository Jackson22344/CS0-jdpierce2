"""
Conditional Logic Lab
Updated By: Jackson Pierce
CSCI 110 Lab
Date: 3/4/2025

Read and solve the Kattis problem: https://open.kattis.com/problems/twostones 

Algorithm Steps:
  1. Read the number of stones
  2. Check if the number of stones is odd or even
  3. Print the winner
    3.a. If the number is odd, Alice wins.
    3.b. Otherwise, Bob wins.
"""


def main():
    """Main function that solves the problem
    """
    # FIXME 1: read the number of stones *Fixed*
    stone = int(input("How many stones are left? "))

    # FIXME 2: call answer function passing the number of stones as an argument *Fixed*
    result = answer(stone)

    # FIXME 3: print the answer as shown in the sample output *Fixed*
    print(result)

def odd_even(number: int):
    """Checks if the number is odd or even

    Args:
        number (int): number to check odd or even

    Returns:
        str: 'odd' if the number is odd, 'even' otherwise
    """
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
    # FIXME 4: if the number divided by 2 has 0 remainder, return 'even'
    # otherwise, return 'odd' *Fixed*
    
    ans = "FIXME"
    return ans


def answer(stone: int):
    """Creates the final answer and returns it given the number of stones

    Args:
        stone (int): number of stones

    Returns:
        str: 'Alice' if the number of stones is odd, 'Bob' otherwise
    """
    evenorodd = odd_even(stone)
    if evenorodd == "odd":
        return "Alice"
    else:
        return "Bob"


if __name__ == "__main__":
    main()