#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Image Utilities

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""
from itertools import product
from typing import Iterator, Tuple


def tile(start: Tuple[int], end: Tuple[int], tile_size: int,
         overlap: int=0) -> Iterator[Tuple[int]]:
    """
    Tile rectangle with overlapping chips without padded boarder.

    :param start: first column, first row
    :param end: last column, last row
    :param tile_size: size of square chip
    :param overlap: length of chip overlap
    :return: coordinates of next chip \
        (min column, min row, max column, max row)
    """
    def boundary(first_val: int, next_val: int, max_val: int) -> tuple:
        """
        Determine tile boundary conditions.

        :param first_val: first value
        :param next_val: proposed next value
        :param max_val: maximum value
        :return: first and second coordinates of the new tile
        """
        v0 = first_val
        if next_val <= max_val:
            v1 = next_val
        else:
            v0 = max_val - tile_size
            v1 = next_val

        return v0, v1

    c_min = start[0]
    c_max = end[0]
    r_min = start[1]
    r_max = end[0]

    grid = product(range(c_min, c_max, tile_size - overlap),
                   range(r_min, r_max, tile_size - overlap))

    for c, r in grid:
        c_next, r_next = (n + tile_size for n in (c, r))
        c, c_end = boundary(c, c_next, c_max)
        r, r_end = boundary(r, r_next, r_max)
        yield c, r, c_end, r_end


if __name__ == '__main__':
    pass
