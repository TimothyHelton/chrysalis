#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Code Wars Exercises

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""
from typing import List


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


if __name__ == '__main__':
    pass
