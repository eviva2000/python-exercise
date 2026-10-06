"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def _contains(big, small):
    if not small:
        return True
    return any(
        big[i:i + len(small)] == small
        for i in range(len(big) - len(small) + 1)
    )


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if _contains(list_two, list_one):
        return SUBLIST
    if _contains(list_one, list_two):
        return SUPERLIST
    return UNEQUAL
