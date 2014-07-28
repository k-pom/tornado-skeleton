#!/usr/bin/env python
# -*- coding: utf8 -*-
"""Setup script for tornado-skeleton"""
from viper import __version__

from setuptools import find_packages, setup

with open("README.rst") as f:
    readme = f.read()

with open("requirements.txt") as f:
    requires = f.read()

setup(
    name='tornado-skeleton',
    description='Tornado Skeleton Framework',
    install_requires=requires,
    license=',
    long_description=readme,
    version=1.0,
)
