#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from selectmenu import __author__, __version__

with open("README.rst", "r") as fp:
    long_description = fp.read()

setup(
    name="SelectMenu",
    author=__author__,
    author_email="takemehighermore@gmail.com",
    description=(
        "SelectMenu is the input form to choose from menu by arrow keys."),
    long_description=long_description,
    version=__version__,
    license="MIT License",
    url="https://github.com/alice1017/SelectMenu",
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
