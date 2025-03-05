"""Module to test important functions in main.py
"""

import main

# test function must start with test_ prefix for pytest to recognize it


def test_odd_even():
    """Function to test odd_even function
    """
    number = 99999
    expected = "odd"
    ans = main.odd_even(number)
    assert (main.odd_even(number) ==
            ans), f"Expected: {expected}, but got: {ans}"


def test_odd_even2():
    """Function to test odd_even function"""
    assert (main.odd_even(200) ==
            "even"), f"Expected: even, but got: {main.odd_even(200)}"


# FIXME 5: Write 3rd test case *Fixed*

def test_odd_even3():
    """Function to test odd_even function
    """
    number = -123
    expected = "odd"
    ans = main.odd_even(number)
    assert (main.odd_even(number) ==
            ans), f"Expected: {expected}, but got: {ans}"

# FIXME 6: Write 4th test case *Fixed*

def test_odd_even4():
    """Function to test odd_even function
    """
    number = 300000000
    expected = "even"
    ans = main.odd_even(number)
    assert (main.odd_even(number) ==
            ans), f"Expected: {expected}, but got: {ans}"

# FIXME 7: Write 3 test functions to test answer function *Fixed*

def test_answer1():

    input_value = 10
    expected = "Bob" 
    ans = main.answer(input_value)
    assert (main.answer(input_value) ==
            ans), f"Expected: {expected}, but got: {ans}"

def test_answer2():
    
    input_value = 5
    expected = "Alice"  
    ans = main.answer(input_value)
    assert (main.answer(input_value) ==
            ans), f"Expected: {expected}, but got: {ans}"

def test_answer3():

    input_value = 400000000000000000000000000000000000000000000000000000000000000000
    expected = "Bob"  
    ans = main.answer(input_value)
    assert (main.answer(input_value) ==
            ans), f"Expected: {expected}, but got: {ans}"