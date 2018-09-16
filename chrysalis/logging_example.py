#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Example of proper use of Logging

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""
import logging


def format_logger() -> logging.Logger:
    """Format the logger."""
    log_format = ('%(asctime)s  %(levelname)8s  -> %(name)s <- '
                  '(line: %(lineno)d) %(message)s\n')
    date_format = '%m/%d/%Y %I:%M:%S'
    logging.basicConfig(format=log_format, datefmt=date_format,
                        level=logging.INFO)
    return logging.getLogger(__name__)


if __name__ == '__main__':
    logger = format_logger()
    logger.setLevel(logging.INFO)

    name = 'Tim'
    logger.info(f'This is a log statement with a variable: {name}')
