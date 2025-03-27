"""Moduel to test important function in pet.py.
"""

import pet


def test_answer() -> None:
    """Tests answer function."""
    ans = pet.answer([10, 20, 11, 15, 13])
    expected = "2 20"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_answer2() -> None:
    """Tests answer function."""
    ans = pet.answer([6, 10, 8, 4, 15])
    expected = "5 15"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 1: add a test case function to test answer function         #Fixed
def test_answer3() -> None:
    """Tests answer function."""
    ans = pet.answer([35, 15, 22, 18, 60])
    expected = "4 60"  
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 2: add a test case function to test answer function          #Fixed
def test_answer4() -> None:
    """Tests answer function."""
    ans = pet.answer([1, 12, 5, 0, 12])
    expected = "4 12"  
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_list_sum() -> None:
    """Tests list_sum function."""
    ans = pet.list_sum([6, 7, 8, 10])
    expected = 31
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_list_sum2() -> None:
    """Tests list_sum function."""
    ans = pet.list_sum([2, 3, 4, 5])
    expected = 14
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 3: add a test case function to test list_sum function        #Fixed
def test_list_sum3() -> None:
    """Tests list_sum function."""
    ans = pet.list_sum([8, 4, 6, 10, 5])
    expected = 33
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 4: add a test case function to test list_sum function        #Fixed
def test_list_sum4() -> None:
    """Tests list_sum function."""
    ans = pet.list_sum([10, 20, 30])
    expected = 60
    assert ans == expected, f"Expected: {expected}, but got: {ans}"