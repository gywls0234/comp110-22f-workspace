"""EX04 - utils."""

__author__ = "730617586"


def all(x: list[int], y: int) -> bool:
    """Check whether ints in the list is same as int given or not."""
    index: int = 0
    
    if len(x) == 0:
        return False

    while index < len(x):
        if x[index] != y:
            return (False)
        index = index + 1 
    return True


def max(input: list[int]) -> int:
    """Find largest number in the list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    index: int = 0
    high_score = -99999999999999999

    while index < len(input):
        if input[index] > high_score:
            high_score = input[index]
        index = index + 1
    return high_score


def is_equal(x: list[int], y: list[int]) -> bool:
    """Check whether two list of integers are same each other or not."""
    if len(x) != len(y): 
        return False 
    index: int = 0
    while index < len(x): 
        if x[index] != y[index]:
            return False
        index = index + 1 
    return True 