#!/usr/bin/python3
""" Find_peak """


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    """
    length = len(list_of_integers)

    if length == 0:
        return None

    if length == 1:
        return list_of_integers[0]

    for i in range(1, length):
        if list_of_integers[i] > list_of_integers[i-1]:
            # Check if the current element is greater than its neighbors
            if i == length - 1 or list_of_integers[i] > list_of_integers[i+1]:
                return list_of_integers[i]

    # If no peak is found, return the last element as a peak
    return list_of_integers[length - 1]
