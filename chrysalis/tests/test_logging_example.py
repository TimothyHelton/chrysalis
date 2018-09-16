#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for Complementary DNA Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""
import logging

from .. import logging_example


def test_format_logger(caplog):
    with caplog.at_level(logging.DEBUG):
        logger = logging_example.format_logger()
        logger.debug('Debug')
        logger.info('Info')
        assert caplog.record_tuples == [
            ('chrysalis.logging_example', logging.DEBUG, 'Debug'),
            ('chrysalis.logging_example', logging.INFO, 'Info'),
        ]


if __name__ == '__main__':
    pass
