"""EX07 - Dictionary."""

__author__ = "730617586"


def invert(dict: dict[str, str]) -> dict[str, str]:
    """Switch beginning and ending value using invert function."""
    new: dict[str, str] = {}
    
    for key in dict:
        if dict[key] in new:
            raise KeyError("Encounter more than one of the same key!")
        else:
            new[dict[key]] = key
    return new

    
def favorite_color(dict: dict[str, str]) -> str:
    """Find favorite color using favorite_color function."""
    new: dict[str, int] = {}

    for key in dict:
        if dict[key] in new: 
            new[dict[key]] += 1
        else:
            new[dict[key]] = 1

    max: int = 0
    biggest_color: str = ""

    for key in new:
        if max < new[key]:
            max = new[key]
            biggest_color = key
    return biggest_color


def count(x: list[str]) -> dict[str, int]:
    new: dict[str, int] = {}

    item: str = ""
    for item in x:
        if item in new: 
            new[item] += 1
        else:
            new[item] = 1
    return new