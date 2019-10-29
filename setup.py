#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import os
import re

from setuptools import setup, find_packages


def get_version():
    py = open(os.path.join("autofactory", "__init__.py")).read()
    py_version = re.search("__version__ = ['\"]([^'\"]+)['\"]", py).group(1)

    return py_version


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
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Testing",
    ],
    description="AutoFactoryBoy generates factories for you.",
    install_requires=install_requires,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="autofactory",
    name="autofactory",
    packages=find_packages(exclude=["tests", "tests.*"]),
    url="https://github.com/nickgashkov/autofactoryboy",
    version=get_version(),
    zip_safe=False,
)
