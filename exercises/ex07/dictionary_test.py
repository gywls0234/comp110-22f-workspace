"""EX07 - Dictionary Tests."""

__author__ = "730617586"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_empty() -> None: 
    """Tests for the invert functions."""
    x = {} 
    assert invert(dict[x]) == {}


def test_invert_two_unit_cases_1() -> None: 
    """Tests for the invert functions."""
    x = {'a': 'z', 'b' : 'y', 'c': 'x'}
    assert invert(dict[x]) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_two_unit_cases_2() -> None: 
    """Tests for the invert functions."""
    x = {'apple': 'cat'}
    assert invert(dict[x]) == {'cat': 'apple'}


with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color_empty() -> None: 
    """Tests for the favorite_color functions."""
    x = {} 
    assert favorite_color(dict[x]) == {}


def test_favorite_color_two_unit_cases_1() -> None: 
    """Tests for the favorite_color functions."""
    x = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"} 
    assert favorite_color(dict[x]) == {"blue"}
 

def test_favorite_color_two_unit_cases_2() -> None: 
    """Tests for the favorite_color functions."""
    x = {"Marc": "red", "Ezri": "orange", "Kris": "blue"} 
    assert favorite_color(dict[x]) == {}
 

def test_count_empty() -> None: 
    """Tests for the count functions."""
    x = [] 
    assert count(x) == {}


def test_count_two_unit_cases_1() -> None: 
    """Tests for the count functions."""
    x: list[str] = ["orange", "apple", "banana", "orange"] 
    assert count(x) == {"orange": 2, "apple": 1, "banana": 1}


def test_count_two_unit_cases_2() -> None: 
    """Tests for the count functions."""
    x = list[str] = ["student", "professor", "homework", "test"] 
    assert count(x) == {"student": 1, "professor": 1, "homework": 1, "test": 1}