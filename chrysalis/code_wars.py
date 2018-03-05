#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Code Wars Exercises

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""


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


if __name__ == '__main__':
    pass
