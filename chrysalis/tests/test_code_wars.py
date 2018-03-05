#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for Complementary DNA Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""
import pytest

from .. import code_wars


# Test .check_square()
check_square = {
    'Zero': (0, False),
    'Negative': (-4, False),
    'Positive': (16, True),
    'Large Number': (3413080033, False),
}

@pytest.mark.parametrize('n, expected',
                         list(check_square.values()),
                         ids=list(check_square.keys()))
def test__check_square(n, expected):
    assert code_wars.check_square(n) == expected

    
# Test complementary_dna()
complementary_dna = {
    'All Letters': ('ATCG', 'TAGC'),
    'Single Letter': ('AAAA', 'TTTT'),
    'Sequential Repeat': ('ATTGC', 'TAACG'),
    'Multiple Letters': ('GTAT', 'CATA'),
    'Lowercase Letters': ('atcg', 'TAGC'),
}


@pytest.mark.parametrize('input_dna, expected',
                         list(complementary_dna.values()),
                         ids=list(complementary_dna.keys()))
def test_complementary_dna(input_dna, expected):
    assert code_wars.complementary_dna(input_dna) == expected


def test_complementary_dna_invalid_input():
    with pytest.raises(ValueError):
        code_wars.complementary_dna('b')


if __name__ == '__main__':
    pass
