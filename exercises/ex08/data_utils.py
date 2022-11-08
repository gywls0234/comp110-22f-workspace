"""Dictionary related utility functions."""

__author__ = "730617586"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a `list` of rows, each row represented as `dict[str, str]`."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding='utf8')

    cvs_reader = DictReader(file_handle)

    for row in cvs_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-orientaed table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_based_table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Produce a new column_based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in column_based_table:
        x: list[str] = []
        max: int = len(column_based_table[column])
        if number_of_rows < max: 
            for row in range(0, number_of_rows):
                x.append(column_based_table[column][row])
            result[column] = x   
        else:
            result = column_based_table
    return result


def select(column_based_table: dict[str, list[str]], name_of_columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for key in name_of_columns:
        result[key] = column_based_table[key]
    return result


def concat(data_1: dict[str, list[str]], data_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in data_1:
        result[key] = data_1[key]
    for key in data_2:
        if key in result:
            for item in data_2[key]:
                result[key].append(item)
        else: 
            result[key] = data_2[key]
    return result
   

def count(list_of_values: list[str]) -> dict[str, int]:
    """Counting the frequencies of valuea."""
    result: dict[str, int] = {}
    for item in list_of_values:
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result