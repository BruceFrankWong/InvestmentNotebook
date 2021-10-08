# -*- coding: utf-8 -*-

__author__ = 'Bruce Frank Wong'


import os
from pathlib import Path


PACKAGE_PATH: Path = Path(os.path.abspath(''))
DATA_PATH: Path = PACKAGE_PATH.joinpath('data')
