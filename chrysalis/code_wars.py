#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Code Wars Exercises

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""
from collections import defaultdict
from itertools import chain, zip_longest
from operator import add
import string
from typing import Dict, List, Union

import numpy as np


def alternate_sort(values: list) -> list:
    """Sort items by absolute value and return alternating negative positive.

    :param values: items to be sorted
    :return: sorted values
    """
    values = sorted(values, key=abs)
    pos = [x for x in values if x >= 0]
    neg = [x for x in values if x < 0]
    return [x for x in chain(*zip_longest(neg, pos)) if x is not None]


def check_square(n: int) -> bool:
    """Check if a number is a perfect square.

    :param n: number
    :return: True if number is square
    """
    return n > 0 and (n**0.5).is_integer()


def complementary_dna(dna: str) -> str:
    """Calculate complement DNA sequence.

    A <-> T
    C <-> G
    :param dna: initial DNA string
    :return: complement DNA string
    """
    dna = dna.upper()
    valid_input = 'ATCG'
    if set(dna).difference(valid_input):
        raise ValueError('Only "A", "T", "C", and "G" are valid inputs')
    table = str.maketrans('ATCG', 'TAGC')

    return dna.translate(table)


def count_vowels(phrase: str) -> int:
    """Count the number of vowels in the phrase.

    :param phrase: text to be examined
    :return: number of vowels in phrase
    """
    return len([x for x in phrase.lower() if x in 'aeiou'])


def interest_calc(yearly_deposit: int, goal: int) -> Dict[int, int]:
    """Calculate years to achieve financial goal for return rates between 1-6%.

    :param yearly_deposit: annual contribution to account
    :param goal: minimum desired end dollar value of account
    :return: years required to achieve goal assuming interest rates 1-6%.
    """
    forecast = defaultdict(int)
    for int_rate in range(1, 7):
        balance = 0
        year = 0
        while balance < goal:
            year += 1
            balance = (balance + yearly_deposit) * (1 + int_rate / 100)
            forecast[int_rate] = year

    return forecast


def matrix_add(*arrays: List[List[int]]) -> List[List[int]]:
    """
    Elementwise summation of arrays.

    :type arrays: arrays to be combined
    :return: summation array
    """
    return [list(map(add, *x)) for x in zip(*arrays)]


def is_pangram(text: str) -> bool:
    """Determine if text is a pangram.

    ..note:: A pangram is a string that contains every single letter of the \
        alphabet at least once (case is irrelevant).
    :param text: text to evaluate
    :return: True if text is a pangram
    """
    return set(string.ascii_lowercase) <= set(text.lower())


def pet_age(years: int) -> List[int]:
    """Calculate pet age for dogs and cats.

    ..note:: years argument must be greater than or equal to 1
    :param years: human years
    :return: [human_age, cat_age, dog_age]
    """
    def adult_age(multiplier: int) -> int:
        """Total age of pet if years is greater than two.

        :param multiplier: age multiplier (cat=4, dog=5)
        :return: pet age
        """
        return 24 + (years - 2) * multiplier

    if years < 1:
        raise ValueError('years must be greater than or equal to 1')

    return [years, adult_age(4), adult_age(5)] if years > 1 else [years, 15, 15]


def rectangle_to_squares(length: int, width: int,
                         squares: Union[None, list]=None) -> Union[None, list]:
    """Calculate the number of squares in a rectangle.

    ..note:: if given inputs for a square the output will be None
    :param length: rectangle length
    :param width: rectangle width
    :param squares: previous list of squares
    :return: sizes of squares contained in rectangle
    """
    if squares is None:
        squares = []
    if length == width and not squares:
        return None

    length, width = sorted([length, width], reverse=True)
    squares.append(width)
    new_length = length - width
    if new_length > 0:
        rectangle_to_squares(new_length, width, squares)

    return squares


def replace_zero(array: iter) -> int:
    """Find index to maximize number of consecutive ones in array.

    ..note:: If there is a tie for length of consecutive numbers the last \
        index will be returned.
    :param array: sequence of ones and zeros
    :return: index of zero to replace maximizing the length of ones
    """
    zeros = [n for n, v in enumerate(array) if v == 0]
    if len(zeros) == 1:
        return zeros[0]
    begin = zeros[1]
    end = len(array) - zeros[-2] - 1
    z = [0] + zeros + [len(array) - 1]
    counts = [z[n + 2] - z[n] - 1 for n in range(len(z) - 2)]
    counts[0] = begin
    counts[-1] = end

    return zeros[max([n for n, v in enumerate(counts) if v == max(counts)])]


def sort_odd(values: iter) -> iter:
    """Return array with odd values sorted in ascending order.

    :param values: array of integer values
    :return: sorted array
    """
    arr = np.array(values)
    odds = np.sort(arr[arr % 2 != 0])
    arr[np.isin(arr, odds)] = odds
    return arr.tolist()


if __name__ == '__main__':
    pass
