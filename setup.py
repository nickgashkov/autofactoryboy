#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from setuptools import setup, find_packages


def get_version():
    return __import__("__version__").__version__


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
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Testing",
    ],
    description="AutoFactoryBoy generates factories for you.",
    install_requires=install_requires,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords="autofactory",
    name="autofactory",
    packages=find_packages(include=["autofactory"]),
    url="https://github.com/nickgashkov/autofactoryboy",
    version=get_version(),
    zip_safe=False,
)
