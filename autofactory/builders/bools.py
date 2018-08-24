# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from factory import Faker


def build_booleanfield(field_cls):
    return Faker('pybool')


def build_nullbooleanfield(field_cls):
    # TODO: Implement ~ pybool or ``None``.
    return Faker('pybool')
