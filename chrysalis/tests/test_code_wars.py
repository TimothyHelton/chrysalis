#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for Complementary DNA Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""
import pytest

from .. import code_wars


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
