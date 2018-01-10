"""
Run:
    python -m doctest -v stats.py
"""

from collections import defaultdict


def add(num1, num2):
    """Add two numbers
    Arguments:
        num1: int
        num2: int
    Returns:
        The sum
    Doctests:
        >>> add(3,4)
        7
    """
    return num1 + num2


def volume(length, width, height):
    """Finds the volume of cube
    Arguments:
        length: number
        width: number
        height: number
    Returns:
        The volume
    Doctests:
        >>> volume(3,4,5)
        60
    """
    return length * width * height


def mean(numbers):
    """Finds the mean
    Arguments:
        numbers: list of numbers
    Returns:
        The average
    Doctests:
        >>> mean([3,4,5])
        4.0
    """
    return sum(numbers) / len(numbers)


def median(numbers):
    """
    Computes the median of a list of numbers.
    Arguments:
        numbers: list of numbers
    Returns:
        The median
    Doctests:
        >>> median([2,1,6])
        2
        >>> median([3,5,4,9])
        4.5
    """
    numbers = sorted(numbers)
    middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return sum(numbers[middle - 1:middle + 1]) / 2  # even list
    return numbers[middle]                              # odd list


def mode(numbers):
    """Find the most common value in the list
    Arguments:
        numbers: list of numbers
    Returns:
        The mode
    Doctests:
        >>> mode([1,2,2,2,3,3,4])
        2
    """
    counts = defaultdict(int)
    for num in numbers:
        counts[num] += 1
    return sorted(counts, key=lambda k: counts[k])[-1]


def variance(numbers, ddof):
    return sum([(num - mean(numbers)) ** 2 for num in numbers]) / (len(numbers) - ddof)


def stdev(numbers, ddof):
    return variance(numbers, ddof) ** 0.5