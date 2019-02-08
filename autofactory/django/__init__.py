# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from autofactory.django.factories import DjangoModelAutoFactory
from autofactory.django.shortcuts import autofactory

try:
    pass
except ImportError as e:
    raise ImportError(
        "Couldn't import Django. AutoFactoryBoy x Django won't work if "
        "Django is not installed."
    )


__all__ = (
    "autofactory",
    "DjangoModelAutoFactory",
)
