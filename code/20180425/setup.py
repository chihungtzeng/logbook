"""
An example for python to call C functions.
The example is from https://docs.python.org/3/extending/extending.html.

Tested in Python 3.6.
Simply run
    python setup.py build
"""
from distutils.core import setup, Extension

module1 = Extension('spam',
                    sources = ['spam.c'])

setup (name = 'SpamPackageName',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
