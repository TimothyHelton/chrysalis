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


# Test count_vowels()
count_vowels = {
    'All Vowels': ('aeiou', 5),
    'White Space': ('a e  i   o    u', 5),
    'None': ('bcd', 0),
    'Mixed Case': ('An Example: story', 5),
}


@pytest.mark.parametrize('phrase, expected',
                         list(count_vowels.values()),
                         ids=list(count_vowels.keys()))
def test_count_vowels(phrase, expected):
    assert code_wars.count_vowels(phrase) == expected


# Test is_pangram()
is_pangram = {
    'Not Pangram': ('abc', False),
    'Pangram': ('The quick, brown fox jumps over the lazy dog!', True),
    'Numbers': ('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ', True),
}


@pytest.mark.parametrize('text, expected',
                         list(is_pangram.values()),
                         ids=list(is_pangram.keys()))
def test_is_pangram(text, expected):
    assert code_wars.is_pangram(text) == expected


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


# Test rectangle_to_squares()
rectangle_to_squares = {
    'square_input': (5, 5, None),
    'long': (5, 3, [3, 2, 1, 1]),
    'tall': (3, 5, [3, 2, 1, 1]),
    'even': (20, 14, [14, 6, 6, 2, 2, 2]),
}


@pytest.mark.parametrize('length, width, expected',
                         list(rectangle_to_squares.values()),
                         ids=list(rectangle_to_squares.keys()))
def test_rectangle_to_squares(length, width, expected):
    print(code_wars.rectangle_to_squares(length, width))
    assert code_wars.rectangle_to_squares(length, width) == expected


# Test sort_odd()
sort_odd = {
    'empty': ([], []),
    'example': ([5, 3, 2, 8, 1, 4], [1, 3, 2, 8, 5, 4]),
}


# Test .replace_zero()
replace_zero = {
    '0, 1': ([0, 1], 0),
    '1, 0': ([1, 0], 1),
    '0, 0, 1': ([0, 0, 1], 1),
    '1, 0, 0': ([1, 0, 0], 1),
    '1, 0, 1, 0': ([1, 0, 1, 0], 1),
    '0, 1, 0, 1, 0': ([0, 1, 0, 1, 0], 2),
    '0, 0, 1, 0, 0': ([0, 0, 1, 0, 0], 3),
    '1, 1, 0, 1, 1, 0, 1, 1': ([1, 1, 0, 1, 1, 0, 1, 1], 5),
    '1, 1, 1, 0, 1, 1, 0, 1, 1, 1': ([1, 1, 1, 0, 1, 1, 0, 1, 1, 1], 6),
    '0, 1, 1, 1, 1, 1, 0': ([0, 1, 1, 1, 1, 1, 0], 6),
    '1, 0, 0, 0, 1': ([1, 0, 0, 0, 1], 3),
    '1, 0, 1, 0, 1, 1, 1, 1': ([1, 0, 1, 0, 1, 1, 1, 1], 3),
}


@pytest.mark.parametrize('array, expected',
                         list(replace_zero.values()),
                         ids=list(replace_zero.keys()))
def test_replace_zero(array, expected):
    assert code_wars.replace_zero(array) == expected


@pytest.mark.parametrize('values, expected',
                         list(sort_odd.values()),
                         ids=list(sort_odd.keys()))
def test_sort_odd(values, expected):
    assert code_wars.sort_odd(values) == expected


if __name__ == '__main__':
    pass
