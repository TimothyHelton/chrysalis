#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Config Parser Example

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>

The config_file would have keys followed by values.


[pgadmin]
PGADMIN_DEFAULT_EMAIL = enter_user@testpkg.com
PGADMIN_DEFAULT_PASSWORD = enter_password

[postgres]
POSTGRES_HOST = chrysalis_postgres
POSTGRES_USER = enter_user
POSTGRES_PASSWORD = enter_password
"""
import logging
from configparser import ConfigParser
import os


logger = logging.getLogger(__name__)

parser = ConfigParser()
parser.read('config_file')
try:
    for key in parser['postgres']:
        os.environ[key.upper()] = parser.get('postgres', key)
except KeyError:
    logger.warning(
        '''
        The following required system variables must be defined:
            POSTGRES_HOST
            POSTGRES_USER
            POSTGRES_PASSWORD
        '''
    )


if __name__ == '__main__':
    pass
