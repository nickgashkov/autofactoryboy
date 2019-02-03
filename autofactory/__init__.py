# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from autofactory.django.factory import DjangoModelAutoFactory
from autofactory.shortcuts import autofactory

__author__ = "Nick Gashkov"
__email__ = "nick@gashkov.com"
__version__ = __import__("__version__").__version__

__all__ = (
    "DjangoModelAutoFactory",
    "autofactory",
)
