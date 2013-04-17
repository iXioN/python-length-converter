#!/usr/bin/env python
#  setup.py
#  python-length-converter
#  
#  Created by Antonin Lacombe on 2013-04-18.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__="0.0.1"

setup(
    name="python-length-converter",
    version=__version__,
    license='LGPLv3',
    description='A simple length unit converter',
    author='Antonin Lacombe',
    author_email='antonin.lacombe@gmail.com',
    url='https://github.com/iXioN/python-length-converter.git',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
      ],
)