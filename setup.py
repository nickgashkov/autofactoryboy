#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

install_requires = [
    "factory_boy>=2.11.0"
]

setup(
    author="Nick Gashkov",
    author_email="nick@gashkov.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="AutoFactoryBoy generates factories for you.",
    install_requires=install_requires,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords="autofactory",
    name="autofactory",
    packages=find_packages(include=["autofactory"]),
    url="https://github.com/nickgashkov/autofactory",
    version="0.1.0",
    zip_safe=False,
)
