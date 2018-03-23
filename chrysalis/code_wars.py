#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Code Wars Exercises

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""
import string
from typing import List, Union


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


if __name__ == '__main__':
    pass
