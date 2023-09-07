"""
Homework 4: Number Magic Tests    
=======================
Course:   CS 5001
Semester: UPDATE
Student:  UPDATE


Tests A series of functions that deal with number manipulation and string concatenation 
"""
from number_magic import number_string, evens, odds



def check(actual: str, expected: str) -> int:
    """checks for error, returns 1 if error exists, 0 if it doesn't

    Args:
        actual (str): actual value
        expected (str): expected value
    """
    if actual != expected:
        print(f"Actual: {actual} does not equal Expected: {expected}")
        return 1
    return 0


def test_number_string() -> int:
    """
    tests number_magic.number_string

    Returns:
        int: the number of tests **failed**
    """
    fail = 0
    fail += check(number_string(), "0,2,4,6,8,10")
    fail += check(number_string(2, 9), "0,2,4,6,8")
    fail += check(number_string(3, 9), "0,3,6,9")
    fail += check(number_string(4, 16), "0,4,8,12,16")
    ## May want to add more tests here
    return fail


def test_evens() -> int:
    """checks number_magic.evens

    Returns:
        int: the total number of errors
    """
    fail = 0
    fail += check(evens(), "0,2,4,6,8,10")
    fail += check(evens(max=17), "0,2,4,6,8,10,12,14,16")

    return fail


# Add test_odds

def main() -> None:
    fail = 0
    #fail += test_number_string()
    #fail += test_evens()
    # don't forget to update this

    print(f"Failed {fail} tests.")


if __name__ == "__main__":
    main()