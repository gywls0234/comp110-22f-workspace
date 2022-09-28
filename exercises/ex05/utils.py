"""EX05 - `list` Utility Functions"""

__author__ = "730617586"


def only_evens(x: list[int]) -> list[int]:
    "Give even numbers in a list of integers."
    index: int = 0
    empty_list = []

    while index < len(x):
        if x[index] % 2 == 0:
            empty_list.append(x[index])
        index = index + 1
    return empty_list

    
def concat(x: list[int], y: list[int]) -> list[int]:
    "New list containing first list and following by second list of integers."
    empty_list = []
    index: int = 0

    while index < len(x):
        empty_list.append(x[index])
        index = index + 1
    
    index = 0
    while index < len(y):
        empty_list.append(y[index])
        index = index + 1
    return empty_list

    
def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Using Sub function, find subset of the given list, between start index and end index -1."""
    output_list: list[int] = []
    index: int = start_index
    while index < end_index:
        output_list.append(a_list[index])
        index = index + 1
    return output_list