#!/usr/bin/env python

from setuptools import setup, find_packages

try:
    import multiprocessing
except ImportError:
    pass

dependencies = [
    # packages for which we want latest stable version
    "pep8>=1.5.6",
    "pylint>=1.2.1",
    "ipython>=2.0.0",
    "uwsgi>=2.0.4",
    # Flask and extensions
    "flask==0.10.1",
    "flask-assets==0.9",
    "flask-migrate==1.2.0",
    "flask-script==2.0.5",
    "flask-webtest==0.0.7",
    "flask-wtf==0.9.5"
    # Additional packages
]

setup(
    name="deaf_grandma",
    version="0.1dev",
    url="https://github.com/smithjason/deaf_grandma",
    packages=find_packages(),
    install_requires=dependencies
)
