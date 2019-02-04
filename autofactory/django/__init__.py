# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

try:
    import django
except ImportError as e:
    raise ImportError(
        "Couldn't import Django. AutoFactoryBoy x Django won't work if "
        "Django is not installed."
    )

from autofactory.django.shortcuts import autofactory
from autofactory.django.factory import DjangoModelAutoFactory

__all__ = (
    "autofactory",
    "DjangoModelAutoFactory",
)
