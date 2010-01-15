#!/usr/bin/env python

from setuptools import setup
setup(
name = 'iencode-ng',
version='0.5.1',
author='tuxtof',
author_email='dev@geo6.net',
description='iPhone video encoding tools.',
url='http://github.com/tuxtof/iencode-ng',
license='GPLv2',

long_description="""iencode-ng is the evolution of iencode , a set of scripts to ease encoding of movies and series for iPhone/iPod Touch.""",

py_modules = ['iencode'],

entry_points = {
    'console_scripts': [
        'iencode = iencode:main',
    ],
},

)
