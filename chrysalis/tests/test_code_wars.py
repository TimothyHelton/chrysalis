#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for Complementary DNA Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""
import pytest

from .. import code_wars


# Test check_square()
check_square = {
    'Zero': (0, False),
    'Negative': (-4, False),
    'Positive': (16, True),
    'Large Number': (3413080033, False),
}


@pytest.mark.parametrize('n, expected',
                         list(check_square.values()),
                         ids=list(check_square.keys()))
def test_check_square(n, expected):
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


# Test pet_age()
pet_age = {
    'One Year': (1, [1, 15, 15]),
    'Two Year': (2, [2, 24, 24]),
    'Ten Year': (10, [10, 56, 64]),
}


@pytest.mark.parametrize('human_years, expected',
                         list(pet_age.values()),
                         ids=list(pet_age.keys()))
def test_pet_age(human_years, expected):
    assert code_wars.pet_age(human_years) == expected


def test_pet_age_exception():
    with pytest.raises(ValueError):
        code_wars.pet_age(-3)


if __name__ == '__main__':
    pass
