#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from selectmenu import __author__, __version__

setup(
    name="SelectMenu",
    author=__author__,
    description=(
        "SelectMenu is the input form to choose from menu by arrow keys."),
    version=__version__,
    license="MIT License",
    packages=find_packages(),
    install_requires=["prompt-toolkit==1.0.15"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ]
)
