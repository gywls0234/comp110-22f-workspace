"""EX05 - `list` Utility Functions"""

__author__ = "730617586"


"""Tests for the only_evens function."""

from exercises.ex05.utils import only_evens

def test_only_evens_empty() -> None: 
    x: list[int] = []
    assert only_evens(x) == []

def test_only_evens_two_unit_cases_1() -> None:
    x: list[int] = [0, 8, 11]
    assert only_evens(x) == [0, 8]

def test_only_evens_two_unit_cases_2() -> None:
    x: list[int] = [1, 9, 11]
    assert only_evens(x) == []


"""Tests for the concat function."""

from exercises.ex05.utils import concat

def test_concat_empty() -> None:
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []

def test_concat_two_unit_case_1() -> None:
    x: list[int] = [1, 2, 3]
    y: list[int] = [3, 2, 1]
    assert concat(x, y) == [1, 2, 3, 3, 2, 1]

def test_concat_two_unit_case_2() -> None:
    x: list[int] = []
    y: list[int] = [4, 8, 7]
    assert concat(x, y) == [4, 8, 7]


"""Tests for the sub function."""

from exercises.ex05.utils import sub

def test_sub_empty() -> None: 
    a_list: list[int] = []
    start_index: int = []
    end_index: int = []
    assert sub(a_list, start_index, end_index) == []

def test_sub_two_unit_case_1() -> None: 
    a_list: list[int] = [0, 20, 15, 47]
    start_index: int = 0
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == [0, 20, 15]

def test_sub_two_unit_case_2() -> None: 
    a_list: list[int] = [0, 0, 0, 0]
    start_index: int = 0
    end_index: int = 0
    assert sub(a_list, start_index, end_index) == []