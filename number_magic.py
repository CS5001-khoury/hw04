"""
Homework 4: Number Magic    
=======================
Course:   CS 5001
Semester: UPDATE
Student:  UPDATE


A series of functions that deal with number manipulation and string concatenation 
"""


def evens(max: int = 10) -> str:
    """Returns an even number only string separated by commas

    Examples:
        >>> evens()
        '0,2,4,6,8,10'
        >>> evens(max=17)
        '0,2,4,6,8,10,12,14,16'

    Args:
        max (int, optional): the max number in the sequence. Defaults to 10.

    Returns:
        str: returns even numbers up to max separated by commas
    """
    pass  # remove and replace with your code


def odds(max: int = 10) -> str:
    """Returns an odd number only string separated by commas

    Examples:
        >>> odds()
        '1,3,5,7,9'
        >>> odds(15)
        '1,3,5,7,9,11,13,15'

    Args:
        max (int, optional): the max number in the sequence. Defaults to 10.

    Returns:
        str: returns even numbers up to max separated by commas
    """
    pass # remove and replace with your code


def number_string(number: int = 2, max: int = 10, 
                  invert: bool = False, delim: str = ",") -> str:
    """
    generate a number string with commas between each number
    only showing the numbers divisible by a set number. Adding invert = True
    prints out the inverted set of numbers.

    Examples:
        >>> number_string()
        '0,2,4,6,8,10'
        >>> number_string(3, 9)
        '0,3,6,9'
        >>> number_string(invert=True)
        '1,3,5,7,9'
        >>> number_string(2, 15, True)
        '1,3,5,7,9,11,13,15'
        >>> number_string(2, 15, True, ' ')
        '1 3 5 7 9 11 13 15'

    Args:
        number (int, optional): the divisor. Defaults to 2.
        max (int, optional): the max number in the sequence. Defaults to 10.
        invert (bool, optional): whether to print out the 
            divisor set or inverted set. Defaults to False
        delim (str, optional): deliminator to put between numbers. 
            Defaults to ','

    Returns:
        str: a comma separated value string of numbers
    """
    pass # remove and replace with your code