"""Test cases for simonsays.py
"""

import simonsays


def test_valid_command():
    """Test valid_command function.
    """
    ans = simonsays.valid_command("Simon says do this")
    expected = True
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_valid_command2():
    """Test valid_command function."""
    ans = simonsays.valid_command("do this")
    expected = False
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 7: add a new test case function to test valid_command function          *Fixed*

def test_valid_command_empty():
    """Test valid_command with an empty string."""
    ans = simonsays.valid_command("")
    expected = False  
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 8: add a new test case function to test valid_command function              *Fixed*

def test_valid_command3():
    """Test valid_command function."""
    ans = simonsays.valid_command("Simon says")
    expected = True  
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

def test_answer():
    """Test answer function.
    """
    ans = simonsays.answer("Simon says do this")
    expected = "do this"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 9: add a new test case function to test answer function                 *Fixed*

def test_answer_no_simon_says():
    """Test answer function.
    """
    ans = simonsays.answer("do this")
    expected = None  
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


# FIXME 10: add a new test case function to test answer function              *Fixed*

def test_answer_sorta_simon_says():
    """Test answer function with something similar to Simon says 'do this'."""
    ans = simonsays.answer("Simon says go")
    expected = "go"  
    assert ans == expected, f"Expected: {expected}, but got: {ans}"