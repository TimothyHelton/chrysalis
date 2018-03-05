#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from pkg_resources import get_distribution, DistributionNotFound
import os.path as osp
from . import code_wars

__version__ = '0.0.0'

try:
    _dist = get_distribution('chrysalis')
    dist_loc = osp.normcase(_dist.location)
    here = osp.normcase(__file__)
    if not here.startswith(osp.join(dist_loc, 'chrysalis')):
        raise DistributionNotFound
except DistributionNotFound:
    __version__ = 'Please install this project with setup.py'
else:
    __version__ = _dist.version
